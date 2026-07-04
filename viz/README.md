# Engine-driven production visuals

Two full-production, engine-driven visuals for the SVE (structured-vacuum
electrodynamics) programme. Each is produced by a **Python engine driver** under
`src/scripts/viz/` that exports a scene/data JSON, consumed by a **self-contained
interactive HTML** (vanilla `<canvas>`, no external JS) plus **static renders**
in the house figure style (`ave.viz.style`, white background, Okabe-Ito).

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

## Reproduce

```
cd src
PYTHONPATH=. python3 scripts/viz/electron_lattice_scene.py   # -> viz/electron_lattice/*
PYTHONPATH=. python3 scripts/viz/hibef_moment_scene.py       # -> viz/hibef_moment/*
```

Open the `*.html` files directly in a browser (no server, no build step).
