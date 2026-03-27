"""Privacy-aware event logging helpers for AISUS."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class SafetyEvent:
    timestamp_utc: str
    risk: str
    allowed: bool
    reason: str


def make_event(risk: str, allowed: bool, reason: str) -> SafetyEvent:
    return SafetyEvent(
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        risk=risk,
        allowed=allowed,
        reason=reason,
    )
