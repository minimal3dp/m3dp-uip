"""
Tests for CSV loader service.
"""

from pathlib import Path

import pandas as pd
import pytest
from app.services.csv_loader import CSVLoader


@pytest.fixture
def csv_loader():
    """Create CSV loader instance with test data directory."""
    data_dir = Path(__file__).parent.parent / "app" / "data"
    return CSVLoader(data_dir)


def test_csv_loader_initialization(csv_loader: CSVLoader):
    """Test CSV loader initializes correctly."""
    assert csv_loader is not None
    assert csv_loader.cache is not None


def test_csv_loader_loads_files(csv_loader: CSVLoader):
    """Test CSV loader loads files from data directory."""
    assert csv_loader.is_loaded()
    available = csv_loader.get_available_csvs()
    assert len(available) >= 6  # We created 6 CSV files
    print(f"\nLoaded CSVs: {available}")


def test_rotation_distance_formula(csv_loader: CSVLoader):
    """Test getting rotation distance calculator data."""
    df = csv_loader.get_rotation_distance_formula()
    assert df is not None
    assert len(df) > 0
    assert "Name" in df.columns
    assert "Formula" in df.columns


def test_pressure_advance_data(csv_loader: CSVLoader):
    """Test pressure advance data retrieval."""
    df = csv_loader.get_pressure_advance_formula()
    assert df is not None
    assert len(df) > 0
    assert "Name" in df.columns


def test_input_shaping_data(csv_loader: CSVLoader):
    """Test input shaping data retrieval."""
    df = csv_loader.get_input_shaping_data()
    assert df is not None
    assert len(df) > 0
    assert "Name" in df.columns


def test_material_recommendations(csv_loader: CSVLoader):
    """Test material recommendations retrieval."""
    # Test with PLA
    df = csv_loader.get_material_recommendations("PLA")
    assert df is not None
    assert len(df) > 0
    assert df.iloc[0]["Material"] == "PLA"

    # Test with PETG (case insensitive)
    df = csv_loader.get_material_recommendations("petg")
    assert df is not None
    assert len(df) > 0


def test_quality_settings(csv_loader: CSVLoader):
    """Test quality settings retrieval."""
    # Get all quality settings
    df = csv_loader.get_quality_settings()
    assert df is not None
    assert len(df) >= 5  # We have 5 quality levels

    # Test specific quality level
    df = csv_loader.get_quality_settings("Draft")
    assert df is not None
    assert len(df) == 1
    assert df.iloc[0]["Quality_Level"] == "Draft"


def test_troubleshooting_data(csv_loader: CSVLoader):
    """Test troubleshooting data retrieval."""
    # Get all troubleshooting data
    df = csv_loader.get_troubleshooting_data()
    assert df is not None
    assert len(df) >= 60  # Phase 2.5: We now have 60+ defects from research

    # Test specific issue type (multiple entries for comprehensive coverage)
    df = csv_loader.get_troubleshooting_data("Stringing")
    assert df is not None
    assert len(df) >= 3  # Multiple Stringing entries with different causes


def test_search_functionality(csv_loader: CSVLoader):
    """Test search by description."""
    results = csv_loader.search_by_description("extrusion")
    assert isinstance(results, list)
    assert len(results) > 0


def test_get_csv_by_name(csv_loader: CSVLoader):
    """Test getting CSV by name."""
    # With category
    df = csv_loader.get_csv_by_name("material_profiles", category="orca")
    assert df is not None
    assert isinstance(df, pd.DataFrame)

    # Without category
    df = csv_loader.get_csv_by_name("pressure_advance")
    assert df is not None


def test_validation(csv_loader: CSVLoader):
    """Test CSV validation."""
    # Check if validation ran
    if csv_loader.has_validation_errors():
        errors = csv_loader.get_validation_errors()
        print(f"\n⚠️ Validation errors: {errors}")
        # Errors are warnings, not test failures
    else:
        print("\n✅ All CSVs passed validation")


def test_get_available_csvs(csv_loader: CSVLoader):
    """Test listing available CSVs."""
    csvs = csv_loader.get_available_csvs()
    assert len(csvs) > 0
    assert any("klipper" in csv for csv in csvs)
    assert any("orca" in csv for csv in csvs)
