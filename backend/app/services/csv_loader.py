"""
CSV Knowledge Base Loader

Loads and processes CSV files containing Klipper calibrations
and OrcaSlicer recommendations. Implements caching for performance.
"""

from pathlib import Path

import pandas as pd


class CSVLoader:
    """
    Manages loading and querying CSV knowledge bases.

    CSV files are loaded once at startup and cached in memory.
    Router pattern ensures only relevant CSVs are accessed per query.
    """

    def __init__(self, data_dir: Path):
        """
        Initialize CSV loader.

        Args:
            data_dir: Path to directory containing CSV files
        """
        self.data_dir = data_dir
        self.cache: dict[str, pd.DataFrame] = {}
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
            df = pd.read_csv(file_path)
            cache_key = f"{category}:{file_path.stem}"
            self.cache[cache_key] = df
            print(f"✅ Loaded CSV: {cache_key} ({len(df)} rows)")
        except Exception as e:
            print(f"❌ Failed to load {file_path}: {e}")

    def get_rotation_distance_formula(self) -> pd.DataFrame | None:
        """
        Get rotation distance calculator data.

        Returns rows containing formulas from the Klipper
        Extruder Rotation Distance CSV.
        """
        key = "klipper:Extruder Rotation Distance"
        return self.cache.get(key)

    def get_pressure_advance_formula(self) -> pd.DataFrame | None:
        """Get pressure advance calculator data."""
        key = "klipper:Pressure Advance"
        return self.cache.get(key)

    def get_flow_rate_formula(self) -> pd.DataFrame | None:
        """Get flow rate calculator data."""
        key = "klipper:Flow Rate"
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
        key = "orca:Material Profiles"
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

    def get_available_csvs(self) -> list[str]:
        """Get list of loaded CSV files."""
        return list(self.cache.keys())

    def is_loaded(self) -> bool:
        """Check if any CSVs are loaded."""
        return len(self.cache) > 0


# Global CSV loader instance
_csv_loader: CSVLoader | None = None


def get_csv_loader() -> CSVLoader:
    """Get global CSV loader instance."""
    global _csv_loader

    if _csv_loader is None:
        data_dir = Path(__file__).parent.parent / "data"
        _csv_loader = CSVLoader(data_dir)

    return _csv_loader
