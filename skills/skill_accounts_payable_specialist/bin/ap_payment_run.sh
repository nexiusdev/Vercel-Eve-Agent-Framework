#!/usr/bin/env bash
set -euo pipefail

# Stub script: payment run planner
# Usage: ap_payment_run.sh "<from_due_date>" "<to_due_date>"

FROM="${1:-}"
TO="${2:-}"
if [[ -z "$FROM" || -z "$TO" ]]; then
  echo "Usage: $0 <from_due_date> <to_due_date>" >&2
  exit 2
fi

echo "[stub] Build payment batch for invoices due between $FROM and $TO"
echo "[stub] Consider cash flow constraints + vendor priority"
