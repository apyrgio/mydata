from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from mydata.models_2_0_0.transport_types_v2_0_0 import DeliveryEventType


@dataclass(kw_only=True)
class GetDeliveryNoteStatusResponseType:
    mark: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    dispatch_timestamp: XmlDateTime = field(
        metadata={
            "name": "dispatchTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    lifecycle_history: list[DeliveryEventType] = field(
        default_factory=list,
        metadata={
            "name": "lifecycleHistory",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GetDeliveryNoteStatusResponse(GetDeliveryNoteStatusResponseType):
    pass
