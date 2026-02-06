from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class RejectDeliveryNoteRequest:
    """
    Αίτημα Απόρριψης.

    Attributes:
        qr_url: Το url qr του δελτίου
        rejection_reason: Περιγραφή του λόγου απόρριψης.
    """

    qr_url: str = field(
        metadata={
            "name": "qrUrl",
            "type": "Element",
            "required": True,
        }
    )
    rejection_reason: None | str = field(
        default=None,
        metadata={
            "name": "rejectionReason",
            "type": "Element",
            "max_length": 150,
        },
    )
