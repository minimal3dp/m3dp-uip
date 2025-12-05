#!/usr/bin/env python3
"""
Download and organize 3D printing defect datasets for vision validation.

This script downloads datasets from multiple sources and organizes them into
the validation dataset structure expected by the VisionValidator service.

Usage:
    python scripts/download_validation_datasets.py [OPTIONS]

Options:
    --dataset {kaggle,roboflow_large,roboflow_small,all}  Which dataset to download
    --output PATH                                         Output directory (default: backend/validation_data)
    --skip-existing                                       Skip if dataset already exists
    --samples N                                           Only download N samples per defect type (for testing)

Examples:
    # Download all datasets
    python scripts/download_validation_datasets.py --dataset all

    # Download only Kaggle dataset
    python scripts/download_validation_datasets.py --dataset kaggle

    # Download 10 samples per defect for testing
    python scripts/download_validation_datasets.py --dataset all --samples 10
"""

import argparse
import json
import logging
import shutil
import sys
from pathlib import Path
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Dataset configurations
DATASETS = {
    "kaggle": {
        "name": "FDM 3D Printing Defect Dataset",
        "source": "Kaggle",
        "url": "wengmhu/fdm-3d-printing-defect-dataset",
        "license": "MIT",
        "image_count": 1912,
        "defect_mapping": {
            "Cracking": "Layer_Separation",  # Map to our taxonomy
            "Layer_shifting": "Layer_Shift",
            "Off_platform": None,  # Skip - not in our taxonomy
            "Stringing": "Stringing",
            "Warping": "Warping",
        },
    },
    "roboflow_large": {
        "name": "3D Printing Defects (5.9k images)",
        "source": "Roboflow",
        "workspace": "abdelrahman-elkafas-yjn0j",
        "project": "3d-printing-defects-tlhcb",
        "version": 1,
        "license": "CC BY 4.0",
        "image_count": 5900,
        "defect_mapping": {
            "spaghetti": "Spaghetti",
            "stringing": "Stringing",
            "zits": "Extrusion_Issue",  # Zits are form of extrusion problem
        },
    },
    "roboflow_small": {
        "name": "3D Error Monitoring (588 images)",
        "source": "Roboflow",
        "workspace": "3d-defects",
        "project": "3d-error-monitoring2",
        "version": 7,
        "license": "CC BY 4.0",
        "image_count": 588,
        "defect_mapping": {
            "over_extrusion": "Extrusion_Issue",
            "spaghetti": "Spaghetti",
            "stringing": "Stringing",
            "under_extrusion": "Extrusion_Issue",
            "warping": "Warping",
            "zits": "Extrusion_Issue",
        },
    },
}


class DatasetDownloader:
    """Handles downloading and organizing defect datasets."""

    def __init__(self, output_dir: Path, skip_existing: bool = False, max_samples: int | None = None):
        """Initialize downloader.

        Args:
            output_dir: Base directory for validation data
            skip_existing: Skip download if dataset exists
            max_samples: Maximum samples per defect type (None = all)
        """
        self.output_dir = output_dir
        self.skip_existing = skip_existing
        self.max_samples = max_samples
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download_kaggle_dataset(self, config: dict[str, Any]) -> bool:
        """Download Kaggle FDM dataset.

        Args:
            config: Dataset configuration

        Returns:
            True if successful
        """
        logger.info(f"Downloading {config['name']}...")

        try:
            # Check if kaggle is installed
            try:
                import kaggle  # noqa: F401
            except ImportError:
                logger.error("Kaggle API not installed. Install with: pip install kaggle")
                logger.error("Also configure API key: https://www.kaggle.com/docs/api")
                return False

            # Download dataset
            dataset_slug = config["url"]
            download_path = self.output_dir / "temp_kaggle"
            download_path.mkdir(exist_ok=True)

            logger.info(f"Downloading from Kaggle: {dataset_slug}")
            from kaggle.api.kaggle_api_extended import KaggleApi

            api = KaggleApi()
            api.authenticate()
            api.dataset_download_files(dataset_slug, path=str(download_path), unzip=True)

            # Find the extracted directory
            extracted_dirs = list(download_path.glob("*"))
            if not extracted_dirs:
                logger.error("No files extracted from Kaggle dataset")
                return False

            # Organize by defect type
            defect_mapping = config["defect_mapping"]
            stats = {}

            for source_defect, target_defect in defect_mapping.items():
                if target_defect is None:
                    logger.info(f"Skipping {source_defect} (not in taxonomy)")
                    continue

                # Find source images
                source_images = list(download_path.rglob(f"{source_defect}/*.*"))
                if not source_images:
                    # Try different patterns
                    source_images = list(download_path.rglob(f"*{source_defect}*/*.*"))

                if self.max_samples:
                    source_images = source_images[: self.max_samples]

                # Create target directory
                target_dir = self.output_dir / target_defect.lower() / "images"
                target_dir.mkdir(parents=True, exist_ok=True)

                # Copy images
                copied = 0
                for img_path in source_images:
                    if img_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                        target_path = target_dir / f"kaggle_{img_path.name}"
                        shutil.copy2(img_path, target_path)
                        copied += 1

                stats[target_defect] = copied
                logger.info(f"  {target_defect}: {copied} images")

            # Create metadata
            self._create_metadata(config, stats)

            # Cleanup
            shutil.rmtree(download_path)

            logger.info(f"✓ Successfully downloaded {sum(stats.values())} images from Kaggle")
            return True

        except Exception as e:
            logger.error(f"Failed to download Kaggle dataset: {e}")
            return False

    def download_roboflow_dataset(self, config: dict[str, Any]) -> bool:
        """Download Roboflow dataset.

        Args:
            config: Dataset configuration

        Returns:
            True if successful
        """
        logger.info(f"Downloading {config['name']}...")

        try:
            # Check if roboflow is installed
            try:
                from roboflow import Roboflow
            except ImportError:
                logger.error("Roboflow API not installed. Install with: pip install roboflow")
                logger.info(
                    "Get API key from: https://app.roboflow.com/settings/api"
                )
                return False

            # Check for API key
            import os

            api_key = os.environ.get("ROBOFLOW_API_KEY")
            if not api_key:
                logger.error("ROBOFLOW_API_KEY not set in environment")
                logger.info("Export your API key: export ROBOFLOW_API_KEY=your_key_here")
                return False

            # Initialize Roboflow
            rf = Roboflow(api_key=api_key)
            workspace = rf.workspace(config["workspace"])
            project = workspace.project(config["project"])
            dataset = project.version(config["version"]).download("coco")

            # Organize by defect type
            download_path = Path(dataset.location)
            defect_mapping = config["defect_mapping"]
            stats = {}

            # Parse COCO annotations to get class labels
            annotations_file = download_path / "train" / "_annotations.coco.json"
            if annotations_file.exists():
                with open(annotations_file) as f:
                    coco_data = json.load(f)

                # Create class ID to name mapping
                class_map = {cat["id"]: cat["name"] for cat in coco_data["categories"]}

                # Group images by class
                image_classes = {}
                for ann in coco_data["annotations"]:
                    img_id = ann["image_id"]
                    class_name = class_map.get(ann["category_id"])
                    if img_id not in image_classes:
                        image_classes[img_id] = set()
                    if class_name:
                        image_classes[img_id].add(class_name)

                # Map image IDs to filenames
                img_id_to_file = {img["id"]: img["file_name"] for img in coco_data["images"]}

                # Organize images by defect type
                for source_defect, target_defect in defect_mapping.items():
                    if target_defect is None:
                        continue

                    target_dir = self.output_dir / target_defect.lower() / "images"
                    target_dir.mkdir(parents=True, exist_ok=True)

                    copied = 0
                    for img_id, classes in image_classes.items():
                        # Only use images with single class (avoid multi-defect confusion)
                        if len(classes) == 1 and source_defect in classes:
                            if self.max_samples and copied >= self.max_samples:
                                break

                            filename = img_id_to_file.get(img_id)
                            if filename:
                                source_path = download_path / "train" / filename
                                if source_path.exists():
                                    target_path = target_dir / f"roboflow_{config['project']}_{filename}"
                                    shutil.copy2(source_path, target_path)
                                    copied += 1

                    stats[target_defect] = copied
                    logger.info(f"  {target_defect}: {copied} images")

            else:
                logger.warning("COCO annotations not found, organizing by directory structure")

            # Create metadata
            self._create_metadata(config, stats)

            # Cleanup download
            shutil.rmtree(download_path)

            logger.info(f"✓ Successfully downloaded {sum(stats.values())} images from Roboflow")
            return True

        except Exception as e:
            logger.error(f"Failed to download Roboflow dataset: {e}")
            return False

    def _create_metadata(self, config: dict[str, Any], stats: dict[str, int]) -> None:
        """Create metadata files for downloaded datasets.

        Args:
            config: Dataset configuration
            stats: Statistics (defect_type -> image_count)
        """
        for defect_type, count in stats.items():
            if count == 0:
                continue

            metadata = {
                "defect_type": defect_type,
                "description": f"{defect_type} defect images from {config['source']}",
                "source": {
                    "name": config["name"],
                    "provider": config["source"],
                    "license": config["license"],
                    "url": config.get("url", f"{config.get('workspace')}/{config.get('project')}"),
                },
                "image_count": count,
                "validation_notes": f"Downloaded from {config['source']} - ready for validation",
            }

            defect_dir = self.output_dir / defect_type.lower()
            metadata_file = defect_dir / f"{config['source'].lower()}_metadata.json"
            metadata_file.parent.mkdir(parents=True, exist_ok=True)

            with open(metadata_file, "w") as f:
                json.dump(metadata, f, indent=2)

            logger.info(f"  Created metadata: {metadata_file.name}")


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Download 3D printing defect datasets for validation"
    )
    parser.add_argument(
        "--dataset",
        choices=["kaggle", "roboflow_large", "roboflow_small", "all"],
        default="all",
        help="Which dataset to download",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("backend/validation_data"),
        help="Output directory for validation data",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip download if dataset already exists",
    )
    parser.add_argument(
        "--samples",
        type=int,
        help="Maximum samples per defect type (for testing)",
    )

    args = parser.parse_args()

    # Print header
    logger.info("=" * 60)
    logger.info("3D Printing Defect Dataset Downloader")
    logger.info("=" * 60)
    logger.info(f"Output directory: {args.output}")
    logger.info(f"Max samples: {args.samples or 'All'}")
    logger.info("")

    # Initialize downloader
    downloader = DatasetDownloader(
        output_dir=args.output,
        skip_existing=args.skip_existing,
        max_samples=args.samples,
    )

    # Download datasets
    success_count = 0
    total_count = 0

    datasets_to_download = (
        [args.dataset] if args.dataset != "all" else ["kaggle", "roboflow_large", "roboflow_small"]
    )

    for dataset_key in datasets_to_download:
        config = DATASETS[dataset_key]
        total_count += 1

        logger.info("")
        logger.info("-" * 60)
        logger.info(f"Dataset: {config['name']}")
        logger.info(f"License: {config['license']}")
        logger.info(f"Expected images: ~{config['image_count']}")
        logger.info("-" * 60)

        try:
            if dataset_key == "kaggle":
                success = downloader.download_kaggle_dataset(config)
            else:
                success = downloader.download_roboflow_dataset(config)

            if success:
                success_count += 1
        except Exception as e:
            logger.error(f"Unexpected error: {e}")

    # Summary
    logger.info("")
    logger.info("=" * 60)
    logger.info("DOWNLOAD SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Successfully downloaded: {success_count}/{total_count} datasets")

    # List downloaded defect types
    defect_dirs = sorted(args.output.glob("*/"))
    if defect_dirs:
        logger.info("")
        logger.info("Downloaded defect types:")
        for defect_dir in defect_dirs:
            if defect_dir.is_dir():
                image_count = len(list((defect_dir / "images").glob("*.*")))
                logger.info(f"  • {defect_dir.name}: {image_count} images")

    logger.info("")
    logger.info("Next steps:")
    logger.info("  1. Review downloaded images for quality")
    logger.info("  2. Create per-image metadata files with ground truth labels")
    logger.info("  3. Run validation: python -m backend.scripts.validate_vision_model")

    return 0 if success_count == total_count else 1


if __name__ == "__main__":
    sys.exit(main())
