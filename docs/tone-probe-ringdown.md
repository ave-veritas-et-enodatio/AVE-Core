# Tone probe recorder and harmonic-inversion ring-down analyzer

**Backing page:** Math tone-reader backing page, 2026-10-06, sha1 b0cdef5db22f (candidate).
**Branch:** `feat/tone-probe-ringdown`. **Status:** candidate — no engine edits.

---

## What this tool measures, and what it does not

### What it measures

**Probe recorder** (`src/ave/topological/tone_probe.py`): records the engine's
public `u`, `omega`, `u_dot`, `omega_dot` arrays at chosen alive sites over
time, by wrapping `CosseratField3D.step()` at the runner level. No engine code
is modified.

**Analyzer** (`src/ave/topological/tone_analyzer.py`): pure post-processing on
the dumped arrays. Uses the **matrix pencil method** (Hua & Sarkar 1990,
doi:10.1109/29.56027) to extract complex frequencies from short time records.
Treats each probe time series as

    y(t) = Σ_k  c_k · exp(−i ω_k t),     ω_k = Ω_k − i Γ_k

and returns the angular frequency Ω_k, decay rate Γ_k, Q = Ω_k/(2Γ_k), and
amplitude per mode.

**What it gives (beyond what the engine already had):**

| Reading | Method |
|---|---|
| Bound-mode angular frequency Ω | T2 probe HI at sheath sites |
| Real Q = Ω/(2Γ) from ring-down envelope | T2 ring-down |
| Growth flag (Im ω > 0, Γ < 0) | T2 complex ω |
| 2ω content / KW-flag | T2 sheath vs far-field probes |
| d(Ω)/d(A²) backbone | T2 at several amplitudes |
| Mode profile vs radius | T2 radial rake probes |

### What it does NOT measure

- **Spatial mode shape.** The probe layout shows amplitude vs radius (via the
  radial rake) but not the full 3-D mode shape.
- **Toroidal/poloidal winding pattern (T3).** A separable Cartesian FFT or a
  probe time series alone cannot isolate the (m,n) torus-knot harmonic. T3
  (the mode projector; Transform 3 in the Math page) is a follow-on.
- **True Q without box-size validation.** Kill line **KBOX**: a reported Q is
  accepted only if unchanged under a 1.5× box and 2× sponge thickness. This
  tool provides the measurement infrastructure; the KBOX run is a follow-on.
- **Branch discrimination alone.** See the branch-split note below.

---

## LEAN flag

**The 10–20 period recommendation is LEAN** (a judgment by the AVE Mathematical
Theorist, 2026-10-06). The *direction* — that the matrix pencil method beats the
plain-FFT 1/T resolution limit for few-pole deterministic signals — is **DERIVED**
from the Cramér–Rao bound (Rife & Boorstyn 1974, doi:10.1109/TIT.1974.1055282)
and the FDTD precedent (MEEP/Harminv; Oskooi et al. 2010,
doi:10.1016/j.cpc.2009.11.008). The **binding limits** in this engine are:

1. **Non-stationarity:** Kerr chirp as the ring-down amplitude falls (the
   "backbone" shift, Feldman 1994).
2. **Band-edge continuum:** the gapped 3-D band edge contributes a non-pole
   tail ∝ t^(−3/2)·exp(−iω_m t). This fades faster than a high-Q pole; start
   the record a few periods after the kick to let it clear.
3. **Pole stability (KPOLE):** accept only poles stable under ±30% record
   length and a shifted window.

For spreading knots (like ENV-D's tube doubling in ~11 periods), use
**sliding-window analysis** (3–5-period windows) rather than a single fit.
See `sliding_window_analyze()` in `tone_analyzer.py`.

### Record-length accuracy table

Measured by `TestRecordLengthTable` and `TestRecordLengthNonstationarityTable`
(`src/tests/test_tone_probe_ringdown.py`).
Synthetic signal: Ω=1.9, Q=100, noise=1e-10 (simulating integrator error),
dt=0.165. The clean case uses 10 Monte Carlo trials; nonstationarity cases use 8.

**Clean signal only** (Ω_err_mean ± std, Q_err_mean ± std):

| periods | N_samples | Ω_err_mean  | Ω_err_std   | Q_err_mean  | Q_err_std   |
|--------:|----------:|------------:|------------:|------------:|------------:|
|       5 |       100 |  3.09e-12   |  2.39e-12   |  3.54e-08   |  2.99e-08   |
|      10 |       200 |  1.02e-12   |  9.87e-13   |  1.22e-08   |  9.61e-09   |
|      15 |       301 |  7.41e-13   |  5.67e-13   |  8.76e-09   |  6.42e-09   |
|      20 |       401 |  7.15e-13   |  6.09e-13   |  5.82e-09   |  3.37e-09   |
|      50 |      1002 |  3.21e-13   |  1.97e-13   |  2.87e-09   |  1.68e-09   |
|     100 |      2004 |  1.67e-13   |  1.24e-13   |  2.58e-09   |  1.25e-09   |

**Four-case comparison** (mean Ω error and mean Q error; chirp = fractional Ω
drift per period; drift = slow sinusoid at Ω/10, amplitude 1% of main signal):

| periods | N | Ω clean | Q clean | Ω c-1e-4 | Q c-1e-4 | Ω c-1e-3 | Q c-1e-3 | Ω drift-1% | Q drift-1% |
|--------:|---:|--------:|--------:|----------:|----------:|----------:|----------:|-----------:|-----------:|
|       5 | 100 | 3.4e-12 | 3.8e-08 | 4.6e-04 | 7.0e-02 | 4.6e-03 | 7.2e-01 | 1.7e-04 | 3.4e-01 |
|      10 | 200 | 1.2e-12 | 1.2e-08 | 8.9e-04 | 6.5e-02 | 8.9e-03 | 5.9e-01 | 2.1e-05 | 7.9e-01 |
|      15 | 301 | 7.8e-13 | 8.0e-09 | 1.3e-03 | 2.0e-01 | 1.3e-02 | 1.6e+00 | 2.2e-06 | 1.4e-02 |
|      20 | 401 | 7.3e-13 | 6.6e-09 | 1.7e-03 | 2.1e-01 | 1.7e-02 | 1.6e+00 | 4.4e-06 | 1.1e-01 |
|      50 | 1002 | 3.1e-13 | 2.4e-09 | 3.4e-03 | 3.1e-01 | 3.3e-02 | 1.4e+00 | 1.3e-06 | 1.7e-02 |
|     100 | 2004 | 2.1e-13 | 2.6e-09 | 4.9e-03 | 3.7e-01 | 3.9e-02 | 1.1e+00 | 1.3e-06 | 8.8e-03 |

**What the new columns show (LEAN flag):**
For the clean case, **even 5 periods give Ω error ~3e-12** — 10–20 periods is
more than adequate. For chirp-1e-4, the Ω error is already ~4.6e-4 at 5 periods
(dominated by the frequency drift) and grows with record length (5→100 periods:
4.6e-4 → 4.9e-3), because longer records accumulate more chirp. For chirp-1e-3
the errors are 10× larger still. The drift-1% case shows erratic Q errors due to
the slow baseline interfering with the HI fit at record lengths comparable to the
drift period (10 × T_period ≈ 33 time units); Ω errors are well below 1e-3 at
≥15 periods once the record is long enough to resolve the drift from the main pole.

**LEAN conclusion:** 10–20 periods suffice for clean signals. The binding limit
is non-stationarity (Kerr chirp), not noise. For chirp ≥ 1e-3 per period,
Ω errors of ~1% persist at all record lengths, independent of N; using sliding
windows (3–5 periods each) is the correct response in that regime, not longer
total records.

---

## Probe placement

Default probe placement (from `_default_probe_sites()`):

- **Sheath shell** (8 probes): ρ_t ≈ r_t, outer-equator (ψ=0), distributed in
  toroidal angle φ. This is the classically allowed region for in-window tones
  (s_tan ∈ [(ω²−2)/4, ω²/4]; anatomy page sha1 1c49fad87f10 §3.1).
- **Radial rake** (5 probes): ρ_t ∈ {0.5, 1.0, 1.5, 2.0, 3.0}·r_t at φ=0.
  Shows the mode's radial profile (needed for KA1).
- **Far-field** (6 probes): ±x/y/z at distance ≥ max(5, 3r_t) from centre.
  Monitors radiated energy and the 2ω content (KA5, KW).
- **Bulk reference** (2 probes): opposite side of the periodic box from the
  knot. Cross-check against far-field.
- **Sponge monitor** (1 probe, if pml_thickness > 0): just inside the sponge.
  Needed to measure reflected fraction (KBOX).

All sites are snapped to the nearest alive site (mask_A ∪ mask_B;
`cosserat_field_3d.py`:994–998).

An explicit override list of probe sites can be passed as `probe_sites=`.
A shell-average can be computed offline from the sheath probes after loading.

---

## WRAP-UNRESOLVED convention

From `src/scripts/envd_u4_b2.py` (post PR #1060): the per-site vector length
is |ω| = sqrt(ωx²+ωy²+ωz²). Max |ω| is recorded alongside every sample.
**Readouts cannot be trusted once max |ω| > π.** Samples exceeding π are
saved but flagged via `wrap_flags` in the .npz output and counted in the JSON
metadata (`n_wrap_flags`).

---

## `extract_quality_factor` is a geometry formula, not a ring-down

`CosseratField3D.extract_quality_factor()` at
`src/ave/topological/cosserat_field_3d.py`:2627–2630 computes the geometric
identity 16π³Rr + 4π²Rr + πd. This is **not** a ring-down Q. On a
ENV-D-like knot (R ≈ 8, r ≈ 2.5) it prints about 1.07×10⁴ — a number
unrelated to any leak (arithmetic, DERIVED from the Math page).

The ring-down Q = Ω/(2Γ) from `tone_analyzer.py` is the dissipation Q
(stored energy / energy lost per radian). These are different objects.
`extract_quality_factor` was left unedited.

---

## Band references (engine natural units)

Engine natural units: G = G_c = γ = ρ_vac = 1, ℓ_node = 1 (dx = 1).
All frequencies are dimensionless (1/time_unit where c_T = √(G/ρ) = 1).

From F1 dispersion (sha1 db7a54e50815):

| Symbol | Value | Meaning |
|---|---|---|
| ω_ac,top = √(10/3) | ≈ 1.8257 | acoustic/longitudinal top |
| ω_T,top = 1 | 1.0 | transverse top |
| ω_m = 2 | 2.0 | rotational sector bottom |
| ω_rot,top = √6 | ≈ 2.4495 | rotational sector top |
| 9% window | [√(10/3), 2] = [1.826, 2.0] | clean stop band (bound-mode target) |
| T1-widened | [1, 2] | includes transverse sector |
| Rotational band | [2, √6] | rotational pass band |
| Kill line KW | 2·Ω ∈ [2, √6] | doubled-tone check |

---

## Branch-split note

The engine (`cosserat_field_3d.py`:815/825) codes **only branch (a),
soften-on-strain**. A measured d(Ω)/d(A²) is branch-(a) saturation **NET of
the Op10, reflection, and Hopf stiffeners**. It does NOT discriminate bond
rules unless the saturation selector is exposed as a runner option (a
follow-on) OR k_op10 = k_refl = k_hopf = 0. Do not interpret the sign of
d(Ω)/d(A²) alone as selecting the bond rule.

With k_op10 = k_refl = k_hopf = 0 and use_saturation=True (exposed as public
attributes `cosserat_field_3d.py`:1037, :1041): the sign tests the pure
soften-on-strain branch (a) selector and confirms DC-page Q2(i). This variant
is supported via the runner; set them to 0 before stepping.

**Shared-medium consistency check (R26.196, banked):** A falling measured tone
(d(Ω)/d(A²) < 0) means the engine's loaded medium slows waves at higher strain,
which is the *opposite* of the birefringence Letter's faster-light direction. A
rising tone (d(Ω)/d(A²) > 0) matches the Letter's direction. This is a
shared-medium consistency check only (from a room evaluation, tracker R26.196,
which is banked). It is not evidence on the Letter's registered test.

---

## Smoke test result (KV1 — uniform k=0 mode)

**Setup:** 12×12×12 periodic grid, k_op10 = k_hopf = k_refl = 0,
use_saturation=False, damping_gamma=0.0. Uniform ω_z kick at amplitude
a=0.05 (linear regime, a/ε_y = 0.05 ≪ 1). 15 periods × 2π/ω_m, dt≈0.095.

**Expected:** ω_m = 2 exactly (DERIVED from the engine's micropolar energy
W_micropolar = 2G_c·n_alive·|ω|², giving ω_ddot = −4G_c·ω → f=2).

**Result:** Ω ≈ 2.003. The offset from ω_m=2 is the **Verlet integrator
dispersion shift**: at dt≈0.095 (cfl_dt for the 12×12×12 grid), the VV
discrete-time oscillator rings at `(2/dt)·asin(dt) ≈ 2.003` rather than 2.0
exactly (Gate corpus-conflict #2, resolved 2026-10-06). This is *not* a
record-length or noise-floor error. The analyzer pipeline is confirmed
functional.

No WRAP (max |ω| = 0.005 ≪ π). No growing modes (Hamiltonian engine,
energy-conserving VV).

**Interpretation:** the smoke test validates the analyzer pipeline against a
closed-form result. A larger error would indicate a pipeline fault, not a
physics finding. For a full knot run, longer records and the box-size
condition (KBOX) are required before any Q value is meaningful.

---

## Growth-tolerance rule (Gate k-cal 2026-10-06)

**Scope:** identified-tone growth/decay flag only — NOT the cold-seed
window-presence test and NOT the shell-flux zero kill (tracker R26.196b).

The locked formula (`_classify_pole`, Gate k-cal 2026-10-06):

```
σ_Γ_CR = √6 · σ_resid / (|c| · dt · √(N(N²−1)))
growth_tol = max(5·σ_Γ_CR, 3·Gamma_err, 50·eps_mach·|Ω|)
is_growth  = Gamma < −growth_tol
```

`σ_resid` is the per-component RMS residual `√(mean(|y−ŷ|²)/2)` from the
multi-pole reconstruction; it is computed inside `analyze()` and passed to
`_classify_pole` automatically. `|c|` is the fitted pole amplitude.

**Why k=5:** empirical matrix-pencil scatter is ~1.45–1.51× the analytic CR
(k=5 on the σ_resid form covers this gap at 0% FP over 250 null trials).
k=3 on the CR_resid form gives ~2% FP (Gate FAIL). False "leaks" are the
costly error in ENV-D cold-seed decisions.

**Null FP table** (Γ=0, Ω=1.9, dt=0.165, 15 periods, N=301, 200 trials,
complex Gaussian noise, seed=1; `TestGrowthNullFloor` in the test suite):

| noise    | FP main | FP any | σ_emp Γ   | σ_CR Γ (ref) | emp/CR |
|----------|---------|--------|-----------|--------------|--------|
| 1e-10    | 0%      | 0.5%   | 7.82e-13  | 5.69e-13     | 1.38   |
| 1e-8     | 0%      | 0.5%   | 7.82e-11  | 5.69e-11     | 1.38   |
| 1e-6     | 0%      | 0.5%   | 7.82e-9   | 5.69e-9      | 1.38   |

Prior formula `max(3·Gamma_err, 50·eps·|Ω|)` gave ~49% FP main / ~72% FP
any at noise ≥1e-10 (Gate FAIL, 2026-10-06 audit). True positives at
Γ=−1e-4 and −1e-3 with noise 1e-8 remain 100% (sensitivity intact; k=5
margin ×35 and ×350 above growth_tol respectively).

---

## Kill lines

| Line | What it tests | Status |
|---|---|---|
| **KV1** | Uniform k=0 mode rings at ω_m=2 | **VALIDATED** by smoke test |
| **KV2** | Knot-free box reproduces F1 band edges | Not run (follow-on) |
| **KBOX** | Q unchanged under 1.5× box + 2× sponge | Not run (follow-on) |
| **KPOLE** | HI pole stable under ±30% record length | Implemented in `analyze()` |
| **KQ** | Measured Q_ring vs Q=α⁻¹ claim | Instrument built; run is a follow-on |
| **KA1** | Tone energy at sheath (s_tan window) | Instrument built; run is a follow-on |
| **KA4** | d(Ω)/d(A²) with selector exposed | Follow-on (see branch-split note) |
| **KA5** | No 2ω propagation to far field | Instrument built; run is a follow-on |
| **KW** | 2·Ω in [2, √6] check | Flag implemented in `band_report()` |

---

## Follow-ons (out of scope for this PR)

**(a) BIND-1 — spinning-lump test.** Does a hard-driven, spinning knot at
max|θ| ≥ π hold together? Needs a new seed with Q_H ≠ 0 and a Grant GO.
This build supplies BIND-1's *readouts* (tone, Q, mode profile) but not the
experiment.

**(b) Toroidal/poloidal mode projector (T3).** The (m,n) torus projector CAN
read the (2,3) pattern even with Q_H = 0 and would read ENV-D's untying better
than the crossing count. What it cannot do without Q_H ≠ 0 and max|θ| ≥ π is
tell a topologically protected knot from a merely drawn phase pattern. See
Math page §1.3, ⚑1.

**(c) Expose the saturation selector.** To discriminate branch (a) from (b)/(c)
via the d(Ω)/d(A²) sweep, the S-factor at `:815/:825` must be exposed as a
runner-level config option. This is one runner line once the GO is given.

**(d) KV2 + KBOX runs.** Knot-free box for band-edge validation; then
progressively larger boxes to verify Q does not move with box size (KBOX).

---

## Corpus conflicts (Standing Rule 10 / R26.191)

| # | Where | Corpus claim | Engine/method says instead |
|---|---|---|---|
| **CQ1** | `manuscript/ave-kb/claim-quality.md`:423; `manuscript/ave-kb/common/trampoline-analogy-primer.md`:379 | "the breathing-soliton Q-factor at the Golden Torus gives α = 1/(4π³+π²+π)" — called a **dynamic result** | `extract_quality_factor` at `cosserat_field_3d.py`:2627–2630 is a **geometry formula** (16π³Rr + 4π²Rr + πd). The engine has no ring-down Q measurement. The tool built here measures the **dissipation Q** = Ω/(2Γ), a different object. Kill line **KQ**: if the measured Q_ring of the bound tone ≠ 137 ± error, this refutes "Q = α⁻¹" as a dissipation statement. Caveats: (i) the claim is made for the Master Equation FDTD engine, not cf3d; (ii) the Golden Torus R·r = 1/4 in ℓ_node units is sub-cell in cf3d (r ≤ 1/16 cell for resolved R ≥ 4). |
| **CQ2** | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md`:13 | "permanently trapping the energy" | The window is a finite stop-band, so a bound tone has a **finite Q** via Paley–Wiener tunnelling (F1 §3, anatomy page L4). T2 measures it, or bounds it from below. The same line's own annotation already re-scopes "trapping" to topology + boundary. |
| **CQ3** | `cosserat_field_3d.py`:1003–1009 (doc comment) | "Cosserat-sector PML … mirrors the K4 Sponge PML" | The absorber is a **velocity-scaling sponge** (`:1017–1018`), not a PML. It reflects a frequency-dependent fraction. Its reflection must be measured before any Q is trusted (KBOX). |

---

## Implementation notes

**Doc convention:** `docs/` directory, following the pattern of `docs/USAGE.md`
and `docs/workflows/`.

**No engine edits.** The probe recorder is purely at the runner level: it
wraps `step()` and reads the public `u / omega / u_dot / omega_dot` arrays.
`extract_quality_factor` is untouched.

**Authored by Claude (Sonnet 4.6)**, 2026-10-06. Per `feat/tone-probe-ringdown`
PR body.
