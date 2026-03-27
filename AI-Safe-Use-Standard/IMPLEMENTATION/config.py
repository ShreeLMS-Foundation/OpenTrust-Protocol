"""Central AISUS configuration constants."""

from __future__ import annotations

SAFE_MODE_DEFAULT = True

BANNED_INPUT_KEYWORDS = {
    "hack",
    "steal",
    "attack",
    "ddos",
    "malware",
    "ransomware",
    "phishing",
    "carding",
    "data theft",
}

BANNED_OUTPUT_KEYWORDS = {
    "how to hack",
    "bypass law",
    "illegal exploit",
}

HIGH_RISK_MARKERS = ("hack", "steal", "attack", "malware", "phishing", "exploit")
MEDIUM_RISK_MARKERS = ("bypass", "scrape", "osint", "de-anonymize")
SAFE_MODE_PATTERNS = ("bypass", "evade", "undetected")
