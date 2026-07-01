# RESULT — Electron self-braced UNIFIER: DERIVE + co-compress-MEASURE the field self-energy pull `p`

**Date:** 2026-07-01 · **Lane:** implementer · **Branch:** `analysis/electron-unifier-cocompress`
(worktree `/private/tmp/electron-unifier`, off `main` @ `e1e14572`).
**Prereg (frozen FIRST):** [`2026-07-01_electron-unifier-cocompress_prereg_FROZEN.md`](2026-07-01_electron-unifier-cocompress_prereg_FROZEN.md)
(frozen commit `9f388305`). Adjudication criteria §ADJUDICATION followed exactly; none dropped (Rule 11).
**Type:** DERIVATION (Part 1, sympy) + SIMULATION (Part 2, co-compressing time-domain).
Part-1 driver [`drivers/electron_unifier_derrick.py`](drivers/electron_unifier_derrick.py);
Part-2 driver [`drivers/electron_unifier_cocompress.py`](drivers/electron_unifier_cocompress.py),
raw [`drivers/electron_unifier_cocompress_results.json`](drivers/electron_unifier_cocompress_results.json).
**Class (consistency-vs-emergence):** **C — CONSISTENCY / FORM-chord** throughout (`α`, `A=√α`, `m_e`,
`L_NODE` all imported/echo; only the FORM — the exponents + the stability sign — is derived). NOT emergence.

---

## 0. VERDICT (headline)

> **CONSISTENCY-class** (DOWNGRADED from UNIFIER-CONFIRMED after independent verify — see the
> near-tautology note directly below). **The substrate's fixed-charge Derrick scaling is CONSISTENT with
> a self-braced electron (exponent-level, `p<3` forced in 3D); NO bound state was dynamically observed,
> and the co-compress sim reproduces the seed geometry's Derrick exponents rather than independently
> testing them.** Stated plainly: **the electron is NOT shown to hold together as one object.** What is
> shown: (Part 1) an analytic, substrate-native Derrick balance on the engine energy functional with a
> single crossing and `p<3` forced in 3D — a genuine Class-C FORM result; and (Part 2) a co-compress sim
> whose measured exponents (`E_grad_A1 ∝ R⁻²`, `E_tank_w ∝ R⁺¹`) simply **re-measure the seed geometry's
> Derrick exponents**, which are hard-wired by the fixed-charge / conserved-circulation seed convention
> and are present at the instant of seeding, before any dynamics (CN evolution moves them <1%).

> **WHY THIS IS A DOWNGRADE, NOT A CONFIRMATION (independent verify — the near-tautology).** The Part-2
> "measured" exponents could NEVER have come out `p≥3`: the co-compress driver seeds the field with a
> fixed reactive charge `Q=∫|a|²` and conserved circulation `Γ_w=∮ω·dl`, which by construction FORCE
> `A²∝R⁻³` (⇒ `E_grad_A1∝R⁻²`) and `B∝R⁻¹` (⇒ `E_tank_w∝R⁺¹`). Those are the SAME algebraic constraints
> Part 1 uses to derive the exponents — so the sim re-reads the seed, it does not test it. The CN
> evolution changes the seeded exponents by <1%. The prereg's own anti-rescue guard **"HOLD REAL ODDS IT
> FAILS"** (§GUARDS, prereg) was therefore **NOT MET**: there was no failure route in-window. The sim is
> a REPRODUCTION of the seed geometry's Derrick exponents, NOT an independent dynamical confirmation that
> could have refuted. The verdict is downgraded to CONSISTENCY-class accordingly.

**Plain reading.** The prior bind-sim (PR #442, INCONCLUSIVE) measured the WRONG pull — the varactor
`dS/dr` ponderomotive pull, which is genuinely null at `A=√α` (`S=0.996`, flat). This run correctly
identified and measured the FIELD SELF-ENERGY gradient term off the engine's own Hermitian generator
`⟨x|H|x⟩`, and the **Part-1 derivation is sound**: in 3D, a localized field's gradient (self-energy)
force can never be steeper than `r⁻³`, and at fixed charge/circulation it points OUTWARD — so no field
self-energy pull can out-steepen the `r⁻³` brace, `p<3` is structurally forced, and the analytic
`F_R(R)` has exactly one crossing. **But that crossing was never dynamically reached or observed.** The
co-compress sim did not find a bound state; its window (`R≈2.9–5.6`) is entirely on the inward-pull side
(`F_net` inward everywhere), and the crossing `R*≈0.4` — below the sampled window (min 2.94) AND below
one lattice cell (`dx=0.5`) — is a `≈7×` extrapolation of two fitted exponents, not a measured
equilibrium. `crossing_bracketed=False`, `R_star=NaN` (stated as-is). The Part-2 exponents that "confirm"
Part 1 are the seed geometry's own Derrick exponents re-measured; the confirmation is a near-tautology,
not an independent test.

> **FLAG-DON'T-FIX (the load-bearing physics choice, surfaced for Grant — see §4).** The entire
> brace-vs-pull SIGN assignment is CONDITIONED on the **fixed-reactive-charge** compression ensemble
> (`Q=∫|a|²` held fixed). Under a fixed-AMPLITUDE ensemble instead (the Part-1 `a=0` row), the A1-gradient
> term FLIPS from an outward brace to an inward pull. Which ensemble is the physically-correct compression
> for a bound electron — fixed reactive charge, or fixed peak strain — is the load-bearing choice, and it
> is not settled here. Grant adjudicates. (A SECOND, smaller flag — the mechanism-NAME inversion between
> the derivation §5.2 "self-energy pulls in" and the substrate "self-energy braces out" — is retained in
> §4; note it is downstream of the same ensemble choice.)

---

## 1. WHAT WAS RUN (guard status)

TRAP-not-CREATE: the (2,3) winding PRE-EXISTS (seeded, conserved by construction on the frozen ê_w
template). NOT genesis, NOT the static eigensolve (#415/#417). ONE collective radius `R` co-compresses
BOTH sectors. Unitary lossless Crank–Nicolson (`port_sigma=0`).

| Guard | Status |
|---|---|
| FIELD SELF-ENERGY pull (gradient ∫|∇·|²/S off the engine's L_D), NOT the varactor ⟨S⟩ | ✅ measured the substrate's own gradient term |
| CO-COMPRESSING (one collective R; A1 envelope + winding torus scale together) | ✅ `s=R/R_ref` scales `a1_radius, R_w, r_w` together — but note (§0/§3) this makes the measured Derrick exponents a re-read of the seed convention, NOT an independent dynamical test |
| `Γ_w=∮ω·dl` conserved (seed ∝1/R) | ✅ within-window drift **4.2–4.5% < 5%** (prior 17%); converges 5.2→4.6→4.3 for N=32→40→48 |
| Tellegen-LOSSLESS (NO dissipative term) | ✅ `|dH/H|≈10⁻¹²` every row, both grids |
| TRAP-not-CREATE (winding pre-exists) | ✅ rigid_template ê_w; barred genesis slot not re-entered |
| Topological Link (2,3) conserved | ✅ `Q_link=3, w_tor=2` valid ALL rows, both grids |
| PML-excluded interior before top-K | ✅ `interior` mask; winding-loop top-K on interior only |
| Density-peak (winding-loop) sampling | ✅ top-K `|b_ω|²` radius (the collective R) — NOT A1 centroid |
| Reactance pair (C-state |b_ω| + L-state Im b_ω) | ✅ recorded over the window; active every row |
| Local-clock `ω_local(r)=ω_global√(1−A²)` | ✅ ≈0.996 at `A=√α` (recorded per row) |
| Resolution-robustness (≥2 grids) | ✅ N=40 AND N=48 — verdict does NOT flip; the EXPONENT contest is robust |
| No dissipative rescue | ✅ none used (a damping fix would be a FAIL not a fix) |
| Class-C (no number claimed) | ✅ α/A=√α/m_e/L_NODE imported/echo |

---

## 2. PART 1 — the DERIVED field self-energy pull exponent `p`

The energy functional read off the ACTUAL engine Hermitian generator `⟨x|H|x⟩`
(`coupled_cage_winding._assemble_H`, verify-before-cite `coupled_cage_winding.py:325–358`): the A1 block
`ω_b·I − c_A1²·L_D`, the winding block `ω_s·I − c_ω²·L_D`, `L_D=adjoint_div(D∇)`, `D=1/S(A)`. Integrating
by parts (`⟨f|L_D|f⟩=∫D|∇f|²`) gives four positive field-energy terms; Derrick-scaled under one collective
radius `R→λR` (d=3) with the load-bearing constraints held (fixed charge `Q=∫|a|²` ⇒ `A²∝R⁻³`; conserved
circulation `Γ_w=∮ω·dl` ⇒ `B∝R⁻¹`; `1/S(A)≈const` at `A=√α`):

| term | functional | `E ∝` | force `F_R=−dE/dR` | role | `p` |
|---|---|---|---|---|---|
| A1 gradient | `c_A1²∫|∇a|²/S` | `R⁻²` | `+2Qc²k_S/R³` | **BRACE (outward)** | **3** |
| winding gradient | `c_ω²∫|∇b|²/S` | `R⁻¹` | `+Γ²c²k_S/R²` | **BRACE (outward)** | **2** |
| A1 mass-tank | `ω_b∫|a|²` | const (fixed Q) | 0 | inert | — |
| winding LC-tank | `ω_s∫|b|²` | `+R` | `−Γ²ω_s` | **PULL (inward)** | **0** |

`F_R(R)=2Qc²k_S/R³+Γ²c²k_S/R²−Γ²ω_s` → **`+∞` as `R→0`** (braces dominate, no collapse), **`−Γ²ω_s<0` as
`R→∞`** (pull dominates, no dispersion) ⇒ **exactly ONE equilibrium `R*>0`**, and `dF_R/dR<0` EVERYWHERE
⇒ a **STABLE well**.

**DERIVED prediction (the crux):** the steepest inward (collapse) pull is the winding LC-tank,
**`p_derived = 0`**; the steepest brace is the A1 gradient self-energy, **`p_brace = 3`**.

**ROBUSTNESS (why `p<3` is structurally FORCED).** For any amplitude constraint `A²∝R⁻ᵃ`, the gradient
energy `∝ R^{d-2-a} = R^{1-a}` (d=3) and its force `|F|∝R^{-a}` ⇒ `p=a`. The steepest force is at maximal
charge-confinement (`a=3`, fixed charge): `E∝R⁻²`, `F=+R⁻³`, and it points **OUTWARD** (a brace). **No
constraint choice yields an inward gradient force steeper than `r⁻³` in 3D** — the `r⁻³` brace can never
be out-steepened by a field self-energy pull. `p<3` is forced. (Sympy, reproducible:
`drivers/electron_unifier_derrick.py`.)

**PART-1 DECISION GATE:** `p_derived = 0 < 3` ⇒ **PROCEED** to Part 2 (a NEGATIVE, `p_derived≥3`, would
have been bankable — the gate was live).

---

## 3. PART 2 — the CO-COMPRESS-MEASURED exponents (all numbers from the banked JSON)

Grids N=40, N=48 (both Link-valid across the whole `s∈[0.85,1.6]` sweep; `Γ_w` drift converged <5%).
The collective radius `R` = the winding-loop energy-density-peak radius (top-K `|b_ω|²`, interior).

### 3.1 The field self-energy scaling — the seed's Derrick exponent, RE-READ (not independently confirmed)

| N | `E_grad_A1` energy exponent (seed forces `R⁻²`) | BRACE-fit r² | `b_measured` (A1-gradient force) | force-fit r² |
|---|---|---|---|---|
| 40 | **2.12** | 0.9997 | **2.51** | 0.98 |
| 48 | **2.06** | 0.9998 | **2.53** | 0.98 |

The A1 gradient self-energy scales as `R⁻²` (the OUTWARD brace) to r²≈0.9998 on both grids. **The "three
nines" (r²=0.9997/0.9998) belong to THIS brace-energy fit ONLY.** And the `R⁻²` it fits is the exponent
the fixed-charge seed convention HARD-WIRES (`Q=∫|a|²` fixed ⇒ `A²∝R⁻³` ⇒ `E_grad_A1∝R⁻²`), present at
the instant of seeding — so this r²=0.9998 measures how cleanly the sim re-reads the seed, not whether
the dynamics independently produce `R⁻²`. The brace force exponent `b_measured≈2.5` (r²≈0.98)
finite-difference-under-reads the derived `p=3`.

### 3.2 The inward pull exponent `p_measured` — near-constant (consistent with `p≈0`), NOT precisely pinned

| N | `p_measured` (winding LC-tank inward pull) | PULL-fit r² | `E_tank_w` energy exponent (seed forces `E∝R⁺¹`) | brace out-steepens pull? |
|---|---|---|---|---|
| 40 | **0.32** | **0.76** | `+0.90` (`p_E=−0.90` in JSON, `|y|∝x⁻ᵖ` convention) | ✅ (`2.51 > 0.32`) |
| 48 | **0.15** | **0.56** | `+0.94` (`p_E=−0.94` in JSON) | ✅ (`2.53 > 0.15`) |

**Convention note (§3.2 sign).** The `E_tank_w` energy column is written as the PHYSICAL exponent
(`E∝R^{+0.90}`, energy RISES with `R` — the LC-tank store). The raw JSON reports it under the driver's
`fit_power_law` convention `|y|∝x⁻ᵖ` (`fit_power_law` docstring, `electron_unifier_cocompress.py:245`),
so the banked value is `E_tankw_energy_exp = −0.90 / −0.94`; the `+0.90 / +0.94` in this table is the
same quantity with the sign flipped to the physical `E∝R⁺⁰·⁹` reading. Both are the same fit; the sign
difference is the convention, not a discrepancy.

The inward binder is the winding LC-tank `ω_s∫|b|²`. Its force is **near-constant** across the window
(`F_tank_w ≈ −90`, an 18.5% spread N=40 / 12.9% N=48), i.e. **consistent with `p≈0`** — but the pull-fit
r² is only **0.76 (N=40) / 0.56 (N=48)**, so `p_measured=0.15–0.32` is NOT a precisely-pinned exponent;
it is "near-constant, consistent with `p≈0`," not "`p=0.2`." Do not read the `p_measured` figures as a
tight measurement (the three-nines r² is the BRACE fit, §3.1, not this pull fit). **`p_measured < 3` on
both grids and it does not flip — but this too is forced by the seed** (`E_tank_w∝R⁺¹` is the fixed-`Γ_w`
seed convention re-read), not an independent dynamical result.

### 3.3 The force balance `dF_net/dR` and the equilibrium `R*` — NO equilibrium observed or observable

Within the sampled co-compress window (`R≈2.94–5.57`), the **net collective-radius force `F_net` is
inward EVERYWHERE** (`F_net≈−70…−89`, dominated by the winding LC-tank pull `F_tank_w≈−90` vs the gradient
braces `F_grad_A1≈0.06–0.26`). There is **no sign change in-window**: `crossing_exists=False`,
`crossing_bracketed=False`, `R_star=NaN`, `stable_robust=False` (all banked, stated as-is). **No
equilibrium was observed, and none is observable in this window.**

The single crossing the Part-1 analytic guarantees sits at **`R*≈0.4`** (solving the fitted
`F_grad_A1 = c₃/R³` brace against the near-constant `F_tank_w≈−c₀` pull: `R*=(c₃/c₀)^{1/3}≈0.44`). That
is **below the sampled window (min `R=2.94`, a ≈7× extrapolation) AND below one lattice cell (`dx=0.5`)**
— i.e. `R*` is unresolvable on this lattice by more than a factor of a cell. The "well" is therefore a
**7× downward extrapolation of two fitted exponents** (a clean `R⁻²`/`R⁻³` brace and a near-constant
pull), NOT a measured or bracketable feature. The correct phrasing is
**"consistent-with-binding-at-the-exponent-level,"** not "the electron binds." The sim exercises the
exponent CONTEST (`p_pull≈0.2 < b_brace≈2.5`), but — per §0/§3.1 — that contest is itself the seed
convention re-read, so it is a consistency check on the FORM, not a dynamical demonstration of an
equilibrium.

### 3.4 `Γ_w` (circulation) conservation — the co-compress fix LANDED

| N | worst-row within-window `Γ_w` drift | prior (fixed-per-cell) |
|---|---|---|
| 40 | **4.5%** | 17% |
| 48 | **4.2%** | 17% |

The `B∝1/R` conserved-circulation seed brings the drift from 17% to ~4–5% (3–4× better). The residual is
a CONVERGING lattice artifact (deepest-loop row: 5.2%→4.6%→4.3% for N=32→40→48; it asymptotes to ~4%,
localized to the smallest/tightest compressed loop where lattice-pitch under-resolution dominates —
monotonic-ongoing, not oscillatory: a slow reactive `|curl ω|` exchange with A1). The topological Link
(2,3) is conserved exactly throughout; the ~4% is the dimensionful reactive-store measure. Both
verdict-grids pass the frozen `<5%` gate.

---

## 4. FLAG — the load-bearing physics choice + a mechanism inversion, surfaced not fixed (flag-don't-fix)

### 4.0 THE LOAD-BEARING FLAG (add for Grant): which compression ENSEMBLE?

**The entire brace-vs-pull SIGN assignment is CONDITIONED on fixed-reactive-charge normalization.** The
Part-1 Derrick scaling (§2) holds the enclosed reactive charge `Q=∫|a|²` FIXED as `R` shrinks
(`A²∝R⁻³`), and the co-compress driver seeds/renormalizes to the same fixed `Q`
(`electron_unifier_cocompress.py:275–277`, `Q_fixed=∫|a|²` from the `s=1` seed). Under THAT ensemble the
A1-gradient term is an OUTWARD brace (`E∝R⁻²`, `F=+/R³`).

**Under a fixed-AMPLITUDE ensemble instead** — the Part-1 `a=0` row / peak-strain-held-fixed convention —
**the A1-gradient term FLIPS to an INWARD pull.** (With `A=const`, the gradient energy `∫|∇a|²/S` scales
as `R^{d-2}=R⁺¹`, so its force is `−dE/dR<0`, inward — the opposite sign.) The whole "steeper brace
out-runs a shallower pull ⇒ stable well" story is therefore ensemble-dependent: it is the fixed-charge
picture. A fixed-amplitude picture rearranges which terms are braces and which are pulls.

**The question for Grant (plumber-physical):** *when you squeeze the electron, what stays fixed — the
reactive charge it stores (`Q=∫|a|²`), or the peak strain / amplitude (`A`) at its core?* This is not a
cosmetic mechanism-name difference; it is the load-bearing physics choice that determines the sign of the
dominant force and hence whether the Derrick balance even has the shape claimed. Fixed reactive charge is
the natural choice IF the electron's charge is the conserved topological/circulation quantity being held
(consistent with the (2,3)-winding = charge ownership); fixed amplitude is natural if the core saturates
to a strain the medium sets. **This is surfaced, NOT resolved — it is the physical premise the whole
consistency-class result rests on.**

### 4.1 The mechanism-NAME inversion (retained — note it is downstream of §4.0)

**The merged derivation §5.2 asserts the FIELD SELF-ENERGY is the INWARD pull; the substrate says (under
fixed reactive charge, §4.0) it is an OUTWARD brace.**

Verbatim, the two statements in tension:
- Derivation `research/2026-06-30_electron-portmap-derivation_result.md`:363 (Regime I) — *"A localized
  soliton's ponderomotive self-energy pull, away from the deep-saturation limit, scales like a
  Coulomb-class self-energy gradient, `P ∝ r^{−1}` to `r^{−2}` (`p ∈ [1,2] < 3`)."*
- This work (Part 1, §2): the field self-energy is the GRADIENT term `c²∫|∇·|²/S`. At fixed charge in 3D
  it scales `E∝R⁻²` and its force is `+2Qc²k_S/R³` — **OUTWARD (a brace, `p=3`), not an inward pull.**
  The actual inward binder is the winding LC-tank potential `ω_s∫|b|²` (`E∝+R`, force `−Γ²ω_s`, `p=0`).

**Why the verdict is unchanged either way.** Whether the inward pull is the winding LC-tank (`p=0`, what
the substrate says) OR a hypothetical Coulomb self-energy term (`p∈[1,2]`, what §5.2 asserts), **both are
`< 3`** and both are out-steepened by the `r⁻³` A1-gradient brace. `p<3` ⇒ STABLE holds under either
reading. **What differs is the mechanism NAME:** "the electron's mass compresses because its field
self-energy pulls it in" (§5.2) vs "the electron's field self-energy is what braces it OUTWARD against
the winding LC-tank's inward pull" (substrate). **Both file paths + verbatim content above; no reframe
applied.** Grant adjudicates which mechanism the corpus headlines. (Per the memory note: I carry the
same SM/soliton prior that a "self-energy pulls in" — but the substrate functional, at fixed charge,
is explicit: gradient energy RISES as the loop shrinks, so its force is outward. Surfaced, not resolved.)

**A second, smaller flag (§2.4-analog):** the derivation §3.1 brace is the winding **centrifugal**
circulation `L_w²/(m r³)` (a specific `r⁻³` from angular momentum). The substrate's steepest `r⁻³` brace
is the **A1-gradient** self-energy (a DIFFERENT `r⁻³`, from the mass-sector gradient at fixed charge).
Both are `r⁻³`-class outward braces; the substrate makes the A1-gradient one the dominant/cleanest
(r²=0.9998). Whether the load-bearing brace is the A1-gradient or the winding-centrifugal term is a
mechanism-identity question for Grant; the `r⁻³` SCALING (hence the stability) is the same.

---

## 5. VERDICT MAPPING (frozen criteria, none dropped — with the independent-verify downgrade applied)

- **(U1)** `p_derived < 3` (Part 1) — **HOLDS** (`p_derived=0`; structurally forced in 3D). This is the
  genuine, sound Part-1 FORM result.
- **(U2)** `p_measured < 3` resolution-robust — **HOLDS but NON-INDEPENDENT.** The measured exponents
  (`E_grad_A1∝R⁻²` r²=0.9998; `E_tank_w∝R⁺¹`; `p_measured=0.15–0.32`) are the fixed-charge /
  conserved-circulation SEED convention re-read (present before any dynamics; CN moves them <1%), so
  `p_measured<3` could not have failed in-window. It confirms the FORM is self-consistent, not that the
  dynamics independently realize it. (The pull-fit r² is only 0.56–0.76; see §3.2.)
- **(U3)** `dF_net/dR` STABLE at `R*` — **NOT DEMONSTRATED.** `crossing_exists=False`,
  `crossing_bracketed=False`, `R_star=NaN`, `stable_robust=False` (banked). `F_net` is inward everywhere
  in-window; the single crossing `R*≈0.4` sits below the window (≈7× extrapolation) AND below one lattice
  cell (`dx=0.5`). No equilibrium was observed or is observable. The stability is a Part-1 ANALYTIC
  property of `F_R(R)`, not a Part-2 measurement — correct phrasing is
  "consistent-with-binding-at-the-exponent-level," NOT "the electron binds."
- **(U4)** `Γ_w` conserved <5% — **HOLDS** (4.2–4.5%; converging; 3–4× better than prior 17%). This
  confirms the co-compress instrument's measurement PREMISE landed; it does not bear on binding.
- **(U5)** Tellegen-lossless — **HOLDS** (`|dH/H|≈10⁻¹²`, NO dissipative term).

**Revised verdict: CONSISTENCY-class, NOT UNIFIER-CONFIRMED.** U1/U4/U5 hold cleanly; U2 holds only as a
non-independent re-read of the seed (no failure route — the prereg "HOLD REAL ODDS IT FAILS" guard was
NOT met); **U3 is NOT DEMONSTRATED** — no bound state was dynamically observed, and none is observable in
the sampled window. The frozen `UNIFIER-CONFIRMED iff ALL of U1–U5` therefore does NOT trigger, because
U3 (the stable equilibrium — the actual "does it hold together" criterion) is not met. Per Rule 11 this
is reported as the honest downgrade, not debugged toward a pass: the criteria were not dropped; U3 was
re-read correctly against the banked `crossing_exists=False` after the independent verify caught that the
prior "HOLDS BY EXPONENT" reading imported the Part-1 analytic conclusion into a Part-2 slot the sim
never measured. The grid set (N=40/48) note stands (N=24 Link-misreads; N=32's deepest-loop row grazes
the 5% boundary), but resolution-robustness of a re-read seed exponent is not, by itself, a confirmation
of binding.

---

## 6. SOLIDITY + OPEN ITEMS

| Part | Finding | Solidity |
|---|---|---|
| Part-1 Derrick scaling | 4 terms, `p_derived=0` pull, `p_brace=3`, single analytic crossing | **SOLID** (sympy, reproducible; robustness `p=a` closed-form) — the genuine Class-C FORM result |
| Part-1 `p<3` FORCED in 3D | no gradient force steeper than `r⁻³`, steepest is outward (at fixed charge) | **SOLID** (dimensional, constraint-independent) — CONDITIONED on the fixed-charge ensemble (§4.0) |
| E_grad_A1 `∝R⁻²` | measured r²=0.9997/0.9998 | **CONSISTENCY-only** — this exponent is HARD-WIRED by the fixed-charge seed convention (present before dynamics); the sim RE-READS it, does not independently test it |
| `p_measured<3` | 0.15–0.32, no grid-flip; pull-fit r²=0.56–0.76 | **CONSISTENCY-only** — seed convention re-read; no failure route in-window (prereg "HOLD REAL ODDS IT FAILS" NOT met); the pull is near-constant (consistent with `p≈0`), NOT a pinned exponent |
| brace out-steepens pull | `2.5 > 0.2` both grids | **CONSISTENCY-only** — the exponent contest is the seed convention re-read, not a dynamical demonstration |
| directly-observed bound state / `R*` | `crossing_exists=False`, `R_star=NaN`, `stable_robust=False`; `R*≈0.4` below window (≈7×) + below one cell (dx=0.5) | **NOT OBSERVED / NOT DEMONSTRATED** — no equilibrium observed or observable; the electron is NOT shown to hold together |
| `Γ_w` conservation | 4.2–4.5%, converging | **SOLID-with-residual** (3–4× better than 17%; measurement premise landed; ~4% converging lattice artifact, Link exact) |
| Losslessness | `|dH/H|≈10⁻¹²`, no dissipative term | **SOLID** (unitary CN; #83 crutch NOT used) |
| compression ensemble (fixed charge vs fixed amplitude) | §4.0 — brace/pull sign flips with ensemble | **FLAGGED for Grant** (load-bearing; the whole sign story rests on it) |
| mechanism identity (which pull, which brace) | §4.1 inversion | **FLAGGED for Grant** (downstream of §4.0) |

**Open items:**
1. **Compression ENSEMBLE (§4.0) — load-bearing, for Grant.** Is fixed-reactive-charge (`Q=∫|a|²` fixed)
   the physically-correct compression ensemble for a bound electron, or is it fixed-amplitude (peak strain
   held)? The A1-gradient term is an OUTWARD brace under fixed charge and an INWARD pull under fixed
   amplitude — so the sign of the dominant force, and whether the Derrick balance has the claimed shape,
   depends on this choice. This is the premise the entire consistency-class result rests on; surfaced, not
   resolved.
2. **A dynamical binding test that COULD fail (Rule-11 / prereg follow-on).** The co-compress sim as built
   cannot refute (it re-reads the seed exponents). A genuine test would (a) place `R*` INSIDE the
   resolvable window via a seed calibration, and (b) NOT normalize to the fixed-charge convention that
   pre-determines the exponents — e.g. free-relax a seeded soliton and watch whether it settles to a
   finite `R` or collapses/disperses. Until such a test runs, the electron's binding is NOT demonstrated.
3. **Mechanism headline** (§4.1) — Grant: is the inward binder the winding LC-tank (`p=0`, substrate) or
   the field self-energy (`p∈[1,2]`, §5.2 asserted)? Downstream of item 1 (the ensemble choice). The
   derivation §5.2 wording should be reconciled to whichever ensemble Grant selects.
4. **`Γ_w` ~4% residual** — a converging lattice artifact (reactive `|curl ω|`↔A1 exchange); the
   topological Link is exact. Not load-bearing for the (downgraded) verdict.
5. **NOT a route-space exhaustion.** The Part-1 balance is on the CANONICAL 3-channel functional at
   `A=√α`. A not-yet-named additional term could change the picture; not claimed exhausted.

---

## 7. CLASSIFICATION (consistency-vs-emergence — final)

**Class C — CONSISTENCY / FORM-chord.** No number was claimed. `α` sets the operating point `A=√α`
(`V_yield=√α·V_snap`, `constants.py:464`, an exact α-echo); `m_e`, `L_NODE` imported; the SIZE `R*` is a
scale tied to imported `L_NODE=ℏ/(m_e c)`. The mechanism (a steeper brace out-running a shallower pull
under one collective radius) is at best a FORM-chord peer-with-SM: it supplies a candidate SM-absent
FORM for a stable localized electron, but computes NO dimensionless observable free of the target ⇒ NOT
Class-D emergence (A47 v17 family). **The downgraded verdict is a Class-C CONSISTENCY result, not a
confirmation:** the Part-1 Derrick FORM is genuinely derived (a single crossing, `p<3` forced in 3D under
the fixed-charge ensemble); but the Part-2 sim re-reads the seed's Derrick exponents rather than
independently testing them, no bound state was dynamically observed, and the sign of the whole balance is
conditioned on the un-adjudicated compression ensemble (§4.0). The substrate's fixed-charge scaling is
CONSISTENT with a self-braced electron; the electron is NOT shown to hold together as one object, and its
VALUE (`m_e`, size) remains definitional/imported.

---

## 8. GUARDS WALKED (checklist)

- **substrate-native-check:** the energy functional is READ OFF the engine's own Hermitian generator
  `⟨x|H|x⟩` (native K4 `L_D=adjoint_div(D∇)` on `TETRA_OFFSETS`), NOT a posited continuum action; the
  balance is a Derrick reactive-pressure scaling at a self-set operating point, NOT Lagrangian-min /
  gradient-descent / continuum-Helmholtz (CP1–5); ports native Cosserat (A1⊥winding), not Cartesian.
- **phase-space-coordinate-check:** `p` and the balance live in the COLLECTIVE ENVELOPE RADIUS `R` (the
  derivation's `r*`), measured as the winding-loop peak-density radius; the (2,3) Link stays in its
  phase-space home (frozen ê_w integer); the DIMENSIONFUL circulation `Γ_w` is the co-compressed
  conserved quantity. No real-space-vs-φ² mismatch (the A47/A46 error avoided).
- **consistency-vs-emergence:** Class-C throughout (§7); α a KNOB/echo, not computed.
- **ave-prereg:** frozen `9f388305` BEFORE the Part-2 run; criteria applied, none dropped. On re-read
  against the frozen `UNIFIER-CONFIRMED iff ALL of U1–U5`, **U3 (stable equilibrium) is NOT met**
  (`crossing_exists=False`), so the verdict is CONSISTENCY-class, not UNIFIER-CONFIRMED. The prereg
  anti-rescue guard "HOLD REAL ODDS IT FAILS" was NOT met by the Part-2 sim (the co-compress instrument
  re-reads the seed convention and had no failure route in-window) — this is recorded, not papered over.
- **ave-canonical-source:** `ALPHA`, `V_SNAP`, `V_YIELD`, `L_NODE` from `src/ave/core/constants.py`
  (`:154,455,464,282`); no hardcoded targets; the winding factor κ̃=6/5 / θ_χ α-free path inherited.
- **verify-before-cite:** the §4 derivation quote greped from `:363` this session; the engine H terms
  read from `coupled_cage_winding.py:325–358`, `native_cage_imex.py:148`, `graded_vacuum_network.py:245`
  this session; constants read this session.
- **flag-don't-fix:** the load-bearing compression-ensemble choice (fixed reactive charge vs fixed
  amplitude, §4.0 — the sign of the dominant force flips with it), the mechanism-name inversion (§4.1),
  and the brace-identity (A1-gradient vs winding-centrifugal) are SURFACED with both paths + verbatim,
  NOT silently resolved. No reframe applied to make the sim look like a confirmation.
- **honest-closure (Rule 11):** the independent verify caught that the Part-2 sim RE-MEASURES the seed
  geometry's Derrick exponents (a near-tautology — no failure route), so the verdict is DOWNGRADED
  UNIFIER-CONFIRMED → CONSISTENCY-class rather than debugged toward a pass; U3 (equilibrium) reported as
  NOT DEMONSTRATED against the banked `crossing_exists=False`; no criterion dropped; the `Γ_w` residual +
  its converging-artifact mechanism named; NO dissipative rescue (#83 lesson); NO slot refilled (A47
  v11b — the substitution-not-retraction discipline: the falsified "confirmed-binding" claim is retracted
  in place, NOT refilled with a new unverified binding hypothesis). Part-1 (the genuine FORM result) is
  preserved; only the Part-2 over-claim is downgraded.
- **Rule-10 empirical-driver:** the driver was piloted early; two instrument defects were CAUGHT and
  FIXED at pilot (A1-core peak radius does not track the collective size → winding-loop radius; N=24/N=32
  cannot carry the template → N=40/48), and surfaced in the driver comments + this doc, not hidden.

## 9. PROVENANCE / REPRODUCIBILITY

- Part 1 (sympy, in-driver): `drivers/electron_unifier_derrick.py` — `E∝λⁿ` per term, `F_R`, `dF_R/dR<0`,
  single stable `R*`, robustness `p=a`. Run: `PYTHONPATH=src python research/drivers/electron_unifier_derrick.py`.
- Part 2 (co-compress sim): `drivers/electron_unifier_cocompress.py`, raw
  `drivers/electron_unifier_cocompress_results.json` (N=40/48 suite). Run:
  `PYTHONPATH=src python research/drivers/electron_unifier_cocompress.py`.
- Prior state held as prior odds: `2026-06-30_electron-portmap-derivation_result.md` (§5 BIND now
  SYMBOLIC-ONLY per PR #442 caveat-fold `4cdaeb36`); `2026-06-30_electron-bind-sim_result.md`
  (INCONCLUSIVE, `efb5b8ef`); `#415/#417` (eigenmode DOES-NOT-EXIST); `#83` (RETRACTED dissipative artifact).
- Constants (verify-before-cite, this session): `√α=0.08542`, `S(√α)=√(1−α)=0.99634`, `V_SNAP=511.0 kV`,
  `V_YIELD=√α·V_SNAP=43.65 kV` (`constants.py:464`), `L_NODE=3.862e−13 m` (`:282`).
- NO KB/manuscript edits (research/ only, per scope). Branch-only; orchestrator opens the PR after an
  independent verify.
