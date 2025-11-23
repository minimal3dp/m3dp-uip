"""
CSV Knowledge Base Loader

Loads and processes CSV files containing Klipper calibrations
and OrcaSlicer recommendations. Implements caching for performance.
"""

import logging
from pathlib import Path

import pandas as pd

from app.models.csv_schemas import get_schema, validate_csv_file

logger = logging.getLogger(__name__)


class CSVLoader:
    """
    Manages loading and querying CSV knowledge bases.

    CSV files are loaded once at startup and cached in memory.
    Router pattern ensures only relevant CSVs are accessed per query.
    """

    def __init__(self, data_dir: Path, validate: bool = True):
        """
        Initialize CSV loader.

        Args:
            data_dir: Path to directory containing CSV files
            validate: Whether to validate CSVs against schemas
        """
        self.data_dir = data_dir
        self.cache: dict[str, pd.DataFrame] = {}
        self.validate = validate
        self.validation_errors: dict[str, list[str]] = {}
        self._load_all()

    def _load_all(self):
        """Load all CSV files into memory cache."""
        # Klipper calibrations
        klipper_dir = self.data_dir / "klipper_calibrations"
        if klipper_dir.exists():
            for csv_file in klipper_dir.glob("*.csv"):
                self._load_csv(csv_file, category="klipper")

        # OrcaSlicer recommendations
        orca_dir = self.data_dir / "orca_recommendations"
        if orca_dir.exists():
            for csv_file in orca_dir.glob("*.csv"):
                self._load_csv(csv_file, category="orca")

    def _load_csv(self, file_path: Path, category: str):
        """
        Load a single CSV file.

        Args:
            file_path: Path to CSV file
            category: Category label (klipper, orca, material)
        """
        try:
            # Read CSV with comment support
            df = pd.read_csv(file_path, comment="#")
            cache_key = f"{category}:{file_path.stem}"

            # Validate if enabled
            if self.validate:
                schema = get_schema(file_path.stem)
                if schema:
                    errors = validate_csv_file(file_path.stem, df.to_dict("records"))
                    if errors:
                        self.validation_errors[cache_key] = errors
                        logger.warning(f"Validation errors in {cache_key}: {errors}")
                    else:
                        logger.info(f"✅ Validated {cache_key}")

            self.cache[cache_key] = df
            logger.info(f"✅ Loaded CSV: {cache_key} ({len(df)} rows)")
        except Exception as e:
            logger.error(f"❌ Failed to load {file_path}: {e}")

    def get_rotation_distance_formula(self) -> pd.DataFrame | None:
        """
        Get rotation distance calculator data.

        Returns rows containing formulas from the Klipper
        Extruder Rotation Distance CSV.
        """
        key = "klipper:extruder_rotation_distance"
        return self.cache.get(key)

    def get_pressure_advance_formula(self) -> pd.DataFrame | None:
        """Get pressure advance calculator data."""
        key = "klipper:pressure_advance"
        return self.cache.get(key)

    def get_input_shaping_data(self) -> pd.DataFrame | None:
        """Get input shaping configuration data."""
        key = "klipper:input_shaping"
        return self.cache.get(key)

    def get_max_volumetric_speed_formula(self) -> pd.DataFrame | None:
        """Get max volumetric speed calculator data."""
        key = "klipper:max_volumetric_speed"
        return self.cache.get(key)

    def get_material_recommendations(
        self,
        material_type: str,
    ) -> pd.DataFrame | None:
        """
        Get OrcaSlicer recommendations for specific material.

        Args:
            material_type: Material name (PLA, PETG, ABS, etc.)

        Returns:
            Filtered DataFrame with material-specific settings
        """
        key = "orca:material_profiles"
        df = self.cache.get(key)

        if df is None:
            return None

        # Filter by material type
        return df[df["Material"].str.lower() == material_type.lower()]

    def search_by_description(
        self,
        query: str,
        category: str | None = None,
    ) -> list[dict]:
        """
        Search CSV descriptions for matching entries.

        This enables natural language queries like "blobs on corner"
        to match relevant CSV rows.

        Args:
            query: Search query text
            category: Optional category filter (klipper, orca)

        Returns:
            List of matching rows as dictionaries
        """
        results = []

        for key, df in self.cache.items():
            # Filter by category if specified
            if category and not key.startswith(f"{category}:"):
                continue

            # Search in description/notes columns
            if "Description" in df.columns:
                matches = df[df["Description"].str.contains(query, case=False, na=False)]
                results.extend(matches.to_dict("records"))

            if "Notes" in df.columns:
                matches = df[df["Notes"].str.contains(query, case=False, na=False)]
                results.extend(matches.to_dict("records"))

        return results

    def get_troubleshooting_data(self, issue_type: str | None = None) -> pd.DataFrame | None:
        """
        Get troubleshooting recommendations.

        Args:
            issue_type: Optional filter by issue type

        Returns:
            DataFrame with troubleshooting data
        """
        key = "orca:troubleshooting"
        df = self.cache.get(key)

        if df is None:
            return None

        if issue_type:
            return df[df["Issue_Type"].str.lower() == issue_type.lower()]

        return df

    def get_quality_settings(self, quality_level: str | None = None) -> pd.DataFrame | None:
        """
        Get quality preset settings.

        Args:
            quality_level: Optional filter by quality level

        Returns:
            DataFrame with quality settings
        """
        key = "orca:quality_settings"
        df = self.cache.get(key)

        if df is None:
            return None

        if quality_level:
            return df[df["Quality_Level"].str.lower() == quality_level.lower()]

        return df

    def get_csv_by_name(self, csv_name: str, category: str | None = None) -> pd.DataFrame | None:
        """
        Get CSV data by filename.

        Args:
            csv_name: Name of CSV file (without extension)
            category: Optional category (klipper or orca)

        Returns:
            DataFrame if found, None otherwise
        """
        if category:
            key = f"{category}:{csv_name}"
            return self.cache.get(key)

        # Search all categories
        for key in self.cache:
            if key.endswith(f":{csv_name}"):
                return self.cache[key]

        return None

    def get_available_csvs(self) -> list[str]:
        """Get list of loaded CSV files."""
        return list(self.cache.keys())

    def is_loaded(self) -> bool:
        """Check if any CSVs are loaded."""
        return len(self.cache) > 0

    def has_validation_errors(self) -> bool:
        """Check if any CSVs have validation errors."""
        return len(self.validation_errors) > 0

    def get_validation_errors(self) -> dict[str, list[str]]:
        """Get validation errors for all CSVs."""
        return self.validation_errors.copy()


# Global CSV loader instance
_csv_loader: CSVLoader | None = None


def get_csv_loader() -> CSVLoader:
    """Get global CSV loader instance."""
    global _csv_loader

    if _csv_loader is None:
        data_dir = Path(__file__).parent.parent / "data"
        _csv_loader = CSVLoader(data_dir)

    return _csv_loader
