#!/usr/bin/env bash
set -euo pipefail

# Stub script: invoice triage classifier
# Usage: ap_triage.sh "<invoice_id>"

INVOICE_ID="${1:-}"
if [[ -z "$INVOICE_ID" ]]; then
  echo "Usage: $0 <invoice_id>" >&2
  exit 2
fi

echo "[stub] Triage invoice: $INVOICE_ID"
echo "[stub] Next action: OCR -> validate -> 3-way match -> approve/hold"
