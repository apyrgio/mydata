from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime


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
