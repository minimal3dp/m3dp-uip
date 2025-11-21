"""
Tests for CSV loader service.
"""

from pathlib import Path

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


@pytest.mark.skip(reason="CSV files not yet added")
def test_csv_loader_loads_files(csv_loader: CSVLoader):
    """Test CSV loader loads files from data directory."""
    assert csv_loader.is_loaded()
    available = csv_loader.get_available_csvs()
    assert len(available) > 0


@pytest.mark.skip(reason="CSV files not yet added")
def test_rotation_distance_formula(csv_loader: CSVLoader):
    """Test getting rotation distance calculator data."""
    df = csv_loader.get_rotation_distance_formula()
    assert df is not None
    assert len(df) > 0
