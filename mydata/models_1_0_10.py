from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime


@dataclass
class ErrorType:
    """
    Attributes:
        message: Μήνυμα Σφάλματος
        code: Κωδικός Σφάλαματος
    """

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
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

    issuer_vat: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerVAT",
            "type": "Element",
            "required": True,
        },
    )
    invoice_provider_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceProviderMark",
            "type": "Element",
            "required": True,
        },
    )
    invoice_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceUid",
            "type": "Element",
            "required": True,
        },
    )
    authentication_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authenticationCode",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ProviderInfoType:
    """
    Attributes:
        vatnumber: ΑΦΜ
    """

    vatnumber: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VATNumber",
            "type": "Element",
        },
    )


@dataclass
class ContinuationTokenType2:
    class Meta:
        name = "continuationTokenType"

    next_partition_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "required": True,
        },
    )
    next_row_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ReceptionEmailsType:
    """
    Attributes:
        email: Email
    """

    class Meta:
        name = "receptionEmailsType"

    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
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

    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 150,
        },
    )


@dataclass
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

    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    cancellation_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "cancellationMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    cancellation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "cancellationDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )


@dataclass
class ContinuationTokenType1:
    class Meta:
        name = "ContinuationTokenType"
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    next_partition_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    next_row_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
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

    signing_author: Optional[str] = field(
        default=None,
        metadata={
            "name": "SigningAuthor",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 15,
        },
    )
    session_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SessionNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "length": 6,
        },
    )


@dataclass
class InvoiceE3DetailType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    v_afm: Optional[str] = field(
        default=None,
        metadata={
            "name": "V_Afm",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_mark: Optional[str] = field(
        default=None,
        metadata={
            "name": "V_Mark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_book: Optional[str] = field(
        default=None,
        metadata={
            "name": "vBook",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    is_cancelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCancelled",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    v_class_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "V_Class_Category",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_class_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "V_Class_Type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    v_class_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "V_Class_Value",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
class InvoiceVatDetailType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    mark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    is_cancelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCancelled",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    vat301: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat301",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat302: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat302",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat303: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat303",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat304: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat304",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat305: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat305",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat306: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat306",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat331: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat331",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat332: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat332",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat333: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat333",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat334: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat334",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat335: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat335",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat336: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat336",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat361: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat361",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat362: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat362",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat363: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat363",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat364: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat364",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat365: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat365",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat366: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat366",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat381: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat381",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat382: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat382",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat383: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat383",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat384: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat384",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat385: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat385",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat386: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat386",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat342: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat342",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat345: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat345",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat348: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat348",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat349: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat349",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat310: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat310",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat402: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat402",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat407: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat407",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat411: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat411",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat423: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat423",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat422: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vat422",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat_unclassified361: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VatUnclassified361",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat_unclassified381: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VatUnclassified381",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
class ProviderSignatureType:
    """
    Attributes:
        signing_author: Provider’s Id
        signature: Υπογραφή
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    signing_author: Optional[str] = field(
        default=None,
        metadata={
            "name": "SigningAuthor",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 20,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )


@dataclass
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

    application_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    application_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "applicationDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    doy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    ship_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )


@dataclass
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

    tax_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "taxType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 5,
        },
    )
    tax_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "taxCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
        },
    )
    underlying_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "underlyingValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tax_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
class TransportDetailType:
    """
    Attributes:
        vehicle_number: Αριθμός Μεταφορικού Μέσου
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    vehicle_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        },
    )


@dataclass
class ContinuationTokenType3:
    class Meta:
        name = "continuationTokenType"
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    next_partition_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    next_row_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )


@dataclass
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

    classification_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "classificationType",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    classification_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "classificationCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        },
    )
    vat_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    vat_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    vat_exemption_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatExemptionCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )


class IncomeClassificationCategoryType(Enum):
    CATEGORY1_1 = "category1_1"
    CATEGORY1_2 = "category1_2"
    CATEGORY1_3 = "category1_3"
    CATEGORY1_4 = "category1_4"
    CATEGORY1_5 = "category1_5"
    CATEGORY1_6 = "category1_6"
    CATEGORY1_7 = "category1_7"
    CATEGORY1_8 = "category1_8"
    CATEGORY1_9 = "category1_9"
    CATEGORY1_10 = "category1_10"
    CATEGORY1_95 = "category1_95"
    CATEGORY3 = "category3"


class IncomeClassificationValueType(Enum):
    E3_106 = "E3_106"
    E3_205 = "E3_205"
    E3_210 = "E3_210"
    E3_305 = "E3_305"
    E3_310 = "E3_310"
    E3_318 = "E3_318"
    E3_561_001 = "E3_561_001"
    E3_561_002 = "E3_561_002"
    E3_561_003 = "E3_561_003"
    E3_561_004 = "E3_561_004"
    E3_561_005 = "E3_561_005"
    E3_561_006 = "E3_561_006"
    E3_561_007 = "E3_561_007"
    E3_562 = "E3_562"
    E3_563 = "E3_563"
    E3_564 = "E3_564"
    E3_565 = "E3_565"
    E3_566 = "E3_566"
    E3_567 = "E3_567"
    E3_568 = "E3_568"
    E3_570 = "E3_570"
    E3_595 = "E3_595"
    E3_596 = "E3_596"
    E3_597 = "E3_597"
    E3_880_001 = "E3_880_001"
    E3_880_002 = "E3_880_002"
    E3_880_003 = "E3_880_003"
    E3_880_004 = "E3_880_004"
    E3_881_001 = "E3_881_001"
    E3_881_002 = "E3_881_002"
    E3_881_003 = "E3_881_003"
    E3_881_004 = "E3_881_004"
    E3_598_001 = "E3_598_001"
    E3_598_003 = "E3_598_003"


@dataclass
class RequestedProviderDoc:
    """
    Παραστατικά από Πάροχο.
    """

    continuation_token: List[ContinuationTokenType2] = field(
        default_factory=list,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "sequence": 1,
        },
    )
    invoice_provider_type: List[InvoiceProviderType] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceProviderType",
            "type": "Element",
            "sequence": 1,
        },
    )


@dataclass
class ReceptionProvidersType:
    """
    Attributes:
        provider_info: Πληροφορίες Παρόχου
    """

    class Meta:
        name = "receptionProvidersType"

    provider_info: List[ProviderInfoType] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
        },
    )


@dataclass
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

    loading_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "loadingAddress",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    delivery_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "deliveryAddress",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    start_shipping_branch: Optional[int] = field(
        default=None,
        metadata={
            "name": "startShippingBranch",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    complete_shipping_branch: Optional[int] = field(
        default=None,
        metadata={
            "name": "completeShippingBranch",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
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

    vat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 30,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    branch: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 200,
        },
    )
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    document_id_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentIdNo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 100,
        },
    )
    supply_account_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "supplyAccountNo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 100,
        },
    )
    country_document_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryDocumentId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
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

    type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 8,
        },
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    payment_method_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "paymentMethodInfo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tip_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "tipAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "transactionId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 200,
        },
    )
    providers_signature: Optional[ProviderSignatureType] = field(
        default=None,
        metadata={
            "name": "ProvidersSignature",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    ecrtoken: Optional[EcrtokenType] = field(
        default=None,
        metadata={
            "name": "ECRToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
class RequestedE3InfoType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    continuation_token: Optional[ContinuationTokenType1] = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    e3_info: List[InvoiceE3DetailType] = field(
        default_factory=list,
        metadata={
            "name": "E3Info",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
class RequestedVatInfoType:
    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    continuation_token: Optional[ContinuationTokenType1] = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat_info: List[InvoiceVatDetailType] = field(
        default_factory=list,
        metadata={
            "name": "VatInfo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
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

    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        },
    )
    expenses_classification_detail_data: List[ExpensesClassificationType] = (
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


@dataclass
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

    classification_type: Optional[IncomeClassificationValueType] = field(
        default=None,
        metadata={
            "name": "classificationType",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    classification_category: Optional[IncomeClassificationCategoryType] = (
        field(
            default=None,
            metadata={
                "name": "classificationCategory",
                "type": "Element",
                "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
                "required": True,
            },
        )
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )


@dataclass
class ResponseType:
    """
    Attributes:
        index: ΑΑ γραμμής οντότητας
        invoice_uid: Αναγνωριστικό οντότητας
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης παραστατικού
        qr_url: QR Code Url
        classification_mark: Μοναδικός Αριθμός Παραλαβής Χαρακτηρισμού
        cancellation_mark: Μοναδικός Αριθμός Ακύρωσης
        payment_method_mark: Μοναδικός Αριθμός Παραλαβής Τρόπου Πληρωμής
        authentication_code: Συμβολοσειρά Αυθεντικοποίησης Παρόχου
        reception_providers: Πάροχοι Λήπτη
        reception_emails: Email Παραλαβής
        errors: Λίστα Σφαλμάτων
        status_code: Κωδικός αποτελέσματος
    """

    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    invoice_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceUid",
            "type": "Element",
        },
    )
    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
        },
    )
    qr_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "qrUrl",
            "type": "Element",
        },
    )
    classification_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
        },
    )
    cancellation_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "cancellationMark",
            "type": "Element",
        },
    )
    payment_method_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "paymentMethodMark",
            "type": "Element",
        },
    )
    authentication_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authenticationCode",
            "type": "Element",
        },
    )
    reception_providers: Optional[ReceptionProvidersType] = field(
        default=None,
        metadata={
            "name": "receptionProviders",
            "type": "Element",
        },
    )
    reception_emails: Optional[ReceptionEmailsType] = field(
        default=None,
        metadata={
            "name": "receptionEmails",
            "type": "Element",
        },
    )
    errors: Optional["ResponseType.Errors"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Errors:
        error: List[ErrorType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )


@dataclass
class EntityType:
    """
    Attributes:
        type_value: Κατηγορία
        entity_data: Στοιχεία Οντότητας
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
        },
    )
    entity_data: Optional[PartyType] = field(
        default=None,
        metadata={
            "name": "entityData",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )


@dataclass
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
        stamp_duty_amount: Ποσό Χαρτοσήμου
        stamp_duty_percent_category: Κατηγορία Συντελεστή  Χαρτοσήμου
        fees_amount: Ποσό Τελών
        fees_percent_category: Κατηγορία Συντελεστή Τελών
        other_taxes_percent_category: Κατηγορία Συντελεστή Λοιπών Φόρων
        other_taxes_amount: Ποσό Φόρου Διαμονης
        deductions_amount: Ποσό Κρατήσεων
        line_comments: Σχόλια Γραμμής
        income_classification: Λίστα Χαρακτηρισμών Εσόδων
        expenses_classification: Λίστα Χαρακτηρισμού Εξόδων
        quantity15: Ποσότητα Θερμοκρασίας 15 βαθμών
        other_measurement_unit_quantity: Πλήθος Μονάδας Μέτρησης Τεμάχια
            Άλλα
        other_measurement_unit_title: Τίτλος Μονάδας Μέτρησης Τεμάχια
            Άλλα
        not_vat195: Ένδειξη μη συμμετοχής στο ΦΠΑ (έσοδα – εκροές)
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
        },
    )
    rec_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "recType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 7,
        },
    )
    taric_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaricNo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "length": 10,
        },
    )
    item_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 50,
        },
    )
    item_descr: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescr",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 300,
        },
    )
    fuel_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "fuelCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
        },
    )
    measurement_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementUnit",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_detail_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceDetailType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    net_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "netValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    vat_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    vat_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    vat_exemption_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatExemptionCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dienergia: Optional[ShipType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    discount_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "discountOption",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    withheld_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "withheldAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    withheld_percent_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "withheldPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    stamp_duty_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "stampDutyAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    stamp_duty_percent_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "stampDutyPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    fees_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "feesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    fees_percent_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "feesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_taxes_percent_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherTaxesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_taxes_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherTaxesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    deductions_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "deductionsAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    line_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "lineComments",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    income_classification: List[IncomeClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "incomeClassification",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    expenses_classification: List[ExpensesClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "expensesClassification",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    quantity15: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
        },
    )
    other_measurement_unit_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "otherMeasurementUnitQuantity",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_measurement_unit_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherMeasurementUnitTitle",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    not_vat195: Optional[bool] = field(
        default=None,
        metadata={
            "name": "notVAT195",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
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
        income_classification: Λίστα Χαρακτηρισμών Εσόδων
        expenses_classification:
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    total_net_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalNetValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    total_vat_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalVatAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    total_withheld_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalWithheldAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    total_fees_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalFeesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    total_stamp_duty_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalStampDutyAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    total_other_taxes_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalOtherTaxesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    total_deductions_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalDeductionsAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    total_gross_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalGrossValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    income_classification: List[IncomeClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "incomeClassification",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    expenses_classification: List[ExpensesClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "expensesClassification",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
class RequestedE3Info(RequestedE3InfoType):
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class RequestedVatInfo(RequestedVatInfoType):
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
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

    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        },
    )
    classification_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    entity_vat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    transaction_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "transactionMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    invoices_expenses_classification_details: List[
        InvoicesExpensesClassificationDetailType
    ] = field(
        default_factory=list,
        metadata={
            "name": "invoicesExpensesClassificationDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    classification_post_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationPostMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 0,
            "max_inclusive": 1,
        },
    )


@dataclass
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

    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        },
    )
    income_classification_detail_data: List[IncomeClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "incomeClassificationDetailData",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "min_occurs": 1,
        },
    )


@dataclass
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

    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
            "required": True,
        },
    )
    payment_method_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "paymentMethodMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
        },
    )
    entity_vat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
        },
    )
    payment_method_details: List[PaymentMethodDetailType] = field(
        default_factory=list,
        metadata={
            "name": "paymentMethodDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/paymentMethod/v1.0",
            "min_occurs": 1,
        },
    )


@dataclass
class ResponseDoc:
    """
    Comment describing your root element.
    """

    response: List[ResponseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
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
        dispatch_date: Ημερομηνία  Έναρξης Αποστολής
        dispatch_time: Ώρα Έναρξης Αποστολής
        vehicle_number: Αριθμός Οχήματος
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
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        },
    )
    aa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        },
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    invoice_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    vat_payment_suspension: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vatPaymentSuspension",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    exchange_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "exchangeRate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    correlated_invoices: List[int] = field(
        default_factory=list,
        metadata={
            "name": "correlatedInvoices",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    self_pricing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "selfPricing",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dispatch_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dispatchDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dispatch_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "dispatchTime",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vehicle_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    move_purpose: Optional[int] = field(
        default=None,
        metadata={
            "name": "movePurpose",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 19,
        },
    )
    fuel_invoice: Optional[bool] = field(
        default=None,
        metadata={
            "name": "fuelInvoice",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    special_invoice_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "specialInvoiceCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_variation_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceVariationType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_correlated_entities: List[EntityType] = field(
        default_factory=list,
        metadata={
            "name": "otherCorrelatedEntities",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_delivery_note_header: Optional[OtherDeliveryNoteHeaderType] = field(
        default=None,
        metadata={
            "name": "otherDeliveryNoteHeader",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    is_delivery_note: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDeliveryNote",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_move_purpose_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherMovePurposeTitle",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    third_party_collection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "thirdPartyCollection",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    multiple_connected_marks: List[int] = field(
        default_factory=list,
        metadata={
            "name": "multipleConnectedMarks",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    table_aa: Optional[str] = field(
        default=None,
        metadata={
            "name": "tableAA",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 50,
        },
    )
    total_cancel_delivery_orders: Optional[bool] = field(
        default=None,
        metadata={
            "name": "totalCancelDeliveryOrders",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )


@dataclass
class ExpensesClassificationsDoc:
    """
    Χαρατηρισμοί Εξόδων Πρότυπων Παραστατικών ΑΑΔΕ.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"

    expenses_invoice_classification: List[
        InvoiceExpensesClassificationType
    ] = field(
        default_factory=list,
        metadata={
            "name": "expensesInvoiceClassification",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
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

    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        },
    )
    classification_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    entity_vat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    transaction_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "transactionMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    invoices_income_classification_details: List[
        InvoicesIncomeClassificationDetailType
    ] = field(
        default_factory=list,
        metadata={
            "name": "invoicesIncomeClassificationDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )


@dataclass
class PaymentMethodsDoc:
    """
    Μέθοδοι Πληρωμής.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/paymentMethod/v1.0"

    payment_methods: List[PaymentMethodType] = field(
        default_factory=list,
        metadata={
            "name": "paymentMethods",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class AadeBookInvoiceType:
    """
    Attributes:
        uid: Αναγνωριστικό Παραστατικού
        mark: Μοναδικός Αριθμός Καταχώρησης Παραστατικού
        cancelled_by_mark: Μοναδικός Αριθμός Καταχώρησης Ακυρωτικού
        authentication_code: Συμβολοσειρά Αυθεντικοποίησης Παρόχου
        transmission_failure: Αδυναμία Επικοινωνίας Παρόχου ή Αδυναμία
            διαβίβασης ERP
        issuer: Στοιχεία Εκδότη
        counterpart: Στοιχεία Λήπτη
        invoice_header: Γενικά Στοιχεία
        payment_methods: Πληρωμές
        invoice_details: Λεπτομέρειες Παραστατικού
        taxes_totals: Σύνολα Φόρων
        invoice_summary: Συγκεντρωτικά Στοιχεία
        qr_code_url: QR Code Url
        other_transport_details: Λοιπές Λεπτομέρειες Διακίνησης (Ορισμός
            - Αλλαγή Μτφ Μέσων, Μεταφορτώσεις, κλπ)
    """

    class Meta:
        target_namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    mark: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    cancelled_by_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "cancelledByMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    authentication_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authenticationCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    transmission_failure: Optional[int] = field(
        default=None,
        metadata={
            "name": "transmissionFailure",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 3,
        },
    )
    issuer: Optional[PartyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    counterpart: Optional[PartyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_header: Optional[InvoiceHeaderType] = field(
        default=None,
        metadata={
            "name": "invoiceHeader",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    payment_methods: Optional["AadeBookInvoiceType.PaymentMethods"] = field(
        default=None,
        metadata={
            "name": "paymentMethods",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_details: List[InvoiceRowType] = field(
        default_factory=list,
        metadata={
            "name": "invoiceDetails",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_occurs": 1,
        },
    )
    taxes_totals: Optional["AadeBookInvoiceType.TaxesTotals"] = field(
        default=None,
        metadata={
            "name": "taxesTotals",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    invoice_summary: Optional[InvoiceSummaryType] = field(
        default=None,
        metadata={
            "name": "invoiceSummary",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    qr_code_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "qrCodeUrl",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_transport_details: List[TransportDetailType] = field(
        default_factory=list,
        metadata={
            "name": "otherTransportDetails",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )

    @dataclass
    class PaymentMethods:
        """
        Attributes:
            payment_method_details: Στοιχεία Πληρωμών
        """

        payment_method_details: List[PaymentMethodDetailType] = field(
            default_factory=list,
            metadata={
                "name": "paymentMethodDetails",
                "type": "Element",
                "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
                "min_occurs": 1,
            },
        )

    @dataclass
    class TaxesTotals:
        taxes: List[TaxTotalsType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
                "min_occurs": 1,
            },
        )


@dataclass
class IncomeClassificationsDoc:
    """
    Χαρατηρισμοί Εσόδων Πρότυπων Παραστατικών ΑΑΔΕ.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"

    income_invoice_classification: List[InvoiceIncomeClassificationType] = (
        field(
            default_factory=list,
            metadata={
                "name": "incomeInvoiceClassification",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )


@dataclass
class InvoicesDoc:
    """
    Παραστατικό ΑΑΔΕ.
    """

    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    invoice: List[AadeBookInvoiceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class RequestedDoc:
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    continuation_token: Optional[ContinuationTokenType3] = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
        },
    )
    invoices_doc: Optional["RequestedDoc.InvoicesDoc"] = field(
        default=None,
        metadata={
            "name": "invoicesDoc",
            "type": "Element",
        },
    )
    cancelled_invoices_doc: Optional["RequestedDoc.CancelledInvoicesDoc"] = (
        field(
            default=None,
            metadata={
                "name": "cancelledInvoicesDoc",
                "type": "Element",
            },
        )
    )
    income_classifications_doc: Optional[
        "RequestedDoc.IncomeClassificationsDoc"
    ] = field(
        default=None,
        metadata={
            "name": "incomeClassificationsDoc",
            "type": "Element",
        },
    )
    expenses_classifications_doc: Optional[
        "RequestedDoc.ExpensesClassificationsDoc"
    ] = field(
        default=None,
        metadata={
            "name": "expensesClassificationsDoc",
            "type": "Element",
        },
    )
    payment_methods_doc: Optional["RequestedDoc.PaymentMethodsDoc"] = field(
        default=None,
        metadata={
            "name": "paymentMethodsDoc",
            "type": "Element",
        },
    )

    @dataclass
    class InvoicesDoc:
        invoice: List[AadeBookInvoiceType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass
    class CancelledInvoicesDoc:
        cancelled_invoice: List[CancelledInvoiceType] = field(
            default_factory=list,
            metadata={
                "name": "cancelledInvoice",
                "type": "Element",
            },
        )

    @dataclass
    class IncomeClassificationsDoc:
        income_invoice_classification: List[
            InvoiceIncomeClassificationType
        ] = field(
            default_factory=list,
            metadata={
                "name": "incomeInvoiceClassification",
                "type": "Element",
            },
        )

    @dataclass
    class ExpensesClassificationsDoc:
        expenses_invoice_classification: List[
            InvoiceExpensesClassificationType
        ] = field(
            default_factory=list,
            metadata={
                "name": "expensesInvoiceClassification",
                "type": "Element",
            },
        )

    @dataclass
    class PaymentMethodsDoc:
        payment_methods: List[PaymentMethodType] = field(
            default_factory=list,
            metadata={
                "name": "paymentMethods",
                "type": "Element",
            },
        )
