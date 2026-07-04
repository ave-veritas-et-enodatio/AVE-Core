# FROZEN PREREG — Stage 2 of the srs Elastic-Tensor Arc: the chiral micropolar (Cosserat) constitutive tensor + the geometry-fixed piezo-class cross-coupling B

**Date:** 2026-07-04 · **Lane:** implementer (Grant-fired 2026-07-04)
**Branch:** `analysis/srs-chiral-micropolar` (off `origin/main`)
**Status:** FROZEN — the bins, the fallout inheritance, and the two blind readings
below are frozen BEFORE any Stage-2 micropolar number is read.
**Driver (to build):** `src/scripts/vol_1_foundations/srs_chiral_micropolar.py`
**Module (to build):** `src/ave/core/micropolar_bloch.py`
**Parent (Stage 1, PR #506, MERGED):** `research/2026-07-04_srs-elastic-tensor_result.md`
**Carrier declaration (D1 policy 3):** RATIFIED chiral **srs-z3** (`build_srs_net`,
I4₁32, Wyckoff-8a, 8 sublattices, z=3). Diamond-z4 reused ONLY as the achiral
symmetry NULL control (B≡0 must emerge on the centrosymmetric Fd-3m lattice).

---

## SUBSTRATE-FIRST SECTOR HEADER (mandatory, BEFORE any standard-physics word)

- **WHICH SECTOR.** The **full micropolar (Cosserat) sector** of the chiral srs-z3 net:
  per node **6 DOF** = 3 translational `u` + 3 micro-rotational `φ`. 8 Wyckoff-8a
  sublattices/cell → a **48×48 Bloch dynamical matrix D(k)** (Stage 1's 24×24 u-only
  block, PLUS the φ-block, PLUS the u↔φ cross-block). This is the sector Stage 1
  INTEGRATED OUT (Stage 1 §5: "Cosserat couple-stress does NOT enter the k→0 Cauchy
  slopes"). Stage 2 does NOT contradict that — it asks a DIFFERENT question: does the
  CHIRAL u↔φ cross-coupling (the piezo-analog pseudo-tensor B), when the rotational
  sector is integrated back out via a long-wave elimination, BACK-REACT on the
  effective Cauchy ν? A cross-coupling B that is zero at k→0 in the bare tensor can
  still shift ν_eff through the O(k²) elimination (the internal-strain / Kleinman
  mechanism, one grade up).

- **THE BOND MODEL (three blocks per z=3 bond).**
  1. **u↔u (translational):** the Stage-1 Born rank-2 tensor
     `Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂)` — UNCHANGED from Stage 1 (k_a stretch, k_s shear).
  2. **φ↔φ (couple-stress):** a bond-curvature stiffness `γ` penalizing relative
     micro-rotation of bonded nodes: `½·γ·|φ_i − φ_j|²` per bond. `γ` sets the
     couple-stress modulus; `ℓ_c²=γ/G` is the corpus Cosserat coupling length
     (`constants.py:298`, `ℓ_c=√6·ℓ_node`). Enters the bands at finite kℓ, not k→0.
  3. **u↔φ (THE CHIRAL CROSS-COUPLING — the object under test).** Computed BLIND
     TWO WAYS (Grant ruling 2026-07-04, verbatim: "run both blindly, but what do our
     coupled network equations or spice approach say?"), see §0.5.

- **REGIME.** Cold linear (small-signal), sub-yield, saturation OFF. The 4₁-screw
  handedness enters the COLD tensor here ONLY through the bond GEOMETRY (the Wyckoff-8a
  attachment offset / screw pitch), NOT through κ_chiral (which is saturation-only,
  `cosserat_field_3d.py`). So the chiral B pseudo-tensor, if nonzero, is a
  GEOMETRIC-CHIRALITY effect of the non-centrosymmetric I4₁32 point group — exactly
  the "acoustic-activity class, MECHANICAL sibling of the A44 gyrotropic converter"
  the brief names. It MUST flip sign under enantiomorph swap (right↔left); ν_eff MUST
  NOT (ν is a modulus ratio, parity-even). Both are frozen falsifiers (§READOUT d).

- **PHASE-SPACE vs REAL-SPACE (A46).** Real-space / spatial-Brillouin: `ω(k)` acoustic
  slopes + the k→0 elimination → C_ijkl, D_ijkl, B_ijkl → ν_eff. ν_eff is a real-space
  moduli ratio; the ν=2/7 corpus claim is itself a real-space moduli ratio. Coordinates
  match. NOT a phase-space (V_inc,V_ref)/Clifford-torus claim.

- **CONSISTENCY-vs-EMERGENCE class.** CONSISTENCY. ν_eff, Zener, K/G, B/(G·ℓ) are
  dimensionless RATIOS from lattice geometry + bond stiffnesses — NO CODATA, NO α, NO
  Q_TANK on the verdict path (α-CLEAN). **NO tuning of any stiffness toward 2/7** — the
  bins + fallout map are frozen FIRST, the guard. Per the ½/¼-coincidence tell: if the
  reduction to a point REQUIRES reading (b)'s κ_rot at a tuned value that lands on
  target, that value is the K=2G import in a THIRD costume — booked as such, NOT as a
  geometric determination.

---

## 0. North star — what Stage 2 tests that Stage 1 could not

Stage 1 found the Cauchy tensor is a **one-parameter family in ρ=k_a/k_s**; ν=2/7 only
at an externally-supplied ρ*≈9.7734 where **K=2G exactly** (ρ* = K=2G re-imported, the
½-costume). The corpus's OWN hypothesis for WHY K=2G — verified at HEAD 2026-07-04 —
is that the MICROPOLAR ROTATIONAL SECTOR forces it:

- `manuscript/ave-kb/vol2/claim-quality.md:1059` (clm-o3q9ul, DCVE spec, VERIFIED
  verbatim): "Standard Cauchy elasticity (K=(5/3)G)... causes unbounded contraction...
  the engine must instantiate a Chiral LC micropolar continuum with explicit rotational
  kinematics κ_rot·ε_ijk(θ_k−φ_k) to enforce K=2G trace-reversed identity and prevent
  array implosion." **Solidity 0.50, asserted-not-derived; OPEN strengthen-by**
  (`.index/strengthen-by.jsonl:186`, clm-crbl60): "Justify the Cauchy relation
  K_vac=2G_vac for the chiral micropolar lattice."
- `research/2026-06-08_vacuum-as-chiral-piezoelectric.md:83,129-135` (VERIFIED): the
  coupling channel is **antisymmetric stress σ^A → couple-stress → ω**; the two Cosserat
  equations `ρü=∇·σ+f`, `I_ω·φ̈=∇·μ+2σ^A+g` are "coupled through σ^A."
- `research/_archive/L3_electron_soliton/02_lagrangian_derivation.md:252` (VERIFIED):
  after K=2G eliminates K and the isotropic-bending ansatz eliminates β_c,γ'_c, "That
  leaves three independent moduli: G, G_c, γ."

**Stage 2 tests the corpus's own hypothesis, BLIND:** does the geometry-fixed chiral
micropolar coupling REDUCE the Stage-1 ρ-family (possibly to a point), and what ν_eff
results — WITHOUT being asked to find 2/7. If it reduces to a point, report that point's
ν/K/G/Zener flat (whatever they are) and whether K=2G holds there (not sought).

## 0.5. THE TWO BLIND READINGS (Grant ruling (c), 2026-07-04) + the EE-canon diagnostic

The u↔φ cross-coupling is computed BLIND two ways; the fork itself is the discriminator:

- **READING (a) — GEOMETRY-FIXED LEVER-ARM (zero new knobs).** The z=3 bond force acts
  at the strut's attachment point, offset from the node's rotational center by a lever
  arm `b` FIXED BY LATTICE GEOMETRY (the Wyckoff-8a site offset + the 4₁-screw pitch).
  A transverse bond force `f` then makes a torque `τ = b × f` on the node micro-rotation
  automatically. The coupling constant is set by `b` and the SAME (k_a,k_s) as Stage 1 —
  NO new stiffness. In continuum language this is the σ^A-mediated channel
  (`vacuum-as-chiral-piezoelectric.md:129`): forces carrying moment arms about the
  material point. **EE-canon FORM anchor (VERIFIED at HEAD):** def-ch1crc
  (`vocabulary-register.md:700`): the chirality carrier is "an INTER-tank coupling, NOT a
  per-node C-vs-L reactance" — wiring-topology-determined, not a new component. Its
  MAGNITUDE is flagged imposed/STATED-pending (`device-circuit-models.md:163`: "the
  non-reciprocity MAGNITUDE is not yet computed... the cubic-FDTD engine averages
  chirality out"). **This blind run adjudicates whether srs geometry alone supplies that
  value** — the exact frontier that leaf flags.

- **READING (b) — INDEPENDENT κ_rot (swept knob).** An explicit torsional/relative-rotation
  bond spring `½·κ_rot·|φ_i−φ_j−(the rigid-body part)|²` carried ON TOP OF (k_a,k_s),
  a genuinely new third stiffness. Swept across κ_rot ∈ [0, large] like Stage-1's ρ. In
  continuum language this is the μ-mediated (couple-stress modulus) channel. **The
  ½/¼-tell is armed:** if ν_eff reaches 2/7 only at a tuned κ_rot* (as Stage-1's ρ*
  reached it only at K=2G), that κ_rot* is the import in a third costume — booked as
  such (family CONSTRAINED-NOT-PINNED-by-geometry).

- **THE DIAGNOSTIC (Grant pointer 2).** Track WHICH continuum channel carries the
  computed B in each reading: **σ^A-mediated ⟺ geometric (lever-arm) ⟺ reading (a);
  μ-mediated ⟺ independent stiffness ⟺ reading (b).** Report the decomposition; it says
  which physical picture the srs lattice actually implements.

## 0.6. SPICE / coupled-network cross-check (Grant, bounded — drop if it balloons)

Per the SPICE-lane pilot pattern (`research/2026-07-03_spice-lane-feasibility_note.md`:
numpy-native, **ngspice UNINSTALLED — named limitation applies**): a small numpy-MNA
two-tank cell netlist comparison as an INDEPENDENT network-equations read on the same
fork — (a) shared-node / mutual coupling where the coupling coefficient comes from wiring
topology alone, vs (b) an explicit coupling element with a swept value. It cross-checks
that the geometry-fixed vs free-knob distinction reproduces in the circuit picture. If it
balloons past a self-contained cell, DROP it and say so in the result.

---

## FALLOUT INHERITANCE — the Stage-1 fallout map carries over (frozen)

Stage 1's fallout map (F.A code constants, F.B manuscript /7 leaves, F.C the three PPN
couplings, F.D the C11 relabel) carries over UNCHANGED as the inheritance. Stage 2 does
NOT re-enumerate it; it only ADDS the micropolar-specific verdict on top. The
[FAMILY-REDUCED-TO-POINT] and [FAMILY-CONSTRAINED-NOT-PINNED] bins execute as HONEST
status changes on the SAME leaves Stage 1 mapped — surfaced for auditor + Grant, NOT
landed by this implementer lane (flag-don't-fix). The one NEW leaf in scope:

| Leaf | Claim | Stage-2 verdict lands as |
|---|---|---|
| clm-o3q9ul (`vol2/claim-quality.md:1059`) | "micropolar κ_rot·ε_ijk(θ_k−φ_k) enforces K=2G" | the DIRECT object under test. If (a) geometry-fixed reduces the family to K=2G with ZERO knobs → the strengthen-by (clm-crbl60) is CLOSED (geometry DOES force it). If only (b)'s tuned κ_rot* hits it → the claim stays asserted-not-derived; κ_rot is the import in a third costume. |
| clm-crbl60 strengthen-by (`strengthen-by.jsonl:186`) | "Justify K_vac=2G_vac for the chiral micropolar lattice" | CLOSED-affirmative / STAYS-OPEN, per the bin. |
| def-ch1crc magnitude (`vocabulary-register.md`, `device-circuit-models.md:163`) | non-reciprocity/chiral-coupling MAGNITUDE "STATED-pending chiral-crystal engine" | Stage 2's B magnitude is the first geometry-derived number for this slot (or confirms it stays imposed). |

---

## FROZEN ADJUDICATION BINS (frozen before any Stage-2 number)

- **[FAMILY-REDUCED-TO-POINT].** The geometry-fixed chiral coupling (reading a, zero
  knobs) collapses the Stage-1 ρ-family to a distinguished point. → Report that point's
  ν_eff / K / G / Zener FLAT (whatever they are), and whether K=2G holds there (NOT
  sought — reported honestly). If K=2G/ν=2/7 emerges from geometry alone with no tuned
  knob, the clm-crbl60 strengthen-by CLOSES affirmative and the seam gains a crystalline
  micropolar grounding. If the point is elsewhere, report where.

- **[FAMILY-CONSTRAINED-NOT-PINNED].** The coupling constrains ρ (shrinks the family)
  but does not pin it to a point; OR the family is pinned only in reading (b) at a tuned
  κ_rot* (the ½/¼-tell — the import in a third costume). → Report the constrained range,
  ν_eff across it, and (if b) that κ_rot* is externally-supplied not geometry-fixed.

- **[CHIRAL-COUPLING-NEGLIGIBLE].** B is nonzero on srs but its back-reaction leaves
  ν_eff unmoved (the elimination shift is below tolerance). → B exists (the acoustic-
  activity channel is real) but does not ground ν; Stage-1's one-param-family verdict
  stands, ν=2/7 stays GR-imported.

- **[B-VANISHES].** B ≡ 0 on srs (within tolerance) — the piezo channel does not exist
  mechanically on the srs bond model. → Book WHY (which symmetry / which bond-block
  structure kills it). This would be a surprise given I4₁32 non-centrosymmetry; the
  diamond null-control (B≡0 on Fd-3m) is the calibrated contrast that makes this bin
  interpretable.

- **[STUCK-FRAMING → Grant].** A NEW framing fork the axioms + corpus cannot settle.
  STOP and surface (Rule 16). The bond-model fork is already Grant-adjudicated (c).

---

## VALIDATE-ON-KNOWN (frozen, run BEFORE the srs verdict — HALT if fail)

The 6-DOF micropolar pipeline MUST pass these BEFORE any srs Stage-2 number counts:

| # | Known | Target | Tolerance | Rationale |
|---|---|---|---|---|
| M0 | **Stage-1 recovery**: the u↔u block ALONE (κ_rot=0, γ=0, no cross-coupling) must reproduce Stage-1's srs C_ij (the one-param ρ-family) BIT-FOR-BIT | ν(ρ), Zener(ρ), K/G(ρ) = Stage-1 table to <1e-8 | rel-err <1e-6 | the 6-DOF matrix must contain the 3-DOF Stage-1 answer as its u-block limit — the load-bearing regression that says the extension didn't corrupt the parent |
| M1 | **DIAMOND NULL CONTROL (the symmetry control)**: the chiral pseudo-tensor B on the centrosymmetric Fd-3m diamond lattice, BOTH readings | B ≡ 0 (identically, to numerical zero) | \|B\|/(G·ℓ) < 1e-8 | centrosymmetry FORBIDS the piezo-class pseudo-tensor — B MUST vanish on diamond. This is the elegant reuse of the retired instrument as a symmetry null. If B≠0 on diamond → the extraction is broken; HALT. |
| M2 | **Enantiomorph sign flip**: B on srs-right vs srs-left | B(left) = −B(right) (sign-flipped, magnitude preserved) | rel-err <1e-6 | the pseudo-tensor is parity-ODD by construction; a chiral coupling that does NOT flip is a bond-operator bug |
| M3 | **ν_eff parity**: ν_eff(right) vs ν_eff(left) | ν_eff identical (parity-EVEN) | rel-err <1e-6 | ν is a modulus ratio, parity-even; if ν_eff flips with hand → the elimination mixed a parity-odd term into an even observable (bug) |
| M4 | **micropolar consistency (known continuum limit)**: γ→0, κ_rot→0, b→0 recovers pure Cauchy; large γ opens the couple-stress band gap at the expected `ℓ_c²=γ/G` scale | the couple-stress band appears at kℓ_c~1 | qualitative + scale | confirms the φ-sector is wired correctly (the band-gap tell) |

If M0/M1/M2/M3 fail → the extraction is wrong; HALT, report no srs verdict.

---

## THE READOUTS (frozen; reported whatever they say)

**(a) Is B nonzero on srs, and what sets its magnitude?** Report B_ijkl (the chiral
pseudo-tensor block) for BOTH readings. Trace EVERY constant in B to lattice geometry
(strut angles, Wyckoff offset, screw pitch) OR to canon — verify geometry-fixed vs knob.
Report which continuum channel (σ^A vs μ) carries it. Report both bond models (Born +
Keating — robust only if model-independent, Stage-1's standard).

**(b) ν_eff INCLUDING the chiral back-reaction.** Integrate out the rotational sector
via the long-wave elimination (the same Born-Huang machinery, one grade up: the acoustic
3×3 now eliminates BOTH the optic-translation AND the micro-rotation DOF at O(k²)).
Report ν_eff(ρ) with the cross-coupling ON vs OFF — the shift IS the back-reaction.

**(c) Does the coupling constrain ρ (reduce the family)?** Report whether a distinguished
point emerges and WHERE (ν/K/G/Zener there, and whether K=2G holds — WITHOUT being asked
to find 2/7). Both readings, both bond models, both hands.

**(d) Both enantiomorphs.** B(left)=−B(right); ν_eff(left)=ν_eff(right). Frozen falsifier.

## OUTPUT

`src/ave/core/micropolar_bloch.py` (the 6-DOF Bloch + long-wave elimination module).
`src/scripts/vol_1_foundations/srs_chiral_micropolar.py` → `_output/srs_chiral_micropolar.json`
(validate-on-known M0–M4, the B_ijkl tensor both readings + both models + both hands, the
ν_eff(ρ) cross-coupling ON/OFF curves, the diamond null-control, the σ^A-vs-μ channel
diagnostic, the SPICE cross-check if bounded, the bin verdict). Result doc:
`research/2026-07-04_srs-chiral-micropolar_result.md`. Claims-register: status rows ONLY
per the bin (no rewrites; auditor lands). NO self-merge; REVIEW: pending-orchestrator.

---

## Cross-references (verified at HEAD 2026-07-04)

- Parent (Stage 1): `research/2026-07-04_srs-elastic-tensor_result.md` (PR #506)
- Stage-1 driver (extends): `src/scripts/vol_1_foundations/srs_elastic_tensor.py`
- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net` / `build_diamond_net` (null)
- Micropolar-forces-K=2G hypothesis: `manuscript/ave-kb/vol2/claim-quality.md:1059` (clm-o3q9ul)
- OPEN strengthen-by: `manuscript/ave-kb/.index/strengthen-by.jsonl:186` (clm-crbl60)
- σ^A channel decomposition: `research/2026-06-08_vacuum-as-chiral-piezoelectric.md:83,129-135`
- 3-moduli {G,G_c,γ}: `research/_archive/L3_electron_soliton/02_lagrangian_derivation.md:252`
- Cosserat coupling length ℓ_c=√6·ℓ_node: `src/ave/core/constants.py:298`
- def-ch1crc (inter-tank, magnitude-pending): `manuscript/ave-kb/common/vocabulary-register.md:700`; `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:163`
- A44 gyrotropic (EM sibling): `src/ave/core/cross_sector_coupling.py:5-10`; `src/ave/core/crystal_engine.py:30-32`
- SPICE-lane pilot (numpy-MNA, ngspice absent): `research/2026-07-03_spice-lane-feasibility_note.md`
- Grant bond-model + (c) ruling: this session 2026-07-04
