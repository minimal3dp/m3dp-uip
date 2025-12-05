#!/usr/bin/env python3
"""
Generate per-image metadata files for validation dataset.

This script creates metadata JSON files for each image in the validation dataset,
which are required by the VisionValidator service.

Usage:
    python scripts/generate_image_metadata.py [OPTIONS]

Examples:
    # Generate metadata for all images
    python scripts/generate_image_metadata.py

    # Generate for specific defect type
    python scripts/generate_image_metadata.py --defect stringing

    # Dry run (preview without creating files)
    python scripts/generate_image_metadata.py --dry-run
"""

import argparse
import json
import logging
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Default metadata templates by defect type
METADATA_TEMPLATES = {
    "spaghetti": {
        "severity": "severe",
        "visual_markers": [
            "complete print failure",
            "tangled filament",
            "no layer structure",
            "chaotic extrusion",
        ],
        "description_template": "Spaghetti failure with tangled filament",
    },
    "stringing": {
        "severity": "moderate",
        "visual_markers": [
            "thin threads between parts",
            "cobweb-like strands",
            "wispy filament",
            "fine strings during travel moves",
        ],
        "description_template": "Stringing visible between print features",
    },
    "warping": {
        "severity": "moderate",
        "visual_markers": [
            "corners lifting from bed",
            "edges curling upward",
            "base layer separation",
            "uneven bottom surface",
        ],
        "description_template": "Warping with lifted corners or curled edges",
    },
    "under_extrusion": {
        "severity": "moderate",
        "visual_markers": [
            "gaps in layers",
            "weak infill",
            "missing material",
            "thin walls",
            "visible gaps between perimeters",
        ],
        "description_template": "Under-extrusion showing gaps and weak structure",
    },
    "over_extrusion": {
        "severity": "moderate",
        "visual_markers": [
            "bulging surfaces",
            "blob artifacts",
            "excess material",
            "rough texture",
            "zits and surface defects",
        ],
        "description_template": "Over-extrusion with excess material and blobs",
    },
    "layer_shift": {
        "severity": "severe",
        "visual_markers": [
            "misaligned layers",
            "stepped appearance",
            "horizontal offset",
            "skipped steps visible",
        ],
        "description_template": "Layer shifting with visible misalignment",
    },
    "layer_separation": {
        "severity": "severe",
        "visual_markers": [
            "delamination between layers",
            "vertical cracks",
            "layers splitting apart",
            "poor layer adhesion",
        ],
        "description_template": "Layer separation showing delamination",
    },
    "ringing": {
        "severity": "moderate",
        "visual_markers": [
            "ripples on surface",
            "echo artifacts",
            "wave patterns after corners",
            "ghosting effect",
        ],
        "description_template": "Ringing artifacts visible on flat surfaces",
    },
    "poor_bridging": {
        "severity": "moderate",
        "visual_markers": [
            "sagging bridges",
            "drooping overhangs",
            "failed horizontal spans",
            "stringy bridge surface",
        ],
        "description_template": "Poor bridging with sagging or drooping",
    },
}


def generate_metadata_for_image(
    image_path: Path,  # noqa: ARG001
    defect_type: str,
    source: str,
    template: dict,
) -> dict:
    """Generate metadata for a single image.

    Args:
        image_path: Path to image file (reserved for future use)
        defect_type: Defect type classification
        source: Source of image (kaggle, roboflow, etc.)
        template: Metadata template with defaults

    Returns:
        Metadata dictionary
    """
    # Normalize defect type name
    defect_type_title = defect_type.replace("_", " ").title().replace(" ", "_")

    metadata = {
        "defect_type": defect_type_title,
        "severity": template.get("severity", "moderate"),
        "source": source,
        "source_url": None,  # TODO: Can be filled in manually if needed
        "printer_type": "FDM",  # Default, can be overridden
        "material": "Unknown",  # Can be filled in manually
        "expected_classification": defect_type_title,
        "visual_markers": template.get("visual_markers", []),
        "notes": f"{template.get('description_template', 'Defect image')} - Auto-generated metadata",
    }

    return metadata


def generate_metadata_for_defect(
    defect_dir: Path,
    dry_run: bool = False,
    overwrite: bool = False,
) -> tuple[int, int]:
    """Generate metadata files for all images in a defect directory.

    Args:
        defect_dir: Path to defect type directory
        dry_run: If True, don't create files
        overwrite: If True, overwrite existing metadata

    Returns:
        Tuple of (created_count, skipped_count)
    """
    defect_type = defect_dir.name
    images_dir = defect_dir / "images"

    if not images_dir.exists():
        logger.warning(f"No images directory found in {defect_dir}")
        return 0, 0

    # Get template for this defect type
    template = METADATA_TEMPLATES.get(
        defect_type,
        {
            "severity": "moderate",
            "visual_markers": [],
            "description_template": f"{defect_type} defect",
        },
    )

    # Find all images
    image_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    images = [img for img in images_dir.iterdir() if img.suffix.lower() in image_extensions]

    if not images:
        logger.warning(f"No images found in {images_dir}")
        return 0, 0

    created_count = 0
    skipped_count = 0

    for image_path in images:
        # Determine metadata path (same name with _metadata.json suffix)
        metadata_path = images_dir / f"{image_path.stem}_metadata.json"

        # Check if metadata already exists
        if metadata_path.exists() and not overwrite:
            skipped_count += 1
            continue

        # Determine source from filename
        source = "unknown"
        if "kaggle" in image_path.name:
            source = "kaggle"
        elif "roboflow" in image_path.name:
            source = "roboflow"

        # Generate metadata
        metadata = generate_metadata_for_image(
            image_path=image_path,
            defect_type=defect_type,
            source=source,
            template=template,
        )

        if dry_run:
            logger.info(f"Would create: {metadata_path.name}")
            created_count += 1
        else:
            # Write metadata file
            with open(metadata_path, "w") as f:
                json.dump(metadata, f, indent=2)
            logger.debug(f"Created: {metadata_path.name}")
            created_count += 1

    return created_count, skipped_count


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate per-image metadata for validation dataset"
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("backend/validation_data"),
        help="Path to validation dataset directory",
    )
    parser.add_argument(
        "--defect",
        type=str,
        help="Only generate metadata for specific defect type",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be created without creating files",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing metadata files",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Print header
    logger.info("=" * 60)
    logger.info("Validation Dataset Metadata Generator")
    logger.info("=" * 60)
    logger.info(f"Dataset: {args.dataset}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Overwrite: {args.overwrite}")
    logger.info("")

    # Check dataset directory exists
    if not args.dataset.exists():
        logger.error(f"Dataset directory not found: {args.dataset}")
        return 1

    # Find defect directories
    if args.defect:
        defect_dirs = [args.dataset / args.defect]
    else:
        defect_dirs = [d for d in args.dataset.iterdir() if d.is_dir() and d.name != "temp_kaggle"]

    if not defect_dirs:
        logger.error("No defect directories found")
        return 1

    # Generate metadata for each defect type
    total_created = 0
    total_skipped = 0

    for defect_dir in sorted(defect_dirs):
        if not defect_dir.exists():
            logger.warning(f"Defect directory not found: {defect_dir}")
            continue

        logger.info(f"\nProcessing: {defect_dir.name}")
        created, skipped = generate_metadata_for_defect(
            defect_dir=defect_dir,
            dry_run=args.dry_run,
            overwrite=args.overwrite,
        )

        total_created += created
        total_skipped += skipped

        if created > 0:
            logger.info(f"  ✓ Created: {created} metadata files")
        if skipped > 0:
            logger.info(f"  ⊘ Skipped: {skipped} (already exist)")

    # Summary
    logger.info("")
    logger.info("=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Created: {total_created} metadata files")
    logger.info(f"Skipped: {total_skipped} (already exist)")

    if args.dry_run:
        logger.info("")
        logger.info("This was a dry run. No files were created.")
        logger.info("Run without --dry-run to create metadata files.")
    else:
        logger.info("")
        logger.info("Next steps:")
        logger.info("  1. Review generated metadata files")
        logger.info("  2. Update any incorrect or missing information")
        logger.info("  3. Run validation: python -m backend.scripts.validate_vision_model")

    return 0


if __name__ == "__main__":
    sys.exit(main())
