from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum


@dataclass(kw_only=True)
class AmountType:
    value: Decimal = field(
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class AmountType2:
    value: Decimal = field(
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 3,
        }
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


@dataclass(kw_only=True)
class DeductionsType:
    value: Decimal = field(
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("100"),
            "fraction_digits": 2,
        }
    )


class DeliveryOutcomeType(Enum):
    FULL = "FULL"
    PARTIAL = "PARTIAL"
    NONE = "NONE"


@dataclass(kw_only=True)
class ExchangeRateType:
    value: Decimal = field(
        metadata={
            "required": True,
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("50000"),
            "fraction_digits": 5,
        }
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
    NOT_VAT_295 = "NOT_VAT_295"


@dataclass(kw_only=True)
class FeesType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 22,
        }
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


@dataclass(kw_only=True)
class InvoiceDetailType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
        }
    )


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
    VALUE_9_1 = "9.1"
    VALUE_9_2 = "9.2"
    VALUE_9_3 = "9.3"
    VALUE_10_1 = "10.1"
    VALUE_10_2 = "10.2"
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


@dataclass(kw_only=True)
class InvoiceVariationType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 4,
        }
    )


@dataclass(kw_only=True)
class OtherTaxesType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 30,
        }
    )


@dataclass(kw_only=True)
class QuantityType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 7,
        }
    )


@dataclass(kw_only=True)
class ReverseDeliveryNotePurposeType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 5,
        }
    )


@dataclass(kw_only=True)
class SpecialInvoiceCategoryType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 13,
        }
    )


@dataclass(kw_only=True)
class StampDutyType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 4,
        }
    )


@dataclass(kw_only=True)
class VatExemptionType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 31,
        }
    )


@dataclass(kw_only=True)
class VatType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 10,
        }
    )


@dataclass(kw_only=True)
class WithheldType:
    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 18,
        }
    )
