# PREREG — FROZEN — Graded-region pulse reflection Γ(A) on the srs scalar TLM engine (means-test Class C)

**Status:** FROZEN at authoring. This document is written by a prereg-author agent
FIREWALLED from results: no run has been executed, no measured number appears here,
and the author will never see the run. The run agent executes this document verbatim;
any deviation is recorded as an amendment in the RESULT doc, never edited here.
**Date frozen:** 2026-08-24
**GO (Grant, verbatim, 2026-08-24):** "go on C" — ratifying the Class-C row of the
means-test register, `research/2026-08-24_ave-chart-instrument_note.md` §7 (line 151),
branch `infra/2026-08-24-ave-chart-instrument` (PR #1008): *"launch a pulse in the
in-tree scalar TLM engine at a REGION GRADED by the kernel; measure the reflected
amplitude vs grading level; overlay the measured Γ(A) on the three drawn forms ...
the J/B/taper fork's substrate adjudication: the lattice itself draws whichever locus
is real. A prereg (challenge-canonical-negative config-grep incl.) is owed before any run"*.
**Result lands as:** its own research pair (`..._result.md`) via reviewed PR, per the
Class-C row's lane spec (3-lens adversarial verify downstream of the run).

---

## §0 — SECTOR / REGIME / MODE DECLARATION (house table)

| Axis | Declaration |
|---|---|
| **MODE** | Numerical measurement: impose-and-probe scattering. A passive pulse is launched in a closed lattice and its reflection off an IMPOSED, STATIC, kernel-shaped grading is measured. Reflection-coefficient (Op3) observable, read in (V_inc, V_ref) TLM port coordinates (§4.4). |
| **SECTOR** | Scalar/translational (longitudinal V-sector) channel ONLY. Carrier: `srs-z3` — the D1-ratified production carrier (`build_srs_net`, `src/ave/core/chiral_lattice.py:206-232`). No charge/Cosserat-winding content, no T2/transverse content, no μ-sign-selector content (PR #260 discipline: rim language never says "magnetic wall"). |
| **ENGINE-DOF receipt** | The SCX Phase-0 requirements doc, `research/2026-08-24_solver-crosscheck-phase0_requirements.md:25`: *"the scalar/translational TLM channel is carried by `chiral_lattice.scalar_tlm_step` on `build_srs_net`"* — the engine carries the DOF under test. |
| **REGIME** | LINEAR probe on a statically graded medium. The scatter matrices depend on the imposed grading field A(x) and NOT on the propagating field V — dynamics are amplitude-independent by construction. Op14 dynamic saturation is OFF; the Axiom-4 kernel S(A)=√(1−A²) enters ONLY through the imposed impedance map (§4.2). |
| **PHASE-STATE** | Cold lattice everywhere except the FROZEN-IMPOSED grading region, A ∈ [0, 0.99]. The grading is imposed-and-probed: never self-consistent, never pumped, never evolving. Closed system, no drive after t=0, no loss terms. |
| **CLASS** | Response-map measurement (medium's Γ(A) map under each imposed grading geometry). Adjudicates the J/B/taper side-assignment fork per the substrate-adjudicates-forks discipline. Nothing minted; no canonical leaf edited by the run. |

**consistency-vs-emergence tag:** this is a **consistency/response-map** measurement of
the engine's own linear scattering off imposed gradings, compared against lumped-circuit
forms. It is NOT an emergence test, NOT a bound-state test, NOT a CODATA fit.

## §1 — BINDING SCOPE (from the annulus result's own scoping, PR #1007)

This test measures the **MEDIUM'S RESPONSE MAP** — the reflection of a probe pulse off
an imposed, static, kernel-shaped grading. It does **NOT** form, test, or claim anything
about the electron or any bound state. Canon pins the electron's A1 at √α; the annulus
is the response map, not an orbit; nothing in this run touches either. The following
conclusion-shapes are FORBIDDEN in the result doc regardless of what the run shows:

- "therefore a bound state / electron can (or cannot) form" — out of scope by construction;
- "therefore the energize-LOCK negative is explained away / reopened" (§3.1);
- "therefore an eigenmode exists / does not exist" (§3.2);
- any charge-sector, winding, or spin statement (§0 SECTOR).

The ONLY claims the run may produce: (i) the measured Γ(A) locus per imposed grading
geometry, (ii) the frozen qualitative classification of each locus (§6), (iii) the
resulting adjudication of the J/B/taper fork as response-map forms (§6.4).

## §2 — What is being adjudicated (the fork) and the comparison targets

The chart instrument draws three lumped-step forms of Γ(A)
(`src/ave/viz/ave_chart.py:117-161`, branch `infra/2026-08-24-ave-chart-instrument`),
all built on the shared canonical impedance map z(A) = √(S(A)), S(A) = √(1−A²)
(`cvr-reflection-smith.md` §2: Z_core = Z₀·√S):

| form | expression (rootS ≡ √S(A)) | endpoints | distinguishing lumped features |
|---|---|---|---|
| **core** | Γ = (rootS − 1)/(rootS + 1) | 0 → −1 | matched at A=0; monotone negative; no floor, no crossing |
| **J** (junction-side bias) | Γ = (rootS/2 − 1)/(rootS/2 + 1) | −1/3 → −1 | FLOOR at −1/3 (the bare z=3 vertex counting fact, `translation-circuit.md:189`); monotone negative; NO zero-crossing |
| **B** (bond-side bias) | Γ = (1/2 − rootS)/(1/2 + rootS) | −1/3 → +1 | FLOOR at −1/3; MATCHED CROSSING Γ=0 at rootS = 1/2, i.e. A* = √15/4 ≈ 0.96825 (`A_MATCHED_B`, `ave_chart.py:79`); endpoint +1 |
| **taper** (expectation, not a drawn form) | — | — | |Γ| SUPPRESSED relative to either step (adiabatic impedance ramp reflects less than any lumped step); no floor |

The J/B fork is the UNDERIVED-SIDE-ASSIGNMENT engineering choice tagged in the chart
note §6: which side of the junction the bias lands on. Grant's ratified Class-C row makes
the lattice itself the adjudicator. **Scoping inherited verbatim:** the −1/3 floor is the
bare/isolated/incoherent per-vertex reading; in-band collective carriers homogenize it
(~0.12 of the incoherent value, T4 fork close, `translation-circuit.md:189`). The
in-lattice measurement is a collective-carrier measurement, so the FLOOR VALUE is not
expected to survive quantitatively — §6 freezes what floor-existence means instead.

**Quantitative deviation from ALL lumped forms is EXPECTED and NOT adjudicating** (§6.5):
the engine is the in-lattice truth; the lumped forms are two-element circuit cartoons.
Adjudication is exclusively on the frozen qualitative signatures and endpoint behavior of §6.

## §3 — CONFIG-GREP (challenge-canonical-negative, MANDATORY)

Per the challenge-canonical-negative discipline: a new framing near a closed negative
must prove, at CONFIG level, that it does not reconstruct the closed path. Three closed
negatives live in this neighborhood. Side-by-side signatures:

### §3.1 — The energize-LOCK / keystone-pump closed negative (electron-genesis-from-free-precursor, LEANS-FALSIFIED, 3 escape hatches CLOSED)

Canonical statements of the closed path's config:
- `research/2026-06-24_engine-phase-space-winding_prereg.md:12`: *"NO external drive. This is the operational line between this test (winding-existence under lossless evolution) and the barred self-formation (which PUMPED `H` at `dt→0`)."*
- `research/2026-06-23_engine-stage2-native-cage_prereg.md:51-56`: *"We do NOT claim formation-from-free-precursor: that is the leaning-negative keystone-pump (the convergence-engine coupling pumps H at dt→0)."*

| config key | CLOSED energize-LOCK path | THIS test |
|---|---|---|
| initial state | FREE PRECURSOR seeded to self-form | a passive probe pulse; nothing seeded that could bind |
| drive / pump | convergence-engine coupling; H PUMPED; pump ramp; behavior probed in the dt→0 limit | ZERO drive for t>0; closed system; conservation is a run GATE (§5, CS-1/V2), not a casualty |
| dt→0 limit | load-bearing (the pump appears as dt→0) | DOES NOT EXIST here: the TLM step IS the discrete bond transit (scatter+connect, `chiral_lattice.py:294-300`); there is no tunable integrator dt, no limit taken |
| medium↔field coupling | SELF-CONSISTENT (field builds/modifies its own cage) | NONE: scatter matrices are PRECOMPUTED CONSTANTS from the frozen A(x); the step function has no A-update and no V-dependence of S (structural, §4.2; checksum-gated, V2) |
| claim scope | electron formation route | static linear response map of an imposed grading; formation claims FORBIDDEN (§1) |

**Structural proof of non-reconstruction:** genesis requires (precursor ∧ pump ∧
self-consistency). This config has NONE of the three conjuncts. A linear response map at
frozen grading cannot say anything about formation dynamics; §1 forbids the result doc
from drawing any formation conclusion in either direction. No escape hatch of the
energize-LOCK negative is touched, reopened, or "explained".

### §3.2 — #415 (static coupled eigensolve: bound eigenstate carrying both mass and winding DOES-NOT-EXIST)

Cited at `research/2026-07-01_electron-unifier-cocompress_prereg_FROZEN.md:22`.

| config key | #415 closed path | THIS test |
|---|---|---|
| operation | eigensolve of the coupled static operator | time-domain pulse scattering; NO eigensolve anywhere |
| object sought | bound eigenstate (mass + winding) | none — no bound-state search, no mode-existence claim |
| reconstruction risk | — | a reflection coefficient off an imposed slab cannot assert eigenmode existence; §1 forbids the conclusion-shape |

### §3.3 — #417 (phase-space winding reads the LC CARRIER RATIO, not topology)

Cited at `research/2026-07-08_electron-lock-barrier_prereg.md:15` (the detuning sweep:
"(2,3)" tracks ω_b:ω_s continuously; a topological integer cannot slide), banked from
`research/2026-06-24_engine-phase-space-winding_result.md:29`.

| config key | #417 closed path | THIS test |
|---|---|---|
| channels | TWO coupled carriers (ω_b, ω_s), phase-space winding readout | ONE scalar channel (`srs-z3` scalar per port); no second carrier exists in the machinery |
| observable | winding ratio (toroidal/poloidal turns) | signed reflection amplitude Γ; no winding, no ratio, no phase-space orbit |
| reconstruction risk | — | none of #417's observables are constructible from this run's data |

### §3.4 — Over-determination tell (the ½/¼ coincidence check)

No adjudication threshold in §6 is tuned to land on any closed negative's number. The
only privileged constants consumed are: −1/3 (a counting fact, `translation-circuit.md:189`),
√15/4 (Form-B algebra, `ave_chart.py:79`, used as a NON-BINDING report-against target only),
and 1/√3 (the cold network factor, a sanity GATE not an adjudicator). All thresholds in
§5/§6 are declared engineering choices with stated rationale.

## §4 — Measurement design

### §4.1 — Machinery (per the capability verdict)

- **Net:** `build_srs_net(L=16, enantiomorph="right")` — periodic srs, degree-3, girth-10,
  carrier `srs-z3` (`src/ave/core/chiral_lattice.py:206-232`). L=16 → 8·16³ = 32768 nodes.
  [ENGINEERING-CHOICE: L=16 — big enough for source/probe/slab/wrap-margin layout of §4.3;
  any L ≥ 12 satisfying the V3 timing budget is acceptable, recorded if changed.]
- **Step:** `chiral_lattice.scalar_tlm_step` (scatter+connect, closed system,
  `src/ave/core/chiral_lattice.py:294-300`) — the SCX-receipted carrier of the scalar channel.
- **Graded extension (minimal, declared here):** `scalar_tlm_step` applies ONE global S;
  `scatter_matrix(n, z_local)` is uniform-only (z_local reserved, `chiral_lattice.py:81-103`
  — verified at authoring). The run agent implements the standard unequal-admittance
  shunt-junction generalization of the SAME Op5/KCL derivation the uniform matrix quotes:
  per-port admittances Y_p ⇒ node voltage V = 2·(Σ_j Y_j V_j^inc)/(Σ_k Y_k) ⇒
  **S_ij = 2·Y_j/(Σ_k Y_k) − δ_ij** (per node), applied as V_ref[u] = S_u @ V_inc[u]; the
  CONNECT map is untouched. This is lossless under the line-power norm
  **E_Y = Σ_{u,p} Y_{b(u,p)}·V_inc[u,p]²** — conservation of E_Y is GATED (V2), not assumed.
  Regression gate CS-4: with all bonds cold (all Y = Y₀) the per-node path must reproduce
  the uniform-`scatter_matrix(3)` trajectory to ≤ 1e-12 max abs deviation over 200 steps.

### §4.2 — The imposed grading (FROZEN map, per-bond)

- Grading is a **per-BOND** scalar A_b (a bond has ONE impedance; both end-ports of a bond
  carry the same Y_b — enforced by construction, asserted at build time).
- **Canonical map (shared with the comparison forms, so the A-axis is common):**
  z_b = √(S(A_b)), S(A) = √(1−A²) exact/unclipped (as `ave_chart.saturation_kernel`);
  Y_b = Y₀/z_b. Cold bond: A_b = 0 ⇒ z_b = 1.
- The A-field is computed ONCE before t=0 from the config geometry (§4.3), the per-node
  S_u are precomputed, and a SHA-256 checksum of the stacked S_u array is taken at t=0 and
  re-verified at end-of-run (V2): the grading is FROZEN, never self-consistent, never pumped.

### §4.3 — Geometry, launch, and the three graded configurations

Propagation axis: x̂ (Cartesian axis 0). Interface plane x_I and slab of width W = 6 cells
[ENGINEERING-CHOICE], all coordinates in units of a_cell. Layout [ENGINEERING-CHOICE]:
source center x_s = x_I − 7; probe plane x_p = x_I − 3; slab back x_B = x_I + 6; wrap
margin ≥ 3 cells. Bond membership by endpoints/midpoint minimum-image x-coordinates.

- **Launch [ENGINEERING-CHOICE]:** baseband Gaussian plane pulse, directionally weighted:
  V_inc[u,p](t=0) = exp(−(x_u−x_s)²/(2σ_x²)) · max(0, +x̂·b̂_{u,p}), σ_x = 1.5 a_cell.
  No carrier tone (baseband ⇒ spectral content concentrated at small k; band-content
  gated at CS-2). Residual backward radiation is handled by windows + wrap sentinel (V3).
- **CONFIG G-J (far-side / junction-cell graded ~ FORM J analog):** A_b = A for every bond
  with BOTH endpoints in x_I < x < x_B; bonds crossing x_I stay cold. The incident wave
  arrives on a cold feed bond and sees graded far arms — the junction-side bias assignment.
- **CONFIG G-B (single-bond graded ~ FORM B analog):** A_b = A ONLY for bonds crossing
  x_I (one endpoint each side); everything else cold. The incident wave transits a biased
  bond against cold far arms — the bond-side bias assignment. DECLARED CAVEAT: in-lattice
  this is a thin (one-bond) biased layer, i.e. a two-interface composite; the lumped Form B
  is its single-interface cartoon. The B adjudication (§6) is therefore on the crossing/
  endpoint-sign signatures, which survive compositing, not on magnitudes.
- **CONFIG G-T (N-cell taper):** A_b = A · r(x_mid), with r linear 0→1 over
  [x_I, x_I + 3] and r = 1 on [x_I + 3, x_B] [ENGINEERING-CHOICE: N_taper = 3 cells,
  linear profile]. Same far-side load as G-J with an adiabatic entry — the taper-vs-step
  comparison partner of G-J.
- **Amplitude grid [ENGINEERING-CHOICE, chosen to resolve a possible crossing near
  A_MATCHED_B and the endpoint, not tuned to any negative]:**
  A ∈ {0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.925, 0.95, 0.9682, 0.98, 0.99}.
  A = 0.0 is the null-calibration point (grading identically absent ⇒ the config IS the
  cold lattice; it defines the noise floor ε₀, §5 CS-5). 16 points × 3 configs = 48 runs.

### §4.4 — Γ extraction (DECLARED; phase-space-coordinate-check)

**Coordinate map (explicit).** The TLM node variables ARE the chart's phasor coordinates:
`V_inc[u,p]` is the incident-wave amplitude arriving at node u on port p; the scattered
wave is V_ref = S_u V_inc. On a probe bond (u₋, u₊) crossing x_p (u₋ on the source side),
after CONNECT the port variable at u₊ facing u₋ carries the **forward** (+x̂) wave and the
port variable at u₋ facing u₊ carries the **backward** (−x̂) wave. This directional
decomposition on the bond cross-section is exactly Op3's (V_inc, V_ref) split; Γ = V_ref/V_inc
on that cross-section. No real-space field amplitude is used as a proxy for a phase-space
quantity — the port variables are read directly.

- **Records:** F(t) = Σ_{probe bonds} V_inc[u₊, p(u₊←u₋)] and B(t) = Σ_{probe bonds}
  V_inc[u₋, p(u₋←u₊)], each summed over the probe-plane bond set every step.
- **Windows:** DERIVED from the cold run, not assumed: the incident window brackets the
  measured F-pulse transit of the cold (A=0) run of the same config geometry; the reflected
  window opens after the incident window closes and closes before the earliest contaminant
  arrival (slab-back-face first return for G-J/G-T computed from measured graded transit
  times, and the V3 wrap budget), with a declared guard margin of 2σ_t on each edge
  [ENGINEERING-CHOICE], σ_t = measured cold pulse temporal sigma at the probe. For G-J/G-T
  the extraction targets the FIRST (front-face / distributed-taper) reflection only —
  the lumped comparison forms are single-interface objects.
- **Primary signed estimator (matched filter):** Γ_meas = (Σ_t B(t)·F(t−τ*)) / (Σ_t F(t−τ*)²)
  over the reflected window, τ* = argmax over lag of |cross-correlation(B, F)|. Sign
  convention: Γ < 0 = polarity-inverted echo (short-like, toward −1 rim); Γ > 0 =
  same-polarity echo (open-like, toward +1 rim) — matching Γ = (z−1)/(z+1).
- **Secondary unsigned cross-check:** |Γ|_E = √(E_B/E_F) with E = Σ_t (·)² over the
  respective windows. Discordance |(|Γ_meas| − |Γ|_E)| / max(|Γ|_E, θ) > 0.2 at a grid
  point marks the point UNRELIABLE; > 4 unreliable points in one config ⇒ that config is
  INVALID-EXTRACTION (no adjudication for it; reported as such) [ENGINEERING-CHOICE: 0.2, 4].

## §5 — Cold sanity gate (FIRST; the run is VOID if it fails)

Run BEFORE any graded configuration, on the exact net + launch of §4:

- **CS-1 (closed-system conservation, cold):** uniform `scatter_matrix(3)`, seeded pulse;
  max relative energy drift over 200 steps < 1e-10 — the banked smoke gate
  (`src/tests/test_chiral_lattice_smokes.py::test_smoke_a_energy_conservation`).
- **CS-2 (velocity vs the frozen receipt + band edge):** `measure_dispersion`
  (`src/ave/core/chiral_lattice_dynamics.py`) on the run's net, m = 1..4: the extracted
  network factor c/c_link at the smallest k must match **ANALYTIC_NETWORK_FACTOR = 1/√3
  = 0.5773502691896258** (`chiral_lattice_dynamics.py:43-48`; SCX requirements row
  `research/2026-08-24_solver-crosscheck-phase0_requirements.md:98`) within 2 %
  [ENGINEERING-CHOICE]. Band edge: ≥ 95 % of the launched pulse's spectral energy must lie
  in the k-band where measured c(k) deviates < 5 % from the small-k value
  [ENGINEERING-CHOICE] — the probe must live in the linear/long-wavelength band.
- **CS-3 (time-of-flight cross-check):** the cold pulse centroid velocity source→probe
  must match the CS-2 small-k velocity within 5 % [ENGINEERING-CHOICE] — ties the
  dispersion receipt to the actual probe pulse.
- **CS-4 (graded-path regression):** per-node-S machinery with ALL bonds cold reproduces
  the uniform-S trajectory to ≤ 1e-12 max abs deviation over 200 steps.
- **CS-5 (null calibration):** for each of the three config geometries at A = 0, the full
  extraction pipeline (§4.4) must return |Γ| < 0.02 [ENGINEERING-CHOICE]; define the noise
  floor ε₀ = max over the three configs of these A=0 readings, and the adjudication
  threshold **θ = max(3·ε₀, 0.05)** [ENGINEERING-CHOICE].

**Any CS failure ⇒ the ENTIRE run is VOID** (V1). No graded data may be interpreted.

## §6 — FROZEN EXPECTATIONS and ADJUDICATION RULES

### §6.1 — Lumped-form qualitative signatures (the comparison targets, restated frozen)

- **FORM J:** floor near −1/3 at A→0; signed Γ monotone decreasing; NO zero-crossing;
  endpoint sign NEGATIVE (→ −1).
- **FORM B:** floor near −1/3 at A→0; ONE zero-crossing, direction − → +, at some A*
  (lumped algebra puts it at √15/4 ≈ 0.96825 — reported-against, NON-BINDING); endpoint
  sign POSITIVE (→ +1).
- **TAPER:** |Γ| suppressed relative to both stepped configs; no floor; no crossing.
- **CORE (baseline shape):** no floor; no crossing; negative; monotone.

**Floor honesty note (frozen before any run):** at A = 0 every config IS the cold lattice,
so Γ_meas(0) ≡ 0 up to noise — the lumped forms' literal −1/3 intercept belongs to the
ISOLATED vertex, which does not exist in-lattice (T4 homogenization scoping, §2). The
floor signature is therefore tested as an EXTRAPOLATED intercept (§6.2 FLOOR), and a
NO-FLOOR reading is a foreseen, recorded outcome that demotes J/B to their floorless
variants rather than a NONE by itself.

### §6.2 — Frozen classifiers (computed per stepped config from the valid grid points)

With θ from CS-5 and per-point noise band δ = max(ε₀, 0.01) [ENGINEERING-CHOICE]:

- **SIGN_top:** sign of Γ_meas at the highest valid grid point (A = 0.99).
- **CROSSING:** exists adjacent valid grid pair with opposite signs, BOTH |Γ_meas| > θ;
  direction recorded (−→+ or +→−); count recorded.
- **FLOOR:** linear fit of signed Γ_meas over the valid points with 0 < A ≤ 0.5
  extrapolates to |intercept at A=0| > θ (the A=0 point itself is excluded — identically cold).
- **MONOTONE:** signed Γ_meas monotone across valid points within ±δ.
- **TAPER-SUPPRESSED:** |Γ_GT(A)| < ½·|Γ_GJ(A)| [ENGINEERING-CHOICE: factor ½] at EVERY
  grid A ∈ [0.5, 0.9] where |Γ_GJ(A)| > θ.

### §6.3 — What counts as the lattice "drawing" each form

- **G-J draws J-class** iff: no CROSSING ∧ SIGN_top = − ∧ MONOTONE. With FLOOR ⇒ full
  Form-J signature; without FLOOR ⇒ "floorless negative (core/J-class) locus" — the
  side-assignment content of J (graded far arms ⇒ deepening negative echo, never a
  polarity flip) is still drawn; the floor verdict is recorded separately.
- **G-B draws B-class** iff: exactly ONE CROSSING with direction − → + ∧ SIGN_top = +.
  Measured A* reported against √15/4 (non-binding).
- **G-T draws the taper expectation** iff: TAPER-SUPPRESSED ∧ no FLOOR ∧ no CROSSING in G-T.
- **NONE-OF-THE-THREE (per config)** iff any of: a + → − crossing; multiple crossings;
  SIGN_top = + without a crossing; positive Γ_meas > θ at any A ≤ 0.5; non-monotone
  beyond ±δ (stepped configs); for G-T, ANY band point with |Γ_GT| ≥ |Γ_GJ| > θ.
  A NONE verdict means the lattice drew a locus none of the lumped cartoons describe:
  the measured locus itself is the result, reported without a lumped label.

### §6.4 — Fork adjudication (frozen outcome table)

The J/B fork is a side-assignment question: each form claims to be the response map of
its own bias geometry. Therefore:

| outcome | verdict on the fork |
|---|---|
| G-J draws J-class AND G-B draws B-class | BOTH forms validated as maps of their own geometries; the "fork" dissolves — side-assignment is a physical-geometry choice, and the chart may keep drawing both forms with the geometry label attached |
| G-J draws J-class, G-B = NONE (or vice versa) | the NONE-side lumped form is REFUTED as the response map of its geometry; only the surviving form remains drawable as physics (the other demotes to cartoon-with-caveat) |
| both stepped configs draw the SAME class | the side-assignment is DEGENERATE at response-map level; recorded, chart forms demote to a single locus |
| both NONE | both lumped constructions refuted in-lattice; the measured loci replace them |
| G-T fails taper suppression | the taper expectation is REFUTED (a qualitative surprise; reported prominently — an adiabatic ramp reflecting ≥ a step is a real finding about the graded medium) |

### §6.5 — Explicit non-adjudicators

Quantitative deviation from all lumped curves is EXPECTED (bulk collective carriers,
girth-10 srs geometry, discrete bonds, thin-layer compositing in G-B) and adjudicates
NOTHING. The floor VALUE −1/3 and the crossing LOCATION √15/4 are report-against numbers,
never pass/fail. The overlay figure (measured points on the three drawn forms) is
published for the record in the result doc regardless of verdicts.

## §7 — Engineering-choice register (every non-lattice-derived parameter)

| # | parameter | value | tag rationale |
|---|---|---|---|
| E1 | L = 16 cells | layout + wrap budget | not lattice-derived; any L ≥ 12 passing V3 acceptable |
| E2 | slab width W = 6, taper N_t = 3 (linear), layout x_s/x_p/x_I offsets 7/3 | geometry | imposed-probe geometry, not substrate-derived |
| E3 | pulse: baseband Gaussian, σ_x = 1.5 a_cell, directional weighting max(0, x̂·b̂) | launch | probe design; band-content gated at CS-2 |
| E4 | A-grid (16 points, §4.3) | sweep resolution | dense near possible crossing + endpoint; not tuned to any negative (§3.4) |
| E5 | run length: until reflected windows close (from measured TOF) + margins; hard cap 6000 steps | budget | timing derived from cold measurements, cap is engineering |
| E6 | window guard margins 2σ_t; matched-filter estimator; discordance 0.2 / 4 points | extraction | declared estimator; cross-checked |
| E7 | gate tolerances: 2 % (CS-2), 5 % (CS-2 band / CS-3), 1e-10 / 1e-12 / 1e-8 drifts, ε₀ cap 0.02, θ = max(3ε₀, 0.05), δ = max(ε₀, 0.01), taper factor ½, band [0.5, 0.9] | thresholds | all declared pre-run; none tuned to closed negatives |
| E8 | enantiomorph "right" | build choice | scalar channel is achiral in Phase-0 receipts; choice immaterial, recorded |
| E9 | impedance map z_b = √S(A_b) | SHARED canonical map (`cvr-reflection-smith.md` §2 via `ave_chart.py`) | NOT an engineering choice on the comparison axis — it is the frozen common A-parametrization of both sides; flagged here so nobody mistakes the test as adjudicating the map's exponent (it does not; it adjudicates geometry/side-assignment at fixed map) |

## §8 — VOID conditions (the run is null and interprets NOTHING)

- **V1 — Cold sanity fail:** any CS-1..CS-5 failure (§5).
- **V2 — Grading leaks into dynamics:** E_Y (the Y-weighted norm, §4.1) relative drift
  ≥ 1e-8 in any graded run; OR the t=0 SHA-256 checksum of the stacked per-node S array
  fails re-verification at end-of-run; OR CS-4 regression fails. (A structural-null lens
  is owed here in reverse: the gate confirms the grading is IN the dynamics as a static
  scatterer and ONLY as a static scatterer.)
- **V3 — Wrap-around / contamination:** sentinel monitors (field magnitude at the
  wrap-margin plane opposite the source) show a contaminant front arriving inside ANY
  extraction window; windows must be constructible with positive width under the measured
  timing budget — if not constructible, VOID, and the geometry (E1/E2) must be re-frozen
  in an amended prereg before any re-run.
- **V4 — Window overlap:** incident and reflected windows overlap at the probe for any
  config (pulse too wide for the geometry).
- Per-config **INVALID-EXTRACTION** (§4.4 discordance) voids that config's adjudication
  only; the run survives for the other configs.

## §9 — Reporting requirements (binding on the run agent)

1. RESULT doc = this prereg's pair: verbatim gate outcomes with numbers, the 48-point
   Γ_meas table (signed, both estimators, per-point valid/unreliable flags), classifier
   outputs (§6.2), verdicts strictly via §6.3/§6.4 tables, overlay figure
   (white-background house style via `ave.viz.style.apply`, Okabe-Ito, honest axes).
2. Any deviation from this document is an AMENDMENT logged in the result doc with its own
   dated entry; the prereg file itself is never edited.
3. The §1 forbidden-conclusion list is restated in the result doc's scope block.
4. Adversarial verify (3-lens, per the Class-C row's lane spec) happens AFTER the result
   doc is drafted; verdict language stays frozen-criterion-only until then.

— END OF FROZEN PREREG —
