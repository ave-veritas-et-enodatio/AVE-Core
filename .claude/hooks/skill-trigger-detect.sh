#!/bin/bash
# Hook: PreToolUse trigger-detect for AVE-discipline skills.
#
# Runs on Write|Edit|Bash tool calls; greps the proposed content/command for
# trigger keywords that match skill descriptions in ~/.claude/skills/.
# If matches found, outputs reminders to stderr (visible to agent) about
# which skills may apply. Does NOT block (always exits 0).
#
# Plumber-physical: this is a passive sensor (current transformer) that
# reads what's flowing through the tool-call wire and lights an indicator
# lamp if it detects current matching specific signatures. The agent sees
# the indicator and chooses whether to invoke the skill via Skill tool.
#
# Closes the gap surfaced in 2026-05-18 session post-mortem: 11 skills
# should have fired but didn't because there's no automatic mechanism;
# all firing is currently agent-discipline-driven without any nudge.
#
# Design note: this is the Phase 2 work flagged in
# ~/.claude/skills/README.md §6 ("auto-detection hook for skill firings —
# Phase 2 work"). Prototype implementation; iterate as triggers prove
# under-/over-sensitive.

set -uo pipefail

# Read JSON payload Claude Code pipes to stdin
PAYLOAD=$(cat)
TOOL_NAME=$(printf '%s' "$PAYLOAD" | jq -r '.tool_name // empty')

# Extract content based on tool type
CONTENT=""
case "$TOOL_NAME" in
    "Write")
        CONTENT=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.content // empty')
        FILE_PATH=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.file_path // empty')
        ;;
    "Edit")
        CONTENT=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.new_string // empty')
        FILE_PATH=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.file_path // empty')
        ;;
    "Bash")
        CONTENT=$(printf '%s' "$PAYLOAD" | jq -r '.tool_input.command // empty')
        FILE_PATH=""
        ;;
    *)
        exit 0  # only fire on Write|Edit|Bash
        ;;
esac

# Skip if AVE-Core path not detected (other repos use different disciplines)
if [[ -n "$FILE_PATH" ]] && [[ "$FILE_PATH" != *"AVE-Core"* ]] && [[ "$FILE_PATH" != *"AVE-staging"* ]]; then
    exit 0
fi

# Combine FILE_PATH + CONTENT for matching
HAYSTACK="$FILE_PATH"$'\n'"$CONTENT"

# Accumulator for triggered-skill list
TRIGGERED=""

# Helper: append skill + reason
trigger() {
    local skill="$1"
    local reason="$2"
    TRIGGERED="${TRIGGERED}  • ${skill} — ${reason}"$'\n'
}

# ============================================================
# Trigger rules (skill → keyword/pattern → reason)
# ============================================================

# consistency-vs-emergence: comparing computed value to CODATA/canonical target
if echo "$HAYSTACK" | grep -qE "ave\.core\.constants|CODATA|alpha.{0,5}=.{0,5}1/137|137\.036|6\.674e-11|8.{0,3}pi.{0,3}alpha|8πα|fine.{0,5}structure|predictions\.yaml"; then
    trigger "consistency-vs-emergence" "constants.py or CODATA-target compare detected"
fi

# ave-canonical-source: new Python script with hardcoded constants
if [[ "$FILE_PATH" == *.py ]] && echo "$HAYSTACK" | grep -qE "1\s*\.\s*0?\s*/\s*137\.|137\.03[0-9]+|6\.674[eE]-?11|9\.10[0-9]+[eE]-?31|1\.602[0-9]+[eE]-?19|6\.626[0-9]+[eE]-?34|1\.054[0-9]+[eE]-?34|ALPHA\s*=|^G_NEWTON|^M_E_KG|^HBAR"; then
    trigger "ave-canonical-source" "hardcoded numerical constant in Python script (should import from ave.core.constants)"
fi

# substrate-native-check: new solver/operator code
if [[ "$FILE_PATH" == *"src/ave/solvers/"* ]] || [[ "$FILE_PATH" == *"src/ave/topological/"* ]] || [[ "$FILE_PATH" == *"src/ave/core/"* ]]; then
    trigger "substrate-native-check" "writing to src/ave/{solvers,topological,core}/ — substrate-physics walk required"
fi
if echo "$HAYSTACK" | grep -qE "eigenvalue|eigsolve|Hessian|gradient.descent|Lagrangian.minimization|basin.of.attraction|energy.landscape"; then
    trigger "substrate-native-check" "SM/QM-default keyword (eigenvalue/Hessian/gradient descent) detected — verify substrate-native framing"
fi

# pre-test-physics-check: new test or prereg
if [[ "$FILE_PATH" == *"src/tests/"* ]] || [[ "$FILE_PATH" == *"prereg"*".md" ]] || [[ "$FILE_PATH" == *"_test_"* ]]; then
    trigger "pre-test-physics-check" "new test/prereg file — physical-picture check required before locking design"
fi

# phase-space-coordinate-check: phase-space / topology keywords
if echo "$HAYSTACK" | grep -qE "phase.space|Lissajous|phasor|V_inc|V_ref|Clifford.torus|\(2,3\).{0,5}torus|\(p,q\).{0,5}knot|impedance.plane"; then
    trigger "phase-space-coordinate-check" "phase-space coordinate keywords detected — verify coordinate-system match before test"
fi

# ave-discrimination-check: load-bearing/strong-positive claims
if echo "$HAYSTACK" | grep -qE "load-bearing|AVE-distinct|STRONG POSITIVE|foreword promotion|canonical anchor|empirical confirmation"; then
    trigger "ave-discrimination-check" "strength-claim keyword detected — SM-counterfactual + interpretive-alternatives check required"
fi

# ave-evidence-framing-discipline: precision/strength language
if echo "$HAYSTACK" | grep -qE "approximately matches|within [0-9]+%|rigorous|exact match|survives|confirms|validates|demonstrates|essentially exact|to within rounding"; then
    trigger "ave-evidence-framing-discipline" "strength language detected — precision check required (verify the quantitative claim)"
fi

# ave-infinity-discipline: continuum-limit / divergence claims
if echo "$HAYSTACK" | grep -qE "continuum limit|ℓ_node.{0,3}→.{0,3}0|UV divergence|UV cutoff|renormalization|RG flow|continuum approximation|Clay.class"; then
    trigger "ave-infinity-discipline" "continuum/infinity keyword detected — lattice+saturation discipline applies"
fi

# ave-independence-check: N-instance claims
if echo "$HAYSTACK" | grep -qE "[0-9]+ independent|[0-9]+ instances|[0-9]+ pillars|[0-9]+ anchors|[0-9]+ confirmations|multi-confirmation"; then
    trigger "ave-independence-check" "N-instance enumeration detected — pairwise algebraic check required"
fi

# verify-before-cite: file:line citation claims
if echo "$HAYSTACK" | grep -qE "per \`[^\`]+:[0-9]+\`|at \[[^]]+:[0-9]+\]|file:line|the corpus says|according to the canonical"; then
    trigger "verify-before-cite" "file:line citation detected — verify content before asserting"
fi

# ave-prereg: new research/*.md or new derivation script
if [[ "$FILE_PATH" == *"research/"* ]] && [[ "$FILE_PATH" == *.md ]] && [[ "$FILE_PATH" != *"_archive"* ]]; then
    trigger "ave-prereg" "new research doc — corpus-grep for prior work + pre-registration discipline"
fi
if [[ "$FILE_PATH" == *"src/scripts/verify/"* ]] && [[ "$FILE_PATH" == *.py ]]; then
    trigger "ave-prereg" "new verify script — corpus-grep prior work + pre-registration before derivation"
fi

# ave-walk-back: editing matrix or KB anchor or chapter
if [[ "$FILE_PATH" == *"divergence-test-substrate-map.md"* ]] || [[ "$FILE_PATH" == *"closure-roadmap.md"* ]]; then
    trigger "ave-walk-back" "editing matrix/closure-roadmap — walk-back propagation graph applies (matrix + KB + chapter + foreword + changelog)"
fi

# ave-audit: about to spawn ave-auditor or ave-corpus-grep
if echo "$HAYSTACK" | grep -qE "ave-auditor|ave-corpus-grep|Agent.{0,30}subagent_type"; then
    trigger "ave-audit" "audit-agent spawn detected — pre-audit grep verification required"
fi

# ============================================================
# Output reminder if any skills triggered
# ============================================================

if [[ -n "$TRIGGERED" ]]; then
    # Output to stderr so it appears in Claude's tool feedback
    cat >&2 <<EOF
[skill-trigger-detect] potential skill matches for this tool call:
${TRIGGERED}
Per ~/.claude/skills/SKILL.md descriptions, consider invoking via:
  Skill(skill: "<skill-name>")
This is a non-blocking nudge. If skill doesn't apply, proceed.
EOF
fi

# Always exit 0 — non-blocking nudge only
exit 0
