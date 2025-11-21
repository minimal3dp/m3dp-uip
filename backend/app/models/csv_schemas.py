"""
CSV schema definitions for M3DP-UIP knowledge base.

Defines the expected structure and validation rules for each CSV type.
Used by the CSV loader to validate data integrity.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class CSVCategory(str, Enum):
    """Categories of CSV files."""

    KLIPPER = "klipper_calibrations"
    ORCA = "orca_recommendations"


class DataType(str, Enum):
    """Supported data types for CSV columns."""

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"


@dataclass
class ColumnSchema:
    """Schema definition for a CSV column."""

    name: str
    data_type: DataType
    required: bool = True
    min_value: float | None = None
    max_value: float | None = None
    allowed_values: list[str] | None = None
    description: str = ""

    def validate(self, value: Any) -> tuple[bool, str | None]:
        """
        Validate a column value.

        Args:
            value: Value to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check required
        if self.required and (value is None or str(value).strip() == ""):
            return False, f"Required column '{self.name}' is empty"

        # Skip validation if empty and not required
        if not self.required and (value is None or str(value).strip() == ""):
            return True, None

        # Type validation
        try:
            if self.data_type == DataType.INTEGER:
                value = int(value)
            elif self.data_type == DataType.FLOAT:
                value = float(value)
            elif self.data_type == DataType.BOOLEAN and str(value).lower() not in {
                "true",
                "false",
                "1",
                "0",
                "yes",
                "no",
            }:
                return False, f"Invalid boolean value: {value}"
        except (ValueError, TypeError):
            return False, f"Invalid {self.data_type.value} value: {value}"

        # Range validation
        if isinstance(value, (int, float)):
            if self.min_value is not None and value < self.min_value:
                return False, f"Value {value} below minimum {self.min_value}"
            if self.max_value is not None and value > self.max_value:
                return False, f"Value {value} above maximum {self.max_value}"

        # Allowed values validation
        if self.allowed_values and str(value) not in self.allowed_values:
            return (
                False,
                f"Value '{value}' not in allowed values: {self.allowed_values}",
            )

        return True, None


@dataclass
class CSVSchema:
    """Schema definition for a CSV file."""

    name: str
    category: CSVCategory
    columns: list[ColumnSchema]
    description: str = ""

    def validate_row(self, row: dict[str, Any]) -> list[str]:
        """
        Validate a single row of data.

        Args:
            row: Dictionary of column name to value

        Returns:
            List of error messages (empty if valid)
        """
        errors = []

        # Check for required columns
        for col in self.columns:
            if col.required and col.name not in row:
                errors.append(f"Missing required column: {col.name}")

        # Validate each present column
        for col_name, value in row.items():
            col_schema = next((c for c in self.columns if c.name == col_name), None)
            if col_schema:
                is_valid, error = col_schema.validate(value)
                if not is_valid:
                    errors.append(error)

        return errors


# Klipper CSV Schemas
EXTRUDER_ROTATION_DISTANCE_SCHEMA = CSVSchema(
    name="extruder_rotation_distance",
    category=CSVCategory.KLIPPER,
    description="Extruder rotation distance calibration data",
    columns=[
        ColumnSchema("Name", DataType.STRING, description="Parameter name"),
        ColumnSchema("Description", DataType.STRING, description="Parameter description"),
        ColumnSchema("Formula", DataType.STRING, required=False, description="Calculation formula"),
        ColumnSchema("Units", DataType.STRING, description="Measurement units"),
        ColumnSchema("Expected_Range", DataType.STRING, description="Typical value range"),
        ColumnSchema("Notes", DataType.STRING, required=False, description="Additional notes"),
    ],
)

PRESSURE_ADVANCE_SCHEMA = CSVSchema(
    name="pressure_advance",
    category=CSVCategory.KLIPPER,
    description="Pressure advance calibration settings",
    columns=[
        ColumnSchema("Name", DataType.STRING),
        ColumnSchema("Description", DataType.STRING),
        ColumnSchema("Formula", DataType.STRING, required=False),
        ColumnSchema("Units", DataType.STRING),
        ColumnSchema("Expected_Range", DataType.STRING),
        ColumnSchema("Notes", DataType.STRING, required=False),
    ],
)

INPUT_SHAPING_SCHEMA = CSVSchema(
    name="input_shaping",
    category=CSVCategory.KLIPPER,
    description="Input shaping resonance compensation",
    columns=[
        ColumnSchema("Name", DataType.STRING),
        ColumnSchema("Description", DataType.STRING),
        ColumnSchema("Formula", DataType.STRING, required=False),
        ColumnSchema("Units", DataType.STRING),
        ColumnSchema("Expected_Range", DataType.STRING),
        ColumnSchema("Notes", DataType.STRING, required=False),
    ],
)

# OrcaSlicer CSV Schemas
MATERIAL_PROFILES_SCHEMA = CSVSchema(
    name="material_profiles",
    category=CSVCategory.ORCA,
    description="Material-specific slicer settings",
    columns=[
        ColumnSchema("Material", DataType.STRING),
        ColumnSchema("Nozzle_Temp_Min", DataType.INTEGER, min_value=150, max_value=300),
        ColumnSchema("Nozzle_Temp_Max", DataType.INTEGER, min_value=150, max_value=300),
        ColumnSchema("Bed_Temp", DataType.INTEGER, min_value=0, max_value=150),
        ColumnSchema("Print_Speed", DataType.INTEGER, min_value=10, max_value=200),
        ColumnSchema("Fan_Speed", DataType.INTEGER, min_value=0, max_value=100),
        ColumnSchema("Retraction_Distance", DataType.FLOAT, min_value=0, max_value=10),
        ColumnSchema("Retraction_Speed", DataType.INTEGER, min_value=10, max_value=100),
        ColumnSchema("Notes", DataType.STRING, required=False),
    ],
)

QUALITY_SETTINGS_SCHEMA = CSVSchema(
    name="quality_settings",
    category=CSVCategory.ORCA,
    description="Print quality presets",
    columns=[
        ColumnSchema("Quality_Level", DataType.STRING),
        ColumnSchema("Layer_Height", DataType.FLOAT, min_value=0.04, max_value=0.5),
        ColumnSchema("Line_Width", DataType.FLOAT, min_value=0.2, max_value=1.0),
        ColumnSchema("Infill_Density", DataType.INTEGER, min_value=0, max_value=100),
        ColumnSchema("Perimeters", DataType.INTEGER, min_value=1, max_value=10),
        ColumnSchema("Top_Layers", DataType.INTEGER, min_value=1, max_value=20),
        ColumnSchema("Bottom_Layers", DataType.INTEGER, min_value=1, max_value=20),
        ColumnSchema("Print_Speed", DataType.INTEGER, min_value=10, max_value=300),
        ColumnSchema("Travel_Speed", DataType.INTEGER, min_value=10, max_value=500),
        ColumnSchema("Notes", DataType.STRING, required=False),
    ],
)

TROUBLESHOOTING_SCHEMA = CSVSchema(
    name="troubleshooting",
    category=CSVCategory.ORCA,
    description="Common issues and solutions",
    columns=[
        ColumnSchema("Issue_Type", DataType.STRING),
        ColumnSchema("Symptom", DataType.STRING),
        ColumnSchema("Likely_Cause", DataType.STRING),
        ColumnSchema("Slicer_Setting", DataType.STRING, required=False),
        ColumnSchema("Klipper_Setting", DataType.STRING, required=False),
        ColumnSchema("Mechanical_Fix", DataType.STRING, required=False),
        ColumnSchema("Notes", DataType.STRING, required=False),
        # Phase 2.5 enrichment columns
        ColumnSchema(
            "visual_markers",
            DataType.STRING,
            required=False,
            description="Observable features for vision API",
        ),
        ColumnSchema(
            "reference_image_url",
            DataType.STRING,
            required=False,
            description="Link to reference defect image",
        ),
        ColumnSchema(
            "severity",
            DataType.STRING,
            required=False,
            allowed_values=["Critical", "High", "Medium", "Low"],
            description="Severity level",
        ),
        ColumnSchema(
            "printer_dependency",
            DataType.STRING,
            required=False,
            allowed_values=["Generic", "Bowden", "Direct Drive"],
            description="Printer-specific dependency",
        ),
        ColumnSchema(
            "skill_level_required",
            DataType.STRING,
            required=False,
            allowed_values=["Beginner", "Intermediate", "Advanced"],
            description="Skill level to apply fix",
        ),
        ColumnSchema(
            "related_defects",
            DataType.STRING,
            required=False,
            description="Comma-separated related defects",
        ),
    ],
)

# Registry of all schemas
SCHEMA_REGISTRY: dict[str, CSVSchema] = {
    "extruder_rotation_distance": EXTRUDER_ROTATION_DISTANCE_SCHEMA,
    "pressure_advance": PRESSURE_ADVANCE_SCHEMA,
    "input_shaping": INPUT_SHAPING_SCHEMA,
    "material_profiles": MATERIAL_PROFILES_SCHEMA,
    "quality_settings": QUALITY_SETTINGS_SCHEMA,
    "troubleshooting": TROUBLESHOOTING_SCHEMA,
}


def get_schema(csv_name: str) -> CSVSchema | None:
    """
    Get schema for a CSV file.

    Args:
        csv_name: Name of CSV file (without extension)

    Returns:
        CSVSchema if found, None otherwise
    """
    return SCHEMA_REGISTRY.get(csv_name)


def validate_csv_file(csv_name: str, data: list[dict[str, Any]]) -> list[str]:
    """
    Validate an entire CSV file.

    Args:
        csv_name: Name of CSV file
        data: List of row dictionaries

    Returns:
        List of error messages (empty if valid)
    """
    schema = get_schema(csv_name)
    if not schema:
        return [f"No schema found for CSV: {csv_name}"]

    errors = []
    for idx, row in enumerate(data, start=1):
        row_errors = schema.validate_row(row)
        for error in row_errors:
            errors.append(f"Row {idx}: {error}")

    return errors
