from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass(kw_only=True)
class ContinuationTokenType1:
    class Meta:
        name = "ContinuationTokenType"

    next_partition_key: None | str = field(
        default=None,
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    next_row_key: None | str = field(
        default=None,
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class InvoiceVatDetailType:
    mark: None | str = field(
        default=None,
        metadata={
            "name": "Mark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    is_cancelled: None | bool = field(
        default=None,
        metadata={
            "name": "IsCancelled",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    issue_date: XmlDateTime = field(
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    vat301: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat301",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat302: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat302",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat303: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat303",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat304: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat304",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat305: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat305",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat306: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat306",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat331: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat331",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat332: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat332",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat333: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat333",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat334: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat334",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat335: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat335",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat336: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat336",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat361: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat361",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat362: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat362",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat363: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat363",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat364: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat364",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat365: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat365",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat366: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat366",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat381: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat381",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat382: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat382",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat383: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat383",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat384: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat384",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat385: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat385",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat386: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat386",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat342: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat342",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat345: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat345",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat348: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat348",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat349: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat349",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat310: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat310",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat402: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat402",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat407: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat407",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat411: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat411",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat423: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat423",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat422: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vat422",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat_unclassified361: None | Decimal = field(
        default=None,
        metadata={
            "name": "VatUnclassified361",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat_unclassified381: None | Decimal = field(
        default=None,
        metadata={
            "name": "VatUnclassified381",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class RequestedVatInfoType:
    continuation_token: None | ContinuationTokenType1 = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat_info: list[InvoiceVatDetailType] = field(
        default_factory=list,
        metadata={
            "name": "VatInfo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class RequestedVatInfo(RequestedVatInfoType):
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"
