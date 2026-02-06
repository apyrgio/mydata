from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class QrUrlsType:
    qr_url: list[str] = field(
        default_factory=list,
        metadata={
            "name": "qrUrl",
            "type": "Element",
            "min_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class GenerateGroupQrcodeRequestType:
    class Meta:
        name = "GenerateGroupQRCodeRequestType"

    qr_urls: QrUrlsType = field(
        metadata={
            "name": "qrUrls",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GenerateGroupQrcodeRequest(GenerateGroupQrcodeRequestType):
    class Meta:
        name = "GenerateGroupQRCodeRequest"
