# RESULT — Vacuum-Birefringence Facility / Tolerance Survey (E-route is the AVE test; magnetic-route does NOT test AVE)

**Date:** 2026-06-22 · **Lane:** implementer · **Branch:** `docs/birefringence-arc-2026-06-22`
**Scope:** the global facility landscape + tolerance ranges that could run the AVE vacuum-birefringence test.
Characterization + tracking only — not a ranking or a recommendation. Every number carries an inline
`[facility, source]` citation.
**Workflow:** `w14ptjz80` (26 setups, 4 sub-surveys, citations sourced & verified in-code against
`src/ave/bench/birefringence.py`).
**Class:** survey / tracking (no physics claim originated here; the AVE prediction it characterizes is
`clm-pp3qwf` E-route + `clm-pvlas1` static-B null).

> **RESOLVED FRAMING (read this first).** Per the node-up resolution
> ([`2026-06-22_node-up-small-large-signal_result.md`](2026-06-22_node-up-small-large-signal_result.md),
> `clm-pvlas1`), a **static B is transparent to AVE** (`δn_μ = 0` exactly). So the magnetic-route facilities
> (PVLAS / BMV / OVAL / VMB@CERN, and the high-field magnet user labs) test **QED magnetic birefringence**,
> and do **NOT** test the AVE prediction. The earlier "PVLAS falsifies AVE by ~37,000×" headline is
> **RETRACTED** — it fed a static-B field through the ε-route proxy, conflating a propagating-wave
> energy-density construction with a static-DC-B response (FORK-1 §5). **The real AVE test is the E-route**:
> HIBEF @ European XFEL is the only purpose-built E-route bench. The matched differential ratio is
> `7.5/α³ ≈ 1.93×10⁷` (field-independent).

---

## 0. The discriminator (why field magnitude is not the gate)

Verified in-code (`src/ave/bench/birefringence.py`, origin/main): the substrate identity
`(E_CRIT/E_YIELD)² = 137.035999 = 1/α` EXACT; `E_YIELD = 1.1304×10¹⁷ V/m`; `B_yield = 3.77×10⁸ T`
(`= √α·B_crit`). The AVE/QED **ratio is FIELD-INDEPENDENT** — at every reachable field, AVE rides a
fixed factor above the QED Euler-Heisenberg signal on a *shared E²-leading slope* (the discriminator is the
COEFFICIENT, not the exponent; the historical "E⁴" form is retracted as a `√ε` conflation, `clm-pp3qwf`).

The highest *real* focused field in the lane (CoReLS, `E ~ 9.1×10¹³ V/m`) is still ~1.2×10³ below `E_YIELD`,
so `A_E = E/E_yield ~ 6.5×10⁻⁷` even at record intensity. **But the AVE/QED ratio does not depend on field**,
so reaching `E_yield` is NOT the gate; the gate is whether a fielded polarimeter can read a retardance that
exceeds the QED prediction by ~7 orders at *whatever* field is reached. The signal is never floor-limited —
`ψ_AVE` sits 4-7 orders above both `ψ_QED` and every cited polarimetry floor.

> **Coefficient convention (carried as a band, not a point).** The headline ratio depends on which
> (AVE-coefficient, `a_EH`) pair is quoted: code uses `δn_AVE = −¼A²` with `a_EH`-dependent ratio
> `4.1×10⁶` (7/45) … `9.7×10⁶` (3/45 differential); the manuscript OQ-1 differential is `−½A²` + `7.5/α³`,
> exactly 2× the code's differential ratio. Cite as the band `[4×10⁵, 2×10⁷]`; the physics verdict is
> identical (`~10⁶–10⁷×` QED, field-independent).

## 1. The E-route — the AVE test (Lane B)

Lane B splits into **one measurement facility** and **ten field sources**.

### 1.1 HIBEF @ European XFEL (BIREF@HIBEF) — the only purpose-built E-route bench

- **Setup:** pump = ReLaX optical Ti:Sa relativistic laser (1.55 eV / 800 nm) polarizes a vacuum region;
  probe = EuXFEL hard-X-ray pulse acquires a polarization flip; readout = high-purity X-ray polarimeter
  (channel-cut Si/diamond, 6× 90° reflections) in crossed-polarizer "dark-field" geometry. Single-pass
  (no Fabry-Perot), interaction length `z ~ 10 µm`.
- **Field:** ReLaX peak intensity `I_L = 10²¹ W/cm²` → `E ~ 8.7×10¹³ V/m` [BIREF@HIBEF LoI, arXiv:2405.18063
  / HPLSE 2024, Cambridge Core 9AD9183974A2A5A90D4EE35A86DE5CAB]. EuXFEL probe 5-24 keV, scenarios at
  8766 eV / 12.914 keV, `~10¹² photons/pulse` [arXiv:1807.03302; NJP 2021, doi:10.1088/1367-2630/ac1df4].
  `A² = (E/E_yield)² ~ 6×10⁻⁷`.
- **Polarimetry floor (binding for the whole lane):** required X-ray purity `P = 1.4×10⁻¹⁰`
  [NJP 2021]. Best DEMONSTRATED purity: `2.4(±0.9)×10⁻¹⁰` at 6.457 keV, `5.7×10⁻¹⁰` at 12.914 keV
  (Si channel-cut, 6× 90°) [Marx-Schulze, PRL 110, 254801 (2013)]. Predicted QED flip-probability `~10⁻¹²`;
  `~0.86` signal photons/hr vs `~5.6×10⁶` background photons/hr → 5σ "impractically long" at current optical
  intensity [NJP 2021].
- **AVE-vs-QED:** the same field-independent amplitude ratio holds; on flip-PROBABILITY it squares to
  `~9×10¹³×` QED, driving the predicted flip-prob `>1` (perturbative form breaks) — i.e. the AVE signal
  would sit orders above any X-ray floor at the field actually reached, while QED sits below it.
- **takes_requests:** collaboration.

### 1.2 PW-laser field sources (10 facilities — field but no fielded polarimeter)

These deliver the `E`-field but read produced PARTICLES (or nothing polarimetric); none fields a
vacuum-birefringence polarimeter. A birefringence run would require importing an X-ray-probe + high-purity
polarimeter. This is the dominant structural gap for the lane.

| Facility | Location | Peak intensity / field | Rep rate | takes_requests |
|---|---|---|---|---|
| **ELI-Beamlines L4 ATON** (10 PW / 1.5 kJ) | Dolní Břežany, CZ | `10²⁴ W/cm²` → `E ~ 2.7×10¹⁴ V/m` [doi:10.1063/5.0022120] | 1 shot/min | open user |
| **ELI-NP HPLS** (2×10 PW) | Măgurele, RO | `10²²–10²³ W/cm²` → `E ~ 8.7×10¹³ V/m`; two-arm pump+probe geometry [HPLSE 10, e21 (2022)] | 1/60 Hz | open user |
| **Apollon** (LULI, design 10 PW; 2 PW commissioned) | Saclay, FR | `>10²³ W/cm²` design [arXiv:2412.09267] | 1 shot/min | open user |
| **CoReLS** (4 PW, world intensity record) | Gwangju, KR | `1.1(±0.2)×10²³ W/cm²` → `E ~ 9.1×10¹³ V/m` (highest real focused field) [Optica 8, 630 (2021)] | 0.1 Hz | collaboration |
| **SULF** (10 PW + 1 PW user) | Shanghai, CN | `>10²² W/cm²` → `E > 2.7×10¹³ V/m` [researching.cn OJcb1d43e6088a2bf] | 0.1 Hz (1 PW) | collaboration |
| **SEL / Station of Extreme Light** (100 PW, under constr. ~2027) + 20 keV SC-XFEL | Shanghai, CN | `>10²³ W/cm²`; projected ellipticity `1.8×10⁻¹⁰–10⁻⁹`, ~10 flip photons/shot [PPCF 60, 044002 (2018)] | front-end 0.1 Hz | unclear |
| **Vulcan 20-20** (20 PW + 20 kJ, under constr.) | RAL, UK | `>10²³ W/cm²` class (focal field unpublished) [clf.stfc.ac.uk] | unpublished | open user |
| **ELI-ALPS HF** (2 PW @ 10 Hz — highest PW-class rep) | Szeged, HU | `~10²² W/cm²` → `E ~ 2.7×10¹³ V/m` [arXiv:2105.05494] | 10 Hz | open user |
| **ZEUS** (3 PW, NSF mid-scale) | U. Michigan, US | `>10²² W/cm²` → `E ~ 2.7×10¹³ V/m` [Phys. Plasmas 32, 103107 (2025)] | 1 shot/min | open user |
| **CETAL-PW** (1 PW) | Măgurele, RO | `10²¹ W/cm²` → `E ~ 8.7×10¹² V/m` [cetal.inflpr.ro] | 0.1 Hz | open user |
| **Texas PW** (~1 PW) | UT Austin, US | `~2×10²¹ W/cm²` → `E ~ 1.2×10¹³ V/m` [AIP CP 1507, 874 (2012)] | ~1 shot/hr | open user |

Plus two strong-field-QED **E-route programs** that reach the field but read particles, not retardance:
**DESY LUXE** (16.5 GeV EuXFEL e-beam × laser; `1.3×10²⁰ → 1.2×10²¹ W/cm²`, ξ = 7.9 → 23.6; scintillator /
tracker / γ-spectrometer diagnostics) [LUXE TDR arXiv:2308.00515] and **SLAC E320 / FACET-II** (10-13 GeV
beam × 10 TW laser; `~10²⁰ W/cm²`, a₀ = 3-7; positron tracker + Compton spectrometers)
[arXiv:2506.04992; arXiv:2604.23805]. Both would need a wholly different (X-ray-probe) polarimeter.

## 2. The magnetic route — does NOT test AVE (Lanes A/C)

Per `clm-pvlas1`, a static `B` gives `δn_μ = 0` exactly in AVE. These facilities measure QED magnetic
birefringence and **do not test the AVE prediction** — recorded here for completeness and as the QED
validate-on-known anchor (PVLAS recovers `A_e = 1.32×10⁻²⁴ T⁻²`, the bench's gate). They are NOT the AVE
discriminator.

### 2.1 READY end-to-end magnetic-birefringence benches

| Facility | Location | Field | Cavity | Polarimetry floor / result | takes_requests |
|---|---|---|---|---|---|
| **PVLAS** (ended 2018) | INFN Ferrara, IT | two 0.8 m, 2.5 T rotating permanent dipoles (∫B²dL ≈ 10 T²m, 100% DC duty) [arXiv:1301.4918] | F = 4.14×10⁵ (sci-run 2.4×10⁵), L = 3.303 m, λ = 1064 nm | best `Ψ_floor = 1.5×10⁻¹⁰ rad @1600 s`; null `Δn = (12±17)×10⁻²³ @2.5 T` (~7× QED). Wall = mirror intrinsic birefringence + seismic/thermal beam-spot motion [arXiv:1510.08052] | no (ended) |
| **BMV** | LNCMI Toulouse, FR | pulsed 6.5 T (XXL upgrade ∫B²L up to 100 T²m) [arXiv:1302.5389] | F = 4.4×10⁵, L = 1.83 m | shot-noise diff-arm `~10⁻¹³ rad/√Hz`, per-shot VMB floor `~8×10⁻²¹ T⁻²`. Wall = dynamical mirror birefringence ∝ (angle-of-incidence)², vibration-modulated [arXiv:1812.10409] | collaboration |
| **OVAL** | Tokyo / Tohoku, JP | high-rep pulsed 9.0 T (max 11.4 T), ∫B²dz = 13.8 T²m, f_rep = 0.2 Hz [arXiv:1705.00495] | F ~ 6.5×10⁵, L = 1.38 m | shot-noise-limited prototype (extinction σ² = 3×10⁻⁷); projected `Δk = 1.2×10⁻²⁰/√(T_run[s])` | collaboration |
| **VMB@CERN** (proposed) | CERN, CH | LHC SC dipole, B²L ~ 1200 T²m (~8.3 T × ~15 m); novel co-rotating-HWP modulation (magnet can't rotate) [arXiv:2110.03943] | intracavity-element-limited (cites F_PVLAS ~ 7×10⁵) | bench polarimeter `3.5×10⁻⁷ rad/√Hz` (RIN-limited), → `~5×10⁻⁸` over 53 s; target signal `ψ₀ ~ 1.4×10⁻¹⁴` | unclear |

(ALPS II @ DESY is Lane-A-ADJACENT: a light-shining-through-wall axion experiment, 2×12 HERA dipoles @ 5.3 T,
BL = 563.2 T·m — NOT a birefringence polarimeter, NO ellipticity floor. Listed for completeness.)

### 2.2 PURE-CAPABILITY high-field magnet user labs (B source; need an imported polarimeter)

All EMFL / MagLab open user facilities; none hosts a resident VMB ellipsometer. None tests AVE (static B).

| Facility | Type | Peak field / bore | takes_requests |
|---|---|---|---|
| **LNCMI-Toulouse** | pulsed | 98.8 T non-destructive (~100 ms) / 200 T destructive (µs) [lncmi.cnrs.fr; arXiv:2506.23779] | open user |
| **LNCMI-Grenoble** | DC | 37 T resistive / 43 T hybrid, 34 mm bore [IEEE 9714155] | open user |
| **NHMFL** | pulsed (LANL) + DC (Tallahassee) | 100 T pulsed (5 ms, 15 mm bore) / 45 T hybrid + 41.5 T resistive DC [osti.gov/786730; Nature s41586-019-1293-1] | open user |
| **HLD Dresden** | pulsed | >95 T (11 ms, 16 mm bore), 50 MJ bank [hzdr.de] | open user |
| **HFML-FELIX Nijmegen** | DC | 37.5 T Bitter / 45 T hybrid (commissioning) [hfml-felix.nl] | open user |

## 2.3 Why the magnetic route is moot for AVE (the resolved physics call)

The earlier tolerance pass flagged a "lane tension": because the (incorrectly-applied) AVE/QED ratio is
field-independent, the published PVLAS/BMV nulls at 2.5-6.5 T appeared to *already exclude* an AVE
`−¼A²` coefficient at lab field by `~3.7×10⁴×` (surviving coefficient `~6.8×10⁻⁶` vs `0.25`) — UNLESS
yield-field scaling deferred onset. **That tension is now resolved and the apparent exclusion is void:** it
fed a static `B` through the **ε-route** proxy `A = cB/E_yield`, which is a propagating-wave / energy-density
construction, NOT a static-DC-B response. The correct μ-grade response to a static `B` is `δn_μ = 0` exactly
(`clm-pvlas1`). So the magnetic-route nulls neither falsify nor constrain AVE — they simply do not test it.

## 3. Cross-setup tolerance comparison

| Dimension | Range across setups (cited) |
|---|---|
| **Ellipticity / polarimetry floor** | B-route (rad-ellipticity): BMV diff-arm shot-noise `~10⁻¹³ rad/√Hz` → PVLAS integrated `1.5×10⁻¹⁰ rad @1600 s` (wideband `~3×10⁻⁷ rad/√Hz` with cavity) → OVAL σ² = 3×10⁻⁷ → VMB@CERN `3.5×10⁻⁷ rad/√Hz`. E-route (X-ray purity, different unit): required `P = 1.4×10⁻¹⁰`, best demonstrated `2.4×10⁻¹⁰ @6.457 keV` [PRL 110, 254801]. Two non-commensurable detector families. |
| **Peak field** | B-route: PVLAS 2.5 T → BMV 6.5 T (XXL ∫B²L 100 T²m) → OVAL 9 T → VMB@CERN ~8.3 T × 15 m → magnet labs 37-200 T. E-route: `I` from `10²¹ → 10²⁴ W/cm²`; highest real focused field CoReLS `E ~ 9.1×10¹³ V/m`; ELI-Beamlines L4 design `E ~ 2.7×10¹⁴ V/m`. All ~7-9 orders below `E_yield = 1.13×10¹⁷ V/m` / `B_yield = 3.77×10⁸ T` — but the ratio is field-independent, so peak field never gates discrimination. |
| **Cavity finesse** | B-route tightly clustered `F ~ 4-7×10⁵`, all λ = 1064 nm (PVLAS / BMV / OVAL). E-route: NO Fabry-Perot — single-pass X-ray probe `z ~ 10 µm`, enhancement via dark-field crossed-polarizer + flip-photon yield. |
| **Dominant systematic** | B-route wall is universally MIRROR INTRINSIC BIREFRINGENCE (caps the whole lineage ~7× short of QED). E-route wall is finite X-ray polarimeter purity (perpendicular-mode scatter) + pump-probe overlap/jitter. |
| **Integration / duty** | PVLAS 100% DC duty (`T_max = 10⁶ s` target). BMV/OVAL pulsed (ms flat-top, capacitor-recharge-limited). E-route: HIBEF EuXFEL `27,000 pulses/s` but optical ReLaX gates `~1 shot/min`; ELI-ALPS HF 10 Hz (highest PW-class). |

## 4. Citation gaps + the coefficient-convention note

**Open citation gaps (flagged for a primary-paper fetch):**

1. BMV best ellipticity in `rad/√Hz` — only the `~4×10⁻⁹` limit + per-shot nulls `1.0-1.4×10⁻⁸ rad` sourced;
   primary BMV results-paper noise floor not fetched.
2. BMV dominant systematic budget (magnet-pulse mirror perturbation + residual-gas Cotton-Mouton) unsourced.
3. BMV total integration / shot-count for the published exclusion runs.
4. BMV operational peak field ambiguous (design 25 T vs operational 2.3-14 T); used 6.5 T (2014) + 10 T (XXL).
5. VMB@CERN committed peak field given only via `B²L ~ 1200 T²m` + secondary `~8.3-9.5 T`; needs the CERN
   proposal doc.
6. All PW lasers except HIBEF: birefringence-specific ellipticity floor / finesse / systematics
   unsourced-by-construction (field sources, no fielded polarimeter) — the dominant structural gap.
7. LUXE phase-0 live status as of 2026; E320 exact peak intensity (a₀ = 3-7, "~10²⁰ W/cm²" qualitative).
8. BIREF@HIBEF LoI exact HPLSE journal DOI (Cambridge Core article ID + arXiv:2405.18063 are solid).

**Coefficient-convention note (verified in-code, origin/main):** `(E_CRIT/E_YIELD)² = 1/α` EXACT;
`E_YIELD = 1.1304×10¹⁷ V/m`; `B_yield = 3.77×10⁸ T`. The field-independent ratio is `a_EH`-dependent, NOT a
single number: `4.14×10⁶` (7/45 single-mode), `9.65×10⁶` (3/45 differential), `4.42×10⁵` (PVLAS `A_e`
convention). The prompt's `−½A² + 7.5/α³ = 1.93×10⁷` is exactly 2× the code's differential ratio. Cite as a
**range `[4×10⁵, 2×10⁷]`**, not a point — physics verdict identical (`~10⁶-10⁷×` QED, field-independent).

---

### Provenance

Facility survey workflow `w14ptjz80` (4 sub-surveys: dedicated polarimetry / PW-laser / high-field-magnet,
+ synthesis). Numbers sourced & verified in-code against `src/ave/bench/birefringence.py` on origin/main.
Companions: FORK-1 resolution
[`2026-06-22_node-up-small-large-signal_result.md`](2026-06-22_node-up-small-large-signal_result.md)
(`clm-vca7r1`, the static-B-transparent result), PVLAS verdict leaf
[`pvlas-static-b-verdict.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md)
(`clm-pvlas1`), E-route coefficient leaf
[`vacuum-birefringence-e4.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md)
(`clm-pp3qwf`). Arc record:
[`_orchestration/2026-06-22_birefringence-vca-bench-arc.md`](../_orchestration/2026-06-22_birefringence-vca-bench-arc.md).
