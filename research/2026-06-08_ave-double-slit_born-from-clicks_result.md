# AVE Double-Slit — the Born Rule ASSEMBLING from Clicks — RESULT

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-ave-double-slit`
**Driver**: `src/scripts/vol_2_subatomic/ave_double_slit_born/` (run `python -m scripts.vol_2_subatomic.ave_double_slit_born.run_capstone`)
**Figures**: `research/figures/2026-06-08-ave-double-slit/`
**Discipline stack**: substrate-native-check + ave-canonical-source + consistency-vs-emergence + validate-what-you-did + ave-evidence-framing
**Outcome**: **Born rule p ∝ |E|² RECOVERED from threshold-crossing detector statistics — no Born postulate anywhere in the click code. χ²/dof = 1.02.**

This is the QM-trio capstone visual: superposition (aliasing → interference),
collapse (threshold-crossing → discrete clicks), and the Born rule (p = 2
*derived*, not postulated) shown together — the smooth interference field AND
the discrete clicks building the *same* fringe pattern (wave AND particle).

---

## Engine (substrate-native-check + ave-canonical-source)

Two deliberately separate sectors:

### Field sector — REAL FDTD (canonical engine)
`field_engine.py` reuses the **canonical** `ave.core.fdtd_3d.FDTD3DEngine`
(Yee-cell K4-TLM Maxwell solver). **No Maxwell update is re-implemented.** A
z-thin slab (`nz=3`) carries a TM_z 2D slice: with a z-uniform Ez source and a
z-uniform PEC slit-wall, only (Ez, Hx, Hy) populate and the field stays
z-uniform (measured z-uniformity = **2.4e-4**), so the mid-plane is a faithful
2D Maxwell solution. The two-slit PEC barrier is imposed by clamping the
tangential Ez to 0 at wall cells each step (a boundary condition layered on the
canonical engine, not a new solver). A perimeter sponge damps edge reflections.

The coherent interference profile |E|²(y) at the detector row is extracted by
I/Q phasor demodulation of a pulsed wavepacket over ~3 carrier periods at peak
arrival — this rejects both the diffuse steady-state floor and the moving-fringe
smear, giving deep-minima fringes.

- carrier λ = 18.0 cells (analytic 18.1) · slit sep d = 72 · slit-to-detector L = 192
- **fringe spacing = 46.5 cells vs de-Broglie / Fraunhofer λL/d = 48.0 cells (3.1%)**, Fresnel # = 1.50

### Detector sector — Axiom-4 saturation kernel (canonical)
`click_detector.py` reuses the **canonical** Axiom-4 saturation kernel
`ave.axioms.scale_invariant.saturation_factor`, S(A) = √(1 − (A/A_yield)²), as
the self-trap gate. The kernel is **not** hand-rolled.

---

## The click model (the load-bearing honest part)

A detector screen is a row of cells. Each cell accumulates absorbed field
**energy** under fluctuation-dissipation (FDT) noise — shot (Poisson) +
Johnson-Nyquist (Gaussian) — and **self-traps (one click)** the instant its
accumulated amplitude crosses the Axiom-4 saturation yield S(A) → 0
(A → A_yield). That is the entire rule: stochastic energy loading + a
first-passage threshold.

The detector consumes **only the physical absorbed-power density** (the FDTD
field energy density, = |E|²) — as an absorption **rate**, never as a
probability. It runs in the single-quantum-sensitive regime (m = A_yield²/quantum
≈ 1): the first cell to absorb a yield-quantum self-traps. By the
competing-exponentials theorem, independent first-passages fire cell *i* first
with probability proportional to its rate (= |E|²) → **Born emerges**.

**Why the exponent (the "2") is honest, not circular.** A real detector
responds to **energy**, and field energy density is |E|² (Poynting/Maxwell —
computed by the FDTD, not chosen). So the per-cell absorption rate ∝ |E|². The
exponent 2 is "energy ∝ amplitude²", **not** the Born postulate. Counterfactual
(see validation): a detector responding to |E|¹ or |E|³ does **not** reproduce
the wave pattern; only the physical energy exponent does. The probability law is
never written down — it assembles from the click statistics.

**What is NOT in the click placement code** (confirmed by grep, see below): no
Born rule, no p = |ψ|², no sampling from |ψ|² (`rng.choice(p=…)`, inverse-CDF of
|E|², or normalisation-to-a-probability). The intensity is rescaled to unit
*mean* (a units/efficiency choice — it does not sum to 1).

---

## Validation (validate-what-you-did)

| Check | Result | Verdict |
|---|---|---|
| Histogram match — χ²/dof (clicks vs FDTD \|E\|², 6000 clicks) | **1.02** | Born recovered (consistent with Poisson sampling of \|E\|²) |
| Histogram match — KS statistic | **0.009** | excellent |
| Histogram match — Pearson corr | **0.968** | excellent |
| Fringe spacing — clicks vs de-Broglie λL/d | 46.5 vs 48.0 cells (**3.1%**) | matches wave prediction |
| z-uniformity of the 2D slice | 2.4e-4 | faithful 2D Maxwell |
| **No-Born grep of detector CODE** | **all_pass = True** | no Born/p=2/\|ψ\|² in placement |
| Energy-exponent counterfactual (only p=2 should match) | \|E\|¹→χ²=4.89, **\|E\|²→1.13**, \|E\|³→2.29 | exponent is energy-forced |
| **Argmax-fallback audit** — clicks routed through the \|E\|² safety fallback | **0 / 6000 (0.00%)** | every click a genuine first-passage crossing |

The no-Born grep tokenizes `click_detector.py`, strips comments + docstrings,
and confirms the executable tokens contain no `born`, no `psi`, no weighted
sampler (`p=`/`multinomial`), no `intensity.sum` normalisation, while confirming
`saturation_factor` (canonical kernel) IS used and intensity is consumed as a
`rate`. The words "born"/"psi" occur **only** in prose — docstrings and comments,
never executable code (9 and 3 raw occurrences; the "born" count is +2 over the
original 7 solely from the two new fallback-audit instrumentation comments).

**Argmax-fallback audit (auditor nit).** `accumulate_clicks` has a safety
fallback: if a cell never crosses the saturation yield within `max_micro_steps`
(60000) the click is routed to the brightest realised cell, `argmax(accum)` — a
direct |E|²-correlated path that would *partially manufacture* the Born
agreement. With mean first-passage ≈ 14 micro-steps it fires effectively never,
but a future retune (higher `thermal_kT` / lower `coupling`) could silently
route a fraction of clicks through it. The detector now **counts** every
fallback fire and exposes it on `ClickResult`; `validate.fallback_audit`
**asserts the count is 0** (reporting the fraction in its failure message) and
writes `argmax_fallback_count` / `argmax_fallback_fraction` into
`capstone_validation.json`. Re-run result: **0 / 6000 (0.00%)** — every click is
a genuine first-passage yield-crossing, and the Born stats are byte-unchanged
(χ²/dof = 1.02, KS = 0.009), confirming the counter is pure instrumentation, not
a physics change.

The m=2 detector (quantum=0.5) degrades to χ²/dof = 1.59, confirming the
single-quantum (m≈1) Born regime predicted by competing-exponentials theory —
i.e. Born is recovered *because* of the threshold-crossing mechanism, not by
construction.

---

## Classification (consistency-vs-emergence)

- **Discrete localized clicks from a continuous field** (collapse / particle
  behaviour) — **Class-2 emergence** (mechanism: saturation-kernel self-trap).
- **Click histogram reproducing |ψ|²** (Born statistics) — **Class-2 emergence**
  (mechanism: competing first-passage at rate ∝ absorbed power).
- **Agreement with the QM Born rule + the Fraunhofer fringe spacing** —
  **Class-4 consistency** (matches established QM / wave optics).

Per ave-evidence-framing: the claim is **"Born p ∝ |E|² is recovered as the
large-N statistics of threshold-crossing clicks; no Born postulate in the
detector; the exponent 2 is the energy-vs-amplitude relation, physically
forced."** It is **not** a from-nothing derivation of the integer 2 from
topology.

---

## Honesty (heightened, per the capstone brief)

- The interference field is **REAL FDTD** (canonical Maxwell engine).
- The click model is **threshold-crossing first-passage** under FDT noise —
  REAL mechanism, not a fit to |ψ|².
- **|ψ|² EMERGES** (verified non-circular by the grep + the exponent
  counterfactual).
- The electron's **(2,3) torus-knot winding is NOT shown** — it is not hostable
  in this field-sector showcase. What propagates through the slits is the EM
  field wavepacket (the soliton's radial wake / field envelope), not the knot
  core.
- The field is **linear Maxwell** (deeply below V_yield); the Axiom-4
  non-linearity is used in the **detector** (the saturation self-trap), which is
  where it physically belongs for absorption/collapse.
- The smooth-field still is **column-normalised** for display (to defeat the
  ~1/r cylindrical decay and reveal the fan); the quantitative |E|² profile at
  the detector is shown un-normalised in the histogram figure.

---

## Figures (research/figures/2026-06-08-ave-double-slit/)

- `a_smooth_interference_field.png` — the smooth REAL FDTD |E|² interference fan
- `b_clicks_first.png` — the first 12 clicks (scattered, no pattern)
- `c_clicks_hundreds.png` — 700 clicks (the fringe pattern emerging)
- `d_born_recovered.png` — final 6000-click histogram vs the field |ψ|² (Born back)
- `born_from_clicks_animation.mp4` — 15 s / 360 frames: clicks landing one-by-one
  over the real field, the live histogram assembling the fringes
- `capstone_validation.json` — machine-readable validation record

---

## Reproduce

```bash
PYTHONPATH=src python -m scripts.vol_2_subatomic.ave_double_slit_born.run_capstone
# add --skip-anim to skip the mp4 (stills + validation only, ~10 s)
```
