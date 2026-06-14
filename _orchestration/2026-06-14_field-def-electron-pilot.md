# FIELD-DEF LANE — ELECTRON PILOT (instance-1) — DISPATCH BRIEF (2026-06-14, re-dispatch)

You are the implementer for the Field-def lane. This brief is self-contained and has been adjudicated through an auditor (Grant) over multiple rounds — the corrections below are NON-NEGOTIABLE and override any contrary instinct or any contrary text you find in old corpus adjudication docs (e.g. AUDITOR_STATE.md, which contains the SUPERSEDED pre-correction framing). **Nothing you produce merges, pushes, or promotes to SOLID. You stage everything `proposed`, run the gates, and STOP. Output returns through the auditor.**

RE-DISPATCH NOTE: a prior run correctly stopped on a base-SHA drift gate. The base has been re-adjudicated by the orchestrator and moved forward to current `origin/main` (clean fast-forward; see §0 + §4.1). No work was done in the prior run; start clean.

FIRST ACTION: write this entire brief verbatim to `_orchestration/2026-06-14_field-def-electron-pilot.md` on your branch as commit 1 ("I understand the task" checkpoint).

## 0. Worktree & branch (do this before anything else)
- `git -C /Users/grantlindblom/AVE-staging/AVE-Core fetch origin`
- Verify `git -C /Users/grantlindblom/AVE-staging/AVE-Core rev-parse origin/main` == `3093e747` (the re-adjudicated verified base; full hash `3093e747d89df3047ad63b4fac111963d6c26105`). If origin has advanced PAST `3093e747`, STOP and report the drift before proceeding (same gate as before — do not silently re-base again).
- Create a worktree off `origin/main`: `git -C /Users/grantlindblom/AVE-staging/AVE-Core worktree add -b analysis/2026-06-14-field-def-electron-pilot /Users/grantlindblom/AVE-staging/AVE-Core-fielddef-wt origin/main`
- Do ALL work in `/Users/grantlindblom/AVE-staging/AVE-Core-fielddef-wt`. Never touch the main checkout. `main` is protected.
- Incremental commits only: skeleton-first, one section per commit. Do NOT do single huge Write calls (they socket-timeout). Commit after each coherent step.

## 1. Mission
Define the electron's field components (real R + reactive jX) as **instance-1** of a `SubstrateExcitation` class-tree, and factor the **electron-specific instance VALUES** out of the genuinely class-invariant FORMS so the engine stops carrying the electron operating point as a hidden universal default. This is an electron-instance **CONSISTENCY** pilot (the corpus already grades the reflection relation "CONSISTENCY, not emergence" at cvr-reflection-smith.md:5) — not an emergence/class-law claim.

## 2. CORRECTED factor-out target (read carefully — this changed)
α is the UNIVERSAL electromagnetic coupling constant (it couples to any charge; an unexplained SM free parameter). It is NOT electron-specific and must NOT be factored out.
- **KILL `|Γ|²=1−1/Q`.** Do NOT generalize `gamma_mag_sq_leak` to `1−1/Q`. That move wrongly demotes the universal α to a per-instance variable. The reflection form stays **`|Γ|²=1−α`**, with α the universal coupling (NOT renamed `1/Q`).
- **Factor OUT the electron-specific INSTANCE fields:** geometry / (p,q) / mass / L / C / ω₀ / **the electron's Q VALUE** (Q_e = 1/α = 137.036, derived from the electron's torus geometry 4π³+π²+π).
- **Factor these out FROM the genuinely class-invariant FORMS (keep as forms):** the pole shape `s± = −ω₀/(2Q) ± jω_d`, the root-locus, `S(A) = √(1−(A/A_c)²)`, and the `Γ_spinor = −1` wall.
- Net: the class-invariant machinery must accept arbitrary instance fields (a different Q, ω₀, L/C) and produce correspondingly different outputs; the ELECTRON instance reproduces today's numbers exactly by plugging in the electron's values. α stays in the form, universal, NOT varied.

## 3. The Γ-homonym (LOAD-BEARING — disambiguate + label, do NOT resolve)
Run `ave-representation-capability-check` on the symbol "Γ" before authoring any reflection value. There are TWO distinct Γ's and they must never be conflated:
- **`Γ_spinor = −1`** — the topological 2π→4π spinor-sign reflection. ALL fermions have it (electron AND proton). This is the class-invariant "Γ=−1 wall" / perfect-short stability boundary (resonant-lc-solitons.md:64). It is NOT the EM leak.
- **`|Γ_EM|² = 1−α`** — the EM-radiative reflection (the wall falls short of the unit circle by exactly α, the per-cycle radiative leak). Electron-scoped corollary (cvr-reflection-smith.md:36, boxed).
- The electron has BOTH. Label them DISTINCTLY in the def-node and leaf. Do NOT write "electron = |Γ|²=1" and do NOT write "electron = |Γ|²=1−α" without saying WHICH Γ. Do NOT promote `|Γ_EM|²=1−α` to a universal class law — that is gated on a pending human physics ruling; keep it DEFAULT electron-scoped. Surface the homonym as an open item for the auditor; do NOT resolve it yourself.

## 4. Verified starting state (grep-confirmed at 26f27966; surfaces byte-clean through 3093e747 — re-verify any content you cite per verify-before-cite)
Engine (`src/scripts/vol_9_device/cvr_ee_sweep/`):
- `cvr_model.py:58` `Q_TANK = 1.0/ALPHA` — the electron's instance Q value (legitimately electron-specific now; label it so, don't let functions DEFAULT to it as if universal).
- `cvr_model.py:147-155` `gamma_mag_sq_leak(alpha=ALPHA) -> 1.0-alpha` — **KEEP AS-IS** (α universal → returns 1−α). Do NOT add a Q parameter. Do NOT generalize to 1−1/Q.
- `cvr_model.py:158` `A_at_electron_wall(alpha=ALPHA)` — electron-instance; parametrize or clearly scope as instance-specific (parallel site, was previously omitted).
- `cvr_model.py:183` `poles(Q=Q_TANK)`, `:195` `H_scalar(Q=Q_TANK)`, `:209` `H_chiral(Q=Q_TANK)` — these are the factor-out targets: Q must become an explicit instance field, not a hidden electron default. `:209 H_chiral` was previously omitted — include it.
- `cvr_model.py` `verify_constants()` (≈:249/:254/:257/:262/:264) — electron self-check; KEEP electron-pinned (its job is to verify the electron constants).
- `cvr_ee_sweep.py` — the six-view pipeline (DC-op → H(s) → Smith → phasor/reactance → stability → basin); consumes `M.Q_TANK` etc. Parametrize where it presents the class form vs the electron instance; the electron run must stay byte-identical.
- Constants: import ALPHA etc. from `ave.core.constants` (PEP-420 namespace). Do NOT hardcode numeric values. (ave-canonical-source.)

KB (`manuscript/ave-kb/`):
- Extend the MAIN copy of `vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md` (kind: leaf; claims [clm-kezk9z, clm-p5cf3t]). A divergent l3 copy exists (do NOT reconcile). **Add a real "do-not-merge / divergent-copy" adjudication note** referencing that the l3 copy stripped its kb-frontmatter — the marker the prior adjudication assumed does NOT actually exist.
- CITE, do NOT re-derive (already class-invariant): `S(A)=√(1−(A/A_c)²)` at `saturation-operator.md:22` (NOTE the symbol is `A_c`, not `A_yield`); the Q-general pole `s±=−ω₀/(2Q)±jω_d` at `cvr-transfer-function.md:30/:37-38`; the eigenmode Q-sweep 2→1/α at `cvr-stability-eigenmode.md:24/:48`; `L=ξ_topo⁻²·m` at `topological-kinematics.md:76`; `Z=√(μ/ε)` universal magnitude (clm-gdd70j).
- Byte-identical gate values from `cvr_ee_sweep/_output/cvr_ee_sweep_metrics.json` — assert EACH field against its OWN exact string: `gamma_mag_sq_leak = 0.9927026474307` (=1−α); `pole_real_over_w0 = -0.0036486762846499998` (field); `minus_alpha_over_2 = -0.00364867628465` (separate field). These last two are float-equal but NOT byte-identical — do not cross-assign the strings.

## 4.1 BASE-DRIFT CAVEAT (new — read before citing)
The base moved `26f27966 → 3093e747` (+5 commits, clean fast-forward; orchestrator-verified). Exactly 7 files changed in that range: `_orchestration/2026-06-14_discipline-infra-hardening-lane.md`, `_orchestration/parallel-site-gate.md`, `_orchestration/parallel-site-gate.template.js`, `manuscript/ave-kb/claim-quality-closure-roadmap.md`, `manuscript/ave-kb/common/claim-quality.md`, `manuscript/ave-kb/common/trampoline-analogy-primer.md`, `research/2026-06-14_magic-angle-provenance-bh-forward-test-audit.md`.
- **None of your pilot surfaces are in that list** (verified: cvr_model.py, cvr_ee_sweep.py, metrics.json, resonant-lc-solitons.md, vocabulary-register.md, the 5 cited ch1/ch6 KB files, electron-identification.md, topological-kinematics.md, constants.py — all byte-clean). The §4 line numbers and gate values hold.
- **EXCEPTION — re-verify any citation that lands in:** `common/claim-quality.md`, `claim-quality-closure-roadmap.md`, or `common/trampoline-analogy-primer.md` (these 3 changed). If your carried-flags M/Q/J dimensional reading or any provenance cites `common/claim-quality.md` line numbers, re-grep at `3093e747`. The vol4/vol1 `claim-quality.md` files (hosting clm-rtdmsn, clm-lv3uw1, clm-kezk9z, clm-gdd70j) are byte-clean.
- **BONUS — use the new infra:** the parallel-site re-verify gate landed on your base — `_orchestration/parallel-site-gate.md` (discipline) + `_orchestration/parallel-site-gate.template.js` (reusable template). USE the template to implement gate leg 3 (residual-default grep) instead of an ad-hoc grep.

## 5. The mint — PATH B (INVARIANT-S12, ZERO schema change)
- Mint `SubstrateExcitation` + `BoundResonator` as `def-` vocabulary nodes at status **`proposed`** in `common/vocabulary-register.md` (`<!-- id: def-xxxxxx -->` entries; 6-char `[a-z0-9]{6}` ids; verify 0 prior corpus hits first — they are clean as exact tokens). Then run `refresh-kb-metadata` to materialize into `.index/claims.jsonl`. This is NOT a new SCHEMA.md node_type/prefix (`def` is already a frozen, Stage-2-materialized node_type — zero schema change). Existing examples to match format: `def-24e6e6` (κ_share), `def-088f0d` (r_env).
- Each def-node MUST carry an explicit map to the canon nouns: unknot dilatation-mass / Mass-Dilatation Resonator / Resonant LC Tank / 0₁ unknot + (2,3) winding. The labels `SubstrateExcitation`/`BoundResonator` are zero-hit non-canon — do NOT let them drift into a noun-swap. "vortex ring" / "lossless pivot" stay research-only (not canon).
- Electron R/X/Q/L/C bundle = new `clm-` claim(s) + the leaf extension.

## 6. HARD ontology fence (master-equation.md:20, Grant-ratified Rule-12 block)
The H(s)/phasor view is the **MASS-"3" (A1 dilatation) ONLY**. The charge-"3" ((2,3) Cosserat micro-rotation winding) is orthogonal (A1 ⊥ T2) and **MUST NEVER be wired into the breather's (V_inc, V_ref) phasor** — V_ref is a read-only projection of the same scalar V, not an independent DOF; wiring it self-inflicts the genesis-24 double-count. Re-stated as a no-claim rule at `cvr-transfer-function.md:5/:10`. Preserve this fence in everything you author.

## 7. Schema corrections (baked in — apply all)
Recommended class schema: `particle · (p,q) · m→L=ξ_topo⁻²·m · Q[instance VALUE; electron=1/α] · {Q_vol,Q_surf,Q_line}[derived] · A_yield[saturation-kernel yield] · A₀ · R/X[derived] · S(A)[class method] · Γ_spinor=−1[class wall] · |Γ_EM|²=1−α[electron-scoped corollary] · provenance · carried-flags`. With:
- **DROP `A_yield²=2α`.** `√(2α)≈0.1208` is the Regime I/II small-signal boundary `r₁` (`four-regimes.md:35-38`, `lattice-impedance-decomposition.md:130`), a DIFFERENT quantity from the saturation-kernel yield normalization `A_yield` in `S(A)=√(1−(A/A_c)²)`. Source the electron's actual yield amplitude correctly (INVARIANT-C1: `V_yield=√α·V_snap≈43.65 kV`; in V_YIELD units the yield is A=1.0). Use `ave-dimensional-provenance-check` + `ave-canonical-source`. Do NOT default A_yield to √(2α).
- **`(p,q)` provenance → `electron-identification.md:27`** (the canonical (p,q) home). Do NOT cite `def-3638f2` — that is the ambiguous "winding" homonym (status: ambiguous, open-ambiguity-flag YES), not a (p,q) definition.
- **`ξ_topo` gloss = the electromechanical transduction constant `e/ℓ_node` (C/m)** per INVARIANT-C2 / clm-i9l284. NOT "topological coherence length." (The `L=ξ_topo⁻²·m` relation itself is correct.)
- **Sector field = mark PROVISIONAL** with the open FLAG-2 cited inline. It rests on `clm-lv3uw1` which is build_band `input-only` (solidity 0.50) AND is the claim behind the still-OPEN FLAG-2 sector-attribution (capacitive C_eff→∞ vs magnetic μ_eff→0 co-attribution). Do not present it as settled.
- provenance(`clm-rtdmsn` [Q-factor; verify its current line — was ~vol4/claim-quality.md:1192] / `clm-lv3uw1` [provisional] / `clm-kezk9z`).
- carried-flags: S^0.25 exponent defect (`cvr-reflection-smith.md:66`) / S_min clip (`cvr-dc-operating-point.md:51`) / sector-attribution FLAG-2 (`cvr-dc-operating-point.md:55`).

## 8. Validation gate (CORRECTED — THREE legs, all required)
1. **BYTE-IDENTICAL:** re-run the six-view pipeline for the ELECTRON instance after the factor-out; reproduce the three values in §4 byte-identical (per-field exact strings). Diff metrics JSON + (if feasible) figures. Treat PNG byte-identity as a soft check (fragile to matplotlib/font/metadata); the metrics JSON is the hard check.
2. **DEAD-INPUT TEST** (proves the factor-out is real, not a no-op rename): for the now-parametric Q machinery (`poles`, `H_scalar`, `H_chiral`), call with `Q ∈ {50, 100, 200}` and confirm the pole real part `−ω₀/(2Q)` MOVES accordingly (NOT stuck at the electron `−αω₀/2`); then call with the electron `Q=1/α` and confirm it reproduces `pole_real_over_w0` exactly. Hold α FIXED (universal) throughout — confirm `|Γ_EM|²=1−α` does NOT vary with Q (α is universal, not a per-instance knob). Document the table of (Q → pole) outputs.
3. **RESIDUAL-DEFAULT GREP** (catches surviving parallel sites — there is no second canonical copy of cvr_model.py, so a byte-diff cannot catch this): use the `_orchestration/parallel-site-gate.template.js` infra. After the factor-out, grep the engine for any remaining hidden electron-value default in a class-invariant code path (`Q_TANK` defaults, `1/ALPHA`, `1.0/ALPHA` in signatures of the general forms). The genuinely electron-instance sites (`verify_constants`, the electron instance constructor, `gamma_mag_sq_leak`'s α) are allowed to keep α/electron values; the class-invariant FORM functions must not silently default to them.

## 9. Skills (fire deliberately — they don't auto-fire)
`ave-cavity-class-identification` (load-bearing — the BoundResonator-vs-OpenCosseratScrew discriminator: confirm the electron is a BoundResonator, not an open Cosserat screw, before minting); `ave-representation-capability-check` (the Γ-homonym §3 AND the (p,q)/label disambiguation); `substrate-native-check`; `consistency-vs-emergence` (guards against re-introducing the α-as-per-instance substitution; classify the reflection relation honestly); `ave-prereg` (inventory before authoring); `ave-canonical-leaf-pull`; `verify-before-cite` (every line:number you cite); `ave-dimensional-provenance-check` (A_yield, ξ_topo, L/C). Write a 60-second skill-selection plan as part of commit 1.

## 10. Execution & stop conditions
- Stage everything `proposed`. Run `make verify-kb-metadata` (or the repo's equivalent) in-worktree and confirm it passes. Run the engine's `verify_constants` + the three gate legs.
- Do NOT merge. Do NOT push. Do NOT promote anything to SOLID. Do NOT finalize/announce claim-IDs as canonical — they are `proposed` pending the auditor gate.
- If you hit a framing fork the brief doesn't cover (especially anything touching the Γ-homonym resolution, the universal-vs-electron scope of 1−α, or the proton), STOP and surface it — do NOT decide it.

## 11. Completion report (return this structured)
Return: (a) worktree path + branch + base SHA (and any origin drift); (b) the def-ids minted + their canon-noun maps; (c) the clm-id(s) created + the leaf diff summary; (d) gate results — byte-identical (the three values, pass/fail), dead-input (the Q→pole table), residual-grep (clean/hits); (e) verify-kb-metadata result; (f) the Γ-homonym disambiguation outcome (the two labels you used, where); (g) every deviation from this brief and every open item you surfaced for the auditor; (h) the commit list. Be honest about anything that didn't validate.

---

## IMPLEMENTER SKILL-SELECTION PLAN (60-second, commit-1 checkpoint)

Plan written BEFORE touching engine/KB. Applied-set will be retroactively audited before final return; drift flagged.

1. `ave-cavity-class-identification` — FIRST, gate before any mint. Confirm electron = BoundResonator (closed standing-wave LC tank, A1 dilatation breather) and NOT an OpenCosseratScrew (radiative/propagating). Load-bearing because the whole class label `BoundResonator` is asserted by the mint; if the discriminator says otherwise the mint is wrong.
2. `ave-representation-capability-check` — on the symbol "Γ" (§3 two-Γ homonym: Γ_spinor=−1 topological vs |Γ_EM|²=1−α radiative) AND on the labels `SubstrateExcitation`/`BoundResonator` (zero-hit non-canon — must MAP to canon nouns, not noun-swap) AND on (p,q) (avoid def-3638f2 winding homonym).
3. `substrate-native-check` — K4/Cosserat/Op14/phase-space-vs-real-space walk before authoring numerics. The H(s)/phasor view is phase-space (V_inc,V_ref); keep the A46 coordinate discipline + the master-equation.md:20 mass-"3"-only fence (§6).
4. `consistency-vs-emergence` — classify the reflection relation. Corpus grades it CONSISTENCY (cvr-reflection-smith.md:5); guard against re-introducing α-as-per-instance (the killed 1−1/Q move). Tag the clm honestly.
5. `ave-prereg` — inventory existing def-/clm- ids + the cited lines BEFORE authoring (referential integrity; zero-hit verification for new def tokens).
6. `verify-before-cite` — every file:line in §4/§7 re-grepped at 3093e747 before it lands in a node. Special re-grep for the 3 base-drift-changed files (§4.1) if any citation lands there.
7. `ave-dimensional-provenance-check` — A_yield (NOT √(2α)), ξ_topo (= e/ℓ_node C/m, NOT coherence length), L=ξ_topo⁻²·m, R/X derivations. Dimensional sanity on every factored field.
8. `ave-canonical-leaf-pull` — leaf-extension format for resonant-lc-solitons.md; canonical-source for constants (import from ave.core.constants, no hardcoded numerics).

Stop-and-surface triggers (do NOT decide): Γ-homonym resolution, universal-vs-electron scope of 1−α, anything touching the proton, any framing fork not covered by the brief.

---

## ADDENDUM (2026-06-14, Rule-12 dated — body above preserved)

The brief body above was written PRE-reconciliation. §3 ("The Γ-homonym — disambiguate + label, do NOT resolve") and §11(f) framed the Γ-homonym as an OPEN item to surface for the auditor, NOT to resolve. That instruction was correct for the pilot run. It has since been **adjudicated and is no longer open** — recorded here per Rule-12 (preserve the original body; append the resolution, do not rewrite §3).

**RESOLVED RULING (Grant-ratified 2026-06-14):** Γ is **TWO DISTINCT objects**, not one homonym to be collapsed:

- **Γ_impedance = −1** — the impedance-short reflection at Z_core → 0. This is the **A1 dilatation-mass** sector (Pauli/TIR; resonant-lc-solitons.md:45–48).
- **Γ_spinor = −1** — the topological 2π→4π spinor-sign STABILITY wall. This is the **T2 Cosserat micro-rotation** sector (finkelstein-misner-spin-half-derivation.md:58–59).

They are numerically coincident at −1 and share the glyph "Γ" but are **distinct objects: A1 ⊥ T2** (master-equation.md:20). They are NOT the same wall and must not be conflated. (|Γ_EM|² = 1−α — the EM radiative-leak reflection — remains the third, electron-scoped corollary; the "three Γ's" are spinor / impedance / EM.)

**Reconciled in-corpus per PR #230** (merge commit 262bd49c; the three-Γ TWO-DISTINCT block now lives at cvr_model.py THE THREE Γ's comment, ~:269–287, with the spinor cite re-pointed). Commit: "field-def reconcile: three-Γ TWO-DISTINCT (A1⊥T2) + re-point spinor cite — Rule-12 reconciliation" (3f3de407).

GAP unchanged: the spin-statistics derivation tying the topological spinor sign to fermion-exclusion statistics is NOT claimed (per A47; vol1/claim-quality.md:721).
