# Half-Cover Derivation Audit — Is n̂ ≡ −n̂ AVE-native or SM/QED in disguise?

**Date:** 2026-04-22
**Scope:** Determine whether Ch 8's antipodal identification on the
Clifford torus (n̂ ≡ −n̂, giving R·r = 1/4 and Λ_surf = π²) can be
derived from AVE axioms + K4 structure + classical topology, or
whether it requires an additional postulate equivalent to SU(2)
spinor algebra.

**Prompted by:** Grant's 2026-04-22 challenge: "Is option 2 [RP²
projection] just SM and QED in disguise?"

**Supersedes:** `29_ch8_audit.md` §F5's overturn of Ch 8 half-cover
from "imported" to "K4-derived." This audit shows the overturn
was too fast.

---

## §1 The question and why it matters

Ch 8's α⁻¹ = 137 derivation depends on three hard algebraic
constraints:
- d = 1 (Nyquist, Axiom 1) — derivable
- R − r = 1/2 (self-avoidance, Axiom 2 saturation at crossings) — derivable
- R·r = 1/4 (**Clifford half-cover**, from spin-½) — **under audit here**

Ch 8 says: "the spin-1/2 structure forces a half-cover of this
surface" — only half of T² corresponds to physically distinct
observables. This gives:

```
Full Clifford torus (no half-cover):   R·r = 1/2  →  R/r = 2.0
Half Clifford torus (spin-½):          R·r = 1/4  →  R/r = φ² = 2.618
```

**Golden Torus requires the half-cover.** Without it, AVE's electron
geometry collapses to R/r = 2.0 (classical), and Ch 8's α⁻¹ = 4π³ +
π² + π = 137 doesn't hold.

If half-cover is K4-native, Ch 8's derivation is AVE-axiomatic.
If it's an additional postulate equivalent to SU(2) spinor algebra,
AVE's electron derivation requires SM/QED-equivalent content at
exactly the step that produces the α⁻¹ = 137 signature.

**The audit matters because it determines whether AVE's claim of
"zero-parameter derivation" survives at the tightest scrutiny.**

---

## §2 Mapping to the four AVE axioms

The four axioms (Ch 1):
- **Axiom 1** — LC network substrate on K4 diamond, ℓ_node = ℏ/(m_e c)
- **Axiom 2** — Topo-kinematic isomorphism, [Q] ≡ [L], ξ_topo = e/ℓ_node
- **Axiom 3** — Effective Action principle, Maxwell-form Lagrangian
- **Axiom 4** — Non-linear dielectric saturation, C_eff = C_0/√(1−(Δφ/α)²)

**What can be derived from these four plus K4 classical topology:**
- ω_C = c/ℓ_node (Axiom 1)
- Three-regime saturation (Axioms 4)
- Extended-unknot Finkelstein-Misner kink with 4π temporal double-cover
  (K4 + classical topology, Vol 2 App B spin-half-paradox)
- Gyroscopic-spinor isomorphism (10⁻⁸ numerical verification)
- Self-avoidance at (2,3) crossings (Axiom 2 saturation at crossing loci)
- Nyquist cutoff d ≥ 1 (Axiom 1 resolution)
- Transverse-only photon mode (Cosserat continuum mechanics)

**What requires additional postulates beyond these:**
- Ch 8's antipodal identification of n̂ on the Clifford torus
- The specific rule "half of T² is physically inaccessible"

The four axioms constrain the K4 lattice dynamics and the saturation
behavior. They do NOT automatically produce the statement "the
orientation field on the Clifford torus has antipodal equivalence"
— that's a claim about the *target manifold structure* of the
orientation field, not about the lattice or the action.

---

## §3 Candidate 1 — K4 lattice Z₂ symmetry (REJECTED)

### §3.1 Hypothesis

Does the K4 diamond lattice's own geometry include a Z₂ symmetry
that identifies ω(r) with −ω(r) as the same physical state (either
at each node or between A/B sublattice pairs)?

### §3.2 Findings

**K4 point-group analysis** (research/L3_electron_soliton/22_step1_k4_rotation_action.md):

K4's proper-rotation symmetry is the tetrahedral group T = A₄ (order
12). This group:
- Preserves A/B sublattice structure under pure rotations
- Contains NO inversion and NO reflections — **the diamond is strictly chiral**
- Does NOT swap A ↔ B sublattices

Doc 22_ §5 explicitly states: "To get an A↔B SWAP (needed for the
bipartite-spinor argument), we need to include reflections (full
T_d = S₄) or some other physical mechanism."

Full T_d is a crystallographic point group that AVE's K4 lattice
does NOT have (it's chiral by construction). So the lattice provides
no inversion to generate antipodal n̂.

### §3.3 Numerical check

Direct computation: `R(ω)·ẑ` for `ω = [0.1, 0.2, 0.3]` gives
`[0.195, −0.098, 0.931]`. For `−ω`: `[−0.195, 0.098, 0.931]`. **Not
equal; not antipodes either.** There is no code path or axiom that
makes the K4 field treat ±ω as equivalent.

The K4 scattering matrix `S = (1/2)𝟙 − I` at each node acts on
voltage magnitudes and has no ω-sign dependence. The Cosserat energy
functional uses |ω|², |∇ω|² (even functions of ω), so it's
ω-sign-invariant — but |ω|² = |−ω|² doesn't mean ω and −ω are
IDENTIFIED as the same state; it means the energy is degenerate
across the pair.

### §3.4 Verdict

**Candidate 1 REJECTED.** The K4 lattice provides no intrinsic Z₂
antipodal symmetry for the orientation field. Energy degeneracy
under ω → −ω is not the same as physical identification.

---

## §4 Candidate 2 — Finkelstein-Misner kink on (2,3) extended defect (PRODUCES 4π, NOT ANTIPODAL)

### §4.1 Hypothesis

The Finkelstein-Misner kink derivation of spin-½ for extended
1D defects (`spin-half-paradox.md`) is K4-classical topology. Does
the kink mechanism IMPLY antipodal identification of n̂ on the
Clifford torus, or does it only produce 4π double-cover at the
kink-topology level?

### §4.2 What the KB entry actually derives

From `manuscript/ave-kb/vol2/appendices/app-b-paradoxes/spin-half-paradox.md`
line 8, verbatim:

> "An extended knotted line defect embedded in an SO(3) manifold
> exhibits SU(2) spinor behaviour through the generation of a
> Finkelstein-Misner Kink (also known as the Dirac Belt Trick). The
> continuous geometric extension of the topological loop provides a
> **double-cover over the SO(3) background**, reproducing Spin-1/2
> quantum statistics without violating macroscopic solid-state
> geometry."

**Precise output:** 4π double-cover of the KINK TOPOLOGY over the
SO(3) background. Not n̂ ≡ −n̂ on the Clifford torus.

### §4.3 What the gyroscopic-spinor isomorphism demonstrates

From `spin-gyroscopic-isomorphism.md`:

> "Classical ODE: dL/dt = γ L × B
> Quantum ODE: i d|ψ⟩/dt = −½ γ σ·B |ψ⟩
> Maximum deviation: ~10⁻⁸"

The isomorphism shows **the classical gyroscope ODE is algebraically
identical to Pauli spinor evolution** under identical forcing. Both
have 4π periodicity.

**What this verifies:** 4π temporal double-cover as a classical
consequence.

**What this does NOT verify:** n̂ ≡ −n̂ on the orientation manifold.
The isomorphism is a statement about ODE evolution, not about target-
space identification.

### §4.4 What doc 23_ derives vs assumes

From `23_step2_spin_half_from_k4.md` lines 142-147:

> "K4-native (derivable from Axioms + K4 + classical topology):
> 1. The unknot as smallest stable extended defect
> 2. **The 4π double-cover via Finkelstein-Misner kink on extended defects**
> 3. Gyroscopic precession dynamics
> 4. The mathematical equivalence to SU(2) spinor evolution
> 5. The 4π factor in R_TIR = Z_0/(4π)"

**NOT listed as K4-native:** antipodal identification of n̂ on the
orientation manifold. The doc derives 4π double-cover at the kink
level and the algebraic equivalence with SU(2), but does not
separately derive that the orientation field satisfies n̂ ≡ −n̂.

### §4.5 The conflation trap in doc 01_ (identity adjudication)

`01_identity_adjudication.md` §4 (Candidate C3 section) claims:

> "Ch 8's π² factor from 'spin-1/2 half-cover of the Clifford torus'
> is now structural, not assumed: SU(2) IS the double cover of SO(3),
> so the half-cover prefactor Λ_surf = π² falls out of the SU(2) →
> SO(3) 2-to-1 map."

**This conflates two distinct statements:**

(a) SU(2) → SO(3) is a 2-to-1 map — standard Lie-group topological
    fact. *True.*

(b) The orientation field n̂(r) on the spatial Clifford torus T²
    satisfies n̂ ≡ −n̂ — **a separate geometric claim**. The Lie-group
    2-to-1 map does NOT automatically imply spatial-field
    antipodality.

Doc 01_ treats (b) as following from (a) without explicit derivation.
That step is an implicit QM assumption — in quantum mechanics, rays
in Hilbert space are identified (|ψ⟩ ≡ e^{iθ}|ψ⟩, including −|ψ⟩).
This is a QM POSTULATE applied to the orientation field, not an
emergent property of K4 + classical topology.

### §4.6 Verdict

**Candidate 2: Finkelstein-Misner derives 4π double-cover at the
kink level. It does NOT automatically derive antipodal identification
of the orientation field.** The step from 4π to n̂ ≡ −n̂ is an
SU(2)-quantum-postulate application, not a classical-topology
consequence.

---

## §5 Candidate 3 — Transverse Cosserat polarization (NOT DOCUMENTED)

### §5.1 Hypothesis

If the free photon (transverse Cosserat shear wave) has unoriented
polarization in AVE's framework, and if the electron is a confined
version of this mode, then n̂ ≡ −n̂ could follow from polarization
structure.

### §5.2 Findings

Vol 3 Ch 2 line 139, verbatim:

> "A photon is a purely transverse Cosserat shear wave; it carries
> no rest mass and has no longitudinal (scalar) component."

Vol 4 Ch 1 lines 491-495, verbatim:

> "When massless Bosons (photons) propagate, they act as linear
> transverse shear waves. Because they do not possess a static
> inductive core, they do not geometrically saturate the dielectric
> lattice (Δφ ≪ α). The local metric impedance remains perfectly
> matched at Z₀ ≈ 376.7 Ω."

**The corpus does not discuss photon polarization as oriented or
unoriented.** It identifies the photon as transverse and notes it's
mechanically blind to the bulk, but the polarization-structure
question doesn't appear.

One forward-looking reference (Vol 4 Ch 13 line 166):

> "Radiation pattern polarization (circular polarization content vs.
> knot handedness)"

— marked as **future** work, not currently elaborated.

### §5.3 Classical EM baseline

In standard electromagnetism, a transverse wave has a DEFINITE
polarization direction at any instant. ±E differ by π phase and are
NOT the same state. The AVE corpus provides no mechanism that would
reverse this — no time-averaging argument, no quadrupolar coupling,
no symmetric-tensor structure.

### §5.4 Bound-state concern

Even if the free photon had unoriented polarization, standing-wave
confinement (the electron's TIR boundary) creates NODES that
localize direction. The corpus doesn't discuss whether unoriented
polarization survives confinement.

### §5.5 Verdict

**Candidate 3: not supported by the corpus.** Unoriented photon
polarization is not documented as an AVE-native property, and no
mechanism for it to carry over to confined bound states is
discussed.

---

## §6 Where the SU(2) spinor postulate slips in

The Ch 8 half-cover argument, expanded:

1. **"The electron has spin-½"** — derived from Finkelstein-Misner
   (K4-native, CORRECT).
2. **"Spin-½ means 4π double-cover of the temporal phase"** — derived
   from the kink geometry (K4-native, CORRECT).
3. **"4π double-cover of temporal phase implies spatial phase cycle
   is half of the full complex-torus parameterization"** — **THIS
   STEP is where the SU(2) postulate enters**. This invokes that the
   *physical state space* of a spin-½ system is the projective
   Hilbert space (rays, not vectors); two spinors differing by an
   overall sign represent the same physical state.
4. **"Therefore half of T² is physically inaccessible; Λ_surf = π²"**
   — geometric consequence of step 3 (follows mechanically).

**Step 3 is the SM/QED import.** In quantum mechanics, this is
axiomatic: the physical state space of any spin system is the
projective Hilbert space. Mathematically: Hilbert rays, not
Hilbert vectors.

**In classical Cosserat mechanics, this is not automatic.** A
classical microrotation ω and its negative −ω are, in principle,
different physical states (they generate opposite rotations).

Translating QM's "ψ ≡ −ψ" to classical field theory's "ω ≡ −ω" or
"n̂ ≡ −n̂" requires an additional structural assumption that the
AVE corpus does not derive from the four axioms.

---

## §7 Verdict

### §7.0 STATUS UPDATE (2026-04-22, after 36_ investigation)

**Verdict REVISED.** The original conclusion below (§7.1+) was
reached via over-narrow candidate framing. Path B investigation
(see [`36_pathB_trefoil_z2_investigation.md`](36_pathB_trefoil_z2_investigation.md))
found a fourth candidate this audit missed: **classical SO(3)
observable structure**.

**Corrected verdict:** The half-cover IS AVE-native, via the
automatic action of the SU(2) → SO(3) 2-to-1 cover on the Clifford
torus embedded in S³. This is classical group theory + classical
Cosserat mechanics — not the QM projective-Hilbert postulate. The
mathematical content is identical to SU(2) spinor projection, but
the physical justification in AVE is classical:

1. AVE's Cosserat microrotation is SO(3)-valued (Axiom 1 + classical
   Cosserat).
2. The Rodrigues projection `_project_omega_to_nhat` respects the
   SO(3) quotient automatically (R(ω) = R(ω + 2π·ω̂)).
3. Clifford torus T² ⊂ S³ = SU(2) projects to T²/Z₂ ⊂ SO(3) with
   area halved 2π² → π².
4. The four AVE axioms plus classical group theory produce the
   half-cover; no fifth axiom required.

**Remaining derivation:** Prove the electron's T² is specifically
the canonical Clifford torus (r₁ = r₂ = 1/√2 in S³) via
ropelength-minimality of (p,q) torus-knot embeddings on K4 with
Axiom-4 self-avoidance. This is a classical knot-theory /
topology question — no SM/QED input required. Phase-1 sub-item.

§7.1+ below is retained as the transparent record of the
intermediate reasoning. Read in conjunction with 36_ for the
final state.

### §7.1 Original verdict (SUPERSEDED — retained for reasoning trail)

**The half-cover identification is an additional postulate beyond
AVE's four axioms.** It is not derivable from any of the three
AVE-native candidates:

- K4 lattice Z₂ — doesn't provide antipodal symmetry (K4 is chiral)
- Finkelstein-Misner — produces 4π double-cover of kink, not
  orientation antipodal identification
- Transverse polarization — not documented in the corpus as
  unoriented

**Therefore: Option 2 (implementing RP² projection or Lagrange
antipodal penalty) IS SM/QED in disguise** unless it's preceded by
an AVE-native derivation of the half-cover. Implementing it without
that derivation would smuggle in the SU(2) spinor projective-Hilbert-
space postulate under a different name.

**CORRECTION (per 36_):** The three-candidate framing above missed
that the simulation's Rodrigues projection IS the classical SO(3)
implementation — the half-cover is built in, not missing. Option 2
would be redundant, not an import. See 36_ §7 for the corrected
reading.

Original paths A/B/C preserved below for reasoning-trail
transparency but superseded by 36_'s resolution:

- **Path A:** AVE adopts the half-cover as a **fifth axiom**
  (projective identification of orientation: ω ≡ −ω on the
  orientation manifold). This is an honest framing — AVE's
  zero-parameter status then depends on five postulates, not four.
  The analytical Ch 8 derivation would need to cite this fifth
  axiom explicitly.

- **Path B:** AVE derives the half-cover from something deeper —
  maybe a K4-structure mechanism not yet identified, or an
  emergent property of the (2,3) extended defect's specific
  topology (not the general extended unknot).
  *→ Path B investigation in 36_ closed this: not (2,3)-specific,
  but classical SO(3)-observable structure closes it more generally.*

- **Path C:** AVE drops the half-cover and accepts the classical
  full-Clifford result R/r = 2.0. This would invalidate Ch 8's
  α⁻¹ = 4π³ + π² + π = 137. **Cost:** the clean α⁻¹ closure
  disappears.
  *→ Not needed; Path B resolution avoids this.*

---

## §8 Implications for prior audit and research docs

### §8.1 `29_ch8_audit.md` §F5 needs re-opening

The 2026-04-21 audit revision that overturned F5 from "imported" to
"K4-derived" was premature. The correction should read:

> "**Spin-½ existence** (4π double-cover at the kink level) is
> K4-derivable via extended-unknot Finkelstein-Misner. **Spin-½
> antipodal identification** (n̂ ≡ −n̂ on the Clifford torus) is a
> separate claim not derivable from the Finkelstein-Misner
> mechanism alone. Ch 8 implicitly applies the SU(2) projective-
> Hilbert-space postulate to translate the kink 4π into spatial
> half-cover. This step requires a fifth axiom, further derivation,
> or acceptance that AVE adopts a projective orientation-manifold
> structure."

### §8.2 `01_identity_adjudication.md` §4 C3 claim conflation

Doc 01_'s claim that "the half-cover falls out of the SU(2) → SO(3)
2-to-1 map" conflates group-theoretic 2-to-1 with spatial-field
antipodal identification. The claim should be corrected to:

> "The SU(2) → SO(3) 2-to-1 map is a property of the group
> homomorphism, not automatically of the spatial orientation field.
> Translating 'SU(2) is a double cover' into 'n̂ on T² has antipodal
> identification' requires the projective-Hilbert-space postulate
> from QM (rays, not vectors). This is not derived from AVE axioms."

### §8.3 `34_x4_constrained_s11.md` next-steps reframing

X4 found a stable electron-like bound state at Ch 8 Golden Torus with
23% S11 preference over classical full-Clifford. But the sim cannot
discriminate the two without the half-cover. Under this audit:

- **Option 2 (implement RP² projection)** is now understood as
  "add the SU(2) projective postulate as a numerical constraint."
  If Grant adopts this path, it should be documented as **axiom-
  extension**, not AVE-native discovery.
- **Alternative research path:** investigate whether the specific
  (2,3) extended-defect topology on the K4 lattice produces
  emergent antipodal identification that the general extended-
  unknot Finkelstein-Misner doesn't capture. If so, that would
  save AVE's zero-parameter status without invoking the QM
  postulate.

---

## §9 Open research questions surfaced

1. **Does the (2,3) trefoil's specific topology on K4 produce
   emergent n̂ ≡ −n̂?** The Finkelstein-Misner derivation is for the
   general extended unknot. The electron is specifically a (2,3)
   trefoil — has anyone examined whether the TREFOIL's self-crossing
   structure induces a quotient on the orientation manifold?

2. **Is the "projective orientation manifold" postulate compatible
   with classical Cosserat mechanics?** If we impose ω ≡ −ω as a
   fifth axiom, does it conflict with any other axiom (energy
   positivity, causality, Lagrangian structure)?

3. **What's the physical mechanism that could produce antipodal
   identification?** Candidates to investigate:
   - Z₂ gauge symmetry (impose that all observables are invariant
     under ω → −ω)
   - Dual-sector resolution (some AVE sector with Z₂ structure)
   - Emergent from specific crossing geometry at (2,3) loci

4. **Does the weak preference found in X4 (23% lower S11 at
   Golden Torus vs classical) come from the ansatz bias or from
   S11 structure?** If it's ansatz-bias, then without the half-
   cover AVE cannot discriminate electron from classical at all.
   If it's S11 structure, there's a weak AVE-native discrimination
   that might be sharpenable without the half-cover postulate.

---

## §10 Recommended action

**Do NOT implement Option 2 (RP² projection) as a numerical test
without first resolving the conceptual question.** Running it would
produce the SM/QED-style "discrimination of electron from classical"
but we'd be unable to claim it as an AVE-native derivation.

**Preferred next step:** Research question #1 above — does the
(2,3) trefoil topology specifically produce antipodal identification
that general unknot topology does not? This is a concrete
mathematical question answerable from classical knot theory + K4
structure, not requiring any SM/QED input.

If #1 yields a positive result, Option 2 becomes K4-native (the
antipodal identification is derived from specific trefoil topology,
not imported from SU(2) spinor algebra).

If #1 is negative, AVE must choose between Path A (accept fifth
axiom), Path B (find some other mechanism), or Path C (accept
R/r = 2.0 classical result and retract Ch 8's α⁻¹ = 137 closure).

**This is a program-level decision that belongs with Grant.**

---

## §11 Side observations from KB CLAUDE.md

During this research I encountered `manuscript/ave-kb/CLAUDE.md` with
cross-cutting invariants. Two observations relevant to this audit:

### §11.1 Axiom numbering inconsistency

KB CLAUDE.md claims the four axioms are:
- Axiom 1: ABCD cascade / coupled amplitude
- Axiom 2: Topological phase dislocation
- Axiom 3: Least reflected action
- Axiom 4: SiLU / saturation gate

But `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex`
names them:
- Axiom 1: LC Network substrate (K4 topology)
- Axiom 2: Topo-kinematic isomorphism ([Q] ≡ [L])
- Axiom 3: Effective Action Principle (Maxwell form)
- Axiom 4: Dielectric saturation

**These differ substantively.** The KB's "ABCD cascade / coupled
amplitude" is not how Ch 1 frames Axiom 1. Worth flagging for a
separate audit — not directly relevant to this doc but indicates
cross-volume axiom-labeling drift.

### §11.2 Op10 not in KB's operator list

KB INVARIANT-N3 lists known operators as Op2, Op3, Op4, Op8, Op9,
Op14. **Op10 (Junction Projection Loss) — load-bearing in the L3
electron-soliton work — is not in the KB's canonical list.** This
may indicate Op10 is a research-period addition not yet promoted to
the cross-volume invariant set. Worth flagging separately.

---

## §12 Files

- This doc: `research/L3_electron_soliton/35_halfcover_derivation_audit.md`
- Audit updates required:
  - `29_ch8_audit.md` §F5 overturn revision
  - `01_identity_adjudication.md` §4 C3 claim correction
  - `34_x4_constrained_s11.md` §9.8 next-steps reframing
