"""AISUS request validator and risk scorer demo."""

from __future__ import annotations

from dataclasses import dataclass

from config import SAFE_MODE_DEFAULT
from pipeline import moderate_exchange
from risk import analyze_risk


@dataclass(frozen=True)
class ValidationResult:
    allowed: bool
    risk: str
    reason: str
    output: str
    timestamp_utc: str


def validate_request(user_input: str, model_response: str, safe_mode: bool = SAFE_MODE_DEFAULT) -> ValidationResult:
    pipeline_result = moderate_exchange(user_input, model_response, safe_mode=safe_mode)
    event = pipeline_result.event

    return ValidationResult(
        allowed=event.allowed,
        risk=event.risk,
        reason=event.reason,
        output=pipeline_result.output,
        timestamp_utc=event.timestamp_utc,
    )


if __name__ == "__main__":
    samples = [
        ("How do I build a study planner app?", "Use a calendar and spaced repetition."),
        ("How to hack a school database", "Here is how to hack..."),
        ("How to bypass platform rules undetected", "Try to bypass law by doing X"),
    ]

    for user_input, model_output in samples:
        result = validate_request(user_input, model_output, safe_mode=True)
        derived_risk = analyze_risk(user_input)
        print(f"Input: {user_input}")
        print(f"Risk (pipeline): {result.risk}")
        print(f"Risk (analyze_risk): {derived_risk}")
        print(f"Allowed: {result.allowed}")
        print(f"Reason: {result.reason}")
        print(f"Timestamp (UTC): {result.timestamp_utc}")
        print(f"Output: {result.output}")
        print("-" * 48)
