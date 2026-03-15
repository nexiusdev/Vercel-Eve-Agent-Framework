#!/usr/bin/env bash
set -euo pipefail

# Stub script: cash application matcher
# Usage: ar_cash_apply.sh "<bank_statement_file.csv>"

FILE="${1:-}"
if [[ -z "$FILE" ]]; then
  echo "Usage: $0 <bank_statement_file.csv>" >&2
  exit 2
fi

echo "[stub] Import bank statement: $FILE"
echo "[stub] Match payments to invoices (refs/amount/currency/name similarity)"
echo "[stub] Output matched/unmatched + partial allocations"
