# Nordtvedt-η acceptance test — FROZEN prereg (engine-derived η, strain-field register)

**Freeze discipline.** This prereg is frozen **by push**: it is pushed as its own
commit BEFORE the driver/test/helper code exists (the `tethered_pivot_x34b.py` /
EP-CMRR pattern; methods P9–P11 addendum, PR #622). The freeze is claimed by commit
ordering — this prereg commit precedes and is pushed ahead of the test-code commit.
Bins below are frozen; per the P12 addendum (#622) **frozen bins enforce, flags
don't**.

**Class.** Consistency / **certification** (per P10 below, η=0 is ENTAILED by the
solver's single-source construction — this run CERTIFIES-AND-EXPOSES the installed
gravity keying's Nordtvedt-status; it does NOT freely measure a fitted parameter).
**No chord mint.**

**Deliverable.** Convert **A7's Nordtvedt leg** (`_orchestration/2026-07-10_rulings-docket.md`
continuation, "A7 · queued for next sweep") from a **retrieval ASSUMPTION** (the
imported LLR bound) into an **engine-CERTIFIED prediction** (certify-and-expose per
the X36 install-tautology, `research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`).

---

## Sector header (mandatory — substrate-native-first)

- **SECTOR** = **A1 dilatation / gravity, sub-yield.** The equivalence principle is
  ONE identity (energy gravitates exactly as energy resists acceleration — one
  ledger), probed here in **register-2: STRAIN-FIELD-distributed energy** (the
  gravitational binding energy that lives in the substrate strain field *between* /
  *around* knots, in no knot). Register-1 (KNOT-localized energy = WEP, vary
  composition, infinite-CMRR by identity) is the EP-CMRR test's domain (#650,
  `src/tests/engine_acceptance/test_ep_cmrr.py`); THIS test is register-2.
- **Does the engine carry the DOF?** YES — the landed **two-way back-reaction
  solver** (`src/ave/gravity/backreaction.py`, #86, landed 2026-06-29): the field
  sources itself (`T₀₀^total = T₀₀^matter + ½g|∇ε₁₁|²`), M_eff emerges via a Picard
  fixed point with the binding-deficit subtraction. The **strain-field energy** IS
  the `U_bind = ∫½|∇ε₁₁|²` register.
- **REGIME** = sub-yield (weak/moderate field, `max A < 0.2`, `S(A)≈1`, provably
  contractive Picard). NOT the near-yield saturated / BH regime.
- **DOF / register variable = the gravitational SELF-ENERGY FRACTION**
  `f = E_grav/E_total = U_bind/(M_matter+U_bind)`, NOT the total mass and NOT the
  matter amount. That distinction is the whole content of the Nordtvedt probe.
- **GR-frame subtlety AVE escapes:** GR cannot localize gravitational field energy
  (the Landau–Lifshitz pseudo-tensor is coordinate-dependent), so "how much energy
  is in the field" is not well-posed in GR. A **lattice has a real local
  strain-energy density** `½|∇ε₁₁|²` — so the register-2 question **IS well-posed
  here**. This is the reason the test can exist at all.
- **phase-space vs real-space (A46):** every quantity (∫T₀₀, ∮ field flux, the
  monopole coefficient, f) is REAL-SPACE (energy density / field flux / radius);
  measured in real-space. No phase-space φ² claim at issue — A46 clean.
- **consistency-vs-emergence (A47):** the run is **CERTIFICATION** (η=0 entailed by
  the single-T₀₀ construction), NOT an emergence claim. α-CLEAN (gravity sector; the
  solver is G-imported, no `ALPHA`/`Q_TANK`).

---

## Corpus sweep (STEP-0, ave-prereg — did anyone already compute η?)

Grep + read of `src/ave/gravity/backreaction.py`, `src/tests/test_grqed_stage3_backreaction.py`,
`research/2026-06-29_grqed-stage3-backreaction_result.md`, and the docket
(`_orchestration/2026-07-10_rulings-docket.md`):

- The #86 arc computes the **binding-DEFICIT** `M_eff = M_matter − U_bind`
  (`effective_mass()`; U_bind ≈ 2–6% of M_matter across the weak band). It is a
  **single-configuration** ledger; it **never sweeps f**, never compares the
  gravitating register against the inertial register, and **never computes η or
  states η=0.**
- The corpus carries Nordtvedt only as an **imported LLR bound** (`SEP-CMRR ~1e-4`,
  `translation-circuit.md:148`) and an **OPEN docket item** (`A7 · queued for next
  sweep`). The U6 register row currently reads the SEP self-energy term as a
  "nonzero mismatch / both T4 branches REQUIRE a finite value."

**VERDICT: entailed-but-never-stated-or-probed.** No HALT. Proceed with the honest
P10 framing below. (**Flag for the auditor** — surfaced, NOT resolved here: the U6
row's "nonzero mismatch / finite REQUIRED" wording is in tension with the ONE-EP
carve's η=0 one-ledger prediction; per KEEP-BOTH the U6 row stands as-is with a
**post-η refinement as a gated follow-on** — the auditor lands any U6 edit.)

---

## The apparatus (Rule-14 — drive the landed solver as-is; NO engine edit)

The instrument REUSES the landed public entry points **verbatim** (no engine module
is modified; helper + test live in `src/tests/engine_acceptance/`):

- `backreaction.solve_backreaction(N, T00_matter=…, g_self=1.0)` — the self-consistent
  two-way solve (the self-gravitating field).
- `backreaction.gaussian_blob(…)` — the unlabeled energy blob (renormalized to a
  FIXED rest energy — see below).
- `backreaction.field_energy_density(eps, Grad, kappa)` — the strain-field energy
  `½g|∇ε₁₁|²` (register-2), for `U_bind`.
- `gw_propagation._build_native_grad_div(N)` — the native diamond-K4 Grad/Div (the
  same operator the solve uses; NO Cartesian gradient — the K4 checkpoint).
- `graded_vacuum_network.stiffness_profile(A, exponent=0.5, S_min)` — `D=1/S(A)`, to
  reconstruct the divergence-form operator `L = Div·diag(D)·Grad` (the SAME `L` the
  solver assembles, `gw_propagation.py:698-701`) for the **field-side flux** read.

### The configuration family (fixed rest energy, varying binding fraction)

Gaussian blobs renormalized so the **matter/rest energy is IDENTICAL**
(`∫T₀₀^matter = M_TARGET` for every member), swept from **tight → diffuse**
(`SIGMAS`): a tighter blob has steeper `|∇ε₁₁|` ⇒ larger `U_bind` ⇒ larger `f`. So
the family holds the composition/rest energy fixed and varies **only** the
gravitational self-energy fraction `f` — exactly the Nordtvedt setup. `f` is
**DERIVED from the solver's own energy ledger**, not asserted.

### The two registers (measured by DIFFERENT routes — the crux)

- **m_g (gravitating charge, FIELD-side "far-field" read):**
  `m_g = Σ_interior (L @ ε₁₁)` — apply the gravitational divergence-form operator to
  the *solved* strain field and integrate over the source-enclosing interior (the
  discrete Gauss flux). Additionally report the enclosed flux **vs radius** to
  confirm it **plateaus** (a genuine monopole whose far-field charge is
  radius-independent).
- **m_i (inertial mass = total energy, ENERGY-side ledger):**
  `m_i = M_matter + U_bind` = (matter rest energy `Σ T₀₀^matter`) + (strain-field
  energy functional `Σ ½g|∇ε₁₁|²`). A DIFFERENT code path from m_g.

The one-ledger identity is the statement that these two independently-computed
registers agree. **η = slope of `(m_g/m_i − 1)` vs `f`** across the family
(`eta_slope`, ref = smallest-f member).

---

## FROZEN parameters (from the exploratory probe; NOT tuned to a desired output)

| name | value | provenance |
|---|---|---|
| `N` | 24 | probe: converged, clean, ~2.5–3.1 s/solve |
| `M_TARGET` | 4.0 | probe: `max A ≤ 0.2` (weak, provably contractive) |
| `SIGMAS` | (1.4, 1.8, 2.2, 2.6) | probe: source enclosed by R≈9; f ∈ [0.024, 0.060] |
| `G_SELF` | 1.0 | full two-way back-reaction |
| `S_MIN` | 1e-3 | solver default (clip-independent per #86 Check-2) |
| `ETA_TOL` | 1e-3 | probe: measured `|η_cert| ≈ 8×10⁻⁵` (boundary-truncation-limited); 10× margin |
| `EPS_PLANT` | 0.10 | P11 planted two-ledger coupling |
| `PLANT_TOL` | 0.02 | probe: planted-ε recovered to ~6×10⁻⁴; generous |
| `FLUX_PLATEAU_TOL` | 0.05 | monopole radius-independence (outer two enclosing radii) |
| `MIXED_ETA_MIN` | 1.0 | probe: mixed-register pairing gives η ≈ 2.3 |
| `LLR_BOUND` | 4.4×10⁻⁴ | **imported-observational** (LLR Nordtvedt program; comparator for bin ii ONLY) |

---

## LEG definitions + PRE-REGISTERED BINS (frozen)

### LEG-1 — CERTIFICATION (the one-ledger null; **bin i**)

Solve the family; read m_g (field-side flux) and m_i (energy ledger); fit
`η = slope[(m_g/m_i − 1) vs f]`.

- **PASS (bin i — one-ledger CERTIFIED):** `|η| < ETA_TOL` **AND** the enclosed flux
  is a monopole (relative change over the outer two enclosing radii `< FLUX_PLATEAU_TOL`)
  **AND** the flux equals ∫T₀₀^total to the relaxation residual (field-side Gauss on
  native K4) **AND** every member converged. ⇒ the far-field gravitating charge
  tracks the total-energy ledger ⇒ register-2 (strain-field) energy carries the SAME
  one ledger ⇒ **AVE certifies the LLR-Nordtvedt null.**
- **FAIL / bin (ii):** `ETA_TOL ≤ |η|` with a clean linear slope ⇒ a **real
  two-ledger finding** — must then face `|η| ≲ LLR_BOUND` (imported-observational).
- **bin (iii):** no clean linear η ⇒ construction-dependent — surface, don't force.

### P11 — planted two-ledger coupling (detector TEETH)

At the **helper level** (NOT an engine edit), weight the field-energy's contribution
to the **gravitating register only** by `(1+ε)`: `m_g_planted = m_g + ε·U_bind`
(i.e. `M + (1+ε)U`), holding m_i (the energy ledger `M+U`) fixed. This is a genuine
two-ledger coupling (register-2 energy gravitates ε-more than it weighs).

- **PASS (teeth):** `|η_planted − EPS_PLANT| < PLANT_TOL` (the detector FIRES and
  recovers the planted slope) **AND** the **ε=0 negative control** gives
  `|η| < ETA_TOL` (exactly the LEG-1 null; the detector does NOT fire when nothing is
  planted).
- **FAIL:** the planted ε is not recovered (detector blind) OR the negative control
  fires (spurious).

### FLAG — mixed-register exposure (`flag-don't-fix`; documented, NOT a bin gate)

Pairing the **far-field register** (`m_g = M+U`, field energy ADDS to the gravitating
source) against the **binding-deficit register** (`m_i = M_eff = M−U`, Grant-RULED
SUBTRACT 2026-06-29, `…grqed-stage3-backreaction_result.md:343`) yields `η ≈ +2.3`.
This is **NOT a physical two-ledger violation** — it is the solver's internal
**source-side ADD vs ledger-side SUBTRACT** convention gap (the two mass registers
differ at `O(2f)`). The test RECORDS `η_mixed > MIXED_ETA_MIN` (proving the detector
is NOT dead — the LEG-1 null is a real null, not a blind zero) and **SURFACES the gap
for Grant/auditor**. Per flag-don't-fix + Rule-14 it is **not resolved and the engine
is not touched.** The one-ledger η=0 holds for **either** self-consistent register
choice (both m_g,m_i = the total-energy ledger → η=0; both = the binding-deficit
ledger → η=0); η≠0 arises ONLY from MIXING them.

---

## P10 — honesty framing (binding; stated verbatim)

**η = 0 is ENTAILED, not freely measured.** The solver sources the far field from a
**single** energy density `T₀₀^total = T₀₀^matter + ½g|∇ε₁₁|²`. By the discrete
divergence theorem (Gauss) on the native-K4 operator `L`, the far-field monopole
charge = `∫T₀₀^total` = the total energy content. When m_g and m_i are BOTH read off
this single ledger, `η = 0` by construction. So **bin (i) is the expected fire and
the run is CERTIFICATION-class**, per the X36 install-tautology (the engine returns
whatever ledger is installed; the test makes the installed ledger's Nordtvedt-status
VISIBLE — it does not adjudicate whether one-ledger is physically correct).

**Why it is still a genuine (risked-in-principle) certification:** (1) the two
registers are computed by **different routes** (a field-operator flux vs an
energy-functional ledger) — their agreement is a real cross-check, not a re-quote;
(2) the **P11 plant** proves the detector FIRES on a genuine two-ledger coupling
(η=ε), so the null is risked; (3) bins (ii)/(iii) remain fireable — the
**construction-dependence** (bin iii) genuinely manifests as the mixed-register
M_eff-vs-far-field gap (η≈2.3), surfaced as the flag. The **VALUE** is converting
A7's Nordtvedt leg from an imported assumption into an engine-certified prediction.

**A7 consequence (ordering).** If LEG-1 certifies η=0: A7's Nordtvedt leg becomes a
**derived-null consistency channel**, and A7 reduces to the ephemerides /
EFE-quadrupole channel alone. **A7's branch-signature freeze should POSTDATE this
result** (recorded in the result doc + docket).

---

## Runtime / scope

Target **~10–15 s** (4 converged two-way solves at N=24; the P11 plant and the
mixed-register flag REUSE those solves — no extra solve). This is the same
**cost+role tier** as the #86 at-risk checks, so the heavy family test registers in
the **`engine_sim`** partition (`src/tests/conftest.py`, mirroring the
`test_grqed_stage3_backreaction.py` entries); a fast single-solve Gauss-flux identity
check + the pure-arithmetic detector unit-test STAY in the gating lane. No new
substrate-physics claim; `mass = A1` (PR#260/#311) untouched.
