from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"


@dataclass(kw_only=True)
class IncomeClassificationType:
    """
    Attributes:
        classification_type: Κωδικός Χαρακτηρισμού
        classification_category: Κατηγορία Χαρακτηρισμού
        amount: Ποσό Χαρακτηρισμού
        id: Μοναδικός Αριθμός Χαρακτηρισμού
    """

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
class InvoicesIncomeClassificationDetailType:
    """
    Attributes:
        line_number: Γραμμή Παραστατικού
        income_classification_detail_data: Λίστα Χαρακτηρισμών Εσόδων
    """

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
