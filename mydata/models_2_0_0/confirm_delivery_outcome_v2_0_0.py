from __future__ import annotations

from dataclasses import dataclass, field

from mydata.models_2_0_0.simple_types_v2_0_0 import DeliveryOutcomeType
from mydata.models_2_0_0.transport_types_v2_0_0 import PackagingDetailType


@dataclass(kw_only=True)
class ConfirmDeliveryOutcomeRequest:
    """
    Επιβεβαίωση-Δήλωση Παράδοσης-Παραλαβής Παραστατικού.

    Attributes:
        qr_url: Το url qr του δελτίου
        outcome: Αποτέλεσμα
        delivered_without_recipient: Ένδειξη  παράδοσης χωρίς τη φυσική
            παρουσία του παραλήπτη.
        delivered_packaging: Λίστα με τις συσκευασίες και τις ποσότητες
            που παραδόθηκαν.
    """

    qr_url: str = field(
        metadata={
            "name": "qrUrl",
            "type": "Element",
            "required": True,
        }
    )
    outcome: DeliveryOutcomeType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    delivered_without_recipient: None | bool = field(
        default=None,
        metadata={
            "name": "deliveredWithoutRecipient",
            "type": "Element",
        },
    )
    delivered_packaging: list[PackagingDetailType] = field(
        default_factory=list,
        metadata={
            "name": "deliveredPackaging",
            "type": "Element",
        },
    )
