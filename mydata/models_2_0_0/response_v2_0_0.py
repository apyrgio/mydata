from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ErrorType:
    """
    Attributes:
        message: Μήνυμα Σφάλματος
        code: Κωδικός Σφάλαματος
    """

    message: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    code: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProviderInfoType:
    """
    Attributes:
        vatnumber: ΑΦΜ
    """

    vatnumber: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VATNumber",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ReceptionEmailsType:
    """
    Attributes:
        email: Email
    """

    class Meta:
        name = "receptionEmailsType"

    email: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ReceptionProvidersType:
    """
    Attributes:
        provider_info: Πληροφορίες Παρόχου
    """

    class Meta:
        name = "receptionProvidersType"

    provider_info: list[ProviderInfoType] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ResponseType:
    """
    Attributes:
        index: ΑΑ γραμμής οντότητας
        invoice_uid: Αναγνωριστικό οντότητας
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης παραστατικού
        classification_mark: Μοναδικός Αριθμός Παραλαβής Χαρακτηρισμού
        cancellation_mark: Μοναδικός Αριθμός Ακύρωσης
        payment_method_mark: Μοναδικός Αριθμός Παραλαβής Τρόπου Πληρωμής
        authentication_code: Συμβολοσειρά Αυθεντικοποίησης Παρόχου
        reception_providers: Πάροχοι Λήπτη
        reception_emails: Email Παραλαβής
        qr_url: QR Code Url
        statement_id: Μοναδικός Αριθμός Δήλωσης
        recall_id: Μοναδικός Κωδικός Καταχώρισης της Ανάκλησης
        transfer_mark: Μοναδικός Αριθμός Εκκίνησης/Μεταφόρτωσης
            Διακίνησης
        reject_mark: Μοναδικός Αριθμός Απόρριψης Διακίνησης
        errors: Λίστα Σφαλμάτων
        status_code: Κωδικός αποτελέσματος
    """

    index: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    invoice_uid: None | str = field(
        default=None,
        metadata={
            "name": "invoiceUid",
            "type": "Element",
        },
    )
    invoice_mark: None | int = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
        },
    )
    classification_mark: None | int = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
        },
    )
    cancellation_mark: None | int = field(
        default=None,
        metadata={
            "name": "cancellationMark",
            "type": "Element",
        },
    )
    payment_method_mark: None | int = field(
        default=None,
        metadata={
            "name": "paymentMethodMark",
            "type": "Element",
        },
    )
    authentication_code: None | str = field(
        default=None,
        metadata={
            "name": "authenticationCode",
            "type": "Element",
        },
    )
    reception_providers: None | ReceptionProvidersType = field(
        default=None,
        metadata={
            "name": "receptionProviders",
            "type": "Element",
        },
    )
    reception_emails: None | ReceptionEmailsType = field(
        default=None,
        metadata={
            "name": "receptionEmails",
            "type": "Element",
        },
    )
    qr_url: None | str = field(
        default=None,
        metadata={
            "name": "qrUrl",
            "type": "Element",
        },
    )
    statement_id: None | str = field(
        default=None,
        metadata={
            "name": "statementId",
            "type": "Element",
        },
    )
    recall_id: None | str = field(
        default=None,
        metadata={
            "name": "recallId",
            "type": "Element",
        },
    )
    transfer_mark: None | str = field(
        default=None,
        metadata={
            "name": "transferMark",
            "type": "Element",
        },
    )
    reject_mark: None | str = field(
        default=None,
        metadata={
            "name": "rejectMark",
            "type": "Element",
        },
    )
    errors: None | ResponseType.Errors = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status_code: str = field(
        metadata={
            "name": "statusCode",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Errors:
        error: list[ErrorType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class ResponseDoc:
    """
    Comment describing your root element.
    """

    response: list[ResponseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
