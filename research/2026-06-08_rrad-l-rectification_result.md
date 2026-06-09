# Result — acoustic-rectification DC momentum (dark-wake thrust, Phase 2)

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-rrad-l-darkwake` (Phase 2; same branch as Phase 1)
**Prereg**: [`2026-06-08_rrad-l-rectification_prereg.md`](2026-06-08_rrad-l-rectification_prereg.md)
**Driver**: [`src/scripts/vol_4_engineering/rrad_l_acoustic_rectification.py`](../src/scripts/vol_4_engineering/rrad_l_acoustic_rectification.py)
**Phase-1 result**: [`2026-06-08_rrad-l-darkwake_result.md`](2026-06-08_rrad-l-darkwake_result.md)
**Adjudication seed**: [`AVE-Propulsion-ionpump/research/2026-06-08_NEXT-STEP_Rrad-L_core-brief.md`] §"ADJUDICATION 2026-06-08 (Grant)".
**Home leaf (mechanism)**: AVE-Propulsion `manuscript/vol_propulsion/chapters/03_acoustic_rectification.tex`.

> **HONEST-CLOSURE STATEMENT (ave-driver-script-honesty, Rule 11).** This is a
> **clean NEGATIVE on the rectification signature** with a **single named
> mechanism** (Rule 7), plus a clean **SHEAR** mode verdict. The asymmetric
> duty cycle did **NOT** produce a directed DC momentum that the symmetric
> control lacks — across three waveforms (symmetric triangle, asymmetric
> triangle, faithful flyback) and three grids — **even with the Axiom-4
> saturation slip valve fully engaged**. The result is NOT a rescue-debuggable
> "almost"; it is a structural finding about what the engine's saturation model
> can and cannot rectify. The absolute thrust magnitude remains BLOCKED (same
> gate as Phase 1). No false closure is claimed in either direction: this does
> not *prove* AVE cannot thrust, it shows the canonical chiral-ω drive + the
> engine's instantaneous-even saturation kernel do not exhibit rectification.

---

## 0. Headline (the three questions)

1. **Did the asymmetric cycle produce nonzero DC momentum while the symmetric
   control gave zero (rectification = ledger ∮≠0)?** **NO — rectification NOT
   confirmed.** The symmetric control does **not** null. The far-field 2nd-order
   momentum is dominated by a large **non-chiral common-mode radiation pressure**
   (`ρ⟨u̇²⟩`), essentially **identical** for symmetric and asymmetric drive at
   equal peak (`J_cm`: SYM `+0.882` vs ASYM `+0.886`). The chiral-**directed**
   part is small (`J_dir ≈ 0.7%` of common-mode) and is **NOT enhanced** by
   time-asymmetry: the directed momentum from the asymmetric triangle (`|J_dir|
   = 3.8e-3`) and the faithful flyback (`1.9e-3`) are **smaller** than the
   symmetric control (`6.1e-3`) — rectification ratios **0.62** and **0.31**,
   both **< 1**, the opposite of the predicted "≫1 with SYM→0".
2. **Is BOTH-breakings-required confirmed?** **NO.** The time-asymmetry breaking
   produces **no contrast at all** in the directed-momentum channel, so the
   "both required" claim cannot be confirmed — the rectification (time) leg
   fails outright. Only the chiral breaking shows a directed part, and that part
   is **marginal** (grid-sign-unstable, noise-floor) and **symmetric-drive-
   invariant** → it is the chiral **grip** (reactive, parity-set), **not**
   rectification.
3. **Is the bounce BULK or SHEAR — does the electron-unification recover?**
   **SHEAR (2/7, photon channel), robustly** (K4-native far-slab strain
   `bulk_fraction = 0.40` for triangles, `0.24` for flyback — all `< 0.5` across
   N=24/28/32). **The Q→∞ electron pilot-wave unification does NOT recover at
   the mode level.** The chiral ω-Beltrami source drives the shear/microrotation
   sector by construction (`ε_antisym = −ε_ijk ω`); the bulk-P-wave (1/7,
   electron) channel would require a translational/compressional drive (BLOCKED).
   Phase-1's shear assignment holds for the 2nd-order object too.

**Single mechanism (Rule 7) — why all of the above:** the engine's Axiom-4
saturation kernel `S(A) = √(1−(A/A_yield)²)` is an **instantaneous EVEN function
of A** (no hysteresis / no memory). Two consequences compose:
- **⟨A²⟩-invariance (analytic):** a triangle's mean-square amplitude `∫₀¹A²dφ =
  A_peak²/3` is **independent** of the charge/quench asymmetry `f`. So any
  quadratic / even-in-A response (radiation pressure, the even saturation kernel)
  produces **identical** 2nd-order momentum for symmetric and asymmetric drive.
- **No hysteretic slip valve:** rectification per `03_acoustic_rectification.tex`
  needs the slip to be a distinct **zero-impedance phase (Γ=−1) the medium
  *enters* on the fast edge and does NOT symmetrically reverse** — a
  rate-dependent / state-dependent (memory) nonlinearity. An even-in-A
  instantaneous kernel cannot break the charge↔quench time-symmetry into a net
  directed DC.

This one mechanism explains every observation: (a) common-mode ≈ identical
SYM/ASYM; (b) directed part not enhanced by asymmetry; (c) saturation engagement
(`A²_src` up to 15) does not help; (d) the faithful flyback (slip-on-fast-edge)
also fails.

**Classification:** Class-B **manifestation** (consistency-class), CP8 emergence
does NOT fire (driven source). As pre-registered.

---

## 1. DERIVED (analytic, corpus-grounded)

- **The thrust object** = the 2nd-order directed momentum-flux tensor
  `T_ij = −σ_ij + ρ u̇_i u̇_j` (Cauchy stress + convective Reynolds stress), with
  `σ` from the engine's own linear Cosserat energy density (constitutive form
  IDENTICAL to the Phase-1 driver, reused as the single source of truth). The
  directed (thrust) observable is the chiral-antisymmetric far-slab axial
  component `J_dir = (T_pp^RH − T_pp^LH)/2`; the non-chiral common-mode
  `(T_pp^RH + T_pp^LH)/2` is generic radiation pressure.
- **⟨A²⟩-triangle identity:** for an asymmetric triangle (rise over `f`, fall
  over `1−f`), `∫₀¹A²dφ = f/3 + (1−f)/3 = A_peak²/3` — **independent of `f`**.
  → A quadratic-order / even-in-A 2nd-order momentum is **identical** for the
  symmetric and asymmetric triangle by construction; rectification requires a
  **rate-dependent / hysteretic (odd-order in the edge direction)** coupling.
  This is the analytic core of the null and is resolution-independent.
- **Hysteresis gap (the structural finding):** `03_acoustic_rectification.tex`
  describes the slip as the medium *entering* a saturated zero-impedance phase
  on the fast edge and slipping backward (state-/rate-dependent). The engine's
  kernel `S(A) = √(1−(A/A_yield)²)` ([cosserat_field_3d.py:332,837](../src/ave/topological/cosserat_field_3d.py),
  `ω_yield = π`) is **instantaneous and even in A** — it carries no hysteresis.
  The rectifier the leaf's mechanism requires is **not implemented** by the
  engine's saturation model. (Flag-don't-fix; §4 + §7 queue.)
- **Source-sector assignment:** the chiral ω-Beltrami source injects
  `ε_antisym = −ε_ijk ω` (pure microrotation) → it drives the **shear sector**
  (2/7, photon channel) by construction. Testing the bulk-P-wave (1/7, electron)
  channel needs a translational/compressional drive — a separate source.

## 2. NUMERICALLY VERIFIED (smoke, qualitative — SIGNS / RATIOS / CONTRAST only)

Representative run N=28, pml=4, amp=1.4, carrier λ=4 steps, duty=16 steps,
charge_frac(ASYM)=0.85, 4-integer-cycle average (robust across N=24/28/32,
amp=1.0/1.4/2.0):

| cond | `T_pp` far-slab | `conv` (ρ⟨u̇²⟩) | `A²_src` max/mean | strain bulk-frac |
|---|---|---|---|---|
| SYM_LH | +0.889 | +0.889 | 4.63 / 1.75 | 0.436 |
| SYM_RH | +0.876 | +0.889 | 4.68 / 1.75 | 0.492 |
| ASYM_LH | +0.890 | +0.892 | 4.54 / 1.69 | 0.398 |
| ASYM_RH | +0.882 | +0.891 | 4.62 / 1.69 | 0.406 |
| ASYM_NC (linear) | +0.434 | +0.440 | 3.84 / 0.85 | 0.411 |
| FB_LH (flyback) | +0.253 | +0.253 | 3.58 / 0.59 | 0.234 |
| FB_RH (flyback) | +0.249 | +0.253 | 3.52 / 0.58 | 0.245 |

- **Far-field momentum ≈ pure radiation pressure.** `T_pp ≈ conv = ρ⟨u̇²⟩` for
  every condition (the linear `−σ_pp` part is tiny by comparison). This is the
  generic 2nd-order acoustic radiation pressure — **non-chiral, non-directional,
  always positive (outward).**
- **No rectification.** Directed `J_dir`: SYM `−6.07e-3`, ASYM `−3.79e-3`,
  flyback `−1.91e-3` → ratios **0.62** (ASYM) and **0.31** (FB), both **< 1**.
  The asymmetric and flyback drives produce **less** directed momentum than the
  symmetric control, not more. Common-mode radiation pressure SYM `+0.882` ≈
  ASYM `+0.886` (the ⟨A²⟩-identity, confirmed numerically). The flyback's lower
  common-mode (`+0.251`) is simply its lower average amplitude (sub-yield grip),
  not rectification.
- **Slip valve engaged, no effect.** `A²_src` crosses yield in every drive
  (`A²_max` = 2.3–15 across amps); the flyback grip is **sub-yield**
  (`A²_mean ≈ 0.58`) while its spike is **over-yield** (`A²_max ≈ 3.5`) — the
  faithful flyback geometry. Engaging the valve does **not** produce rectification.
- **Chiral-directed part is marginal.** `J_dir` is ~0.7% of common-mode and its
  **sign flips with grid size** (N=28 negative; N=24/32 positive) → it sits at
  the standing-wave / sublattice noise floor, not a robust directed thrust. The
  one faint chiral-opposite hint is the flyback `P_x`-drift (`LH +3.5e-4`,
  `RH −1.7e-4`), but `P_x`-drift is transient-fill-contaminated (positive and
  non-chiral for the triangles) and is reported, not claimed.
- **Mode = SHEAR.** K4-native far-slab strain `bulk_fraction = 0.40` (triangles),
  `0.24` (flyback) — robustly `< 0.5` → the excited far field is deviatoric/
  rotational (shear), not dilatational (bulk). 2/7/photon channel.

## 3. Two live measurement fixes (empirical-driver discipline, Rule 10)

Both surfaced at integrator time, not in static design — and both materially
changed the numbers:
1. **Bipartite-lattice staggered sampling.** The K4 lattice is bipartite and the
   `u` field carries a **staggered odd-even node structure** (every other
   `x`-plane is a near-node, `|u| ~ 10⁻⁸` vs `~0.3`). A single far-**plane**
   landed on a node, giving a spurious `conv ≈ 0` and an apparent
   `strain_bulk_frac = 0.53`. **Fix:** sample a multi-plane far **SLAB**
   (PML-excluded) spanning both sublattices → the real `ρ⟨u̇²⟩ ≈ 0.89` appears
   and `bulk_frac` settles to its true `0.40` (SHEAR).
2. **Non-K4-native gradient.** The first decomposition used `np.gradient` of `u`
   (Cartesian stencil) → read `0.000` at the node plane while the K4-native
   `_compute_strain` (tetrahedral gradient) read `O(1)`. **Fix:** removed the
   `np.gradient` path entirely; bulk-vs-shear uses only the substrate-native
   `_compute_strain` stencil. (Had I trusted the single-plane `np.gradient`
   read, I would have reported a spurious BULK 0.53. The corrected, robust
   answer is SHEAR 0.40.)

## 4. FLAG — corpus tension (flag-don't-fix; for Grant adjudication)

The negative is **mechanistically located**, not mysterious — and it surfaces a
genuine tension between two canonical pieces, surfaced (not silently resolved):

- **`03_acoustic_rectification.tex`** (AVE-Propulsion, the thrust mechanism)
  requires a **hysteretic slip valve**: the medium *enters* a saturated
  zero-impedance phase (`Γ=−1`) on the fast quench and slips backward,
  transferring **zero** negative momentum — a state-/rate-dependent (memory)
  nonlinearity.
- **The engine's Axiom-4 kernel** `S(A) = √(1−(A/A_yield)²)` (INVARIANT-S2;
  cosserat_field_3d.py) is **instantaneous and even in A** — no hysteresis.

These are physically different nonlinearities. An even-in-A instantaneous kernel
**cannot** rectify a time-asymmetric drive into a directed DC (the ⟨A²⟩ identity
+ §0 single mechanism). **Either** (a) the rectification mechanism needs a
hysteretic-valve refinement to be substrate-realizable (the slip is a *phase the
medium latches into*, not an instantaneous function of the present amplitude),
**or** (b) the engine's saturation model is missing the memory the leaf assumes.
This is a substrate-physics question — surfaced for Grant, not adjudicated here.

## 5. Bulk-vs-shear + the unification gate

- **Verdict: SHEAR** (2/7, photon channel), robust across grids/amps/waveforms.
  The as-driven dark wake lives in the **shear/microrotation sector** — the same
  channel Phase 1 assigned to the *linear* object, now confirmed for the
  *2nd-order* object.
- **Q→∞ electron pilot-wave unification does NOT recover at the mode level.** The
  reframe's hope (brief §"Open" (1): if the bounce is bulk-acoustic P-wave the
  electron unification recovers) is **not realized with the canonical chiral
  ω-source**, because that source drives the shear sector by construction
  (`ε_antisym = −ε_ijk ω`). The bulk-P-wave (1/7, electron) channel is
  **structurally inaccessible to an ω-only drive** → the unification recovery is
  deferred to a translational/compressional source design (BLOCKED §6).

## 6. What is DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED (analytic):**
- Thrust object `T_ij = −σ_ij + ρ u̇_i u̇_j`; directed observable `J_dir`.
- ⟨A²⟩-triangle identity → quadratic/even-in-A response is asymmetry-blind →
  rectification needs a rate-dependent/hysteretic nonlinearity.
- The engine's even-in-A instantaneous `S(A)` lacks that hysteresis → the
  rectification mechanism of `03_acoustic_rectification.tex` is not implemented.
- The chiral ω-Beltrami source drives the shear sector by construction.

**NUMERICALLY VERIFIED (smoke, qualitative):**
- Far-field 2nd-order momentum = non-chiral common-mode radiation pressure
  `ρ⟨u̇²⟩`, ⟨A²⟩-controlled (SYM ≈ ASYM at equal peak).
- NO rectification: directed `J_dir` ratios 0.62 (ASYM), 0.31 (flyback), both
  `< 1`, across N=24/28/32 and amp=1.0/1.4/2.0.
- Saturation slip valve engaged (`A²_src` ≫ 1; flyback spike over-yield, grip
  sub-yield) without producing rectification.
- Mode = SHEAR (`bulk_frac` 0.24–0.49, all `< 0.5`).
- Chiral-directed part marginal (~0.7% of common-mode, grid-sign-unstable).

**BLOCKED (precise remaining gaps):**
1. **Absolute thrust magnitude** — same gate as Phase 1 (converged radiating
   sim + a defensible source-"current" normalization). Only signs/ratios/
   contrasts are trustworthy this pass.
2. **Whether a HYSTERETIC saturation valve would rectify** — the leaf's actual
   mechanism. Requires implementing a memory/state-dependent (latching) slip
   nonlinearity in the engine — a NEW model, not the canonical even-in-A kernel.
   Named follow-on; not attempted (would be a rescue-build, out of scope for this
   honest-closure pass).
3. **The translational/bulk-P-wave "genuine bounce" channel** — the chiral
   ω-source is shear-sector by construction; testing the bulk/electron-channel
   recovery needs a translational/compressional drive (separate source design).
4. **Spike time-resolution** — the flyback spike is ~2 steps at duty=16; finer
   resolution is a convergence caveat (the ⟨A²⟩/even-in-A argument is
   resolution-independent, but the dynamical-memory test in (2) would need it).

## 7. Result-time skills (discrimination / consistency / provenance)

- **consistency-vs-emergence → Class-B manifestation.** The measured 2nd-order
  momentum is a property of a **driven** source (CP8 does NOT fire), assembled
  from corpus quantities. As pre-registered. Not headlined as emergence.
- **ave-discrimination-check → the measured effect is GENERIC, not AVE-distinct.**
  The dominant signal (`ρ⟨u̇²⟩` common-mode radiation pressure) is **generic
  acoustic radiation pressure** — any nonlinear medium has it; it carries no
  handedness and no rectification. The AVE-distinct content that *would* have
  been the headline (chiral parity-directed **rectified** thrust) is **NOT
  demonstrated** — the chiral-directed part is marginal/noise and the
  rectification is absent. So this pass produces **no AVE-distinct thrust signal**;
  it produces a generic streaming background + a mechanism diagnosis.
- **ave-dimensional-provenance-check.** `T_ij = −σ_ij + ρ u̇_i u̇_j` has clean
  momentum-flux dimensions `[Pa] = [N/m²]` throughout (Cauchy stress +
  Reynolds stress), unlike the dimensionally-underspecified legacy
  `τ_zx = ρ_Op14·Z_vac·∇|E|²`. The object is dimensionally sound; the BLOCKED
  item is the absolute normalization, not the dimensions.

## 8. Honest closure (Rule 11) + substitution-not-retraction (Rule 12)

The Phase-2 hypothesis — *"the asymmetric duty cycle rectifies the reactive grip
into a chiral-directed DC thrust (the ledger ∮≠0) in the AVE engine"* — is
**falsified for the canonical chiral-ω drive + the engine's instantaneous-even
saturation kernel**, with a single explanatory mechanism (the even-in-A kernel
has no hysteretic slip valve; ⟨A²⟩ is asymmetry-invariant). Per Rule 11 this is
the discipline working at full strength: a clean negative, one mechanism named,
branch finding recorded. **No rescue-debug toward a positive** (the obvious next
move — building a hysteretic valve to *make* it rectify — is named as BLOCKED
follow-on §6.2, NOT executed, because that would be filling the falsified slot
with an unverified new mechanism — Rule 12). The dark-wake-as-thruster premise is
now deflated on **both** the linear object (Phase 1: high-Q reactance) and the
2nd-order rectified object (Phase 2: no rectification with the even-in-A kernel).

What SURVIVES (preserve, do not over-retract): the **mechanism diagnosis** is a
positive deliverable — it tells the corpus *exactly* what a substrate-realizable
acoustic-rectification thruster would need (a hysteretic/latching slip valve,
not an instantaneous saturation), and that the canonical chiral ω-source is
shear-sector (so a bulk-channel electron-unification needs a translational
drive). These are forward-useful constraints, not just a null.

## 9. Corpus-state deltas to queue (auditor lands these — I surface only)

- **`clm-7tynm2` (dark-wake τ_zx thrust object):** the 2nd-order rectified-DC
  reading of the thrust object is **NOT confirmed** in the AVE engine — the
  asymmetric/flyback duty cycle produces no directed DC the symmetric control
  lacks (rectification ratios 0.62/0.31 < 1), with the even-in-A saturation
  kernel as the named cause. Phase-1's deflation (reactance-dominated linear
  object) now extends to the 2nd-order object. Mode = SHEAR confirmed.
- **FLAG for Grant (corpus tension):** `03_acoustic_rectification.tex` (hysteretic
  slip valve) vs the engine's Axiom-4 kernel `S(A) = √(1−(A/A_yield)²)`
  (instantaneous, even in A). The rectification mechanism requires hysteresis the
  kernel does not carry. Substrate-physics adjudication: refine the mechanism to
  a latching valve, or extend the saturation model. (§4.)
- **Q→∞ electron unification:** does NOT recover at the mode level via the chiral
  ω-source (shear-sector by construction). Recovery (if any) is gated on a
  translational/compressional drive — a new source-design workstream.
- **Driver capability added:** `rrad_l_acoustic_rectification.py` — reusable
  2nd-order momentum-flux + duty-cycle/flyback drive + K4-native far-slab
  bulk-vs-shear extractor (the two Rule-10 sampling fixes baked in).
