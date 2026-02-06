from __future__ import annotations

from dataclasses import dataclass, field

from mydata.models_2_0_0.transport_types_v2_0_0 import TransportDetailType


@dataclass(kw_only=True)
class Transport:
    """
    Μεταφόρτωση.

    Attributes:
        transport_mark: Αποδεικτικό Λήψης Μεταφόρτωσης. Συμπληρώνεται
            από την Υπηρεσία
        qr_url: Το url qr του δελτίου
        transport_detail: Λεπτομέρειες Μεταφόρτωσης
    """

    transport_mark: None | int = field(
        default=None,
        metadata={
            "name": "transportMark",
            "type": "Element",
        },
    )
    qr_url: str = field(
        metadata={
            "name": "qrUrl",
            "type": "Element",
            "required": True,
        }
    )
    transport_detail: TransportDetailType = field(
        metadata={
            "name": "transportDetail",
            "type": "Element",
            "required": True,
        }
    )
