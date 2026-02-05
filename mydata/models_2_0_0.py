from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime


class DeliveryOutcomeType(Enum):
    FULL = "FULL"
    PARTIAL = "PARTIAL"
    NONE = "NONE"


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
class LocationType:
    """
    Τοποθεσία.

    Attributes:
        longitude: Γεωγραφικό Μήκος
        latitude: Γεωγραφικό Πλάτος
    """

    longitude: Decimal = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    latitude: Decimal = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackagingDetailType:
    """
    Πληροφορίες Συσκευασίας.

    Attributes:
        packaging_type: Είδος Συσκευασίας
        quantity: Πλήθος
        other_packaging_type_title: Τίτλος για Λοιπά Είδη Συσκευασίας
    """

    packaging_type: int = field(
        metadata={
            "name": "packagingType",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
        }
    )
    quantity: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    other_packaging_type_title: None | str = field(
        default=None,
        metadata={
            "name": "otherPackagingTypeTitle",
            "type": "Element",
            "max_length": 150,
        },
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
class RecalledStatementType:
    """
    Attributes:
        statement_id: Μοναδικός Κωδικός Αρχικής Δήλωσης που έχει
            ανακληθεί
        entity_vat_number: ΑΦΜ Υπόχρεης Επιχείρησης
        recall_id: Μοναδικός Κωδικός Καταχώρησης της Ανάκλησης
        recall_status: Κατάσταση Ανάκλησης
        recall_date: Ημερομηνία Πλήρης Ανάκλησης. Συμπληρώνεται από
            Πελάτη
        transaction_date: Ημερομηνία Ανάκλησης Συναλλαγής. Συμπληρώνεται
            από την Υπηρεσία
        recall_vat_number: ΑΦΜ Ανάκλησης Δήλωσης
    """

    statement_id: int = field(
        metadata={
            "name": "statementID",
            "type": "Element",
            "required": True,
        }
    )
    entity_vat_number: str = field(
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "required": True,
        }
    )
    recall_id: int = field(
        metadata={
            "name": "recallId",
            "type": "Element",
            "required": True,
        }
    )
    recall_status: int = field(
        metadata={
            "name": "recallStatus",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
        }
    )
    recall_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "recallDate",
            "type": "Element",
        },
    )
    transaction_date: XmlDate = field(
        metadata={
            "name": "transactionDate",
            "type": "Element",
            "required": True,
        }
    )
    recall_vat_number: str = field(
        metadata={
            "name": "recallVatNumber",
            "type": "Element",
            "required": True,
        }
    )


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


@dataclass(kw_only=True)
class RejectionDetailsType:
    """
    Ένδειξη απόρριψης του παραστατικού διακίνησης από τον παραλήπτη του.
    """

    reason: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Statement:
    """
    Attributes:
        statement_id: Μοναδικός Αριθμός Δήλωσης. Συμπληρώνεται από την
            Υπηρεσία
        submission_date_time: Ημερομηνία υποβολής Δήλωσης. Συμπληρώνεται
            από την Υπηρεσία
        entity_vat_number: ΑΦΜ Υπόχρεης Επιχείρησης
        liable_user_category: Κατηγορία Υπόχρεου
        provider_type: Τύπος Παρόχου
        is_b2_btransactions: Συναλλαγές B2B
        is_b2_ctransactions: Συναλλαγές B2C
        is_b2_gtransactions: Συναλλαγές B2G
        provider_vat_number: ΑΦΜ Παρόχου
        provider_licence_number: Αριθμός Αδείας Παρόχου
        provider_contract_number: Αριθμός Σύμβασης Παρόχου
        provider_contract_conclusion_date: Ημερομηνία σύναψης σύμβασης
            οντότητας με τον Πάροχο
        provider_contract_activation_date: Ημερομηνία έναρξης ισχύος της
            σύμβασης
        issue_start_date: Ημερομηνία έναρξης έκδοσης στοιχειών για
            συναλλαγές
        issue_stop_date: Ημερομηνία διακοπής έκδοσης στοιχείων για
            συναλλαγές
        internet_provider: Παρόχος Διαδικτύου Οντότητας-Εκδότη
        internet_provider_contract_number: Αριθμός Σύμβασης Οντότητας-
            Εκδότη με Πάροχο Διαδικτύου
        internet_provider_contract_date: Ημερομηνία Σύμβασης Οντότητας-
            Εκδότη με Πάροχο Διαδικτύου
    """

    statement_id: None | int = field(
        default=None,
        metadata={
            "name": "statementId",
            "type": "Element",
        },
    )
    submission_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "submissionDateTime",
            "type": "Element",
        },
    )
    entity_vat_number: str = field(
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "required": True,
        }
    )
    liable_user_category: int = field(
        metadata={
            "name": "liableUserCategory",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
        }
    )
    provider_type: int = field(
        metadata={
            "name": "providerType",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
        }
    )
    is_b2_btransactions: None | bool = field(
        default=None,
        metadata={
            "name": "isB2BTransactions",
            "type": "Element",
        },
    )
    is_b2_ctransactions: None | bool = field(
        default=None,
        metadata={
            "name": "isB2CTransactions",
            "type": "Element",
        },
    )
    is_b2_gtransactions: None | bool = field(
        default=None,
        metadata={
            "name": "isB2GTransactions",
            "type": "Element",
        },
    )
    provider_vat_number: str = field(
        metadata={
            "name": "providerVatNumber",
            "type": "Element",
            "required": True,
        }
    )
    provider_licence_number: str = field(
        metadata={
            "name": "providerLicenceNumber",
            "type": "Element",
            "required": True,
        }
    )
    provider_contract_number: str = field(
        metadata={
            "name": "providerContractNumber",
            "type": "Element",
            "required": True,
        }
    )
    provider_contract_conclusion_date: XmlDateTime = field(
        metadata={
            "name": "providerContractConclusionDate",
            "type": "Element",
            "required": True,
        }
    )
    provider_contract_activation_date: XmlDateTime = field(
        metadata={
            "name": "providerContractActivationDate",
            "type": "Element",
            "required": True,
        }
    )
    issue_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "issueStartDate",
            "type": "Element",
        },
    )
    issue_stop_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "issueStopDate",
            "type": "Element",
        },
    )
    internet_provider: None | str = field(
        default=None,
        metadata={
            "name": "internetProvider",
            "type": "Element",
        },
    )
    internet_provider_contract_number: None | str = field(
        default=None,
        metadata={
            "name": "internetProviderContractNumber",
            "type": "Element",
        },
    )
    internet_provider_contract_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "internetProviderContractDate",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ContinuationTokenType2:
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
class AddressType:
    """
    Attributes:
        street:
        number: Αριθμός
        postal_code: ΤΚ
        city:
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    street: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    postal_code: str = field(
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    city: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 150,
        }
    )


@dataclass(kw_only=True)
class CancelledInvoiceType:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης του ακυρωμένου
            Παραστατικού
        cancellation_mark: Μοναδικός Αριθμός Καταχώρησης της Ακύρωσης
        cancellation_date: Ημερομηνία Ακύρωσης Παραστατικού
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    invoice_mark: int = field(
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    cancellation_mark: int = field(
        metadata={
            "name": "cancellationMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    cancellation_date: XmlDate = field(
        metadata={
            "name": "cancellationDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContinuationTokenType1:
    class Meta:
        name = "ContinuationTokenType"
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

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
class EcrtokenType:
    """
    Attributes:
        signing_author: ECR id: Αριθμός μητρώου του φορολογικού
            μηχανισμού
        session_number: Μοναδικός 6-ψήφιος κωδικός που χαρακτηρίζει την
            κάθε συναλλαγή
    """

    class Meta:
        name = "ECRTokenType"
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    signing_author: str = field(
        metadata={
            "name": "SigningAuthor",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 15,
        }
    )
    session_number: str = field(
        metadata={
            "name": "SessionNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "length": 6,
        }
    )


@dataclass(kw_only=True)
class InvoiceE3DetailType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

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
class InvoiceSummaryType:
    """
    Attributes:
        total_net_value: Σύνολο Καθαρής Αξίας
        total_vat_amount: Σύνολο ΦΠΑ
        total_withheld_amount: Σύνολο Παρ. Φόρων
        total_fees_amount: Σύνολο Τελών
        total_stamp_duty_amount: Σύνολο Χαρτοσήμου
        total_other_taxes_amount: Σύνολο Λοιπών Φόρων
        total_deductions_amount: Σύνολο Κρατήσεων
        total_gross_value: Συνολική Αξία
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    total_net_value: str = field(
        metadata={
            "name": "totalNetValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    total_vat_amount: str = field(
        metadata={
            "name": "totalVatAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    total_withheld_amount: str = field(
        metadata={
            "name": "totalWithheldAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    total_fees_amount: str = field(
        metadata={
            "name": "totalFeesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    total_stamp_duty_amount: str = field(
        metadata={
            "name": "totalStampDutyAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    total_other_taxes_amount: str = field(
        metadata={
            "name": "totalOtherTaxesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    total_deductions_amount: str = field(
        metadata={
            "name": "totalDeductionsAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    total_gross_value: str = field(
        metadata={
            "name": "totalGrossValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceVatDetailType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

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
class ProviderSignatureType:
    """
    Attributes:
        signing_author: Provider’s Id
        signature: Υπογραφή
        end_to_nd_reference_id: Το μοναδικό αναγνωριστικό αιτήματος
            πληρωμής (για πληρωμές IRIS)
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    signing_author: str = field(
        metadata={
            "name": "SigningAuthor",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 20,
        }
    )
    signature: str = field(
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    end_to_nd_reference_id: None | str = field(
        default=None,
        metadata={
            "name": "EndToΕndReferenceID",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class ShipType:
    """
    Attributes:
        application_id: Αριθμός Δήλωσης διενέργειας δραστηριότητας
        application_date: Ημερομηνία Δήλωσης
        doy:
        ship_id: Στοιχεία Πλοίου
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    application_id: str = field(
        metadata={
            "name": "applicationId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    application_date: XmlDate = field(
        metadata={
            "name": "applicationDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    doy: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    ship_id: str = field(
        metadata={
            "name": "shipId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxTotalsType:
    """
    Attributes:
        tax_type: Είδος Φόρου
        tax_category: Κατηγορία Φόρου
        underlying_value: Υποκείμενη Αξία
        tax_amount: Ποσό Φόρου
        id:
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    tax_type: int = field(
        metadata={
            "name": "taxType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 5,
        }
    )
    tax_category: None | int = field(
        default=None,
        metadata={
            "name": "taxCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
        },
    )
    underlying_value: None | str = field(
        default=None,
        metadata={
            "name": "underlyingValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tax_amount: str = field(
        metadata={
            "name": "taxAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    id: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class ContinuationTokenType3:
    class Meta:
        name = "continuationTokenType"
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    next_partition_key: str = field(
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    next_row_key: str = field(
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ExpensesClassificationType:
    """
    Attributes:
        classification_type: Κωδικός Χαρακτηρισμού
        classification_category: Κατηγορία Χαρακτηρισμού
        amount: Ποσό Χαρακτηρισμού
        vat_amount: Πόσο Φόρου
        vat_category: Κατηγορία ΦΠΑ
        vat_exemption_category: Κατηγορία Εξαίρεσης ΦΠΑ
        id: Μοναδικός Αριθμός Χαρακτηρισμού
    """

    class Meta:
        target_namespace = (
            "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"
        )

    classification_type: None | str = field(
        default=None,
        metadata={
            "name": "classificationType",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    classification_category: None | str = field(
        default=None,
        metadata={
            "name": "classificationCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    amount: str = field(
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        }
    )
    vat_amount: None | str = field(
        default=None,
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    vat_category: None | str = field(
        default=None,
        metadata={
            "name": "vatCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    vat_exemption_category: None | str = field(
        default=None,
        metadata={
            "name": "vatExemptionCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    id: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )


@dataclass(kw_only=True)
class IncomeClassificationType:
    """
    Attributes:
        classification_type: Κωδικός Χαρακτηρισμού
        classification_category: Κατηγορία Χαρακτηρισμού
        amount: Ποσό Χαρακτηρισμού
        id: Μοναδικός Αριθμός Χαρακτηρισμού
    """

    class Meta:
        target_namespace = (
            "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"
        )

    classification_type: None | str = field(
        default=None,
        metadata={
            "name": "classificationType",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    classification_category: str = field(
        metadata={
            "name": "classificationCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        }
    )
    amount: str = field(
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        }
    )
    id: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )


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
class GenerateGroupQrcodeResponse(GenerateGroupQrcodeResponseType):
    class Meta:
        name = "GenerateGroupQRCodeResponse"


@dataclass(kw_only=True)
class OutcomeDetailsType:
    """
    Λεπτομέρειες της παράδοσης/παραλαβής των αγαθών (από μεταφορέας ή
    παραλήπτη).

    Attributes:
        outcome: Αποτέλεσμα Παράδοσης
        delivered_without_recipient:
        delivered_packaging:
    """

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


@dataclass(kw_only=True)
class PackingsDeclaration:
    """
    Δήλωση Συσκευασιών.

    Attributes:
        packages: Συσκευασίες
    """

    packages: list[PackagingDetailType] = field(
        default_factory=list,
        metadata={
            "name": "Packages",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RequestedProviderDoc:
    """
    Παραστατικά από Πάροχο.
    """

    continuation_token: list[ContinuationTokenType2] = field(
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


@dataclass(kw_only=True)
class RequestedStatement:
    """
    Attributes:
        statement:
        accept_vat_number: ΑΦΜ αποδοχής δήλωσης (αφορά Υπόχρεη
            Επιχείρηση)
        accept_date: Ημερομηνία αποδοχής δήλωσης από Υπόχρεη Επιχείρηση.
            Συμπληρώνεται από την Υπηρεσία
        recall_statement:
    """

    statement: None | Statement = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    accept_vat_number: None | str = field(
        default=None,
        metadata={
            "name": "acceptVatNumber",
            "type": "Element",
        },
    )
    accept_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "acceptDate",
            "type": "Element",
        },
    )
    recall_statement: None | RecalledStatementType = field(
        default=None,
        metadata={
            "name": "recallStatement",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class StatementDoc:
    """
    Δήλωση έκδοσης στοιχείων μέσω Παρόχου ή ΙδιοΠαρόχου.
    """

    statement: Statement = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TransportDetailType:
    """
    Attributes:
        vehicle_number: Αριθμός Μεταφορικού Μέσου (Αριθμός
            κυκλοφορίας/Όνομα πλωτού μέσου/Κωδικός Δρομολογίου ή
            πτήσης/Διακίνηση άνευ Μεταφορικού Μέσου)
        transport_type: Είδος Μεταφορικού Μέσου
        time_stamp: Χρονοσφραγίδα
        carrier_vat_number: ΑΦΜ Μεταφορικής Εταιρείας
        p_number: Αριθμός κυκλοφορίας "Ρ" (αριθμός κυκλοφορίας του
            επικαθήμενου/ρυμουλκούμενου οχήματος)
        location: Τοποθεσία Μεταφόρτωσης
    """

    vehicle_number: str = field(
        metadata={
            "name": "vehicleNumber",
            "type": "Element",
            "required": True,
            "max_length": 50,
        }
    )
    transport_type: int = field(
        metadata={
            "name": "transportType",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
        }
    )
    time_stamp: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
        },
    )
    carrier_vat_number: str = field(
        metadata={
            "name": "carrierVatNumber",
            "type": "Element",
            "required": True,
            "max_length": 20,
        }
    )
    p_number: None | str = field(
        default=None,
        metadata={
            "name": "pNumber",
            "type": "Element",
            "max_length": 50,
        },
    )
    location: None | LocationType = field(
        default=None,
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
class InvoiceRowType:
    """
    Attributes:
        line_number: ΑΑ Γραμμής
        rec_type: Είδος Γραμμής
        taric_no: Κωδικός Taric
        item_code: Κωδικός Είδους
        item_descr: Περιγραφή Είδους
        fuel_code: Κωδικός Καυσίμου
        quantity: Ποσότητα
        measurement_unit: Είδος Ποσότητας
        invoice_detail_type: Επισήμανση
        net_value: Καθαρή Αξία
        vat_category: Κατηγορία ΦΠΑ
        vat_amount: Ποσό ΦΠΑ
        vat_exemption_category: Κατηγορία Αιτίας Εξαίρεσης ΦΠΑ
        dienergia: ΠΟΛ 1177/2018 Αρ. 27
        discount_option: Δικαίωμα Έκπτωσης
        withheld_amount: Ποσό Παρ. Φόρου
        withheld_percent_category: Κατηγορία Συντελεστή  Παρ. Φόρου
        stamp_duty_amount: Ποσό Ψηφιακού Τέλους συναλλαγής
        stamp_duty_percent_category: Κατηγορία Συντελεστή Ψηφιακού
            Τέλους συναλλαγής
        fees_amount: Ποσό Τελών
        fees_percent_category: Κατηγορία Συντελεστή Τελών
        other_taxes_percent_category: Κατηγορία Συντελεστή Λοιπών Φόρων
        other_taxes_amount: Ποσό Φόρου Διαμονης
        deductions_amount: Ποσό Κρατήσεων
        line_comments: Σχόλια Γραμμής
        quantity15: Ποσότητα Θερμοκρασίας 15 βαθμών
        other_measurement_unit_quantity: Πλήθος Μονάδας Μέτρησης Τεμάχια
            Άλλα
        other_measurement_unit_title: Τίτλος Μονάδας Μέτρησης Τεμάχια
            Άλλα
        not_vat195: Ένδειξη μη συμμετοχής στο ΦΠΑ (έσοδα – εκροές)
        move_purpose_line: Σκοπός Διακίνησης Γραμμής
        other_move_purpose_line_title: Τίτλος της Λοιπής Αιτίας
            Διακίνησης Γραμμής
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    line_number: int = field(
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
        }
    )
    rec_type: None | int = field(
        default=None,
        metadata={
            "name": "recType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 7,
        },
    )
    taric_no: None | str = field(
        default=None,
        metadata={
            "name": "TaricNo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "length": 10,
        },
    )
    item_code: str = field(
        metadata={
            "name": "itemCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        }
    )
    item_descr: str = field(
        metadata={
            "name": "itemDescr",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 300,
        }
    )
    fuel_code: None | str = field(
        default=None,
        metadata={
            "name": "fuelCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    quantity: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
        },
    )
    measurement_unit: None | str = field(
        default=None,
        metadata={
            "name": "measurementUnit",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_detail_type: None | str = field(
        default=None,
        metadata={
            "name": "invoiceDetailType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    net_value: str = field(
        metadata={
            "name": "netValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    vat_category: str = field(
        metadata={
            "name": "vatCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    vat_amount: str = field(
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    vat_exemption_category: None | str = field(
        default=None,
        metadata={
            "name": "vatExemptionCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dienergia: None | ShipType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    discount_option: None | bool = field(
        default=None,
        metadata={
            "name": "discountOption",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    withheld_amount: None | str = field(
        default=None,
        metadata={
            "name": "withheldAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    withheld_percent_category: None | str = field(
        default=None,
        metadata={
            "name": "withheldPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    stamp_duty_amount: None | str = field(
        default=None,
        metadata={
            "name": "stampDutyAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    stamp_duty_percent_category: None | str = field(
        default=None,
        metadata={
            "name": "stampDutyPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    fees_amount: None | str = field(
        default=None,
        metadata={
            "name": "feesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    fees_percent_category: None | str = field(
        default=None,
        metadata={
            "name": "feesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_taxes_percent_category: None | str = field(
        default=None,
        metadata={
            "name": "otherTaxesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_taxes_amount: None | str = field(
        default=None,
        metadata={
            "name": "otherTaxesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    deductions_amount: None | str = field(
        default=None,
        metadata={
            "name": "deductionsAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    line_comments: None | str = field(
        default=None,
        metadata={
            "name": "lineComments",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    quantity15: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
        },
    )
    other_measurement_unit_quantity: None | int = field(
        default=None,
        metadata={
            "name": "otherMeasurementUnitQuantity",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_measurement_unit_title: None | str = field(
        default=None,
        metadata={
            "name": "otherMeasurementUnitTitle",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    not_vat195: None | bool = field(
        default=None,
        metadata={
            "name": "notVAT195",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    move_purpose_line: None | int = field(
        default=None,
        metadata={
            "name": "movePurposeLine",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 20,
        },
    )
    other_move_purpose_line_title: None | str = field(
        default=None,
        metadata={
            "name": "otherMovePurposeLineTitle",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )


@dataclass(kw_only=True)
class OtherDeliveryNoteHeaderType:
    """
    Attributes:
        loading_address: Διεύθυνση Φόρτωσης
        delivery_address: Διεύθυνση Παράδοσης
        start_shipping_branch: Εγκατάσταση έναρξης διακίνησης (Εκδότη)
        complete_shipping_branch: Εγκατάσταση ολοκλήρωσης διακίνησης
            (Λήπτη)
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    loading_address: AddressType = field(
        metadata={
            "name": "loadingAddress",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    delivery_address: AddressType = field(
        metadata={
            "name": "deliveryAddress",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    start_shipping_branch: None | int = field(
        default=None,
        metadata={
            "name": "startShippingBranch",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    complete_shipping_branch: None | int = field(
        default=None,
        metadata={
            "name": "completeShippingBranch",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class PartyType:
    """
    Attributes:
        vat_number:
        country: Κωδ. Χώρας
        branch: Αρ. Εγκατάστασης
        name:
        address: Διεύθυνση
        document_id_no:
        supply_account_no: Αρ. Παροχής Ηλ. Ρεύματος
        country_document_id: Κωδ. Χώρας Έκδοσης Επίσημου Εγγράφου
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    vat_number: str = field(
        metadata={
            "name": "vatNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 30,
        }
    )
    country: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    branch: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 200,
        },
    )
    address: None | AddressType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    document_id_no: None | str = field(
        default=None,
        metadata={
            "name": "documentIdNo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 100,
        },
    )
    supply_account_no: None | str = field(
        default=None,
        metadata={
            "name": "supplyAccountNo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 100,
        },
    )
    country_document_id: None | str = field(
        default=None,
        metadata={
            "name": "countryDocumentId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class PaymentMethodDetailType:
    """
    Attributes:
        type_value: Τύπος Πληρωμής
        amount: Αναλογούν Ποσό
        payment_method_info: Λοιπές Πληροφορίες
        tip_amount: Φιλοδώρημα
        transaction_id: Μοναδική Ταυτότητα Πληρωμής
        tid: tid POS
        providers_signature: Υπογραφή Πληρωμής Παρόχου
        ecrtoken: Υπογραφή Πληρωμής ΦΗΜ με σύστημα λογισμικού (ERP)
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    type_value: int = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 8,
        }
    )
    amount: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    payment_method_info: None | str = field(
        default=None,
        metadata={
            "name": "paymentMethodInfo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tip_amount: None | str = field(
        default=None,
        metadata={
            "name": "tipAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    transaction_id: None | str = field(
        default=None,
        metadata={
            "name": "transactionId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 200,
        },
    )
    providers_signature: None | ProviderSignatureType = field(
        default=None,
        metadata={
            "name": "ProvidersSignature",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    ecrtoken: None | EcrtokenType = field(
        default=None,
        metadata={
            "name": "ECRToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class RequestedE3InfoType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

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
class RequestedVatInfoType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

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
class InvoicesExpensesClassificationDetailType:
    """
    Attributes:
        line_number: Γραμμή Παραστατικού
        expenses_classification_detail_data: Λίστα Χαρακτηρισμών Εσόδων
    """

    class Meta:
        target_namespace = (
            "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"
        )

    line_number: int = field(
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        }
    )
    expenses_classification_detail_data: list[ExpensesClassificationType] = (
        field(
            default_factory=list,
            metadata={
                "name": "expensesClassificationDetailData",
                "type": "Element",
                "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
                "min_occurs": 1,
            },
        )
    )


@dataclass(kw_only=True)
class InvoicesIncomeClassificationDetailType:
    """
    Attributes:
        line_number: Γραμμή Παραστατικού
        income_classification_detail_data: Λίστα Χαρακτηρισμών Εσόδων
    """

    class Meta:
        target_namespace = (
            "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"
        )

    line_number: int = field(
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        }
    )
    income_classification_detail_data: list[IncomeClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "incomeClassificationDetailData",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class DeliveryEventType:
    """
    Ένα γεγονός (σταθμός) στον κύκλο ζωής (lifecycle) παράδοσης του δελτίου
    διακίνησης.

    Attributes:
        event_type: Ο τύπος του Συμβάντος (e.g., "RegisterTransfer",
            "ConfirmOutcome", "Rejection").
        event_timestamp: Χρονοσφραγίδα συμβάντος
        actor_vat: ΑΦΜ Χρήστη που δημιούργησε το συμβάν.
        mark: Μοναδικός Αριθμός Καταχώρησης Συμβάντος (παράγεται από το
            myDATA)
        transport_details: Λεπτομέρειες Εκκίνησης Διακίνησης -
            Μεταφορτώσεις Διακίνησης
        outcome_details: Λεπτομέρειες της παράδοσης/παραλαβής των αγαθών
            (από μεταφορέας ή παραλήπτη)
        rejection_details: Ένδειξη απόρριψης του παραστατικού διακίνησης
            από τον παραλήπτη του
    """

    event_type: str = field(
        metadata={
            "name": "eventType",
            "type": "Element",
            "required": True,
        }
    )
    event_timestamp: XmlDateTime = field(
        metadata={
            "name": "eventTimestamp",
            "type": "Element",
            "required": True,
        }
    )
    actor_vat: str = field(
        metadata={
            "name": "actorVat",
            "type": "Element",
            "required": True,
        }
    )
    mark: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    transport_details: None | TransportDetailType = field(
        default=None,
        metadata={
            "name": "transportDetails",
            "type": "Element",
        },
    )
    outcome_details: None | OutcomeDetailsType = field(
        default=None,
        metadata={
            "name": "outcomeDetails",
            "type": "Element",
        },
    )
    rejection_details: None | RejectionDetailsType = field(
        default=None,
        metadata={
            "name": "rejectionDetails",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class GenerateGroupQrcodeRequest(GenerateGroupQrcodeRequestType):
    class Meta:
        name = "GenerateGroupQRCodeRequest"


@dataclass(kw_only=True)
class RequestedStatementDoc:
    """
    Δηλώσεις έκδοσης στοιχείων μέσω Παρόχου ή ΙδιοΠαρόχου.
    """

    requested_statement: list[RequestedStatement] = field(
        default_factory=list,
        metadata={
            "name": "requestedStatement",
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


@dataclass(kw_only=True)
class EntityType:
    """
    Attributes:
        type_value: Κατηγορία
        entity_data: Στοιχεία Οντότητας
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    type_value: int = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
        }
    )
    entity_data: PartyType = field(
        metadata={
            "name": "entityData",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestedE3Info(RequestedE3InfoType):
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass(kw_only=True)
class RequestedVatInfo(RequestedVatInfoType):
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass(kw_only=True)
class InvoiceExpensesClassificationType:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης Παραστατικού
        classification_mark: Αποδεικτικό Λήψης Χαρακτηρισμού Εξόδων.
            Συμπληρώνεται από την Υπηρεσία
        entity_vat_number: ΑΦΜ Οντότητας Αναφοράς
        transaction_mode: Αιτιολογία Συναλλαγής
        invoices_expenses_classification_details:
        classification_post_mode: Μέθοδος Υποβολής Χαρακτηρισμού
    """

    class Meta:
        target_namespace = (
            "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"
        )

    invoice_mark: int = field(
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        }
    )
    classification_mark: None | int = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    entity_vat_number: None | str = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    transaction_mode: None | int = field(
        default=None,
        metadata={
            "name": "transactionMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    invoices_expenses_classification_details: list[
        InvoicesExpensesClassificationDetailType
    ] = field(
        default_factory=list,
        metadata={
            "name": "invoicesExpensesClassificationDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    classification_post_mode: None | int = field(
        default=None,
        metadata={
            "name": "classificationPostMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 0,
            "max_inclusive": 1,
        },
    )


@dataclass(kw_only=True)
class InvoiceIncomeClassificationType:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης Παραστατικού
        classification_mark: Αποδεικτικό Λήψης Χαρακτηρισμού Εσόδων.
            Συμπληρώνεται από την Υπηρεσία
        entity_vat_number: ΑΦΜ Οντότητας Αναφοράς
        transaction_mode: Αιτιολογία Συναλλαγής
        invoices_income_classification_details:
    """

    class Meta:
        target_namespace = (
            "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"
        )

    invoice_mark: int = field(
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        }
    )
    classification_mark: None | int = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    entity_vat_number: None | str = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    transaction_mode: None | int = field(
        default=None,
        metadata={
            "name": "transactionMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    invoices_income_classification_details: list[
        InvoicesIncomeClassificationDetailType
    ] = field(
        default_factory=list,
        metadata={
            "name": "invoicesIncomeClassificationDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )


@dataclass(kw_only=True)
class PaymentMethodType:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης Παραστατικού
        payment_method_mark: Αποδεικτικό Λήψης Τρόπων Πληρωμής.
            Συμπληρώνεται από την Υπηρεσία
        entity_vat_number: ΑΦΜ Οντότητας Αναφοράς
        payment_method_details:
    """

    class Meta:
        target_namespace = "https://www.aade.gr/myDATA/paymentMethod/v1.0"

    invoice_mark: int = field(
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
            "required": True,
        }
    )
    payment_method_mark: None | int = field(
        default=None,
        metadata={
            "name": "paymentMethodMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
        },
    )
    entity_vat_number: None | str = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
        },
    )
    payment_method_details: list[PaymentMethodDetailType] = field(
        default_factory=list,
        metadata={
            "name": "paymentMethodDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
            "min_occurs": 1,
        },
    )


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


@dataclass(kw_only=True)
class InvoiceHeaderType:
    """
    Attributes:
        series: Σειρά Παραστατικού
        aa: ΑΑ Παραστατικού
        issue_date: Ημερομηνία Έκδοσης
        invoice_type: Είδος Παραστατικού
        vat_payment_suspension: Αναστολή Καταβολής ΦΠΑ
        currency: Νόμισμα
        exchange_rate: Ισοτιμία
        correlated_invoices: Συσχετιζόμενα Παραστατικά
        self_pricing: Ένδειξη Αυτοτιμολόγησης
        dispatch_date: Ημερομηνία  Έναρξης Αποστολής (Προγραμματισμένη -
            Σχεδιασμένη - Εκτιμώμενη)
        dispatch_time: Ώρα Έναρξης Αποστολής (Προγραμματισμένη -
            Σχεδιασμένη - Εκτιμώμενη)
        vehicle_number: Αριθμός Οχήματος (Προγραμματισμένο -
            Σχεδιασμένο)
        move_purpose: Σκοπός Διακίνησης
        fuel_invoice: Παραστατικό Καυσίμων
        special_invoice_category: Ειδική Κατηγορία Παραστατικού
        invoice_variation_type: Τύπος Απόκλισης Παραστατικού
        other_correlated_entities: Λοιπές συσχετιζόμενες οντοτήτες
        other_delivery_note_header: Λοιπά Γενικά Στοιχεία Διακίνησης
        is_delivery_note: Ένδειξη Παραστατικού Διακίνησης
        other_move_purpose_title: Τίτλος της Λοιπής Αιτίας Διακίνησης
        third_party_collection: Ένδειξη Εισπράξης Τρίτων
        multiple_connected_marks: Πολλαπλά Συνδεόμενα MARKs
        table_aa: AA ΤΡΑΠΕΖΙOY (για Δελτία Παραγγελίας Εστίασης)
        total_cancel_delivery_orders: Ένδειξη συνολικής αναίρεσης
            Δελτίων Παραγελίας
        reverse_delivery_note: Αντίστροφη Διακίνηση
        reverse_delivery_note_purpose: Αιτία Έκδοσης Αντίστροφης
            Διακίνησης
        to_weigh: Ένδειξη Προς Ζύγιση
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    series: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        }
    )
    aa: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        }
    )
    issue_date: XmlDate = field(
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    invoice_type: str = field(
        metadata={
            "name": "invoiceType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    vat_payment_suspension: None | bool = field(
        default=None,
        metadata={
            "name": "vatPaymentSuspension",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    exchange_rate: None | str = field(
        default=None,
        metadata={
            "name": "exchangeRate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    correlated_invoices: list[int] = field(
        default_factory=list,
        metadata={
            "name": "correlatedInvoices",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    self_pricing: None | bool = field(
        default=None,
        metadata={
            "name": "selfPricing",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dispatch_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "dispatchDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dispatch_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "dispatchTime",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vehicle_number: None | str = field(
        default=None,
        metadata={
            "name": "vehicleNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    move_purpose: None | int = field(
        default=None,
        metadata={
            "name": "movePurpose",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 20,
        },
    )
    fuel_invoice: None | bool = field(
        default=None,
        metadata={
            "name": "fuelInvoice",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    special_invoice_category: None | str = field(
        default=None,
        metadata={
            "name": "specialInvoiceCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_variation_type: None | str = field(
        default=None,
        metadata={
            "name": "invoiceVariationType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_correlated_entities: list[EntityType] = field(
        default_factory=list,
        metadata={
            "name": "otherCorrelatedEntities",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_delivery_note_header: None | OtherDeliveryNoteHeaderType = field(
        default=None,
        metadata={
            "name": "otherDeliveryNoteHeader",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    is_delivery_note: None | bool = field(
        default=None,
        metadata={
            "name": "isDeliveryNote",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_move_purpose_title: None | str = field(
        default=None,
        metadata={
            "name": "otherMovePurposeTitle",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    third_party_collection: None | bool = field(
        default=None,
        metadata={
            "name": "thirdPartyCollection",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    multiple_connected_marks: list[int] = field(
        default_factory=list,
        metadata={
            "name": "multipleConnectedMarks",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    table_aa: None | str = field(
        default=None,
        metadata={
            "name": "tableAA",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 50,
        },
    )
    total_cancel_delivery_orders: None | bool = field(
        default=None,
        metadata={
            "name": "totalCancelDeliveryOrders",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    reverse_delivery_note: None | bool = field(
        default=None,
        metadata={
            "name": "reverseDeliveryNote",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    reverse_delivery_note_purpose: None | str = field(
        default=None,
        metadata={
            "name": "reverseDeliveryNotePurpose",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    to_weigh: None | bool = field(
        default=None,
        metadata={
            "name": "toWeigh",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass(kw_only=True)
class ExpensesClassificationsDoc:
    """
    Χαρατηρισμοί Εξόδων Πρότυπων Παραστατικών ΑΑΔΕ.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"

    expenses_invoice_classification: list[
        InvoiceExpensesClassificationType
    ] = field(
        default_factory=list,
        metadata={
            "name": "expensesInvoiceClassification",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class IncomeClassificationsDoc:
    """
    Χαρατηρισμοί Εσόδων Πρότυπων Παραστατικών ΑΑΔΕ.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"

    income_invoice_classification: list[InvoiceIncomeClassificationType] = (
        field(
            default_factory=list,
            metadata={
                "name": "incomeInvoiceClassification",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )


@dataclass(kw_only=True)
class PaymentMethodsDoc:
    """
    Μέθοδοι Πληρωμής.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/paymentMethod/v1.0"

    payment_methods: list[PaymentMethodType] = field(
        default_factory=list,
        metadata={
            "name": "paymentMethods",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class GetDeliveryNoteStatusResponse(GetDeliveryNoteStatusResponseType):
    pass


@dataclass(kw_only=True)
class AadeBookInvoiceType:
    """
    Attributes:
        uid: Αναγνωριστικό Παραστατικού
        mark: Μοναδικός Αριθμός Καταχώρησης Παραστατικού
        cancelled_by_mark: Μοναδικός Αριθμός Καταχώρησης Ακυρωτικού
        authentication_code: Συμβολοσειρά Αυθεντικοποίησης Παρόχου
        transmission_failure: Αδυναμία Επικοινωνίας Παρόχου ή Αδυναμία
            διαβίβασης ERP ή διαβίβαση μέσω Παρόχου για τις οντότητες
            άρθρου 5, 2η παράγραφος της περ. 1γ
        issuer: Στοιχεία Εκδότη
        counterpart: Στοιχεία Λήπτη
        invoice_header: Γενικά Στοιχεία
        payment_methods: Πληρωμές
        invoice_details: Λεπτομέρειες Παραστατικού
        taxes_totals: Σύνολα Φόρων
        invoice_summary: Συγκεντρωτικά Στοιχεία
        qr_code_url: QR Code Url
        downloading_invoice_url: Url με το οποίο ο λήπτης του
            παραστατικού θα μπορεί να το λαμβάνει
        packings_declarations: Δηλώσεις Συσκευασιών
        invoive_delivery_status: Κατάσταση (Status) Παραστατικού Δελτίου
            Διακίνησης
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    uid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    mark: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    cancelled_by_mark: None | int = field(
        default=None,
        metadata={
            "name": "cancelledByMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    authentication_code: None | str = field(
        default=None,
        metadata={
            "name": "authenticationCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    transmission_failure: None | int = field(
        default=None,
        metadata={
            "name": "transmissionFailure",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 4,
        },
    )
    issuer: None | PartyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    counterpart: None | PartyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_header: InvoiceHeaderType = field(
        metadata={
            "name": "invoiceHeader",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    payment_methods: None | AadeBookInvoiceType.PaymentMethods = field(
        default=None,
        metadata={
            "name": "paymentMethods",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_details: list[InvoiceRowType] = field(
        default_factory=list,
        metadata={
            "name": "invoiceDetails",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_occurs": 1,
        },
    )
    taxes_totals: None | AadeBookInvoiceType.TaxesTotals = field(
        default=None,
        metadata={
            "name": "taxesTotals",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_summary: InvoiceSummaryType = field(
        metadata={
            "name": "invoiceSummary",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        }
    )
    qr_code_url: None | str = field(
        default=None,
        metadata={
            "name": "qrCodeUrl",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    downloading_invoice_url: None | str = field(
        default=None,
        metadata={
            "name": "downloadingInvoiceUrl",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    packings_declarations: list[str] = field(
        default_factory=list,
        metadata={
            "name": "packingsDeclarations",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoive_delivery_status: None | int = field(
        default=None,
        metadata={
            "name": "invoiveDeliveryStatus",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 7,
        },
    )

    @dataclass(kw_only=True)
    class PaymentMethods:
        """
        Attributes:
            payment_method_details: Στοιχεία Πληρωμών
        """

        payment_method_details: list[PaymentMethodDetailType] = field(
            default_factory=list,
            metadata={
                "name": "paymentMethodDetails",
                "type": "Element",
                "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class TaxesTotals:
        taxes: list[TaxTotalsType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class InvoicesDoc:
    """
    Παραστατικό ΑΑΔΕ.
    """

    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    invoice: AadeBookInvoiceType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestedDoc:
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    continuation_token: None | ContinuationTokenType3 = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
        },
    )
    invoices_doc: None | RequestedDoc.InvoicesDoc = field(
        default=None,
        metadata={
            "name": "invoicesDoc",
            "type": "Element",
        },
    )
    cancelled_invoices_doc: None | RequestedDoc.CancelledInvoicesDoc = field(
        default=None,
        metadata={
            "name": "cancelledInvoicesDoc",
            "type": "Element",
        },
    )
    income_classifications_doc: (
        None | RequestedDoc.IncomeClassificationsDoc
    ) = field(
        default=None,
        metadata={
            "name": "incomeClassificationsDoc",
            "type": "Element",
        },
    )
    expenses_classifications_doc: (
        None | RequestedDoc.ExpensesClassificationsDoc
    ) = field(
        default=None,
        metadata={
            "name": "expensesClassificationsDoc",
            "type": "Element",
        },
    )
    payment_methods_doc: None | RequestedDoc.PaymentMethodsDoc = field(
        default=None,
        metadata={
            "name": "paymentMethodsDoc",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class InvoicesDoc:
        invoice: list[AadeBookInvoiceType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class CancelledInvoicesDoc:
        cancelled_invoice: list[CancelledInvoiceType] = field(
            default_factory=list,
            metadata={
                "name": "cancelledInvoice",
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class IncomeClassificationsDoc:
        income_invoice_classification: list[
            InvoiceIncomeClassificationType
        ] = field(
            default_factory=list,
            metadata={
                "name": "incomeInvoiceClassification",
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class ExpensesClassificationsDoc:
        expenses_invoice_classification: list[
            InvoiceExpensesClassificationType
        ] = field(
            default_factory=list,
            metadata={
                "name": "expensesInvoiceClassification",
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class PaymentMethodsDoc:
        payment_methods: list[PaymentMethodType] = field(
            default_factory=list,
            metadata={
                "name": "paymentMethods",
                "type": "Element",
            },
        )
