# P4 — forward-voltage conduction threshold for charge-keyed static loading — PREREG (FROZEN)

**Date:** 2026-07-08 · **Lane:** implementer · **Branch:** `analysis/p4-forward-voltage`
**Contention:** P4 of the paper-hardening epic (`research/2026-07-08_paper-hardening-ledger.md`,
`origin/analysis/paper-hardening-ledger`). Grant ruled **P4 = YES cutoff-limited** and reframed the
lattice cutoff as a **forward-voltage / minimum-bias-to-conduct threshold** `V_f`.
**Gated on (upstream results, imported not re-litigated):**
- round-3 charge-keyed `[DERIVED: CHARGE-KEYED]` — `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md` (merged #547)
- muonic-H `[C-EXCLUDED]` — `research/2026-07-05_problem3-muonic-lamb_RESULT.md` (merged #539)
- semiconductor C-V / varactor mapping — `research/2026-07-07_semiconductor-cv-dip_RESULT.md`

**This prereg is frozen BEFORE any compute** (git commit ordering = freeze proof). The RESULT doc and the
driver `src/scripts/vol_9_device/p4_forward_voltage_threshold.py` are committed AFTER this file.

---

## SECTOR HEADER (mandatory — declare before any substrate word)

- **SECTOR:** **T2 transverse permittivity** (the ε-grade varactor; the **shunt-C per node**,
  `ε_eff = ε₀ S(A_V)`, `A_V = V/V_yield = |E|/E_yield`). **NOT** the A1 longitudinal bond compliance
  (`C₀/S`, keyed `V_snap`); **NOT** the µ-grade circulation inductor; **NOT** the real-carrier
  (pair-production) sector. Anti-cross-wire: the threshold gates the **T2** varactor, keyed on `V_yield`.
- **MODE / REGIME:** cold lattice (`A=0 ⇒ S=1`) driven to a **HELD STATIC bias** (a DC operating point),
  probed weak-small-signal. **Ax3-LOSSLESS** below the pair-production wall `V_snap`. Reactive throughout.
- **PHASE-STATE:** reactive (lossless). The proposed threshold `V_f` (if it exists) is a **dead zone** in
  the reactive varactor: flat at `C₀`/`ε₀` for `|V|<V_f`, loading for `|V|≥V_f`.
- **PHASE-SPACE COORDINATE CHECK (A46):** the corpus claim is `A = |E|/E_yield = V_bond/V_yield` — a
  **field-amplitude ratio**. The copper/muonic tests measure `A²(r) = (E(r)/E_yield)²` in real-space and
  compare it to the kernel's `A²` argument **in the same coordinate** (field-amplitude ratio). No
  phase-space↔real-space mismatch: both sides are `|E|/E_yield`. (This is NOT a `V_inc/V_ref`
  Clifford-torus claim; it is an amplitude-ratio claim, measurable in real space directly.)
- **CONSISTENCY-VS-EMERGENCE:** **CONSISTENCY / FALSIFICATION-class.** `E_c = E_yield = √α·E_crit` is
  CODATA-derived through `α, m_e`; `δ_Cu ≈ 2.4e-5` is an external empirical input (tagged). No emergence
  headline. The verdict is a consistency identity of the network topology + the Ax-4 kernel, and a
  falsification comparison against an external decrement.

---

## THE CIRCUIT TO FORMALIZE (Grant-walked; direction NOT re-litigated)

Lossless L–C link — **series L per bond** (`L_cell = μ₀ℓ_node`), **shunt C per node**
(`C_cell = ε₀ℓ_node`), `Z₀ = √(L/C) = 376.7 Ω`, `ω_C = 1/√(LC) = c/ℓ_node`. The shunt C is the **T2
varactor** (`C_diel ∝ ε_eff = ε₀ S`, rolls DOWN under load). The NEW ingredient is a **forward-voltage
threshold**: a **DEAD ZONE** — the varactor stays at `C₀` (`ε₀`) until `|V_bond| ≥ V_f`, then loads.
Polarity-symmetric (S depends on `E²`) ⇒ the gate is **back-to-back / anti-series diodes (a DIAC)** in
front of the varactor. Piecewise constitutive law to state and test:

```
ε_eff(E) = ε₀                       for |E| < E_f      (transparent, C = C₀)
ε_eff(E) = ε₀ √(1 − (E/E_c)²)       for |E| ≥ E_f      (loads)
```

with `E_f = V_f/ℓ_node`, `A_f = V_f/V_yield = E_f/E_c`.

---

## ★ THE MAKE-OR-BREAK QUESTION (pre-registered): is `V_f` FORCED or FREE?

Candidate canonical scales to test (each: does a canonical scale FALL OUT that (i) is a genuine
dead-zone onset and (ii) survives the copper + muonic constraints?):

| Candidate | `V_f` | `A_f = V_f/V_yield` | Provenance to test |
|---|---|---|---|
| **C1** lattice phonon gap | gap of `ω(q)` | — | K4/srs dispersion `ω=(2c/ℓ)|sin(qℓ/2)|` — gapped? |
| **C2** slew-energy image | `α·V_snap = √α·V_yield` | `√α ≈ 0.0854` | `E_SLEW = α m_e c²` (constants:783) |
| **C3** D-turnover (reference) | `V_yield/2` | `0.5` | `E_C,max = E_c/2` real-branch max |
| **C4** D-turnover (actual field) | `V_yield/√2` | `0.7071` | actual field at turnover `E=E_c/√2` |
| **C5** pair-production gap | `V_snap` | `1/√α ≈ 11.7` | `ℏω_C = m_e c² = e V_snap` (first REAL excitation) |
| **C6** A0 protective cutoff image | `E(9ℓ_node)·ℓ_node` | — | the ~9·ℓ_node ≈ 3.5 pm muonic cutoff, imaged to a bond voltage |

**Pre-registered decision rule (frozen bins):**
- **[FORCED]** — iff a canonical scale from {C1..C5} is (a) a genuine *dead-zone onset* (the kernel is
  flat at `ε₀` below it) AND (b) simultaneously (i) keeps copper consistent, (ii) keeps the µeV muonic
  window, and (iii) keeps the radiative weak-field (`A²≈6e-7`) birefringence sector loading. All three,
  one canonical scale, no tuning.
- **[FREE]** — iff no such canonical scale exists and `V_f` must be tuned to survive. **If FREE, say so
  plainly** — that makes the cutoff an **echo/fit**, exactly the A0 "free parameter" flag
  (`research/2026-07-05_problem3-muonic-lamb_RESULT.md`:158). No post-hoc rescue.

**Structural sub-checks (pre-registered, can-fire):**
- **S1 — round-3 compatibility.** Round-3 derived a **continuous** `ε₀ S(A)` law that loads `∝ ½A²`
  from `A=0` with **NO dead zone**. Test: is the `V_f=0` member of the DIAC-gated family exactly the
  round-3 law? (Expected YES — round-3 = the `V_f=0` special case.) Then any `V_f>0` is a **departure**
  from the round-3 derivation. FLAG if a nonzero `V_f` contradicts round-3's continuous loading.
- **S2 — direction check.** A0's protective cutoff SUPPRESSES loading for `r < r_cut` (**strong** field /
  large bond voltage). A forward-voltage **dead zone** suppresses loading for `|V| < V_f` (**weak** field
  / small bond voltage). Test whether these act on the SAME or OPPOSITE field region. FLAG if opposite
  (then the "9·ℓ_node cutoff ↔ V_f" identity fails directionally).

---

## COMPUTE PLAN (three deliverables — frozen)

1. **Circuit mapping (formal).** Emit `L_cell, C_cell, Z₀, ω_C` from constants (verify_constants), the
   piecewise constitutive law, and a **house-WHITE** equivalent-circuit + constitutive-law figure
   (`ave.viz.style.apply`, `strict=True`, Okabe-Ito, no baked title) in the Vol-9 datasheet register.
2. **Derive `V_f`** per the make-or-break bins above (sympy where symbolic; constants imported).
3. **Constraints WITH the threshold.**
   - **(a) Copper** (Z=29, FCC `a=3.615 Å`, WS-cell volume-average): compute `⟨A²⟩` of the atomic-core
     Coulomb field over the cell with (i) continuum interior-excluded at the turnover, (ii) reduced-Compton
     `ℓ_node` inner cutoff, (iii) with the `V_f` dead zone. AVE decrement `δ_index = ¼⟨A²⟩`, ε-deficit
     `½⟨A²⟩`. Compare to `δ_Cu ≈ 2.4e-5` (external, tagged). **OUR compute; do not adopt any external
     ~1e-7 estimate.** Bare-Z is the direction-conservative UPPER bound (screening only lowers it).
     - **Bins:** `[CONSISTENT]` iff `δ_AVE < 1%·δ_Cu = 2.4e-7` (hides under the measured decrement's
       known accuracy); `[CONSTRAINT]` iff `δ_AVE ≳ 2.4e-7` (would show in the measured decrement).
   - **(b) Muonic recomputation** (Z=1): recompute the loading fraction WITH the dead zone and WITH the
     `ℓ_node` cutoff; does it drop below the µeV window? **Bins:** `[RESCUED]` iff the with-threshold
     shift `< 2.3 µeV`; `[C-STANDS]` otherwise. Cross-check against A0's L-i (`4.92e4 µeV`).
   - **(c) Delbrück / γ fence.** State whether the reactive-line dispersion fences Delbrück / γ-attenuation
     above the `ℏω_C = 511 keV` response scale (band edge `ω_max = 2ω_C`).

## DISCIPLINE (frozen)

- ave-canonical-source: every number imported from `ave.core.constants`; `verify_constants()` COMPUTES the
  cross-checks (`V_yield=√α·V_snap`, `E_yield=V_yield/ℓ_node`, `ℏω_C=e·V_snap`); NO hardcoding.
- pre-register: this file frozen before compute (git ordering).
- ONE blocking driver run; standing test added; `make verify` green.
- Rule 11 honest closure: route against these bins, no post-hoc drops. If `V_f` is FREE, headline it FREE.
- Rule 12: round-3 preserved; this is a NEW derivation (the DIAC-gated generalization) with its own chain,
  not a refill of round-3's slot. Round-3 = the `V_f=0` member.
- flag-don't-fix: if the threshold contradicts round-3 (S1) or reverses the A0 cutoff direction (S2),
  surface with both file paths + verbatim, do not silently resolve.
- pure-AVE-corpus: no external attribution in any tracked file; `δ_Cu` tagged as an external empirical
  input by value only.
- NO self-merge: push branch, open PR `[REVIEW: pending-orchestrator]`.
