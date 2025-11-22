from enum import Enum


class IssueType(str, Enum):
    mechanical = "mechanical"
    slicer = "slicer"
    material = "material"


# Very minimal stub classification based on keyword heuristics; replace with model later.
KEYWORDS: dict[IssueType, set[str]] = {
    IssueType.mechanical: {"belt", "layer shift", "vfa", "extruder"},
    IssueType.slicer: {"retraction", "seam", "infill", "support"},
    IssueType.material: {"stringing", "abs", "pla", "petg", "humidity"},
}


def classify_issue(text: str) -> IssueType:
    lowered = text.lower()
    for issue_type, words in KEYWORDS.items():
        if any(w in lowered for w in words):
            return issue_type
    return IssueType.mechanical  # default fallback


__all__ = ["IssueType", "classify_issue"]
