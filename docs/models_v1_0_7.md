# Table of Contents

* [mydata.models\_v1\_0\_7](#mydata.models_v1_0_7)
  * [ErrorType](#mydata.models_v1_0_7.ErrorType)
  * [InvoiceProviderType](#mydata.models_v1_0_7.InvoiceProviderType)
  * [ProviderInfoType](#mydata.models_v1_0_7.ProviderInfoType)
  * [ReceptionEmailsType](#mydata.models_v1_0_7.ReceptionEmailsType)
  * [AddressType](#mydata.models_v1_0_7.AddressType)
  * [CancelledInvoiceType](#mydata.models_v1_0_7.CancelledInvoiceType)
  * [PaymentMethodDetailType](#mydata.models_v1_0_7.PaymentMethodDetailType)
  * [ShipType](#mydata.models_v1_0_7.ShipType)
  * [TaxTotalsType](#mydata.models_v1_0_7.TaxTotalsType)
  * [TransportDetailType](#mydata.models_v1_0_7.TransportDetailType)
  * [RequestedProviderDoc](#mydata.models_v1_0_7.RequestedProviderDoc)
  * [ReceptionProvidersType](#mydata.models_v1_0_7.ReceptionProvidersType)
  * [PartyType](#mydata.models_v1_0_7.PartyType)
  * [ExpensesClassificationType](#mydata.models_v1_0_7.ExpensesClassificationType)
  * [IncomeClassificationType](#mydata.models_v1_0_7.IncomeClassificationType)
  * [ResponseType](#mydata.models_v1_0_7.ResponseType)
  * [EntityType](#mydata.models_v1_0_7.EntityType)
  * [InvoiceRowType](#mydata.models_v1_0_7.InvoiceRowType)
  * [InvoiceSummaryType](#mydata.models_v1_0_7.InvoiceSummaryType)
  * [InvoicesExpensesClassificationDetailType](#mydata.models_v1_0_7.InvoicesExpensesClassificationDetailType)
  * [InvoicesIncomeClassificationDetailType](#mydata.models_v1_0_7.InvoicesIncomeClassificationDetailType)
  * [ResponseDoc](#mydata.models_v1_0_7.ResponseDoc)
  * [InvoiceHeaderType](#mydata.models_v1_0_7.InvoiceHeaderType)
  * [InvoiceExpensesClassificationType](#mydata.models_v1_0_7.InvoiceExpensesClassificationType)
  * [InvoiceIncomeClassificationType](#mydata.models_v1_0_7.InvoiceIncomeClassificationType)
  * [AadeBookInvoiceType](#mydata.models_v1_0_7.AadeBookInvoiceType)
    * [PaymentMethods](#mydata.models_v1_0_7.AadeBookInvoiceType.PaymentMethods)
  * [ExpensesClassificationsDoc](#mydata.models_v1_0_7.ExpensesClassificationsDoc)
  * [IncomeClassificationsDoc](#mydata.models_v1_0_7.IncomeClassificationsDoc)
  * [InvoicesDoc](#mydata.models_v1_0_7.InvoicesDoc)

<a id="mydata.models_v1_0_7"></a>

# mydata.models\_v1\_0\_7

<a id="mydata.models_v1_0_7.ErrorType"></a>

## ErrorType Objects

```python
@dataclass
class ErrorType()
```

**Attributes**:

- `message` - Μήνυμα Σφάλματος
- `code` - Κωδικός Σφάλαματος

<a id="mydata.models_v1_0_7.InvoiceProviderType"></a>

## InvoiceProviderType Objects

```python
@dataclass
class InvoiceProviderType()
```

**Attributes**:

- `issuer_vat` - ΑΦΜ Εκδότη
- `invoice_provider_mark` - Μοναδικός Αριθμός Καταχώρησης
  παραστατικού Παρόχου
- `invoice_uid` - Αναγνωριστικό οντότητας
- `authentication_code` - Συμβολοσειρά Αυθεντικοποίησης Παραστατικού
  Παρόχου

<a id="mydata.models_v1_0_7.ProviderInfoType"></a>

## ProviderInfoType Objects

```python
@dataclass
class ProviderInfoType()
```

**Attributes**:

- `vatnumber` - ΑΦΜ

<a id="mydata.models_v1_0_7.ReceptionEmailsType"></a>

## ReceptionEmailsType Objects

```python
@dataclass
class ReceptionEmailsType()
```

**Attributes**:

- `email` - Email

<a id="mydata.models_v1_0_7.AddressType"></a>

## AddressType Objects

```python
@dataclass
class AddressType()
```

**Attributes**:

  street:
- `number` - Αριθμός
- `postal_code` - ΤΚ
  city:

<a id="mydata.models_v1_0_7.CancelledInvoiceType"></a>

## CancelledInvoiceType Objects

```python
@dataclass
class CancelledInvoiceType()
```

**Attributes**:

- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης του ακυρωμένου
  Παραστατικού
- `cancellation_mark` - Μοναδικός Αριθμός Καταχώρησης της Ακύρωσης
- `cancellation_date` - Ημερομηνία Ακύρωσης Παραστατικού

<a id="mydata.models_v1_0_7.PaymentMethodDetailType"></a>

## PaymentMethodDetailType Objects

```python
@dataclass
class PaymentMethodDetailType()
```

**Attributes**:

- `type_value` - Τύπος Πληρωμής
- `amount` - Αναλογούν Ποσό
- `payment_method_info` - Λοιπές Πληροφορίες

<a id="mydata.models_v1_0_7.ShipType"></a>

## ShipType Objects

```python
@dataclass
class ShipType()
```

**Attributes**:

- `application_id` - Αριθμός Δήλωσης διενέργειας δραστηριότητας
- `application_date` - Ημερομηνία Δήλωσης
  doy:
- `ship_id` - Στοιχεία Πλοίου

<a id="mydata.models_v1_0_7.TaxTotalsType"></a>

## TaxTotalsType Objects

```python
@dataclass
class TaxTotalsType()
```

**Attributes**:

- `tax_type` - Είδος Φόρου
- `tax_category` - Κατηγορία Φόρου
- `underlying_value` - Υποκείμενη Αξία
- `tax_amount` - Ποσό Φόρου
  id:

<a id="mydata.models_v1_0_7.TransportDetailType"></a>

## TransportDetailType Objects

```python
@dataclass
class TransportDetailType()
```

**Attributes**:

- `vehicle_number` - Αριθμός Μεταφορικού Μέσου

<a id="mydata.models_v1_0_7.RequestedProviderDoc"></a>

## RequestedProviderDoc Objects

```python
@dataclass
class RequestedProviderDoc()
```

Παραστατικά από Πάροχο.

<a id="mydata.models_v1_0_7.ReceptionProvidersType"></a>

## ReceptionProvidersType Objects

```python
@dataclass
class ReceptionProvidersType()
```

**Attributes**:

- `provider_info` - Πληροφορίες Παρόχου

<a id="mydata.models_v1_0_7.PartyType"></a>

## PartyType Objects

```python
@dataclass
class PartyType()
```

**Attributes**:

  vat_number:
- `country` - Κωδ. Χώρας
- `branch` - Αρ. Εγκατάστασης
  name:
- `address` - Διεύθυνση
  document_id_no:
- `supply_account_no` - Αρ. Παροχής Ηλ. Ρεύματος
- `country_document_id` - Κωδ. Χώρας Έκδοσης Επίσημου Εγγράφου

<a id="mydata.models_v1_0_7.ExpensesClassificationType"></a>

## ExpensesClassificationType Objects

```python
@dataclass
class ExpensesClassificationType()
```

**Attributes**:

- `classification_type` - Κωδικός Χαρακτηρισμού
- `classification_category` - Κατηγορία Χαρακτηρισμού
- `amount` - Ποσό Χαρακτηρισμού
- `vat_amount` - Πόσο Φόρου
- `vat_category` - Κατηγορία ΦΠΑ
- `vat_exemption_category` - Κατηγορία Εξαίρεσης ΦΠΑ
- `id` - Μοναδικός Αριθμός Χαρακτηρισμού

<a id="mydata.models_v1_0_7.IncomeClassificationType"></a>

## IncomeClassificationType Objects

```python
@dataclass
class IncomeClassificationType()
```

**Attributes**:

- `classification_type` - Κωδικός Χαρακτηρισμού
- `classification_category` - Κατηγορία Χαρακτηρισμού
- `amount` - Ποσό Χαρακτηρισμού
- `id` - Μοναδικός Αριθμός Χαρακτηρισμού

<a id="mydata.models_v1_0_7.ResponseType"></a>

## ResponseType Objects

```python
@dataclass
class ResponseType()
```

**Attributes**:

- `index` - ΑΑ γραμμής οντότητας
- `invoice_uid` - Αναγνωριστικό οντότητας
- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης παραστατικού
- `qr_url` - QR Code Url
- `classification_mark` - Μοναδικός Αριθμός Παραλαβής Χαρακτηρισμού
- `cancellation_mark` - Μοναδικός Αριθμός Ακύρωσης
- `authentication_code` - Συμβολοσειρά Αυθεντικοποίησης Παρόχου
- `reception_providers` - Πάροχοι Λήπτη
- `reception_emails` - Email Παραλαβής
- `errors` - Λίστα Σφαλμάτων
- `status_code` - Κωδικός αποτελέσματος

<a id="mydata.models_v1_0_7.EntityType"></a>

## EntityType Objects

```python
@dataclass
class EntityType()
```

**Attributes**:

- `type_value` - Κατηγορία
- `entity_data` - Στοιχεία Οντότητας

<a id="mydata.models_v1_0_7.InvoiceRowType"></a>

## InvoiceRowType Objects

```python
@dataclass
class InvoiceRowType()
```

**Attributes**:

- `line_number` - ΑΑ Γραμμής
- `rec_type` - Είδος Γραμμής
- `item_descr` - Περιγραφή Είδους
- `fuel_code` - Κωδικός Καυσίμου
- `quantity` - Ποσότητα
- `measurement_unit` - Είδος Ποσότητας
- `invoice_detail_type` - Επισήμανση
- `net_value` - Καθαρή Αξία
- `vat_category` - Κατηγορία ΦΠΑ
- `vat_amount` - Ποσό ΦΠΑ
- `vat_exemption_category` - Κατηγορία Αιτίας Εξαίρεσης ΦΠΑ
- `dienergia` - ΠΟΛ 1177/2018 Αρ. 27
- `discount_option` - Δικαίωμα Έκπτωσης
- `withheld_amount` - Ποσό Παρ. Φόρου
- `withheld_percent_category` - Κατηγορία Συντελεστή  Παρ. Φόρου
- `stamp_duty_amount` - Ποσό Χαρτοσήμου
- `stamp_duty_percent_category` - Κατηγορία Συντελεστή  Χαρτοσήμου
- `fees_amount` - Ποσό Τελών
- `fees_percent_category` - Κατηγορία Συντελεστή Τελών
- `other_taxes_percent_category` - Κατηγορία Συντελεστή Λοιπών Φόρων
- `other_taxes_amount` - Ποσό Φόρου Διαμονης
- `deductions_amount` - Ποσό Κρατήσεων
- `line_comments` - Σχόλια Γραμμής
- `income_classification` - Λίστα Χαρακτηρισμών Εσόδων
- `expenses_classification` - Λίστα Χαρακτηρισμού Εξόδων
- `quantity15` - Ποσότητα Θερμοκρασίας 15 βαθμών

<a id="mydata.models_v1_0_7.InvoiceSummaryType"></a>

## InvoiceSummaryType Objects

```python
@dataclass
class InvoiceSummaryType()
```

**Attributes**:

- `total_net_value` - Σύνολο Καθαρής Αξίας
- `total_vat_amount` - Σύνολο ΦΠΑ
- `total_withheld_amount` - Σύνολο Παρ. Φόρων
- `total_fees_amount` - Σύνολο Τελών
- `total_stamp_duty_amount` - Σύνολο Χαρτοσήμου
- `total_other_taxes_amount` - Σύνολο Λοιπών Φόρων
- `total_deductions_amount` - Σύνολο Κρατήσεων
- `total_gross_value` - Συνολική Αξία
- `income_classification` - Λίστα Χαρακτηρισμών Εσόδων
  expenses_classification:

<a id="mydata.models_v1_0_7.InvoicesExpensesClassificationDetailType"></a>

## InvoicesExpensesClassificationDetailType Objects

```python
@dataclass
class InvoicesExpensesClassificationDetailType()
```

**Attributes**:

- `line_number` - Γραμμή Παραστατικού
- `expenses_classification_detail_data` - Λίστα Χαρακτηρισμών Εσόδων

<a id="mydata.models_v1_0_7.InvoicesIncomeClassificationDetailType"></a>

## InvoicesIncomeClassificationDetailType Objects

```python
@dataclass
class InvoicesIncomeClassificationDetailType()
```

**Attributes**:

- `line_number` - Γραμμή Παραστατικού
- `income_classification_detail_data` - Λίστα Χαρακτηρισμών Εσόδων

<a id="mydata.models_v1_0_7.ResponseDoc"></a>

## ResponseDoc Objects

```python
@dataclass
class ResponseDoc()
```

Comment describing your root element.

<a id="mydata.models_v1_0_7.InvoiceHeaderType"></a>

## InvoiceHeaderType Objects

```python
@dataclass
class InvoiceHeaderType()
```

**Attributes**:

- `series` - Σειρά Παραστατικού
- `aa` - ΑΑ Παραστατικού
- `issue_date` - Ημερομηνία Έκδοσης
- `invoice_type` - Είδος Παραστατικού
- `vat_payment_suspension` - Αναστολή Καταβολής ΦΠΑ
- `currency` - Νόμισμα
- `exchange_rate` - Ισοτιμία
- `correlated_invoices` - Συσχετιζόμενα Παραστατικά
- `self_pricing` - Ένδειξη Αυτοτιμολόγησης
- `dispatch_date` - Ημερομηνία  Έναρξης Αποστολής
- `dispatch_time` - Ώρα Έναρξης Αποστολής
- `vehicle_number` - Αριθμός Οχήματος
- `move_purpose` - Σκοπός Διακίνησης
- `fuel_invoice` - Παραστατικό Καυσίμων
- `special_invoice_category` - Ειδική Κατηγορία Παραστατικού
- `invoice_variation_type` - Τύπος Απόκλισης Παραστατικού
- `other_correlated_entities` - Λοιπές συσχετιζόμενες οντοτήτες

<a id="mydata.models_v1_0_7.InvoiceExpensesClassificationType"></a>

## InvoiceExpensesClassificationType Objects

```python
@dataclass
class InvoiceExpensesClassificationType()
```

**Attributes**:

- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης Παραστατικού
- `classification_mark` - Αποδεικτικό Λήψης Χαρακτηρισμού Εξόδων.
  Συμπληρώνεται από την Υπηρεσία
- `entity_vat_number` - ΑΦΜ Οντότητας Αναφοράς
- `transaction_mode` - Αιτιολογία Συναλλαγής
  invoices_expenses_classification_details:
- `classification_post_mode` - Μέθοδος Υποβολής Χαρακτηρισμού

<a id="mydata.models_v1_0_7.InvoiceIncomeClassificationType"></a>

## InvoiceIncomeClassificationType Objects

```python
@dataclass
class InvoiceIncomeClassificationType()
```

**Attributes**:

- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης Παραστατικού
- `classification_mark` - Αποδεικτικό Λήψης Χαρακτηρισμού Εσόδων.
  Συμπληρώνεται από την Υπηρεσία
- `entity_vat_number` - ΑΦΜ Οντότητας Αναφοράς
- `transaction_mode` - Αιτιολογία Συναλλαγής
  invoices_income_classification_details:

<a id="mydata.models_v1_0_7.AadeBookInvoiceType"></a>

## AadeBookInvoiceType Objects

```python
@dataclass
class AadeBookInvoiceType()
```

**Attributes**:

- `uid` - Αναγνωριστικό Παραστατικού
- `mark` - Μοναδικός Αριθμός Καταχώρησης Παραστατικού
- `cancelled_by_mark` - Μοναδικός Αριθμός Καταχώρησης Ακυρωτικού
- `authentication_code` - Συμβολοσειρά Αυθεντικοποίησης Παρόχου
- `transmission_failure` - Αδυναμία Επικοινωνίας Παρόχου ή Αδυναμία
  διαβίβασης ERP
- `issuer` - Στοιχεία Εκδότη
- `counterpart` - Στοιχεία Λήπτη
- `invoice_header` - Γενικά Στοιχεία
- `payment_methods` - Πληρωμές
- `invoice_details` - Λεπτομέρειες Παραστατικού
- `taxes_totals` - Σύνολα Φόρων
- `invoice_summary` - Συγκεντρωτικά Στοιχεία
- `qr_code_url` - QR Code Url
- `other_transport_details` - Λοιπές Λεπτομέρειες Διακίνησης (Ορισμός
  - Αλλαγή Μτφ Μέσων, Μεταφορτώσεις, κλπ)

<a id="mydata.models_v1_0_7.AadeBookInvoiceType.PaymentMethods"></a>

## PaymentMethods Objects

```python
@dataclass
class PaymentMethods()
```

**Attributes**:

- `payment_method_details` - Στοιχεία Πληρωμών

<a id="mydata.models_v1_0_7.ExpensesClassificationsDoc"></a>

## ExpensesClassificationsDoc Objects

```python
@dataclass
class ExpensesClassificationsDoc()
```

Χαρατηρισμοί Εξόδων Πρότυπων Παραστατικών ΑΑΔΕ.

<a id="mydata.models_v1_0_7.IncomeClassificationsDoc"></a>

## IncomeClassificationsDoc Objects

```python
@dataclass
class IncomeClassificationsDoc()
```

Χαρατηρισμοί Εσόδων Πρότυπων Παραστατικών ΑΑΔΕ.

<a id="mydata.models_v1_0_7.InvoicesDoc"></a>

## InvoicesDoc Objects

```python
@dataclass
class InvoicesDoc()
```

Παραστατικό ΑΑΔΕ.

