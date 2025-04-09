from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlTime


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
class ContinuationTokenType1:
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


class CountryType(Enum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OC = "OC"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    ST = "ST"
    SV = "SV"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


class CurrencyType(Enum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EEK = "EEK"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GWP = "GWP"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TVD = "TVD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    YER = "YER"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZWL = "ZWL"


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


class FuelCodes(Enum):
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_50 = "50"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_999 = "999"


class InvoiceType(Enum):
    VALUE_1_1 = "1.1"
    VALUE_1_2 = "1.2"
    VALUE_1_3 = "1.3"
    VALUE_1_4 = "1.4"
    VALUE_1_5 = "1.5"
    VALUE_1_6 = "1.6"
    VALUE_2_1 = "2.1"
    VALUE_2_2 = "2.2"
    VALUE_2_3 = "2.3"
    VALUE_2_4 = "2.4"
    VALUE_3_1 = "3.1"
    VALUE_3_2 = "3.2"
    VALUE_4 = "4"
    VALUE_5_1 = "5.1"
    VALUE_5_2 = "5.2"
    VALUE_6_1 = "6.1"
    VALUE_6_2 = "6.2"
    VALUE_7_1 = "7.1"
    VALUE_8_1 = "8.1"
    VALUE_8_2 = "8.2"
    VALUE_8_4 = "8.4"
    VALUE_8_5 = "8.5"
    VALUE_8_6 = "8.6"
    VALUE_9_3 = "9.3"
    VALUE_11_1 = "11.1"
    VALUE_11_2 = "11.2"
    VALUE_11_3 = "11.3"
    VALUE_11_4 = "11.4"
    VALUE_11_5 = "11.5"
    VALUE_12_1 = "12"
    VALUE_13_1 = "13.1"
    VALUE_13_2 = "13.2"
    VALUE_13_3 = "13.3"
    VALUE_13_4 = "13.4"
    VALUE_13_30 = "13.30"
    VALUE_13_31 = "13.31"
    VALUE_14_1 = "14.1"
    VALUE_14_2 = "14.2"
    VALUE_14_3 = "14.3"
    VALUE_14_4 = "14.4"
    VALUE_14_5 = "14.5"
    VALUE_14_30 = "14.30"
    VALUE_14_31 = "14.31"
    VALUE_15_1 = "15.1"
    VALUE_16_1 = "16.1"
    VALUE_17_1 = "17.1"
    VALUE_17_2 = "17.2"
    VALUE_17_3 = "17.3"
    VALUE_17_4 = "17.4"
    VALUE_17_5 = "17.5"
    VALUE_17_6 = "17.6"


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
    underlying_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "underlyingValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "taxAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
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
class ContinuationTokenType2:
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


class ExpensesClassificationCategoryType(Enum):
    CATEGORY2_1 = "category2_1"
    CATEGORY2_2 = "category2_2"
    CATEGORY2_3 = "category2_3"
    CATEGORY2_4 = "category2_4"
    CATEGORY2_5 = "category2_5"
    CATEGORY2_6 = "category2_6"
    CATEGORY2_7 = "category2_7"
    CATEGORY2_8 = "category2_8"
    CATEGORY2_9 = "category2_9"
    CATEGORY2_10 = "category2_10"
    CATEGORY2_11 = "category2_11"
    CATEGORY2_12 = "category2_12"
    CATEGORY2_13 = "category2_13"
    CATEGORY2_14 = "category2_14"
    CATEGORY2_95 = "category2_95"


class ExpensesClassificationValueType(Enum):
    E3_101 = "E3_101"
    E3_102_001 = "E3_102_001"
    E3_102_002 = "E3_102_002"
    E3_102_003 = "E3_102_003"
    E3_102_004 = "E3_102_004"
    E3_102_005 = "E3_102_005"
    E3_102_006 = "E3_102_006"
    E3_104 = "E3_104"
    E3_201 = "E3_201"
    E3_202_001 = "E3_202_001"
    E3_202_002 = "E3_202_002"
    E3_202_003 = "E3_202_003"
    E3_202_004 = "E3_202_004"
    E3_202_005 = "E3_202_005"
    E3_204 = "E3_204"
    E3_207 = "E3_207"
    E3_209 = "E3_209"
    E3_301 = "E3_301"
    E3_302_001 = "E3_302_001"
    E3_302_002 = "E3_302_002"
    E3_302_003 = "E3_302_003"
    E3_302_004 = "E3_302_004"
    E3_302_005 = "E3_302_005"
    E3_304 = "E3_304"
    E3_307 = "E3_307"
    E3_309 = "E3_309"
    E3_312 = "E3_312"
    E3_313_001 = "E3_313_001"
    E3_313_002 = "E3_313_002"
    E3_313_003 = "E3_313_003"
    E3_313_004 = "E3_313_004"
    E3_313_005 = "E3_313_005"
    E3_315 = "E3_315"
    E3_581_001 = "E3_581_001"
    E3_581_002 = "E3_581_002"
    E3_581_003 = "E3_581_003"
    E3_582 = "E3_582"
    E3_583 = "E3_583"
    E3_584 = "E3_584"
    E3_585_001 = "E3_585_001"
    E3_585_002 = "E3_585_002"
    E3_585_003 = "E3_585_003"
    E3_585_004 = "E3_585_004"
    E3_585_005 = "E3_585_005"
    E3_585_006 = "E3_585_006"
    E3_585_007 = "E3_585_007"
    E3_585_008 = "E3_585_008"
    E3_585_009 = "E3_585_009"
    E3_585_010 = "E3_585_010"
    E3_585_011 = "E3_585_011"
    E3_585_012 = "E3_585_012"
    E3_585_013 = "E3_585_013"
    E3_585_014 = "E3_585_014"
    E3_585_015 = "E3_585_015"
    E3_585_016 = "E3_585_016"
    E3_586 = "E3_586"
    E3_587 = "E3_587"
    E3_588 = "E3_588"
    E3_589 = "E3_589"
    E3_881_001 = "E3_881_001"
    E3_881_002 = "E3_881_002"
    E3_881_003 = "E3_881_003"
    E3_881_004 = "E3_881_004"
    E3_882_001 = "E3_882_001"
    E3_882_002 = "E3_882_002"
    E3_882_003 = "E3_882_003"
    E3_882_004 = "E3_882_004"
    E3_883_001 = "E3_883_001"
    E3_883_002 = "E3_883_002"
    E3_883_003 = "E3_883_003"
    E3_883_004 = "E3_883_004"
    VAT_361 = "VAT_361"
    VAT_362 = "VAT_362"
    VAT_363 = "VAT_363"
    VAT_364 = "VAT_364"
    VAT_365 = "VAT_365"
    VAT_366 = "VAT_366"
    E3_103 = "E3_103"
    E3_203 = "E3_203"
    E3_303 = "E3_303"
    E3_208 = "E3_208"
    E3_308 = "E3_308"
    E3_314 = "E3_314"
    E3_106 = "E3_106"
    E3_205 = "E3_205"
    E3_305 = "E3_305"
    E3_210 = "E3_210"
    E3_310 = "E3_310"
    E3_318 = "E3_318"
    E3_598_002 = "E3_598_002"


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

    continuation_token: List[ContinuationTokenType1] = field(
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
    country: Optional[CountryType] = field(
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
    country_document_id: Optional[CountryType] = field(
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
            "max_inclusive": 7,
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
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
    tip_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "tipAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
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

    classification_type: Optional[ExpensesClassificationValueType] = field(
        default=None,
        metadata={
            "name": "classificationType",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    classification_category: Optional[ExpensesClassificationCategoryType] = (
        field(
            default=None,
            metadata={
                "name": "classificationCategory",
                "type": "Element",
                "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            },
        )
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "fraction_digits": 2,
        },
    )
    vat_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": Decimal("0"),
            "fraction_digits": 2,
        },
    )
    vat_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "vatCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 8,
        },
    )
    vat_exemption_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "vatExemptionCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 31,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
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
    fuel_code: Optional[FuelCodes] = field(
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
    measurement_unit: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementUnit",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 7,
        },
    )
    invoice_detail_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceDetailType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    net_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "netValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    vat_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "vatCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 9,
        },
    )
    vat_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    vat_exemption_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "vatExemptionCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 31,
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
    withheld_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "withheldAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    withheld_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "withheldPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 18,
        },
    )
    stamp_duty_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "stampDutyAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    stamp_duty_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "stampDutyPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 4,
        },
    )
    fees_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "feesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    fees_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "feesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 22,
        },
    )
    other_taxes_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "otherTaxesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 19,
        },
    )
    other_taxes_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "otherTaxesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    deductions_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "deductionsAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
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

    total_net_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalNetValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    total_vat_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalVatAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    total_withheld_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalWithheldAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    total_fees_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalFeesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    total_stamp_duty_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalStampDutyAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    total_other_taxes_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalOtherTaxesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    total_deductions_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalDeductionsAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    total_gross_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalGrossValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
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
    invoice_type: Optional[InvoiceType] = field(
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
    currency: Optional[CurrencyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    exchange_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "exchangeRate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("50000"),
            "fraction_digits": 5,
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
    special_invoice_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "specialInvoiceCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 12,
        },
    )
    invoice_variation_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceVariationType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 4,
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

    continuation_token: Optional[ContinuationTokenType2] = field(
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
                "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
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
