# FROZEN PREREG — The SATURATED srs Elastic-Tensor Arc: small-signal C_ij about a DC Q-point, swept across the full operating-point regime, both channel assignments

**Date:** 2026-07-04 · **Lane:** implementer · **Status:** FROZEN — all adjudication bins,
the fallout, and the positive-control target are frozen BEFORE any saturated number is read.
**Branch:** `analysis/saturated-elastic-tensor` (branched off `origin/analysis/matter-stiffening-rho`,
the PR #518 tip — #518 is OPEN/unmerged at branch time; this work STACKS on it).
**Driver (to build):** `src/scripts/vol_1_foundations/saturated_elastic_tensor.py`
**Carrier declaration (D1 policy 3):** the RATIFIED chiral **srs-z3** net (`build_srs_net`,
degree-3, I4₁32, Wyckoff-8a, 8 sublattices/cell). NOT the diamond-z4 instrument.

<!-- SKELETON — sections filled one commit at a time (incremental-write discipline) -->

## SUBSTRATE-FIRST SECTOR HEADER (mandatory, BEFORE any standard-physics word)

- **WHICH SECTOR.** The **translational (Cauchy-grade) sector** of the chiral srs-z3 net,
  the SAME 24×24 Bloch object the cold arc used, but with the RANK-2 bond tensor evaluated at
  **SATURATED** per-channel stiffnesses: `Φ_b(A) = k_a(A_axial)·d̂⊗d̂ + k_s(A_shear)·(I−d̂⊗d̂)`.
  BOTH `k_a` and `k_s` are **translational-u / CAPACITIVE** springs (axial STRETCH vs transverse
  SHEAR of the *same* bond) — NOT the ε-vs-μ photon pair. This is the exact sector ownership the
  #518 result header states verbatim (`matter-stiffening-rho_result.md`: "BOTH k_a and k_s are
  translational-u/**capacitive** springs … NOT the ε-vs-μ photon pair"). The Cosserat couple-stress
  (`G_c, γ`) is STAGE 2 only (orthogonal to the k→0 Cauchy slopes; `axiom4-moduli:24`) and is NOT
  invoked — same scope as the cold arc.

- **MODE.** SMALL-SIGNAL long-wave (Born-Huang acoustic slopes ω(k)→C_ij). The saturated `k(A)`
  are the **differential (small-signal) bond stiffnesses at the DC bias point** — the tangent
  stiffness of the Axiom-4 arc at operating point `A`. The tensor is the small-signal elastic
  response *about* that Q-point (varactor-bias picture, `CLAUDE.md`:75, INVARIANT-S2 "analogous to
  DC bias on a semiconductor varactor").

- **REGIME.** QUASI-STATIC about a DC bias. Op14 saturation is **ON** (this is the whole point —
  the bias sets `S<1`). PHASE-STATE = **saturated, S<1** (the cold arc's PHASE-STATE was S=1,
  saturation OFF — this is the axis that separates this arc from the cold one). Sub-yield (A<1
  strictly on the sweep interior; A→1 is the yield-wall limit, approached but not reached).
  Handedness is saturation-*kernel*-only (`cosserat_field_3d.py:562`); the small-signal elastic
  tensor at a given `(S_axial, S_shear)` is still parity-symmetric BY CONSTRUCTION (both k_a, k_s
  are hand-independent scalars) — both enantiomorphs must give the SAME saturated C_ij. **KEEP-BOTH
  CAVEAT (flagged, tested):** the saturation *kernel* `κ_chiral` biases which handedness saturates
  faster under a *chiral drive*; but at a PRESCRIBED (S_axial, S_shear) operating point the tensor
  is hand-symmetric. This arc prescribes the operating point (does not evolve the chiral kernel),
  so parity-symmetry is the expected control; a nonzero hand-difference = a bug.

- **COORDS (A46).** The saturation arguments `A_axial, A_shear` are **phase-space / reactance
  operating-point amplitudes** on the Ax4 arc (the #518 header states this verbatim: "phase-space/
  reactance operating-point amplitudes … NOT real-space lattice-Cartesian field magnitudes"). The
  ELASTIC READOUT (ω(k) slopes → C_ij → ν, Zener, K/G) is **real-space / spatial-Brillouin** — and
  the ν=2/7 corpus claim is ITSELF a real-space moduli ratio. So: the *operating-point knob* lives
  in phase-space, the *tensor readout* lives in real-space, and each is measured in ITS OWN matching
  coordinate. No φ²/winding comparison is made; no phase-space prediction is checked against a
  real-space measurement. A46-clean on both axes.

- **CONSISTENCY-vs-EMERGENCE class.** ν, Zener, K/G are dimensionless RATIOS from lattice geometry +
  the SATURATED bond ratio ρ_eff = k_a·S_axial/(k_s·S_shear). The verdict path is **CONSISTENCY /
  MANIFESTATION** (does the saturated small-signal tensor reproduce the cold ν(ρ) family under
  ρ→ρ_eff?). α enters ONLY through the √α core operating amplitude (a Class-C α-echo, def-vyvsn1) —
  it is NOT on the ratio verdict path (ρ_eff is a ratio of S-factors; the ratio ν(ρ_eff) is
  α-clean). **EMERGENCE grade is FORBIDDEN** for any VALUE: 2/7, 9.7734, and 0.99479 are ALL
  GR-imported / read-off VISIBLE TARGETS — per the ½/¼ knife (below), NO parameter may be tuned
  toward any of them.

## 0. NORTH STAR — the seam this closes (the #518 §6 scope flag, verbatim)

PR #518 (`matter-stiffening-rho_result.md` §6, "FLAG-DON'T-FIX — the cold-ρ vs saturated-ρ_eff
regime scope") flagged EXACTLY the gap this arc closes, verbatim:

> "The srs-elastic-tensor ρ*=9.77 is a COLD bond ratio; my ρ_eff is a SATURATED effective ratio.
> … driving the saturated ρ_eff to 9.77 is NOT proven to land the same ν=2/7/K=2G elastic tensor
> as setting the cold ρ=9.77. **The saturated C_ij(ρ_eff) would need to be recomputed from the
> saturated bond stiffnesses (a Born-Huang run on the saturated Φ_b)** to claim the matter-Poisson
> operating point is reached. I do NOT claim it."

The two arcs it stacks on:
- **COLD arc (merged):** `srs-elastic-tensor_result.md` — cold Cauchy C_ij is a one-parameter
  family in ρ=k_a/k_s; ν_Hill=2/7 ⟺ K=2G ONLY at ρ*=9.7734 (GR-imported); Zener A=1.229 there;
  K<0 (unstable) for ρ<2; two-hand cross-validation (long-wave + direct eigensolve) agreed to
  C11=0.72786, C44=0.24876 at ρ*. **PHASE-STATE: cold, saturation OFF.**
- **#518 (OPEN):** ρ_eff = ρ_cold·(S_axial/S_shear), ρ_cold=1 (Ax3). Shear-loads STIFFENS (ρ_eff
  rises, crosses 9.77 at A_wall=0.99479, overshoots to 222 at A→1); axial-loads SOFTENS (ρ_eff→0);
  pure-AC radiation gives ρ_eff=ρ_cold. **[DRIVES-STIFF-QUALITATIVE]: direction earned, value
  imported.** It computed the RATIO ρ_eff only — NOT the tensor.

This arc does the untested piece: the **Born-Huang tensor on the saturated Φ_b**, swept across the
full regime, both assignments, with two-hand cross-validation at ≥3 points including the crossing.

## 0.5. FRAMING — resolved by corpus + #518 (no new Grant escalation on the ontology axis)

**Pre-test-physics-check fired.** The load-bearing ontology: *"is this a small-signal elastic
response about a DC Q-point, or something else?"* This is **corpus-settled**, so no new Grant
escalation on this axis:
- The varactor-bias / operating-point framing is canonical: `CLAUDE.md`:75 (INVARIANT-S2)
  "the dynamical state of the LC tank, analogous to DC bias on a semiconductor varactor";
  "Small-signal transverse propagation through a region at operating point A_0 sees modulated
  effective parameters".
- #518 §6 (Grant-fired 2026-07-04) NAMES this exact next test ("a Born-Huang run on the saturated
  Φ_b"). Grant ratified "sweep all regimes" (FLAG-1) and KEEP-BOTH "record and do both" (FLAG-2)
  for this arc.
- The channel-assignment fork (SHEAR-LOADS vs AXIAL-LOADS) is the ONLY fork, and it is handled by
  **KEEP-BOTH** (run both blind, record both as a formal fork axis; the substrate decides) — Grant
  already ratified this disposition for #518 and this arc. No new fork the axioms cannot settle is
  expected; if one arises mid-run, STOP and surface (bin [STUCK-FRAMING → Grant]).

## 0.6. THE LOAD-BEARING PHYSICS — homogeneity of Born-Huang C_ij (the a-priori prediction)

The single fact that drives every bin. The Born-Huang long-wave map `(k_a, k_s) ↦ C_ij` is
**homogeneous of degree 1** in the bond stiffnesses (each C_ij is a sum of terms each linear in one
bond stiffness — see the driver's `acoustic_christoffel`: `Φ_b = k_a·P + k_s·(I−P)` enters
linearly, and the long-wave `Γ = Φ2_aa − Φ1_ao·Φ0_oo⁻¹·Φ1_oa` is degree-1 in the stiffnesses
because the `Φ0_oo⁻¹` degree-(−1) exactly cancels the two degree-1 `Φ1` factors). Consequences,
**pre-registered as the expected outcome**:

1. **Dimensionless RATIOS are homogeneous degree-0** ⟹ ν, Zener A, K/G depend **ONLY** on the
   ratio ρ_eff = k_a·S_axial / (k_s·S_shear) = ρ_cold·(S_axial/S_shear). An overall stiffness
   scale S **drops out of every ratio.** So the saturated ν(ρ_eff) map is the **cold ν(ρ) map with
   ρ→ρ_eff** — bit-for-bit at matched ρ_eff. **⟹ predicts [SAME-TENSOR-POINT].**
2. **Absolute moduli are homogeneous degree-1** ⟹ K, G, C_ij, and the acoustic speeds all scale
   by the overall S factor. Near the yield wall (A→1, S→0) the lattice goes **floppy** (K,G→0 in
   magnitude) even though the ratios freeze — the corpus "topology melts" picture
   (`electron-bh-isomorphism.md:32`, G_shear→0).
3. **sign(K) is scale-invariant for S>0** ⟹ the K<0 instability boundary is set by ρ_eff alone
   (the same ρ_eff=2 crossing as cold), NOT shifted by saturation magnitude. The *magnitude* of K
   is softened by S, the *sign* is not.

**Prereg dimensional/analytic check (ave-prereg Step 3.5).** ρ_eff is dimensionless (ratio of
S-factors ∈ (0,1]). At the #518 shear-loads crossing: S_axial = S(√α) = √(1−α) = 0.992703,
S_shear = S(0.99479) = 0.10194, ρ_eff = 0.992703/0.10194 = 9.737 (the #518 crossing lands ρ_eff
just under the cold ρ*=9.7734 read-off; the exact crossing A_wall is where ρ_eff = 9.7734 which
the driver locates). At the cold control A_wall=0: S_axial=S_shear=1 ⟹ ρ_eff = ρ_cold = 1 ⟹ the
saturated tensor MUST equal the cold tensor at ρ=1 (C11=0.1768, C12=−0.1768, C44=0.1768,
K=−0.0589 unstable, Zener=1.000) — the positive-control identity. **These expected values are
frozen HERE, before the driver runs.**

## SWEEP AXES (frozen)

## POSITIVE CONTROL (frozen target — planted-source gate)

## READOUTS (frozen; reported whatever they say)

## VALIDATE-ON-KNOWN (frozen; HALT if fail)

## FROZEN ADJUDICATION BINS (per-assignment)

## FALLOUT MAP (frozen before any saturated number)

## OUTPUT

## Cross-references (verified at branch HEAD)
