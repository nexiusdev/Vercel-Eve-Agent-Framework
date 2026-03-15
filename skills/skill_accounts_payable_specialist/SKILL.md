# Accounts Payable Specialist (skill_accounts_payable_specialist)

Handles the full accounts payable lifecycle from invoice receipt through payment execution. Automates three-way matching, manages approval workflows, and ensures timely vendor payments while maintaining accurate records for month-end close.

## What this skill does

### Invoice Processing (target: 95% automated)
- OCR extraction
- Data validation
- Three-way matching (PO ↔ receipt ↔ invoice)

### Payment Scheduling (target: 90% automated)
- Due date tracking
- Cash flow optimization
- Batch processing

### Vendor Reconciliation (target: 85% automated)
- Statement matching
- Discrepancy detection
- Auto-resolution (rules-based)

## Inputs this skill expects
- Vendor invoice (PDF/image) and/or extracted invoice fields
- Purchase Order (PO) data
- Goods receipt / service confirmation data
- Vendor master data (bank details, terms, tax IDs)
- Approval policy (thresholds, owners, SLA)

## Core workflows

### 1) Invoice intake → OCR → validation
1. Receive invoice (email/upload/scan)
2. OCR extract key fields (vendor, invoice #, date, due date, line items, totals, tax)
3. Validate:
   - Required fields present
   - Vendor exists and is active
   - Duplicate invoice detection (vendor + invoice # + amount)
   - Math checks (subtotal + tax = total)

### 2) Three-way match
- Match invoice lines to PO lines (qty/price/tolerance)
- Verify receipt exists (partial receipts supported)
- Outcomes:
  - **Auto-approve** if within tolerance and policy allows
  - **Route for approval** if exceptions found (price variance, missing receipt, no PO)
  - **Hold** if vendor/bank/tax validation fails

### 3) Approval workflow
- Assign approver based on:
  - Cost center / department
  - Invoice amount thresholds
  - Exception type
- Track SLA and escalate if overdue

### 4) Payment scheduling & execution
- Build payment runs by:
  - Due date window
  - Cash position constraints
  - Priority vendors (utilities, critical suppliers)
- Batch payments; generate remittance advice

### 5) Month-end close readiness
- Ensure postings are complete and auditable:
  - Invoice status, approval trail
  - Accrual flags (unreceived invoices)
  - A/P aging and GR/IR reconciliation

### 6) Vendor statement reconciliation
- Match vendor statements to ledger
- Detect discrepancies:
  - Missing invoices/credits
  - Unapplied payments
  - Duplicate postings
- Auto-resolve common cases via rules; otherwise open a case

## Outputs
- Clean, validated invoice record
- Match status + exception list
- Approval request package (context + variance summary)
- Scheduled payment batch + remittance advice
- Reconciliation report + discrepancy cases

## Templates
This folder includes templates you can adapt:
- `templates/approval_request.md`
- `templates/vendor_discrepancy_email.md`
- `templates/remittance_advice.md`

## Scripts (placeholders)
This repo is framework-only. The scripts in `bin/` are stubs you can wire to your ERP/accounting stack.
- `bin/ap_triage.sh` — classify invoice + next action
- `bin/ap_payment_run.sh` — generate a payment batch plan

## Guardrails
- Never change vendor bank details without an explicit verified workflow.
- Always keep an audit trail: who/what/when for extraction, edits, approvals, and payments.
- Respect segregation of duties (SoD): creator ≠ approver ≠ payer.
