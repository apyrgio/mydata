from __future__ import annotations

from enum import Enum


class DeliveryOutcomeType(Enum):
    FULL = "FULL"
    PARTIAL = "PARTIAL"
    NONE = "NONE"
