from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from mydata.models_2_0_0.expenses_classification_v2_0_0 import (
    InvoiceExpensesClassificationType,
)
from mydata.models_2_0_0.income_classification_v2_0_0 import (
    InvoiceIncomeClassificationType,
)
from mydata.models_2_0_0.invoices_doc_v2_0_0 import AadeBookInvoiceType
from mydata.models_2_0_0.payment_methods_v2_0_0 import PaymentMethodType

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass(kw_only=True)
class CancelledInvoiceType:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης του ακυρωμένου
            Παραστατικού
        cancellation_mark: Μοναδικός Αριθμός Καταχώρησης της Ακύρωσης
        cancellation_date: Ημερομηνία Ακύρωσης Παραστατικού
    """

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
class ContinuationTokenType2:
    class Meta:
        name = "continuationTokenType"

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
class RequestedDoc:
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    continuation_token: None | ContinuationTokenType2 = field(
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
