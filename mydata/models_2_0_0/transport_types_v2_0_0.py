from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDateTime

from mydata.models_2_0_0.simple_types_v2_0_0 import DeliveryOutcomeType


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
