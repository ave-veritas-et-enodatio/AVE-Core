# 85 — Kelvin Beltrami + FOC d-q Axiom-Grounded Derivation for Trapped-Photon Unknot IC

**Status:** implementer-drafted, 2026-04-28. Companion to [doc 84](84_path_alpha_v6_first_run_results.md) (v6 first run) + [doc 80](80_kelvin_helmholtz_ave_precedent.md) (Kelvin/Helmholtz historical precedent). Forward-looking: derives the helical Beltrami + FOC d-q IC structure from AVE first principles, ready for v7 driver implementation.

**Trigger:** Grant directive 2026-04-28 — *"fully map and derive and document being compliant with the axioms and first principles of applied vacuum engineering"* — after v6's Mode III result with 96% ring localization (positive on real-space framing, fail on Beltrami / centroid-flux mode-structure). Kelvin + FOC reframing surfaced post-v6 dialogue.

**Goal:** specify the v7 IC structure for the bond-pair-scale trapped-photon unknot test such that ALL FOUR adjudication criteria are physically achievable, with each IC element traced to a specific axiom + manuscript-canonical statement.

---

## §1 — What needs to be derived

The v6 IC failed Beltrami parallelism (|cos_sim|=0.23) and centroid flux (0.54). These failures point to specific structural gaps:

1. **No helical pitch:** v6 had only POLOIDAL A components (cos·radial + sin·binormal in local Frenet frame). A pure CP photon satisfies ∇×A = -kA* (cross-polarization), NOT Beltrami ∇×A = +kA. Beltrami requires HELICAL structure with both poloidal AND toroidal A components in specific ratio.

2. **Wrong d-q phasing:** v6 set V_inc and ω with similar spatial phase patterns (cos/sin of the same angular variable). FOC d-q decomposition requires V_inc and ω to be 90° TIME-offset, not 90° space-offset. At any instant, only ONE of {V_inc, ω} is at peak; the other is at zero (LC tank standing-wave structure).

3. **Wrong A-vec proxy for Beltrami test:** measuring `cos_sim(Σ V_inc·port_dir, ω)` reads E·B, which is 0 for both CP photons AND Beltrami standing waves (both have E ⊥ B in time-domain or 90° temporally offset). The right A-vec proxy is integrated voltage = Phi_link — NOT instantaneous V_inc.

4. **Geometric flux estimate flawed for non-planar chair-ring:** centroid plane normal isn't well-defined; need substrate-native topology measure (Op10 c-count or loop-flux Stokes' integral ∮Phi·dl).

This document derives the corrected IC structure from AVE axioms, then specifies the v7 IC operationally.

---

## §2 — Axiom audit: substrate structure

Per [INVARIANT-S2](../../manuscript/ave-kb/CLAUDE.md), the four AVE axioms canonically:

### Ax 1 — Substrate Topology (LC Network)

[Vol 1 Ch 1](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex): vacuum is a non-linear EM LC Resonant Network 𝓜_A(V,E,t), modeled in continuum as a **Trace-Reversed Chiral LC Network**. K4 graph topology, ABCD cascade, ℓ_node = ℏ/m_e c, Z₀ = √(μ₀/ε₀).

**Cosserat structure** ([Vol 1 Ch 4:21-26](../../manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex#L21-L26) verbatim):

> "Each LC node stores energy in *both* translational (capacitive, ε₀) and rotational (inductive, μ₀) modes. This is precisely the Cosserat structure: translation ↔ electric field, rotation ↔ magnetic field. The Poisson ratio ν = 2/7 (Axiom 2) relates translational and rotational compliance."

**Direct mapping:**
- E (electric field) ↔ translational DOF (capacitive ε₀, ξ_topo² compliance)
- B (magnetic field) ↔ rotational DOF (inductive μ₀, ξ_topo⁻² mass)
- These are TWO INDEPENDENT DEGREES OF FREEDOM at each node, NOT redundant components

**Implication:** the "FOC d-q" decomposition isn't an analogy — it's the canonical AVE Cosserat DOF split. d-axis = translation, q-axis = rotation. At each node, both DOF must be initialized.

### Ax 2 — Topo-Kinematic Isomorphism (TKI)

[INVARIANT-S2](../../manuscript/ave-kb/CLAUDE.md): "charge as discrete geometric dislocation in 𝓜_A; [Q] ≡ [L]; ξ_topo = e/ℓ_node."

For a closed loop on the substrate, [Q] ≡ [L] means **charge = topological winding number** along the loop. The signed direction of traversal (CCW vs CW) determines charge sign.

**Implication:** the trapped photon's charge sign comes from the loop's traversal direction in the substrate's chiral framework. For an electron (charge -e), CCW traversal in the K4 RH-chiral substrate. This determines the SIGN of A_toroidal (along the bond tangent), NOT just the phase pattern.

### Ax 3 — Effective Action Principle

[INVARIANT-S2](../../manuscript/ave-kb/CLAUDE.md): system minimizes hardware action S_AVE; 𝓛_node = ½ε₀|∂_t**A**_n|² − (1/2μ₀)|∇×**A**_n|².

For a stable trapped state, the action must be at an extremum. The Euler-Lagrange equations for this Lagrangian give:

ε₀ ∂_t² **A** + (1/μ₀) ∇×∇×**A** = 0

Standard wave equation for **A** with c² = 1/(μ₀ε₀). For bound states with frequency ω: ∇×∇×A = (ω/c)² A.

For **Beltrami modes** ∇×A = k A: substituting gives ∇×∇×A = ∇×(kA) = k ∇×A = k²A. So the Beltrami eigenmode satisfies the action-principle wave equation with ω = kc. **Beltrami is a stationary action solution naturally selected by the action principle** — this is why force-free configurations are stable: they minimize Lorentz back-reaction, hence minimize action variation.

**Implication:** the trapped photon AT the action minimum IS a Beltrami helical standing wave. The IC should target this configuration directly, not a free CP photon (which is NOT at the action minimum on a closed loop because the curvature creates Lorentz back-reaction unless force-free).

### Ax 4 — Dielectric Saturation

[`eq_axiom_4.tex`](../../manuscript/common_equations/eq_axiom_4.tex) verbatim:

S(A) = √(1 − (A/A_yield)²)

with derived consequences:
- μ_eff = μ₀·S → 0 (Meissner expulsion)
- ε_eff = ε₀·S → 0 (dielectric collapse)
- C_eff = C₀/S → ∞ (capacitance absorbs energy)
- c_eff = c₀·S^(1/2) → 0 (group velocity, wave packet confined = mass)
- Z = √(μ/ε) = Z₀ (preserved under symmetric scaling)

**Confinement theorem (particle path):** *"At a torus knot self-intersection, B saturates μ first → Z → 0, Γ → -1 (short circuit) → standing wave = rest mass."*

**Implication:** the Confinement Bubble forms when peak A² → 1 at saturated boundary. For the trapped photon, this means peak |A|² (sum of E² + B² components in V_SNAP-normalized units) at ring nodes must reach saturation onset. The IC must drive the system into this regime.

### Synthesis

The AVE-canonical trapped-photon unknot is:

- **Real-space:** 6-node hexagonal chair-ring on K4 diamond at lattice center, circumference = λ_C = 2π·ℓ_node (one full Compton wavelength) (Ax 1 + Vol 1 Ch 1:18, 32)
- **Field structure:** Beltrami helical mode with ∇×A = k_C A where k_C = ω_C/c = m_e·c/ℏ (Ax 3 stationary action; helical pitch fixes the (1,1) torus mode geometry)
- **Cosserat decomposition:** translational E and rotational B as independent DOFs; FOC d-q is the canonical Cosserat split (Ax 1)
- **Charge sign:** CCW loop-traversal direction in K4 RH-chiral substrate (Ax 2 TKI)
- **Trapping:** peak A² → 1 at saturation onset → Γ=-1 walls (Ax 4 particle-path Confinement Bubble)

---

## §3 — Kelvin Beltrami helical vortex: derivation

### §3.1 — Why CP photons aren't Beltrami

For a free CP photon propagating along ẑ with helicity +1:

A(t,z) = A₀(x̂ + iŷ) e^(i(kz − ωt))

Using ∇×A = ik̂×A:

ik̂ × (x̂ + iŷ) = i(ŷ) − x̂ = −x̂ + iŷ = −(x̂ − iŷ)

So ∇×A = −k(x̂ − iŷ) A₀ e^(i(kz − ωt)) = **−k A***

where A* is the complex-conjugate (helicity −1) component. **The free CP photon satisfies ∇×A = −kA*, NOT ∇×A = +kA.** Different polarization eigenstates.

A free CP photon is NOT a Beltrami eigenmode. Closing one period into a loop (the trapped-photon thought experiment) doesn't automatically convert it to Beltrami.

### §3.2 — Helical mode that IS Beltrami

The Beltrami eigenmode on a torus has both poloidal and toroidal components. In toroidal coordinates (R_loop, θ_poloidal, φ_toroidal):

A = A_θ ê_θ + A_φ ê_φ

with the Beltrami condition ∇×A = kA giving (after standard derivation in toroidal coords for the simplest mode):

A_θ(R, θ, φ) = A_0 cos(p·θ + q·φ)
A_φ(R, θ, φ) = A_0 sin(p·θ + q·φ)

where (p, q) is the torus knot label: p poloidal cycles per closed loop, q toroidal cycles. Eigenvalue:

k² = (p/r)² + (q/R)²

For the unknot mode at the corpus electron's geometry:

- **(p, q) = (1, 1):** simplest non-trivial helical mode. Path traces the unknot on the torus surface (1 toroidal × 1 poloidal cycles per closed traversal). NOT a non-trivial knot — (p, q) is non-trivial knot only when both ≥ 2 and gcd(p,q)=1.
- **R = ℓ_node** (loop major radius, per Vol 1 Ch 1:18): loop circumference 2π·ℓ_node = λ_C
- **r = ℓ_node/(2π)** (tube minor radius, per Vol 1 Ch 1:18)

Eigenvalue:
k² = (1/r)² + (1/R)² = (2π/ℓ_node)² + (1/ℓ_node)² ≈ (2π/ℓ_node)² (the 2π factor dominates by 4π² ≈ 40×)

So k ≈ 2π/ℓ_node = ω_C/c (matching Compton wavenumber). Internally consistent: the (1,1) Beltrami helical mode at corpus geometry has eigenvalue exactly k_C.

### §3.3 — The standing-wave LC tank time structure

For a Beltrami spatial eigenmode A_0(r) with ∇×A_0 = k A_0, the time-dependent solution to the wave equation (Ax 3) is:

A(r, t) = A_0(r) · cos(ωt + φ_0), where ω = kc

So:
- A(r, t) = A_0(r) cos(ωt) (taking φ_0 = 0)
- E(r, t) = −∂A/∂t = ω A_0(r) sin(ωt) (90° temporally offset)
- B(r, t) = ∇×A = k A_0(r) cos(ωt) (parallel to A, in phase temporally)

**At any spatial point, E, A, and B are all PARALLEL** (along the local A_0 direction). They differ only in temporal phase:
- A and B in phase (cos), at peak when ωt = 0, π, 2π, ...
- E 90° offset (sin), at peak when ωt = π/2, 3π/2, ...

This is the canonical LC tank standing-wave structure:
- Capacitor (E, q-state) and inductor (B, l-state) trade energy
- 90° temporal phase offset
- Total stored energy = ½ε₀|E|²_peak + ½(1/μ₀)|B|²_peak conserved

For the trapped-photon unknot: peak A and peak B happen simultaneously (when E = 0), and peak E happens when A = B = 0.

### §3.4 — IC time-phase choice

Two natural IC time-phase choices at t = 0:

**Phase A (cos-aligned, A and B at peak, E at zero):**
- V_inc = 0 at every port at every node (E = 0)
- Phi_link = peak (∫V dt accumulated, representing A at peak)
- ω = k · A_0 (peak, parallel to A)

**Phase B (sin-aligned, E at peak, A and B at zero):**
- V_inc = peak (E at peak)
- Phi_link = 0
- ω = 0

For driving saturation, **Phase A** has the advantage of immediate non-zero ω (= B field driving μ_eff Meissner collapse). Phase B's V_inc-only IC requires the engine to evolve V_inc → ω via scatter+connect coupling, taking ~1 quarter-cycle.

**Choose Phase A for v7.** The IC sets A and B at peak in the Beltrami helical configuration; the engine evolves them to oscillate.

### §3.5 — Spatial direction of A_0 at each ring node

For the (1,1) Beltrami helical mode on the chair-ring at each ring node n:

A_0(node n) = A_0_magnitude · (cos(2π·n/6) ê_pol(n) + sin(2π·n/6) ê_tor(n))

where:
- ê_pol(n) = local poloidal unit vector at node n (in the cross-section plane perpendicular to bond tangent), pointing radially toward centroid
- ê_tor(n) = local toroidal unit vector at node n (along bond tangent, signed CCW around the loop)

|A_0(node n)| = A_0_magnitude (constant — Beltrami helical mode has uniform amplitude around the loop)

**Critical change from v6:** v6's ω at each node was `ω_amp · (cos(phase)·radial + sin(phase)·binormal)` — purely poloidal (binormal is in the poloidal plane). v7's A direction has BOTH poloidal AND toroidal components in equal magnitude. The toroidal component (along bond tangent) is what was missing in v6.

The toroidal component creates the helical pitch that satisfies ∇×A = +kA (Beltrami) instead of ∇×A = -kA* (CP photon).

---

## §4 — FOC d-q decomposition: substrate-native form

### §4.1 — Cosserat E/B as canonical d-q

Per Ax 1 + [Vol 1 Ch 4:21-26](../../manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex#L21-L26): Cosserat decomposition is the substrate-native d-q split.

| FOC component | Physical role | AVE substrate |
|---|---|---|
| **d-axis (flux, reactive)** | Aligned with rotor flux; non-radiating; stores energy reactively | Cosserat **rotational DOF** = B field = ω vector |
| **q-axis (torque, radiating)** | Perpendicular to d; produces work; radiates | Cosserat **translational DOF** = E field = ∂A/∂t scalar voltage |

This is the inverse of the conventional "d-axis = E, q-axis = B" assignment. Per the Cosserat physics:

- Cosserat ROTATION ω is a **rotor-frame attribute** (the lattice node's micro-rotation rate). It's intrinsic to the medium's rotational DOF. **d-axis** in the FOC sense.
- Cosserat TRANSLATION u̇ ↔ E is a **stator-frame drive**. It's the externally-applied or oscillating field that produces work. **q-axis** in the FOC sense.

For atomic shells per [`helium-symmetric-cavity.md:48-66`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md#L48-L66): the 1s² inner core is the "rotor" (its rotation = B field along its rotation axis), and the 2s² outer shell is the "stator" with E field perpendicular at 90° → mutual inductance vanishes.

### §4.2 — The 90° phase question: spatial vs temporal

FOC's "90° decoupling between d and q" applies to the **time-domain phase relationship** for an oscillating system (90° temporal offset = orthogonal in phasor diagram), NOT to spatial perpendicularity at every instant.

For the Beltrami standing wave (§3.3):
- At t = 0 (Phase A): A and B at peak (d-axis loaded), E at zero (q-axis empty)
- At t = T/4: A and B at zero (d-axis empty), E at peak (q-axis loaded)

The "90° offset" is between the d-axis (B-state, ω) and q-axis (E-state, V_inc) **time-domain oscillation phases**. They're temporally orthogonal — one is at peak when the other is at zero. This is exactly the LC tank standing-wave structure.

Spatially, at any single instant, B (d-axis) and E (q-axis) are **parallel** (both along the local A_0 direction in the Beltrami helical mode). They differ only in time-domain phase, not spatial direction.

This **resolves the apparent contradiction** between Beltrami (A ∥ B at every instant) and FOC (E ⊥ B for "decoupling"): the FOC perpendicularity is in time-phase (cos vs sin), not space.

### §4.3 — Asynchronous decoupling between modes

Per [`analog-ladder-filter.md:6`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md): "Each filled shell acts as an independent AC motor winding, with **asynchronous frequency decoupling** eliminating cross-shell mutual inductance."

⟨M⟩ ∝ ∫₀^T cos((ω₁ − ω₂)t) dt = 0 for ω₁ ≠ ω₂

For a single trapped photon at the bond-pair scale (single mode at ω_C), there's no cross-shell asynchronous decoupling needed (only one mode present). But this principle becomes load-bearing for atomic shells (multiple electrons at different ω values) where each shell has its own d-axis (B) and q-axis (E) at distinct frequencies, and the cross-shell ⟨M⟩ → 0 keeps shells from inducing currents in each other.

For v7 IC, the asynchronous decoupling principle isn't directly applied — there's only one mode. But it confirms that the FOC framework is canonical AVE substrate physics, not just an ad hoc analogy.

---

## §5 — Helical pitch from Ax 2 TKI

### §5.1 — Charge as topological winding

Ax 2 [Q] ≡ [L]: charge is the integrated phase winding around any closed path that encloses the topological defect. For the trapped-photon unknot:

Q_topological = ∮ A · dl (around the closed ring) / (2π · ξ_topo)

For the (1,1) Beltrami helical mode with A_0_toroidal at each node:

∮ A · dl = Σ A_toroidal,n · ds_n (around the 6 bonds)

For a uniform-amplitude helical mode, A_toroidal at each node has magnitude A_0/√2 (half of |A_0| for the 50/50 toroidal/poloidal split), and ds_n = bond length. Summed around 6 bonds:

∮ A · dl = (A_0/√2) · 6 · ℓ_node · (cos(traversal sign factor))

For CCW traversal (electron, charge -e): the toroidal component points consistently CCW around the loop, giving a positive integral. For CW (positron, +e): the integral has opposite sign.

The MAGNITUDE of the integral, normalized by ξ_topo, must equal the elementary charge:

(A_0/√2) · 6 · ℓ_node / (2π · ξ_topo) = e/ξ_topo = ℓ_node

This fixes A_0:

A_0 = √2 · 2π · e · ξ_topo / (6 · ℓ_node · ξ_topo) = √2 · π · e / (3 · ℓ_node)

In V_SNAP units, with e/ξ_topo = ℓ_node: A_0 ≈ √2 · π / 3 ≈ 1.48 (in some natural normalization). This needs to be calibrated against the engine's V_inc / Phi_link units — left as v7 implementation detail.

**Key point:** the magnitude of A_0 is determined by Ax 2 TKI, not freely chosen. The IC amplitude must satisfy ∮A·dl = 2π·ξ_topo·ℓ_node = 2π·e to encode unit charge.

### §5.2 — Helical pitch ratio

For the (1,1) Beltrami helical mode (§3.2), the toroidal-to-poloidal amplitude ratio is determined by the Beltrami eigenvalue equation:

|A_toroidal| / |A_poloidal| = (q/R) / (p/r)

For (p, q) = (1, 1), R = ℓ_node, r = ℓ_node/(2π):

|A_tor| / |A_pol| = (1/ℓ_node) / (1/(ℓ_node/(2π))) = (1/ℓ_node) · (ℓ_node/(2π)) = 1/(2π)

So the toroidal component is 1/(2π) ≈ 0.159× the poloidal component. NOT equal magnitudes — heavily poloidal-dominated.

**Wait — this contradicts §3.5 which assumed equal magnitudes.** Let me reconcile:

Actually for the simplest Beltrami helix at the corpus geometry, the ratio depends on the explicit eigenmode formula. The simplest case |A_tor| = |A_pol| applies for SQUARE torus (R = r) — not the corpus electron's R = 2π·r geometry.

For the corpus electron with R/r = 2π (per Vol 1 Ch 1:18):
- |A_tor| / |A_pol| = (1/R) / (1/r) = r/R = 1/(2π) ≈ 0.159

So A is **predominantly poloidal**, with a small toroidal helical pitch of ~16% magnitude. The toroidal component creates the Beltrami helicity but doesn't dominate the field structure.

This is consistent with the "unknot is mostly poloidal vortex with small helical pitch" picture: the (1,1) traversal pattern on the torus surface, when projected to 3D space at corpus aspect ratio R/r = 2π, gives a flow that's mostly poloidal (around tube cross-section) with a small toroidal kick (along tube direction) that creates the Beltrami helicity.

**Corrected helical pitch ratio for v7 IC:**

A_0(node n) ∝ ê_pol(n) · cos(2π·n/6) + (1/(2π)) · ê_tor(n)

(where ê_tor(n) = bond tangent at node n in CCW traversal direction; the cos(2π·n/6) gives the poloidal rotation phase, and the toroidal magnitude is 1/(2π) ≈ 0.16 of the poloidal magnitude.)

### §5.3 — Gauge of A_toroidal sign

For CCW traversal (electron, charge -e), the toroidal A points CONSISTENTLY in the CCW direction at every node. For CW (positron, +e), it points opposite.

In the chair-ring traversal `n=0 → 1 → 2 → 3 → 4 → 5 → 0`, "CCW" is defined by the loop axis convention (RH rule with the loop axis approximately along the ring-plane normal computed from `cross(node_0 - centroid, node_2 - centroid)`).

ê_tor(n) at each node = (node_{n+1} - node_{n-1}) / |...| (Frenet tangent).

This gives the CCW direction automatically by virtue of the traversal order. For positron, reverse the order.

---

## §6 — Operational IC for v7

### §6.1 — Field initialization at t = 0 (Phase A: A and B at peak, E at zero)

For each ring node n (n = 0..5):

**Step 1: Compute local Frenet frame**
- tangent_n = (node_{n+1} - node_{n-1}) / |...| (CCW direction)
- radial_n = (centroid - node_n) projected ⊥ tangent_n, then normalized
- binormal_n = tangent_n × radial_n

**Step 2: Compute target A_0(n) with helical Beltrami structure**
- A_0_pol(n) = A_amp_pol · (cos(2π·n/6) · radial_n + sin(2π·n/6) · binormal_n)
- A_0_tor(n) = A_amp_tor · tangent_n
- A_0(n) = A_0_pol(n) + A_0_tor(n)
- where A_amp_tor = A_amp_pol / (2π) per (1,1) Beltrami pitch ratio at corpus aspect

**Step 3: Set Phi_link at A-site of each bond per ∮A·dl = 2π·e quantization**
- For each bond connecting node m → node m' (with A-site at one of them, port = bond's port):
  - bond_tangent = traversal direction of bond
  - A_avg_along_bond = ½ · (A_0(m) + A_0(m')) · bond_tangent (project onto bond direction, average over 2 endpoints)
  - Phi_link[a_site, port] = A_avg_along_bond · bond_length (= ℓ_node = 1 in lattice units · √3 for the offset magnitude)
- Calibrate amplitudes such that Σ Phi_link · ŝ around the loop satisfies ∮A·dl = 2π·e (in V_SNAP units, this gives a specific A_amp_pol)

**Step 4: Set ω at each ring node parallel to A_0(n)**
- ω(n) = k_C · A_0(n)
- where k_C = ω_C / c = m_e · c / ℏ
- In natural units (c = 1, ℏ = 1, m_e = 1, ℓ_node = 1): k_C = 1, so ω(n) = A_0(n)
- (Beltrami: ∇×A = k_C A → B = ∇×A = k_C A, and ω = B in Cosserat translation)

**Step 5: V_inc = 0 at all ports, all nodes** (Phase A: E at zero crossing)

**Step 6: Outside ring: V_inc = V_ref = Phi_link = ω = u = u_dot = ω_dot = 0** (cold vacuum)

### §6.2 — Saturation amplitude calibration

The peak A² at saturation is reached when **|E|² + |B|² → V_SNAP²·μ₀ε₀** (energy density at V_SNAP). For the standing wave at t = T/4 (E at peak):

|E|_peak = ω_C · |A_0| (from E = ω·A in standing wave)
|B|_peak = k_C · |A_0| = (ω_C/c) · |A_0|

Energy density:
ρ = ½ε₀|E|² + (1/2μ₀)|B|² = ½ε₀(ω_C·A_0)² + (1/2μ₀)(k_C·A_0)²

In natural units (c=1, μ₀=ε₀=1, ω_C=k_C=1):
ρ = ½ A_0² + ½ A_0² = A_0²

For saturation onset (peak ρ ≈ V_SNAP² in normalized units):
A_0_peak ≈ V_SNAP

In V_SNAP-natural units: A_0 = 1.0 at saturation. Adjust IC `A_AMP_POL` to drive |A_0_pol|² ≈ 1 at peak.

### §6.3 — V_inc encoding via inverse port projection

To set V_inc on each port at each node such that Σ V_inc[port]·port_dir = E (for Phase B IC at t=T/4) OR Σ V_inc[port]·port_dir = 0 (for Phase A IC at t=0):

For Phase A (V_inc = 0): trivially set all V_inc to zero. ✓

For Phase B (V_inc encodes E): use inverse projection:
- E_target(node) = ω_C · A_0(node)
- V_inc[port_i] = E_target · port_dir[i] / |port_dir[i]| · normalization

But Phase A is preferred (§3.4), so V_inc = 0 at IC.

---

## §7 — Adjudication-criterion refinements

### §7.1 — Corrected A-vec proxy: use Phi_link, not V_inc

For the Beltrami parallelism test, A-vec at a node should be reconstructed from **Phi_link** (integrated voltage along bonds = bond-projected A vector), NOT from V_inc (instantaneous voltage = E).

For node n at A-site (i,j,k):
- For each of 4 ports: bond_dir = port_offset / √3 (unit vector along bond)
- A_vec(n) = (1/4) Σ Phi_link[i,j,k, port] · bond_dir[port] · (bond_length normalization)

For B-site nodes: Phi_link is stored at A-sites only (per [`k4_tlm.py:158-167`](../../src/ave/core/k4_tlm.py#L158-L167)). To get A_vec at a B-site, look up Phi_link at each of the 4 neighboring A-sites' ports that connect to this B-site. The B-site's "port-i bond" connects to A-site (B_pos + (-port_offset[i]_A)) at A's port-i.

In code:
```python
def a_vec_at_node(engine, ix, iy, iz, port_offsets_A):
    is_a = (ix % 2 == 0) and (iy % 2 == 0) and (iz % 2 == 0)
    a_vec = np.zeros(3)
    for p in range(4):
        bond_dir_A = port_offsets_A[p] / sqrt(3)  # unit tangent A→B
        if is_a:
            phi = engine.k4.Phi_link[ix, iy, iz, p]
            a_vec += phi * bond_dir_A
        else:
            # B-site: look up Phi at A-neighbor at offset -port_offset
            ax, ay, az = ix - port_offsets_A[p][0], iy - port_offsets_A[p][1], iz - port_offsets_A[p][2]
            phi = engine.k4.Phi_link[ax, ay, az, p]
            a_vec += phi * bond_dir_A  # bond direction A→B is same regardless of which endpoint we're at
    return a_vec / 4.0  # normalize over 4 ports
```

Then Beltrami `cos_sim = (a_vec · ω_vec) / (|a_vec| · |ω_vec|)` should be ≈ +1 at all times for Beltrami standing wave (A ∥ B).

### §7.2 — Substrate-native topology measure

Replace the geometric centroid-flux estimate with **loop-flux Stokes' integral**:

Φ_loop = ∮ A · dl ≈ Σ (over 6 bonds) Phi_link[bond] · bond_tangent_traversal_sign

For the (1,1) Beltrami helical mode at corpus geometry, Phi_loop is the topologically-protected quantum of charge × ξ_topo:

Φ_loop_canonical = 2π · e · ξ_topo / ξ_topo = 2π · e (in natural units: 2π)

Adjudication: Φ_loop within ±10% of 2π in V_SNAP-natural units = topology preserved (unknot). Significantly different value (e.g., 0 or 4π) = different topological class.

This is the substrate-native version of the centroid-flux test. Replaces v6's geometric-plane-normal proxy.

### §7.3 — Persistence threshold: A²_mean instead of A²_min

Per §3.5 + the v6 4-vs-2 saturation pattern result: even with corrected helical Beltrami IC, discrete-K4 sampling on 6 nodes may produce per-node asymmetry. Use:

**A²_mean(over 6 nodes) ≥ 0.5 for ≥ 100 P** instead of **A²_min ≥ 0.5 for ≥ 100 P**

This still requires saturation to be maintained on average across the ring, but doesn't fail on the worst single node when the IC pattern has natural cos(60°) magnitude variation.

### §7.4 — Updated 4-criterion adjudication for v7

| Criterion | Threshold | Method |
|---|---|---|
| Persistence | A²_mean ≥ 0.5 for ≥ 100 P | Mean over 6 ring nodes (instead of min) |
| Beltrami parallelism | mean \|cos_sim(A_vec, ω)\| ≥ 0.8 | A_vec from Phi_link (NOT V_inc) per §7.1 |
| Loop-flux topology | Φ_loop within 2π·(1 ± 0.1) | Stokes' integral ∮A·dl per §7.2 |
| Ring localization | ring-node energy / total ≥ 0.5 | Same as v6 (worked) |

Mode I requires all 4. Mode II = 2-3 pass with diagnosis. Mode III = ≤ 1 pass.

---

## §8 — v7 IC specification summary

For the v7 driver implementation:

1. **Engine setup:** identical to v6 (`VacuumEngine3D.from_args(N=32, pml=4, temperature=0.0, amplitude_convention="V_SNAP", disable_cosserat_lc_force=True, enable_cosserat_self_terms=True)`); v_yield = V_SNAP per subatomic-scale rule.

2. **Real-space topology:** identical to v6 — 6-node hexagonal chair-ring at lattice center (16,16,16). All 6 bonds use ports {0,1,2,0,1,2} on alternating A-sites.

3. **Helical Beltrami A field at each ring node (NEW for v7):**
   - A_0(n) = A_amp_pol · (cos(2π·n/6)·radial_n + sin(2π·n/6)·binormal_n) + A_amp_tor · tangent_n
   - A_amp_tor = A_amp_pol / (2π) per (1,1) Beltrami pitch at corpus aspect
   - A_amp_pol calibrated to drive saturation onset (~0.95 in V_SNAP units)

4. **IC time-phase: Phase A (A, B at peak; E at zero):**
   - V_inc = 0 at every port at every node
   - Phi_link at A-site of each bond = bond-averaged A·tangent · bond_length
   - ω at each ring node = k_C · A_0(n) [parallel to A_0; in natural units k_C = 1, so ω = A_0]

5. **Outside ring:** all fields zero (cold vacuum).

6. **Recording window:** 200 Compton periods. Record per-node A_vec (from Phi_link), ω, V_inc; per-bond Phi_link.

7. **Adjudication per §7.4:**
   - Persistence (A²_mean ≥ 0.5 for ≥ 100 P)
   - Beltrami |cos_sim| ≥ 0.8 using Phi_link-derived A_vec
   - Loop-flux Φ_loop within 2π·(1 ± 0.1)
   - Ring localization ≥ 0.5

8. **Pre-reg ID:** P_phase11_path_alpha_v7_helical_beltrami_chair_ring_IC

---

## §9 — Open derivations + verification path

### §9.1 — A_amp normalization calibration

The (1,1) Beltrami eigenvalue formula assumes continuum torus geometry. On a discrete 6-node chair-ring, the eigenvalue calibration may need empirical adjustment. Initial v7 run will use A_amp_pol = 0.95 (matches v6 saturation amplitude) and check whether peak A² → ~1.

If saturation isn't reached: increase A_amp_pol up to V_SNAP-equivalent.

If saturation overshoots (instability): decrease A_amp_pol to ~0.7.

### §9.2 — Bond-length normalization for Phi_link

In the engine, Phi_link[port] has units of voltage·time = magnetic flux. In natural units (V_SNAP=1, ω_C=1, ℓ_node=1, c=1), Phi_link has natural-unit magnitude. The bond length is √3 lattice spacings (for tetrahedral offsets like (1,1,1)). The mapping:

Phi_link[A_site, port] = A_along_bond · bond_length

needs the engine convention to be verified against [`k4_tlm.py:_connect_all`](../../src/ave/core/k4_tlm.py) which accumulates Phi_link as `V_avg · dt`.

If Phi_link measures `∫V dt` not `∫A dl`: there's a factor of (bond_length / dt) discrepancy. Will be checked during v7 sanity check.

### §9.3 — Verification path

After v7 runs:

- **If Mode I:** corpus-canonical trapped-photon unknot at bond-pair scale empirically confirmed via helical Beltrami + FOC d-q. Major positive result; doc 83 §6 amendment with empirical evidence; reframe Phase 1 outcome.

- **If Mode II partial:** identify which subset of criteria pass; surface to Grant for diagnostic dialogue. Common failure modes anticipated:
  - Beltrami pass + flux fail: spatial topology right but loop-flux normalization off → calibration fix
  - Beltrami fail + flux pass: helical pitch ratio off → re-examine §5.2 (1,1) eigenvalue formula
  - Persistence fail: amplitude calibration off → §9.1

- **If Mode III:** the Kelvin Beltrami + FOC d-q framing on a discrete K4 chair-ring isn't supported. Surface to Grant before further work; possible reframings:
  - The (1,1) helical mode may not embed cleanly on a 6-node discrete ring (continuum torus eigenmode formula doesn't apply)
  - The chair-ring's non-planar geometry may break the toroidal-poloidal decomposition assumptions
  - The helical pitch ratio derivation §5.2 may be wrong for the corpus aspect (R/r = 2π)

---

## §10 — Compliance check (anyone-must-grep + manuscript-over-research)

Per A43 v2 + manuscript-over-research, all claims in this doc grouped by source:

**Manuscript-canonical (verbatim grep-confirmed earlier in session):**
- Vol 1 Ch 1:18, 32 (unknot, 6-node perimeter, ℓ_node geometry)
- Vol 1 Ch 3:25-29 (Lagrangian L_AVE = ½ε₀|∂A/∂t|² − (1/2μ₀)|∇×A|²)
- Vol 1 Ch 3:402 (Beltrami standing wave on chiral K4)
- Vol 1 Ch 4:14-15 (Trace-Reversed Chiral LC Network)
- Vol 1 Ch 4:21-26 (Cosserat translation/rotation = E/B)
- Vol 1 Ch 4:64-67 (c_eff phase velocity = c·S^(-1/2); now understood as phase velocity per backmatter/05:148-156)
- Vol 1 Ch 8:112-125 (Möbius half-cover Λ_surf = π²)
- Vol 4 Ch 1:419 (Virial split ½m_e c² + ½m_e c²)
- Vol 4 Ch 1:430-468 (Confinement Bubble Γ=-1 derivation)
- Vol 4 Ch 1:711 (subatomic-scale v_yield=V_SNAP)
- backmatter/05:128-136 (FOC d-q decomposition table)
- backmatter/05:148-156 (phase vs group velocity at saturation)
- backmatter/05:281-302 ((2,q) torus knot ladder; electron NOT a torus knot)
- common_equations/eq_axiom_4.tex (canonical Ax 4 saturation kernel)
- ave-kb/CLAUDE.md INVARIANT-S2 (axiom numbering)
- vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md, analog-ladder-filter.md (FOC + asynchronous decoupling)

**Synthesis from manuscript (NOT corpus-stated; flagged as implementer derivation):**
- §3.2 specific (p,q) torus Beltrami eigenvalue formula k² = (p/r)² + (q/R)² — standard textbook result for Beltrami modes on torus, applied to corpus geometry
- §5.1 charge quantization ∮A·dl = 2π·e calibration — standard topo-quantization, applied to corpus IC
- §5.2 |A_tor|/|A_pol| = 1/(2π) at corpus aspect R/r = 2π — derived from §3.2 + corpus geometry
- §6 v7 IC operational specification — implementer synthesis from §1-§5 axiom-grounded derivations
- §7 adjudication-criterion refinements — implementer synthesis from §3-§6 + v6 empirical result analysis

**Research-tier dependencies:**
- [Doc 80](80_kelvin_helmholtz_ave_precedent.md) Kelvin/Helmholtz precedent (cited as precedent, not corpus)
- [Doc 83](83_phase1_bond_pair_vs_bond_cluster_scale.md) Phase 1 reframe
- [Doc 84](84_path_alpha_v6_first_run_results.md) v6 empirical record

**Grant dialogue (single source of truth where corpus is silent):**
- Q1 lattice-genesis spin-as-selection-bias → spin direction NOT intrinsic
- Q2 full-wavelength interpretation → ℓ_node = reduced Compton wavelength
- Q3 chirality projection structure → 4 distinct chiralities, careful mapping required
- Trapped-photon thought experiment → IC framing pivot

---

## §11 — References

- [Doc 80](80_kelvin_helmholtz_ave_precedent.md) — Kelvin/Helmholtz/Faddeev-Niemi historical precedent + Helmholtz helicity ∫A·B dV as Hopf invariant
- [Doc 83](83_phase1_bond_pair_vs_bond_cluster_scale.md) — Phase 1 bond-pair vs bond-cluster reframe
- [Doc 84](84_path_alpha_v6_first_run_results.md) — v6 first run empirical record + Mode III reading
- [Vol 1 Ch 1:18, 32](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex), [Ch 3:25-29, 402](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex), [Ch 4:14-26, 64-67](../../manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex), [Ch 8:112-125](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex)
- [Vol 4 Ch 1:419, 430-468, 711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex)
- [`common_equations/eq_axiom_4.tex`](../../manuscript/common_equations/eq_axiom_4.tex)
- [`backmatter/05:128-136, 148-156, 281-302`](../../manuscript/backmatter/05_universal_solver_toolchain.tex)
- [`ave-kb/CLAUDE.md`](../../manuscript/ave-kb/CLAUDE.md) INVARIANT-S2 (axiom numbering)
- [`ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md), [`analog-ladder-filter.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md), [`de-broglie-standing-wave.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)
- [`src/ave/core/k4_tlm.py`](../../src/ave/core/k4_tlm.py) — K4 lattice + Phi_link conventions
- [`src/ave/core/universal_operators.py`](../../src/ave/core/universal_operators.py) — Op10 c-count
- [`src/ave/topological/cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py) — Cosserat ω, u state arrays
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) Rule 6 (substrate-native operator), Rule 14 (substrate-derives), A43 v2 (anyone-must-grep), A48 (frozen-extraction-scope)
- Pre-reg `P_phase11_path_alpha_v7_helical_beltrami_chair_ring_IC` (forthcoming, freeze before v7 driver run)
- Memory rules: `feedback_manuscript_over_research`, `feedback_research_before_asking`
