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
"""
