# Table of Contents

* [mydata.models\_2\_0\_0](#mydata.models_2_0_0)
  * [ErrorType](#mydata.models_2_0_0.ErrorType)
  * [InvoiceProviderType](#mydata.models_2_0_0.InvoiceProviderType)
  * [LocationType](#mydata.models_2_0_0.LocationType)
  * [PackagingDetailType](#mydata.models_2_0_0.PackagingDetailType)
  * [ProviderInfoType](#mydata.models_2_0_0.ProviderInfoType)
  * [RecalledStatementType](#mydata.models_2_0_0.RecalledStatementType)
  * [RejectDeliveryNoteRequest](#mydata.models_2_0_0.RejectDeliveryNoteRequest)
  * [RejectionDetailsType](#mydata.models_2_0_0.RejectionDetailsType)
  * [Statement](#mydata.models_2_0_0.Statement)
  * [ReceptionEmailsType](#mydata.models_2_0_0.ReceptionEmailsType)
  * [AddressType](#mydata.models_2_0_0.AddressType)
  * [CancelledInvoiceType](#mydata.models_2_0_0.CancelledInvoiceType)
  * [EcrtokenType](#mydata.models_2_0_0.EcrtokenType)
  * [InvoiceSummaryType](#mydata.models_2_0_0.InvoiceSummaryType)
  * [ProviderSignatureType](#mydata.models_2_0_0.ProviderSignatureType)
  * [ShipType](#mydata.models_2_0_0.ShipType)
  * [TaxTotalsType](#mydata.models_2_0_0.TaxTotalsType)
  * [ExpensesClassificationType](#mydata.models_2_0_0.ExpensesClassificationType)
  * [IncomeClassificationType](#mydata.models_2_0_0.IncomeClassificationType)
  * [ConfirmDeliveryOutcomeRequest](#mydata.models_2_0_0.ConfirmDeliveryOutcomeRequest)
  * [OutcomeDetailsType](#mydata.models_2_0_0.OutcomeDetailsType)
  * [PackingsDeclaration](#mydata.models_2_0_0.PackingsDeclaration)
  * [RequestedProviderDoc](#mydata.models_2_0_0.RequestedProviderDoc)
  * [RequestedStatement](#mydata.models_2_0_0.RequestedStatement)
  * [StatementDoc](#mydata.models_2_0_0.StatementDoc)
  * [TransportDetailType](#mydata.models_2_0_0.TransportDetailType)
  * [ReceptionProvidersType](#mydata.models_2_0_0.ReceptionProvidersType)
  * [InvoiceRowType](#mydata.models_2_0_0.InvoiceRowType)
  * [OtherDeliveryNoteHeaderType](#mydata.models_2_0_0.OtherDeliveryNoteHeaderType)
  * [PartyType](#mydata.models_2_0_0.PartyType)
  * [PaymentMethodDetailType](#mydata.models_2_0_0.PaymentMethodDetailType)
  * [InvoicesExpensesClassificationDetailType](#mydata.models_2_0_0.InvoicesExpensesClassificationDetailType)
  * [InvoicesIncomeClassificationDetailType](#mydata.models_2_0_0.InvoicesIncomeClassificationDetailType)
  * [DeliveryEventType](#mydata.models_2_0_0.DeliveryEventType)
  * [RequestedStatementDoc](#mydata.models_2_0_0.RequestedStatementDoc)
  * [ResponseType](#mydata.models_2_0_0.ResponseType)
  * [Transport](#mydata.models_2_0_0.Transport)
  * [EntityType](#mydata.models_2_0_0.EntityType)
  * [InvoiceExpensesClassificationType](#mydata.models_2_0_0.InvoiceExpensesClassificationType)
  * [InvoiceIncomeClassificationType](#mydata.models_2_0_0.InvoiceIncomeClassificationType)
  * [PaymentMethodType](#mydata.models_2_0_0.PaymentMethodType)
  * [ResponseDoc](#mydata.models_2_0_0.ResponseDoc)
  * [InvoiceHeaderType](#mydata.models_2_0_0.InvoiceHeaderType)
  * [ExpensesClassificationsDoc](#mydata.models_2_0_0.ExpensesClassificationsDoc)
  * [IncomeClassificationsDoc](#mydata.models_2_0_0.IncomeClassificationsDoc)
  * [PaymentMethodsDoc](#mydata.models_2_0_0.PaymentMethodsDoc)
  * [AadeBookInvoiceType](#mydata.models_2_0_0.AadeBookInvoiceType)
    * [PaymentMethods](#mydata.models_2_0_0.AadeBookInvoiceType.PaymentMethods)
  * [InvoicesDoc](#mydata.models_2_0_0.InvoicesDoc)

<a id="mydata.models_2_0_0"></a>

# mydata.models\_2\_0\_0

<a id="mydata.models_2_0_0.ErrorType"></a>

## ErrorType Objects

```python
@dataclass(kw_only=True)
class ErrorType()
```

**Attributes**:

- `message` - Μήνυμα Σφάλματος
- `code` - Κωδικός Σφάλαματος

<a id="mydata.models_2_0_0.InvoiceProviderType"></a>

## InvoiceProviderType Objects

```python
@dataclass(kw_only=True)
class InvoiceProviderType()
```

**Attributes**:

- `issuer_vat` - ΑΦΜ Εκδότη
- `invoice_provider_mark` - Μοναδικός Αριθμός Καταχώρησης
  παραστατικού Παρόχου
- `invoice_uid` - Αναγνωριστικό οντότητας
- `authentication_code` - Συμβολοσειρά Αυθεντικοποίησης Παραστατικού
  Παρόχου

<a id="mydata.models_2_0_0.LocationType"></a>

## LocationType Objects

```python
@dataclass(kw_only=True)
class LocationType()
```

Τοποθεσία.

**Attributes**:

- `longitude` - Γεωγραφικό Μήκος
- `latitude` - Γεωγραφικό Πλάτος

<a id="mydata.models_2_0_0.PackagingDetailType"></a>

## PackagingDetailType Objects

```python
@dataclass(kw_only=True)
class PackagingDetailType()
```

Πληροφορίες Συσκευασίας.

**Attributes**:

- `packaging_type` - Είδος Συσκευασίας
- `quantity` - Πλήθος
- `other_packaging_type_title` - Τίτλος για Λοιπά Είδη Συσκευασίας

<a id="mydata.models_2_0_0.ProviderInfoType"></a>

## ProviderInfoType Objects

```python
@dataclass(kw_only=True)
class ProviderInfoType()
```

**Attributes**:

- `vatnumber` - ΑΦΜ

<a id="mydata.models_2_0_0.RecalledStatementType"></a>

## RecalledStatementType Objects

```python
@dataclass(kw_only=True)
class RecalledStatementType()
```

**Attributes**:

- `statement_id` - Μοναδικός Κωδικός Αρχικής Δήλωσης που έχει
  ανακληθεί
- `entity_vat_number` - ΑΦΜ Υπόχρεης Επιχείρησης
- `recall_id` - Μοναδικός Κωδικός Καταχώρησης της Ανάκλησης
- `recall_status` - Κατάσταση Ανάκλησης
- `recall_date` - Ημερομηνία Πλήρης Ανάκλησης. Συμπληρώνεται από
  Πελάτη
- `transaction_date` - Ημερομηνία Ανάκλησης Συναλλαγής. Συμπληρώνεται
  από την Υπηρεσία
- `recall_vat_number` - ΑΦΜ Ανάκλησης Δήλωσης

<a id="mydata.models_2_0_0.RejectDeliveryNoteRequest"></a>

## RejectDeliveryNoteRequest Objects

```python
@dataclass(kw_only=True)
class RejectDeliveryNoteRequest()
```

Αίτημα Απόρριψης.

**Attributes**:

- `qr_url` - Το url qr του δελτίου
- `rejection_reason` - Περιγραφή του λόγου απόρριψης.

<a id="mydata.models_2_0_0.RejectionDetailsType"></a>

## RejectionDetailsType Objects

```python
@dataclass(kw_only=True)
class RejectionDetailsType()
```

Ένδειξη απόρριψης του παραστατικού διακίνησης από τον παραλήπτη του.

<a id="mydata.models_2_0_0.Statement"></a>

## Statement Objects

```python
@dataclass(kw_only=True)
class Statement()
```

**Attributes**:

- `statement_id` - Μοναδικός Αριθμός Δήλωσης. Συμπληρώνεται από την
  Υπηρεσία
- `submission_date_time` - Ημερομηνία υποβολής Δήλωσης. Συμπληρώνεται
  από την Υπηρεσία
- `entity_vat_number` - ΑΦΜ Υπόχρεης Επιχείρησης
- `liable_user_category` - Κατηγορία Υπόχρεου
- `provider_type` - Τύπος Παρόχου
- `is_b2_btransactions` - Συναλλαγές B2B
- `is_b2_ctransactions` - Συναλλαγές B2C
- `is_b2_gtransactions` - Συναλλαγές B2G
- `provider_vat_number` - ΑΦΜ Παρόχου
- `provider_licence_number` - Αριθμός Αδείας Παρόχου
- `provider_contract_number` - Αριθμός Σύμβασης Παρόχου
- `provider_contract_conclusion_date` - Ημερομηνία σύναψης σύμβασης
  οντότητας με τον Πάροχο
- `provider_contract_activation_date` - Ημερομηνία έναρξης ισχύος της
  σύμβασης
- `issue_start_date` - Ημερομηνία έναρξης έκδοσης στοιχειών για
  συναλλαγές
- `issue_stop_date` - Ημερομηνία διακοπής έκδοσης στοιχείων για
  συναλλαγές
- `internet_provider` - Παρόχος Διαδικτύου Οντότητας-Εκδότη
- `internet_provider_contract_number` - Αριθμός Σύμβασης Οντότητας-
  Εκδότη με Πάροχο Διαδικτύου
- `internet_provider_contract_date` - Ημερομηνία Σύμβασης Οντότητας-
  Εκδότη με Πάροχο Διαδικτύου

<a id="mydata.models_2_0_0.ReceptionEmailsType"></a>

## ReceptionEmailsType Objects

```python
@dataclass(kw_only=True)
class ReceptionEmailsType()
```

**Attributes**:

- `email` - Email

<a id="mydata.models_2_0_0.AddressType"></a>

## AddressType Objects

```python
@dataclass(kw_only=True)
class AddressType()
```

**Attributes**:

  street:
- `number` - Αριθμός
- `postal_code` - ΤΚ
  city:

<a id="mydata.models_2_0_0.CancelledInvoiceType"></a>

## CancelledInvoiceType Objects

```python
@dataclass(kw_only=True)
class CancelledInvoiceType()
```

**Attributes**:

- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης του ακυρωμένου
  Παραστατικού
- `cancellation_mark` - Μοναδικός Αριθμός Καταχώρησης της Ακύρωσης
- `cancellation_date` - Ημερομηνία Ακύρωσης Παραστατικού

<a id="mydata.models_2_0_0.EcrtokenType"></a>

## EcrtokenType Objects

```python
@dataclass(kw_only=True)
class EcrtokenType()
```

**Attributes**:

- `signing_author` - ECR id: Αριθμός μητρώου του φορολογικού
  μηχανισμού
- `session_number` - Μοναδικός 6-ψήφιος κωδικός που χαρακτηρίζει την
  κάθε συναλλαγή

<a id="mydata.models_2_0_0.InvoiceSummaryType"></a>

## InvoiceSummaryType Objects

```python
@dataclass(kw_only=True)
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

<a id="mydata.models_2_0_0.ProviderSignatureType"></a>

## ProviderSignatureType Objects

```python
@dataclass(kw_only=True)
class ProviderSignatureType()
```

**Attributes**:

- `signing_author` - Provider’s Id
- `signature` - Υπογραφή
- `end_to_nd_reference_id` - Το μοναδικό αναγνωριστικό αιτήματος
  πληρωμής (για πληρωμές IRIS)

<a id="mydata.models_2_0_0.ShipType"></a>

## ShipType Objects

```python
@dataclass(kw_only=True)
class ShipType()
```

**Attributes**:

- `application_id` - Αριθμός Δήλωσης διενέργειας δραστηριότητας
- `application_date` - Ημερομηνία Δήλωσης
  doy:
- `ship_id` - Στοιχεία Πλοίου

<a id="mydata.models_2_0_0.TaxTotalsType"></a>

## TaxTotalsType Objects

```python
@dataclass(kw_only=True)
class TaxTotalsType()
```

**Attributes**:

- `tax_type` - Είδος Φόρου
- `tax_category` - Κατηγορία Φόρου
- `underlying_value` - Υποκείμενη Αξία
- `tax_amount` - Ποσό Φόρου
  id:

<a id="mydata.models_2_0_0.ExpensesClassificationType"></a>

## ExpensesClassificationType Objects

```python
@dataclass(kw_only=True)
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

<a id="mydata.models_2_0_0.IncomeClassificationType"></a>

## IncomeClassificationType Objects

```python
@dataclass(kw_only=True)
class IncomeClassificationType()
```

**Attributes**:

- `classification_type` - Κωδικός Χαρακτηρισμού
- `classification_category` - Κατηγορία Χαρακτηρισμού
- `amount` - Ποσό Χαρακτηρισμού
- `id` - Μοναδικός Αριθμός Χαρακτηρισμού

<a id="mydata.models_2_0_0.ConfirmDeliveryOutcomeRequest"></a>

## ConfirmDeliveryOutcomeRequest Objects

```python
@dataclass(kw_only=True)
class ConfirmDeliveryOutcomeRequest()
```

Επιβεβαίωση-Δήλωση Παράδοσης-Παραλαβής Παραστατικού.

**Attributes**:

- `qr_url` - Το url qr του δελτίου
- `outcome` - Αποτέλεσμα
- `delivered_without_recipient` - Ένδειξη  παράδοσης χωρίς τη φυσική
  παρουσία του παραλήπτη.
- `delivered_packaging` - Λίστα με τις συσκευασίες και τις ποσότητες
  που παραδόθηκαν.

<a id="mydata.models_2_0_0.OutcomeDetailsType"></a>

## OutcomeDetailsType Objects

```python
@dataclass(kw_only=True)
class OutcomeDetailsType()
```

Λεπτομέρειες της παράδοσης/παραλαβής των αγαθών (από μεταφορέας ή
παραλήπτη).

**Attributes**:

- `outcome` - Αποτέλεσμα Παράδοσης
  delivered_without_recipient:
  delivered_packaging:

<a id="mydata.models_2_0_0.PackingsDeclaration"></a>

## PackingsDeclaration Objects

```python
@dataclass(kw_only=True)
class PackingsDeclaration()
```

Δήλωση Συσκευασιών.

**Attributes**:

- `packages` - Συσκευασίες

<a id="mydata.models_2_0_0.RequestedProviderDoc"></a>

## RequestedProviderDoc Objects

```python
@dataclass(kw_only=True)
class RequestedProviderDoc()
```

Παραστατικά από Πάροχο.

<a id="mydata.models_2_0_0.RequestedStatement"></a>

## RequestedStatement Objects

```python
@dataclass(kw_only=True)
class RequestedStatement()
```

**Attributes**:

  statement:
- `accept_vat_number` - ΑΦΜ αποδοχής δήλωσης (αφορά Υπόχρεη
  Επιχείρηση)
- `accept_date` - Ημερομηνία αποδοχής δήλωσης από Υπόχρεη Επιχείρηση.
  Συμπληρώνεται από την Υπηρεσία
  recall_statement:

<a id="mydata.models_2_0_0.StatementDoc"></a>

## StatementDoc Objects

```python
@dataclass(kw_only=True)
class StatementDoc()
```

Δήλωση έκδοσης στοιχείων μέσω Παρόχου ή ΙδιοΠαρόχου.

<a id="mydata.models_2_0_0.TransportDetailType"></a>

## TransportDetailType Objects

```python
@dataclass(kw_only=True)
class TransportDetailType()
```

**Attributes**:

- `vehicle_number` - Αριθμός Μεταφορικού Μέσου (Αριθμός
  κυκλοφορίας/Όνομα πλωτού μέσου/Κωδικός Δρομολογίου ή
  πτήσης/Διακίνηση άνευ Μεταφορικού Μέσου)
- `transport_type` - Είδος Μεταφορικού Μέσου
- `time_stamp` - Χρονοσφραγίδα
- `carrier_vat_number` - ΑΦΜ Μεταφορικής Εταιρείας
- `p_number` - Αριθμός κυκλοφορίας "Ρ" (αριθμός κυκλοφορίας του
  επικαθήμενου/ρυμουλκούμενου οχήματος)
- `location` - Τοποθεσία Μεταφόρτωσης

<a id="mydata.models_2_0_0.ReceptionProvidersType"></a>

## ReceptionProvidersType Objects

```python
@dataclass(kw_only=True)
class ReceptionProvidersType()
```

**Attributes**:

- `provider_info` - Πληροφορίες Παρόχου

<a id="mydata.models_2_0_0.InvoiceRowType"></a>

## InvoiceRowType Objects

```python
@dataclass(kw_only=True)
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
- `stamp_duty_amount` - Ποσό Ψηφιακού Τέλους συναλλαγής
- `stamp_duty_percent_category` - Κατηγορία Συντελεστή Ψηφιακού
  Τέλους συναλλαγής
- `fees_amount` - Ποσό Τελών
- `fees_percent_category` - Κατηγορία Συντελεστή Τελών
- `other_taxes_percent_category` - Κατηγορία Συντελεστή Λοιπών Φόρων
- `other_taxes_amount` - Ποσό Φόρου Διαμονης
- `deductions_amount` - Ποσό Κρατήσεων
- `line_comments` - Σχόλια Γραμμής
- `quantity15` - Ποσότητα Θερμοκρασίας 15 βαθμών
- `other_measurement_unit_quantity` - Πλήθος Μονάδας Μέτρησης Τεμάχια
  Άλλα
- `other_measurement_unit_title` - Τίτλος Μονάδας Μέτρησης Τεμάχια
  Άλλα
- `not_vat195` - Ένδειξη μη συμμετοχής στο ΦΠΑ (έσοδα – εκροές)
- `move_purpose_line` - Σκοπός Διακίνησης Γραμμής
- `other_move_purpose_line_title` - Τίτλος της Λοιπής Αιτίας
  Διακίνησης Γραμμής

<a id="mydata.models_2_0_0.OtherDeliveryNoteHeaderType"></a>

## OtherDeliveryNoteHeaderType Objects

```python
@dataclass(kw_only=True)
class OtherDeliveryNoteHeaderType()
```

**Attributes**:

- `loading_address` - Διεύθυνση Φόρτωσης
- `delivery_address` - Διεύθυνση Παράδοσης
- `start_shipping_branch` - Εγκατάσταση έναρξης διακίνησης (Εκδότη)
- `complete_shipping_branch` - Εγκατάσταση ολοκλήρωσης διακίνησης
  (Λήπτη)

<a id="mydata.models_2_0_0.PartyType"></a>

## PartyType Objects

```python
@dataclass(kw_only=True)
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

<a id="mydata.models_2_0_0.PaymentMethodDetailType"></a>

## PaymentMethodDetailType Objects

```python
@dataclass(kw_only=True)
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

<a id="mydata.models_2_0_0.InvoicesExpensesClassificationDetailType"></a>

## InvoicesExpensesClassificationDetailType Objects

```python
@dataclass(kw_only=True)
class InvoicesExpensesClassificationDetailType()
```

**Attributes**:

- `line_number` - Γραμμή Παραστατικού
- `expenses_classification_detail_data` - Λίστα Χαρακτηρισμών Εσόδων

<a id="mydata.models_2_0_0.InvoicesIncomeClassificationDetailType"></a>

## InvoicesIncomeClassificationDetailType Objects

```python
@dataclass(kw_only=True)
class InvoicesIncomeClassificationDetailType()
```

**Attributes**:

- `line_number` - Γραμμή Παραστατικού
- `income_classification_detail_data` - Λίστα Χαρακτηρισμών Εσόδων

<a id="mydata.models_2_0_0.DeliveryEventType"></a>

## DeliveryEventType Objects

```python
@dataclass(kw_only=True)
class DeliveryEventType()
```

Ένα γεγονός (σταθμός) στον κύκλο ζωής (lifecycle) παράδοσης του δελτίου
διακίνησης.

**Attributes**:

- `event_type` - Ο τύπος του Συμβάντος (e.g., "RegisterTransfer",
  "ConfirmOutcome", "Rejection").
- `event_timestamp` - Χρονοσφραγίδα συμβάντος
- `actor_vat` - ΑΦΜ Χρήστη που δημιούργησε το συμβάν.
- `mark` - Μοναδικός Αριθμός Καταχώρησης Συμβάντος (παράγεται από το
  myDATA)
- `transport_details` - Λεπτομέρειες Εκκίνησης Διακίνησης -
  Μεταφορτώσεις Διακίνησης
- `outcome_details` - Λεπτομέρειες της παράδοσης/παραλαβής των αγαθών
  (από μεταφορέας ή παραλήπτη)
- `rejection_details` - Ένδειξη απόρριψης του παραστατικού διακίνησης
  από τον παραλήπτη του

<a id="mydata.models_2_0_0.RequestedStatementDoc"></a>

## RequestedStatementDoc Objects

```python
@dataclass(kw_only=True)
class RequestedStatementDoc()
```

Δηλώσεις έκδοσης στοιχείων μέσω Παρόχου ή ΙδιοΠαρόχου.

<a id="mydata.models_2_0_0.ResponseType"></a>

## ResponseType Objects

```python
@dataclass(kw_only=True)
class ResponseType()
```

**Attributes**:

- `index` - ΑΑ γραμμής οντότητας
- `invoice_uid` - Αναγνωριστικό οντότητας
- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης παραστατικού
- `classification_mark` - Μοναδικός Αριθμός Παραλαβής Χαρακτηρισμού
- `cancellation_mark` - Μοναδικός Αριθμός Ακύρωσης
- `payment_method_mark` - Μοναδικός Αριθμός Παραλαβής Τρόπου Πληρωμής
- `authentication_code` - Συμβολοσειρά Αυθεντικοποίησης Παρόχου
- `reception_providers` - Πάροχοι Λήπτη
- `reception_emails` - Email Παραλαβής
- `qr_url` - QR Code Url
- `statement_id` - Μοναδικός Αριθμός Δήλωσης
- `recall_id` - Μοναδικός Κωδικός Καταχώρισης της Ανάκλησης
- `transfer_mark` - Μοναδικός Αριθμός Εκκίνησης/Μεταφόρτωσης
  Διακίνησης
- `reject_mark` - Μοναδικός Αριθμός Απόρριψης Διακίνησης
- `errors` - Λίστα Σφαλμάτων
- `status_code` - Κωδικός αποτελέσματος

<a id="mydata.models_2_0_0.Transport"></a>

## Transport Objects

```python
@dataclass(kw_only=True)
class Transport()
```

Μεταφόρτωση.

**Attributes**:

- `transport_mark` - Αποδεικτικό Λήψης Μεταφόρτωσης. Συμπληρώνεται
  από την Υπηρεσία
- `qr_url` - Το url qr του δελτίου
- `transport_detail` - Λεπτομέρειες Μεταφόρτωσης

<a id="mydata.models_2_0_0.EntityType"></a>

## EntityType Objects

```python
@dataclass(kw_only=True)
class EntityType()
```

**Attributes**:

- `type_value` - Κατηγορία
- `entity_data` - Στοιχεία Οντότητας

<a id="mydata.models_2_0_0.InvoiceExpensesClassificationType"></a>

## InvoiceExpensesClassificationType Objects

```python
@dataclass(kw_only=True)
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

<a id="mydata.models_2_0_0.InvoiceIncomeClassificationType"></a>

## InvoiceIncomeClassificationType Objects

```python
@dataclass(kw_only=True)
class InvoiceIncomeClassificationType()
```

**Attributes**:

- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης Παραστατικού
- `classification_mark` - Αποδεικτικό Λήψης Χαρακτηρισμού Εσόδων.
  Συμπληρώνεται από την Υπηρεσία
- `entity_vat_number` - ΑΦΜ Οντότητας Αναφοράς
- `transaction_mode` - Αιτιολογία Συναλλαγής
  invoices_income_classification_details:

<a id="mydata.models_2_0_0.PaymentMethodType"></a>

## PaymentMethodType Objects

```python
@dataclass(kw_only=True)
class PaymentMethodType()
```

**Attributes**:

- `invoice_mark` - Μοναδικός Αριθμός Καταχώρησης Παραστατικού
- `payment_method_mark` - Αποδεικτικό Λήψης Τρόπων Πληρωμής.
  Συμπληρώνεται από την Υπηρεσία
- `entity_vat_number` - ΑΦΜ Οντότητας Αναφοράς
  payment_method_details:

<a id="mydata.models_2_0_0.ResponseDoc"></a>

## ResponseDoc Objects

```python
@dataclass(kw_only=True)
class ResponseDoc()
```

Comment describing your root element.

<a id="mydata.models_2_0_0.InvoiceHeaderType"></a>

## InvoiceHeaderType Objects

```python
@dataclass(kw_only=True)
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
- `dispatch_date` - Ημερομηνία  Έναρξης Αποστολής (Προγραμματισμένη -
  Σχεδιασμένη - Εκτιμώμενη)
- `dispatch_time` - Ώρα Έναρξης Αποστολής (Προγραμματισμένη -
  Σχεδιασμένη - Εκτιμώμενη)
- `vehicle_number` - Αριθμός Οχήματος (Προγραμματισμένο -
  Σχεδιασμένο)
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
- `reverse_delivery_note` - Αντίστροφη Διακίνηση
- `reverse_delivery_note_purpose` - Αιτία Έκδοσης Αντίστροφης
  Διακίνησης
- `to_weigh` - Ένδειξη Προς Ζύγιση

<a id="mydata.models_2_0_0.ExpensesClassificationsDoc"></a>

## ExpensesClassificationsDoc Objects

```python
@dataclass(kw_only=True)
class ExpensesClassificationsDoc()
```

Χαρατηρισμοί Εξόδων Πρότυπων Παραστατικών ΑΑΔΕ.

<a id="mydata.models_2_0_0.IncomeClassificationsDoc"></a>

## IncomeClassificationsDoc Objects

```python
@dataclass(kw_only=True)
class IncomeClassificationsDoc()
```

Χαρατηρισμοί Εσόδων Πρότυπων Παραστατικών ΑΑΔΕ.

<a id="mydata.models_2_0_0.PaymentMethodsDoc"></a>

## PaymentMethodsDoc Objects

```python
@dataclass(kw_only=True)
class PaymentMethodsDoc()
```

Μέθοδοι Πληρωμής.

<a id="mydata.models_2_0_0.AadeBookInvoiceType"></a>

## AadeBookInvoiceType Objects

```python
@dataclass(kw_only=True)
class AadeBookInvoiceType()
```

**Attributes**:

- `uid` - Αναγνωριστικό Παραστατικού
- `mark` - Μοναδικός Αριθμός Καταχώρησης Παραστατικού
- `cancelled_by_mark` - Μοναδικός Αριθμός Καταχώρησης Ακυρωτικού
- `authentication_code` - Συμβολοσειρά Αυθεντικοποίησης Παρόχου
- `transmission_failure` - Αδυναμία Επικοινωνίας Παρόχου ή Αδυναμία
  διαβίβασης ERP ή διαβίβαση μέσω Παρόχου για τις οντότητες
  άρθρου 5, 2η παράγραφος της περ. 1γ
- `issuer` - Στοιχεία Εκδότη
- `counterpart` - Στοιχεία Λήπτη
- `invoice_header` - Γενικά Στοιχεία
- `payment_methods` - Πληρωμές
- `invoice_details` - Λεπτομέρειες Παραστατικού
- `taxes_totals` - Σύνολα Φόρων
- `invoice_summary` - Συγκεντρωτικά Στοιχεία
- `qr_code_url` - QR Code Url
- `downloading_invoice_url` - Url με το οποίο ο λήπτης του
  παραστατικού θα μπορεί να το λαμβάνει
- `packings_declarations` - Δηλώσεις Συσκευασιών
- `invoive_delivery_status` - Κατάσταση (Status) Παραστατικού Δελτίου
  Διακίνησης

<a id="mydata.models_2_0_0.AadeBookInvoiceType.PaymentMethods"></a>

## PaymentMethods Objects

```python
@dataclass(kw_only=True)
class PaymentMethods()
```

**Attributes**:

- `payment_method_details` - Στοιχεία Πληρωμών

<a id="mydata.models_2_0_0.InvoicesDoc"></a>

## InvoicesDoc Objects

```python
@dataclass(kw_only=True)
class InvoicesDoc()
```

Παραστατικό ΑΑΔΕ.

