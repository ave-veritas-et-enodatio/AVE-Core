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
> `flag-don't-fix` (the ε-vs-C exponent tension §2.1 and the c_EM-rises imaging question §3.4 are
> surfaced for Grant/BH-matrix, not resolved ad hoc); Rule 12.

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
| `RHO_CAV` = −1/φ | −0.6180339887 | `cavitation_flow.py:64` (NOT constants.py — registry R8) |

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
| Small-signal ↔ large-signal boundary | `A = √(2α) ≈ 0.1208` (regime I→II, `four-regimes.md:26,33`) |
| Large-signal validity | regimes II–III, `√(2α) ≤ A < 1`; Axiom-4 kernel active |
| Rupture (absolute-max) | `A = 1` (`V = V_yield`), S→0, topology destroyed (`four-regimes.md:56`) |
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
Curve in `fig1b_slew_compression.png` / `slew_compression_curve.csv`. The regime boundaries
(`√(2α)`, `√3/2`, `1`) are the canonical four-regime phase-diagram tags (`four-regimes.md:26-29`,
Vol-9 ch14).

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
| **SYM** | **2.9×10⁻¹⁵** (machine zero) | ~0 | **NO** — `d ln Z/dx ≡ 0` |
| **μ-only** | 0.559 | 0.313 | **YES** |
| **ε-only** | 0.559 | 0.313 | **YES** |

Three results, all clean:
1. **SYM → zero echo**, to machine precision — the canonical `discrete-lattice-entropy-constant.md:59`
   result ("reflection set by the rate of change of Z; symmetric saturation → `dZ/dr=0` → no reflection
   to first order"). **Echoes are a falsifiable signature of the *asymmetric* realization classes only.**
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

## §3 — THE DILATION CURVES (derating-curve style)  *(next commit)*

## §4 — BH-MATRIX HOOKS  *(next commit)*

## §5 — Promotion note  *(next commit)*
