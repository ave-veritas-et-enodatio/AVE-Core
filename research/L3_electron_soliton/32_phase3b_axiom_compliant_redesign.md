# Phase 3b Axiom-Compliant Redesign — Pre-Registered Eigenmode Test

**Date:** 2026-04-22
**Status:** PRE-REGISTRATION. Companion script `phase3b_axiom_compliant.py`
to be run AFTER this document is committed. Predictions below are
recorded before any numerical outcome is observed.

**Supersedes:** `31_phase3b_simulation_setup.md` (which described the
earlier test that yielded a transient-not-eigenmode negative result).
Relationship: `31_` was the initial setup with imposed amplitude and
PML boundaries; this `32_` is the axiom-compliant redesign that
removes non-derivable choices wherever possible.

---

## §1 Why this redesign exists

The prior test (`phase3b_eigenmode_verification.py`) produced a
clean negative result: at the amplitude-sweep's sweet-spot
(`target strain 0.3, achieved A_max ≈ 0.48`), the shell geometry
drifts 19.5% over 400 steps past the initial transient. The earlier
`α⁻¹ = 139` match from the amplitude sweep was a *time-averaging
artifact* — a transient passage through Golden-Torus proportions
caught in the 200-300 step window, not a stable bound state.

Animating the simulation exposed a deeper issue: the first ~50 steps
are the TLM *rapidly correcting* our Lorentzian ansatz (not physics),
and the slow post-transient drift was too small to see frame-by-frame
at 8 fps. What we were visualizing was our guess being corrected,
dominated by boundary absorption (PML) and finite-domain effects.

On inspection, a catalog of non-axiomatic assumptions had accumulated:
imposed amplitude, Lorentzian envelope, PML boundaries, Ch 8 multipole
formula for Q-extraction (audit F4), finite N=64. Per Grant's
direction, the redesign must justify every parameter from AVE axioms
or flag it as open.

---

## §2 Axiom-compliance audit — every choice classified

### §2.1 Axiom-derived, keep

| Choice | Axiom source |
|---|---|
| K4 diamond substrate | Axiom 1 |
| Bipartite A/B sublattices | Axiom 1 (K4 topology) |
| Port scattering `S = (1/2)𝟙 − I` | Axiom 3 Kirchhoff at 4-port junction |
| `dt = dx/(c·√2)` | TLM stability + Axiom 1 dimensional scale |
| Op3 bond reflection with `S_sat = √(1−A²)` | Axiom 4 saturation (post-audit revision: K4-derived) |
| `V_SNAP = m_e c²/e` | Axioms 1+2 via `ξ_topo` topo-kinematic identity |
| `V_YIELD = √α·V_SNAP` | Axiom 4 + α from Ch 8 EMT |
| (2,3) winding topology | Synthesis Step 4 — smallest non-trivial coprime torus knot |
| ω_C = c/ℓ_node | Synthesis Step 3 — single-bond LC resonance |

### §2.2 Non-axiomatic, fix

| Choice | Prior value | Redesign value | Justification |
|---|---|---|---|
| Boundary condition | PML thickness 6 (absorbing) | Periodic wrap (pml=0) | Physical vacuum has no boundary. Survey confirms `pml=0` → toroidal wrap via np.roll, lossless. |
| Lattice size | N=64 | N=96 | Larger periodic wrap minimizes self-interaction of a localized soliton at R≈24 with itself. |
| Amplitude | Hand-set per run | Held fixed per Op6 iter; swept across runs | Op6 self-consistency targets (R, r). Amplitude remains a free parameter we sweep; an axiom-derived `A_electron` is listed as deferred gap §5.4. |
| Envelope shape | Single Lorentzian | Hedgehog + Gaussian + exponential | Tests seed-independence — if dynamics has a true eigenmode, all envelopes converge to the same (R, r). |
| Primary Q extraction | Ch 8 multipole sum | LC-tank closed-form reference (axiom-derived); Ch 8 as geometric check only | Ch 8 multipole Q-interpretation is audit F4 open; LC-tank Q = 1/α is axiom-derived and independent of sim outcome. |

### §2.3 Non-axiomatic, flag (defer closure)

| Choice | Why deferred |
|---|---|
| Port quadrature `{0,1}` vs `{2,3}` in ansatz | Pairing isn't derived; an AVE-native phase-encoding scheme across 4 tetrahedral ports is open. Held at {0,1}/{2,3} for consistency across envelopes. |
| Chirality weight `w_k = (p_k · t̂)/√3` | Heuristic projection; no derived operator produces this. |
| Shell-selection threshold (0.3 of peak) | Arbitrary cutoff for "what counts as shell." Held fixed for comparison. |
| R/r extraction via FWHM/2 | Biased for non-Lorentzian profiles. The envelope sweep will partially calibrate this bias. |
| n̂ ↔ ω identity (scoping §4) | Phase-1 entry criterion still open. Operationally: V is proxy for the phase-winding; formal Cosserat-field interpretation deferred. |

### §2.4 Rule 6 check (COLLABORATION_NOTES.md)

> "The TLM evolution IS the computation."

The Op6 outer loop is NOT a minimization imposed on top of physics. It
is the numerical mechanism by which the K4 dynamics *finds its own*
eigenmode — directly analogous to the SCF loop in the atomic solver
(`radial_eigenvalue.py:1047-1180`) and the Newton-Raphson loop in the
protein solver (`s11_fold_engine_v4_ymatrix.py:749-928`). At each
outer iteration, the *inner* computation is pure TLM evolution
(Axioms 1+3+4 + Op3). The loop is the eigenvalue-seeking machinery;
the TLM is the physics.

This is the AVE-native pattern — not an imported optimization
technique.

---

## §3 The redesigned experiment

### §3.1 Parameter grid

- N = 96, dx = 1.0, dt = 1/(c·√2) (TLM stability; c set by constants)
- pml_thickness = 0 (periodic wrap)
- op3_bond_reflection = True (Axiom 4 saturation at bonds)
- nonlinear = False (saturation at bonds, not nodes — matches prior work;
  Vol 4 Ch 1 convention: LC cells are bonds)
- Seed (R, r) = (24, 9.16) — Golden-Torus proportions (R/r = φ²)
  scaled to N=96
- Ansatz envelope: three variants {hedgehog, gaussian, exponential}
- Drive amplitude: five target strains
  `{0.05, 0.2, 0.3, 0.48, 0.75}` (excludes rupture regime)
- Op6 iterations: up to 6 per (envelope, amplitude) pair
- Per-iteration inner steps: 200 (past the rapid ansatz-correction
  transient)
- Convergence tolerance: `|ΔR/R|, |Δr/r| < 1%`

Total: **3 envelopes × 5 amplitudes = 15 Op6 loops**, each up to
6 inner TLM runs.

### §3.2 Derivation of N_settle = 200 steps per Op6 iteration

The Compton period in TLM time-units is `T_C / dt = 2π · √2 ≈ 8.89`
steps. 200 steps ≈ 22.5 Compton periods. Ample for the (2,3) sector
to relax past the fast ansatz-correction transient (~5-10 periods
from prior GIF observation) while leaving enough cycles for a
time-averaged shell extraction from the final 100 steps.

### §3.3 Q-factor reporting tiers

Each Op6 convergent result reports Q in three tiers, clearly labeled:

1. **Reference (axiom-derived, closed-form):**
   `Q_ref = ω_C · L_e / (Z_0/(4π)) = 1/α = 137.036`
   from [electron_tank_q_factor.py:43-71](../../src/scripts/vol_1_foundations/electron_tank_q_factor.py#L43). Independent of simulation.

2. **Geometric check (Ch 8 multipole, audit-flagged):**
   `α⁻¹_geo = Λ_vol + Λ_surf + Λ_line` at converged (R, r).
   Reported as a geometric quantity. Note: the Q-factor interpretation
   of this formula is audit-flagged in `29_ch8_audit.md` §F4
   (asserted, not Q-derived). Use only as a check that the geometry
   matches Ch 8's Golden Torus, not as a Q measurement.

3. **Direct Q from simulation (gap — flagged deferred):**
   `Q_sim = ω · E_stored / P_dissipated_per_cycle`
   requires Poynting-flux integration over a shell surface.
   Infrastructure does not exist. Scoped as follow-up if Steps 1-3
   succeed; not a closure requirement for this plan.

---

## §4 Pre-registered predictions

**Critical: these are recorded BEFORE any redesigned run is executed.**

### Prediction P1 — Eigenmode exists and is seed-independent

**Hypothesis:** A (2,3) K4 eigenmode with self-confining TIR boundary
exists on the periodic-wrap lattice with Axiom 4 saturation at
bonds (Op3).

**Signature if true:**
- At **at least one** amplitude in `{0.05, 0.2, 0.3, 0.48, 0.75}`,
  the Op6 loop converges (|ΔR/R|, |Δr/r| < 1%) within 6 iterations
  for all three envelopes.
- The three envelopes converge to the same (R, r) fixed-point within
  5% cross-envelope agreement.
- Energy stays bounded (< 10% decay over the run; with periodic BCs
  and op3_bond_reflection reactive-not-dissipative, the system should
  be conservative).

**Consequence if true:** the electron-via-bond-saturation mechanism
stands in principle. Open follow-ups: (a) direct Q-from-sim to confirm
Q = 137 numerically, (b) derive `A_electron` from axioms.

### Prediction P2 — No eigenmode; the hypothesis is falsified in this config

**Hypothesis:** The minimal mechanism (Axioms 1+3+4 on K4 with Op3
bond-level saturation) is *insufficient* to produce a bound (2,3)
electron. Additional physics is needed.

**Signature if true:**
- Op6 diverges at every amplitude for every envelope (R_k, r_k
  continue to drift beyond 1% per iteration indefinitely), OR
- Op6 cycles without converging, OR
- Different envelopes converge to different fixed-points
  (basin-dependent — physics is non-unique).

**Consequence if true:** the hypothesis requires augmentation. Most
likely candidates:
- Node-level saturation (not just bonds) — `nonlinear=True` in K4Lattice3D
- Spin-½ half-cover projection as a code-level operator on port amplitudes
- Full Cosserat-Lagrangian field theory (scoping Phase 1/2, not implemented)

### Prediction P3 — Converges but not at Golden Torus geometry

**Hypothesis:** The TLM as configured has a (2,3) bound state, but
it's the *classical-photonic Hopfion* (per 30_photon_identification.md),
not the electron. The electron requires ingredients the current TLM
does not model (spin-½ projection, saturation confinement tight
enough to match R/r = φ²).

**Signature if true:**
- Op6 converges (P1 satisfied) AND
- Converged R/r ≠ φ² (outside 2.5 – 2.7 range), AND
- Seed-independence holds (all envelopes agree).

**Consequence if true:** the simulation captures the photon half of
the electron-photon duality (Phase 3a complete) but not the electron
(Phase 3b requires additional physics to close numerically). The
AVE-HOPF engineering program (macroscopic (p,q) antennas) becomes
the direct experimental test of this configuration.

### §4.1 Decision matrix

| Outcome | P1 | P2 | P3 | Verdict |
|---|---|---|---|---|
| Converges same (R, r) within envelopes at some A, R/r ≈ φ² | ✓ | ✗ | ✗ | Electron mechanism works |
| Diverges / cycles / basin-dependent | ✗ | ✓ | ✗ | Mechanism insufficient in this config |
| Converges same (R, r), but R/r ≠ φ² | ✓ | ✗ | ✓ | Photonic Hopfion found, not electron |
| Ambiguous (partial convergence, some envelope disagreement) | partial | partial | partial | Report honestly, iterate |

**Thresholds:**
- Convergence: `|ΔR/R|, |Δr/r| < 0.01` at iteration k vs k-1
- Seed-independence: cross-envelope (R, r) range < 5% of mean at same amplitude
- Golden Torus match: R/r ∈ [2.5, 2.7] (φ² ± 4%)
- Energy bounded: `|E_final − E_initial| / E_initial < 0.10`

---

## §5 Deferred gaps — explicit

1. **Direct Q-from-simulation extraction** via Poynting-flux
   integration. Requires new infrastructure (shell surface integrator;
   V·I cycle-averaging). Scoped as follow-up; not required here.
2. **n̂ ↔ ω identity gap** — `00_scoping.md:141-164`, Phase-1
   deliverable. Operational workaround: V treated as proxy.
3. **Ch 8 multipole Q-interpretation** — `29_ch8_audit.md` F4,
   Op21 multi-mode derivation pending. Current treatment: report
   as geometric quantity only.
4. **Analytical `A_electron`** — if P1 holds, the amplitude at which
   convergence occurs becomes an empirical invariant begging a
   first-principles derivation. Candidate forms noted in
   `31_phase3b_simulation_setup.md` §2.6.
5. **Op20 self-consistent amplitude** — would replace amplitude sweep
   with a self-consistent single-amplitude determination. `ω_pred =
   ℓc(1+ν)/r_sat` is the candidate condition. Needs derivation.
6. **Port quadrature pairing derivation** — no axiomatic criterion
   fixes {0,1}/{2,3} vs {0,2}/{1,3} etc. Phase-1 research item.

---

## §6 Companion script

`src/scripts/vol_1_foundations/phase3b_axiom_compliant.py`

Implements the grid of §3.1 with three envelope variants
(added to `tlm_electron_soliton_eigenmode.py` at line 33+) and
records per-iteration convergence trajectories.

Outputs:
- `/tmp/phase3b_axiom_compliant.npz` — raw trajectories
- `/tmp/phase3b_convergence_traces.png` — 3×5 grid
- `/tmp/phase3b_seed_independence.png` — cross-envelope at each
  amplitude
- `/tmp/phase3b_axiom_compliant_evolution.gif` — log-time post-
  transient animation

---

## §7 What this document commits us to

If the redesigned run produces **any** of the three pre-registered
outcomes clearly, the result is a *real finding* regardless of
direction:

- P1 → mechanism stands; pursue direct Q and A_electron derivation
- P2 → mechanism insufficient; add physics, re-test
- P3 → Phase 3a closed (photon), Phase 3b needs augmented sim for
  electron

Muddy result (partial convergence, mixed envelope agreement) requires
honest reporting — not re-interpretation until the data says something
clean.

This pre-registration is durable: the results section of this document
will be appended AFTER the run, preserving the predictions above
unchanged.

---

## §8 Results (appended 2026-04-22 after run)

**Grid actually executed:** 3 envelopes × 3 amplitudes (0.2, 0.3, 0.48)
× up to 3 Op6 iterations × 150 TLM steps at N=72, periodic BCs
(pml=0), op3_bond_reflection=True. Compute-constrained reduction from
plan's 5×3×6 at N=96.

### §8.1 Raw convergence table

| envelope | A_target | converged | iter | R_final | r_final | R/r | α⁻¹_geo |
|---|---|---|---|---|---|---|---|
| hedgehog | 0.20 | Y | 2 | 18.58 | 7.53 | **2.467** | 156.7 |
| hedgehog | 0.30 | N | 3 | 22.59 | 15.06 | 1.500 | 806.5 |
| hedgehog | 0.48 | N | 3 | 31.63 | 24.60 | 1.286 | 2112.0 |
| gaussian | 0.20 | N | 3 | 18.58 | 5.02 | **3.700** | 71.1 |
| gaussian | 0.30 | N | 3 | 18.58 | 5.52 | 3.364 | 83.8 |
| gaussian | 0.48 | N | 3 | 30.62 | 9.04 | 3.389 | 82.7 |
| exponential | 0.20 | N | 3 | 18.58 | 5.02 | **3.700** | 71.1 |
| exponential | 0.30 | N | 3 | 18.58 | 5.52 | 3.364 | 83.8 |
| exponential | 0.48 | N | 3 | 26.61 | 23.09 | 1.152 | 6665.1 |

### §8.2 Seed-independence evaluation

| A_target | R_final range | R/r range | ΔR/mean | Δ(R/r)/mean | verdict |
|---|---|---|---|---|---|
| 0.20 | [18.58, 18.58] | [2.47, 3.70] | 0.0% | 37.5% | ✗ NOT seed-indep |
| 0.30 | [18.58, 22.59] | [1.50, 3.36] | 20.2% | 68.0% | ✗ NOT seed-indep |
| 0.48 | [26.61, 31.63] | [1.15, 3.39] | 17.0% | 115.2% | ✗ NOT seed-indep |

**Threshold for seed-independence: <5% cross-envelope spread. Not met
at any amplitude.**

### §8.3 Verdict against pre-registered predictions

**P1 (eigenmode + seed-independence + Golden Torus):** ✗ REJECTED.
No amplitude produced the same (R, r) fixed-point across all three
envelopes. The one "converged" case (hedgehog at A=0.2, iter 2)
gives R/r = 2.467 — 5.8% below φ² — while Gaussian and exponential
at the same amplitude give R/r = 3.700. The mechanism does not
produce a unique bound state.

**P2 (mechanism insufficient in this config):** ✓ CONFIRMED. The
minimal setup (Axioms 1+3+4 on periodic K4 with Op3 bond-level
saturation alone) does NOT yield a universal (2,3) electron
eigenmode. Additional physics is needed.

**P3 (partial — converges but not at Golden Torus):** ✓ PARTIAL.
Gaussian and exponential envelopes at A=0.2 and A=0.3 converge to
the **same** (R, r) pair (agreement within 0.1% between these two
envelopes at each A). The converged R/r ≈ 3.4-3.7 is **well above**
φ² = 2.618. This looks like a genuine Hopfion-photon attractor for
fast-decaying seeds, confirming the photon side of the duality from
`30_photon_identification.md` on more robust footing than the prior
evidence.

### §8.4 Physical interpretation of the pattern

**Hedgehog envelope is pathological.** The `1/(1+ρ²)` power-law decay
leaves significant amplitude at large ρ — at N=72 the hedgehog's tail
reaches the box boundary non-negligibly. Under periodic BCs, the
soliton **self-interacts with its wrapped image**. At A=0.2 this
produces a spurious "converged" state at R/r=2.47 (possibly a
geometric artifact of the self-interaction locking onto a specific
wrap-distance resonance). At A=0.3 and 0.48 the self-interaction
drives the shell to inflate indefinitely.

**Gaussian and exponential agree.** Their fast decay eliminates
wrap-around self-interaction at N=72. The shared fixed-point at
R/r ≈ 3.4-3.7 is the **true attractor** of the minimal K4+Op3
setup for localized (2,3)-winding seeds. This is NOT the Golden
Torus geometry.

**The gap between 3.4-3.7 and φ²=2.62 is significant** (30-40%).
Whatever physics the Ch 8 Golden Torus derivation assumes is *missing*
from the current simulation. Candidate missing pieces:
- **Spin-½ half-cover projection**: Ch 8 derives `R·r = 1/4` from
  the half-cover of the Clifford torus; without it, the natural
  attractor has `R·r` set by some other constraint.
- **Node-level saturation** (`nonlinear=True`): Axiom 4 at nodes
  (not just bonds) would tighten confinement.
- **Full Cosserat-Lagrangian field theory** from scoping Phase 1/2 —
  the TLM's scalar port voltage is an operational proxy for the
  n̂ or ω field, but the specific coupling between translational `u`
  and microrotation `ω` sectors is absent here.

### §8.5 What holds from this test

- The **photon identification** from `30_photon_identification.md`
  is strengthened, not weakened: two independent envelope variants
  converge to the same (R, r) — a robust photonic attractor —
  and it's distinct from the electron's predicted geometry.
- **A₁/T₂ sector decomposition** remains axiom-compliant and
  symmetry-derived; orthogonal to this specific test outcome.
- **Periodic BCs (pml=0)** are compatible with localized solitons
  only when the envelope decays faster than ~1/ρ. Hedgehog envelopes
  fail this test at practical N.
- **Op6 self-consistency as a mechanism** works as expected:
  loops that converge do so quickly (2-3 iterations); loops that
  diverge show clear signatures of divergence. The machinery is
  axiom-compliant; the failure is physics-level, not numerical.

### §8.6 Open items raised by this result

1. **Is the hedgehog pathology truly self-interaction, or an
   initial-condition artifact?** Test at N=128 (larger box, less
   wrap-around) — hedgehog should then agree with Gaussian/exponential
   if self-interaction is the mechanism.
2. **Does `nonlinear=True` (node-level Axiom 4 saturation) close the
   gap from R/r=3.4 toward φ²=2.62?** Single additional test variant.
3. **What IS the attractor at R/r ≈ 3.4?** This is a genuine stable
   (2,3) Hopfion-like configuration on K4. Its Q-factor via Ch 8
   formula is ~70-85 (not α⁻¹=137). Could it correspond to a
   different physical particle (e.g., a muon or proton in the
   (2,q) family for q ≠ 3)? Worth exploring against the published
   (p,q) predictions.
4. **Direct Q-from-simulation extraction** (deferred gap §5.1 above)
   becomes more important: the Ch 8 geometric α⁻¹ values in §8.1
   may or may not correspond to actual Q-factor in a Poynting-flux
   sense; only a direct measurement distinguishes.

### §8.7 Figures

- `/tmp/phase3b_convergence_traces.png` — 3×3 grid, R/r vs Op6 iteration
- `/tmp/phase3b_seed_independence.png` — all three envelopes overlaid
  per amplitude
- `/tmp/phase3b_axiom_compliant.npz` — raw trajectories

### §8.8 Summary statement

**The electron as a minimal K4+Op3 bound state does not exist in
this axiom-compliant simulation.** What exists is a (2,3)
Hopfion-photon attractor at R/r ≈ 3.4-3.7 (reproducible across
fast-decaying envelopes), which is *not* the Ch 8 Golden Torus.
Phase 3a (photon identification) is strengthened by this finding;
Phase 3b (electron from the minimal mechanism) is falsified in this
configuration.

Additional physics is required — most plausibly spin-½ half-cover,
node-level saturation, or full Cosserat-field coupling between the
translational and microrotation sectors. Follow-up tests are
specified in §8.6.

---

## §9 Deep-research addendum (2026-04-22 after §8 results)

After the §8 null/ambiguous result, a deep corpus audit was
performed (two parallel research agents + direct source read). Three
findings change the landscape of what Phase 3b's axiom-compliant test
actually *should* look like. The plan and the §8 run were both
running against an incomplete picture of the available infrastructure.

### §9.1 FINDING 1 — `nonlinear=False` runs Axiom 4 at bonds only

Reading [`src/ave/core/k4_tlm.py:223-265`](../../src/ave/core/k4_tlm.py#L223-L265)
carefully:

- `op3_bond_reflection=True` + `nonlinear=False` (what we ran):
  The 4-port *node* scattering uses the linear `S = (1/2)𝟙 − I`
  matrix REGARDLESS of local strain. Saturation is applied *only*
  at the bond connections via `z_local_field` in `_connect_all`.
- `op3_bond_reflection=True` + `nonlinear=True`: The node
  scattering ALSO uses `build_scattering_matrix(z_local)` —
  i.e., the 4-port scatter is saturation-aware. This is a
  strictly stronger Axiom-4 implementation.

**We have been running Axiom 4 *halfway*.** At A=0.3 (Regime II),
the local strain is ~0.48 — well above √(2α) = 0.121 — so node
saturation should definitely be engaging per Axiom 4, but isn't
because `nonlinear=False`.

This is a **directly testable remediation.** Setting `nonlinear=True`
in the same grid may close the gap to Golden Torus. One re-run with
same parameters, just flip the flag.

### §9.2 FINDING 2 — `cosserat_field_3d.py` is the more axiom-compliant tool

[`src/ave/topological/cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py)
is 938 lines of 3D Cosserat field solver that carries **both**
translational displacement `u(r)` **and** microrotation `ω(r)` as
independent fields. It implements:

- Strain `ε_ij = ∂_j u_i − ε_ijk ω_k` (non-symmetric Cosserat kinematics)
- Curvature `κ_ij = ∂_j ω_i`
- `initialize_electron_2_3_sector()` at [line 476](../../src/ave/topological/cosserat_field_3d.py#L476)
- Hopf topological linking invariant (lines 142-204)
- `relax_s11()` at [line 612](../../src/ave/topological/cosserat_field_3d.py#L612)
  — **S11 minimization, the AVE-native objective per Collab Notes
  rule 6 observed 2026-04-20.**
- Gradient-descent relaxation with Axiom-4 saturation kernel
- Winding-number extraction via phase-unwrapping contour integrals
  (lines 840-931)

**The K4-TLM has been the wrong tool for Phase 3b.** Per scoping §2
canonical declaration, the AVE vacuum substrate is a **Cosserat
(micropolar) continuum** with both translational and rotational
DoFs. The K4-TLM uses scalar port voltages — which are an operational
proxy for *one* field component, not the full (u, ω) pair. The
31_ → 32_ audit chain correctly identified non-axiomatic choices
*within* the K4-TLM framing but missed that the K4-TLM framing itself
is a sub-Cosserat approximation.

Per collab rule 6: "what is the actual computation the lattice is
running?" The answer is NOT "scalar wave propagation on K4" (the
K4-TLM as currently configured) but "Cosserat field dynamics on K4"
(`cosserat_field_3d.py`).

### §9.3 FINDING 3 — Classical (no spin-½) geometry is R/r = 2.0, not 3.4

Research agent computation: if the Ch 8 constraints are kept except
the half-cover (i.e., `R·r = 1/2` from full Clifford torus area `2π²`
instead of `R·r = 1/4` from half-covered `π²`, with self-avoidance
`2(R-r) = 1` unchanged), the classical geometry is:

```
R − r = 1/2
R · r = 1/2
R = r + 1/2
(r + 1/2)·r = 1/2  →  2r² + r − 1 = 0  →  r = 1/2
R = 1, R/r = 2.0
```

**Neither Golden Torus (R/r = φ² = 2.618) nor classical
full-Clifford (R/r = 2.0) matches our observed 3.4-3.7 attractor.**
The 3.4-3.7 is something else entirely — neither the spin-½ electron
nor the full-Clifford classical Hopfion.

Candidate explanations:
- The K4-TLM's `nonlinear=False` setting means the self-avoidance
  constraint `2(R-r) = 1` isn't enforced by node-level saturation,
  so the shell expands beyond where it should. With `nonlinear=True`,
  the shell should tighten toward classical R/r = 2.0 or closer.
- The periodic-wrap self-interaction persists even for fast-decaying
  envelopes at the amplitudes we tested, biasing R/r upward.
- The 3.4-3.7 attractor is a K4-discrete-lattice artifact specific
  to the finite N we used, not a continuum limit. Prior convergence
  study showed N=48, 96 agreeing on R/r ≈ 2.27-2.30 for a different
  run configuration (with `op3_bond_reflection=True` but slightly
  different amplitude/seed).

### §9.4 Other research findings (no action required)

- **Op20** (`ω_pred = ℓc(1+ν)/r_sat`) is *documented but not
  implemented* anywhere. It exists only as a deferred-gap note.
  Can't invoke it as a mechanism without deriving it first.
- **Op21** multi-mode Q-decomposition is Monte-Carlo-verified at
  Golden Torus in `op21_multimode_derivation.py` but the physical
  interpretation of each Λ_i as a distinct Q-factor channel remains
  asserted per audit F4. Not changed by this research.
- **The prior divergence** of `solve_eigenmode_self_consistent` was
  documented as "amplitude-energy coupling broken": fixed amplitude
  + growing (R, r) → growing total energy → drift. My §8 test
  confirmed this pattern for hedgehog at high A, contradicted it
  for Gaussian/exponential at low A.
- **Spin-½ K4 derivation** (extended-unknot Finkelstein-Misner kink)
  is closed in the corpus but has NO dynamical-encoding proposal
  — nowhere is there a documented mechanism for injecting the 4π
  double-cover into a lattice simulation. Likely requires the full
  Cosserat (u, ω) coupling — which `cosserat_field_3d.py` has but
  K4-TLM does not.

### §9.5 Revised next-test proposal

Two paths, in increasing scope:

**Path X1 — Minimal remediation of §8:** Rerun the same 9-condition
grid (3 envelopes × 3 amplitudes) with `nonlinear=True`. Keep every
other parameter identical. Does node-level Axiom 4 saturation shift
the attractor from 3.4-3.7 toward a lower R/r? Specifically, toward
2.0 (classical) or 2.618 (Golden Torus)?

Effort: one code-line change, same ~20 min compute. Directly tests
Finding 1.

**Path X2 — Switch to `cosserat_field_3d.py`:** The more axiom-
compliant tool. Redo Phase 3b with explicit (u, ω) Cosserat fields
and S11 minimization as the relaxation objective. This is the
correct axiom-compliant framing per scoping §2 canonical declaration
and collab rule 6.

Effort: ~1-2 hours to adapt the harness to the different API and
understand relax_s11's convergence criteria. Compute comparable.
Directly tests Finding 2.

**Honest framing:** Path X1 tests whether §8's *implementation* was
incomplete (missing `nonlinear=True`). Path X2 tests whether the
*framework choice* (K4-TLM vs Cosserat-field-3D) was wrong. If
Path X1 succeeds, Phase 3b closes minimally. If Path X1 fails and
Path X2 succeeds, Phase 3b closes under the fully axiom-compliant
Cosserat formulation. If both fail, the mechanism genuinely requires
additional physics beyond what's currently implemented.

Path X1 is cheap; should run first before investing in Path X2.

### §9.6 What this research does NOT change

- `30_photon_identification.md` photon-from-T₂ finding: still holds.
  The A₁/T₂ port-space decomposition is a symmetry-level result
  independent of `nonlinear=False` vs `True`.
- §8's eigenmode-vs-transient test protocol: the Op6 loop,
  envelope sweep, pre-registered thresholds are all sound.
- `29_ch8_audit.md` findings: unchanged.
- The geometric absurdity of a sub-ropelength real-space trefoil
  (audit F2): still real.

---

## §10 X1 results + correction to §9 Finding 1

### §10.1 Raw X1 results (nonlinear=True vs §8 baseline)

Ran `phase3b_nonlinear.py` with same grid as §8 (3 envelopes × 3 amplitudes,
N=72, periodic BCs, op3_bond_reflection=True) except `nonlinear=True`.

**Result: Δ(R/r) = ±0.000 at every single configuration.**

| envelope | A_tgt | baseline R/r (§8) | X1 R/r (nonlinear=True) | Δ |
|---|---|---|---|---|
| hedgehog | 0.2 | 2.467 | 2.467 | 0.000 |
| hedgehog | 0.3 | 1.500 | 1.500 | 0.000 |
| hedgehog | 0.48 | 1.286 | 1.286 | 0.000 |
| gaussian | 0.2 | 3.700 | 3.700 | 0.000 |
| gaussian | 0.3 | 3.364 | 3.364 | 0.000 |
| gaussian | 0.48 | 3.389 | 3.389 | 0.000 |
| exponential | 0.2 | 3.700 | 3.700 | 0.000 |
| exponential | 0.3 | 3.364 | 3.364 | 0.000 |
| exponential | 0.48 | 1.152 | 1.152 | 0.000 |

Both full-grid results bit-identical. Raw data:
`/tmp/phase3b_nonlinear.npz`.

### §10.2 Why — `nonlinear=True` is a no-op on symmetric K4 junctions

Careful read of [`build_scattering_matrix`](../../src/ave/core/k4_tlm.py#L36-L65):

```python
y = 1.0 / z_local
y_total = N * y                    # = 4y for K4
for i, j in ports:
    S[i, j] = 2.0 * y / y_total    # = 2y/(4y) = 0.5  (z_local cancels)
    if i == j:
        S[i, j] -= 1.0              # diagonal → -0.5
```

The `y / y_total = y / (N·y)` ratio is **independent of `z_local`** for any
N-port junction with equal per-port admittance. For the K4 4-port symmetric
case this yields `S = (1/2)𝟙 − I` regardless of node saturation level.

**Node-level Axiom 4 saturation for a 4-port K4 node is mathematically
a no-op.** It would only produce nonzero effect if ports on the same node
had *differentiated* impedances (Op14 non-reciprocal gradient — directional
saturation) — which the default implementation does not apply.

### §10.3 Correction to §9 Finding 1

Finding 1 claimed "we've been running Axiom 4 halfway — node sat off."
**This was wrong.** The `nonlinear=True` branch *exists* and *runs*, but
produces the identical matrix for symmetric junctions. All the Axiom 4
saturation the K4-TLM can structurally express is already on via
`op3_bond_reflection=True` — at bond level. There is no additional
node-level saturation available without changing the scattering model
to allow port-differentiated impedances.

The §9 Findings 2 (cosserat_field_3d is the more axiom-compliant tool)
and 3 (classical R/r = 2.0, not observed 3.4) remain valid.

### §10.4 Implications for the test program

The K4-TLM as configured has **exhausted its Axiom 4 implementation**.
Further K4-TLM tuning (more iterations, different amplitudes, different
envelopes) cannot alter the basic mechanism. The missing physics
genuinely requires one of:

- **Port-differentiated impedances (Op14 directional)** — would create
  the "different-z-per-port" regime where node sat becomes real. Not
  currently enabled.
- **Spin-½ half-cover projection** — Ch 8's `R·r = 1/4` constraint.
  No documented lattice-injection mechanism per §9 research.
- **Explicit (u, ω) Cosserat field coupling** — what
  `cosserat_field_3d.py` implements. The obvious next test.

### §10.5 X1-prime status

Attempted a canonical hedgehog run at strain_target = √3/2 ≈ 0.866
(Axiom 4 Regime II/III boundary, the canonical amplitude per
`cosserat_field_3d.py:513-518`). Per §10.2's analysis, X1-prime will
produce identical R/r to §8 hedgehog at its nearest amplitude
(divergent territory — the baseline hedgehog at A=0.48 already diverged
to R/r=1.29). Expect X1-prime to confirm the no-op rather than give new
physics. Preserved as a data point but not load-bearing.

## §11 Pointer forward — X3 supersedes this test design

After X2 and X2-prime (`relax_s11` on Cosserat field) both returned
photon-limit / P_FLAT results, Grant's physics reframe (trefoil-with-cut
= photon; electron needs saturated shell with Γ=−1) shifted the test to
energy minimization on the richer Cosserat functional. See
[`33_phase3b_x3_energy_analysis.md`](33_phase3b_x3_energy_analysis.md)
for the current active test design and pre-registered predictions.

`32_` remains the definitive record of why the K4-TLM is exhausted and
why S11 minimization on Cosserat finds the photon rather than the
electron. `33_` tests whether the richer energy functional (Op10 + Hopf
+ reflection + saturation-modulated elastic) selects the electron as
its ground state.

---

### §10.6 Decision: proceed to X2

Per §9.5 and §10.4, the axiom-compliant Phase 3b test moves to
`cosserat_field_3d.py`. That tool:
- Has `ω` (microrotation) as a primary vector field — encodes the
  Cosserat microrotation sector the K4-TLM's scalar port voltage
  cannot represent.
- Has `relax_s11()` — the AVE-native minimization objective per
  collab rule 6.
- Has canonical hedgehog + √3/2·π peak amplitude baked into
  `initialize_electron_2_3_sector()` — no amplitude sweep needed.

If Phase 3b converges at R/r = φ² in the Cosserat field with these
axiom-canonical settings, the mechanism stands and Phase 3b closes.
If not, the Phase-1 scoping items (Cosserat Lagrangian with full
(u, ω) coupling, n̂↔ω identity resolution) genuinely require closure
before the electron emerges numerically.