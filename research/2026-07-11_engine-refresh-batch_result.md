# Engine-refresh batch — result ledger (2026-07-11)

**Branch:** `analysis/engine-refresh-batch` (detached from `origin/main` `f7e8409a`).
**Discipline:** one PR (DO-NOT-MERGE, orchestrator-review-pending), one commit per
unit; U5 = prereg-freeze commit PUSHED before the test commit; KEEP-BOTH on every
superseded string; verify-before-cite at HEAD; adversarial review run by the
orchestrator from the core session (NOT this satellite). No def-nodes minted.

## Four orchestrator-default launch inputs (FLAGGED — Grant may override at merge review)

1. **ch14 walk-back header — NOW** (U7). Honesty header landed on `clm-c54kdd`
   (`…/ch14-leaky-cavity-particle-decay/theory.md`) citing the X43 `Q_μ≈3.5×10¹⁷`
   / **~17.5 OOM** arithmetic (`research/2026-07-11_x43-ringdown-port_result.md:80`);
   the two `Γ=−1` shatter siblings NOTED (`clm-rd9cjm`, `clm-5s5b0d:127`). The
   **low-duty-cycle reconciliation is explicitly NOT substituted** — stays OPEN
   for Grant (Rule 12). **orchestrator-default; Grant may override.**
2. **Firewall-amendment ratification blank — DO NOT BACKFILL** (U7). A dated
   ratification-status note landed BENEATH the block (`_orchestration/index.md`,
   the Grant-ratification code block); the `Date: ___` **stays blank**; downstream
   as-if-YES recorded, verbal sign-off still OWED. **orchestrator-default.**
3. **Band-survey (PR #609) — boards-as-record** (U1). One line in the U1 index
   block ratifies the boards as the record for the #608–#648 arc, band-survey
   included; no new epic doc. **orchestrator-default.**
4. **`axiom-register.md:229` — cosmetic re-scope** (U7). Annotated to
   migration-legs-only, KEEP-BOTH quoting the current wording; the z=3 identity
   itself recorded as SETTLED (D1, Grant 2026-07-03), only the register migration
   legs remain OPEN. **orchestrator-default.**

## Per-unit executed / flagged ledger

| Unit | Status | Receipt |
|---|---|---|
| **U1** index refresh | ✅ EXECUTED | new 2026-07-10/11 top board block above the 2026-07-09 section (KEEP-BOTH); #608–#648 ledger git/gh-confirmed (all 41 MERGED); staleness notice re-stamped; band-survey boards-as-record line. Commit `3413823c`. |
| **U2** S-exponent honesty-lag | ✅ EXECUTED | code confirmed fixed (`master_equation_fdtd.py:184-188` returns `S**0.5`, note `:172-183`; `crystal_engine.py:431-432`); flipped `ch17…/index.md` req (13) + `engine-capability-map.md` §6 to RESOLVED (F1 ruling `design-note:316-319`); split the LIVE `n_eff` overload onto its own line at both sites. Commit `1e5b83fe`. |
| **U3** DAG + CLAUDE.md re-scope | ✅ EXECUTED | `loop-gap-engine-dag.md:3` → "loop-gap-platform manifest" (whole-engine = engine-capability-map); `CLAUDE.md:23` → regime-organized platform tree + facade (names from map §2, no invented count). Commit `adf5eabc`. |
| **U4** engine-capability-map refresh | ✅ EXECUTED | additive §8b.7 (junction_scattering=X38, junction_parasitics=X37, tethered_pivot_x34b, srs_dec x40 girth witness, x42 driver at `src/scripts/vol_2_subatomic/x42_atomic_eigencavity.py` — NOT a src/ave/ cite); INSTRUMENT class, existing cells unchanged (KEEP-BOTH). Commit `2740a912`. |
| **U5** EP-CMRR acceptance test | ✅ EXECUTED (physics unit) | prereg-freeze `076965ba` (PUSHED before code); test `dc812688`. See below. |
| **U6** CMRR register row | ✅ EXECUTED | one §4 row (EP ↔ coupling-level CMRR) in `translation-circuit.md`; distinguished from the ε-sector gauge rider (readout-level, `claim-quality.md:1856`); regime-tagged + originating-leaf cross-ref; KEEP-BOTH the §9 op-amp CMRR row (`clm-3zz0f6`, now `:513`). Skill Step-2 mirror = Grant-gated follow-on (`~/.claude/skills/` NOT edited). Commit `47f28dbe`. |
| **U7** housekeeping | ✅ EXECUTED (5 sub-items) + 1 DROPPED | see below. |

### U7 sub-item detail

- **constants.py:281** ✅ trailing `# ≈ 2.225e-6` → `# ≈ 2.2234e-6 (CODATA-2018 α pin; see :179 digit-carrier)`.
- **cvr_model full-path** ✅ ch17 req (17): bare `cvr_model.py:72` / `:364` →
  `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py:72` / `:364`.
- **axiom-register:229** ✅ default (4) cosmetic re-scope (migration-legs-only, KEEP-BOTH).
- **ch14 walk-back header** ✅ default (1) on `clm-c54kdd`.
- **firewall blank** ✅ default (2) dated note, blank preserved.
- **vol_6 undefined cross-ref** ⛔ **DROPPED (honest closure — no manufactured fix).**
  BUILD-FIRST run: `make vol6` (exit 0, ~90s) → **ZERO undefined `\ref`** in the
  full build (`build/aux/vol_6_periodic_table.log`); the audit's flagged
  `fig:mass_error_vs_Z` resolves in-volume (present at `A_heavy_element_catalog.tex:26`);
  the standalone build's only unresolved refs are cross-volume (`ch:alpha_golden_torus`
  etc.), resolved by the guarded `xr-hyper` namespace import (`main.tex:10-20`) once
  the dependency volumes are built. No genuinely-undefined ref → nothing to fix.

## U5 — the physics unit (freeze receipts + runtime)

**Freeze-by-push ordering (verified):** prereg commit `076965ba`
(`research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md`) was committed AND
**pushed to origin BEFORE** the test-code commit `dc812688`
(`src/tests/engine_acceptance/_ep.py` + `test_ep_cmrr.py`) existed. The freeze is
claimed by commit ordering + the intervening push.

**Sector header:** A1 dilatation/gravity; DOF carried YES (bulk `V` scalar);
sub-yield `S(A)≈1`; drive uniform (common-mode) vs tidal (differential); kernel
variable = the **DIFFERENTIAL** strain `∇V`, NOT `|V|` and NOT `|g|`.

**Driver discipline:** the body-force driver REUSES the certified primitives
verbatim (`eng.c_eff_squared`, `eng._laplacian`, `eng.saturation_kernel`);
`master_equation_fdtd.py` is NOT modified (Rule-14 anti-rebuild).

**Frozen-bin results (all PASS):**

| Leg | Frozen bin | Measured | Verdict |
|---|---|---|---|
| LEG-A (uniform, strain-keyed) | `A_strain < 1e-3`, `min S > 0.999` | `A_strain=0.000e+00`, `min S=1.000000` | PASS (WEP-exact) |
| LEG-B (tide, strain-keyed) | `A_strain` within 5% of 0.2, `min S < 0.999` | `A_strain=0.2020` (rel 0.010), `min S=0.9794` | PASS (kernel loads) |
| P11 sabotage (`|g|`-keyed) | LEG-A fires: `min S_sab < 0.99` | `min S_sab=0.9539` | PASS (WEP-violating detected) |
| Summary | `CMRR > 1e3` | `CMRR≈2.02e11` | PASS |

**P10 (CERTIFIES-AND-EXPOSES, verbatim in the prereg):** does NOT adjudicate T4
(X36 install-tautology). The MOND local-`|g|` keying FAILS LEG-A BY DESIGN = the
honest exposure (the P11 arm is that exposure in miniature). **flag-don't-fix:**
the engine's raw `|V|`-keying is itself common-mode-sensitive — the EP-correct
variable is the differential `∇V`; a KB/Grant call this test EXPOSES, not resolves.

**Runtime:** 4-leg driver **0.07 s**; full `test_ep_cmrr.py` (4 tests) **0.37 s**;
adds ~0.37 s to the engine_acceptance suite (**101 tests pass, regression-clean**).

## Gates (run before final push)

- `make verify` — PASS (per-commit pre-commit hook; ~15 s each).
- `verify-md-links`, `verify-provenance-stamps` — PASS (folded into `make verify`).
- engine_acceptance suite — **101 passed** (incl. the 4 new EP-CMRR tests).
- `make vol6` — exit 0, zero undefined `\ref`.

## Flagged for Grant / auditor (surfaced, not resolved)

- U5 flag-don't-fix: bulk-sector kernel keying `|V|` vs differential `∇V` (the EP-correct variable).
- U2 LIVE: `n_eff` symbol overload (√S EM vs 1/√S gravitational) — KB-owner symbol decision.
- U6: skill Step-2 mirror into `~/.claude/skills/ave-ee-first-mapping/SKILL.md` — Grant-gated follow-on.
- The four orchestrator-defaults above — Grant may override at merge review.
- ch14 low-duty-cycle reconciliation physics — OPEN for Grant (not substituted).
