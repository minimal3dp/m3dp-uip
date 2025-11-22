from app.services.router import IssueType, classify_issue


def test_router_mechanical_keywords():
    assert classify_issue("Belt tension causing layer shift") == IssueType.mechanical
    assert classify_issue("Extruder clicking under load") == IssueType.mechanical


def test_router_slicer_keywords():
    assert classify_issue("Retraction settings causing blobs") == IssueType.slicer
    assert classify_issue("Support interface poorly tuned") == IssueType.slicer


def test_router_material_keywords():
    assert classify_issue("Stringing on PETG due to humidity") == IssueType.material
    assert classify_issue("ABS warping at corners") == IssueType.material


def test_router_default_fallback():
    # No clear keyword -> mechanical default
    assert classify_issue("Unknown surface artifact appears") == IssueType.mechanical
