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
the constitutive gap (at S=1 the transverse-shear mode collapses onto c_EM; the
distinguishing G_shear modulation is a saturated-medium extension). The consistency
content lifts the DERIVATION branch of `clm-crbl60` ("Vacuum Bulk Mass Density and Shear
Modulus") **scoped to the bulk-density / transverse-MODE aspect ONLY** (the mode is present
and propagates losslessly) and `clm-8nkvwy` (the saturation kernel governing the mode
speeds). **SHEAR-MODULUS half gap-reported, NOT credited (2026-06-17 per verify `w0855uvzt`):**
the G_shear constitutive channel is ABSENT at S=1 (no separate shear-modulus DOF in the
engine) — by this leaf's own absence-rule (an absent aspect gets no `sup-` credit, as
applied to T1.7/T1.8), the shear-modulus half of `clm-crbl60` is NOT strengthened by this
test; only the bulk-density/transverse-mode half is. Carries the module ⚑FLAG (the brief
√S vs corpus (1−A²)^(1/4) surface form — RESOLVED 2026-06-17 as the same curve, see the
plan §FLAGS c_shear discharge). Free-standing. Local rigor `quality` and both on-point
fractions are `*pending*`. Figure: `research/figures/engine_acceptance/T1.6_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-crbl60 (f=*pending*) — Vacuum bulk mass density (transverse-MODE aspect ONLY; shear-modulus half gap-reported, NOT credited — G_shear constitutive absent at S=1)
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
`clm-m7qd0w` ("Universal Solver Toolchain — Operator Reuse, Not Per-Domain Derivation",
its canonical title; the cross-domain operator-reuse claim).
CODATA-anchored sub-targets are consistency-class, not headlined emergence. Free-standing.
Local rigor `quality` and both on-point fractions are `*pending*`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-sysqaf (f=*pending*) — Universal Operator Catalog (Op1–Op22)
  - clm-m7qd0w (f=*pending*) — Universal Solver Toolchain — Operator Reuse, Not Per-Domain Derivation (cross-domain reuse)

---

## Support: T3.3 Γ=−1 wall on the posited mass-cage (L3-existence)
<!-- id: sup-1ecv2m -->

Simulation support (INVARIANT-S9/S10): the T3.3 acceptance test
(`src/tests/engine_acceptance/test_l3_mass_cage.py:526`) confirms that a posited saturated
A1-scalar cage exhibits the Γ=−1 reflective wall the corpus says is the electron's confining
TIR boundary — Γ_bulk crosses the canonical OP2 engaged-gate −0.25 by A=0.95 (Γ_min(0.95)=
−0.283, Γ_min(0.99)=−0.454), descends monotonically toward −1, →0 in vacuum (S→1), with the
literal −1 UNREACHABLE (S_min-clipped floor, by design). Read via the **α-FREE** impedance
route `crystal_engine.gamma_bulk()` (Z_eff=√S→0 ⇒ Γ→−1), NOT `gamma_em_sq` (the 1−α bake,
`cvr_model.py:364`). CONSISTENCY / FORM-chord: it POSITS the cage (does NOT show self-
formation, the gated rung-2). It lifts the DERIVATION branch of `clm-kezk9z` (the Γ=−1
confinement wall + Z₀ from the discrete LC ladder) and `clm-uatcql` (the electron's Γ=−1 TIR-
cavity 4-property identification). Free-standing. Local rigor `quality` and both on-point
fractions are `*pending*`. Figure: `research/figures/engine_acceptance/T3.3_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-kezk9z (f=*pending*) — Z₀ from discrete LC ladder + the Γ=−1 confinement wall
  - clm-uatcql (f=*pending*) — Electron canonical identification (Γ=−1 TIR cavity property)

---

## Support: T3.4a mass=cutoff gapped bound mode (L3-existence)
<!-- id: sup-xgx063 -->

Simulation support (INVARIANT-S9/S10): the T3.4a acceptance test
(`src/tests/engine_acceptance/test_l3_mass_cage.py:645`) confirms a DISCRETE gapped breathing
eigenmode ω_cutoff≈2.87 (natural units; ipk=15, peak/mean≈456, 23 zero-crossings) EXISTS on
the posited cage — the mass=ground-state-cutoff-energy of the bound resonator is the FORM (a
chord). m_e the VALUE is NEVER read off the cage (definitional, `constants.py:129` "Input 1";
`electron-identification.md:50` "CALIBRATION ANCHOR, not derivation"). FORM-chord / VALUE-
definitional. Integrator-time note (Rule 10): the mode rings only under a radial-SHELL
breathing kick, not a monopole/DC kick (the latter is the bin-1 1/n_steps relaxation
artifact). It lifts the DERIVATION branch of `clm-ka5zdx` (the mass-closure theorem
mc²=E_reactive, the saturation-locked standing-wave LC tank) and `clm-unk0bd` (the electron
$0_1$ unknot body-loop hosting that standing wave). Free-standing. Local rigor `quality` and
both on-point fractions are `*pending*`. Figure:
`research/figures/engine_acceptance/T3.4_mass_cutoff_eigenmode_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-ka5zdx (f=*pending*) — Mass-Closure Theorem mc²=E_reactive (saturation-locked standing wave)
  - clm-unk0bd (f=*pending*) — Electron body topology ($0_1$ unknot + (2,3) phase-space winding)

---

## Support: T3.4b cold/α-FREE Q — ECHO corroboration (L3-existence)
<!-- id: sup-wuy333 -->

Simulation support (INVARIANT-S9/S10): the T3.4b acceptance test
(`src/tests/engine_acceptance/test_l3_mass_cage.py:645`) measures Q from the eigenmode's cold
ring-down with the α-bake REMOVED (two guards: no Q_TANK = `cvr_model.py:72`, no M.ELECTRON,
no `gamma_em_sq`). The RESULT is **Q_ringdown≈30.8 (Q_linewidth≈3.8), NOT 137**. Because α was
never baked, the α-free cold cage does NOT reproduce 137 ⇒ the corpus Q=1/α (`cvr_model.py:72`)
is an **instance-baked ECHO**, not a cage-emergent chord — a clean chord-vs-echo NEGATIVE.
**This support records that empirical result as CORROBORATION of the already-canonical value-
scoped-echo framing of `clm-rtdmsn`** ([`theorem-3-1-q-factor.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):19,
the "echo at the value level" verdict; :21 the instrument-echo-trap, which says re-measuring Q
from cold dynamics with the bake removed is the only way the chord could be earned — and it
was not). The support is wired to clm-rtdmsn because the empirical evidence is on-point for
that claim's VALUE-scope; it does **NOT** strengthen any "Q=137 is forced/derived" reading
(there is none — clm-rtdmsn already states Q=1/α "predicts no independent value"). The local
rigor `quality` and the on-point fraction are `*pending*`; per INVARIANT-S10 a pending support
contributes nothing to the beneficiary's local_quality and never drags it to pending, so this
corroboration changes no solidity. consistency-vs-emergence: the cold-Q value is a measured-
DERIVATION-branch corroboration of a VALUE-echo classification, NOT an emergence result.
Figure: `research/figures/engine_acceptance/T3.4_cold_Q_ringdown_linewidth_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-rtdmsn (f=*pending*) — Electron Q-factor α⁻¹=Q_tank (value-scoped ECHO; cold-Q corroborates Q=1/α is calibration, NOT cage-emergent)

---

## Support: T3.4c zero-drive persistence (L3-existence)
<!-- id: sup-x7h9yh -->

Simulation support (INVARIANT-S9/S10): the T3.4c acceptance test
(`src/tests/engine_acceptance/test_l3_mass_cage.py:645`) evolves the bare posited cage with NO
drive for t≫τ_relax; the bound-mode amplitude on the PML-excluded interior holds steady
(late/mid≈1.31, late_min≈0.34·amp0) — a non-radiating standing mode. FORM-chord: it shows
PERSISTENCE of the saturation-locked standing structure (ave-conserved-vs-pumped: a conserved
standing invariant measured zero-drive, not pumped). It is NOT the topological-winding
protection (that is the winding sector, bucket B, NOT cage-testable on the A1 scalar cage). It
lifts the DERIVATION branch of `clm-ka5zdx` (mc²=E_reactive of a stable saturation-locked
standing wave) and `clm-uatcql` (the electron bound-resonator identification, whose stability/
non-decay property is the persistence). Free-standing. Local rigor `quality` and both on-point
fractions are `*pending*`. Figure: `research/figures/engine_acceptance/T3.4_persistence_trace_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-ka5zdx (f=*pending*) — Mass-Closure Theorem mc²=E_reactive (stability of the standing wave)
  - clm-uatcql (f=*pending*) — Electron canonical identification (stability/non-decay property)

---

## Support: T3.1 longitudinal-bulk mode is real (L3-existence precursor)
<!-- id: sup-3kq9w7 -->

Simulation support (INVARIANT-S9/S10): the T3.1 acceptance test
(`src/tests/engine_acceptance/test_l3_mass_cage.py:214`) confirms that a propagating
longitudinal-BULK (A1 dilatation) compression mode IS REAL on the extended medium — the
Heaviside-Gibbs-EXCISED scalar grade (def-9a4f07) that textbook EM / QED gauge-DELETES
(Gupta-Bleuler leaves exactly 2 transverse on-shell DOF), and AVE keeps as a physical
acoustic branch. Measured (not asserted) on the PML-excluded interior: the launched
compression PROPAGATES (one-way pulse-peak speed > 0.3·c₀), has a RISING acoustic dispersion
ω(k) (dω/dk > 0), and runs at the K=2G dilatation speed `c_bulk = √(2G/ρ) = √2·c₀`
(|c_bulk/c₀ − √2| < 1e-9) — a SECOND, faster channel distinct from the c₀ transverse photon.
This FLIPS the T1.7 ⊘ absence-finding (the srs vector-TLM carried 2 transverse DOF only; the
canonical Master-Equation scalar engine now carries the longitudinal grade). CHORD —
AVE-distinct EXISTENCE (the QED-counterfactual), NOT a forced-number chord: the DOF is
added-by-design (the corpus says it is physical, def-9a4f07), but propagation/dispersion/speed
are READ off the integrator. It lifts the DERIVATION branch of `clm-crbl60` (vacuum bulk mass
density + shear modulus): the mode propagates at exactly the `c_bulk = √(K/ρ) = √(2G/ρ)` speed
that claim's `K_vac = 2G_vac` Cauchy relation + `G_vac = ρ_bulk·c₀²` construction predict, so
the `√2·c₀` measurement is the empirical (α-FREE) confirmation of that bulk-modulus → bulk-speed
cross-check. Free-standing. Local rigor `quality` and the on-point fraction are `*pending*`.
Figure: `research/figures/engine_acceptance/T3.1_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-crbl60 (f=*pending*) — Vacuum bulk mass density + shear modulus (K=2G; c_bulk=√(2G/ρ)=√2·c₀ confirmed)

---

## Support: T3.2 c_eff(V) stiffening → ∞ at yield (L3-existence precursor)
<!-- id: sup-mz4t0p -->

Simulation support (INVARIANT-S9/S10): the T3.2 acceptance test
(`src/tests/engine_acceptance/test_l3_mass_cage.py:388`) confirms that the longitudinal-bulk
effective speed STIFFENS, `c_eff(V) = c₀·S^(−1/2) → ∞` as A → A_yield (S → 0), driven by the
canonical Axiom-4 kernel `S(A) = √(1−A²)` read DIRECTLY from the engine's authoritative
`c_eff_squared` (`master_equation_fdtd.py:148-151`, the #278-corrected ½-power form). Measured
across the sweep A ∈ {0…0.99}: cold limit c_eff/c₀(0)=1 (<1e-12), monotone-rising, matches
`(1−A²)^(−1/4)` to <1e-9 (an S^0.25 read would FAIL bin 3, catching the refractive_index
exponent-defect), and diverges past the I→II and II→III regime edges toward the wall. This is
the CAGE PRECURSOR (CP8 generative-precursor): the bond stiffens C_eff=C₀/S→∞ at yield, and the
T3.3 Γ=−1 wall is the END of this stiffening. consistency-vs-emergence: Axiom-4 MANIFESTATION /
consistency — NOT a chord (no forced dimensionless number falls out; the stiffening is the
axiom's constitutive law expressed in the longitudinal sector). It lifts the DERIVATION branch
of `clm-gz7ryg` (the single Axiom-4 kernel S(A)=√(1−A²) governing every topological-reorganization
event at every scale): T3.2 confirms the SAME dimensionless kernel manifesting in the
longitudinal-bulk sector. Free-standing. Local rigor `quality` and the on-point fraction are
`*pending*`. Figure: `research/figures/engine_acceptance/T3.2_debug.png`.

> **Leaf references:** [engine-acceptance-suite](./ch17-engine-requirements/engine-acceptance-suite.md).

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-gz7ryg (f=*pending*) — A-034 single Axiom-4 kernel S(A)=√(1−A²) (manifested in the longitudinal sector)

---
