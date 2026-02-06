from __future__ import annotations

from dataclasses import dataclass, field

from mydata.models_2_0_0.invoices_doc_v2_0_0 import PaymentMethodDetailType

__NAMESPACE__ = "https://www.aade.gr/myDATA/paymentMethod/v1.0"


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
