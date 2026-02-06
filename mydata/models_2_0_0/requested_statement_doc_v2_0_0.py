from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from mydata.models_2_0_0.send_statement_v2_0_0 import Statement


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
