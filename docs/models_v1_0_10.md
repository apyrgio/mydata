# Table of Contents

* [mydata.models\_1\_0\_10](#mydata.models_1_0_10)
  * [ErrorType](#mydata.models_1_0_10.ErrorType)
  * [InvoiceProviderType](#mydata.models_1_0_10.InvoiceProviderType)
  * [ProviderInfoType](#mydata.models_1_0_10.ProviderInfoType)
  * [ReceptionEmailsType](#mydata.models_1_0_10.ReceptionEmailsType)
  * [AddressType](#mydata.models_1_0_10.AddressType)
  * [CancelledInvoiceType](#mydata.models_1_0_10.CancelledInvoiceType)
  * [EcrtokenType](#mydata.models_1_0_10.EcrtokenType)
  * [ProviderSignatureType](#mydata.models_1_0_10.ProviderSignatureType)
  * [ShipType](#mydata.models_1_0_10.ShipType)
  * [TaxTotalsType](#mydata.models_1_0_10.TaxTotalsType)
  * [TransportDetailType](#mydata.models_1_0_10.TransportDetailType)
  * [ExpensesClassificationType](#mydata.models_1_0_10.ExpensesClassificationType)
  * [RequestedProviderDoc](#mydata.models_1_0_10.RequestedProviderDoc)
  * [ReceptionProvidersType](#mydata.models_1_0_10.ReceptionProvidersType)
  * [OtherDeliveryNoteHeaderType](#mydata.models_1_0_10.OtherDeliveryNoteHeaderType)
  * [PartyType](#mydata.models_1_0_10.PartyType)
  * [PaymentMethodDetailType](#mydata.models_1_0_10.PaymentMethodDetailType)
  * [InvoicesExpensesClassificationDetailType](#mydata.models_1_0_10.InvoicesExpensesClassificationDetailType)
  * [IncomeClassificationType](#mydata.models_1_0_10.IncomeClassificationType)
  * [ResponseType](#mydata.models_1_0_10.ResponseType)
  * [EntityType](#mydata.models_1_0_10.EntityType)
  * [InvoiceRowType](#mydata.models_1_0_10.InvoiceRowType)
  * [InvoiceSummaryType](#mydata.models_1_0_10.InvoiceSummaryType)
  * [InvoiceExpensesClassificationType](#mydata.models_1_0_10.InvoiceExpensesClassificationType)
  * [InvoicesIncomeClassificationDetailType](#mydata.models_1_0_10.InvoicesIncomeClassificationDetailType)
  * [PaymentMethodType](#mydata.models_1_0_10.PaymentMethodType)
  * [ResponseDoc](#mydata.models_1_0_10.ResponseDoc)
  * [InvoiceHeaderType](#mydata.models_1_0_10.InvoiceHeaderType)
  * [ExpensesClassificationsDoc](#mydata.models_1_0_10.ExpensesClassificationsDoc)
  * [InvoiceIncomeClassificationType](#mydata.models_1_0_10.InvoiceIncomeClassificationType)
  * [PaymentMethodsDoc](#mydata.models_1_0_10.PaymentMethodsDoc)
  * [AadeBookInvoiceType](#mydata.models_1_0_10.AadeBookInvoiceType)
    * [PaymentMethods](#mydata.models_1_0_10.AadeBookInvoiceType.PaymentMethods)
  * [IncomeClassificationsDoc](#mydata.models_1_0_10.IncomeClassificationsDoc)
  * [InvoicesDoc](#mydata.models_1_0_10.InvoicesDoc)

<a id="mydata.models_1_0_10"></a>

# mydata.models\_1\_0\_10

<a id="mydata.models_1_0_10.ErrorType"></a>

## ErrorType Objects

```python
@dataclass
class ErrorType()
```

**Attributes**:

- `message` - Μήνυμα Σφάλματος
- `code` - Κωδικός Σφάλαματος

<a id="mydata.models_1_0_10.InvoiceProviderType"></a>

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

<a id="mydata.models_1_0_10.ProviderInfoType"></a>

## ProviderInfoType Objects

```python
@dataclass
class ProviderInfoType()
```

**Attributes**:

- `vatnumber` - ΑΦΜ

<a id="mydata.models_1_0_10.ReceptionEmailsType"></a>

## ReceptionEmailsType Objects

```python
@dataclass
class ReceptionEmailsType()
```

**Attributes**:

- `email` - Email

<a id="mydata.models_1_0_10.AddressType"></a>

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

<a id="mydata.models_1_0_10.CancelledInvoiceType"></a>

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

<a id="mydata.models_1_0_10.EcrtokenType"></a>

## EcrtokenType Objects

```python
@dataclass
class EcrtokenType()
```

**Attributes**:

- `signing_author` - ECR id: Αριθμός μητρώου του φορολογικού
  μηχανισμού
- `session_number` - Μοναδικός 6-ψήφιος κωδικός που χαρακτηρίζει την
  κάθε συναλλαγή

<a id="mydata.models_1_0_10.ProviderSignatureType"></a>

## ProviderSignatureType Objects

```python
@dataclass
class ProviderSignatureType()
```

**Attributes**:

- `signing_author` - Provider’s Id
- `signature` - Υπογραφή

<a id="mydata.models_1_0_10.ShipType"></a>

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

<a id="mydata.models_1_0_10.TaxTotalsType"></a>

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

<a id="mydata.models_1_0_10.TransportDetailType"></a>

## TransportDetailType Objects

```python
@dataclass
class TransportDetailType()
```

**Attributes**:

- `vehicle_number` - Αριθμός Μεταφορικού Μέσου

<a id="mydata.models_1_0_10.ExpensesClassificationType"></a>

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

<a id="mydata.models_1_0_10.RequestedProviderDoc"></a>

## RequestedProviderDoc Objects

```python
@dataclass
class RequestedProviderDoc()
```

Παραστατικά από Πάροχο.

<a id="mydata.models_1_0_10.ReceptionProvidersType"></a>

## ReceptionProvidersType Objects

```python
@dataclass
class ReceptionProvidersType()
```

**Attributes**:

- `provider_info` - Πληροφορίες Παρόχου

<a id="mydata.models_1_0_10.OtherDeliveryNoteHeaderType"></a>

## OtherDeliveryNoteHeaderType Objects

```python
@dataclass
class OtherDeliveryNoteHeaderType()
```

**Attributes**:

- `loading_address` - Διεύθυνση Φόρτωσης
- `delivery_address` - Διεύθυνση Παράδοσης
- `start_shipping_branch` - Εγκατάσταση έναρξης διακίνησης (Εκδότη)
- `complete_shipping_branch` - Εγκατάσταση ολοκλήρωσης διακίνησης
  (Λήπτη)

<a id="mydata.models_1_0_10.PartyType"></a>

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

<a id="mydata.models_1_0_10.PaymentMethodDetailType"></a>

## PaymentMethodDetailType Objects

```python
@dataclass
class PaymentMethodDetailType()
```

**Attributes**:

- `type_value` - Τύπος Πληρωμής
- `amount` - Αναλογούν Ποσό
- `payment_method_info` - Λοιπές Πληροφορίες
- `tip_amount` - Φιλοδώρημα
- `transaction_id` - Μοναδική Ταυτότητα Πληρωμής
- `tid` - tid POS
- `providers_signature` - Υπογραφή Πληρωμής Παρόχου
- `ecrtoken` - Υπογραφή Πληρωμής ΦΗΜ με σύστημα λογισμικού (ERP)

<a id="mydata.models_1_0_10.InvoicesExpensesClassificationDetailType"></a>

## InvoicesExpensesClassificationDetailType Objects

```python
@dataclass
class InvoicesExpensesClassificationDetailType()
```

**Attributes**:

- `line_number` - Γραμμή Παραστατικού
- `expenses_classification_detail_data` - Λίστα Χαρακτηρισμών Εσόδων

<a id="mydata.models_1_0_10.IncomeClassificationType"></a>

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

<a id="mydata.models_1_0_10.ResponseType"></a>

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
- `payment_method_mark` - Μοναδικός Αριθμός Παραλαβής Τρόπου Πληρωμής
- `authentication_code` - Συμβολοσειρά Αυθεντικοποίησης Παρόχου
- `reception_providers` - Πάροχοι Λήπτη
- `reception_emails` - Email Παραλαβής
- `errors` - Λίστα Σφαλμάτων
- `status_code` - Κωδικός αποτελέσματος

<a id="mydata.models_1_0_10.EntityType"></a>

## EntityType Objects

```python
@dataclass
class EntityType()
```

**Attributes**:

- `type_value` - Κατηγορία
- `entity_data` - Στοιχεία Οντότητας

<a id="mydata.models_1_0_10.InvoiceRowType"></a>

## InvoiceRowType Objects

```python
@dataclass
class InvoiceRowType()
```

**Attributes**:

- `line_number` - ΑΑ Γραμμής
- `rec_type` - Είδος Γραμμής
- `taric_no` - Κωδικός Taric
- `item_code` - Κωδικός Είδους
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
- `other_measurement_unit_quantity` - Πλήθος Μονάδας Μέτρησης Τεμάχια
  Άλλα
- `other_measurement_unit_title` - Τίτλος Μονάδας Μέτρησης Τεμάχια
  Άλλα
- `not_vat195` - Ένδειξη μη συμμετοχής στο ΦΠΑ (έσοδα – εκροές)

<a id="mydata.models_1_0_10.InvoiceSummaryType"></a>

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

<a id="mydata.models_1_0_10.InvoiceExpensesClassificationType"></a>

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

<a id="mydata.models_1_0_10.InvoicesIncomeClassificationDetailType"></a>

## InvoicesIncomeClassificationDetailType Objects

```python
@dataclass
class InvoicesIncomeClassificationDetailType()
```

**Attributes**:

- `line_number` - Γραμμή Παραστατικού
- `income_classification_detail_data` - Λίστα Χαρακτηρισμών Εσόδων

<a id="mydata.models_1_0_10.PaymentMethodType"></a>

## PaymentMethodType Objects

```python
@dataclass
class PaymentMethodType()
```

**Attributes**:

- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης Παραστατικού
- `payment_method_mark` - Αποδεικτικό Λήψης Τρόπων Πληρωμής.
  Συμπληρώνεται από την Υπηρεσία
- `entity_vat_number` - ΑΦΜ Οντότητας Αναφοράς
  payment_method_details:

<a id="mydata.models_1_0_10.ResponseDoc"></a>

## ResponseDoc Objects

```python
@dataclass
class ResponseDoc()
```

Comment describing your root element.

<a id="mydata.models_1_0_10.InvoiceHeaderType"></a>

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
- `other_delivery_note_header` - Λοιπά Γενικά Στοιχεία Διακίνησης
- `is_delivery_note` - Ένδειξη Παραστατικού Διακίνησης
- `other_move_purpose_title` - Τίτλος της Λοιπής Αιτίας Διακίνησης
- `third_party_collection` - Ένδειξη Εισπράξης Τρίτων
- `multiple_connected_marks` - Πολλαπλά Συνδεόμενα MARKs
- `table_aa` - AA ΤΡΑΠΕΖΙOY (για Δελτία Παραγγελίας Εστίασης)
- `total_cancel_delivery_orders` - Ένδειξη συνολικής αναίρεσης
  Δελτίων Παραγελίας

<a id="mydata.models_1_0_10.ExpensesClassificationsDoc"></a>

## ExpensesClassificationsDoc Objects

```python
@dataclass
class ExpensesClassificationsDoc()
```

Χαρατηρισμοί Εξόδων Πρότυπων Παραστατικών ΑΑΔΕ.

<a id="mydata.models_1_0_10.InvoiceIncomeClassificationType"></a>

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

<a id="mydata.models_1_0_10.PaymentMethodsDoc"></a>

## PaymentMethodsDoc Objects

```python
@dataclass
class PaymentMethodsDoc()
```

Μέθοδοι Πληρωμής.

<a id="mydata.models_1_0_10.AadeBookInvoiceType"></a>

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

<a id="mydata.models_1_0_10.AadeBookInvoiceType.PaymentMethods"></a>

## PaymentMethods Objects

```python
@dataclass
class PaymentMethods()
```

**Attributes**:

- `payment_method_details` - Στοιχεία Πληρωμών

<a id="mydata.models_1_0_10.IncomeClassificationsDoc"></a>

## IncomeClassificationsDoc Objects

```python
@dataclass
class IncomeClassificationsDoc()
```

Χαρατηρισμοί Εσόδων Πρότυπων Παραστατικών ΑΑΔΕ.

<a id="mydata.models_1_0_10.InvoicesDoc"></a>

## InvoicesDoc Objects

```python
@dataclass
class InvoicesDoc()
```

Παραστατικό ΑΑΔΕ.

