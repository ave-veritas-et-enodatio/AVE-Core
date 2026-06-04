# Full-electron binding re-seed probe — prereg + result + fork verdict (2026-06-04)

**Status**: PREREG FROZEN (result + verdict appended below after the driver run).
**Driver**: [`src/scripts/vol_1_foundations/r10_fdtd3d_electron_binding_v2_reseed.py`](../src/scripts/vol_1_foundations/r10_fdtd3d_electron_binding_v2_reseed.py)
**Engine**: `src/ave/core/fdtd_3d.py` — `FDTD3DEngine` (full-vector Maxwell; nonlinear ε(E)=ε₀√(1−(E·dx/V_yield)²), μ(H)=μ₀√(1−(B/B_yield)²) per Axiom 4; Mur/CPML).
**Brief**: [`_orchestration/2026-06-04_full-electron-binding-reseed-probe.md`](../_orchestration/2026-06-04_full-electron-binding-reseed-probe.md).
**Supersedes attempt**: [`2026-05-18_phase3f-electron-torus-knot-first-attempt.md`](2026-05-18_phase3f-electron-torus-knot-first-attempt.md) (FAIL — 20.9% knot retention vs 56.3% random; §Factor 5 diagnosed the A46 phase-space-placement failure).

---

## §0 — TL;DR (prereg)

The 2026-05-18 phase3f attempt to bind a (2,3)-knotted electron on the full-vector
Maxwell engine FAILED because it put the (2,3) winding in REAL space (E-tangent to the
knot), but the canonical electron carries it in the **(V_inc, V_ref) phasor phase-space**
(`theory.md:16`, `torus-knot-uniqueness.md:15`). This probe re-seeds correctly with four
corrections and discriminates a load-bearing **continuum-vs-discrete fork**:

- **Mode I** (binds: retention > matched baseline, (2,3) winding conserved in the d-q
  phasor, n(r) gradient, breather-criterion persistence, ringdown Q ≈ α⁻¹) ⇒ the
  (V_inc, V_ref) phase-space IS the continuum (E ± Z·H) characteristic decomposition;
  the full electron hosts on `fdtd_3d.py`. CONTINUUM hypothesis confirmed.
- **Mode III** (disperses even with the correct phasor seed + Beltrami pair + near-V_snap
  amplitude, across ≥3 seed parameterizations) ⇒ strong evidence the DISCRETE K4 4-port
  is genuinely load-bearing; the continuum engine cannot host the (2,3); path forward is
  K4-TLM + c_eff(V) (doc 111 Path A). As valuable as a PASS.
- **Mode II** (binds but winding/observables off) ⇒ partial; diagnose.

---

## §1 — Corpus grounding (verify-before-cite: every cite grepped to source this session)

| Claim | Source (file:line) | Verbatim anchor |
|---|---|---|
| Electron = 0₁ unknot (real) + (2,3) Clifford winding in **phase space**, the (V_inc, V_ref) phasor trajectory NOT real-space flux topology | `manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:16` | "the electron is the $0_1$ unknot in real space carrying a $(2,3)$ Clifford-torus winding pattern in phase space … The trefoil lives in the bond-pair LC tank's $(V_{\text{inc}}, V_{\text{ref}})$ phasor trajectory, not in the real-space flux-tube topology." |
| The (2,3) = **2 windings on the d-axis, 3 windings on the q-axis** of the bond-pair LC tank | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md:15` | "the **phase-space Clifford-torus winding pattern** of the electron's bond-pair LC tank (2 windings on the d-axis, 3 windings on the q-axis)" |
| Canonical phase winding 2φ + 3ψ (φ toroidal, ψ poloidal) | `torus-knot-uniqueness.md:31,35`; `cosserat_field_3d.py:938` (`theta = 2.0*phi + 3.0*psi`) | — |
| Beltrami construction: ∇×A=kA, E⊥B closed loop, mutually orthogonal feeding | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md:9,13` | "a Beltrami standing wave where the continuous **E** and **B** field lines are mutually orthogonal and feed into each other in a closed topological loop ($\nabla \times \mathbf{A} = k\mathbf{A}$)" + ropelength 2π, R=r=ℓ_node/(2π) |
| Beltrami-bound-pair handedness: ω_A=−√2·p̂ LH, ω_B=+√2·p̂ RH; Φ_link=±1.0; LH=e⁻, RH=e⁺ | `research/_archive/L3_electron_soliton/70_phase5_resume_methodology.md:41,113-115`; `pair-production-axiom-derivation.md:77` | "inject Beltrami-bound-pair (ω_A = -√2·p̂_bond LH, ω_B = +√2·p̂_bond RH; Φ_link = ±Φ_critical = ±1.0)" + "Parity requires opposite handedness on the two sites → e⁻ (LH Beltrami) + e⁺ (RH Beltrami)" |
| (V_inc, V_ref) candidate = forward/backward propagating waves on the TL (Riemann invariants of E,H) | `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md:311` | "These are the forward and backward propagating waves on the radial transmission line." |
| Q-factor α⁻¹ = LC-tank Q at TIR boundary = ω·U/(per-cycle leak); leak fraction 1/Q = α; **consistency not emergence** (the seeded Λ values require fitting — `electron-unknot-cosserat-seeder.md:84`) | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:15,81`; `electron-unknot-cosserat-seeder.md:84` | "only a fraction $1/Q = \alpha$ … leaks per cycle through the TIR boundary — this IS $\alpha$"; seeder Q-factor test "PASS (after fitting; not autonomous)" |
| Two-engine architecture: `fdtd_3d.py` (this probe's target) is NOT the scalar Master-Equation-FDTD that holds the v14 Mode I PASS | `manuscript/ave-kb/common/two-engine-architecture-a027.md:19`; `electron-unknot-cosserat-seeder.md:95` | v14 Mode I PASS was on `master_equation_fdtd.py` (scalar ∇²V − μ₀ε₀√(1−(V/V_yield)²)∂²ₜV); `fdtd_3d.py` is the full-vector engine, never validated for the (2,3) |

**Corpus extension beyond the orchestrator pre-grep (§3 of brief):**
1. The canonical Cosserat seeder (`cosserat_field_3d.py:875-878,1028-1029`) explicitly states the (2,3)
   (V_inc, V_ref) Layer-3 winding is **K4 V-tank, NOT Cosserat ω real-space** — i.e. there is NO
   existing canonical implementation of the Layer-3 d-q phasor (2,3) winding on ANY full-vector engine.
   This driver builds it from scratch. (Implementer flag, surfaced — not a contradiction.)
2. **Prior K4/Cosserat Beltrami-pair attempt already failed** (`70_…:172,192` Finding A): point-rotation
   Beltrami (single ω vector + Φ_link) scattered 93% in ONE velocity-Verlet step on the Cosserat engine.
   Diagnosis: "topology must be encoded as persistent structural feature, not single-component injection."
   That was a DIFFERENT engine (`cosserat_field_3d.py`), so it does not pre-decide this probe — but it
   raises the prior that a bare ω-vector pair is unstable; my seed uses a **topologically-structured
   (2,3)-winding field** (per the doc-70 §226 Round-7-Stage-2 recommendation), not a bare vector pair.

---

## §2 — Substrate-native-check on `fdtd_3d.py` (walked before any seed code)

| Checkpoint | Finding on `fdtd_3d.py` |
|---|---|
| **Sector** | Full-vector Maxwell (E, H) on a Yee grid; 6 real-space lattice-Cartesian components (Ex,Ey,Ez,Hx,Hy,Hz). |
| **Reactance pair (E↔H)** | E (capacitive, updated via ∇×H / ε_eff) ↔ H (inductive, updated via ∇×E / μ_eff). This is the LC pair. Both C-state (E) and L-state (H) are recorded every step in the recording window (Rule-10 reactance-pair-tracking corollary). |
| **Coordinate system (Checkpoint 4 — THE one, A46)** | Engine STATE is real-space lattice-Cartesian (E, H). There is **NO native (V_inc, V_ref) phasor**. The d-q phasor must be CONSTRUCTED: V_inc = E + Z₀·H, V_ref = E − Z₀·H (per `radial-eigenvalue-solver.md:311` forward/backward characteristics). **Both the seed AND the winding observable are computed in (V_inc, V_ref)** — phase-space-coordinate-check satisfied. |
| **Saturation-modulated clock (c_eff at A→1)** | `_compute_local_epsilon`: ε_eff = ε₀√(1−(E·dx/V_yield)²); as ε→0 the update coeff ce = dt/(ε_eff·dx) → ∞, i.e. c_eff = 1/√(εμ) RISES inside the saturated core (matches two-engine-arch §28). UNLIKE K4-TLM, this engine HAS c_eff(V) modulation — the load-bearing capability for trapping. |
| **Infinity discipline (ave-infinity-discipline)** | Engine has a built-in S_min floor: `ratio_sq = clip(…, 0, 1−EPS_SAT_RATIO)` (EPS_SAT_RATIO=1e-12). phase3f NaN-blew-up at 0.85·V_yield/dx because dt/(ε_eff·dx) still overran the CFL margin near saturation. Stabilization here: (a) post-construction CFL-buffer reduction (`engine.dt *= cfl_safety`), (b) amplitude capped below the empirical blowup, (c) document the clip + report `max_strain_ratio`. |
| **PML exclusion (Rule-10 corollary)** | PML = multiplicative exponential damping over `pml_layers` boundary cells. ALL top-K density extractions filter `pml ≤ {i,j,k} ≤ N−pml−1` BEFORE argpartition (mirrors `r9_canonical_phase_space_phasor.py:make_interior_mask`). |

---

## §3 — The four seed corrections vs phase3f (the load-bearing construction)

**Correction 1 — (2,3) in the (V_inc, V_ref) d-q phasor, NOT real space.**
The corpus-literal reading (`torus-knot-uniqueness.md:15`: "2 windings on the d-axis, 3 windings on
the q-axis") is the **spatial-winding-on-phasor-axes** construction: as the closed toroidal loop is
traversed, the bond-pair phasor wraps 2× in the d-axis (V_inc) and 3× in the q-axis (V_ref). At each
torus-shell cell with toroidal angle φ, poloidal angle ψ:

> **V_inc(φ,ψ) = E + Z₀·H = envelope · cos(2φ)**   (2 windings, d-axis)
> **V_ref(φ,ψ) = E − Z₀·H = envelope · sin(3ψ)**   (3 windings, q-axis)

Real-space (E, H) is recovered by inverting the characteristic map:
**E = (V_inc + V_ref)/2,  Z₀·H = (V_inc − V_ref)/2** — so the real-space fields carry only the plain
toroidal carrier (the unknot); the **entire (2,3) information lives in the d-q split**. This is the
A46 fix: the topology is in the coordinates the corpus claim lives in.

> **LOAD-BEARING CONSTRUCTION CHOICE (surfaced for Grant, brief §IMPORTANT / pre-test-physics-check):**
> The brief states the (2,3) is the "**TEMPORAL** phasor trajectory (2:3 Lissajous)". A single linear
> LC tank has ONE natural frequency, so its (V_inc, V_ref) = forward/backward characteristics of the
> SAME oscillation trace a simple 1:1 ellipse, NOT a 2:3 Lissajous — a true *temporal* 2:3 needs two
> incommensurate frequencies (2ω:3ω) or an anharmonic 3rd-harmonic mechanism, which a bare single-tank
> seed cannot supply. The corpus most-literal statement (`torus-knot-uniqueness.md:15`) is a **spatial**
> winding (d-axis/q-axis windings of the closed loop), which is well-posed on a single seed. I lock the
> **spatial-winding-on-phasor-axes** reading as the PRIMARY seed (parameterization S1) and carry the
> temporal reading as an ALTERNATIVE (S2: seed E,H phase-shifted so the *time-domain* (V_inc,V_ref) at a
> fixed cell traces 2:3 via a deliberately bichromatic 2ω:3ω carrier). If the fork verdict hinges on
> this choice (e.g. S1 disperses but S2 binds, or vice versa) it is escalated to Grant rather than
> self-resolved.

**Correction 2 — self-consistent Beltrami pair, NOT H=0.**
Force-free B∥A standing wave with |E| = c|B|, E⊥B around the horn torus R=r (`electron-unknot.md:13`).
Construction: build a divergence-light toroidal-poloidal vector potential A on the shell, set
B = ∇×A (so B∥A approximately on a Beltrami shell), E = c·(k̂ × B) with k̂ the local loop tangent so
E⊥B and |E|=c|B|. Then overlay the d-q (2,3) split (Correction 1) on the (V_inc, V_ref) characteristics.
Two endpoints A, B with **opposite handedness** (LH=e⁻ at A, RH=e⁺ at B), per `70_…:113-115` +
`pair-production-axiom-derivation.md:77`. The seed is a *topologically-structured* field (the doc-70
§226 Round-7-Stage-2 recommendation), not a bare ω-vector — addressing the prior point-rotation instability.

**Correction 3 — matched-distribution baseline, NOT random.**
phase3f's random baseline had larger single-component amplitudes → more saturation → spurious "better"
retention (its Factor 2). The trivial baseline here has the **SAME per-component amplitude statistics**
as the knot seed but **topologically-trivial winding** — built by RANDOM-PHASE-SHUFFLING the d-q phasor
fields cell-by-cell (destroys the 2φ/3ψ winding coherence, preserves the exact per-component histogram),
then inverting the same characteristic map. Matched first-moment AND amplitude histogram; only the
topological winding differs. A trivial-winding (0,0) carrier at matched envelope is also reported as a
second control.

**Correction 4 — amplitude near V_snap with stabilization.**
Operate the topological seed near V_snap so Γ→−1 engages (the leak-1/Q=α TIR boundary). Stabilize via
(a) `engine.dt *= cfl_safety` (smaller dt than the engine's 0.80 CFL buffer), (b) amplitude swept up
from a safe floor toward V_snap with a hard cap below the empirical NaN-blowup, (c) the EPS_SAT_RATIO
S_min floor (documented clip). `max_strain_ratio` reported every run; any clip is logged.

---

## §4 — Observables (all in matching coordinates; PML-excluded; canonical-imported)

1. **Knot retention** = (peak interior |E| at t_final) / (peak interior |E| at t₀), PML-excluded top-K.
   Compared against the **matched-distribution baseline** retention (Correction 3), NOT random.
2. **(2,3) winding number in the d-q phasor** — the load-bearing topological observable, measured in
   (V_inc, V_ref) (phase-space-coordinate-check). On the seed and after evolution: traverse the
   toroidal contour (fixed ψ) and count d-axis (V_inc) phase windings → target **2**; traverse the
   poloidal contour (fixed φ) and count q-axis (V_ref) phase windings → target **3**. Winding via
   unwrapped-phase accumulation / 2π (mirrors `cosserat_field_3d.py:1773-1839 single_contour_winding`).
3. **n(r) gradient** — effective refractive index n_eff(r) = c₀/c_eff(r) = 1/√(S(E)·S(B)) sampled
   radially OUTSIDE the saturated core; a monotone n(r) > 1 halo = the gravity-class index gradient.
4. **Bound-state persistence (breather criterion, doc 113 / `r9…:PERSISTENCE_GUARD`)** — mean interior
   V_peak over the recording window stays > a threshold fraction of seed (breathing allowed; NOT strict
   stationarity). Reactance pair (E-state AND H-state) recorded every step (Rule-10).
5. **Ringdown Q-factor ≈ α⁻¹** — operational time-domain Q from the interior-energy decay envelope:
   Q = π / |ln(U(t+T)/U(t))| per ring period T (leak fraction 1/Q per cycle). Target Q ≈
   `ALPHA_COLD_INV` ≈ 137.036. **TAGGED CONSISTENCY-class, NOT emergence** (consistency-vs-emergence):
   the canonical α⁻¹ decomposition requires geometry-fitting (`electron-unknot-cosserat-seeder.md:84`),
   so a Q≈137 here is a consistency check that the trapped LC tank leaks at the canonical rate — it is
   NOT an autonomous α-emergence claim (that is the closed Class-B `ch8` derivation).

**Canonical-source discipline (ave-canonical-source):** the driver imports `V_YIELD`, `V_SNAP`,
`L_NODE`, `Z_0`, `ALPHA_COLD_INV`, `C_0`, `EPSILON_0`, `MU_0`, `ALPHA` from `ave.core.constants`; NO
hardcoded literals (phase3f hardcoded `43650.0` + `RandomState(42)` — both fixed). A verify-constants
cross-check prints the imported values and asserts the derived relations (V_YIELD = √α·V_SNAP, Z_0 =
√(μ₀/ε₀)) BEFORE any verdict.

---

## §5 — Adjudication thresholds (substrate-derived or honestly tagged engineering-choice)

| Criterion | Threshold | Provenance |
|---|---|---|
| Retention vs matched baseline | knot retention > matched-baseline retention (strict >, with a margin ≥ the run-to-run jitter measured from the trivial control) | ENGINEERING-CHOICE (comparison test; the *direction* is substrate-meaningful, the margin is empirical-noise-calibrated). |
| (2,3) winding conserved | d-winding ∈ {2} AND q-winding ∈ {3} on a reliable contour, both at seed AND after the recording window | SUBSTRATE: the winding integers are the topological invariants; tolerance is ±0 on the integer (reliability-gated per the contour-reliability metric, `cosserat…:1837`). |
| n(r) gradient | n_eff(r) monotone-decreasing outward over ≥3 interior radial bins with n_core/n_far − 1 > the lattice-noise floor | ENGINEERING-CHOICE on the bin count + floor; the existence of a gradient is substrate-meaningful. |
| Persistence (breather) | mean recording-window V_peak ≥ 0.40 × seed V_peak (breathing allowed) | INHERITED from `r9…:PERSISTENCE_GUARD=0.40` + doc-113 mean-V_peak breather criterion (NOT strict stationary). |
| Ringdown Q ≈ α⁻¹ | Q within ±20% of `ALPHA_COLD_INV` ≈ 137.036 | ENGINEERING-CHOICE tolerance (consistency-class; a coarse FDTD ringdown cannot resolve δ_strain); ±20% is a generous consistency band, not an emergence precision claim. |

**Mode assignment:**
- **Mode I** = retention-beats-baseline ∧ (2,3)-winding-conserved ∧ n(r)-gradient ∧ persistence ∧ Q≈α⁻¹ — ALL five.
- **Mode II** = persistence ∧ retention-beats-baseline but winding OR n(r) OR Q off.
- **Mode III** = disperses (persistence fails OR retention ≤ baseline) **across ≥3 seed parameterizations**
  (S1 spatial-winding, S1 at a 2nd amplitude/resolution, S2 temporal-Lissajous) despite correct phasor
  seed + Beltrami pair + near-V_snap amplitude.

---

## §6 — Honest-closure + framing posture (Rule 11 / Rule 12 / lane discipline)

- This is a **FORWARD test on `fdtd_3d.py`**, NOT a fit (ave-driver-script-honesty): no optimizer drives
  any parameter onto a known answer; the seed is constructed analytically from the corpus recipe; the
  verdict is read off the pre-registered thresholds.
- The fork verdict is the deliverable. **Mode III is reported as a positive scientific result** (the
  discrete-K4 4-port is load-bearing; continuum can't host the (2,3)) — NOT debugged toward a rescue.
- Per lane discipline: if the continuum-vs-discrete call needs a physics adjudication unresolvable from
  the corpus, or the temporal-vs-spatial Lissajous reading turns out load-bearing for the verdict, I
  STOP and surface to Grant via this doc + the final report; I do NOT draft an Ax-5 candidate or a
  methodology pivot, and I do NOT free-build past the ambiguity.

---

<!-- RESULT + FORK VERDICT appended below after the driver run -->
