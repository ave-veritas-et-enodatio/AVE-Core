# FROZEN PREREG — The SATURATED srs Elastic-Tensor Arc: small-signal C_ij about a DC Q-point, swept across the full operating-point regime, both channel assignments

**Date:** 2026-07-04 · **Lane:** implementer · **Status:** FROZEN — all adjudication bins,
the fallout, and the positive-control target are frozen BEFORE any saturated number is read.
**Branch:** `analysis/saturated-elastic-tensor` (branched off `origin/main`; PR #518
`analysis/matter-stiffening-rho` MERGED to main 2026-07-04, merge commit 6d2ecdf4 — the
matter-stiffening ρ_eff result and driver are now MERGED CANON, cited as such below).
**Driver (to build):** `src/scripts/vol_1_foundations/saturated_elastic_tensor.py`
**Carrier declaration (D1 policy 3):** the RATIFIED chiral **srs-z3** net (`build_srs_net`,
degree-3, I4₁32, Wyckoff-8a, 8 sublattices/cell). NOT the diamond-z4 instrument.

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

**AXIS 1 — operating point A_wall** (the swept-channel amplitude), the canon ladder + visible
targets + a dense log-approach to the yield wall:

| A_wall | provenance / role |
|---|---|
| **0** | COLD CONTROL — MUST reproduce the merged cold family exactly (positive-control gate) |
| √α ≈ 0.085425 | def-vyvsn1 A1-core amplitude (α-echo, Class-C) |
| 0.5 | table rung |
| 0.9 | table rung |
| 1−α ≈ 0.992703 | canon-forced near-yield amplitude (a VISIBLE canon point; NOT tuned to) |
| **0.99479** | the #518 shear-loads ρ_eff=9.77 crossing — **READ-OFF ONLY, a VISIBLE TARGET** |
| 0.999 | near-yield rung |
| 0.99999 | deep near-yield (the #518 ρ_eff=222 overshoot point) |
| dense log-approach A_wall → 1 (e.g. 1−10^{−k}, k=1..8) | the floppy-limit / yield-wall approach |

**AXIS 2 — channel assignment** (KEEP-BOTH; run BOTH blind, per #518's exact loading definitions,
`matter_stiffening_rho.py`):
- **SHEAR-LOADS** (Grant-lean, def-vyvsn1-consistent): axial fixed sub-saturated at √α
  (S_axial = √(1−α) = 0.992703), shear swept to A_wall (S_shear = S(A_wall)). ρ_eff = S_axial/S_shear
  RISES → stiffening branch.
- **AXIAL-LOADS** (mirror control): shear fixed sub-saturated at √α, axial swept to A_wall.
  ρ_eff = S_axial/S_shear FALLS → softening branch.

**AXIS 3 — direction/branch coverage** (Grant's standing regime challenge; do NOT sample a lucky
direction): the FULL cubic direction set the cold arc used — [100],[010],[001],[110],[101],[011],
[111],[210],[120],[312] — over-determined least-squares C_ij + per-direction acoustic-slope table
at [100]/[110]/[111]. Both enantiomorphs at every operating point (parity control).

## POSITIVE CONTROL (frozen target — the planted-source gate; MANDATORY BEFORE any saturated number)

At **A_wall = 0** BOTH assignments give S_axial = S_shear = 1 ⟹ ρ_eff = ρ_cold = 1 ⟹ the saturated
tensor MUST be **bit-identical** to the merged cold tensor. The frozen target values (read from the
merged cold arc, `srs-elastic-tensor_result.md` + regenerated cold driver output THIS session):

| Quantity | Cold target (A_wall=0) | tolerance |
|---|---|---|
| C11 at ρ=1 | +0.17678 | rel < 1e-6 |
| C12 at ρ=1 | −0.17678 | rel < 1e-6 |
| C44 at ρ=1 | +0.17678 | rel < 1e-6 |
| K at ρ=1 | −0.05893 (NEGATIVE, unstable) | rel < 1e-6 |
| Zener A at ρ=1 | 1.00000 | abs < 1e-5 |
| K=0 stability floor | ρ_eff = 2.0000 | abs < 1e-4 |
| ν_Hill = 2/7 point | ρ_eff = 9.7734 | abs < 1e-3 |
| C11, C44 at ν=2/7 | 0.72786, 0.24876 | rel < 1e-4 |
| Zener at ν=2/7 | 1.2293 | rel < 1e-3 |
| K/G_Hill at ν=2/7 | 2.0000 | abs < 1e-3 |

If A_wall=0 does NOT reproduce these ⟹ the saturated extraction is wrong; **HALT, report no
saturated verdict.** (This reuses the cold driver's own validate-on-known V1/V2/V3 harness on the
IDENTICAL pipeline — the saturated driver imports the cold extraction functions unmodified and only
prepends the per-channel S(A) stiffness maps.)

## READOUTS (frozen; reported whatever they say) — per operating point, per assignment

1. **C_ij** (C11_elastic, C12, C44) — full cubic tensor.
2. **K = (C11+2C12)/3** (bulk), and **sign(K)** (the stability boundary).
3. **G_Voigt, G_Reuss, G_Hill** (the anisotropy spread) and **C′=(C11−C12)/2**.
4. **ν_Voigt, ν_Reuss, ν_Hill** — compared to 2/7.
5. **Zener anisotropy A = 2C44/(C11−C12)**.
6. **The saturated ν(ρ_eff) MAP** — the deliverable: ν_Hill vs ρ_eff across the full A_wall sweep,
   compared bit-for-bit against the cold ν(ρ) map at matched ρ_eff.
7. **Absolute-scale readout (the NEW physics vs cold):** the overall stiffness scale
   `λ_abs = S_axial` (or `S_shear`; report both) and the acoustic-speed softening — K, G, and the
   longitudinal/transverse slopes at each operating point in ABSOLUTE (S-scaled) units, showing the
   floppy-near-yield limit. This is the axis the cold arc could not see.
8. **Worst-case internal acoustic Γ** — the reflection at the worst internal impedance step across
   the sweep (per Ax3, the substrate minimizes |Γ|²): report max over directions of the acoustic
   impedance mismatch |Γ| = |Z_1−Z_2|/|Z_1+Z_2| between the softest and stiffest acoustic branch
   at each operating point (a mechanical-stability / internal-matching diagnostic).
9. **sign(K) stability boundary** vs the cold ρ=2 one — does saturation SHIFT it (predicted: no,
   sign is scale-invariant) or preserve it.

## VALIDATE-ON-KNOWN (frozen; HALT if fail) — reuses the cold pipeline's proven harness

The saturated driver's extraction is the SAME `extract_cubic_Cij` / `acoustic_christoffel` the cold
arc validated. The saturated arc adds THREE saturated-specific validate-on-known checks on top of
the inherited V1/V2/V3 (simple-cubic, diamond-Born-vs-symbolic, isotropy):

| # | Check | Target | Tol | Rationale |
|---|---|---|---|---|
| VS1 | **cold-recovery**: A_wall=0 both assignments → C_ij = cold C_ij at ρ=1 | the positive-control table above | rel<1e-6 | S=1 must recover the merged cold tensor exactly (planted-source gate) |
| VS2 | **homogeneity**: C_ij(λk_a, λk_s)/λ = C_ij(k_a, k_s) for arbitrary λ; and ν/Zener/(K/G) IDENTICAL under λ-scaling | rel<1e-7 (ratios), rel<1e-7 (C_ij/λ) | the load-bearing §0.6 claim, tested directly: an overall stiffness scale drops out of ratios, scales C_ij by λ |
| VS3 | **saturated == cold-at-matched-ρ_eff**: saturated tensor at (S_axial, S_shear) gives the SAME ν/Zener/(K/G) as cold at ρ=S_axial/S_shear | rel<1e-7 | the [SAME-TENSOR-POINT] mechanism, tested on the SAME extraction |

VS2 + VS3 are the discriminators between [SAME-TENSOR-POINT] and [DEFORMED-FAMILY]: if VS3 passes
to 1e-7 at every operating point, the family is NOT deformed (SAME-TENSOR-POINT); if it fails at
some A_wall, that is [DEFORMED-FAMILY] and the driver reports WHERE and by how much.

## FROZEN ADJUDICATION BINS (per-assignment — SHEAR-LOADS and AXIAL-LOADS each get one)

Frozen VERBATIM from the brief; bins are per-assignment.

- **[SAME-TENSOR-POINT].** At the shear-loads operating point where ρ_eff=9.7734, the saturated
  tensor delivers ν_Hill=2/7 / K=2G to the cold arc's precision (rel<1e-4) ⟹ **the regime gap
  CLOSES**; saturated ρ_eff is tensor-equivalent to cold ρ. (Predicted by §0.6 homogeneity.)

- **[DEFORMED-FAMILY].** Saturation deforms the ν(ρ_eff) map; ν=2/7 lands at a DIFFERENT ρ_eff
  (report where) ⟹ the cold read-across was invalid; the #518 direction result survives but its
  9.77-crossing loses tensor meaning. (Would falsify §0.6 — VS3 would fail.)

- **[NEW-DISTINGUISHED-POINT].** A canon-forced A (√α, 1−α, or the A→1 yield limit) lands ON ν=2/7
  in the saturated family ⟹ **MAXIMUM knife scrutiny**: 2/7, 9.7734, and 0.99479 are ALL visible
  targets; re-derive from scratch, check EVERY input for smuggled tuning, do NOT celebrate; report
  the chain skeptically. (The a-priori expectation from #518 is the OPPOSITE — the crossing
  A_wall=0.99479 is NOT canon-distinguished, so this bin is expected EMPTY. If it fires, treat as
  a red flag for a hidden tuning, not a discovery.)

- **[UNSTABLE].** K<0 at the operating points that matter ⟹ report the saturated stability boundary
  vs the cold ρ=2 one. (Predicted: sign(K) is scale-invariant, so the boundary stays at ρ_eff=2;
  the shear-loads matter branch ρ_eff>1 is stable only above ρ_eff=2, i.e. A_wall above the
  S_axial/S_shear=2 point.)

**KEEP-BOTH discipline:** the saturated ν(ρ_eff) axis lives ALONGSIDE the cold-ρ axis in the result
doc; the cold result is NEVER restated as superseded. The channel-assignment fork is a formal
recorded axis (both blind), not a pre-picked branch.

**[STUCK-FRAMING → Grant].** A framing fork the axioms + corpus cannot settle (a NEW one beyond the
§0.5-resolved ontology + channel-assignment forks). STOP and surface.

## FALLOUT MAP (frozen before any saturated number)

The saturated arc's verdict RIDES ON the cold arc's fallout map (`srs-elastic-tensor_prereg_FROZEN.md`
F.A–F.D — the /7 PPN family, NU_VAC, K=2G leaves). The saturated arc does NOT re-open those; it
resolves ONE flagged scope tension (#518 §6). The per-bin fallout:

| Bin | Fallout on the corpus |
|---|---|
| **[SAME-TENSOR-POINT]** | STRENGTHEN #518's §6 cross-link: the saturated ρ_eff=9.77 DOES reach the same cold ν=2/7/K=2G tensor. But NOTE the knife: this does NOT make 9.77 emergent — it makes the saturated small-signal tensor a SCALED cold tensor; ρ_eff=9.77 is still reached only at the free-knob A_wall=0.99479 (#518 [DRIVES-STIFF-QUALITATIVE] stands). The tensor-equivalence is a CONSISTENCY finding (the map is not deformed), NOT a value derivation. The K=2G-imported grade (PR#261) is UNTOUCHED. |
| **[DEFORMED-FAMILY]** | The #518 §6 flag becomes a HARD SEPARATION: the saturated ρ_eff is NOT tensor-equivalent to cold ρ; the 9.77-crossing has no tensor meaning; #518's mechanism-candidate weakens further (surface with both file paths + the deformation magnitude). |
| **[NEW-DISTINGUISHED-POINT]** | Max scrutiny; if it survives re-derivation, surface for Grant + auditor as a potential (skeptically-reported) canon point — do NOT land any manual. |
| **[UNSTABLE]** | Report the saturated stability boundary; if it shifts from cold ρ=2, that is a NEW finding (would contradict §0.6 sign-invariance — flag it). |

**No rewrites performed.** The result doc proposes status-demotion/strengthen/cross-link ROWS only;
the auditor lane lands the manual entries. Any contradiction with canon is surfaced VERBATIM in the
result doc §flags (flag-don't-fix), not resolved unilaterally.

## OUTPUT

`src/scripts/vol_1_foundations/saturated_elastic_tensor.py` → `_output/saturated_elastic_tensor.json`
(gitignored; driver-regenerable): the VS1/VS2/VS3 validate table, the per-assignment ν(ρ_eff)/Zener/
K-G sweeps, the per-direction slope table at the crossing, the absolute-scale/floppy readout, the
worst-case Γ, the two-hand cross-validation at ≥3 points, the per-assignment bin verdicts.
Test: `src/tests/test_saturated_elastic_tensor.py`. Result doc:
`research/2026-07-04_saturated-elastic-tensor_result.md`. NO self-merge; PR titled with the bin
verdict, tagged [REVIEW: pending-orchestrator].

## Cross-references (verified at branch HEAD)

- COLD arc (merged): `research/2026-07-04_srs-elastic-tensor_result.md`;
  driver `src/scripts/vol_1_foundations/srs_elastic_tensor.py`; prereg
  `research/2026-07-04_srs-elastic-tensor_prereg_FROZEN.md`
- #518 (MERGED 6d2ecdf4): `research/2026-07-04_matter-stiffening-rho_result.md`;
  driver `src/scripts/vol_4_engineering/matter_stiffening_rho.py` (exact loading defs §"THE TWO
  CHANNEL-ASSIGNMENTS"); §6 the scope flag this arc closes
- Sector ownership (both k_a,k_s capacitive): `matter-stiffening-rho_result.md` §sector header;
  `node-up-small-large-signal.md:45-51` (port map)
- Kernel S(A): `src/ave/axioms/scale_invariant.py` `saturation_factor`, `shear_modulus_ratio`
- Varactor-bias / operating-point (INVARIANT-S2): `manuscript/ave-kb/CLAUDE.md`
- Ratio-invariance sibling (EM sector, Z=Z_0 under symmetric loading):
  `per-dof-vacuum-node-circuit.md:60`; `research/2026-06-22_c4-symmetric-loading-reconciliation.md:42`
- Floppy / topology melts: `electron-bh-isomorphism.md:32`; `k2g-crystalline-provenance_result.md:57`
- K/G one-parameter family in ρ: `research/2026-06-15_form-deriving-value-importing_meta-finding.md:161`
- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net`
- Constants: `ALPHA`, `NU_VAC` from `src/ave/core/constants.py`
