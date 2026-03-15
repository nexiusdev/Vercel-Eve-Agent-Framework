# Accounts Receivable Manager (skill_accounts_receivable_manager)

Oversees the entire order-to-cash cycle including invoice generation, payment tracking, collections management, and cash application. Reduces Days Sales Outstanding (DSO) through automated follow-ups and intelligent escalation workflows.

## Expected outcomes
- **40% DSO reduction** (Days Sales Outstanding improvement)
- **98% collection rate** (on-time payment collection)
- **85% faster cash application speed** (automated payment matching)

## What this skill does

### Invoice Generation (target: 95% automated)
- Template management
- Recurring billing
- Multi-currency

### Collections Management (target: 88% automated)
- Dunning automation
- Escalation rules
- Payment reminders

### Cash Application (target: 85% automated)
- Payment matching
- Partial payments
- Bank reconciliation

## Inputs this skill expects
- Customer master data (billing contacts, payment terms, credit limits)
- Sales orders / contracts / subscriptions
- Delivery or service fulfillment confirmation
- Invoice templates + tax rules
- Bank statement / payment gateway exports
- Collections policy (dunning cadence, escalation tiers)

## Core workflows

### 1) Invoice generation & delivery
1. Determine billable items (orders shipped, services delivered, subscription period)
2. Generate invoice from templates (multi-currency, tax/VAT where applicable)
3. Deliver invoice (email + portal) and log delivery evidence
4. Post to AR ledger with correct dimensions (customer, region, product, etc.)

### 2) Payment tracking
- Monitor open invoices and due dates
- Detect promise-to-pay commitments and track compliance
- Identify disputes early (short payments, deductions)

### 3) Collections (dunning)
- Automated reminders based on aging buckets (e.g., -3 days, +1, +7, +14, +30)
- Escalation rules:
  - Tier 1: friendly reminder
  - Tier 2: firm reminder + call task
  - Tier 3: manager escalation
  - Tier 4: credit hold / external collections (per policy)

### 4) Cash application
- Import bank statement / gateway transactions
- Match payments to invoices using:
  - invoice # / reference
  - amount & currency
  - customer and remitter name similarity
  - tolerance rules for fees / FX / rounding
- Support partial payments and split applications
- Create exception queue for unmatched items

### 5) Bank reconciliation
- Reconcile applied cash vs statement totals
- Flag variances (timing differences, chargebacks, fees)

## Outputs
- Issued invoice package + delivery log
- Aging report + collection status per customer
- Dunning activity log + escalation actions
- Cash application report (matched/unmatched, partials)
- Reconciliation summary

## Templates
- `templates/invoice_email.md`
- `templates/dunning_email_tier1.md`
- `templates/dunning_email_tier2.md`
- `templates/escalation_note.md`

## Scripts (placeholders)
Framework-only stubs you can wire to ERP/CRM/billing systems:
- `bin/ar_generate_invoice.sh`
- `bin/ar_run_dunning.sh`
- `bin/ar_cash_apply.sh`

## Guardrails
- Respect customer communication preferences and local regulations.
- Always preserve an audit trail for invoice changes and collections contacts.
- Avoid aggressive escalation when a dispute case is open (unless policy allows).
