# Dark-Sector Response Characterization — the quantitative layer (research-doc DRAFT)

> **Status: research-doc DRAFT — NOT canon. Auditor/Grant-gated.** This doc is the
> **quantitative datasheet layer** under two vocabulary/structure assets that already exist:
> the **field-symbol-registry** (`research/2026-06-10_field-symbol-registry.md`, the names) and the
> **Vol-9 datasheet** ch5 AC + ch7 saturation + ch14 phase-diagram chapters (the format). Where the
> registry says *what a symbol is* and Vol-9 says *which datasheet row it lives in*, this doc supplies
> the **curves and the numbers** — characterized the way an engineer reads a datasheet: a slew spec
> like an op-amp, an impedance like a transmission line, the speeds like derating curves — **adapted**
> where the substrate needs new columns (per-channel; the sector-resolved realization classes
> SYM / μ-only / ε-only; regime tags per the Vol-9 ch14 / four-regimes phase diagram).
>
> **Every curve derives from `src/ave/core/constants.py` primitives ONLY**, via scripts in the repo
> (`src/scripts/vol_9_vacuum_datasheet/`), figures with data-derived captions
> (`research/figures/2026-06-11-dark-sector-response/`). No numeric constant is hard-coded.
>
> **Discipline tags applied:** `ave-canonical-source` (constants imported, cross-checked, never
> hard-coded); `ave-live-fire-derivation-provenance` (every curve RUN, dead-input + forward-vs-fit
> checked; coefficients chosen to land somewhere are tagged FITTED); `verify-before-cite` (every
> file:line grep-verified this session against `AVE-Core @ origin/main f6ffd98d`; the α-slew 2π
> notational slip is surfaced §1.4, **not** silently reconciled); `consistency-vs-emergence` (each row
> class-tagged); `substrate-native-check` (CP10 saturation rendered as a Γ boundary, not a bulk force);
> `flag-don't-fix` (the ε-vs-C exponent tension §2.1, the c_EM-rises imaging question §3.3, the **c_bulk
> floor-value candidate/CONTESTED** §3.1, the **√3/2 spin-2-vs-scalar sector scope** §1.2/§1.3, and the
> **SYM first-order-null + second-order-residual** echo qualifier §2.3 are surfaced for Grant/auditor,
> not resolved ad hoc); `phase-space-coordinate-check` (sector/channel discipline on the √3/2 boundary);
> Rule 12.

## Class-tag legend (per row / per curve)

| Tag | Meaning |
|---|---|
| **canonical** | the form is already canon (cited leaf:line); this doc only renders it |
| **derived-this-arc** | forward-derived this session from canonical primitives; the algebra is new, the inputs are canonical |
| **candidate** | a profile/edge with no canonical source; tagged engineering-convention, used only to draw a curve |
| **engineering-convention** | an external/datasheet choice (band edges, generic A²(r) forms) — not substrate-derived |

## Canonical primitives consumed (all `src/ave/core/constants.py`)

| Symbol | Value | constants.py |
|---|---|---|
| `C_0` | 299 792 458 m/s | :95 |
| `Z_0` | 376.730 Ω | :98 |
| `ALPHA` | 7.2973525693e-3 (1/137.036) | :133 |
| `L_NODE` = ℏ/(m_e c) | 3.86159e-13 m | :239 |
| `V_SNAP` = m_e c²/e | 510.999 kV | :400 |
| `V_YIELD` = √α·V_snap | 43.6519 kV | :409 |
| `PHI` | 1.6180339887 | :199 |
| `RHO_CAV` = −1/φ **(floor-value candidate/CONTESTED)** | −0.6180339887 | `cavitation_flow.py:64` (NOT constants.py — registry R8); floor-VALUE flagged CANDIDATE `cavitation_flow.py:62`, registry §3.10 |

Derived (this doc, forward): `omega_node = c0/ell_node`, `nu_node = omega_node/2π`,
`tau0 = ell_node/c0`, `SR_max = V_yield·omega_node`, `S(A)=√(1−A²)`.

---

## §1 — THE SLEW SPEC (large-signal rate limit, op-amp datasheet style)

**Driver:** `src/scripts/vol_9_vacuum_datasheet/slew_spec_band_comparison.py`
→ `research/figures/2026-06-11-dark-sector-response/fig1_slew_band_comparison.png`,
`fig1b_slew_compression.png`, `slew_compression_curve.csv`.

### §1.1 — The datasheet SR (THE spec) — class: derived-this-arc

An op-amp's slew rate is the **maximum** dV/dt the output can produce — (max swing)/(min slew
time). The lattice has both: the max localized swing is `V_yield` (the Axiom-2/4 yield voltage,
above which the topology ruptures), and the min slew time is one **voxel tick** `τ0 = ℓ_node/c0`
(one signal-crossing of one cell — Grant's gear tooth advancing once,
`substrate-temporal-values-definition.md:12-18`). Hence

$$\boxed{\;SR_{max} \;=\; V_{yield}\cdot \omega_{node}, \qquad \omega_{node}=\frac{c_0}{\ell_{node}}\;}$$

| Quantity | Forward value | Provenance |
|---|---|---|
| `ω_node = c0/ℓ_node` | **7.76344e20 rad/s** | = m_e c²/ℏ (Compton angular rate); Vol-9 ch5 AC index calls it `ω_C` |
| `ν_node = ω_node/2π` | **1.23559e20 Hz** | substrate **Nyquist ceiling** (Vol-9 ch5 AC index) |
| `τ0 = ℓ_node/c0` | 1.28809e-21 s | voxel tick = electron Compton time (`tau-relax-derivation.md:11`) |
| **`SR_max = V_yield·ω_node`** | **3.38889e25 V/s** | **THE DATASHEET SR** |

This is THE datasheet SR. The number is enormous because the lattice tick is the Compton time:
the vacuum can slew a full 43.65 kV node-swing in ~1.3 zeptoseconds.

### §1.2 — Conditions column (op-amp datasheet format)

| Condition | Value / statement |
|---|---|
| Drive sector | bond-LC longitudinal-V (the channel `V_yield` lives in) |
| Operating temperature | cold-lattice `A=0` (the `SR_max` quoted is the unstrained ceiling) |
| Small-signal ↔ large-signal boundary | `A = √(2α) ≈ 0.1208` (regime I→II, **universal**, `four-regimes.md:26,33`) |
| Large-signal validity | `√(2α) ≤ A < 1`; Axiom-4 kernel active. **Sector caveat:** the four-regime II/III split at `√3/2` is the **spin-2** map (`four-regimes.md:52`); this slew channel is **scalar** (bond-LC longitudinal-V, ℓ_min=0) and has **no avalanche-onset sub-boundary** (`four-regimes.md:48`) — its only intrinsic large-signal boundary is rupture at `V_yield`. |
| Rupture (absolute-max) = scalar onset | `A = 1` (`V = V_yield`), S→0, topology destroyed; the **scalar-channel** avalanche onset (`four-regimes.md:48,56`) |
| Load | per-node bond impedance `Z_0 = 376.73 Ω` (the slew sources into the lattice line) |

### §1.3 — Onset / compression near the limit — class: derived-this-arc (from canonical kernel)

The compression behaviour is **read off the canonical varactor kernel, not invented**. The bond is a
vacuum varactor `C_eff(V) = C0/√(1−(V/V_yield)²)` (`parametric-coupling-kernel.md:48`; small-signal
form `ε_eff = ε0·√(1−r²)`, `constants.py:465`). An op-amp's slew is `SR = I_max/C`; as the operating
amplitude rises the varactor stiffens (`C_eff` grows), so for a fixed charge-delivery current the
achievable slew **compresses**:

$$SR(A) = SR_{max}\cdot S(A), \qquad S(A)=\sqrt{1-A^2},\quad A=V/V_{yield}.$$

The slew **freezes to zero at the rupture wall** `A→1` — the gear seizes. This is the same `S(A)→0`
freeze that stops the local clock (`op14-cosmic-horizon-profile.md:22`), seen from the rate side.
Curve in `fig1b_slew_compression.png` / `slew_compression_curve.csv`.

> **🚩 sector-scope (phase-space-coordinate-check / registry Rule 3):** of the canonical four-regime
> boundaries, only `√(2α)` (regime I→II, **universal** small-signal limit, `four-regimes.md:33`) and
> `A=1` (rupture, the **scalar-channel** onset = `V_yield`, `four-regimes.md:48,56`) apply to this
> **scalar** (bond-LC longitudinal-V) slew curve. The **`√3/2` boundary is spin-2/shear-sector-specific**
> (`four-regimes.md:41,50`; the scalar sector ℓ_min=0 has **no** avalanche-onset boundary,
> `four-regimes.md:48`). It is drawn on `fig1b` as a **spin-2 reference line only**, explicitly **not** a
> boundary of the scalar slew curve. Mislabelling it "avalanche onset" on a scalar channel is the W5-adjacent
> sector overload; relabeled, not silently dropped.

> **Live-fire provenance (`ave-live-fire-derivation-provenance`):** `SR_max` is **forward** from
> `{V_yield, ℓ_node, c0}` — no target in the loop (there is no observed "lattice slew rate" to fit to).
> Dead-input check: the band-comparison verdict (§1.5) is invariant to the band edges to within ±3 OOM,
> so the "clean null" is not edge-tuned. No coefficient was chosen to land on a target — `SR(A)=SR_max·S(A)`
> inherits its single functional form (`S`) from the canonical kernel.

### §1.4 — The other candidate: the α-slew flywheel — class: canonical (with a flagged 2π slip)

The corpus already names a substrate rate it calls a **"slew"**: the **α-slew refresh rate**, the
Axiom-4 vacuum-varactor's intrinsic refresh at the Schwinger anomalous-moment kernel
(`parametric-coupling-kernel.md:9,29,52`; `dama-alpha-slew-derivation.md`). Its primitive is

$$\omega_{slew} = \alpha\,\omega_{node}\quad(\text{=}\;\alpha\,\omega_{Compton},\ \texttt{parametric-coupling-kernel.md:52}),\qquad \nu_{slew}=\frac{\omega_{slew}}{2\pi}=\alpha\,\nu_{node}=9.0165\times10^{17}\ \text{Hz}.$$

**This is NOT the datasheet SR.** It is the substrate's **small-signal reactive refresh** — the
per-cycle reactive leak (fraction `1/Q = α`) of the electron LC tank ringing below `V_yield`
(`theorem-3-1-q-factor.md`; `dama-alpha-slew-derivation.md:228-242`). In op-amp terms it is the
**gain-bandwidth / unity-gain frequency** (a small-signal, reactive figure), not the large-signal
slew limit. So:

| Candidate | Form | Datasheet role | Class |
|---|---|---|---|
| **`SR_max = V_yield·ω_node`** | 3.389e25 V/s | **THE slew rate** (large-signal dV/dt ceiling) | derived-this-arc |
| `ω_slew = α·ω_node` | 5.665e18 rad/s | small-signal reactive **refresh** (gain-bandwidth analog) | canonical |
| `ω_node = c0/ℓ_node` | 7.763e20 rad/s | substrate **Nyquist ceiling** (frequency ceiling) | canonical |

> **🚩 verify-before-cite FLAG (surfaced, not fixed):** `dama-alpha-slew-derivation.md:21` writes
> `ν_slew = (α/2π)·ν_Compton` but states the value `9.02×10¹⁷ Hz`. Numerically `(α/2π)·ν_Compton =
> 1.435×10¹⁷ Hz ≠ 9.02×10¹⁷ Hz`. The **stated number** matches `ν_slew = α·ν_node = ω_slew/2π` with
> `ω_slew = α·ω_node` (the `parametric-coupling-kernel.md:52` angular primitive, which is internally
> self-consistent). The `(α/2π)` written form carries a stray 2π (it reads `a_e = α/2π` applied to a
> frequency, then the ω→ν divide is dropped). I used the **angular primitive** `ω_slew = α·ω_node`.
> This is a canon coherence flag for the auditor — both leaves; not reframed.

> **Gaia DEMOTION (honest, per `dama-alpha-slew-derivation.md:8,118,132,142`):** the α-slew co-derives
> a substrate-equilibrium velocity `v_substrate = αc/2π = 348.2 km/s`. The **FLOOR** interpretation of
> this value was **tested and FALSIFIED** 2026-05-17: Toomre-stratified halo populations show |v_CMB|
> *increasing* with peculiar dispersion (not decoupling toward 348), and the globular-cluster
> population (N=165) clusters at median 564 km/s (Outcome III, cosmic-flow-dominated) — so the
> substrate-velocity prediction **does NOT extend to GC-class populations**; scope narrowed to LSR-class
> only (375 km/s observed, 9% above, gap attributed to cosmic-flow). The directional alignment (2.75°
> from the CMB dipole) survives as a **consistency** check, not a floor. I cite the α-slew rate as the
> reactive-refresh primitive; I do **not** import the demoted FLOOR magnitude as load-bearing.

### §1.5 — THE BAND COMPARISON (a clean-null column is a result) — class: engineering-convention edges

The datasheet question: at what frequency does the substrate run out of slew? Answer: the **frequency
ceiling** is `ν_node = 1.236e20 Hz` (the Nyquist ceiling — beyond it the lattice cannot represent a
faster oscillation). Compare against the astrophysical BH bands the BH-matrix cares about. **Scaling
chain (stated):** the bands are quoted **at the source frame** — LIGO ringdown is the final-BH QNM
frequency `f_QNM ≈ 0.37 c³/(2πGM)` (≈250 Hz at 60 M⊙; the 10–10⁴ Hz band spans ~few–10⁴ M⊙); EHT
variability is the SMBH light-crossing/ISCO timescale (M87*/Sgr A*, minutes–days); X-ray QPO is the
NS/BH-binary high-frequency QPO (up to ~1.25 kHz). Cosmological redshift only **lowers** observed
frequencies, so the source frame is the **conservative** (highest) comparison.

| Band | Source-frame range | `ν_node` sits | 
|---|---|---|
| LIGO ringdown (stellar–IM BH QNM) | 10 – 10⁴ Hz | **16.1 – 19.1 OOM above** |
| X-ray QPO (NS/BH binaries) | 0.1 – 1.25×10³ Hz | **17.0 – 21.1 OOM above** |
| EHT variability (SMBH M87*/Sgr A*) | 10⁻⁵ – 10⁻² Hz | **22.1 – 25.1 OOM above** |

**Result — CLEAN NULL COLUMN.** The lattice rate limit sits **≥16 orders of magnitude above every
astrophysical BH band**. The substrate is **never slew-limited** at any frequency LIGO, EHT, or X-ray
timing instruments observe: ringdowns, QPOs, and SMBH variability are, from the substrate's point of
view, DC. This is a *result*, not a non-result — it tells the BH matrix that **no observed BH
frequency row can be a substrate slew-rate effect**; any frequency structure must come from the
*geometry/impedance* of the saturated region (§2–§3), not from the lattice running out of rate.
Figure: `fig1_slew_band_comparison.png` (caption carries the OOM gaps, data-derived).

---

## §2 — THE Z_eff CURVES (transmission-line style)

**Driver:** `src/scripts/vol_9_vacuum_datasheet/zeff_realization_classes.py`
→ `fig2_zeff_echo_predictor.png`, `zeff_realization_classes.csv`,
`zeff_approach_profile.csv`, `echo_reflectivity.csv`.

A transmission line is characterized by `Z` vs operating point and by its
mismatch/reflectivity. The substrate's wall impedance is the canonical Op14
asymmetric-Meissner form (`operators.md:54`; `op14-cosmic-horizon-profile.md:82`):

$$Z_{eff} = Z_0\sqrt{\frac{S_\mu}{S_\varepsilon}}, \qquad S_x=\sqrt{1-A_x^2},\quad \varepsilon_{eff}=\varepsilon_0 S_\varepsilon,\ \mu_{eff}=\mu_0 S_\mu\ (\texttt{constants.py:465}).$$

### §2.1 — Z_eff(A²): the three realization classes — class: canonical (rendered)

This is the **sector-resolved wall canon** — the new datasheet column the substrate needs.
The realization class is *which sector(s) the load drives* (A-034 catalog SYM / ASYM-N(μ) / ASYM-N(ε),
`universal-saturation-kernel-catalog.md`; CLAUDE.md:60 symmetric-vs-asymmetric scope ruling):

| Class | Driven sector | Z_eff(A²) | Limit A²→1 | Canonical anchor |
|---|---|---|---|---|
| **SYM** | both (`S_μ=S_ε`) | `Z_0` (invariant) | `Z_0` — **reflectionless** (Γ=0) | CLAUDE.md:60; `achromatic-impedance-matching.md:28` |
| **μ-only** | magnetic / B-driven (`S_ε=1`) | `Z_0·(1−A²)^{1/4}` | **→ 0** (Γ→−1, Meissner) | `phase-transitions-impedance.md:24` |
| **ε-only** | static-E / capacitive (`S_μ=1`) | `Z_0·(1−A²)^{−1/4}` | **→ ∞** (vacuum mirror) | CLAUDE.md:60; `vacuum-impedance-mirror.md:58` |

Numbers (`zeff_realization_classes.csv`): at A²=0.99 → SYM 376.7 Ω, μ-only 119.1 Ω, ε-only 1191 Ω.
The SYM invariance is **why symmetric gravity is reflectionless** — a mass-soliton carrying internal
**E and B** loads both sectors equally, `Z` never changes, light passes (`achromatic-impedance-matching.md`).
The asymmetry is what makes a wall.

> **🚩 flag-don't-fix (ε-vs-C exponent tension):** the small-signal propagation form is `ε_eff = ε0·S`
> (`constants.py:465`, gives `c_EM = c0/S` rising — self-consistent, §3). But the **large-signal
> varactor** differential capacitance is `C_eff = C0/S` (`parametric-coupling-kernel.md:48`), i.e. `C`
> *rises* where `ε` *falls*. These are **different objects** (small-signal propagation `ε` vs
> large-signal bias-dependent differential `C`), but a naive reader will see `C ∝ ε` and read a sign
> contradiction. Surfaced for the registry's Rule-1 discipline; I use the propagation `ε_eff = ε0·S`
> for all Z/c curves (the load-bearing one for impedance + speed), and the varactor `C_eff` only for
> the §1 slew. Not silently merged.

### §2.2 — The approach profile Z_eff(r) — class: derived-this-arc (canonical exponent flagged)

Canon provides the **limit** (`A²(r)→1` at the Γ=−1 surface, `op14-cosmic-horizon-profile.md:20`) plus
the **Schwarzschild-tracking identity** (`c_shear = c0(1−A²)^{1/4} ≡ c0√(1−r_s/r)`, `temporal-values:29`;
`operators.md:56`) — but **no closed-form A²(r)**. The tracking identity forward-gives the profile:

$$(1-A^2)^{1/4}=\sqrt{1-r_s/r}\ \Rightarrow\ \boxed{\,S(A(r))=1-r_s/r\,}\ \Rightarrow\ A^2(r)=1-(1-r_s/r)^2.$$

Then `Z_eff(r)` follows per class: ε-only diverges, μ-only → 0, SYM flat, all at `r=r_s`
(`zeff_approach_profile.csv`; `fig2` middle panel).

> **🚩 flag-don't-fix (¼-vs-½ exponent):** `op14-cosmic-horizon-profile.md:22` writes the local clock
> as `ω_local = ω_global·√(1−A²)` (the **stale ½** single-speed exponent that `temporal-values:53`
> flags STALE at `op14-local-clock-modulation.md:17,31`). Under that convention `S(A(r))=√(1−r_s/r)`
> and `A²(r)=r_s/r`. The two give different profiles. I use the **post-split** `c_shear`-tracking form
> (`S=1−r_s/r`, authoritative `temporal-values:29`) and store both in the CSV. This is the **same**
> ¼-vs-½ tension `temporal-values §4` already flags, now surfacing in the approach profile — surfaced
> for the auditor, not resolved here.

### §2.3 — Reflectivity vs frequency: THE ECHO PREDICTOR — class: derived-this-arc (standard WKB)

The mismatch/reflectivity integral is **textbook transmission-line math**, cited as such (graded-line
Born/WKB reflection), NOT an AVE construct: the reflection per unit length is `r(x)=½ d(ln Z)/dx`, and
the total amplitude is

$$R(\Omega)=\int \tfrac12\frac{d\ln Z}{dx}\,e^{2i\int k\,dx'}\,dx,\qquad \Omega=\omega r_s/c_0,\ k=\omega/c_{shear}(x).$$

| Class | graded-region max `|R|` | max bounded `R_pow=|R|²` | Echo? |
|---|---|---|---|
| **SYM** | **2.9×10⁻¹⁵** (first-order Born floor: `d ln Z/dx ≡ 0` → floating-point zero) | ~0 | **NO to first order** (2nd-order residual below) |
| **μ-only** | 0.559 | 0.313 | **YES** |
| **ε-only** | 0.559 | 0.313 | **YES** |

Three results, all clean:
1. **SYM → zero echo to FIRST order** — the canonical `discrete-lattice-entropy-constant.md:59`
   result ("reflection set by the rate of change of Z; symmetric saturation → `dZ/dr=0` → no reflection
   *to first order*"). The script's `2.9×10⁻¹⁵` is the **first-order Born floating-point floor**
   (`d ln Z/dx` is identically 0 for SYM), **not** a converged true reflectivity.
   **🚩 second-order residual (carried, not dropped):** `discrete-lattice-entropy-constant.md:61` states a
   **non-zero second-order discrete reflection survives** when `n(r)` is non-linear across the bond
   (`d²n/dr² ≠ 0`), of order `|Γ|² ∼ (ℓ_node/r_sat)²` (`:65`). So SYM echo is **suppressed, not strictly
   absent** — the right claim is *first-order null + a small granularity-scale second-order residual*, not
   "0%". **Echoes remain a falsifiable signature of the *asymmetric* classes (`R_pow~0.31`, orders of
   magnitude above the SYM second-order residual); the discriminator is the echo *amplitude class*, not a
   strict present/absent.**
2. **μ-only and ε-only give the same `|R|` magnitude** — the impedance *step* has opposite sign
   (`Z→0` vs `Z→∞`) but the *log-gradient magnitude* `|½ d ln S/dx|` is identical, so the partial
   reflectivity is the same. The classes differ in sign, not echo strength.
3. **Low-frequency-weighted.** A graded transition is a high-pass *transmitter*: high-`Ω` waves see the
   gradient as adiabatic and pass; low-`Ω` waves reflect. So GW-echo power concentrates at the
   **low-frequency** end of any ringdown — the echo predictor for the BH matrix (`fig2` right panel).

The integral is restricted to the **graded approach region** `r ≥ 1.1 r_s` where the weak-reflection
(Born) approximation is self-consistent (`|R|<1`). At the wall itself the canonical **Γ=−1** perfect
reflector takes over (`R=1`, Op17-bounded) — rendered as a **boundary condition, not a bulk term**
(substrate-native-check CP10).

## §3 — THE DILATION CURVES (derating-curve style)

**Driver:** `src/scripts/vol_9_vacuum_datasheet/dilation_derating_curves.py`
→ `fig3_dilation_derating.png`, `three_speed_split.csv`, `bulk_speed_vs_rho.csv`,
`observed_frequency_transfer.csv`.

A datasheet derates a part vs operating point. The substrate derates **three speeds** — and the
**three-speed split IS the figure** (the load-bearing content is that they go three different ways).

### §3.1 — The three sector speeds — class: canonical forms (rendered); c_bulk **floor-value candidate/CONTESTED**

| Channel | Speed | Behavior at A²→1 | Canonical anchor |
|---|---|---|---|
| **EM-transverse** | `c_EM = c0(1−A²)^{−1/2}` | **RISES → ∞** (Maxwell phase / α-speed) | `substrate-temporal-values:28`; registry §3.1 |
| **shear (matter clock)** | `c_shear = c0(1−A²)^{+1/4}` | **FREEZES → 0** (group / rest-mass speed) | `substrate-temporal-values:29`; `operators.md:56` |
| **bulk (compressional)** | `c_bulk = c0√(1+ρ̄/(1−ρ̄²))` | **FREEZES at ρ̄_cav** (floor-VALUE **candidate/CONTESTED**); stiffens at ρ̄→+1 | form: `substrate-temporal-values:30`; floor: `cavitation_flow.py:64` (value), `:62` ("floor is CANDIDATE") |

`c_bulk(ρ̄_cav) = 0` at `ρ̄_cav = −1/φ = −0.618034` is the **defining root** of `c_bulk²=0` — an
**algebraic identity** (ρ̄_cav is *by construction* the root), **not an independent check**.

> **🚩 flag-don't-fix (c_bulk floor is CONTESTED, carried not resolved):** the c_bulk **form** is canonical
> (`substrate-temporal-values:30`), but the floor **VALUE** `ρ̄_cav=−1/φ` is **CANDIDATE/CONTESTED**, not
> canonical: `cavitation_flow.py:62` comment reads "floor is CANDIDATE" and `v5 prereg:74` says "cite as
> candidate, never canonical", vs a "Q2 resolved" reading at `substrate-temporal-values:61`. The
> field-symbol-registry this doc sits under flags exactly this (registry row `ρ̄_cav`, line 139 + §3.10:
> "floor-VALUE epistemic status CONTESTED … surfaced not resolved"). I render the freeze curve but tag the
> floor value **candidate**; I do **not** promote it to canonical. Routed to the auditor with the registry
> flag, not collapsed here.

Curves: `three_speed_split.csv` (c_EM, c_shear vs A²), `bulk_speed_vs_rho.csv` (c_bulk vs ρ̄). The bulk
speed is plotted on its **own** axis (ρ̄, density) because it rides a distinct strain variable from the
shear/EM amplitude A — whether `A` and `ρ̄` share a strain budget is the `temporal-values §5` residual
flag (OPEN; not assumed here).

### §3.2 — Observed-frequency transfer functions per channel — class: derived-this-arc

A signal emitted at proper frequency `ω_source` in a saturated region (operating point A²) arrives at
an unsaturated observer shifted by the local clock ratio of **that channel** (`temporal-values:40-42`):

| Channel | `H = ω_obs/ω_source` | At A²=0.9 | Physical |
|---|---|---|---|
| **shear** (spectral lines, GW) | `(1−A²)^{1/4}` | **×0.562** (redshift) | atomic transitions/GW run on the matter clock → standard gravitational **redshift** |
| **EM phase** | `(1−A²)^{−1/2}` | **×3.162** (blue) | the EM **phase** advances faster — the α-speed, not a proper matter clock |
| **bulk** | `√(1+ρ̄/(1−ρ̄²))` | (ρ̄-set) | compressional pilot frequency, freezes toward ρ̄_cav |

This is the **c_shear/Schwarzschild tracking made quantitative**: spectral-line redshift `= (1−A²)^{1/4}`
and, via the canonical identity `c_shear/c0 = (1−A²)^{1/4} ≡ √(1−r_s/r)` (`operators.md:56`,
verified `max|diff| = 0`), the redshift `= √(1−r_s/r)` — the GR result, recovered as the **matter-clock**
projection (consistency-class: the mechanism is substrate-native, the number is the GR weak-field redshift).

### §3.3 — The c_EM-rises consequence — 🚩 FLAGGED for the BH matrix, NOT resolved

The two channels carry **opposite-sign** frequency shifts from the same saturated region: spectral
lines (shear) **redshift** `×0.562`, but the EM **phase** speed **rises** `×3.162` (A²=0.9). The
matter-clock redshift is the one observed in spectral lines and is unambiguous. **What the rising EM
phase speed `c_EM = c0(1−A²)^{−1/2}` does to *imaging* — lensing geometry, the BH shadow size, photon-ring
structure — is a genuine open question.** A medium where the EM phase speed *rises* toward the wall is
the opposite of the usual `n>1` gravitational-lens picture, and I will **not** resolve it ad hoc:

> **Surfaced to the BH matrix (shadow/lensing row):** does the observed BH image track the **shear**
> matter clock (giving GR-like shadow/lensing), or does the rising `c_EM` impose an EM-phase-speed
> correction on the photon trajectories near saturation? The two channels diverge by `(1−A²)^{3/4}`
> at the operating point. This is a discriminator the BH matrix must adjudicate — `flag-don't-fix`,
> routed to §4, not collapsed here.

## §4 — BH-MATRIX HOOKS

These curves are the **quantitative substrate-response layer** the BH-modifier matrix reads off. A black
hole in AVE is a **melted / saturated lattice region** bounded by a Γ=−1 surface (H2 SUPPORTED,
`2026-06-10_pilotwake-bhphase-survey_note.md:0`; the horizon is the `A²→1` Γ=−1 saturation surface,
`op14-cosmic-horizon-profile.md:20,31`; `boundary-observables-m-q-j.md:21`). Each curve here is a
**substrate modifier** that sets a BH-matrix row. Per-modifier hooks:

| Modifier (this doc) | BH-matrix row it feeds | What it changes | Realization-class / regime gate |
|---|---|---|---|
| **§2.3 reflectivity curve** `|R(Ω)|` | **echoes** | sets echo amplitude + spectrum: GW-echo power = the graded-region partial reflectivity off the near-wall impedance gradient; **low-Ω-weighted** | **gated on class**: SYM → **first-order null** echo (`d ln Z/dx≡0`), with a small **second-order** granularity residual for non-linear `n(r)` (`|Γ|²∼(ℓ_node/r_sat)²`, `discrete-lattice-entropy-constant.md:61`); μ-only / ε-only → strong echo (`R_pow~0.31`). The discriminator is the echo **amplitude class** (asymmetric `R_pow~0.31` ≫ SYM second-order residual), **not** a strict present/absent. |
| **§1 slew spec** `SR_max`, `ν_node` | **ringdown overtones** | sets the substrate's frequency ceiling for overtone support: `ν_node=1.24e20 Hz` ≥16 OOM above any QNM overtone → the lattice supports **arbitrarily high overtone n without slew-limiting**; overtone cutoff is set by the wall geometry, **not** the substrate rate | **CLEAN-NULL gate**: no observed overtone row can be a slew-rate artifact (§1.5). Any overtone damping is geometric/impedance, not rate. |
| **§3.2 transfer functions** `H_shear, H_EM, H_bulk` | **every frequency row** (ringdown freq, QPO freq, line shifts) | each frequency row carries the **channel-specific** redshift of its source region: GW/line rows ride `H_shear=(1−A²)^{1/4}`; EM-phase rows ride `H_EM=(1−A²)^{−1/2}` | per-channel column: a frequency row must declare its channel (registry Rule 3) before the transfer function applies. |
| **§3.1 three-speed split** + **§3.3 c_EM flag** | **shadow / lensing** | shadow size + photon-ring + lensing geometry depend on which speed light tracks near the wall; the **shear** clock gives GR-like shadow, but `c_EM` **rises** `(1−A²)^{−1/2}` → 🚩 **unresolved**: does imaging follow the matter clock or carry an EM-phase-speed correction? | **OPEN discriminator** routed here from §3.3 — the BH matrix must adjudicate; channels diverge by `(1−A²)^{3/4}`. |
| **§2.1 Z_eff(A²) classes** + **§2.2 Z_eff(r)** | **all of the above** (the common substrate column) | the realization class (SYM / μ-only / ε-only) is the **master gate**: it sets whether the wall reflects (echo), how `Z` approaches the horizon, and the sign of every impedance step | the matrix's **realization-class column**: every BH-modifier row inherits SYM (reflectionless) vs ASYM (wall) from here. |

**Net wiring for the matrix:** the **realization class** (§2.1) is the master switch; the **reflectivity**
(§2.3) feeds echoes; the **slew ceiling** (§1) clamps the ringdown-overtone row to a clean null; the
**transfer functions** (§3.2) modify every frequency row by channel; the **three-speed split** (§3.1)
+ the **c_EM-rises flag** (§3.3) feed shadow/lensing with one **open discriminator** the matrix owns.
The live BH-matrix scouts consume these CSVs; this doc does **not** write the matrix rows (lane
discipline — the matrix scouts + auditor land those).

## §5 — Promotion note (auditor-gated)

These curves are the **quantitative layer** beneath two existing assets — the vocabulary and the
datasheet format — and supply the numbers neither currently carries:

1. **Under the field-symbol-registry** (`research/2026-06-10_field-symbol-registry.md`). The registry's
   §3.1–§3.3 rows name `c_EM`, `c_shear`, `c_bulk`, `Z_eff`, `Γ`, `ρ̄_cav` and declare their channels;
   this doc supplies the **curves** under those names (the registry says *what `c_shear` is*; §3.1 here
   says *how fast it freezes*). Candidate cross-link: registry §3.1/§3.2/§3.5 rows → these CSV curves.

2. **Under the Vol-9 datasheet candidate sections** (auditor-gated):
   - **ch5 AC electrical characteristics** (`vol9/ch5-ac-electrical-characteristics/index.md`) already
     names `ω_C = c0/ℓ_node`, the three sector speeds, and `Z_eff` — §1 (ω_node ceiling) + §3 (the
     three-speed derating curves) are its quantitative figures.
   - **ch7 saturation characteristics** (`vol9/ch7-saturation-characteristics/index.md`) already names
     the four-regime map **and an "op-amp slew rate → Axiom 4" translation row** — §1 (the slew spec)
     is the quantitative content of that row; §1.3's `SR(A)=SR_max·S(A)` compression sits on its
     four-regime phase diagram.
   - **ch14 phase diagrams** (`manuscript/vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex`) — the
     realization-class gating (§2.1) + regime tags (§1.2) are phase-diagram content; pairs with the
     pending ch14 rebuild spec (`2026-06-10_pilotwake-bhphase-survey_note.md`).

**Class (per `consistency-vs-emergence` v1.3):** this doc is **Class B / Class C synthesis** — it
**renders** canonical forms (the three speeds, `Z_eff`, the kernel) as datasheet curves and
**forward-derives** two items this arc (the approach profile `S=1−r_s/r`; the slew spec `SR_max`), both
from canonical primitives with **no new substrate primitive** introduced. It does **not** promote any
classification past its canonical-source ceiling. The Schwarzschild-redshift recovery (§3.2) is
**Class C consistency** (GR number via the matter-clock mechanism), explicitly tagged, not headlined as
emergence.

**Lane note.** Implementer-lane output: surfaces the curves + the flagged tensions — the
ε-vs-C exponent §2.1, the ¼-vs-½ profile exponent §2.2, the c_EM-imaging discriminator §3.3, the
**c_bulk floor-value candidate/CONTESTED** §3.1, the **√3/2 spin-2-vs-scalar sector scope** §1.2/§1.3,
and the **SYM first-order-null + second-order-residual** echo qualifier §2.3 — plus the α-slew 2π
notational slip (§1.4). The **auditor** lands the Vol-9 ch5/ch7/ch14 sections + the registry
cross-links and adjudicates the tensions; **Grant** owns the c_EM-imaging discriminator (§3.3 / §4
shadow-lensing row) and the α-slew coherence flag. Nothing here is canon. *(Three Class-A audit findings
applied this revision: c_bulk floor → candidate; √3/2 → spin-2-sector reference only; SYM echo →
first-order-null + second-order residual.)*

---

### Verification ledger (this doc)

| Item | Check | Result |
|---|---|---|
| constants | imported from `ave.core.constants`, cross-checked ≥6 sig figs | PASS (all 3 scripts) |
| `SR_max` | forward, no target in loop; dead-input on band edges (±3 OOM invariant) | derived (not fit) |
| α-slew value | `9.02e17 Hz = α·ν_node`; `(α/2π)·ν_Compton = 1.435e17` | **FLAG surfaced** §1.4 |
| SYM echo | **first-order** Born floor `d ln Z/dx≡0` (2nd-order residual carried §2.3) | first-order null (2.9e-15); 2nd-order ∼(ℓ_node/r_sat)² survives |
| c_bulk floor | `c_bulk(ρ̄_cav)=0` is the **defining root** (algebraic identity, not a check); floor-VALUE **candidate/CONTESTED** | identity holds; floor value flagged §3.1 |
| Schwarzschild track | `c_shear(r)/c0 ≡ √(1−r_s/r)` | PASS (max|diff|=0) |
| `make verify` | worktree + main checkout, per commit | GREEN ×4 |

