# FROZEN EXPECTATIONS — smith-annulus computation lane

Frozen 2026-08-24, BEFORE any numerics were run. Analytic pre-derivations below are
pencil-work priors; the scripts test them. Nothing in this file is edited after the
first script run (results go in the draft's Results section only).

## Regime declaration (binding)

- Phase-space objects throughout: everything in T1 lives in the Γ-plane
  (reflection-coefficient disk), the same coordinate system as the mark's
  `trefoil_gamma` (smith_sim.py:59-68).
- Baseline: cold sub-yield lossless-reactive lattice — uniform Z₀ everywhere,
  Γ=0 on every matched bond (photon-identification.md:113).
- Amplitude grading enters ONLY through the canonical kernel S(A)=√(1−A²)
  (ave-kb/CLAUDE.md:73), via the canonical impedance trajectory Z = Z₀√S
  (resonant-lc-solitons.md:41; master-equation.md:106).
- SECTOR DECLARATION: the graded Γ(A) built from Z₀√S→0 is the
  **A1-longitudinal tank chart** (Γ→−1 short wall; cvr-reflection-smith.md:80).
  The transverse-T2 wall (Z→∞, Γ→+1) is a distinct impedance on its OWN chart
  (same receipt). The bare −1/3 junction floor is a counting fact on whichever
  channel's Z₀ is uniform (translation-circuit.md:189) — sector-agnostic in form,
  used here on the A1 chart. No silent A1/T2 cross-wiring.
- Coordinate fence: the mark's (R=2, r=1) parametrize the Γ-disk radial profile;
  the Golden-Torus (R=φ/2, r=(φ−1)/2, R·r=1/4) are (V_inc,V_ref) phasor-ellipse
  semi-axes (Q-EMBED step-c:36,55). DIFFERENT objects, DIFFERENT coordinates.
  No welding (mark's own fence, smith_sim.py:16-17).

## Model (fixed before running)

One srs bond = lossless Z₀ line, delay θ = ωℓ_node/c. Each end terminates on a
z=3 shunt junction whose other two bonds are matched semi-infinite Z₀ lines
(x38-s11 derivation:15,46), so each end presents Z₀/2 and the end reflection
seen from inside the bond is Γ_end = (½−1)/(½+1) = −1/3, which must equal
scatter_matrix(3)[0,0] = 2/3 − 1 = −1/3 (chiral_lattice.py:81-102).

Graded end reflection, TWO candidate forms (which side of the boundary carries
the saturation is nowhere derived in canon — both are tagged UNDERIVED-CHOICE
at the side-assignment level; the Z=Z₀√S trajectory itself is canonical):

- FORM J (junction/far-side graded): load = √S·Z₀/2 against cold bond reference
  Z₀ → Γ_J(A) = (√S/2 − 1)/(√S/2 + 1).
- FORM B (bond graded, cold junction): bond reference Z₀√S against load Z₀/2
  → Γ_B(A) = (1/2 − √S)/(1/2 + √S).

## Expectations

- **E1 (H1, endpoints).** FORM J: |Γ|(A=0) = 1/3 exactly, |Γ|(A→A_y) → 1
  exactly (Γ→−1, A1 short wall). FORM B: same |Γ| endpoints (1/3, 1) but the
  wall is Γ→+1 (opposite rim phase) — the two forms land on the two opposite
  rim points canon says differ "only in boundary phase" (ave-kb/CLAUDE.md:73).
  H1 verdict expected: PASS on magnitudes for both forms; wall SIGN is
  form-dependent.
- **E2 (matching section).** Composite reflection seen from one exterior
  semi-infinite line: shunt-impedance pencil work gives Γ_comp(θ→0) = −1/2
  (junctions merge into z=4: 2/4−1) and at quarter-wave θ=π/2 the bond
  transforms Z₀/2 → 2Z₀, giving Z_par = (2/3)Z₀ and Γ_comp = −1/5.
  Expectation: YES, composite |Γ| drops BELOW 1/3, minimum 1/5 = 0.2 at
  θ = π/2, with a finite band around it below 1/3; never reaches 0
  (requires Z_in→∞, impossible for real θ). Unitarity (Σ|S|²=1) must hold
  (Axiom-3 lossless).
- **E3 (modes).** Poles of the composite at e^{−2jθ} = 1/(Γ₁Γ₂) = 9:
  θ_n = nπ + j·(ln9)/2, i.e. ω_n = nπc/ℓ_node, Q_n = nπ/ln9 ≈ 1.430·n.
  Very leaky cold resonator (Q₁ ≈ 1.43). Mode shape: SWR = (1+1/3)/(1−1/3) = 2
  on the bond, partial-soft-short ends (voltage minima toward the junctions).
  Graded: Q(A) = nπ / (2·ln(1/|Γ_J(A)|)) → ∞ as A→A_y (TIR closes the leak,
  photon-identification.md:140).
- **E4 (H2, annulus as image).** FORM J: |Γ_J(A)| is MONOTONE from 1/3 to 1 as
  A: 0→A_y, so the annulus [1/3, 1] is exactly the image of the amplitude swing.
  FORM B: |Γ_B| passes through ZERO at √S = 1/2 (A = √15/4 ≈ 0.968) — the trace
  exits the annulus through the chart centre (a matched event), so H2 FAILS for
  FORM B. H2 verdict expected: PASS for FORM J only; the annulus reading
  requires the far/lattice side to carry the grading.
- **E5 (H3, shape).** Mark profile ρ(t) = (2+cos3t)/3 (pure single harmonic,
  ρ∈[1/3,1]). |Γ_J(A(t))| for the quarter-arc kernel with any smooth A(t)
  swinging 0→A_y at tube phase 3t will match the ENDPOINTS but NOT the pure-
  cosine shape (the Möbius∘quarter-arc composition is not a pure cosine in t).
  Expect measurable harmonic distortion (extra harmonics at 6t, 9t, ... at the
  several-percent level — number to be measured). Endpoints-only ALREADY pins
  the mark parametrization: ρ_min = (R−r)/(R+r) = 1/3 ⇒ R/r = 2. Amplitude
  laws to test (both UNDERIVED-CHOICE; canon has NO amplitude-swing statement,
  Q-EMBED absence #2): N1 A(t) = A_y(1+cos3t)/2; N2 A(t)² = A_y²(1+cos3t)/2.
  Also invert: A_req(t) that reproduces the mark exactly, and check whether it
  is any recognizable simple form (prior: it will not be).
- **E6 (T2 widths, small-A closed form).** Near cold, |Γ_J(A)| ≈ 1/3 + A²/9.
  Ranking at onset expected:
  1. saturation-onset operating-point offset at the electron's A1 point
     A=√α (def-vyvsn1): δ|Γ| = α/9 ≈ 8.1e-4 (dominant |Γ|-width);
  2. radiative loading: a FREQUENCY width Δω/ω = 1/Q ≈ 0.70/n cold, but → 0
     at the rim as TIR closes;
  3. drive/back-reaction: second order, δ|Γ| ~ ε₁₁²/9, ≲1e-18 for any
     terrestrial ε₁₁ ~ 1e-9;
  4. thermal floor at T_CMB: A_th² ~ k_B T_CMB/(m_e c²) ≈ 4.6e-10 →
     δ|Γ| ≈ 5e-11.
- **E7 (T3, lock).** First-order ε₁₁ detuning is DELAY-ONLY: δω_n/ω_n =
  −ν_vac·ε₁₁ with ν_vac = 2/7 (Op19, universal_operators.py:1088;
  gravity/__init__.py:45 — extension of a gravity-sector operator to the bond
  lock, tagged UNDERIVED-EXTENSION). Impedance detuning is SECOND order
  (Z = Z₀√S, A=|ε₁₁|: δZ/Z = −ε₁₁²/4 — no linear Z(ε₁₁) coefficient exists
  in canon, pull absence #4). The 1/3 floor is immune to any SYMMETRIC
  (both-ends-equal) bias — it is a counting fact "immune to symmetric
  transformation" (translation-circuit.md:189); only DIFFERENTIAL end bias
  moves |Γ₁Γ₂| off 1/9 and splits the inner edge.

## Hypothesis→verdict mapping (frozen)

- H1 PASS iff both endpoint magnitudes exact to machine precision.
- H2 PASS iff |Γ(A)| monotone onto [1/3,1] (per form).
- H3: "SHAPE" iff max|ρ_model−ρ_mark| < 1e-3 over t for some tested natural
  A(t); otherwise "ENDPOINTS-ONLY" (which still pins R/r = 2).
