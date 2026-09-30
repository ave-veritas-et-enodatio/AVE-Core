# Engine-driven production visuals

Two full-production, engine-driven visuals for the SVE (structured-vacuum
electrodynamics) programme. Each is produced by a **Python engine driver** under
`src/scripts/viz/` that exports a scene/data JSON, consumed by a **self-contained
interactive HTML** (vanilla `<canvas>`, no external JS) plus **static renders**
in the house figure style (`ave.viz.style`, white background, Okabe-Ito).
Visual 3 is an internal-review **video**: its driver renders an MP4 directly from
the engine arrays, plus key-frame stills.

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

## Reproduce

```
cd src
PYTHONPATH=. python3 scripts/viz/electron_lattice_scene.py   # -> viz/electron_lattice/*
PYTHONPATH=. python3 scripts/viz/hibef_moment_scene.py       # -> viz/hibef_moment/*
PYTHONPATH=. python3 scripts/viz/lattice_vs_projected_strain.py --stills   # -> viz/lattice_vs_projected_strain/*
```

Open the `*.html` files directly in a browser (no server, no build step). Visual 3
needs `ffmpeg` on PATH; its 59 MB engine-array cache goes to the gitignored
`build/viz/lattice_vs_projected_strain/` (about 3 minutes end to end).
