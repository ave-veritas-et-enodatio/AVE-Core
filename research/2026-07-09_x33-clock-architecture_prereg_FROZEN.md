# PREREG (FROZEN) — X33: the clock-architecture discriminator (synchronous walk LIFTS vs PINS)

**Date:** 2026-07-09 · **Branch:** `analysis/x33-clock-architecture` (off main @ 37eaded5) · **Task:** X33 (Grant-fired)
**Consumes:** [`research/2026-07-09_srs-vector-band-survey_result.md`](2026-07-09_srs-vector-band-survey_result.md) (the bracket
[5.441, 17.011] ω_C + the "S^{-1/2} normalization divides out stiffness" tell + §7 fork), the #607 review
(pending-Grant single-scale-vs-stiffness-lifted decision).
**Adjudicates:** the vector band-top bracket [5.441, 17.011] ω_C (PR #607's pending fork) and TYPES the Op5 clock.

**Class (consistency-vs-emergence):** **CONSISTENCY / characterization.** A mathematical/numerical typing of the
substrate's OWN band architecture — does the Op5 synchronous scatter+connect walk pin the multi-channel band ceiling
at the tick Nyquist, or does channel stiffness lift it? ω_C = c₀/ℓ_node is an IDENTITY; 1/√3 is a Class-B
manifestation (`ANALYTIC_NETWORK_FACTOR`); ρ* is GR-imported (bisected to ν=2/7). **No CODATA on any verdict path;
this is math + numerics, NOT an empirical vote.**

---

## 0. substrate-native-check (done BEFORE any numerical code, per Operating Principle 1)

- **Dynamics:** K4/srs-TLM **scatter + connect** discrete-time coined walk (Op5). NOT Lagrangian, NOT
  gradient-descent, NOT continuum-Helmholtz, NOT energy-basin. The walk IS the substrate's own time-stepper.
- **Sector:** vector / T2-translational (the γγ-carrier channel), with stiffness anisotropy ρ* = k_a/k_s (axial
  vs shear bond stiffness). Cold / linear (A≪1), Op14 saturation OFF — this is the cold band architecture.
- **Coords (A46):** the observable is a spectral **dispersion ceiling** ω_top(k). In the walk this is the maximum
  **eigenphase** θ = ω·Δt of the one-step unitary — literally an angle on the unit circle (phase-space native). In
  the continuous architecture it is max √eig(D(k)). Both are ω(k) band tops → **matching coordinates** (dispersion
  top vs dispersion top). No real-space-Cartesian vs φ² mismatch.
- **Clock:** the object UNDER TEST is the Op5 tick itself. Synchronous = one universal Δt for all channels.

## 1. pre-test-physics-check (one plumber question, surfaced to Grant BEFORE design)

**Is the vacuum's clock synchronous (one universal tick for every polarization channel) or continuous (each
channel free to tick at its own stiffness-set rate)?** A synchronous LC ladder clocked by one master oscillator
cannot pass a signal faster than one rung per tick regardless of how stiff that rung is — the stiff channel is
clock-limited. A continuum medium lets the stiff channel's wave outrun the soft one. This is the physical fork; the
engine implements whichever we build, so the ENGINE cannot vote — **Grant/corpus must anchor which the vacuum is.**

---

## 2. THE DECIDABLE QUESTION (frozen exactly this way)

Construct the **synchronous multi-channel coined walk honestly** — ONE universal tick, per-channel scatter/coin
derived from the physical **per-channel transmission coefficients** (the energy-normalized shunt-junction scatter,
so the channel stiffness ratio ρ* enters the coin the way power-conservation demands — DO NOT assume the answer) —
on **(i)** the 1D two-channel chain (primary, tractable) and **(ii)** the srs cell (if tractable). Compute its
**exact spectrum**. Compare its ceiling to the **continuous** (lumped ω=√eig D) architecture's ceiling.

### 2a. Coin derivation (frozen construction — no free choice)

At a shunt node where bonds of admittance Y_b meet, Op5 gives the scatter [S] = (I+Y/Y₀)⁻¹(I−Y/Y₀). In
energy-normalized wave amplitudes a_b = √Y_b · U_b the vector coin is the **Householder reflection**

    C_i = 2 |w_i⟩⟨w_i| − I,   |w_i⟩ = stacked blocks √Φ_b · S_i^{−1/2},   S_i = Σ_b Φ_b,   ⟨w_i|w_i⟩ = I_D,

where Φ_b = k_a d̂⊗d̂ + k_s(I−d̂⊗d̂) is the rank-2 bond tensor. This is FORCED by (a) the physical shunt KCL and (b)
unitarity (Σ|a|² conserved = the closed-TLM energy). The one-step walk U(k) = Shift(k)·C, Shift = arc-reversal
permutation with Bloch phase e^{ik·δ} (channel-blind, topological, one bond per tick). ω = ω_link·θ, θ = eigenphase.

## 3. TWO BRANCHES (fork-record-both, frozen)

- **Branch L (walk LIFTS):** the properly-stiffness-weighted synchronous walk's longitudinal ceiling ALSO rises
  ~√ρ* → single-scale is MATHEMATICALLY DEAD (even the tick architecture lifts) → the bracket collapses to the
  lifted reading (~17.01 ω_C), the fork-A floor stands, the longitudinal-only window [2.78, 8.69] MeV is real in
  BOTH architectures.
- **Branch S (walk PINS):** the synchronous walk's ceiling stays at the tick Nyquist (π·ω_link) for ALL channels →
  the architecture fork is REAL (continuous lifts, walk pins) and CANNOT be settled in-engine (each engine confirms
  its OWN architecture — say this explicitly). Record both; name the discriminating OBSERVABLE (the
  **longitudinal-only window**: exists under lifted/continuous, ABSENT under pinned/walk); surface to Grant as an
  empirical/corpus-anchor question.

## 4. ADJUDICATION RULE (frozen — decision rule fixed before the verdict is read)

Compute the honest synchronous-walk ceiling ω_top^walk(ρ*) at ρ* ∈ {1, 9.77337 (canonical), 100, 1000}.

- **If ω_top^walk(ρ*) rises with ρ* (grows like ~√ρ* to within the top-mode polarization factor) → Branch L.**
  Threshold: ω_top^walk(1000)/ω_top^walk(1) > 3 (a genuine lift; √1000 ≈ 31.6, any real lift clears 3×).
- **If ω_top^walk(ρ*) is ρ*-independent (flat to numerical floor) → Branch S.**
  Threshold: |ω_top^walk(ρ*) − π·ω_link| / (π·ω_link) < 1e-6 for every ρ* tested (pinned at the tick Nyquist).

No post-hoc relaxation. If the walk pins to numerical zero, that is decisive; the mechanism (below) must then be
named algebraically, not merely observed.

## 5. GATES (analytic expectations frozen — ALL must pass for the verdict to stand)

| Gate | Condition (frozen) | Analytic expectation |
|---|---|---|
| **G1 scalar-limit** | single channel (k_a=k_s): the honest walk reduces to the validated scalar arccos band | srs: top = π√3 = 5.44140 ω_C, velocity factor 1/√3; 1D chain: top = π (network units) |
| **G2 walk-is-scatter+connect** | the literal energy-normalized coined-walk UNITARY eigenphases equal ±arccos(eig Ã), Ã = S^{−1/2}A(k)S^{−1/2} | max mismatch < 1e-12; walk unitary to < 1e-12 (DO NOT assume the arccos map — derive it) |
| **G3 low-k agreement** | both architectures give the SAME acoustic velocities (VRH) at long wavelength (they agree at the zone CENTER; the discriminator lives at the zone EDGE) | walk/continuous acoustic-slope ratio = single constant across all branches AND directions (spread < 1e-5) |
| **G4 continuous LIFTS** | the lumped ω=√eig(D) ceiling rises with ρ* (the contrast partner) | √λmax(D) grows unboundedly with ρ* |
| **G5 bipartite pin locus** | λ̃_max = eig_max(S^{−1/2}D S^{−1/2}) = 2 EXACTLY for all ρ* (srs bipartite ⇒ π-mode saturates) | λ̃_max = 2.000000 ∀ρ*; this is WHY the normalized-arccos pins |
| **G6 coin eigenvalue locus** | the coin eigenvalues are ±1 independent of ρ*; ρ* enters ONLY the coin eigenVECTORS | eig(C_i) ∈ {+1 (D-fold), −1 ((z−1)D-fold)} ∀ρ* — the algebraic reason the ceiling cannot lift |

**Driver-honesty discriminators apply** (Rule 10): no dead-actuator (N/A here — no PML, closed spectral solve);
the walk unitary is diagonalized directly (no time-domain snapshot ambiguity); reactance-pair N/A (spectral, not
time-domain). The literal walk unitary is built and diagonalized (G2) so the arccos map is DERIVED, not asserted.

## 6. WHERE THE STIFFNESS ENTERS (the survey's "tell", to be shown algebraically)

The survey flagged: "the symmetric S^{−1/2} normalization divides out the stiffness that should lift the top." This
prereg freezes the claim to be proven: **the √Y (=√S) symmetrization is FORCED by power-conservation/unitarity**
(§2a), not a convenient choice; it makes the coin a reflection whose eigenvalues are ±1 for ANY Y (G6); the bipartite
π-mode (G5) then saturates the eigenphase at π regardless of ρ*. So stiffness enters the coin's **eigenvectors**
(reshaping the band, setting the low-k velocities per G3) but is structurally locked OUT of the coin's
**eigenvalues** and hence the ceiling. The normalized-arccos "pin" is the honest walk, not an artifact — that is the
finding to confirm or refute.

## 7. Op5 CLOCK-TYPE IMPLICATION (frozen consequence of the verdict)

- **Branch L ⇒** Op5's tick lifts with stiffness; the engine reads the lifted ceiling; bracket collapses to lifted.
- **Branch S ⇒** Op5 is a PINNING clock (synchronous discrete-time unitary walk); the Op5 engine will ALWAYS report
  the pinned ceiling and CANNOT see the lift; the lifted reading needs a DIFFERENT (continuous-time ω=√eig)
  solver. The bracket is then an **architecture fork**, in-engine-undecidable, resolved only by Grant/corpus anchor.

## 8. Deliverables

prereg (this, FROZEN) → derivation note + numeric driver `x33_clock_architecture.py` → result doc + JSON + WHITE
figure (both architectures' 1D two-channel spectra overlaid). `make verify`. Commit [REVIEW: pending-orchestrator].
PR (DO-NOT-MERGE).

**FROZEN 2026-07-09. No adjudication axis is dropped or relaxed post-hoc (Rule 11).**
