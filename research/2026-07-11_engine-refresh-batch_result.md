# Engine-refresh batch — result ledger (2026-07-11)

**Branch:** `analysis/engine-refresh-batch` (detached from `origin/main` `f7e8409a`).
**Discipline:** one PR (DO-NOT-MERGE, orchestrator-review-pending), one commit per
unit; U5 = prereg-freeze commit PUSHED before the test commit; verify-before-cite
at HEAD; adversarial review run by the orchestrator from the core session (NOT
this satellite). No def-nodes minted.

**KEEP-BOTH scope (R4 correction).** KEEP-BOTH is honored **where a superseded
row/label is retained in place** — U1's older index sections (verbatim) and U6's
`:513` op-amp CMRR row (verbatim). **U3's `CLAUDE.md:23` was a WHOLESALE line
replacement**, so the superseded string is preserved **verbatim in the U3 ledger
entry below**, not in place. The blanket "every superseded string" phrasing from
the first pass is corrected to this scoped statement.

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
| **U3** DAG + CLAUDE.md re-scope | ✅ EXECUTED | `loop-gap-engine-dag.md:3` → "loop-gap-platform manifest" (whole-engine = engine-capability-map); `CLAUDE.md:23` → regime-organized platform tree + facade (names from map §2, no invented count). **KEEP-BOTH (R4) — the superseded `CLAUDE.md:23` string, verbatim:** `\| src/ave/ \| Engine code (K4Lattice3D, Cosserat field, solvers, observers, integrators) \|`. Commit `adf5eabc`. |
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
| P11 sabotage (`|g|`-keyed) — frozen | `min S_sab < 0.99` (formula) | `min S_sab=0.9539` | PASS (keying loads) |
| P11 evolved teeth (R6) | L2 div > 1e-2 AND neg-ctrl < 1e-9 | `L2=0.1115` (fires), `null=0.00e+00` | PASS (evolved teeth) |
| Summary CMRR | `CMRR > 1e3` (floor-guarded) | **∞ by construction** — LEG-A residual **exactly 0**; the `2e11` is a `1e-12`-divide-floor artifact, NOT a measurement (R7) | PASS |
| R5 damping control (LEG-A) | verdict `min S > 0.999` | `min S=0.999989` (A_strain residual `4.78e-3` = PML-seeded, see R5 amendment) | PASS (verdict unchanged) |
| R5 damping control (LEG-B) | verdict `min S < 0.999` | `min S=0.9687` | PASS (verdict unchanged) |

**P10 (CERTIFIES-AND-EXPOSES, verbatim in the prereg):** does NOT adjudicate T4
(X36 install-tautology). The MOND local-`|g|` keying FAILS LEG-A BY DESIGN = the
honest exposure (the P11 arm is that exposure in miniature). **flag-don't-fix:**
the engine's raw `|V|`-keying is itself common-mode-sensitive — the EP-correct
variable is the differential `∇V`; a KB/Grant call this test EXPOSES, not resolves.

**Runtime:** 4-leg driver **0.07 s**; full `test_ep_cmrr.py` (**5 tests** after the
R5/R6 repairs) **0.73 s**; regression-clean against the engine_acceptance suite.

## Gates (run before final push)

- `make verify` — PASS (per-commit pre-commit hook; ~15 s each).
- `verify-md-links`, `verify-provenance-stamps` — PASS (folded into `make verify`).
- engine_acceptance suite — **102 passed** (incl. the **5** EP-CMRR tests after the
  R5/R6 repairs — LEG-A, LEG-B, P11-with-teeth, R5 damping control, summary).
- `make vol6` — exit 0, zero undefined `\ref`.

## Flagged for Grant / auditor (surfaced, not resolved)

- U5 flag-don't-fix: bulk-sector kernel keying `|V|` vs differential `∇V` (the EP-correct variable).
- U2 LIVE: `n_eff` symbol overload (√S EM vs 1/√S gravitational) — KB-owner symbol decision.
- U6: skill Step-2 mirror into `~/.claude/skills/ave-ee-first-mapping/SKILL.md` — Grant-gated follow-on.
- The four orchestrator-defaults above — Grant may override at merge review.
- ch14 low-duty-cycle reconciliation physics — OPEN for Grant (not substituted).

---

## Post-freeze amendments (dated 2026-07-11) — the frozen prereg file stays byte-untouched

Per substitution-not-retraction, the frozen prereg
(`research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md`) is **NOT edited**;
post-freeze deviations are disclosed here (the x40 companion-amendment pattern).

- **§R5 — PML damping omission (disclosed post-freeze).** The frozen prereg said
  the driver "reimplements no stencil, stepper or kernel," but `body_force_step`
  re-typed a 3-line leapfrog that OMITTED the certified `step()`'s final
  `V *= self.damping` (PML) line — a genuine post-freeze deviation. The engine's
  `step()`/`run()` API admits no full-field body force (only a single-point
  soft-source), so the preferred route (drive the certified `step()` directly) is
  not cheaply possible without modifying the engine (out of scope this PR).
  **Route taken: (a) this dated disclosure + (b) a damping-inclusive CONTROL leg**
  (`test_ep_cmrr_r5_damping_inclusive_control`) that re-runs LEG-A/LEG-B with the
  certified `V *= self.damping` line reinstated and asserts the **verdicts are
  unchanged** (LEG-A `min S=0.999989 > 0.999`; LEG-B `min S=0.9687 < 0.999`). The
  damped LEG-A A_strain metric gains a small PML-seeded boundary residual
  (`4.78e-3`) — which is precisely WHY the frozen driver omitted damping (the
  smooth drives launch no wave, so the PML only seeds a spurious boundary
  gradient); the verdict-level invariant `min S` is robust. The deviation carries
  its own receipt; verdicts unchanged.
- **§R6 — P11 evolved teeth (post-freeze strengthening).** The frozen P11 bin
  (`min S_sab < 0.99`) is a formula-level keying check with no evolved teeth (the
  100-step evolve was dead code for the assert). **The frozen bin is KEPT (not
  loosened);** an EVOLVED-observable assertion is ADDED: the `|g|`-keying is
  planted into the stepping (`c_eff²=c0²/S(A_sab)=1.0483` vs the strain-keyed
  `c0²=1.0`), a probe pulse propagates, and the detector fires on the L2 field
  divergence (`0.1115 > 1e-2`) with an exactly-zero clean-vs-clean negative
  control (`0.00e+00 < 1e-9`). Genuine evolved teeth + determinism.
- **§R7 — CMRR display honesty.** The LEG-A residual is **exactly 0**, so
  `CMRR = A_strain_B / max(A_strain_A, 1e-12)` is **∞ by construction**; the
  displayed `2e11` is a `1e-12`-divide-floor artifact, not a measurement. The test
  print, this result doc, and the PR body all state the honest ∞-by-construction
  form. The frozen prereg's floored formula bin is retained as a computational
  guard (not loosened).

## Adversarial-review repair log (PR #650, 2026-07-11 — 7 CONFIRMED, 0 refuted)

| # | Finding | Repair | Commit |
|---|---|---|---|
| R1 | U6 row: "CMRR infinite BY IDENTITY" unscoped | scoped to WEP/composition level; SEP-CMRR gloss (finite/measurable; Nordtvedt; both T4 branches require finite; clears-bounds = A7) | (repair batch) |
| R2 | n_eff overload anchors drifted (`:12`/`:58`) | re-anchored to `vacuum-birefringence-e4.md:108-110` + `substrate-perspective-electron.md:60` at both KB sites; flagged the stale SOURCE comments at `master_equation_fdtd.py:178-179` (engine untouched) | (repair batch) |
| R3 | ch14 header's own `:46,49,53` self-invalidated by the 24-line insertion | cite by section name §"The SPICE Equivalent" + corrected `:70,73,77` (drift-robust) | (repair batch) |
| R4 | blanket "KEEP-BOTH every superseded string" vs U3's wholesale CLAUDE.md replacement | superseded `CLAUDE.md:23` line quoted verbatim in the U3 ledger entry; blanket claim scoped | (repair batch) |
| R5 | `_ep.py` stepper omitted the certified PML damping vs frozen spec | dated amendment §R5 + damping-inclusive control leg (verdicts unchanged) — route (a)+(b) | (repair batch) |
| R6 | P11 assert = evolution-free arithmetic (no teeth) | evolved L2-divergence detector + negative control (frozen bin kept); amendment §R6 | (repair batch) |
| R7 | "CMRR≈2e11" = 1e-12-floor artifact | honest ∞-by-construction display everywhere; amendment §R7 | (repair batch) |
