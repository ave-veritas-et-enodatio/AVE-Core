# What the lattice sees and reacts to: substrate-perspective view of the canonical electron

**Date:** 2026-05-01
**Predecessor:** [doc 102 §7 Round 12 closure](102_round_12_unknot_cosserat_working.md)
**Status:** working analysis per Grant directive 2026-04-30 ("what does the lattice see and react")

---

## §1 — Question framing

Round 12 closed with the canonical electron seeded as a Cosserat ω-field on a horn-torus unknot — Layer 1 + Layer 2 in the doc 101 §9 three-layer framing. The seeder works; the topology preserves; the energy budget is consistent.

But that's the IMPLEMENTER'S view of the field. **What does the substrate (the K4 LC lattice + Cosserat sector) actually experience locally** when a canonical electron exists in it? What observables fire? What dynamics get triggered? What does the lattice "see," and what does it "react" with?

This is asking for the operational physics from the substrate's point of view, not from the field-theorist's. Per Rule 14 (substrate-derives-the-answer), walking the substrate is the right approach.

---

## §2 — What each lattice node has (observables, per Ax 1)

Each node in the K4 substrate carries these local degrees of freedom:

### §2.1 — K4 sector (capacitive + inductive states on each bond)

For each of 4 ports (tetrahedral connectivity per Ax 1):
- **V_inc[port]** — incoming voltage on that bond LC's C-state
- **V_ref[port]** — reflected voltage (outgoing) on the bond LC's C-state
- **Φ_link[port]** — integrated flux on the bond LC's L-state (conjugate to V_inc; computed every step at [`k4_tlm.py:384-391`](../../src/ave/core/k4_tlm.py#L384-L391) per A-010 reactance-tracking corollary in COLLABORATION_NOTES)

Bond LC dynamics: C-state (V_inc) and L-state (Φ_link) trade off in time; bond stores reactive energy 1/2 C V² + 1/2 L Φ²/L².

### §2.2 — Cosserat sector (rotational + translational microstructure)

Per the Cosserat continuum model (Vol 1 Ch 5 ish):
- **u** — translation displacement (3-vector per node)
- **ω** — rotation displacement (3-vector per node, SO(3)-valued per A-008)
- **ε** (strain tensor) — symmetric part of ∇u plus cross-coupling with ω
- **κ** (curvature tensor) — ∇ω

ω is the substrate microrotation per node. The SO(3) → SU(2) double-cover at the substrate level gives spin-1/2 character to any spinor observable extracted from ω (per A-008 + spin-gyroscopic-isomorphism.md).

### §2.3 — Op14 saturation observables (Ax 4)

These are derived per-cell quantities from the K4 sector amplitude:
- **A²_local** = (Σ_ports V_inc²) / V_SNAP² — per-cell aggregate saturation level (chi-squared-of-4 across ports per A47 v2)
- **S_local** = √(1 − A²_local) — saturation factor (Born-Infeld kernel n=2)
- **Z_eff** = Z_0 / √S — effective impedance (modulated by saturation)
- **c_eff** = c_0 · √S — effective wave speed (modulated by saturation; per A-010 local-clock-modulation corollary)
- **n_eff** = c_0 / c_eff = 1/√S — effective refractive index (gravitational analog per `eq_gravity_derived.tex`)

### §2.4 — Coupled K4-Cosserat saturation (full Ax 4 mixing)

When both K4 V_inc and Cosserat ω are non-zero, the saturation A² couples both:
- A²_total = A²_V + A²_ω where A²_V = (V_inc² + V_ref²) / V_SNAP² and A²_ω = (κ²/ω_yield²) (rotation-yield)

This is the substrate-level coupling channel (Op14 cross-block) that connects K4 sector dynamics to Cosserat sector dynamics. Per A47 v3 + doc 101 §9 three-layer: K4 hosts Layer 3 phase-space, Cosserat hosts Layers 1+2 real-space + bundle, Op14 couples them.

---

## §3 — What the lattice "sees" with the canonical electron present

The canonical electron is a 0₁ unknot (Layer 1, real-space curve) carrying a Beltrami standing wave with SU(2) bundle structure (Layer 2). At horn-torus geometry per Reading A canonical (R = r = ℓ_node/(2π)).

What the substrate's local observables show, point-by-point:

### §3.1 — At the loop's tube core (ρ_tube ≈ 0)

- **|ω|² is large** — the Beltrami standing wave is concentrated here per the hedgehog envelope
- **A²_ω is high** — close to or above the Op14 saturation threshold (√(2α) ≈ 0.121 per A47 v2)
- **S_local is small** — saturation is engaged
- **Z_eff is high** — local impedance is much larger than vacuum Z_0
- **c_eff is small** — wave propagation is slow here
- **n_eff is large** — local refractive index is high (gravitational analog: this is where the substrate's local clock is slowest)

The tube core is a region of **trapped, saturated, slowed substrate**.

### §3.2 — At the loop's surface (Regime II boundary)

- **A²_local crosses √(2α)** from above to below as you move outward
- **|∇A²|** is large here (sharp gradient from saturated to vacuum)
- **|∇Z_eff|** is correspondingly large — sharp impedance step
- **Local reflection coefficient Γ² is high** per Op3 (Γ ≈ (1/2)·∇ln Z_eff, so |Γ|² ∝ |∇Z_eff|²/Z_eff²)
- **TIR-wall behavior**: incoming waves from outside (low Z) bounce off the inside (high Z) surface; trapped waves bounce off going outward

The loop's surface is a **self-formed Total Internal Reflection (TIR) wall** — the field that's there creates the saturation gradient that creates the wall that traps the field. Self-maintaining circular causation.

### §3.3 — Outside the loop (Regime I, vacuum)

- **|ω|² and |V_inc|²** decay rapidly (hedgehog tail; exponentially-suppressed in saturation regime)
- **A²_local ≈ 0** — vacuum
- **S_local ≈ 1, Z_eff ≈ Z_0, c_eff ≈ c_0** — undisturbed substrate

But not perfectly — there's a long-range effect (1/r² via Op14 coupling per [Vol 3 Ch 3 macroscopic-relativity](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex)):
- **Local clock slowing** persists at long range as O(GM/rc²) — the gravitational analog
- **Refractive-index gradient** — light bends around the saturated region (gravitational lensing analog, weakly)

### §3.4 — In the loop's interior (Regime III plasma, IF deep saturation)

If the loop's interior contains sub-Compton-wavelength field structure (which the unknot at horn torus does — the tube interior IS the loop itself, no separate interior), the field is in **Regime III** — fully saturated, A² approaching 1, Z → ∞, c → 0.

In the unknot's case (horn torus, R_loop = r_tube), there's no "interior" — the loop tube IS the structure. Inside the tube, the field is saturated; outside, it's vacuum. The loop is self-contained.

For OTHER structures (e.g., trefoil torus knot for proton 5₁/5₂), there might be a meaningful interior with separate physics. But for the canonical electron unknot, no interior exists.

---

## §4 — How the lattice "reacts" (dynamics)

The lattice doesn't have a special "electron mode" or "electron equation." It has saturating LC dynamics that the canonical electron CONFIGURES into a topologically stable pattern. The reactions are the substrate's standard dynamics evaluated on that pattern:

### §4.1 — Local scattering (Ax 1 substrate)

At each node, V_inc waves arrive on each port; the scatter S-matrix sends out V_ref on each port. With saturation engaged:
- Z_eff modulates the S-matrix coefficients per port
- Bond LC tanks store reactive energy as Φ_link grows
- Energy is conserved per Ax 3 effective action (no dissipation in the closed-system limit)

Where the field is high (loop core), the scatter is heavily-modulated. Where the field is low (vacuum), scatter is near-trivial.

### §4.2 — Self-maintaining trap

The saturation IS where the field is. The field IS where the saturation traps it. This is not a chicken-and-egg problem; it's a **self-organized fixed point** of the substrate's LC dynamics:

- Imagine you remove the field locally. Saturation drops. Z_eff drops to Z_0. The trap dissolves. The (now-undisturbed) substrate has no localized structure.
- Imagine you have field but no saturation (linear regime). The field disperses; no localization. No electron.
- Both are needed simultaneously: field amplitude high enough to engage saturation, saturation patterned enough to trap field. The unknot topology is the simplest stable solution.

This is **Ax 3 (Effective Action) at the operational level**: the substrate's least-reflected-action principle stabilizes the configuration where field + saturation jointly minimize action. The unknot is the topological ground state of that principle.

### §4.3 — Topological conservation

The unknot's c=0 topology is a TOPOLOGICAL invariant. Continuous deformations of the field cannot change c without crossing a barrier. This means:
- **Charge conservation** (per Ax 2 TKI: [Q] ≡ [L]; the unknot's circumference IS the unit charge)
- **The electron can't decay to vacuum** — it would need to cross a topological barrier
- **Two unknots can annihilate** — they can deform into a pair-of-loops then into one big loop then into two opposite-sign loops then to vacuum (this is pair-creation/annihilation kinematics)

The lattice REACTS to these topological constraints via the substrate's continuity equations + saturation dynamics. No special "topology operator" needed.

### §4.4 — Magnetic moment generation

The unknot has circulating ω-field around the loop. This is a **closed current loop**:
- B-flux threads the loop interior (perpendicular to loop plane)
- External B-field exerts torque on the loop's magnetic moment
- Result: gyroscopic precession (Larmor frequency ω_L = γ B_0)

Per `larmor-derivation.md` + spin-gyroscopic-isomorphism.md: this isn't quantum mechanical magic — it's classical Newton's-laws-of-rotation applied to the loop's angular momentum.

The g-factor = 2 emerges from the SU(2) bundle (Layer 2): the SO(3) ω-field has period 2π, but the spinor observable has period 4π → ratio 2 → g=2.

### §4.5 — Op14 long-range coupling (gravitational analog)

In Regime I outside the loop, the substrate is locally "vacuum" but there's a faint refractive-index gradient persisting at long range (Op14 saturation kernel propagates outward via 1/r² coupling). This gives:
- **Light bending around the electron** (gravitational lensing at electron-scale; tiny but nonzero)
- **Time dilation in the electron's vicinity** (clock at radius r runs slower by O(GM/rc²) — substrate's local clock-rate modulation per A-010)
- **Mutual electron interaction** — two electrons feel each other's refractive-index gradients → effective inverse-square attraction at long range (gravitational mass)

This is the **electron's mass** showing up as a long-range gravitational-coupling consequence of the local saturation kernel. Per Vol 3 Ch 3 macroscopic-relativity: gravity IS this Op14-saturation refractive-index gradient propagated to macroscopic scales.

### §4.6 — K4-Cosserat coupling via Op14 (when both sectors are non-zero)

Per A47 v3 + doc 101 §9 three-layer: the canonical electron has structure in BOTH sectors:
- Cosserat ω: Layer 1 + Layer 2 (real-space unknot + SU(2) bundle)
- K4 V_inc/V_ref: Layer 3 (phase-space (2,3) winding on Clifford torus, hypothetical pending Layer 3 audit)

Op14 couples them: A²_total = A²_V + A²_ω. When both sectors have field, the saturation is TOTAL, and the trap involves BOTH:
- Cosserat ω circulates around the loop in real space
- K4 V_inc/V_ref phasor traces (2,3) winding in phase space
- The two patterns are coupled at the substrate via Op14
- Together, they form the FULL canonical electron — the part the L3 arc has been trying to instantiate end-to-end

CoupledK4Cosserat infrastructure was designed to test this coupling. It hit a 4M× energy runaway per session 2026-04-22; resolving that runaway unlocks the full canonical-electron test.

---

## §5 — Operational summary: substrate's "view" of the canonical electron

The lattice doesn't "see an electron." It sees:

1. **A localized region of high A² saturation** — high local impedance, slow local clock, refractive index >> 1
2. **A self-formed TIR wall at the boundary** — sharp Z_eff gradient confining field
3. **A topologically conserved circulation pattern** — closed loop, c=0, can't decay
4. **A circulating current** — generates B-flux, magnetic moment, g=2 via SU(2) bundle
5. **A long-range refractive-index tail** — gravitational mass, light bending, clock slowing in vicinity
6. **A coupled K4-Cosserat field structure** — Layer 1+2 in Cosserat ω, Layer 3 (hypothetical) in K4 V_inc/V_ref

Macroscopically, these substrate observables COMPOSE into what we measure as:
- charge e (from topology + Ax 2 TKI)
- mass m_e (from circumference + Bounding Limit 1)
- spin 1/2 (from SU(2) bundle + A-008)
- gyromagnetic ratio g=2 (from SU(2)-induced doubling)
- Compton wavelength ℓ_node (= reduced Compton = unknot circumference)
- gravitational coupling (from Op14 long-range saturation tail)

But none of these are "extra" properties added on top of the substrate's local observables. They are EMERGENT readings of the substrate's joint state at the canonical electron configuration.

The lattice reacts to the canonical electron by:
- Maintaining the trap (self-consistent saturation + reflection at the loop wall)
- Generating B-flux via the loop current
- Coupling to other substrate disturbances via Op14 long-range refractive index
- Conserving topology (no crossing-number change without topological barrier)
- Precessing in external B (Newton's rotational laws on the loop's angular momentum)

---

## §6 — Implications for Round 13+

Per §4.6: the FULL canonical electron requires both Cosserat ω AND K4 V_inc/V_ref structure, coupled via Op14. Round 12 only validated Cosserat ω-side (Layer 1+2). Round 13+ candidates from doc 102 §7.4 sharpen under §5's substrate-perspective:

**Round 13 most promising approach: K4 V_inc/V_ref Layer 3 test in the corresponding sector independently.**

The existing `initialize_quadrature_2_3_eigenmode` (per A47 v7 at [`tlm_electron_soliton_eigenmode.py:224`](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L224)) is the K4-side seeder for Layer 3. It seeds (V_inc, V_ref) at 90° quadrature with phase = 2φ + 3ψ — the (2,3) winding pattern.

Layer 3 test: run K4-only with that seeder; verify:
- Pre-registered binary criteria for the (2,3) phase-space winding
- Topological invariant in K4 sector (analogous to Cosserat c=0 criterion, but for V_inc/V_ref winding)
- Energy conservation in K4-only (no Cosserat coupling)

**Round 14+: full coupled CoupledK4Cosserat canonical-electron test.**

Unblock by resolving the 4M× energy runaway. Per A44 + COLLABORATION_NOTES.md A47 v9-RESOLUTION pattern: missing-axiom vs engine-bug diagnostic. The runaway is most likely an engine bug (T_kinetic not saturating per A44 fix); audit + fix as Round 14 entry.

**§5's substrate-perspective view also clarifies the FFT extraction question** (doc 100 §22.6 ⏸):

The substrate sees the canonical electron via local observables (A², S, Z_eff, ω, V_inc, Φ_link). FFT of any of these along the loop axis would surface:
- |ω|² FFT: peaked at the Beltrami fundamental k ≈ 1/R_loop
- V_inc FFT: peaked at k_phase corresponding to the (2,3) winding (Layer 3)
- These are the layer-1 and layer-3 spectral signatures respectively

FFT extraction infrastructure is straightforward (numpy.fft on the omega array) — the question is what to extract from. Per §5: extract from BOTH ω-field AND V_inc/V_ref jointly to test the coupling (Op14 cross-block).

---

## §7 — Closure

§5 articulates the substrate's operational view of the canonical electron — what local observables fire, what thresholds trigger reactions, how the reactions combine to maintain the topologically stable trap. This is the plumber-physics view: not "the electron is X" but "when the substrate's local observables enter THIS configuration, the substrate exhibits the properties we macroscopically call 'electron'."

The view explains:
- **Why the unknot is stable** (self-maintaining trap)
- **Where charge comes from** (topology + Ax 2 TKI)
- **Where mass comes from** (circumference + Bounding Limit 1)
- **Where spin-1/2 comes from** (SU(2) bundle + A-008)
- **Where g=2 comes from** (SO(3)/SU(2) doubling)
- **Where gravitational coupling comes from** (Op14 long-range saturation tail)

It also clarifies what the L3 arc has been struggling with:
- The K4-only TLM tests (Round 6) tested Layer 3 in K4 V_inc/V_ref — correct sector for that layer, but limited to ℓ_node-resolved scale
- The Cosserat-only tests (Round 12) tested Layer 1+2 in Cosserat ω — correct sectors, lattice-resolved
- Neither tested the COUPLING via Op14 — that's where the canonical electron's full identity lives
- CoupledK4Cosserat (session 2026-04-22) tried the full coupling but hit 4M× runaway — engineering blocker

The §5 substrate-perspective view doesn't solve the engineering blocker, but it CLARIFIES what the engine needs to deliver: stable saturation-coupled K4 + Cosserat dynamics with both sectors carrying their canonical-electron structure simultaneously.

— Doc 103 closure of substrate-perspective walk per Grant 2026-04-30 ("what does the lattice see and react"). Operational physics view of the canonical electron from the lattice's frame; clarifies Round 13+ direction.
