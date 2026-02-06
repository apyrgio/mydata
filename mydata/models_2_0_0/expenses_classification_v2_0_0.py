from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"


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
class InvoicesExpensesClassificationDetailType:
    """
    Attributes:
        line_number: Γραμμή Παραστατικού
        expenses_classification_detail_data: Λίστα Χαρακτηρισμών Εσόδων
    """

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
