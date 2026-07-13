# X44 — Komar / redshift-weighted source reconciliation — FROZEN prereg

**Freeze discipline.** This prereg is frozen **by push**: it is pushed as its own
commit BEFORE any engine edit / driver / test code exists (methods P9–P11, PR #622;
nordtvedt-η / EP-CMRR pattern). Bins below are frozen; **frozen bins enforce, flags
don't** (P12).

**Authorization.** Grant **RULED (c)** 2026-07-12 on the #651 three-way
(`research/2026-07-11_nordtvedt-eta_result.md` §5 / docket M_eff-vs-far-field row):
source = **REDSHIFT / KOMAR-weighted `T₀₀^matter`** (no separately-added `u_field`).
X44 is the **NAMED + AUTHORIZED** follow-on engine arc that fires **AFTER #651
merges**. This prereg is that arc.

**Class.** Consistency / **CERTIFICATION-class reconciliation** of a latent `#86`
defect — NOT a new chord. The one-ledger PRINCIPLE is already banked (#651 ADD-side
entailment). X44 asks whether the **ruled** source convention makes the engine's
**own-labeled** ADM mass `M_eff` agree with its far-field Gauss flux.

**No chord mint.** α-CLEAN (gravity sector).

---

## Sector header (mandatory — substrate-native-first)

- **SECTOR** = **A1 dilatation / gravity, sub-yield.** Same sector as `#86` /
  `#651`. Mass = A1 (PR#260/#311, untouched).
- **Does the engine carry the DOF?** YES — `src/ave/gravity/backreaction.py`
  Picard loop + Stage-1 saturating bulk operator. X44 **edits the source
  construction** inside that loop (Rule-14 exception for this named arc: engine
  modification is the deliverable).
- **REGIME** = sub-yield (weak/moderate, `max A < 0.2` at the shipped N=24 family;
  contractive Picard). NOT BH / O(1)-compactness (Stage-4).
- **Instrument carrier.** Diamond-K4 Grad/Div (`_build_native_grad_div`) —
  inherits `#86` non-canonical instrument (D1 production carrier = srs-z=3).
  **Flag, do not migrate in this arc** (migration = separate charter).
- **phase-space vs real-space (A46):** all quantities REAL-SPACE. A46 clean.
- **consistency-vs-emergence (A47):** CERTIFICATION / consistency of ledger
  reconciliation. NOT emergence of η or of G.

---

## Corpus sweep (STEP-0)

Grep + read of `backreaction.py`, `gw_propagation.py`, `#86` result, `#651`
result/prereg/docket:

- **Current installed source (ADD):** `T00_total = T00_matter + u_field` with
  `u_field = ½ g |∇ε₁₁|²` (`backreaction.py:303-304`). Far-field Gauss flux
  therefore reads **M+U**.
- **Current installed ADM label (SUBTRACT):** `M_eff = M_matter − U_bind`
  (`effective_mass`, `:185`; module docstring `:17-22`).
- **#651:** first reconciliation of the two → **η_mixed ≈ +2.28 = O(2f)** —
  LATENT `#86` DEFECT EXPOSURE. ADD-side one-ledger η≈0 is ENTAILED; deficit side
  has no independent field-side route under ADD.
- **Grant 2026-06-29 SUBTRACT ruling** (`…grqed-stage3-backreaction_result.md:343-353`):
  substrate reason = local clock `ω_local = ω√S` down-regulates; matter in the well
  weighs less; **positive strain energy is NOT a separate ledger to ADD** — already
  accounted in the down-regulated frequency (no double-count).
- **Grant 2026-07-12 RULED (c):** implement that reading as the **Picard source**
  (not only the post-solve `M_eff` definition). Three-way KEEP-BOTH recorded;
  (a) keep-ADD and (b) bare −u_field stay on record, not installed.
- **No prior Komar/√S source mode** in `src/ave/gravity/` (grep-clean for
  `komar|redshift_weight|clock_weight|source_mode`).

**VERDICT: authorized-open.** No HALT. Proceed.

---

## The ruled source (frozen form)

Per the SUBTRACT ruling's frequency down-regulation (`ω_local = ω√S`) and RULED
(c):

```
A      = clip(|ε₁₁|, 0, 1)                 # Stage-1: ε_yield ≡ 1
S(A)   = (1 − A²)^{1/2} clipped to [S_min, 1]   # Op14, exponent=0.5
T00^src = T00^matter · √S(A)               # redshift / Komar weight
# NO + u_field term
```

Picard outer loop then solves the Stage-1 elliptic with `T00^src` (via the existing
`T00_override` hook). `u_field` / `U_bind` remain **diagnostics** (binding-energy
density still computed for the ledger and for the fireable identity below) but are
**not** added into the source.

**Why √S (not S, not 1/S):** the ruling names `ω_local = ω√S` and `E=ℏω` → mass
scales as √S. Installing `S` or `1/S` would be a different postulate — flagged if
√S fails the fireable identity (do not silently swap).

**Legacy ADD mode:** retained behind an explicit `source_mode="add_field"` kwarg
(default becomes `"komar"`) so `#86` historical ADD behavior remains callable for
A/B comparison and KEEP-BOTH. Shipped gates run on **komar** (the ruled mode).

---

## Analytic expectations (mandatory numbers — ave-prereg v1.6)

Walked picture before any code:

1. **Far-field Gauss flux** `m_g = Σ_interior(L @ ε)` equals `∫ T00^src =
   ∫ T00^matter √S` by the discrete divergence theorem (native K4) — **ENTAILED**
   once the source is installed (X36 install-tautology). Relative residual
   expected ≲ 10⁻⁴ (same order as `#651` ADD residual).

2. **Reconciliation target:** `m_g ≈ M_eff = M_matter − U_bind` across the `#651`
   fixed-rest-energy family (σ ∈ {1.4, 1.8, 2.2, 2.6}, N=24, M=4.0, g_self=1.0).
   Define the mixed-register slope again:
   `(m_g / M_eff − 1) = η_mixed · f`, `f = U_bind/(M+U_bind)`.
   **Expected under successful reconciliation: |η_mixed| < 1×10⁻³** (same
   certification tolerance as `#651` LEG-1; banking basis may still be entailment
   if numeric floor is resolution-limited — disclose via η_mixed-vs-N receipt).

3. **GENUINELY FIREABLE identity (the derivation risk):** the clock-weighting
   deficit
   `Δ_clock = ∫ T00^matter (1 − √S)`
   versus the strain binding
   `U_bind = ∫ ½ g |∇ε₁₁|²`.
   These are **different functionals**. Leading-order weak-field expansions do
   **NOT** identity-match (`Δ_clock ∼ ∫ T00 ε²/4` vs `U_bind ∼ ∫ ½|∇ε|²`).
   **Pre-declared:**
   - if `|Δ_clock − U_bind| / U_bind < 0.30` across the family → **MATCH**
     (O(1) agreement; reconciliation physically coherent);
   - if relative mismatch ≥ 0.30 but |η_mixed| still < 10⁻³ → **PARTIAL**
     (far-field/ADM agree by some other route; clock↔bind identity fails —
     surface, do not retune √S);
   - if |η_mixed| ≥ 10⁻³ → **FAIL** the reconciliation bin (ruled source does
     not close the `#86` defect as hoped).

4. **Picard contractivity:** under komar weighting the source feedback is
   **weaker** than ADD (√S ≤ 1, no positive u_field boost) → expect
   contraction_factor < 1 and all family members converged, max A ≤ 0.2 at N=24.

5. **`#86` at-risk checks** (1/r monopole, S_min-independent M_eff, light
   deflection shape, two-mass nonlinearity, g_self=0 recovery, boundedness):
   expected **PASS** under komar at the same weak-field operating points, with
   possible O(f) shifts in absolute M_eff / K (disclose; ratio/shape gates are the
   load-bearing ones).

6. **ADD-side LEG-1 η** (field flux vs M+U ledger): under komar, M+U is **no
   longer** the installed source integral — the ADD-side certification of `#651`
   becomes a **diagnostic of the retired convention**, not a live gate. Live
   certification moves to **flux vs M_eff**.

---

## Frozen bins

| bin | criterion | meaning |
|---|---|---|
| **(i) RECONCILED** | all family converged, max A < 0.2 (N=24); Gauss residual < 1×10⁻⁴; **\|η_mixed\| < 1×10⁻³**; Δ_clock↔U_bind MATCH (&lt;30%) | ruled source closes the `#86` defect; clock deficit ≈ bind |
| **(ii) RECONCILED-PARTIAL** | \|η_mixed\| < 1×10⁻³ but Δ_clock↔U_bind mismatch ≥ 30% | far-field/ADM agree; fireable identity fails — surface, no √S retune |
| **(iii) UNRECONCILED** | \|η_mixed\| ≥ 1×10⁻³ (or Picard fails / max A ≥ 0.2) | ruled source does **not** close the defect; KEEP-BOTH with ADD; escalate to Grant |
| **(iv) INSTABILITY** | contraction_factor ≥ 1 or systematic non-convergence | komar Picard not contractive in the weak band — HALT engine default flip |

**Entailed-branch check (ave-prereg v1.7):** bin (i)'s Gauss-residual clause is
partly ENTAILED by installing `T00^src` (flux≡source). The **fireable** content is
η_mixed (flux vs `M_eff`) and Δ_clock↔U_bind. Prereg states this explicitly —
Gauss PASS alone is NOT adjudication of reconciliation.

---

## Gates (must all run)

1. Existing `#86` suite: `src/tests/test_grqed_stage3_backreaction.py` (and any
   engine_acceptance consumers of `solve_backreaction`) GREEN under default
   `source_mode="komar"`.
2. Nordtvedt family helper/tests updated to read **flux vs M_eff** as the live
   mixed-register leg; ADD-side LEG-1 retained as diagnostic / KEEP-BOTH.
3. **η_mixed-vs-N convergence receipt** at N ∈ {24, 32, 40} (the `#651` R1
   lesson) — disclose resolution floor; do not bank a numeric LLR claim on N=24
   noise.
4. `make verify` PASS. `mass = A1` untouched.

---

## Out of scope (flag, do not do)

- srs-z=3 migration of the gravity Grad/Div (D1 charter).
- U6 register-row wording edit (auditor-gated KEEP-BOTH from `#651`).
- A7 branch-signature freeze (postdates η / this reconciliation).
- Stage-4 strong-field / BH saturation of √S vs GR √(1−r_s/r).
- Silent swap of √S → S or 1/S if bin (iii) fires.

---

## Deliverables

- This FROZEN prereg (this commit, pushed first).
- Engine edit: `backreaction.solve_backreaction` Komar source + `source_mode` kwarg.
- Tests: `#86` re-green + updated nordtvedt η_mixed gate + η_mixed-vs-N receipt.
- Result doc: `research/2026-07-12_x44-komar-source_result.md`.
- Docket continuation: X44 status board row (KEEP-BOTH).
- PR: `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` — no self-merge.
