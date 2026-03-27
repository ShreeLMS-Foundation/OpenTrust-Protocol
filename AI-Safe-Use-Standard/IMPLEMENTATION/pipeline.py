"""AISUS moderation pipeline: User -> Input Filter -> AI -> Output Filter."""

from __future__ import annotations

from dataclasses import dataclass

from filter import check_input, safe_output
from logging_policy import make_event, SafetyEvent
from risk import analyze_risk


@dataclass(frozen=True)
class PipelineResult:
    event: SafetyEvent
    output: str


def moderate_exchange(user_input: str, model_output: str, safe_mode: bool = True) -> PipelineResult:
    input_result = check_input(user_input, safe_mode=safe_mode)
    risk = analyze_risk(user_input)

    if not input_result.allowed:
        event = make_event(risk="HIGH" if risk != "LOW" else risk, allowed=False, reason=input_result.reason)
        return PipelineResult(event=event, output="⚠️ Request blocked by AISUS input policy")

    final_output = safe_output(model_output)
    blocked = final_output.startswith("⚠️")
    event = make_event(risk=risk, allowed=not blocked, reason="blocked_output_policy" if blocked else "allowed")
    return PipelineResult(event=event, output=final_output)
