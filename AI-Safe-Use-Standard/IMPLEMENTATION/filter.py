"""Basic AISUS filtering utilities.

This module is intentionally lightweight and framework-agnostic so it can be
copied into chatbots, APIs, or web apps.
"""

from __future__ import annotations

from dataclasses import dataclass

from config import BANNED_INPUT_KEYWORDS, BANNED_OUTPUT_KEYWORDS, SAFE_MODE_PATTERNS


@dataclass(frozen=True)
class FilterResult:
    allowed: bool
    reason: str


def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())


def check_input(text: str, safe_mode: bool = True) -> FilterResult:
    cleaned = normalize(text)

    for keyword in BANNED_INPUT_KEYWORDS:
        if keyword in cleaned:
            return FilterResult(False, f"blocked_input_keyword:{keyword}")

    # In safe mode, reject explicit suspicious intent patterns.
    if safe_mode and any(token in cleaned for token in SAFE_MODE_PATTERNS):
        return FilterResult(False, "blocked_safe_mode_pattern")

    return FilterResult(True, "allowed")


def safe_output(response: str) -> str:
    cleaned = normalize(response)
    for keyword in BANNED_OUTPUT_KEYWORDS:
        if keyword in cleaned:
            return "⚠️ Restricted content under AISUS policy"
    return response
