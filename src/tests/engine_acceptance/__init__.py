"""Ground-up substrate-engine acceptance suite — L0 (medium) + L1 (photon).

Each test is a FALSIFIABLE PHYSICS CLAIM with a pre-registered pass/fail bin in
its docstring. The suite is the engine's regression gate per the 2026-06-16
ground-up acceptance-test-driven build plan
(`_orchestration/2026-06-16_groundup-engine-acceptance-plan.md`, §1-§2).

GRID (ratified D-A): the **chiral srs grid** — the v9 chiral Laves / Sunada-K4
trivalent (degree-3, I4_1 32) lattice (`ave.core.chiral_lattice`,
`ave.core.chiral_lattice_vector`, `ave.core.chiral_lattice_dynamics`). The photon
is transverse, so it runs on the vector-TLM layer of the srs grid natively.
Running acceptance tests on the FROZEN srs (loop-gap "v17, transverse-only") does
NOT advance a genesis version — these are CONSISTENCY tests of an existing medium.

CLASS: every test here is CONSISTENCY (reproduce known physics; the engine MUST
pass to be a valid medium) — NOT a chord (a forced dimensionless number). The
chords live at L3-L5 and are out of scope for this L0-L1 build. T0.2 (Z₀) is the
single Class-A identity (Z₀ = √(μ₀/ε₀) by definition); the rest are Class-C
consistency checks via the srs-medium mechanism.

substrate-native-check walk (done before any code, Operating Principle 1):
  * Dynamics  : discrete srs-TLM **scatter + connect** wave propagation
                (NOT Lagrangian / gradient-descent / continuum-Helmholtz /
                energy-basin minimisation). The lattice IS the computation.
  * Sector    : T0.* = scalar V-sector (one scalar per port, unitary TLM);
                T1.* = transverse 2-component VECTOR sector (the photon's two
                E⊥B transverse polarizations carried on the ports). No Cosserat
                micro-rotation and no A1 longitudinal mode are exercised at
                L0-L1 (those are L3/L4).
  * Objective : TLM transmission eigenmode / closed-system energy conservation.
                The one-step operator M = Connect · blockdiag(S) is orthogonal
                (S orthogonal: S^T S = I for the degree-3 Op5 shunt matrix;
                Connect is a port permutation) → every eigenvalue has modulus 1
                → Σ|V_inc|² is conserved exactly. This is the AVE-native
                Γ²+T²=1 unitarity, NOT S₁₁ minimisation, NOT energy-min.
  * Coords A46: observables (energy, amplitude, dispersion ω=ck, front position)
                are real-space / spectral, matching the L0-L1 corpus claims.
                No phase-space φ² / Clifford-torus claim is at issue here, so
                real-space measurement is the correct coordinate system.
  * Saturation: OFF (linear, A << 1). No Op14 local-clock modulation at L0-L1.
  * CP6       : the full V_inc field is the tracked state every step over the
                whole recording window (not a one-phase snapshot), so the
                reactance-pair ambiguity does not arise — energy is conserved by
                construction (orthogonal operator) and verified dynamically.
  * CP7       : the srs net is PBC / CLOSED — NO PML. The PML-cell-exclusion
                corollary is therefore N/A (nothing to exclude); energy is a
                global sum so there is no centroid-of-shell sampling issue.
  * CP9       : every observable is read off the DYNAMICALLY-evolved V field
                (scatter+connect each step), never an algebraic heuristic.
  * CP10      : L0-L1 is free propagation — no confinement / saturation / wall
                rendering, so no bulk-vs-boundary detonation risk.

PBC NOTE (load-bearing for T1.1(c)). The srs medium is a periodic torus: there
is no open free-field boundary and no impedance interface in the bulk, so there
is no macroscopic Γ-discontinuity to reflect off. "Γ≈0, no spurious reflection"
is therefore operationalised as: the fraction of energy that REVERSES its net
propagation direction (back-scatter off lattice discreteness / numerical
interface) stays at the numerical floor. A uniform PBC lattice has no physical
reflector; any measurable back-scatter would be a spurious lattice artifact.

────────────────────────────────────────────────────────────────────────────────
VISUAL-DEBUG LAYER (additive instrumentation — does NOT change any pass/fail bin)
────────────────────────────────────────────────────────────────────────────────
Each test can emit a `<test_id>_debug.png` into research/figures/engine_acceptance/
so the run is visually debuggable: the standard set is an x-t spacetime heatmap
(propagation-axis position × timestep, energy-density color), a filmstrip (1D
profile at t=0,¼,½,¾,T), and an energy-vs-time trace with the max-drift annotated;
per-test extras add the dispersion ω(k) curve (T1.2), the cross-pol leak trace
(T1.3), and the causal-cone info-front slope (T1.4). The figures are recorded off
the SAME engine stepper the functional test runs (`_viz.py`); they are a passive
recorder, not a re-simulation.

Figure emission is GATED on `KF_VIZ` (OFF for a plain `pytest` run, so the physics
path and `make verify` are untouched). REGENERATE ALL FIGURES with one command:

    PYTHONPATH=<worktree>/src KF_VIZ=1 \\
        /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \\
        -m tests.engine_acceptance.regen

(equivalently, `KF_VIZ=1 pytest src/tests/engine_acceptance/ -s`). FLAGSHIP T1.1
note (HARDENED 2026-06-17): the T1.1 seed is now a LOCALIZED, ONE-WAY Gaussian
wave packet (`_medium.oneway_packet`) — single-sign port occupancy suppresses the
counter-propagating partner, so the x-t view is a SINGLE clean diagonal band
translating at the srs network velocity c_net = c_link/√3, and the test ASSERTS
the energy-centroid translates by ≈ c·t (a genuine propagation-distance check),
not just energy conservation. The PRIOR seed (`directional_packet`, a delocalized
cos(k·z) Bloch wave) carries equal ±k content = a STANDING fringe that did NOT
propagate; it is kept as the bottom-row x-t CONTRAST in the T1.1 figure so the fix
is visible side-by-side. The propagation assertion + the clean-diagonal R² are the
new pass/fail content.
"""
