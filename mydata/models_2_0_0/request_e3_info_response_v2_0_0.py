from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDateTime

from mydata.models_2_0_0.request_vat_info_response_v2_0_0 import (
    ContinuationTokenType1,
)

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass(kw_only=True)
class InvoiceE3DetailType:
    v_afm: None | str = field(
        default=None,
        metadata={
            "name": "V_Afm",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_mark: None | str = field(
        default=None,
        metadata={
            "name": "V_Mark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_book: None | str = field(
        default=None,
        metadata={
            "name": "vBook",
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
    v_class_category: None | str = field(
        default=None,
        metadata={
            "name": "V_Class_Category",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_class_type: None | str = field(
        default=None,
        metadata={
            "name": "V_Class_Type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_class_value: None | Decimal = field(
        default=None,
        metadata={
            "name": "V_Class_Value",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class RequestedE3InfoType:
    continuation_token: None | ContinuationTokenType1 = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    e3_info: list[InvoiceE3DetailType] = field(
        default_factory=list,
        metadata={
            "name": "E3Info",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class RequestedE3Info(RequestedE3InfoType):
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"
