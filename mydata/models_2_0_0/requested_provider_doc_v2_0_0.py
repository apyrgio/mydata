from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class InvoiceProviderType:
    """
    Attributes:
        issuer_vat: ΑΦΜ Εκδότη
        invoice_provider_mark: Μοναδικός Αριθμός Καταχώρησης
            παραστατικού Παρόχου
        invoice_uid: Αναγνωριστικό οντότητας
        authentication_code: Συμβολοσειρά Αυθεντικοποίησης Παραστατικού
            Παρόχου
    """

    issuer_vat: str = field(
        metadata={
            "name": "issuerVAT",
            "type": "Element",
            "required": True,
        }
    )
    invoice_provider_mark: int = field(
        metadata={
            "name": "invoiceProviderMark",
            "type": "Element",
            "required": True,
        }
    )
    invoice_uid: str = field(
        metadata={
            "name": "invoiceUid",
            "type": "Element",
            "required": True,
        }
    )
    authentication_code: str = field(
        metadata={
            "name": "authenticationCode",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContinuationTokenType:
    class Meta:
        name = "continuationTokenType"

    next_partition_key: str = field(
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "required": True,
        }
    )
    next_row_key: str = field(
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestedProviderDoc:
    """
    Παραστατικά από Πάροχο.
    """

    continuation_token: list[ContinuationTokenType] = field(
        default_factory=list,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "sequence": 1,
        },
    )
    invoice_provider_type: list[InvoiceProviderType] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceProviderType",
            "type": "Element",
            "sequence": 1,
        },
    )
