[↑ Ch.1 Fundamental Axioms](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from L3 closure synthesis + K4 rotation group + photon-propagation-baseline as canonical K4 cubic-anisotropy empirical signature -->

# Cubic K4 Anisotropy at Saturation Collapse: Empirically Observable Substrate Symmetry

When the K4 substrate collapses into saturation regime ($A^2 \to 1$), the bipolar saturated attractor exhibits **cubic K4 anisotropy** — NOT spherical, NOT isotropic, NOT a numerical artifact. This is the empirical signature of the underlying $T = A_4$ tetrahedral rotation group acting at the substrate scale, projected through Cartesian alignment of the simulation lattice. Confirmed across L3 doc 79 path α v3 (5 sampler views, +x/−x bipolar split) AND v14 cubic-emergence visualizations. **Falsifiable**: any substrate that collapses to perfectly spherical symmetry at saturation is NOT the K4-Cosserat substrate; AVE predicts cubic 6-vertex / 8-face / 12-edge anisotropy emerging from $T_d$ symmetry.

## Key Results

| Result | Statement |
|---|---|
| Empirical signature | **Cubic K4 anisotropy** at saturation collapse — NOT spherical, NOT isotropic |
| Group-theoretic origin | $T = A_4$ proper tetrahedral rotation group, $|T| = 12$ — see [K4 rotation group](k4-rotation-group.md) |
| Cubic axes | $\pm \hat{x}, \pm \hat{y}, \pm \hat{z}$ become preferred directions in saturated attractor |
| Bipolar +x/−x split | Persistent across L3 doc 79 path α v3 5 sampler views (path α v1: +x median 1.89, −x median 5.42; path α v2: +x median 3.62, −x median 4.97) |
| Cardinal-axis kinematics | $v = c \sqrt{2}$ along cardinal axes (vs $v = c$ diagonal-axis) — same cubic anisotropy in propagation |
| Falsifier | Perfectly spherical collapse at saturation falsifies AVE substrate |

## §1 — The empirical observation

When seeded near saturation amplitude and evolved, the K4-Cosserat coupled engine produces a stable attractor that exhibits **cubic symmetry**, not spherical:

- **L3 doc 110** (v14 cubic emergence): visual artifacts `v14_collapse_cubic_emergence.png` + `v14_cubic_vs_spherical_compare.png` show the saturated $|V|$ envelope developing cubic faces aligned with the lattice Cartesian axes
- **L3 doc 79 path α v3** (5 sampler views): bipolar +x/−x R/r split persists across V_inc/V_ref, $(\Phi_{\text{link}}, \omega_x/y/z)$ per-axis, $(\Phi_{\text{link}}, |\omega|)$ magnitude — all exhibit the same cubic anisotropy
- **Photon propagation baseline**: cardinal-axis $v = c\sqrt{2}$ vs diagonal-axis $v = c$ propagation speed split is the same cubic anisotropy in linear regime

The K4 lattice's underlying $T_d$ symmetry imprints on every observable.

## §2 — Group-theoretic origin

The K4 rotation symmetry is $T = A_4$ (12 elements). The full point group with reflections is $T_d = S_4$ (24 elements). When the substrate aligns its Cartesian computational axes with the K4 unit cell's $\pm x / \pm y / \pm z$ directions, the symmetry is **explicitly cubic** in the simulation reference frame.

| K4 symmetry element | Substrate axis |
|---|---|
| 3 face-midpoint $C_2$ axes | $\pm \hat{x}$, $\pm \hat{y}$, $\pm \hat{z}$ |
| 4 vertex $C_3$ axes | $(\pm 1, \pm 1, \pm 1)/\sqrt{3}$ tetrahedral |
| 6 edge $C_2'$ axes (in $T_d$) | $(0, \pm 1, \pm 1)/\sqrt{2}$ etc. |

At saturation collapse, the substrate's nonlinear dynamics select preferred axes consistent with these symmetry elements. The **cubic 6-vertex / 8-face / 12-edge structure** emerges from the natural orientation of $T_d$ relative to the lattice frame.

## §3 — Empirical signatures across tests

### L3 doc 79 path α v3 (5 sampler views, 4 bond-pairs)

| Cluster | View | Median $R/r$ |
|---|---|---|
| +x | (a) 3D $\omega$-PCA | $e_2/e_1 = 1.231$, planarity 0.469 |
| +x | (b-x) | 3.477 |
| +x | (b-y) | 3.173 |
| +x | (b-z) | 4.816 |
| +x | (c) $\|\omega\|$ magnitude | 4.546 |
| −x | (a) | $e_2/e_1 = 1.268$, planarity 0.542 |
| −x | (b-x) | 4.237 |
| −x | (b-y) | 4.081 |
| −x | (b-z) | 6.572 |
| −x | (c) | 5.741 |

**Bipolar +x/−x split persists across all 5 sampler views.** This is robust empirical evidence of substrate-level cubic anisotropy: the K4 lattice's underlying $T_d$ symmetry imprints on the saturated attractor in a way that breaks isotropy along the Cartesian (cardinal) directions.

### v14 cubic emergence

`v14_collapse_cubic_emergence.png` shows the saturated $|V|$ envelope developing **cubic faces** as the simulation evolves. The envelope is NOT a sphere; it has 6 face-centered protrusions (one per face of the K4 unit cube).

`v14_cubic_vs_spherical_compare.png` directly compares the K4-Cosserat output (cubic) against a putative isotropic-medium reference (spherical) — the difference is visually obvious.

## §4 — Connection to photon propagation kinematics

The same cubic anisotropy appears in **photon propagation speeds** on the K4 substrate per [Photon Propagation Baseline](../../dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md):

| Propagation direction | Speed | Origin |
|---|---|---|
| Cardinal ($\pm \hat{x}, \pm \hat{y}, \pm \hat{z}$) | $v = c \sqrt{2}$ | Port projections $\pm 1/\sqrt{3}$ force one cardinal cell per step |
| Diagonal ($\hat{p}_n$ tetrahedral) | $v = c$ | Junction-diagonal, no $\sqrt{2}$ factor |

**Same $T_d$ symmetry, two different observables**: in saturated regime → cubic envelope anisotropy; in linear regime → cardinal-axis propagation speed split.

## §5 — Why this matters

### Substrate-symmetry validation

The cubic anisotropy is **direct empirical access** to the underlying K4 lattice symmetry — a substrate property that's otherwise hidden inside abstract field theories. The substrate's structure becomes **operationally visible** when the engine reaches saturation regime.

### Falsifiability

**AVE predicts cubic anisotropy at saturation collapse.** Any alternative substrate model with different (e.g., spherical, hexagonal, icosahedral) symmetry would predict different anisotropy patterns. The observation of cubic 6-vertex / 8-face / 12-edge symmetry at K4 saturation IS the AVE-specific signature.

Falsifier: if a substrate model claims to be K4-Cosserat but produces perfectly spherical collapse at saturation, that model is INCONSISTENT with its claimed underlying symmetry.

### Implications for engine design

- **PML boundary placement** matters: if PMLs are placed at distances that fit the cubic symmetry (e.g., distance-from-center along cardinal axes), they absorb the cubic-symmetric wavefront cleanly; offset placements may produce artifact reflections
- **Mode-eigsolve at uniform $\sigma$** may miss cubic-symmetric modes if the eigsolver assumes spherical symmetry → diagnostic methodology should account for cubic anisotropy
- **Bipolar averaging** is necessary: any per-direction observable (e.g., $R/r$ in path α v3) needs per-cluster adjudication to capture both ± lobes

## §6 — Status

| Aspect | Status |
|---|---|
| Empirically observed | YES — L3 doc 79 path α v3 + doc 110 v14 visualizations |
| Group-theoretically expected | YES — direct consequence of $T = A_4$ K4 rotation group |
| Substrate-symmetry signature | CANONICAL |
| Falsifiable | YES — perfectly spherical collapse would falsify K4 |

## Cross-references

- **Canonical artifacts:**
  - `assets/sim_outputs/v14_collapse_cubic_emergence.png` — cubic envelope visualization at saturation
  - `assets/sim_outputs/v14_cubic_vs_spherical_compare.png` — direct comparison vs. isotropic reference
  - `src/scripts/vol_1_foundations/r10_master_equation_v14_anisotropy.py` — anisotropy driver
- **KB cross-cutting:**
  - [K4 Rotation Group $T = A_4$](k4-rotation-group.md) — group-theoretic foundation
  - [$\|T\| = 12$ Universality (4 Routes)](tetrahedral-t-universality.md) — $|T| = 12$ across multiple convergent calculations
  - [K4 4-Port Irrep Decomposition](../../operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) — $A_1 \oplus T_2$ irreps on the same port basis
  - [Photon Propagation Baseline ($v/c = \sqrt{2}$)](../../dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md) — cardinal-axis kinematics is the linear-regime version of cubic anisotropy
  - [L3 Electron-Soliton Closure Synthesis §8](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) — path α v3 bipolar +x/−x persistent split (5 sampler views)
- **Canonical manuscript:**
  - Vol 1 Ch 1 (Axiom 1) — K4 lattice tetrahedral connectivity
  - Vol 1 Ch 2 (Macroscopic Moduli) — substrate symmetry classes
