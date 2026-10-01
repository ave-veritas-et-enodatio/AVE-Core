# Engine-driven production visuals

Engine-driven visuals for the SVE (structured-vacuum electrodynamics) programme:
two full-production interactive scenes (Visuals 1 and 2) and two internal-review videos (Visuals 3 and 4). Each is produced by a **Python engine driver** under
`src/scripts/viz/` that exports a scene/data JSON, consumed by a **self-contained
interactive HTML** (vanilla `<canvas>`, no external JS) plus **static renders**
in the house figure style (`ave.viz.style`, white background, Okabe-Ito).
Visuals 3 and 4 are internal-review **videos**: their drivers render an MP4 directly
from the engine arrays, plus key-frame stills. Visual 4 is also **scored**: every
pattern it shows is compared, with no fitted parameters, against a converged reference solver.

Every element is tagged **engine-exact** (computed by the canonical machinery) or
**stylized** (presentation-layer geometry / exaggeration for legibility). The
ledger below is the load-bearing honesty record — see each visual's section.

Naming note: user-facing text uses the neutral public name **SVE**
(structured-vacuum electrodynamics); internal framework names are not exposed in
any text that may travel with a paper or outreach material.

---

## Visual 1 — "The electron in the vacuum lattice"

Directory: `viz/electron_lattice/`
Driver: `src/scripts/viz/electron_lattice_scene.py`

The real chiral **srs** net (degree-3, I4₁32, `chiral_lattice.build_srs_net`)
carrying the seeded **(2,3) winding** (`srs_cage_winding`), node colours from the
canonical **S(A) saturation kernel** at the winding's amplitude field, and the
**meridian loop** — the Δb1=+1 harmonic generator of the punctured complex
(`srs_dec_punctured`), rendered as an actual cycle of srs nodes that links the
winding core exactly once (linking number verified = 1).

### Provenance ledger (Visual 1)

| Element | Engine-exact? | Source |
|---|---|---|
| srs node positions (z=3, chiral) | ENGINE-EXACT | `ave.core.chiral_lattice.build_srs_net` |
| bonds (z=3 connect-map) | ENGINE-EXACT | `LatticeNet.neighbors` |
| ω winding field (2,3) | ENGINE-EXACT | `srs_cage_winding.seed_pq_winding_on_srs` |
| Q_link = 3, w_tor = 2 | ENGINE-EXACT (verified by reader) | `compute_Q_link_srs` |
| node colour S(A) | ENGINE-EXACT | `graded_vacuum_network.saturation_kernel` |
| amplitude field A = \|ω\| / A_yield | ENGINE-EXACT | from seeded ω magnitude |
| meridian loop node-path (Δb1=+1) | ENGINE-EXACT | `srs_dec_punctured` + graph-cycle, linking=1 |
| 3D → 2D projection, camera, drag | STYLIZED | client-side canvas presentation |
| amplitude slider re-scale of A | ENGINE-EXACT FORM | client re-evaluates S=(1−A²)^p |

## Visual 2 — "The HIBEF moment"

Directory: `viz/hibef_moment/`
Driver: `src/scripts/viz/hibef_moment_scene.py`

Pump-probe polarization walk-off at HIBEF's demonstrated ReLaX pump. The pump
envelope shows the S(A) kernel at the real A² = 5.9e-7 (amplitude exaggerated ×N
for visibility, honestly labelled); the two X-ray probe polarization components
accumulate the **real relative phase** Δφ from the GAP-1 feasibility driver; the
polarization-flip meter reads the SVE prediction against the QED co-prediction.

### Provenance ledger (Visual 2)

| Element | Engine-exact? | Source |
|---|---|---|
| A² = 5.9e-7 at demonstrated pump | ENGINE-EXACT (driver number) | `birefringence_gap1_hibef_feasibility` |
| Δφ, Δφ/2 (per probe energy) | ENGINE-EXACT (driver number) | GAP-1 `hibef_point` |
| flip-prob P = sin²(Δφ/2) | ENGINE-EXACT (driver number) | GAP-1 `flip_prob_exact` |
| QED co-prediction Δφ, P | ENGINE-EXACT (driver number) | GAP-1 QED leg |
| S(A) pump-stripe colour | ENGINE-EXACT FORM | `saturation_kernel` |
| ×N amplitude exaggeration | STYLIZED (labelled) | presentation only |
| stripe motion / probe animation | STYLIZED | presentation-layer time axis |

## Visual 3 — "The lattice vs. the projected strain" (internal-review video)

Directory: `viz/lattice_vs_projected_strain/`
Driver: `src/scripts/viz/lattice_vs_projected_strain.py`

A 70-second MP4 that draws picture-lock P1 — `research/2026-08-29_overbraced-crystal-picture-lock.md:27`,
*"Observed / “projected” strain is the AC readout (and the real-space envelope"* S(A(r))) — with the
engine's own state (in this cold run S(A) = 1, so the envelope is flat). A voltage bump is released in a periodic box of 110,592 tanks on the chiral **srs** net (degree 3, I4₁32) and run by the
**Op5 scatter–connect** step with optical activity OFF (the κ=0 channel acceptance test T1.1 runs).
Scenes: the lattice itself; every tank's own voltage; the same state smoothed for display, plus a
smoothing-width sweep; the AC readout at two single tanks; one tank's (V_inc, V_ref) chart; a
provenance card.

**What it is not.** The picture it draws (P1) is Grant-agreed in chat, walk-grade, unaudited (the
`SIGNED` stamp still on main would be demoted by the open, currently blocked, correction PR #1036). The
video visualizes certified engine behaviour and tests nothing: any energy-conserving network with these
junctions and lines draws the same movie (`manuscript/ave-kb/common/claim-quality.md:1382`, *"AC agreement cannot distinguish"*).

**Internal-review build.** On-frame text carries corpus ids (def- ids, file:line cites, Op5) so every caption traces to
its source. A public cut must strip them (naming note above).

### Provenance ledger (Visual 3)

| Element | Engine-exact? | Source |
|---|---|---|
| srs node positions, bonds, degree 3 | ENGINE-EXACT | `ave.core.chiral_lattice.build_srs_net` |
| shortest ring = 10 bonds, writhe −0.041 (mirror net +0.041) | ENGINE-EXACT | `shortest_ring` + `ring_writhe`, both enantiomorphs |
| dynamics (every frame of scenes 2–5) | ENGINE-EXACT | `chiral_lattice_vector.vector_tlm_step`, S = (2/3)J − I |
| tank voltage V_i = (2/3) Σ_p V_inc | ENGINE-EXACT (Op5 shunt node) | the port-sum, which canon names the A1 grade (vocabulary-register common-mode flag, sense d) |
| per-port chart (V_inc, V_ref = S·V_inc) | ENGINE-EXACT | the photon-port pair — `research/2026-09-04_s9-tank-state-chart-join_WALK.md:17`, *"photon-port pair"* |
| AC readout traces | ENGINE-EXACT (raw single-tank voltages) | `lvps_meta.json` readout nodes |
| readout lag (18 / 19 steps) | ENGINE-DERIVED estimate | peak-to-peak and cross-correlation; the two tanks' placement is a display choice |
| run length, 47 steps | ENGINE-DERIVED | set by the wrap guard: step 48 is the first above 1e-3 against a 32-cell box |
| 3b retention numbers (83% / 45%) | ENGINE-DERIVED | smoothed lobe peak ÷ the tanks' own 3D shell mean, at exact window widths; `sweep_receipts` in `lvps_meta.json` |
| voltage-bump seed, σ = 1.5 ℓ_node, all ports equal | DISPLAY CHOICE | zero port current at t = 0 |
| smoothed panel (Gaussian window σ = 1.5 ℓ_node; swept 0.4–3.5) | DISPLAY CHOICE — an illustration | not "the projected strain"; canon's continuum field is the band-limited reconstruction of the samples, `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md:12`, *"can be reconstructed uniquely"* |
| slab \|x\| < 0.75 ℓ_node, per-step colour scaling, 3D camera, tank placement, radial subsample | DISPLAY CHOICE | presentation |

### Caption audit (2026-09-29)

An `ave-auditor` pass checked every on-frame claim against canon before the encode. Applied:

* "Projected strain" is the AC readout (P1), not the smoothing. The word "probe" was dropped from on-frame text: it
  re-imports the framing the picture-lock's Round 3 corrected — `research/2026-08-29_overbraced-crystal-picture-lock.md:190`,
  *"matter/light were probes"*.
* The colour is **node voltage, a stress** under the impedance analogy (`def-1mpanl`), never labelled
  strain. Whether a node's voltage is the compression itself or the integral of compression current
  flowing in is open — `research/2026-08-12_common-mode-continuum-image_derivation.md:464`,
  *"At a vacuum node, is the node voltage the"*.
* No T2 label on the displayed channel: it is the port-sum grade, inside an engine labelled
  transverse-only.
* "The node never moves" became "the graph stays fixed": nodes carry translational DOF —
  `manuscript/common_equations/eq_axiom_1.tex:37`, *"every node a native LC oscillator"*, in a Cosserat
  micropolar crystal.
* Scoped words: "energy conserved in this closed box", not a bare "lossless"; the colour-bar zero is the
  quiescent level.

Second pass (2026-09-30), on the repaired payload. Applied:

* "Charged bump" became "voltage bump". In canon, charge belongs to the micro-rotation winding sector —
  `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`,
  *"charge = Beltrami helicity"* — not to an A1 port-sum voltage.
* P1 is quoted whole, including *"and the real-space envelope"* S(A(r)).
* Bare "lossless" removed from the caution line ("any energy-conserving network").
* The 3b retention numbers are computed in the engine pass at exact widths and written to
  `lvps_meta.json`, with the reference named.
* The wrap guard covers every displayed node (slab, radial-panel sphere, smoothing input), not only the slab.
* Scene 5 marks the displayed channel's sector as open (port-sum grade vs. the photon-port form of the chart).

Third pass (2026-09-30): CLEARED. Its two recommendations are applied: the intro says each bond channel is
*modelled* as a transmission line (`manuscript/ave-kb/common/vocabulary-register.md:958`, *"MODEL-OF,
REGIME-SCOPED"*), and the driver's default encode (`--crf 25`) now reproduces the tracked MP4.

## Visual 4 — "Two slits in the srs lattice" (internal-review video, scored)

Directory: `viz/two_slits_srs/`
Driver: `src/scripts/viz/two_slits_srs.py`

A 67-second MP4. A plane-wave packet in the engine's T1.1 channel (κ = 0; "photon on srs" is the acceptance
test's name, not a sector claim) runs into a screen cut into the chiral **srs** net: every bond crossing the wall
plane outside two slits is shorted at its midpoint. The slab is two cells thick along the slits (periodic there) and
2,962,176 tanks in all; the step is the **Op5 scatter–connect** operator. Scenes: the set-up and the actual tanks at a slit
edge; the wave crossing the lattice with the screen dose piling up; the screen pattern against a converged reference;
the far-field (lens) pattern; the placement sweep; a provenance card.

**Regime and sector.** Cold and linear (no saturation kernel in the loop, so S(A) = 1), one of the two polarization
components, optical activity off. Shown: the port-sum tank voltage, canon's A₁ grade; its physical sector is open, as
in Visual 3. Each bond's transmission-line description is MODEL-OF, regime-scoped
(`manuscript/ave-kb/common/vocabulary-register.md:958`); ωτ = 0.11 here.

**What it shows, in one paragraph.**
- **Far field:** the srs lattice's two-slit field matches the 2D wave equation. The far-field (lens) minima sit
  within 0.70 % of a converged reference's at every one of 16 slit placements at λ = 32 ℓ_node.
- **Near field:** a screen 15 λ behind the slits shows how coarse the bond-cut slit edges still are. At λ = 32 ℓ_node
  the worst fringe extremum sits 0.77–4.05 % (single frequency), 1.08–4.67 % (dose) inside the reference's, depending on
  where the slit edges fall in the crystal. The 2 % bar is met at 8 of 16 placements; the video's own
  placement meets the bar.
- **At λ = 16 ℓ_node:** the near field meets the bar at 0 of 16 placements.
- **What a full pass would cost:** a two-point power-law extrapolation of the worst case suggests λ ≈ 73
  ℓ_node (single frequency) to 112 ℓ_node (dose). That is not run.

**Accuracy is the point of this one, so every pattern is scored, with no fitted parameters:**

* **Near field** (screen 15 λ behind the slits, inside the lattice): against a converged solution of the 2D scalar
  wave equation with a Dirichlet screen, same geometry, solved by independent leapfrog code (no engine import) at
  128 points per wavelength on a grid aligned with the slit edges. Halving its resolution moves the extrema by
  ≤ 0.28 % (single frequency), ≤ 0.34 % (dose).
* **Far field** (what a lens shows at its focal plane): the angular spectrum of the lattice's own field 2 λ past the
  wall, against the reference's far field. The textbook minima sin θ = (m + ½) λ/d are exact only for uncoupled slits
  with symmetric apertures; the reference itself sits up to 0.46 % off them here.

### The bar, and how it changed (disclosed)

The bar was set before the first run of this geometry, on 2026-09-30. It was first written in the scratch probe
that ran it (not committed): fringe extrema in the central lobe within 2 % of Rayleigh–Sommerfeld (Kirchhoff)
diffraction; central visibility ≥ 0.95; energy closes.

The first wide-slit run (a scratch probe, not in this PR: λ = 16 ℓ_node, broadband dose) failed it: 9.3 % and 0.81.
Earlier that day, narrow-slit probes (slits 4 ℓ_node wide, λ = 8–16 ℓ_node) had come before the choice of this
geometry; they were compared only against a geometric forward prediction and never scored.

Diagnosis, all measured. Items 1–3 are scratch-probe numbers, not reproduced by this driver:

1. **My boundary leaked.** The graded absorber let about 8 % of the amplitude wrap around the periodic box and
   re-enter. That figure is estimated from the absorber profile; the single-frequency readout still changed by
   7.8 % late in the run. Fix: the y/z periodic-wrap bonds are dropped (a matched edge), with thicker layers. After
   the fix the lock-in converges to 3e-05 and energy closes to 1e-13.
2. **The reference was wrong for this geometry.** Kirchhoff (uniform aperture illumination) is itself 1.8–4.8 % off the
   converged solution for 2 λ slits at 15 λ, at the 6 extrema it matches; 2 more have no Kirchhoff partner.
   So no correct simulation could pass that bar.
3. **The visibility bar was a far-field number.** In this near-field geometry the reference's central visibility
   is 0.897. The two slits see each screen point at different angles, where each slit's own pattern has a
   different strength; distance differences alone would give 0.9998.
4. **What remained resolves with λ/ℓ_node, slowly.**
   - The driver makes the slits by shorting bonds, so their edges are only as sharp as the bonds.
   - The lattice's long-wave dispersion is also slightly anisotropic (|Δk|/k ≤ 0.34 % at λ = 16 ℓ_node,
     0.08 % at 32; Bloch), which adds phase at oblique angles over the 15 λ path.
   - The split between the two is not separately receipted.
5. **The first λ = 32 PASS did not survive audit.** It rested on a sweep that moved only the wall plane. An auditor's
   test at λ = 24 moved the slit pair along y and raised the worst error by up to 40 %. The committed sweep now moves
   both. At λ = 32 the worst error rose from 1.6 % to 4.7 % (dose), and the bar is met at 8 of
   16 placements, not all of them.

Restated bar: the same 2 % threshold, measured against the converged reference instead of Kirchhoff, and applied to
both readouts (dose and single frequency). Near-field visibility must sit within 2 % of the reference's value
instead of ≥ 0.95. The original ≥ 0.95 is kept for the far field, where it belongs. Energy must close. The restated
bar was adopted after the λ = 16 diagnosis and before any λ = 32 run, and this README is its first written form.
Treat it as a disclosed post-hoc correction, not a pre-registration.

### Scores (from ts_meta.json)

Each λ is run at 16 placements: the wall plane at 4 positions in the cubic cell × the slit pair offset along y by 0,
1/8, 1/4 and 3/8 of the cell.
- The 4 wall-plane positions are exhaustive, because the set of cut bonds changes only when the plane crosses a
  node layer.
- An offset of 1/2 would repeat 0.
- Pairs of placements related by the crystal's symmetry give identical scores.

| | λ = 16 ℓ_node (slit = 32 bonds) | λ = 32 ℓ_node (slit = 64 bonds; this video) |
|---|---|---|
| near field, worst extremum vs reference, single frequency | 2.48–7.35 % | 0.77–4.05 % |
| near field, worst extremum vs reference, time-integrated dose | 3.15–7.48 % | 1.08–4.67 % |
| near field, placements meeting the 2 % bar (both readouts) | 0 of 16 | 8 of 16 |
| near field, worst central visibility vs reference's | 0.859 vs 0.897 (-4.3 %) | 0.885 vs 0.897 (-1.3 %) |
| far field, worst lattice minimum vs the reference's | 2.30 % | 0.70 % |
| far field, deepest-to-shallowest minima (peak = 1) | ≤ 9e-04 | ≤ 4e-04 |
| verdict against the restated bar | FAIL: near-field fringes miss at 16 of 16; near-field visibility at 7 of 16; far-field minima at 2 of 16 (other criteria pass) | FAIL: near-field fringes miss at 8 of 16 (other criteria pass) |

**The video's own placement.** The wall plane sits at cell fraction 0.53, which cuts the same bonds as the 0.50
placement, with no slit offset. Its worst extremum is 1.07 % (single frequency) and 1.30 % (dose):
it meets the bar. It is the driver's default geometry, not a chosen best case.

**Notes on the scores.**
- 742 of 755 near-field extremum errors point inward, toward the axis.
- In 24 comparisons a reference extremum had no lattice extremum of the same type within 0.45 λ; these are counted,
  not scored.
- The reference dose is read at exactly D = 15 λ, while the lattice screens sit within 0.01 λ of it (effect ≤ 0.08 %,
  audit round 1).
- The single-slit row from the first version is gone: it was outside the bar.

### Provenance ledger (Visual 4)

| Element | Grade | Source |
|---|---|---|
| srs slab geometry, degree 3, bond length 1 ℓ_node | ENGINE-EXACT | `chiral_lattice.srs_motif` + `_build_net_from_points` (the `build_srs_net` builder with a non-cubic box); degree, permutation and bond length asserted |
| dynamics | ENGINE-EXACT | one shared step function, `tlm_step`, which the run loop calls; it matches `chiral_lattice_vector.vector_tlm_step` bit for bit (receipt: max \|Δ\| = 0 (exact) after 50 steps) |
| tank voltage V_i = (2/3) Σ_p V_inc | ENGINE-EXACT | the port-sum; canon names it the A1 grade (vocabulary-register common-mode flag, sense d) |
| carrier / lock-in frequency ω₀ = 0.113332 rad/step | ENGINE-EXACT | Bloch one-step operator U(k) on a 2-cell srs supercell; the Grover relation cos ω = μ_max gives the same value (an identity check: equal by theorem). Flat bands are 33% of port states (also a theorem for degree 3) |
| incident wavenumber | ENGINE-DERIVED | read off the free run's field: 0.99999 k₀ |
| the screen (shorted bonds) | BOUNDARY, driver-added | −1 at each short by construction. Measured normal-incidence reflection -0.995-0.031i; its phase (0.031 rad) matches the short plane sitting -0.082 ℓ_node from the nominal wall (2kδ = 0.032 rad) |
| absorbing layers + matched edges | BOUNDARY, driver-added | graded loss exp(−0.1·depth³) per step over 6 λ; y/z periodic-wrap bonds dropped |
| converged reference | REFERENCE | independent leapfrog solver of the 2D scalar wave equation; see the convergence numbers above |
| screen readout (local quadratic regression, 1.5 ℓ_node) | DISPLAY + MEASURED | applied to the reference sampled at each λ's own screen tanks, biased by ≤ 0.17 % (λ = 16), ≤ 0.05 % (λ = 32) |
| far-field transform | ENGINE-DERIVED | Fourier transform of the single-frequency field 2 λ past the wall; free propagation beyond that plane assumed (lattice \|k\| varies ≤ 0.08 % with direction at λ = 32, Bloch) |
| geometry (w = 2 λ, d = 8 λ, D = 15 λ, λ = 32 ℓ_node), packet σ = 3 λ, colour range, smoothing σ = λ/20, inset window | DISPLAY CHOICE | presentation |

**Other receipts in `ts_meta.json`.**
- 17% of the seed's energy never leaves the box. 98.7% of that stays within ±3σ of where the seed
  started, and only 0.02% of it shows in the tank-voltage readout.
- That matches the lattice's flat bands (zero group velocity and zero port-sum), identified by those properties, not
  by projection onto them.
- 99.7% of the screen signal lies within ±15 % of ω₀. Below ω₀/2 the screen sees ≤ 1e-06 of its signal
  power, in the 24 placement runs that record it.

**What it is not.**
- It is a consistency check, not a discriminator. Any medium whose long waves obey the wave equation draws these
  fringes (`manuscript/ave-kb/common/claim-quality.md:1382`, *"AC agreement cannot distinguish"*; Hertz's razor,
  `manuscript/ave-kb/common/physics-lineage-map.md:534`).
- It is wave-only. The moving-defect double slit (a self-transported particle through one slit, its wake through
  both) returned ENGINE-GAP at its transport gate (`src/scripts/vol_1_foundations/moving_defect_transport_gate.py:8`).
  That sim *"must EARN its interference, not assume it"* (`physics-lineage-map.md:463`; that row's "named
  not-yet-run" wording does not yet reflect the gate verdict).
- Two earlier double-slit sims exist, and this visual revisits neither: a click-by-click screen with no defect
  (`research/2026-06-08_ave-double-slit_born-from-clicks_result.md`), and before that an imposed-trajectory K4-TLM
  animation (`research/2026-06-04_k4tlm-double-slit-darkwake-result.md`).
- Which physical sector the displayed port-sum channel is, inside an engine labelled transverse-only, stays open (as
  in Visual 3).

**Internal-review build.** On-frame text carries corpus ids; a public cut strips them.

---

## Verified engine numbers (at HEAD)

Visual 1 (`electron_lattice_scene.json` meta): srs net z=3 (1728 nodes, all
degree-3), winding **Q_link=3** (raw 2.9984), **w_tor=2** (reader-certified),
kernel S(A)=(1−A²)^0.5, doorway **Δb₁=+1** (two-method agree), meridian
**linking=±1**, cycle length 34.0. Canonical matched cut rc=2.8 (extends the
committed lane-Z +1 plateau to L=6). 19 wall nodes at yield (A>0.9, S→0.045).

Visual 2 (`hibef_moment_scene.json`): demonstrated pump A²=5.923e-07; NJP
9835 eV scenario **Δφ=0.1476 rad, Δφ/2=0.0738 rad**, P_SVE=5.438e-03,
P_QED=2.782e-14, ratio 1.95e11 (field-independent across all 3 probes — the
α-echo magnitude). S_true=1.000000 at the true amplitude (recorded honestly;
motivates the labelled visual exaggeration).

Visual 3 (`lvps_meta.json`): srs net z=3, 110,592 tanks, periodic box 67.9 ℓ_node;
47 steps shown; energy drift 5.0e-15; unused polarization component ≡ 0. Wrap guard,
over every displayed node: agrees with a 32-cell box to ≤1e-12 (relative) through
step 36, within 1e-3 through step 47; step 48 is the first to exceed 1e-3, so the run
stops at 47. Readout tanks at r = 9.56 and 20.16 ℓ_node:
lag **18** (peak-to-peak) / **19** (cross-correlation) steps → 0.558–0.589 ℓ_node/step,
against the long-wave c_link/√3 = 0.5774. Seed uniform-mode energy share 0.048%.

Visual 4 (`ts_meta.json`): srs slab, 2,962,176 tanks, 3385 steps at λ = 32 ℓ_node; energy closure
≤ 1.4e-13 over every run; single-frequency readout converged to 3.5e-05. ω₀ = 0.11333207 rad/step from the Bloch
one-step operator (Grover relation: same value, an identity), 0.99973 of c_net·k₀; in-plane isotropy |Δk|/k ≤ 7.9e-04; incident
wavenumber read off the field 0.999988 k₀; normal-incidence wall reflection -0.9953 -0.0310i (short plane -0.082 ℓ_node off the
nominal wall). The video's placement vs the reference (128 points/λ): worst extremum 1.07 % (single frequency), 1.30 % (dose);
central visibility 0.8933 vs 0.8973. Over the 16 placements per λ, see the Visual 4 scores table.

## Cross-checks (pre-push audit)

* HTML client-side kernel `Sof(a)=clip((1−a²)^p, S_min, 1)` reproduces the
  Python `saturation_kernel` **exactly** (max|diff|=0.0 over all 1728 nodes) —
  the amplitude slider re-evaluates the canonical Ax4 form, not an approximation.
* Both scene JSONs regenerate **bit-identically** (deterministic drivers).
* Chirality carrier is the writhe pseudoscalar (flips −0.0409 ↔ +0.0409 L/R),
  correctly **distinct** from the winding integer (Q_link=+3 both hands) — the
  scene labels the enantiomorph without conflating the two.
* Both HTMLs validated headless (node harness): JS executes clean, canvas draws.
* Public-naming leak scan clean (SVE only; no framework/external terms).
* Visual 3: receipts regenerate **bit-identically** (the tracked JSON carries no
  wall-clock field; checked scratch run vs. repo driver). The medium itself is
  certified by acceptance test T1.1 (photon on srs), re-run 2026-09-29 on main
  50fdb644: PASS — |speed|/c_net 0.9957, energy drift 5.2e-14, centroid R² 0.99981.
  Visual 3 carries corpus ids on frame by design (internal-review build).
* Visual 4: `ts_meta.json` regenerates bit-identically from the cached runs (no wall-clock field); an engine
  re-run reproduces the screen dose bit for bit. One step function (`tlm_step`) serves the run loop and the
  receipt that matches it to `vector_tlm_step` exactly (max |Δ| = 0 after 50 steps, the second polarization stays 0).
  Every rendered frame passes an overflow guard (every figure-level text must end inside the frame, horizontally).
  The screen readout, applied to the reference sampled at each λ's own screen tanks, is biased by ≤ 0.17 % (λ = 16)
  and ≤ 0.05 % (λ = 32); halving the reference resolution moves its extrema by ≤ 0.28 % (single frequency),
  ≤ 0.34 % (dose). Two adversarial audits (numerics; framing and cites) ran on the first version; their findings are folded in.

## Reproduce

```
cd src
PYTHONPATH=. python3 scripts/viz/electron_lattice_scene.py   # -> viz/electron_lattice/*
PYTHONPATH=. python3 scripts/viz/hibef_moment_scene.py       # -> viz/hibef_moment/*
PYTHONPATH=. python3 scripts/viz/lattice_vs_projected_strain.py --stills   # -> viz/lattice_vs_projected_strain/*
PYTHONPATH=. python3 scripts/viz/two_slits_srs.py --stills                 # -> viz/two_slits_srs/*
```

Open the `*.html` files directly in a browser (no server, no build step). Visual 3
needs `ffmpeg` on PATH; its 59 MB engine-array cache goes to the gitignored
`build/viz/lattice_vs_projected_strain/` (about 3 minutes end to end). Visual 4 runs 46 lattice runs and 5
reference solves in parallel (`--workers`, default 6); its cache goes to the gitignored
`build/viz/two_slits_srs/` (252 MB here). Measured here: each λ = 32 lattice run takes 6–9 minutes at about 2 GB, each
128-points-per-λ reference solve about 25 minutes at 2.4 GB, so a full build is tens of minutes on 6 cores;
`--render-only` re-renders in under a minute.
