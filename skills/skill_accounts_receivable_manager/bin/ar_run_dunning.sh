#!/usr/bin/env bash
set -euo pipefail

# Stub script: run dunning workflow
# Usage: ar_run_dunning.sh "<as_of_date>"

AS_OF="${1:-}"
if [[ -z "$AS_OF" ]]; then
  echo "Usage: $0 <as_of_date>" >&2
  exit 2
fi

echo "[stub] Run dunning as-of $AS_OF"
echo "[stub] Produce reminders + escalation tasks based on aging buckets"
