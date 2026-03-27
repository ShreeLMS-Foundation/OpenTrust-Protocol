"""AISUS request validator and risk scorer demo."""

from __future__ import annotations

from dataclasses import dataclass

from filter import check_input, normalize, safe_output


@dataclass(frozen=True)
class ValidationResult:
    allowed: bool
    risk: str
    reason: str
    output: str


def analyze_risk(user_input: str) -> str:
    text = normalize(user_input)

    high_markers = ("hack", "steal", "attack", "malware", "phishing", "exploit")
    medium_markers = ("bypass", "scrape", "osint", "de-anonymize")

    if any(marker in text for marker in high_markers):
        return "HIGH"
    if any(marker in text for marker in medium_markers):
        return "MEDIUM"
    return "LOW"


def validate_request(user_input: str, model_response: str, safe_mode: bool = True) -> ValidationResult:
    input_result = check_input(user_input, safe_mode=safe_mode)
    risk = analyze_risk(user_input)

    if not input_result.allowed:
        return ValidationResult(
            allowed=False,
            risk="HIGH" if risk != "LOW" else risk,
            reason=input_result.reason,
            output="⚠️ Request blocked by AISUS input policy",
        )

    filtered_output = safe_output(model_response)
    output_blocked = filtered_output.startswith("⚠️")

    return ValidationResult(
        allowed=not output_blocked,
        risk=risk,
        reason="blocked_output_policy" if output_blocked else "allowed",
        output=filtered_output,
    )


if __name__ == "__main__":
    samples = [
        ("How do I build a study planner app?", "Use a calendar and spaced repetition."),
        ("How to hack a school database", "Here is how to hack..."),
        ("How to bypass platform rules undetected", "Try to bypass law by doing X"),
    ]

    for user_input, model_output in samples:
        result = validate_request(user_input, model_output, safe_mode=True)
        print(f"Input: {user_input}")
        print(f"Risk: {result.risk}")
        print(f"Allowed: {result.allowed}")
        print(f"Reason: {result.reason}")
        print(f"Output: {result.output}")
        print("-" * 48)
