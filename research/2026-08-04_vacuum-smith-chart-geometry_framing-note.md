# Vacuum Smith chart — hyperbolic-geometry framing note (2026-08-04)

**Status: FRAMING NOTE — walk-level, verification-tagged per claim. Mints no `clm-`/`def-`;
adjudicates nothing.** Origin: Grant, in-session 2026-08-04, looking at the chart grid: *"why does
the Smith chart look like the cross section of a photon's propagation path past a black hole?
Toward the right, the paths are shorter/lensed."* This note preserves that observation and the
walked answer, with every claim partitioned by evidence class so nothing here can propagate as
more than it is.

**Tags:** `[M-V]` machine-verified this session (sympy receipts, §V1) · `[T]` textbook-standard,
formal citation owed · `[L]` literature pointer, retrieval-verification ROUTED · `[R]` structural
rhyme, UN-AUDITED, derivation ROUTED.

---

## Layer 1 — the crowding is conformal compactification

- `[M-V 1]` Γ = (z−1)/(z+1) maps the passive half-plane Re z ≥ 0 onto the unit disk
  (|Γ|² − 1 = −4·Re z / |z+1|², symbolically zero).
- `[M-V 2]` z = ∞ maps to Γ = +1: the entire far half-plane is crushed into the right-edge point.
- `[M-V 7]` The chart's natural (mismatch) distance d = 2 artanh|Γ| = ln SWR diverges at the rim
  (numeric-exact; the symbolic form is the definitional log expansion of artanh). The
  "shorter / more relaxed" right-edge arcs are Euclidean-small but **metrically infinite** — the
  conformal-factor illusion, same as an Escher *Circle Limit* print. `[T]`

## Layer 2 — the chart carries the Poincaré-disk geometry, and the grid is a ray beam

- `[M-V 4]` Constant-reactance circles (centers (1, ±1/x), radii 1/|x|) satisfy
  |center|² = 1 + radius² — **orthogonal to the rim** — and `[M-V 5]` all pass through the ideal
  point Γ = +1. Circles orthogonal to the boundary are Poincaré-disk **geodesics** `[T]`; a family
  through one ideal point is a **pencil of asymptotically parallel geodesics**.
- `[M-V 3]` Constant-resistance circles are internally tangent to the rim at Γ = +1
  (center + radius = 1) — **horocycles** at that ideal point `[T]` — and `[M-V 6]` orthogonal to
  the geodesic pencil, i.e. its **wavefronts**.
- **Consequence (the answer to the observation):** the Smith-chart grid *is*, mathematically, a
  beam of parallel rays with their wavefronts, falling toward a point at infinity, drawn in a
  constant-negative-curvature 2-space. The lensing resemblance is a correct reading of the
  geometry, not pareidolia.
- `[M-V 9]` Lossless-line action Γ → Γe^(−2jβl) preserves |Γ| (rotation); `[M-V 8]` the SU(1,1)
  fractional-linear action (|a|² − |b|² = 1) preserves the disk with
  1 − |Γ′|² = (1 − |Γ|²)/|b̄Γ + ā|². SU(1,1)/±1 ≅ SO⁺(2,1) `[T — group-isomorphism citation
  owed]`: **lossless network transformations act on reflection space as a 2+1 Lorentz group.**
  `[L]` ("hyperbolic geometry of the Smith chart," microwave literature — retrieval routed.)
- `[L]` Aberration cross-link: Möbius maps of the celestial sphere ≅ SO⁺(3,1); a boost crowds the
  star field toward the motion point in the same tangent-circle pattern (Penrose,
  apparent-shape/aberration — retrieval routed).

## Layer 3 — the black-hole family resemblance, with its honest limits

- `[L]` Fermat form: photon paths in Schwarzschild are geodesics of an *optical metric* whose
  equatorial Gaussian curvature is **negative**; the deflection angle follows from Gauss–Bonnet on
  that geometry (Gibbons & Werner 2008 — retrieval verification routed).
- **Bounded claim:** BH lensing and the chart grid are both ray congruences in negatively curved
  2D optical geometry — the **same geometric family**. NOT the same object: the Schwarzschild
  optical curvature is r-dependent and asymptotically flat (the disk is homogeneous, K = −1), and
  the grid arcs are coordinate lines, not dynamical trajectories — they become motion only when a
  transformation (line length, grading) drags the load point along them.

## The routed rhyme `[R]`

Rim at infinite mismatch distance ↔ horizon at infinite coordinate time: both conformal-boundary
phenomena. **Checkable, not yet checked:** does the certified circuit's radial wall approach map
isometrically between the graded region's optical metric (gradient-index canon,
trampoline-analogy family) and the chart's hyperbolic metric? If yes, the lensing resemblance is
a change of coordinates; if no, it ends at family resemblance. Routed as **V2** below. Until V2
resolves, this paragraph is a rhyme, and citing it as more than that is a defect.

---

## §V1 — machine receipts (this session, AVE-Core `.venv` sympy)

Checks 1–6, 8–9 symbolic TRUE; check 7 numeric-exact (definitional log form):

```
1. |Γ|²−1 = −4Re(z)/|z+1|²            : True
2. z→∞ ⇒ Γ→+1                          : True
3. r-circle tangent at Γ=+1            : True   (horocycle)
4. x-arcs ⊥ rim  (|O|²−1−R² = 0)       : True   (geodesics)
5. x-arcs through Γ=+1                 : True   (pencil at the ideal point)
6. grid orthogonality (horocycle⊥geod) : True   (wavefronts)
7. d = 2artanh|Γ| = ln SWR             : numeric-exact (definitional)
8. SU(1,1) preserves the disk          : True
9. line action = rotation (|Γ| fixed)  : True
```

Per sweeps-become-scripts: if these checks are ever run again, they get committed as a `tools/`
checker; this note's inline block is the first-run receipt.

## Routed follow-ons

- **V2 — the isometry check** (the `[R]` rhyme): optical-metric ↔ chart-metric mapping for the
  certified wall approach. **Queued behind the Lorentz-compliance arc**
  (`_orchestration/2026-08-04_lorentz-compliance-arc-brief.md`); needs an SVA-headed prereg.
- **V3 — literature retrieval**: Gibbons & Werner 2008; Penrose aberration; the
  hyperbolic-Smith-chart EE literature; a standard reference for SU(1,1)/±1 ≅ SO⁺(2,1).
  External-retrieval lane, session-adjudicated; every `[L]` above upgrades or dies on its return.
- **Figure**: an exploratory interactive chart exists as a session artifact (not corpus). A
  house-style static figure is deferred until V3 lands and V2 resolves.
