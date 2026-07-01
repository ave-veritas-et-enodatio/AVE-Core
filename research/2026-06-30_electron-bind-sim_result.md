# RESULT — Electron self-braced BIND sim: MEASURE the deep-core pull slope `p`

**Date:** 2026-06-30 · **Lane:** implementer · **Branch:** `analysis/electron-bind-sim`
(worktree `/private/tmp/electron-bind-sim`, off `main` @ `e1e14572` — the MERGE of PR #441).
**Prereg (frozen FIRST):** [`2026-06-30_electron-bind-sim_prereg_FROZEN.md`](2026-06-30_electron-bind-sim_prereg_FROZEN.md)
(frozen commit `f678b0fc`). Adjudication criteria followed exactly; none dropped/weakened (Rule 11).
**Type:** SIMULATION (time-domain force-balance). Driver: [`drivers/electron_bind_sim.py`](drivers/electron_bind_sim.py),
runner [`drivers/run_electron_bind_sim.py`](drivers/run_electron_bind_sim.py), raw
[`drivers/electron_bind_sim_results.json`](drivers/electron_bind_sim_results.json).
**Class (consistency-vs-emergence):** **C — CONSISTENCY** throughout (`α`, `A=√α`, `m_e` all
imported/echo; no dimensionless observable computed free of the target). NOT emergence.

---

## 0. VERDICT (headline)

> **INCONCLUSIVE — RESOLUTION-LIMITED, with a single named mechanism (Rule 11 honest closure).**
> The measured deep-core pull slope `p` **FLIPS with grid** (`p=5.23`, r²=0.82 at N=24 vs
> `p=−0.06`, r²=0.003 at N=32) → by the frozen INCONCLUSIVE criterion the `p<3`-vs-`p>3` verdict
> does NOT hold across resolutions. The flip is **not** stochastic: the ROOT CAUSE is
> resolution-robust and physical — at the T2 operating point `A=√α≈0.085` the varactor saturation
> `S(A)=√(1−A²)≈0.996` sits in `[0.996, 1.000]` across the ENTIRE core (S-range **0.35%**, identical at
> N=24 and N=32), so the ponderomotive potential `⟨S(A(r))⟩` the derivation §2.1(i) reads is **FLAT to
> <1%** (U_pond fractional spread 0.6–0.7% across the whole envelope-radius sweep, both grids). There is
> **no ponderomotive well of measurable depth** at `A=√α`; the fitted `p` is the gradient of a flat-to-
> noise potential, which is why it flips.
>
> **The `CoupledCageWinding` engine does NOT exercise the derivation's pull-vs-brace steepness contest
> at the sub-saturated `A=√α` operating point.** This is a Checkpoint-9 **WALL-engine** capability
> finding (the load-bearing observables — the ponderomotive `dS/dr` pull and the conserved-`L_w`
> centrifugal brace — are not dynamically realized here at this operating point), NOT a physics-floor
> falsification of the electron and NOT a confirmation. The symbolic BIND verdict (derivation §5.3) is
> **NEITHER confirmed NOR refuted** by this instrument.

**Plain reading.** The sim did not measure a `p` we can place relative to 3, because the mechanism the
`p` describes is essentially switched OFF at the operating point the T2 ruling assigns the electron. The
same fact the derivation uses to argue the electron binds — *`S(√α)=0.996`, the `S→0` runaway never
fires* — ALSO means the varactor is nearly LINEAR there, so the ponderomotive pull (which is a
saturation-`dS/dr` effect) has no steepness to measure. This is honest and resolution-robust: the
instrument cannot decide the fork at `A=√α`; the fork stays open, and a real contradiction between the
derivation's own two claims is surfaced (§4).

---

## 1. WHAT WAS RUN (guard status)

TRAP-not-CREATE: the (2,3) winding PRE-EXISTS (seeded, conserved by construction on the frozen ê_w
template). NOT genesis, NOT the static eigensolve (#415/#417). All runs on the **unitary lossless**
Crank–Nicolson solver (`port_sigma=0` → closed/lossless), `V_yield=1` native, `A` set to `√α`.

| Guard | Status |
|---|---|
| Tellegen-LOSSLESS (NO dissipative term) | ✅ `|dH/H| ≤ 2.5×10⁻¹²` at every step, both grids (solver tol) |
| TRAP-not-CREATE (winding pre-exists, not genesis) | ✅ seeded rigid_template; barred genesis slot not re-entered |
| Topological Link conserved (the (2,3)) | ✅ `Q_link=3, w_tor=2` held through all evolution, both grids |
| PML-excluded interior before any top-K | ✅ `interior` mask; `top_k_peak_radius` argpartition on interior only |
| Density-peak (not centroid) sampling | ✅ top-K `|field|²` radius read |
| Reactance pair (C-state `|b_ω|` + L-state `Im b_ω`) | ✅ recorded over the window; `reactive_pair_active=True` |
| Local-clock `ω_local(r)=ω_global√(1−A²)` | ✅ = 0.9963 at `A=√α` (0.37% modulation — small, recorded) |
| Resolution-robustness (≥2 grids) | ✅ N=24 AND N=32 — and it is the ROBUSTNESS that delivers the INCONCLUSIVE |
| No dissipative rescue introduced | ✅ (a damping term would be a FAIL not a fix — none used) |
| Class-C (no number claimed) | ✅ α/A=√α/m_e imported/echo |

---

## 2. THE MEASUREMENTS (the deliverable, all numbers from the banked JSON)

### 2.1 Saturation dynamic range — the ROOT CAUSE (resolution-robust)

At `A=√α` the varactor is nearly linear; there is no `dS/dr` steepness for a ponderomotive pull to
have a slope:

| N | S range across core | S-range frac | coupling Ω_max | front_gate(A=√α) | S(√α) |
|---|---|---|---|---|---|
| 24 | [0.99634, 0.99986] | **3.51×10⁻³** | 7.8×10⁻³ | 0.026 | 0.9963 |
| 32 | [0.99634, 0.99999] | **3.64×10⁻³** | 7.8×10⁻³ | 0.026 | 0.9963 |

The front-gated A1↔ω coupling (which engages at the saturation front `A≈4/7`) is at `g_front=0.026` at
`A=√α` — 38× down from its peak. The AC swing it drives is `δA ~ 10⁻⁴`, so the rectification term
`¼S''δA² ~ 10⁻⁸·S''` is negligible.

### 2.2 Deep-core PULL slope `p` (fixed enclosed charge Q, derivation §3.4 model) — FLIPS with grid

Envelope-radius sweep, `Q` held fixed (203±1), so `A_peak ~ Q/r` correctly RISES as the envelope
shrinks (0.039 → 0.199 across `r_env` 5.0 → 1.5):

| N | U_pond fractional spread | fitted `p` | fit r² | 3−p | stable? |
|---|---|---|---|---|---|
| 24 | **0.72%** | **5.23** | 0.82 | −2.23 | ❌ |
| 32 | **0.61%** | **−0.06** | 0.003 | +3.06 | ✅ |

**The verdict flips** (`p>3` unstable at N=24, `p<3` stable at N=32) because `U_pond` varies by <1% — the
`p` is a fit to the numerical gradient of a **flat** potential. The direct `U_pond`-vs-`r_env` slope is
`≈0.00` (r² 0.67/0.96) at both grids — i.e. **no measurable `r`-dependence of the ponderomotive energy at
`A=√α`.** This is criterion INCONCLUSIVE (the slope verdict does not hold across the ≥2 resolutions and
the dynamic range is too small to place `p` relative to 3).

### 2.3 BRACE slope (winding-loop-radius coordinate) — NOT the predicted `r⁻³`

The `r⁻³` brace lives in the winding LOOP radius (the loop the conserved circulation is confined to), a
DIFFERENT coordinate from the A1 envelope (the A1 sweep does not compress the winding template — §5
flag). Sweeping the loop radius:

| N | U_rot vs loop-r slope | expect | brace `b` (=−d U_rot/dr slope) | expect |
|---|---|---|---|---|
| 24 | +1.49 (r²=0.996) | −2 (centrifugal `L²/2I`) | not resolvable | −3 |
| 32 | +1.65 (r²=0.997) | −2 | not resolvable | −3 |

`U_rot=Σ|curl ω|²` **RISES** with loop radius (a bigger torus template holds more winding field), the
OPPOSITE of the centrifugal `L_w²/(2 m_eff r²)∝r⁻²`. The seeded circulation is per-cell-fixed, so its
store scales with loop VOLUME, not as a conserved-`L_w`-in-a-shrinking-loop. **The `r⁻³` brace scaling is
not exercised by this seed.**

### 2.4 `L_w` (circulation quantum) — MEASURED; and it DRIFTS under lossless evolution

- **Topological read (the hypothesis `L_w`=Link):** `Q_link=3`, `w_tor=2` — the (2,3) winding integer,
  conserved by construction (the phase-space-home invariant on the frozen ê_w). |Link|=1 poloidal.
- **Measured reactive circulation (angular momentum `|L_w|=|Σ r×ω|`):** **DRIFTS 16–17%** over 40 steps
  (N=24: 31.85→26.61; N=32: 25.10→20.79) — while the topological Link is conserved AND `|dH/H|≈2×10⁻¹²`.
  So the winding's angular momentum is NOT constant under the coupled lossless evolution (it disperses /
  exchanges with A1). **The `L_w=const` premise the derivation §3.1 brace rests on is NOT satisfied by
  the engine.** (Prereg N4 territory — but see §3: the primary verdict is INCONCLUSIVE, this is a
  contributing named-mechanism finding, not the headline.)

### 2.5 α-ROBUSTNESS SWEEP (the keystone test) — the mechanism has NO teeth anywhere in small-α

Varying `α` slides the operating point `A=√α`. The S-range stays tiny across the whole sweep:

| α_eff | A_op=√α | S-range frac | fitted p (r²) |
|---|---|---|---|
| α/4 = 0.00182 | 0.0427 | 9.0×10⁻⁴ | −3.63 (0.98) |
| α/2 = 0.00365 | 0.0604 | 1.8×10⁻³ | −3.63 (0.98) |
| **α = 0.00730** | **0.0854** | **3.6×10⁻³** | −3.63 (0.98) |
| 2α = 0.01459 | 0.1208 | 7.2×10⁻³ | −3.63 (0.98) |
| 4α = 0.02919 | 0.1708 | 1.5×10⁻² | −3.63 (0.98) |

The fitted `p` is IDENTICAL (−3.63) across all α because `U_pond` is flat at every operating point — the
fit is picking up the same near-flat noise shape, not a physical slope. **The keystone test cannot be
adjudicated:** the mechanism never gets teeth (S-range < 1.5% even at 4α), so there is no
knife-edge-vs-keystone signal to read. This does NOT earn "keystone, not fine-tune" — but it also does
NOT show a knife-edge; the sim simply cannot measure the axis at these operating points.

---

## 3. VERDICT MAPPING (frozen criteria, none dropped)

- (C1) `p<3` resolution-robust — **FAILS** (flips: 5.23 @ N=24 / −0.06 @ N=32; U_pond flat <1%).
- (C2) brace `r⁻³` — **FAILS** (U_rot rises with loop radius, +1.5 not −2).
- (C3) `dF_net/dr>0` — **UNDETERMINED** (follows from an unmeasurable `p`).
- (C4) losslessness `|dH/H|` at tol — **HOLDS** (`≤2.5×10⁻¹²`, NO dissipative term).
- (C5) α-robust margin — **UNDETERMINED** (no teeth anywhere in small-α).
- (N4) `L_w` unwinds — **the ANGULAR-MOMENTUM `L_w` drifts 17%** (Link conserved); contributes.
- (N5) needs damping — **NO** (no dissipative rescue; C4 clean).

**Frozen INCONCLUSIVE condition met:** *"the slope verdict does NOT hold across the ≥2 resolutions
(the `p<3` vs `p>3` verdict FLIPS with grid), OR the fit R²/dynamic range is too poor to place `p`
relative to 3."* BOTH sub-conditions fire. → **INCONCLUSIVE (resolution-limited).**

**Rule-11 single mechanism (all failure paths → one cause):** at `A=√α` the varactor saturation is
nearly linear (`S≈0.996`, S-range 0.35%), so (a) the ponderomotive pull `∝dS/dr` has no measurable
slope, (b) the front-gated coupling that would drive the AC rectification is 38× down, and (c) the
winding store on a fixed template does not realize a conserved-`L_w`-in-a-shrinking-loop. All three are
the SAME fact — the electron's T2 operating point sits in the LINEAR corner of the saturation kernel,
where the nonlinear pull/brace steepness contest the derivation frames simply has no dynamic range. The
branch closes as INCONCLUSIVE-with-named-mechanism; it is NOT debugged toward a rescue.

---

## 4. FLAG — a contradiction inside the derivation, surfaced not fixed (flag-don't-fix)

**The derivation §5.2 asserts the pull at `A=√α` is "Coulomb-class `p∈[1,2]<3`." This sim's measurement
of the pull the derivation §2.1(i) DEFINES (the ponderomotive varactor-energy gradient
`P=−∂⟨½Q²S(A)/C_0⟩/∂r`) shows it is ~ZERO at `A=√α` (flat `U_pond` to <1%), not a `p∈[1,2]` power law.**

Verbatim, the two corpus statements in tension:
- Derivation result `research/2026-06-30_electron-portmap-derivation_result.md`:363–364 (Regime I) —
  *"A localized soliton's ponderomotive self-energy pull, away from the deep-saturation limit, scales
  like a Coulomb-class self-energy gradient, `P ∝ r^{−1}` to `r^{−2}` (`p ∈ [1,2] < 3`)."*
- This sim (§2.2): the ponderomotive potential `⟨S(A(r))⟩` is FLAT to <1% at `A=√α`; there is no
  `r^{−1..−2}` power law because `S(A)` is nearly constant when `A≪1`.

**The resolution is NOT mine to make (surfaced for Grant):** the derivation appears to invoke TWO
different "pulls" under one name. (i) The **ponderomotive/varactor** pull it §2.1(i) DERIVES is a
saturation-`dS/dr` effect — which this sim confirms is null at `A=√α` (S flat). (ii) The **Coulomb-class
self-energy** pull it §5.2 ASSERTS is a soliton electrostatic/strain self-energy gradient — a DIFFERENT,
larger term that is NOT the varactor `dS/dr` and is NOT modeled by `CoupledCageWinding`. If the
load-bearing inward leg is actually (ii), then (a) the derivation's §2 "the pull IS the rectified
varactor compression" mechanism is not the binding pull, and (b) this sim measured the wrong (null) term
and a self-energy-pull instrument is needed. If it is (i), then the pull is genuinely null at `A=√α` and
the §5.2 `p∈[1,2]` claim is unsupported. **Both file paths + verbatim content above; no reframe applied.
Grant adjudicates which pull is load-bearing.**

---

## 5. FLAG — the winding-loop vs A1-envelope coordinate (the prereg Grant-flag, now with data)

The prereg surfaced (and this sim confirms with data): in `CoupledCageWinding` the winding loop radius
(`R, r` template) is a FIXED seed parameter that does NOT dynamically couple to the A1 envelope size.
So the derivation's single collective radius `r*` (in which BOTH `P(r)` and `B(r)` live, §4
`r*=(c_P/c_B)^{1/(p−3)}`) is realized in the engine as TWO decoupled coordinates (A1 envelope size,
winding loop size). The `r⁻³` brace's compression premise (shrink the loop → circulation reactive
pressure rises) is not exercised when the A1 core is compressed, because the loop does not follow. A
faithful test of the derivation's SINGLE-`r*` balance needs a solver where the winding loop is
dynamically tied to the A1 envelope (a genuine co-compressing soliton), which this instrument is not.
**Flagged for the sim-spec of any follow-on; does not change the INCONCLUSIVE verdict.**

---

## 6. SOLIDITY + OPEN ITEMS

| Part | Finding | Solidity |
|---|---|---|
| Losslessness | `|dH/H|≤2.5e−12`, no dissipative term | **SOLID** (unitary CN; resolution-robust) |
| Link conservation | (2,3) `Q_link=3,w_tor=2` held | **SOLID** (by construction, both grids) |
| S-range at `A=√α` | 0.35%, S∈[0.996,1.000] | **SOLID** (resolution-robust root cause) |
| U_pond flatness | <1% spread over the envelope sweep | **SOLID** (both grids, both fixed-Q + A_op-fixed) |
| pull `p` | flips 5.23↔−0.06 with grid | **INCONCLUSIVE** (the verdict itself) |
| brace `r⁻³` | U_rot rises with loop-r (+1.5) | **NOT REALIZED** by this seed |
| `L_w` angular momentum | drifts 17% (Link conserved) | **SOLID** (both grids) — premise unmet |
| §4 derivation-internal pull ambiguity | varactor-`dS/dr` (null) vs Coulomb-self-energy (unmodeled) | **FLAGGED for Grant** |

**Open items:**
1. **Which pull is load-bearing** (§4) — Grant adjudication: the varactor-`dS/dr` pull (this sim: null at
   `A=√α`) or a Coulomb-class self-energy pull (unmodeled here). Blocks any BIND CONFIRMATION.
2. **A co-compressing-soliton instrument** (§5) — needed to test the single-`r*` balance the derivation
   poses; `CoupledCageWinding`'s fixed winding template cannot.
3. **`L_w`-conservation** (§2.4) — the angular-momentum drift under coupled evolution needs its own
   diagnosis (dispersion vs A1-exchange); the topological Link stands.
4. **NOT a falsification of the electron.** INCONCLUSIVE = the instrument cannot decide the fork at
   `A=√α`; the symbolic BIND verdict is untouched (neither confirmed nor refuted). No new hypothesis
   refills any slot (A47 v11b).

---

## 7. CLASSIFICATION (consistency-vs-emergence — final)

**Class C — CONSISTENCY.** No number was claimed. `α` was a KNOB (swept), not computed; `A=√α` is an
exact α-echo (`V_yield=√α·V_snap`, `constants.py:464`); `m_e`, `L_NODE` imported. The INCONCLUSIVE
verdict is a Class-C consistency result: the FORM (the pull/brace steepness contest) could not be
measured because the mechanism has no dynamic range at the imported operating point. No emergence-class
claim anywhere (A47 v17 family).

---

## 8. GUARDS WALKED (checklist)

- **substrate-native-check:** CP1 time-domain reactive-pressure balance (not eigensolve/gradient-descent);
  CP4 coordinate discipline — corrected at pilot from within-soliton profile to collective envelope
  radius (the derivation's `r`); CP5 local-clock recorded (0.37%); CP6 reactance pair tracked; CP7
  PML+density-peak; CP8 TRAP-not-CREATE (not a hosting test); CP9 the load-bearing observable is the
  ponderomotive `dS/dr` — DIAGNOSED as a WALL-engine gap at `A=√α` (S flat), stated as such; CP10 the
  pull read is the BOUNDED `⟨S⟩` gradient (S∈[0.996,1], far from the wall), NOT the singular bulk force.
- **phase-space-coordinate-check:** the (2,3) Link stays in its phase-space home (frozen ê_w); the `p`
  slope is the derivation's real-space COLLECTIVE-envelope-radius scaling (coordinate-matched after the
  pilot correction); no φ²/`R_phase` claim measured in real-space.
- **consistency-vs-emergence:** Class-C throughout; α a swept KNOB, not computed.
- **ave-prereg:** frozen `f678b0fc` BEFORE any run; criteria applied, none dropped; INCONCLUSIVE is a
  frozen verdict, not a post-hoc invention.
- **ave-canonical-source:** `ALPHA`, `V_SNAP`, `V_YIELD`, `L_NODE` from `src/ave/core/constants.py`.
- **verify-before-cite:** the §4 derivation quote greped from the result doc this session; constants
  read from `constants.py:154,455,464,282` this session.
- **flag-don't-fix:** the derivation-internal pull ambiguity (§4) and the winding-loop coordinate (§5)
  are SURFACED with both paths + verbatim content, NOT silently resolved.
- **honest-closure (Rule 11):** no criterion dropped; INCONCLUSIVE reported as-is; single mechanism named
  (linear-corner varactor at `A=√α`); no dissipative rescue; no slot refilled.
