from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class GenerateGroupQrcodeResponseType:
    class Meta:
        name = "GenerateGroupQRCodeResponseType"

    group_qr_url: str = field(
        metadata={
            "name": "groupQrUrl",
            "type": "Element",
            "required": True,
        }
    )
    qr_urls_count: int = field(
        metadata={
            "name": "qrUrlsCount",
            "type": "Element",
            "required": True,
        }
    )
    expires_at: str = field(
        metadata={
            "name": "expiresAt",
            "type": "Element",
            "required": True,
        }
    )
    status_code: str = field(
        metadata={
            "name": "statusCode",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GenerateGroupQrcodeResponse(GenerateGroupQrcodeResponseType):
    class Meta:
        name = "GenerateGroupQRCodeResponse"
