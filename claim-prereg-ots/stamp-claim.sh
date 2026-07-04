#!/usr/bin/env bash
# SHA-pinned prediction pre-registration + OpenTimestamps anchor (fully automated).
#
# Appends a prediction under its frozen commit SHA in claims_by_hash.md, stamps
# the index with OpenTimestamps, commits the pending receipt, then BLOCKS until
# the proof is confirmed on the Bitcoin blockchain and commits the finalized
# receipt. Refuses to run on main (or a detached HEAD): cut a work branch first.
#
# Usage:
#   ./claim-prereg-ots/stamp-claim.sh <commit-ish> "<prediction text>"   # add entry + stamp + anchor
#   ./claim-prereg-ots/stamp-claim.sh --stamp-only                       # (re)stamp current index + anchor
#
# !!! RUNS SYNCHRONOUSLY FOR ~1 HOUR — it blocks polling for Bitcoin confirmation.
#
# Requires: brew install opentimestamps-client   (provides `ots`)
#
# Discipline: stamp BEFORE the predicted readout exists; treat entries as append-only.
#
# Env overrides: OTS_POLL_INTERVAL (sec, default 300), OTS_POLL_MAX_MIN (default 180).
#
# Verify a claim later (each receipt stamps the index as of its own commit):
#   R=claim-prereg-ots/<date>-<tag>.ots
#   C=$(git log --diff-filter=A --format=%H -- "${R}" | head -1)
#   git show "${C}":claim-prereg-ots/claims_by_hash.md > /tmp/snap
#   ots verify -f /tmp/snap "${R}"

set -euo pipefail

usage() {
  cat >&2 <<'EOF'
usage:
  stamp-claim.sh <commit-ish> "<prediction text>"   add entry under its SHA + stamp + anchor
  stamp-claim.sh --stamp-only                        (re)stamp the current index + anchor

  ####################################################################
  ##  !!! WARNING: THIS RUNS SYNCHRONOUSLY FOR ~1 HOUR !!!          ##
  ##  After stamping it BLOCKS, polling until the OpenTimestamps    ##
  ##  proof is confirmed on Bitcoin (~1h, sometimes longer), then   ##
  ##  commits the finalized receipt. The PENDING receipt is         ##
  ##  committed first, so Ctrl-C is safe and the wait is resumable. ##
  ##  Run it where you can leave it, or background it with `&`.      ##
  ####################################################################
EOF
  exit 2
}

POLL_INTERVAL="${OTS_POLL_INTERVAL:-300}"   # seconds between confirmation checks
POLL_MAX_MIN="${OTS_POLL_MAX_MIN:-180}"     # stop polling after this many minutes

commit_paths() {  # <message> <path>... — commit only the given paths; return 1 if nothing changed
  local msg="${1}"; shift
  git -C "${ROOT}" add "${@}"
  git -C "${ROOT}" diff --cached --quiet -- "${@}" && return 1
  git -C "${ROOT}" commit -q -m "${msg}" -- "${@}"
}

ROOT="$(git rev-parse --show-toplevel)"
DIR="${ROOT}/claim-prereg-ots"
INDEX="${DIR}/claims_by_hash.md"
DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

if ! command -v ots >/dev/null 2>&1; then
  echo "missing 'ots' — run: brew install opentimestamps-client" >&2
  exit 1
fi

# ---- parse + validate (read-only; usage-exit must happen before any branch cut) ----
MODE="${1:-}"
[[ -n "${MODE}" ]] || usage

if [[ "${MODE}" == "--stamp-only" ]]; then
  TAG="stamp"
else
  COMMITISH="${1}"
  shift
  PRED="${*}"
  [[ -n "${PRED}" ]] || usage
  SHA="$(git -C "${ROOT}" rev-parse "${COMMITISH}")"
  TAG="${SHA:0:12}"
fi

# ---- guard: never commit on main; refuse a detached HEAD ----
BRANCH="$(git -C "${ROOT}" rev-parse --abbrev-ref HEAD)"
if [[ "${BRANCH}" == "HEAD" ]]; then
  echo "refusing to run on a detached HEAD — check out a work branch first." >&2
  exit 1
fi
if [[ "${BRANCH}" == "main" ]]; then
  echo "refusing to run on 'main' — cut a work branch first (e.g. git checkout -b analysis/prereg-<topic>)." >&2
  exit 1
fi

# ---- mutate: ensure index + append the entry ----
[[ -f "${INDEX}" ]] || printf '# Pre-Registered Predictions By SHA\n' > "${INDEX}"
if [[ "${MODE}" != "--stamp-only" ]]; then
  if grep -qxF "## ${SHA}" "${INDEX}"; then
    # SHA section already present — insert the bullet right after its heading
    awk -v h="## ${SHA}" -v b=" - ${PRED}" '{ print } $0 == h { print b }' "${INDEX}" > "${INDEX}.tmp"
    mv "${INDEX}.tmp" "${INDEX}"
  else
    printf '\n## %s\n - %s\n' "${SHA}" "${PRED}" >> "${INDEX}"
  fi
  echo "added under ## ${SHA}"
  echo "  - ${PRED}"
fi

RECEIPT="${DIR}/${DATE%%T*}-${TAG}.ots"
ots stamp "${INDEX}"
mv "${INDEX}.ots" "${RECEIPT}"
echo "receipt (pending): claim-prereg-ots/$(basename "${RECEIPT}")"

# Commit the pending receipt first, so the long wait is interruption-safe.
if commit_paths "prereg: stamp ${TAG} (pending OTS)" "${INDEX}" "${RECEIPT}"; then
  echo "committed pending receipt on branch '${BRANCH}'"
else
  echo "pending receipt already up to date on branch '${BRANCH}'"
fi

cat <<EOF

##############################################################################
#  BLOCKING for Bitcoin confirmation — expect ~1 HOUR (sometimes longer).    #
#  Ctrl-C is safe: the pending receipt is already committed. Resume with:    #
#    ots upgrade --no-backup '${RECEIPT}'                                     #
##############################################################################
EOF

deadline=$(( $(date +%s) + POLL_MAX_MIN * 60 ))
anchored=0
while [[ "$(date +%s)" -lt "${deadline}" ]]; do
  ots upgrade --no-backup "${RECEIPT}" >/dev/null 2>&1 || true
  if ots info "${RECEIPT}" 2>/dev/null | grep -q BitcoinBlockHeaderAttestation; then
    anchored=1
    break
  fi
  echo "  $(date -u +%H:%M:%SZ) still pending — next check in $(( POLL_INTERVAL / 60 )) min"
  sleep "${POLL_INTERVAL}"
done

if [[ "${anchored}" -eq 1 ]]; then
  if commit_paths "prereg: anchor ${TAG} (OTS Bitcoin-confirmed)" "${RECEIPT}"; then
    echo
    echo "ANCHORED + committed on '${BRANCH}'. Citable now:  ots verify '${RECEIPT}'"
  else
    echo
    echo "ANCHORED (receipt already current) on '${BRANCH}'. Citable now:  ots verify '${RECEIPT}'"
  fi
  osascript -e "display notification \"prereg ${TAG} anchored to Bitcoin\" with title \"OTS prereg\"" >/dev/null 2>&1 || true
else
  echo
  echo "STILL PENDING after ${POLL_MAX_MIN} min — calendars can lag; the pending receipt IS committed on '${BRANCH}'."
  echo "finish later with:"
  echo "  ots upgrade --no-backup '${RECEIPT}' && git -C '${ROOT}' add '${RECEIPT}' && git -C '${ROOT}' commit -m 'prereg: anchor ${TAG}'"
  osascript -e "display notification \"prereg ${TAG} still pending — upgrade later\" with title \"OTS prereg\"" >/dev/null 2>&1 || true
fi
