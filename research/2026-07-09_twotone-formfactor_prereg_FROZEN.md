# TWO-TONE FOUR-PHOTON FORM FACTOR (FORK A) — Pre-Registration (FROZEN)

**Date:** 2026-07-09
**Task:** #31-A — "run it" (Grant standing ruling). The two-tone difference-frequency
four-photon form-factor measurement queued as **FORK A** by the repaired x29 super-band
carrier test (`research/2026-07-09_superband-carrier-fork_result.md` §4, §8.2).
**Branch:** `analysis/x31a-twotone-formfactor` (off `main` @ post-#604/#605, which includes
the repaired x29 driver).
**Status:** **PREREG ONLY — fork record + analytic expectations + gates + adjudication FROZEN
before the production driver.** A throwaway pilot (scratchpad, uncommitted) fixed numerical
parameters (N, dt, sponge, tmax) and numerically CONFIRMED the parity theorem of §5; it did
NOT set the adjudication criteria below, which are physics-principled and frozen here.
**Base driver (Rule 14):** `src/scripts/vol_1_foundations/superband_carrier_fork.py` — the
repaired x29 driver. This run's driver imports its **tagged conservative kernel castings**
(`F_bond`, `U_bond`, `energy_density`, `analytic_kappa`, `sponge_profile`) unmodified and
adds the two-tone machinery (Rule 14: extend, do not re-implement the kernel).
**Skills applied:** `ave-prereg` (v1.6 analytic-expectations §6), `substrate-native-check`
(§4), `pre-test-physics-check` (§0.1 — one plumber-physical question surfaced), `phase-space-
coordinate-check` (A46, §4.4), `consistency-vs-emergence` (§10), `substrate-first-for-numbers`,
`verify-before-cite` (kernel/constants cites verified on this worktree), `ave-driver-script-
honesty` (gates §8), `pure-AVE-corpus`.

---

## 0. TL;DR of the design + the key pre-run physics finding

Drive **two tones** ω_lo, ω_hi, **both above the 1D chain's band top (ω_top = 2.0 ω_C)** —
evanescent, non-propagating, but establishing real skin-region amplitudes. If the vacuum's
χ³ (four-photon) vertex is alive at super-band frequencies, the saturable varactor mixes the
two evanescent shakes into a **propagating in-band** product. **Gate 1** (entry skin) is
measured physics (x29 verified cosh κ = ω²/2−1 to <1%). **Gate 3** (in-band escape) is open by
design. **Gate 2** — where the injected energy sits (spring vs mass), i.e. the form factor —
is THE measurement.

**★ KEY PRE-RUN FINDING (perturbative bookkeeping, §5; numerically confirmed in the pilot).**
The reversible sub-yield kernel `U(r)=1−√(1−r²)` is **even in r** ⇒ its force `F(r)=r+½r³+…`
is **odd** ⇒ the medium is a **pure χ³ (inversion-symmetric) varactor** below yield. A rigorous
parity theorem (§5.2) then forces: **the two-tone response contains a spectral line at
`m·ω_lo + n·ω_hi` ONLY when `m+n` is ODD.** Consequences:

- **The literal "difference frequency" ω_hi − ω_lo (m+n = 0, even) is STRUCTURALLY FORBIDDEN**
  below yield — it would require an even (χ²) term the kernel does not have. (Pilot: the
  ω_hi−ω_lo bin sits **5×10⁹ below** the allowed product — at the numerical floor.)
- **The four-photon in-band product that DOES carry the form factor is the FWM sideband
  `ω_out = 2·ω_lo − ω_hi` (m+n = 1, odd)** — amplitude ∝ A_lo²·A_hi. This is the measured channel.

This SHARPENS (does not contradict) the FORK-A framing: the FORK-A note's "difference-frequency"
naming is loose; the substrate-native four-photon channel below yield is `2ω_lo − ω_hi`, and
`ω_hi − ω_lo` is retained as a **structural-null control** (a witness of inversion symmetry /
proximity-to-rupture — a nonzero reading there means an even-order leak or that yield/rectification
has been touched). Flag-don't-fix: surfaced to the orchestrator; the run measures both.

### 0.1 pre-test-physics-check — the one plumber-physical question (surfaced, run proceeds)

Grant already ruled "run it," so this does not gate the run; it is surfaced per the skill and
recorded here (bench-framed per the v1.2 translation gate):

> *A symmetric varactor bridge (odd C–V curve) driven at f₁ and f₂ puts out the 2f₁−f₂
> intermod but NOT the difference tone f₁−f₂ — the difference tone needs a DC-biased
> (asymmetric) junction. The reversible sub-yield vacuum is a symmetric varactor. So the
> four-photon form factor lives on the odd-allowed 2ω_lo−ω_hi sideband, and ω_hi−ω_lo is a
> structural null. Is the physically interesting channel the odd-allowed sideband (what this
> run measures), or does the corpus expect a DC-biased/asymmetric vacuum operating point
> (background field / gravity grade / near-yield bias) that would open the true difference
> channel?*

The reversible-medium answer (odd-allowed sideband) is what a sub-yield lossless kernel gives
and is what this 1D mechanism probe measures; the biased-junction reading is a distinct
above-yield / operating-point regime (out of scope, §11). No corpus doc settles a preference;
the run measures the reversible channel and records the null control.

---

## 1. Fork record — FOUR branches, NO preferred outcome (Grant standing ruling)

The Letter v5 (clm-gg4wmx, closure-above-ω₀ named-open-item) needs **none** of these branches
to land — v5 pre-registered exactly this open-item situation and adopted EFT-domain scoping.
**No branch is preferred; the frozen gates decide; whatever lands is recorded as fork-record
research-tier and does NOT edit the Letter or KB from this run** (§10).

| # | Branch | Signature (on the overlap-corrected beat power vs tone frequency) | Reading |
|---|---|---|---|
| **(i)** | **DRIVE-TRACKING** | `P_beat / O²` ≈ **flat** in ω̄ once the skin-overlap factor O (§6) is divided out — the four-photon vertex is **frequency-blind** at the node | χ³ alive above band → enhancement survives → **ATLAS tension real** |
| **(ii)** | **PARTICIPATION-SUPPRESSED** | `P_beat / O²` **falls steeply** beyond skin overlap (~(ω₀/ω)⁴-per-leg-pair class) — the capacitor **starves** above resonance | hard closure → **EVADES** |
| **(iii)** | **INTERMEDIATE power law** | `P_beat / O²` ∝ (ω̄)^(−q), q finite and non-trivial | the measured exponent **q IS the form factor** — report it |
| **(iv)** | **NULL** | no `2ω_lo−ω_hi` beat above the noise floor at any sub-yield drive amplitude | exponential-or-stronger closure **BOUND** at this platform's sensitivity (also an answer) |

**Adjudication is the substrate's, not fiat.** Branch is read from the frozen fit (§9) over the
frozen window; INDETERMINATE if the gates (§8) fail.

---

## 2. Platform scoping (STATE EXPLICITLY — do not conflate the two lattices)

**THIS RUN IS THE 1D MECHANISM PROBE.** The platform is the **1D K4 bond-line reduction** (the
same chain as the x29 driver): a single bond-line of saturable-varactor bonds, integrated in
continuous time. Its own linear acoustic band is `ω(k) = 2|sin(kℓ/2)|`, **band top ω_top = 2.0
ω_C** (Laplacian λ_max = 4). **"Above-band" here means above 2.0 ω_C** — this is the 1D chain's
dispersion, **NOT** the 3D srs values.

**The 3D FOLLOW-ON (recorded, NOT run here):** the 3D srs (diamond-cubic K4, I4₁32) band top is
**π√3 ω_C ≈ 5.441 ω_C** (`research/2026-07-09_srs-band-survey_result.md`, #604), with a
stiffness-lifted reading bracketing up to ≈17.01 ω_C (#607 review). The 3D FORK-A tone
recommendation is **(ω_a, ω_b) = (18.51, 17.51) ω_C, Δ = 1.0** — confirmed safe under all three
maps and both bracket endpoints (#607). That placement is for the eventual **3D** run on the
band-survey platform; **this 1D run does not use it and makes no 3D claim.** The 1D result is a
mechanism/form-factor probe; whether the 3D srs kills or preserves the same form factor is a
separate burden (cf. x29 result §8.1: reviving 3D behavior carries an explicit demonstration burden).

**Anti-loophole:** this is not a new firewalled engine — it is a driven-wave sim in the existing
`vol_1_foundations` dispersion/transport lane, extending the x29 driver (Rule 14).

---

## 3. Substrate-first sector header (before any standard-physics term)

- **SECTOR:** the V-sector / ε charge-length AC oscillation on a K4 bond-line. Node scalar
  `V_n` = the photon carrier (AC content of the T2/charge-length sector). 1D transport along
  one bond-line. Charge = DC winding; photon = AC content (framing note §2).
- **REGIME:** cold-to-kernel-engaged, **SUB-YIELD (reversible)**. Bond strain `r_n = V_{n+1}−V_n`;
  yield |r|=1 ⇒ rupture/pair-production = **OUT OF SCOPE** (§11). Runs touching yield are aborted+flagged.
- **NONLIN:** canonical Op2/Op14 saturable varactor. Kernel `S(r)=√(1−r²)`
  (`universal_operators.py:75`, Axiom 4 / Born–Infeld n=2). DEFAULT force `F(r)=r/S` from
  `U(r)=1−S` (conservative Born–Infeld n=2 casting — TAGGED, NOT the Op14 ε-load `F=r/√S`;
  x29 finding #5). The r/√S casting is run as a cross-check. **Both are ODD in r** (the parity
  theorem, §5, holds for both castings).
- **READOUT:** real-space energy flux + temporal DFT spectrum of what propagates. Drive =
  temporal ω tones at a real-space node; read = real-space. A46-clean (§4.4).
- **ALIASING:** spatial-lattice evanescence is PHYSICAL (ℓ_node fixed); the time integrator is
  continuous-time (dt = accuracy knob, decoupled from the lattice), temporal aliasing VERIFIED
  absent by the dt-halving gate (§8e). Symplectic velocity-Verlet; driven-damped energy budget
  closes to ≤1e-5 (§8e).
- **CLASS:** the frequency form factor is **EMERGENCE-class** (Class D) on the 1D model substrate;
  the A⁶ amplitude law and the parity null are **MANIFESTATION-class** (Class B). See §10.

---

## 4. Substrate-native-check walk (BEFORE the driver)

### 4.1 K4 checkpoint — the lattice IS physical
Node pitch ℓ_node = ℏ/(m_e c) is FIXED (`constants.py:282`, native ℓ=1). The band top ω_top=2.0
is a physical consequence of the bond stencil, **not a numerical knob**. Above ω_top there is no
propagating linear mode ⇒ evanescent response (the entry-skin, Gate 1). This is Axiom-1 discreteness.

### 4.2 Op2/Op14 checkpoint — the nonlinearity is a boundary/reactance kernel (no bulk energy term)
The bond is a saturable reactance carrying `S(r)=√(1−r²)`. The constitutive law is conservative,
from a potential (Ax3-lossless), matched so the symplectic integrator conserves an exact H.
`C_eff = C·S` (`universal_operators.py:789`, `Z_eff=Z_0/√S`): capacitance falls with strain ⇒
**local stiffening** ⇒ **HARD** nonlinearity ⇒ self-localized modes sit ABOVE the linear band.
**No φ⁴ minted** — the √(1−r²) IS the Axiom-4 kernel. The leading nonlinearity is CUBIC (§5.1).

### 4.3 Anisotropy is NOT measured (flag)
The (qℓ)⁴ cubic-harmonic anisotropy is 3D/directional k-space content; this 1D transport test
does not probe it. Do not read a form-factor exponent as anisotropy content or vice-versa.

### 4.4 Phase-space vs real-space (A46, phase-space-coordinate-check)
Both tones are **temporal** ω drives at a real-space node; the read is **real-space energy flux +
its temporal ω-content**. Drive and read are in the SAME coordinate frame ⇒ A46-clean. Every
frozen prediction (skin depths κ, overlap factor O, A⁶ scaling, parity null) is real-space/real-
time. We do NOT compare a real-space measurement to a phase-space φ² prediction (A46-disqualified
pattern avoided). DISTINCT from the winding-aliasing prereg (2026-06-08, Clifford-torus phase space).

---

## 5. THE PHYSICS — perturbative bookkeeping of the saturable kernel (FROZEN)

### 5.1 The leading nonlinearity is CUBIC (χ³ = four-photon)
Expand the default force about small strain:

    F(r) = r·(1 − r²)^(−1/2) = r + (1/2)·r³ + (3/8)·r⁵ + …      [r/S  casting; cubic coeff = 1/2]
    F(r) = r·(1 − r²)^(−1/4) = r + (1/4)·r³ + …                 [r/√S casting; cubic coeff = 1/4]

Only **ODD** powers appear (F is odd). The **cubic term is the χ³ four-photon vertex.** The two
castings differ only in the vertex coefficient (½ vs ¼): the FWM field amplitude ratio (r/S : r/√S)
= 2:1, the beat-POWER ratio = 4:1, but the **scaling exponents are identical** (cross-check §9).

### 5.2 The parity theorem (rigorous — forbids the difference frequency)
Under V → −V the equation of motion `V̈_n = F(r_n) − F(r_{n−1})` maps to −(itself) because F is
odd; the damping term −damp·Vd is also odd. Hence the response is an **odd functional of the drive**:
`V[−D] = −V[D]`, so its Volterra expansion contains only ODD orders D¹, D³, D⁵, …. Each order
D^(2k+1) produces frequencies that are a sum of an ODD number of {±ω_lo, ±ω_hi}. A line at
`m·ω_lo + n·ω_hi` requires |m| factors of ω_lo and |n| of ω_hi ⇒ total factor count ≥ |m|+|n|
with the same parity as m+n. **Therefore a line at `m·ω_lo + n·ω_hi` appears only when m+n is ODD.**

| product | (m, n) | m+n | allowed? | frequency (pilot pair 2.6, 4.2) |
|---|---|---|---|---|
| ω_hi − ω_lo (difference) | (−1, +1) | 0 (even) | **FORBIDDEN** | 1.6 (would-be in-band) |
| DC / rectification | (0, 0) | 0 (even) | **FORBIDDEN** | 0 |
| **2·ω_lo − ω_hi (FWM sideband)** | **(+2, −1)** | **1 (odd)** | **ALLOWED** | **1.0 (in-band, MEASURED)** |
| 2·ω_hi − ω_lo (upper sideband) | (−1, +2) | 1 (odd) | allowed | 5.8 (above band, evanescent) |
| 3·ω_lo − 2·ω_hi | (+3, −2) | 1 (odd) | allowed (χ⁵) | 0.4 (in-band, weaker) |

**Pilot confirmation (scratchpad, uncommitted):** for (ω_lo,ω_hi)=(2.6,4.2), A=0.15, read 70
nodes past the interior drive: P(2ω_lo−ω_hi=1.0) = 4.43×10¹, P(ω_hi−ω_lo=1.6) = 8.9×10⁻⁹
(**floor**), ratio 5.0×10⁹. The difference frequency is dead; the FWM sideband carries the signal.

### 5.3 The measured channel and its amplitude law (FROZEN)
**Measured beat product:** `ω_out = 2·ω_lo − ω_hi`, a FWM sideband folded into the propagating band.
Its field amplitude, to leading order, is

    Ṽ(ω_out) ∝ (cubic coeff) · A_lo² · A_hi · O(ω_lo, ω_hi) · G(ω_out)

where A_lo, A_hi are the drive amplitudes, O the skin-overlap factor (§6), and G(ω_out) the O(1)
Green's-function transfer of the near-drive source into the in-band propagating mode (constant
across the sweep because ω_out is held FIXED — §6). With **equal drive amplitudes A_lo=A_hi=A**:

    beat FIELD amplitude ∝ A³           (amplitude exponent = 3)
    beat POWER  P_beat = |Ṽ(ω_out)|² ∝ A⁶   (POWER exponent = 6)   ← the frozen "A⁶" prediction
    (equivalently P_beat ∝ P_drive³ — cubic in input power, the χ³ / four-wave-mixing signature)

**Linear-control corollary (Gate d):** kernel OFF (or A→0), the cubic vanishes ⇒ P_beat → 0
following the A⁶ law down to the numerical floor (NOT to a plateau). A plateau = spectral-leak
or numerical floor, characterized by the kernel-OFF run (§8b/§8d).

---

## 6. Analytic expectations — FROZEN NUMBERS (ave-prereg v1.6 required section)

### 6.1 Per-tone skin depths (from cosh κ = ω²/2 − 1; k → π + iκ)
Exact for the 1D chain. `κ(ω) = arccosh(ω²/2 − 1)`. Skin depth = 1/κ nodes.

### 6.2 The primary form-factor sweep — hold ω_out = 2ω_lo − ω_hi FIXED at 1.0 (in-band)
ω_out = 1.0 sits well inside the band (k = π/3, group velocity v_g = cos(π/6) = 0.866 c — clean
propagation, away from the v_g→0 edge). Holding ω_out fixed makes `P_beat = |Ṽ_{n_read}(ω_out)|²`
directly comparable across the sweep (identical group velocity, identical reader sensitivity).
Sweep the carrier ω̄ = (ω_lo+ω_hi)/2 up; δ = (ω̄−ω_out)/3, ω_lo=ω̄−δ, ω_hi=ω̄+δ (both > 2.0).

**Skin-overlap factor** (the FWM source needs A_lo²·A_hi ⇒ the combination 2κ_lo + κ_hi):

    O(ω_lo, ω_hi) ≡ exp[ −(2·κ_lo + κ_hi) ]     (node-1 leading term; full source = geometric sum, O(1)× this)

| ω̄ | (ω_lo, ω_hi) | κ_lo | κ_hi | 2κ_lo+κ_hi | O | O² |
|---|---|---|---|---|---|---|
| 2.8 | (2.20, 3.40) | 0.8871 | 2.2465 | 4.0207 | 1.794e-2 | 3.218e-4 |
| 3.1 | (2.40, 3.80) | 1.2447 | 2.5144 | 5.0038 | 6.712e-3 | 4.505e-5 |
| 3.4 | (2.60, 4.20) | 1.5129 | 2.7457 | 5.7714 | 3.115e-3 | 9.705e-6 |
| 3.7 | (2.80, 4.60) | 1.7340 | 2.9501 | 6.4181 | 1.632e-3 | 2.662e-6 |
| 4.0 | (3.00, 5.00) | 1.9248 | 3.1336 | 6.9833 | 9.272e-4 | 8.598e-7 |

**Branch predictions on the RAW P_beat (fixed drive amplitude) across this sweep:**
- Branch (i) DRIVE-TRACKING: raw P_beat tracks **O²** (falls ~374× from ω̄=2.8 to 4.0), so
  `P_beat / O²` is **flat** (vertex frequency-blind).
- Branch (ii) PARTICIPATION-SUPPRESSED: raw P_beat falls **faster than O²**; `P_beat / O²`
  falls with a steep exponent (~(ω̄)^(−q), q ≳ 4).
- Branch (iii): `P_beat / O²` ∝ (ω̄)^(−q), q intermediate — report q.
- Branch (iv): raw P_beat at the numerical floor at all ω̄.

### 6.3 The parity-null control (frozen prediction)
At every pair, the ω_hi − ω_lo bin (and the DC bin) must read at the numerical floor
(P ≲ 10⁻⁸ · P(ω_out), pilot-anchored). A reading above ~10⁻³ · P(ω_out) ⇒ even-order leak or
yield/rectification touched ⇒ flag (do not fit).

### 6.4 Absolute normalization — NOT frozen (honest)
The exact absolute beat amplitude requires the full evanescent-profile × Green's-function
integral; it is a **measurement output**, not a frozen prediction. The FROZEN, checkable
predictions are the **exponents** (amplitude 3 / power 6), the **overlap scaling** (O² table),
the **parity null**, and the **casting ratio** (½:¼ vertex). Order-of-magnitude reference at the
sweep-center pair (2.6,4.2), A=0.2, r/S: source ~ ½·A_lo²·A_hi·O ~ ½·(0.2)²(0.2)(3.1e-3) ~ 1.2e-5.

---

## 7. Tone choices (FROZEN)

- **Primary form-factor sweep (§6.2):** 5 pairs {(2.2,3.4),(2.4,3.8),(2.6,4.2),(2.8,4.6),(3.0,5.0)}
  at fixed ω_out = 1.0, **fixed drive amplitude A = 0.15** (kernel-engaged, sub-yield; pilot
  max_bond_r < 0.5). Justification: both tones above the 1D top 2.0 throughout; skin depths
  (§6.2) leave measurable first-node amplitude (κ ≤ 3.13 ⇒ node-1 amplitude ≥ e⁻³·¹ ≈ 4% of drive);
  the FWM product stays in-band and at fixed frequency for clean comparison.
- **Amplitude sweep (the A⁶ gate) at ONE fixed pair (2.6, 4.2):** A ∈ {0.015, 0.03, 0.06, 0.12,
  0.24} — 5 log-spaced (factor 2) sub-yield amplitudes (pilot: A=0.24 → max_bond_r 0.55; A=0.30 →
  0.69, both sub-yield with margin). The 0.015 point is the floor-probe (Gate d). ≥4-point log
  lever arm (8× amplitude ⇒ 2.6×10⁵ in power if slope 6).
- **Difference-of-Δ tone-geometry FLAG:** a **fixed-Δ** sweep (the FORK-A note's "Δ≈0.4") does NOT
  keep an in-band FWM product (2ω_lo−ω_hi = ω_lo − Δ rises out of band as the pair moves up). The
  **fixed-ω_out** family (§6.2) is used instead — the substrate-native design forced by §5. Recorded.

---

## 8. Gates (dead-actuator + driver-honesty; all BINDING)

| Gate | Condition | Method |
|---|---|---|
| **(a) M7 per-tone injection nonzero, ∝ drive²** | each tone establishes a real, nonzero skin amplitude that scales with A (NOT a no-op — the x29 sin(πn) class) | measure node-1 spectral amplitude at ω_lo, ω_hi; confirm ≈ A·e^(−κ) and ∝ A across two amplitudes |
| **(b) Validate-on-known (reader calibration)** | plant a weak REAL in-band linear tone at ω_out directly (no kernel needed); the flux reader recovers the expected outgoing flux | drive a small ω_out tone linearly; confirm net ⟨J⟩ at n_read and |Ṽ(ω_out)|² are consistent with the injected amplitude and known v_g |
| **(c) Ramp-independence (MANDATORY — the x29 transient killer)** | the steady-window beat power is stable under **ramp-duration doubling** | run every measurement at ramp_periods R and 2R; require \|P_beat(2R)−P_beat(R)\|/P_beat(R) < 0.05. Beat read ONLY in a steady window after ramp completes AND the beat has filled the readout region |
| **(d) Linear control (A→0)** | beat → 0 following the A⁶ law down to the floor, NOT to a plateau; kernel-OFF ⇒ ω_out bin at floor | fit the amplitude sweep (§9); confirm the smallest points track slope 6 until they reach the kernel-OFF floor; report the floor |
| **(e) Energy + dt convergence** | driven-damped energy **budget** closes: \|H(t) + ∫P_sponge − ∫P_drive\|/E_scale ≤ 1e-5; beat power changes < 5% under dt → dt/2 | budget ledger over the run; dt-halving on the reference pair |

**Verdict is INDETERMINATE if (c) or (e) fails** (transient/numerical artifact suspected), or if
the fit (§9) cannot separate flat from a power law. **Gate (a) failing ⇒ INVALID (no-op drive).**

---

## 9. Measurement + FROZEN fit window

- **Geometry:** interior drive at node `n_drive = N/2`; matched absorbing sponges at BOTH ends
  (Rule-10 PML-exclusion — sponge cells excluded from all reads). In-band beat radiates BOTH
  directions; read **rightward** flux at `n_drive + n_read` and **leftward** at `n_drive − n_read`
  (equal magnitude, opposite sign by reflection symmetry). `n_read` chosen past the evanescent
  skin (tones spatially filtered: at n_read the tone amplitude ≤ e^(−κ·n_read) ≪ beat).
- **Beat power proxy:** `P_beat = |Ṽ_{n_read}(ω_out)|²` from a Hann-windowed DFT over the steady
  window, cross-validated by the net time-averaged energy flux ⟨J_n⟩ = ⟨−F(r_n)·Vd_{n+1}⟩ (only
  in-band content carries net flux; evanescent tones are reactive) and calibrated to physical flux
  by Gate (b).
- **Steady window:** [t_settle, t_end], t_settle = ramp_time + n_read/v_g + margin; t_end = tmax.
- **Birth-depth profile:** |Ṽ_n(ω_out)| vs distance from the drive; **birth depth** ≡ the node at
  which it first reaches 90% of its propagating plateau (edge ≈ skin depth ⇒ born at edge; large ⇒
  born in bulk). Secondary discriminator between pictures (i)/(ii).
- **FROZEN fit windows (no post-hoc cherry-pick — the x29 window lesson):**
  - **Frequency form factor:** fit `log(P_beat/O²)` vs `log(ω̄)` over **ALL 5 sweep pairs**
    that pass Gates (a,c,e) and read ≥ 10× the parity-null floor. Slope = −q (the form-factor
    exponent). Also report the flatness test: is the slope consistent with 0 (branch i) within
    the sweep-point scatter? Report R² for both flat and power-law.
  - **Amplitude exponent:** fit `log(P_beat)` vs `log(A)` over the amplitude-sweep points that read
    ≥ 10× the kernel-OFF floor (excludes floor-limited points; the 0.015 point is expected floor-
    limited and is the Gate-d witness). Predicted slope = 6.

### 9.1 FROZEN numeric branch thresholds (decision rule)
Let `q = −slope[ log₁₀(P_beat/O²) vs log₁₀(ω̄) ]` (the overlap-corrected form-factor exponent),
fit over the frozen window (pairs sub-yield AND reading ≥ `FLOOR_SNR × parity-null floor`), with
`FLOOR_SNR = 10`. Then:

- **INVALID** if Gate (a) M7 fails (drive no-op / non-∝-A).
- **INDETERMINATE** if Gate (c) ramp or Gate (e) dt/energy fails.
- **(iv) NULL** if < 2 pairs clear `FLOOR_SNR × floor` (no measurable beat).
- **(i) DRIVE-TRACKING** if `|q| < Q_FLAT = 1.0` (overlap-corrected power flat within one decade/decade).
- **(ii) PARTICIPATION-SUPPRESSED** if `q ≥ Q_STEEP = 4.0` (steep suppression beyond overlap).
- **(iii) INTERMEDIATE** if `1.0 ≤ q < 4.0` — report q as the form factor.

Cross-checks reported (not gating the branch): the amplitude exponent (predict 6.0 ± scatter; a
gross mismatch flags a non-χ³ mechanism), the parity-null (`P(ω_hi−ω_lo) < 10⁻³·P_beat` at every
pair), and the r/√S casting (same q within scatter; power prefactor ≈ ¼× the r/S run per §5.1).

---

## 10. Consistency-vs-emergence classification (FROZEN)

| Sub-claim | Class | Rationale |
|---|---|---|
| ω_C = c/ℓ_node band scale; ω_out=1.0, ω_top=2.0 native | **A — Identity** | native units; ℓ_node := ℏ/(m_e c) forces it (`constants.py:282`). |
| Acoustic band + above-band evanescence (entry skin) | **B — Manifestation** | Axiom-1 discreteness + bond stencil; standard discrete-lattice fact, substrate-grounded. |
| Parity null (ω_hi−ω_lo forbidden); A⁶ amplitude law | **B — Manifestation** | direct consequences of the odd (χ³) Axiom-4 kernel; predictable a priori (§5). |
| **The FREQUENCY form-factor exponent q → branch (i)/(ii)/(iii)** | **D — Emergence** | computed from the substrate's own nonlinear dynamics; does NOT use any CODATA/target as input; the actual OPEN measurement. **On the 1D MODEL substrate** (mechanism probe, not 3D). |

**Headline:** this is an **EMERGENCE-class (Class D) measurement of the four-photon form factor on
the 1D model substrate** (mechanism probe). Honest caveat: the ABSOLUTE scale is identity; the A⁶
law and parity null are manifestations; only the frequency exponent is emergent. Feeds the
closure-above-ω₀ open item (Letter v5, clm-gg4wmx). **NO Letter/KB edits from this run**
(research-tier; propagation is a follow-on after adversarial review). No CODATA substitution;
forward simulation only; every gate computed, not asserted; canonical kernel imported by symbol.

---

## 11. Out of scope
- Above-yield rupture / pair-production (AC→DC rectification — the EVEN nonlinearity that WOULD
  open the ω_hi−ω_lo difference channel). Runs touching yield are aborted+flagged+excluded.
- A DC-biased / asymmetric vacuum operating point (§0.1) — a distinct regime that would open the
  difference channel; not this reversible-medium probe.
- The 3D srs run at (18.51, 17.51) ω_C (§2) — the follow-on placement, recorded not run.
- The μ-slew kernel S_B=√(1−A_I²) as a second nonlinearity (x29 KEEP-BOTH follow-on).
- The full FWM matrix element / phase-matching integral (theory, not this driver).
- Anisotropy / (qℓ)⁴ (owned by k4-bloch-dispersion).

---

**PREREG STATUS: FROZEN — 2026-07-09.** Driver + result are separate commits. The branch verdict
is whatever the frozen gates + fit return; all four branches recorded regardless. The parity
theorem (§5) and the fixed-ω_out design (§6.2) are the substrate-native corrections forced by the
bookkeeping and are frozen here BEFORE the production driver.
