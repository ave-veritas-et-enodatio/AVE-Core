[↑ Vol 9: The Vacuum Datasheet](./index.md)

# Vol 9 — The Vacuum Datasheet — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol9/index.md bootstrap directive -->

> **Canonicality.** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires. Entries below are scoped to Vol 9; cross-cutting tripwires with Vol-9-specific manifestations are noted but not duplicated.

> **Vol 9 is a synthesis volume.** Every load-bearing claim in Vol 9 is cited back to a canonical derivation in Vol 1–6. This register is therefore intentionally **thin**: it carries (a) Vol-9-scoped tripwires and reading hazards specific to the datasheet format, and (b) classification anchors for the small number of Vol-9-originated synthesis claims (datasheet-format consolidation tables, cross-chapter integration notes, falsification roll-up tables in Ch 15). Per `consistency-vs-emergence` v1.3 Step 8: any Vol-9-originated content is **Class B (axiom-manifestation consolidation)** or **Class C (consistency / synthesis)** by default. A Vol-9 entry MUST NOT promote a canonical-source claim above its canonical-ceiling classification.

---

## Vol 9 reading hazards

- **Datasheet-format precision.** A datasheet's spec-table entries are precision-spec representations of canonical-source content. Where a canonical leaf reports a confidence/solidity band (e.g., 0.55 PARTIAL band for `clm-009nkt`), the Vol 9 spec table MUST carry the same band — do not promote to TYPICAL/MIN/MAX precision without the corresponding canonical-source closure. The cross-cutting `verify-before-cite` v1.4 discipline applies to every numerical entry.
- **Class promotion-past-canonical-ceiling.** Per `consistency-vs-emergence` v1.3, Vol 9 synthesis content MUST NOT promote a canonical-source Class B claim into Class 2 or a Class C claim into Class E without explicit substrate-physics-primitive identification. The Vol-9 synthesis act (consolidating canonical content into datasheet format) is itself Class B / Class C by construction — it does not add substrate-physics primitives.
- **Engineered-vs-natural framing.** The substrate is natural (the universe's vacuum). Engineering observes / characterizes / measures; AVE derives. Any Vol-9 language that implies the substrate is "engineered," "designed," or "constructed" is a framing error and must be revised. The natural-substrate + engineering-empirical-characterization + AVE-substrate-physics-derivation triad is the Vol 9 framing invariant.
- **EE-as-substrate-native primary.** Per `ave-ee-first-mapping` v1.0 (canonical leaf `common/translation-tables/translation-circuit.md` §2, `clm-eemap1`), EE vocabulary is substrate-native at minimal-DOF. Vol 9 datasheet vocabulary is EE-primary throughout; other classical frameworks (atomic / chemistry / statistical mechanics / fluid / GR / QFT) layer DOFs on top of the EE base and are invoked only where they capture content the EE projection does not (geometric, topological, axiom-selection content; see Vol 9 Ch 13).

---

## Open Vol 9 register

No Vol-9-originated `clm-` entries have yet been authored. The register opens with PR-B (Ch 2 + Ch 4) and is extended as subsequent PRs land. Each entry, when authored, will follow the canonical claim-quality entry shape (see `../vol4/claim-quality.md` for the canonical pattern) with explicit Class B / Class C classification per `consistency-vs-emergence` v1.3 Step 8.

---

## Engine-acceptance suite — derivation-support (`sup-`) register

The `sup-` nodes below materialize the green L0–L2 + Op/scale-invariance tier
acceptance tests as derivation-support edges into the claim-DAG (the MAP-TO-SPINE
ritual step). Each is hosted in the suite leaf
[`ch17-engine-requirements/engine-acceptance-suite.md`](ch17-engine-requirements/engine-acceptance-suite.md);
its `supports:` fan-out lives in that leaf's frontmatter. Per INVARIANT-S9 a sim is a
`sup-`, never an `exp-`; per INVARIANT-S10 the local rigor `quality` and every on-point
fraction are authored `*pending*` (graph-wiring, not scoring) and never drag a
beneficiary to pending.

---

## Support: T0.1 energy conservation / unitary scatter (L0-medium)
<!-- id: sup-uiny42 -->

Simulation support (INVARIANT-S9/S10): the T0.1 acceptance test
(`src/tests/engine_acceptance/test_l0_medium.py:30`) confirms the bare srs-TLM
medium conserves energy — the Op5 degree-3 shunt scatter is provably unitary
(SᵀSᵀ=I, |eig(S)|=1 to < 1e-12) and the dynamical total H stays flat to integrator
floor (drift < 1e-10 over ≥ 2000 steps). It lifts the DERIVATION branch of the
lossless-medium claim by re-asserting on the srs grid the unitarity that
`clm-hd9bee` ("K4-TLM Diamond Lattice — Unitarity to Machine Epsilon") establishes
on the K4 grid. Free-standing (no own dependencies). Local rigor `quality` and the
on-point fraction to the beneficiary are both `*pending*` (wiring, not scoring).
Figure: `research/figures/engine_acceptance/T0.1_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-hd9bee (f=*pending*) — K4-TLM lattice unitarity to machine epsilon

---

## Support: A1b Axiom-1 chirality expressed losslessly (L0-axioms)
<!-- id: sup-zf5d1t -->

Simulation support (INVARIANT-S9/S10): the A1b acceptance test
(`src/tests/engine_acceptance/test_l0_axioms.py:216`) confirms the chiral srs lattice
rotates the photon's polarization plane (optical activity) LOSSLESSLY — rotation-ON
energy drift < 1e-8 for both enantiomorphs, dθ/step == the geometric writhe to < 1e-6,
and L/R rotate oppositely. It feeds the DERIVATION branch of the chirality definition
`def-7c3f9e` ("chirality") by exercising the dynamical, lossless expression of the
handedness the term names (post the copy-first view-aliasing fix). Free-standing. Local
rigor `quality` and the on-point fraction are both `*pending*`. Figure:
`research/figures/engine_acceptance/A1b_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - def-7c3f9e (f=*pending*) — chirality (lossless dynamical expression)

---

## Support: A2 Axiom-2 TKI dimensional identity + defect-hosting (L0-axioms)
<!-- id: sup-u7r3vu -->

Simulation support (INVARIANT-S9/S10): the A2 acceptance test
(`src/tests/engine_acceptance/test_l0_axioms.py:331`) confirms the L0 form of the
Topo-Kinematic Identity — the dimensional identity [Q]≡[L] via ξ_topo=e/ℓ_node and the
VCA bridge round-trip (all to < 1e-12), plus the medium HOSTS a defect (girth-10 closed
circuits with nonzero net helicity). It lifts the DERIVATION branch of `clm-dfaiwj`
("Topo-Kinematic Isomorphism [Q]≡[L]") at the L0 dimensional + hosting form (the charge
INTEGER itself is L4, explicitly out of scope). Free-standing. Local rigor `quality`
and the on-point fraction are both `*pending*`. Figure:
`research/figures/engine_acceptance/A2_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-dfaiwj (f=*pending*) — Topo-Kinematic Isomorphism [Q]≡[L] (L0 dimensional form)

---

## Support: A3b Axiom-3 minimum-reflection matched region (L0-axioms)
<!-- id: sup-l2ah0k -->

Simulation support (INVARIANT-S9/S10): the A3b acceptance test
(`src/tests/engine_acceptance/test_l0_axioms.py:443`) confirms the |Γ|²-minimization
prong of Axiom-3 — a MATCHED (SYM) region drives reflection to the floor (analytic
|Γ_SYM| < 1e-9, dynamical R_SYM < 1e-2) while a MISMATCHED (ASYM, ε-only) step reflects
(contrast ≥ 5×). It lifts the DERIVATION branch of `clm-8nkvwy` ("Symmetric vs
Asymmetric Saturation") at its L0 boundary-reflection form (the precursor of the Op14
SYM-vs-ASYM split). Free-standing. Local rigor `quality` and the on-point fraction are
both `*pending*`. Figure: `research/figures/engine_acceptance/A3b_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-8nkvwy (f=*pending*) — Symmetric vs Asymmetric Saturation (matched→Γ→0 prong)

---

## Support: A4 Axiom-4 saturation kernel constitutive gate (L0-axioms)
<!-- id: sup-2qja9z -->

Simulation support (INVARIANT-S9/S10): the A4 acceptance test
(`src/tests/engine_acceptance/test_l0_axioms.py:555`) verifies the saturation kernel
S(A)=√(1−(A/A_yield)²) directly as an L0 constitutive gate — the quarter-arc identity,
the EM projection (ε_eff=ε₀S, μ_eff=μ₀S, c_EM=c₀/S, Z_EM=Z₀ under SYM), and the
canonical longitudinal c_eff²=c₀²/S (⇒ C_eff/C₀=1/S) all to < 1e-12, with the cold limit
S(0)=1 and the stiffening wall as A→A_yield. It lifts the DERIVATION branch of both
`clm-gz7ryg` ("A-034 Single-Kernel Unification") and `clm-8nkvwy` (the kernel that drives
the SYM/ASYM split). Surfaces the pre-existing S**0.25-vs-S**0.5 exponent flag without
resolving it (flag-don't-fix). Free-standing. Local rigor `quality` and both on-point
fractions are `*pending*`. Figure: `research/figures/engine_acceptance/A4_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-gz7ryg (f=*pending*) — A-034 single saturation kernel at all scales
  - clm-8nkvwy (f=*pending*) — Symmetric vs Asymmetric Saturation (kernel form)

---

## Support: T1.1 photon propagates losslessly (L1-photon, FLAGSHIP)
<!-- id: sup-su0h1a -->

Simulation support (INVARIANT-S9/S10): the T1.1 acceptance test
(`src/tests/engine_acceptance/test_l1_photon.py:29`) confirms a transverse photon
PROPAGATES losslessly on the srs grid — a localized one-way packet conserves energy
(drift < 1e-8), never back-scatters (zero centroid reversals), translates at the lattice
wave speed c_net = c_link/√3 (within 5%) on a clean constant-speed diagonal (R² > 0.99).
It lifts the DERIVATION branch of `clm-3npynp` ("Photon Identification — the T₂-Only
Cosserat Microrotation") and `clm-djpx2v` ("Photon Propagation Baseline"). Free-standing.
Local rigor `quality` and both on-point fractions are `*pending*`. Figure:
`research/figures/engine_acceptance/T1.1_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-3npynp (f=*pending*) — Photon Identification (T₂-only Cosserat microrotation)
  - clm-djpx2v (f=*pending*) — Photon Propagation Baseline

---

## Support: T1.2 dispersionless band ω=ck (L1-photon)
<!-- id: sup-iryl5d -->

Simulation support (INVARIANT-S9/S10): the T1.2 acceptance test
(`src/tests/engine_acceptance/test_l1_photon.py:167`) confirms linear dispersion ω=c·k
across the usable band — c(k) spread < 0.05 for m=1..4 — read off the dynamically-evolved
field, with the zone-edge departure characterised not failed. It lifts the DERIVATION
branch of `clm-djpx2v` ("Photon Propagation Baseline") on the dispersion prong.
Free-standing. Local rigor `quality` and the on-point fraction are `*pending*`. Figure:
`research/figures/engine_acceptance/T1.2_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-djpx2v (f=*pending*) — Photon Propagation Baseline (dispersion prong)

---

## Support: T1.3 transversality — 2 polarizations, no leak (L1-photon)
<!-- id: sup-xn9y6c -->

Simulation support (INVARIANT-S9/S10): the T1.3 acceptance test
(`src/tests/engine_acceptance/test_l1_photon.py:233`) confirms exactly 2 transverse
polarizations that do not mix in the free photon — cross-pol leak < 1e-10 and energy
conserved over the window. It lifts the DERIVATION branch of `clm-3npynp` ("Photon
Identification — T₂-Only Cosserat Microrotation") and `clm-j550uh` ("K4 4-Port Irrep
Decomposition — A₁⊕T₂ under T_d", the 2-transverse-DOF group-theory seat). Free-standing.
Local rigor `quality` and both on-point fractions are `*pending*`. Figure:
`research/figures/engine_acceptance/T1.3_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-3npynp (f=*pending*) — Photon Identification (T₂ transversality)
  - clm-j550uh (f=*pending*) — K4 4-Port Irrep Decomposition A₁⊕T₂

---

## Support: T1.4 causality / front-speed (L1-photon)
<!-- id: sup-xey8a8 -->

Simulation support (INVARIANT-S9/S10): the T1.4 acceptance test
(`src/tests/engine_acceptance/test_l1_photon.py:307`) confirms the information front
rides at the lattice signal speed — a sharp on/off seed's leading edge advances at most
one bond per step (no superluminal lattice signal), with PR #275's K4-TLM info-front=c₀
result referenced as the cross-engine causality corroboration (not transferred). It lifts
the DERIVATION branch of `clm-yr6tu4` ("Cubic-Symmetry Suppression of Lorentz-Violating
Signatures — Emergent Lorentz Invariance from K4") on the causal-front prong.
Free-standing. Local rigor `quality` and the on-point fraction are `*pending*`. Figure:
`research/figures/engine_acceptance/T1.4_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-yr6tu4 (f=*pending*) — Emergent Lorentz invariance (causal front-speed prong)

---

## Support: T1.5 chiral optical activity is lossless (L1-photon)
<!-- id: sup-w6tjvs -->

Simulation support (INVARIANT-S9/S10): the T1.5 acceptance test
(`src/tests/engine_acceptance/test_l1_photon.py:393`) confirms the chiral srs grid
rotates polarization (optical activity) losslessly — rotation-ON drift < 1e-8, |dθ/step|
> 1e-3, dθ/step == writhe to < 1e-6 (Rule-12 substitution: this slot replaced the prior
~O(1)-drift FINDING after the copy-first view-aliasing fix). It feeds the DERIVATION
branch of the chirality definition `def-7c3f9e` and the optical-activity definition
`def-0pt1ac` (the gyrotropic SO(2) polarization-plane rotation). Free-standing. Local
rigor `quality` and both on-point fractions are `*pending*`. Figure:
`research/figures/engine_acceptance/T1.5_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - def-7c3f9e (f=*pending*) — chirality (lossless optical-activity expression)
  - def-0pt1ac (f=*pending*) — optical-activity (gyrotropic polarization-plane rotation)

---

## Support: T1.6 transverse-SHEAR mode (L1-multiwave)
<!-- id: sup-oicgzy -->

Simulation support (INVARIANT-S9/S10): the T1.6 acceptance test
(`src/tests/engine_acceptance/test_l1_multiwave.py:127`) confirms the transverse-shear
mode the srs medium carries propagates losslessly (drift < 1e-8), with linear dispersion
(c(k) spread < 0.05) and a well-defined speed on the known srs projection — and REPORTS
the constitutive gap (at S=1 c_shear=c₀·S^(1/4) collapses onto c_EM; the distinguishing
G_shear modulation is a saturated-medium extension). The consistency content lifts the
DERIVATION branch of `clm-crbl60` ("Vacuum Bulk Mass Density and Shear Modulus", the
transverse-mechanical mode family) and `clm-8nkvwy` (the saturation kernel governing the
mode speeds). Carries the module ⚑FLAG (brief √S vs corpus S^(1/4), surfaced not
reconciled). Free-standing. Local rigor `quality` and both on-point fractions are
`*pending*`. Figure: `research/figures/engine_acceptance/T1.6_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-crbl60 (f=*pending*) — Vacuum bulk mass density + shear modulus (transverse-mode family)
  - clm-8nkvwy (f=*pending*) — Symmetric vs Asymmetric Saturation (mode-speed kernel)

---

## Support: T2.1 refractive index c_EM=c₀/S (L2-em-media)
<!-- id: sup-1sq5c1 -->

Simulation support (INVARIANT-S9/S10): the T2.1 acceptance test
(`src/tests/engine_acceptance/test_l2_em_in_media.py:57`) confirms a region at
operating-point A₀ (SYM) has the canonical EM varactor relations c_EM=c₀/S, n_EM=S,
Z_EM=Z₀ to < 1e-9, with the time-domain in-region phase velocity matching 1/S within 8%
(surfacing the honest sign FINDING: the EM packet ADVANCES, the matter clock retards). It
lifts the DERIVATION branch of `clm-8nkvwy` ("Symmetric vs Asymmetric Saturation") on the
SYM operating-point varactor prong. Free-standing. Local rigor `quality` and the on-point
fraction are `*pending*`. Figure: `research/figures/engine_acceptance/T2.1_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-8nkvwy (f=*pending*) — Symmetric vs Asymmetric Saturation (SYM varactor c_EM=c₀/S)

---

## Support: T2.2 achromatic lensing (L2-em-media, HEADLINE)
<!-- id: sup-lorxuk -->

Simulation support (INVARIANT-S9/S10): the T2.2 acceptance test
(`src/tests/engine_acceptance/test_l2_em_in_media.py:174`) confirms a SYM gradient bends
/ retards a wave FREQUENCY-INDEPENDENTLY with Z matched (group-delay spread < 1e-3 across
the band, |Γ| < 1e-6), matching the path-integral prediction — the AVE-distinct
achromatic gravitational-lensing mechanism. The deflection MAGNITUDE is form-derived but
rides the input A₀(x) profile, so the chord-vs-echo of the magnitude is left OPEN (not
headlined). It lifts the DERIVATION branch of `clm-k9up5c` ("Achromatic Impedance Lens
(Protocol 9) — Γ=0 Across All Angles") and `clm-07kd5v` ("Gravitational Wave Propagation
— Invariant Impedance"). Free-standing. Local rigor `quality` and both on-point fractions
are `*pending*`. Figure: `research/figures/engine_acceptance/T2.2_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-k9up5c (f=*pending*) — Achromatic Impedance Lens (Γ=0 across angles)
  - clm-07kd5v (f=*pending*) — Gravitational wave propagation — invariant impedance

---

## Support: T2.3 asymmetric mirror Γ≠0 (L2-em-media)
<!-- id: sup-874l1g -->

Simulation support (INVARIANT-S9/S10): the T2.3 acceptance test
(`src/tests/engine_acceptance/test_l2_em_in_media.py:278`) confirms a static-E-only
(asymmetric) bias loads ε only → Z=Z₀/√S ≠ Z₀ → the boundary reflects (|Γ| > 0.10 at
A₀=0.9, the time-domain reflected fraction within 2× of analytic R and ≥ 5× the SYM
control) — the Op14 Meissner-asymmetric vacuum-impedance mirror, rendered as a BOUNDARY Γ
(CP10). It lifts the DERIVATION branch of `clm-8nkvwy` ("Symmetric vs Asymmetric
Saturation", the ASYM half) and `clm-5s5b0d` ("Vacuum Impedance Mirror Γ(V)").
Free-standing. Local rigor `quality` and both on-point fractions are `*pending*`. Figure:
`research/figures/engine_acceptance/T2.3_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-8nkvwy (f=*pending*) — Symmetric vs Asymmetric Saturation (ASYM E-only half)
  - clm-5s5b0d (f=*pending*) — Vacuum Impedance Mirror Γ(V)

---

## Support: T2.4 α-invariance under SYM (L2-em-media)
<!-- id: sup-ftxwil -->

Simulation support (INVARIANT-S9/S10): the T2.4 acceptance test
(`src/tests/engine_acceptance/test_l2_em_in_media.py:383`) confirms α is invariant under
SYM scaling because the product ε_eff·c_EM = (ε₀S)(c₀/S) = ε₀c₀ cancels the S — α(A₀)/α₀
== 1 to < 1e-12 across the sweep when c_EM is used, with the c_shear substitution as a
NEGATIVE CONTROL that deviates (1/S^{3/2}) so the test discriminates the right speed. It
lifts the DERIVATION branch of `clm-3zz0f6` ("α Invariance Under Symmetric Gravity") and
`clm-8nkvwy` (the SYM kernel). This is the gold-standard inline-cited test (clm-3zz0f6).
Free-standing. Local rigor `quality` and both on-point fractions are `*pending*`. Figure:
`research/figures/engine_acceptance/T2.4_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-3zz0f6 (f=*pending*) — α Invariance Under Symmetric Gravity
  - clm-8nkvwy (f=*pending*) — Symmetric vs Asymmetric Saturation (SYM α-cancellation)

---

## Support: Op-primitive + scale-invariance tier (`test_operators.py`)
<!-- id: sup-evhfcd -->

Simulation support (INVARIANT-S9/S10): the Op-tier acceptance gates
(`src/tests/engine_acceptance/test_operators.py`) wire the existing Op-primitive (Z, S,
Γ, U, M) and scale-invariance assertions into the acceptance framework and ADD the
scale-invariance instance test (`test_scaleinv_same_op_electron_and_blackhole:218`): the
IDENTICAL Op Python callable runs at the electron operating point AND the black-hole
operating point (30+ OOM apart), returning the same functional form — Op2 S=√(1−r²),
Op22 M=1/S² (A43 v11 canonical, NOT doc-81's 1/(1−S)), Op3 Γ, and the mass-INDEPENDENT
regime-boundary eigenvalue ω_R·M=18/49 at both electron-mass and BH-mass inputs. It lifts
the DERIVATION branch of `clm-sysqaf` ("Universal Operator Catalog (Op1–Op22)") and
`clm-m7qd0w` ("Regime-Boundary Eigenvalue Method", the cross-domain operator-reuse claim).
CODATA-anchored sub-targets are consistency-class, not headlined emergence. Free-standing.
Local rigor `quality` and both on-point fractions are `*pending*`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-sysqaf (f=*pending*) — Universal Operator Catalog (Op1–Op22)
  - clm-m7qd0w (f=*pending*) — Regime-Boundary Eigenvalue Method (cross-domain reuse)

---
