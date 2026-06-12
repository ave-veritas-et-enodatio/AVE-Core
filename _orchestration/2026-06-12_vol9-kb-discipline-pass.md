# Vol 9 KB — discipline pass (2026-06-12)

**Branch:** `analysis/2026-06-12-genesis-v10-cvr-implementor` (uncommitted at pass time)  
**Scope:** KB-first Vol 9 device leaves + bulk-impedance gap closure + §5b hysteresis update

## Skill-selection plan (60 s)

| Skill | Target |
|---|---|
| `verify-before-cite` v1.4 | Numeric + channel rows in 3 new leaves + §5b |
| `consistency-vs-emergence` v1.3 Step 8 | Class B/C tags per `device-circuit-models` §1–§4 |
| `ave-discrimination-check` | $Q=1/\alpha$ row; PONDER-05 framing |
| `ave-canonical-source` | `constants.py` + OP scout JSON |
| `ave-dimensional-provenance-check` | $Z_{bulk}$, $Z_{shear}$ assignments |
| `ave-ee-first-mapping` | EE-primary vocabulary in device leaf |
| `make refresh-kb-metadata` + `verify-kb-metadata` | Spine after edits |

**Not fired (N/A this pass):** `ave-prereg` (no new physics primitive); `ave-walk-back` (single-table Rule-12 fix only); `ave-ip-divide` (public synthesis only).

## Outcomes

| Item | Result |
|---|---|
| `bulk-impedance-at-saturation-boundary.md` | Fixed electron EM row (bulk TIR, not $\Gamma_{EM}=-1$); discipline audit block; §5b xref corrected |
| `device-circuit-models.md` | Class B/C per §; discrimination table for $Q$; PONDER-05 INVARIANT-S2 note; verify audit log |
| `three-channel-impedances.md` | Line-level verify log; `constants.py` line refs |
| `substrate-hysteresis-index.md` §5b | v10 honest-closure one-liner (LOOP GAP still open) |
| `make verify-kb-metadata` | PASS (post-edit) |

## Claim posture

- New Vol 9 leaves remain **`no-claim`** Class B/C synthesis (per `vol9/claim-quality.md`).
- `vol9/claim-quality.md` register still has **zero Vol-9-originated `clm-` entries** — intentional until a promotion adjudication lands.
- `bulk-impedance` closes vocab gap; does not mint a new `clm-`.

## Open follow-ups

1. Tier-1 datasheet figures (`gen_saturation_curves.py`) — tracked on `analysis/2026-06-09-vol9-datasheet-figures`.
2. Reconcile `_orchestration/index.md` R8/v10 state (stale 2026-06-11 block).
3. Optional: add `claims: [clm-8nkvwy, clm-3zz0f6]` to three-channel leaves for stronger S8 back-links (currently prose-cited only).
