"""AISUS risk scoring logic."""

from __future__ import annotations

from config import HIGH_RISK_MARKERS, MEDIUM_RISK_MARKERS
from filter import normalize


def analyze_risk(user_input: str) -> str:
    text = normalize(user_input)

    if any(marker in text for marker in HIGH_RISK_MARKERS):
        return "HIGH"
    if any(marker in text for marker in MEDIUM_RISK_MARKERS):
        return "MEDIUM"
    return "LOW"
