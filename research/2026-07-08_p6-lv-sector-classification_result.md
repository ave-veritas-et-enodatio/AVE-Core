# P6-LV — which SECTOR sources the nonlinear-sector Lorentz violation, and does it map to a bounded SME coefficient? RESULT

**Status:** RESULT. Adjudicates the fork frozen in
`research/2026-07-08_p6-lv-sector-classification_prereg_FROZEN.md`.
**Date:** 2026-07-08 · **Lane:** implementer. **Part:** P6 make-or-break, **Part 1**.
**Class (consistency-vs-emergence):** **CONSISTENCY.** Sector ownership (A1 vs T2) of an EXISTING
non-covariant kernel + classification against an external LV framework (SME). No new claim-id /
constant / axiom. Q=137 stays empty. The 4.9×10⁻³ magnitude rides the external β = v_CMB/c (settled
upstream, PR #574 / #579); it is NOT re-derived here.
**Driver:** `src/scripts/vol_9_device/p6_lv_sector_classification.py`
(run: `PYTHONPATH=src python3 src/scripts/vol_9_device/p6_lv_sector_classification.py`).
**Tests (7, all green):** `src/tests/test_p6_lv_sector_classification.py`.
**Artifact + figure (driver-regenerable, gitignored):**
`src/scripts/vol_9_device/_output/p6_lv_sector_classification.{json,png}`.
**Builds on:** `research/2026-07-08_p6-frame-boost-dependence_result.md` (#579) — kernel keys on
magnitude |E|, BULK corner, first-harmonic P_flip = 4β ≈ 4.94×10⁻³.
**Loci GROUNDED (read-only; NOT edited here — auditor/orchestrator integrates):**
`src/ave/bench/birefringence.py:158-224`, `src/ave/core/constants.py:476-506`,
`manuscript/ave-kb/common/substrate-native-terminology.md:52-65`,
`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:18-20`,
`manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md:189,221`,
`papers/2026_birefringence_letter/main.tex:402-432,850-865`.

---

## ★ VERDICT BOX — SPLIT: Grant's frame-anchor CONFIRMED, Grant's response-sector REFUTED

> **The LV RESPONSE lives in the TRANSVERSE-T2 photon sector; the PREFERRED FRAME is anchored by the
> A1 dilatation rest-mass.** These are two different questions and they answer two different ways —
> reported as a split, not collapsed to one horn (flag-don't-fix; the anti-bias brief forbids steering
> to "longitudinal/unconstrained" to save the flagship).
>
> - **RESPONSE CHANNEL = TRANSVERSE-T2 (Grant REFUTED here).** The birefringence kernel modulates
>   `ε_eff = ε₀·S` — which the canon (`substrate-native-terminology.md:65`;
>   `dual-reactance-storage-taxonomy.md`) names the **transverse-T2 permittivity** (↓ as `S→0`),
>   explicitly ORTHOGONAL to the **longitudinal-A1 compliance** `C₀/S` (↑). Both uniaxial eigen-
>   permittivities in the Letter (`main.tex:857`: `ε₀S` "transverse", `ε₀(S+2S'E²)` "longitudinal")
>   are **T2-photon** permittivities — that "longitudinal" is the **optic-axis orientation** (probe ∥
>   pump), NOT the A1 grade. Grant's claim "the non-covariant RESPONSE is the A1/longitudinal
>   compression mode" would wire the A1 dilatation-scalar into the transverse-photon sector — the
>   canonically-named **two-"3"s double-count** (`master-equation.md:20`;
>   `terminology.md:54`: "the photon **is** transverse … no longitudinal component"). It is REFUTED.
>
> - **FRAME ANCHOR = A1 (Grant CONFIRMED here).** A massless T2 photon is null: no rest frame, Lorentz-
>   covariant by itself (an invariant-keyed kernel gives ZERO pump birefringence, D1). The only reason a
>   preferred frame EXISTS to violate against is that the saturating node is a MASSIVE material element:
>   `E_YIELD = √α·E_CRIT = √α·mₑc²/(e·ℓ_node)` chains to `mₑ` — the **A1 dilatation rest-mass**
>   ("trapped acoustic compression energy", `master-equation.md:20`; saturation onset =
>   "energy density = rest energy per cell", `constants.py:503`). So the LV **exists-because-of A1**
>   (the A1 mass sets the substrate/CMB rest frame), while the LV **response lives in T2** (the readout).
>
> **NET SECTOR VERDICT: TRANSVERSE-T2 response, A1-anchored frame.** Grant's deep intuition — the LV
> is not intrinsic to the transverse photon (which is covariant); it traces to the A1-massive substrate
> — is CORRECT for the FRAME. But his operational claim — that the response is A1/longitudinal and
> therefore transverse-sector experiments are STRUCTURALLY BLIND — is REFUTED: the response is a
> transverse-photon permittivity saturation. Transverse experiments are not structurally blind; they
> are blind to THIS effect for a different reason (below: it is NONLINEAR, they bound LINEAR coefficients).

---

## SME CLASSIFICATION — NONLINEAR photon-sector object, NOT minimal-SME k_F / k_AF

The minimal-SME photon coefficients are CONSTANT background tensors coupling to the LINEAR field
strength F²: **k_F** (CPT-even, mass-dimension-4, dimensionless, 19 components) and **k_AF** (CPT-odd,
mass-dimension-3, dimensionful). Both are **field-amplitude-INDEPENDENT** — present in vacuum at zero
field (`∂(coeff)/∂E = 0`); they are exactly the coefficients that cavity/Michelson resonator and
astrophysical-vacuum-birefringence experiments bound.

The AVE birefringence coefficient is `c_bir(E) = −½·(E/E_YIELD)²` (D5): it **VANISHES at E=0** and
`∂c_bir/∂E = −E/E_YIELD² ≠ 0` — it is **field-amplitude-DEPENDENT (NONLINEAR)**. It requires a pump
field to exist. Therefore it is **NOT k_F and NOT k_AF**, independent of sector — a NONLINEAR /
higher-dimension photon-sector object. (Planted control, D5: a constant background is flagged
field-independent = k_F-class; the AVE ∝A² coefficient is flagged NONLINEAR. Both verdicts reachable.)

**Consequence for the flagship's escape.** The existing transverse LINEAR LV bounds (cavity/Michelson
on k_F, astrophysical birefringence on k_F/k_AF) do NOT constrain the AVE effect — but the correct
reason is **LINEAR-vs-NONLINEAR, not longitudinal-invisibility.** The linear cubic-symmetry photon
anisotropy IS suppressed to `(qℓ_node)⁴ ≈ 2.2×10⁻²²` (the k_F channel, `preferred-frame-and-emergent-
lorentz.md:§2`), consistent with those bounds. The 4.9×10⁻³ sidereal signal lives in the ORTHOGONAL
NONLINEAR channel (a field-amplitude-keyed pump-probe response with a preferred frame). Standard SME
carries no minimal photon-sector coefficient for a preferred-frame NONLINEAR vacuum birefringence.
It is, however, a **transverse-photon-sector** object in principle — a dedicated nonlinear /
higher-dimension / intensity-dependent photon-sector LV experiment COULD bound it. **This hands Part 2
a concrete target: NOT the k_F/k_AF tables (those are linear), but nonlinear / higher-dimension /
strong-field preferred-frame photon-sector LV bounds — and whether any reach the 4.9×10⁻³ level.**

---

## THE SECTOR DECOMPOSITION (five discriminators, all read off engine + canon)

| # | discriminator | reads | result |
|---|---|---|---|
| **D1** | invariance class of the kernel argument | `birefringence.py`; sympy | radiation pump ⇒ `F=B²−E²/c²=0`, `E·B=0` ⇒ invariant-keyed kernel = 0 pump birefringence; **live kernel keys on MAGNITUDE |E|** — non-covariance ENTERS here (but this alone does not assign the sector). |
| **D2** | which reactance the kernel modulates (**load-bearing**) | `birefringence.py` (`n=√(ε_eff/ε₀)=√S`) vs canon `terminology.md:65` | `ε_eff=ε₀·S` **DROPS** with A = the **transverse-T2 permittivity** branch (not the A1 compliance `C₀/S`, which RISES). `δn_bir/δn_iso ≈ 2` — par-perp is 2× isotropic, **both T2-photon**. **RESPONSE = T2.** |
| **D3** | frame-anchor provenance | `constants.py:476-506`; two routes | `E_YIELD` chains to `mₑ` two agreeing ways (`√α·E_CRIT`; `√α·mₑc²/(e·ℓ)`) = the **A1 rest-mass**. Massless T2 photon has no rest frame ⇒ **FRAME ANCHOR = A1.** |
| **D4** | boost-order projection sense | sympy β-expansion of `D=γ(1−βcosθ)` | linear-β coeff of `\|E\|^p` = `−p·cosθ` ⇒ the **O(β)** first harmonic rides `β·k̂` (**propagation-parallel** projection); a **transverse** boost (`cosθ=0`) → `1+2β²` = **O(β²)**. This "longitudinal" is the propagation sense — a THIRD sense, kept distinct from A1-grade and optic-axis. |
| **D5** | SME field-dependence | sympy | `c_bir=−½(E/E_YIELD)²`: `c_bir(0)=0`, `∂c_bir/∂E≠0` ⇒ **NONLINEAR**; k_F/k_AF are field-independent (`∂/∂E=0`). **NOT k_F/k_AF.** |

**The three senses of "longitudinal" — kept separate (this is the whole discipline of the trace):**
1. **A1 grade-scalar** — the Heaviside-excised dilatation-mass "3" (compression breather). *Where Grant's
   mechanism points.* The response does NOT live here (D2); the frame anchor DOES (D3).
2. **optic-axis orientation** — the Letter's `ε₀(S+2S'E²)` "longitudinal" eigen-permittivity (probe ∥
   pump). A **T2-photon** permittivity; the uniaxial extraordinary index. NOT the A1 grade.
3. **propagation-direction projection** — the `β·k̂` that carries the O(β) Doppler (D4). A kinematic
   fact about plane-wave boosts. NOT the A1 grade.
   Conflating any two of these is the trap; the sector verdict rests on keeping (1) apart from (2)/(3).

---

## ★ THE ONE-LINE LV-FRAMEWORK CLASSIFICATION (feeds Part 2 bounds-retrieval)

> **The AVE sidereal LV is a NONLINEAR TRANSVERSE-T2 (ε₀·S permittivity-saturation) object — driven by
> and read out in the transverse photon sector — whose preferred-frame anchor is the A1 dilatation-mass
> yield `E_YIELD ∝ mₑc²`; of dimensionless first-harmonic magnitude ~4.9×10⁻³; it does NOT correspond
> to a minimal-SME k_F or k_AF coefficient (those are LINEAR / field-independent), so existing linear
> cavity/Michelson/astrophysical-birefringence bounds do NOT constrain it — but it IS a transverse-
> sector object, so it is in-principle bounded by a dedicated NONLINEAR / higher-dimension photon-sector
> LV experiment, NOT structurally SME-invisible.**

Part-2 retrieval target (stated as physics, no external sourcing here): **nonlinear / intensity-
dependent / higher-dimension preferred-frame photon-sector LV bounds** (e.g. LV-modified nonlinear
electrodynamics; sidereal-modulated vacuum/pump-probe birefringence), NOT the minimal k_F/k_AF tables —
and whether any published bound reaches the 4.9×10⁻³ first-harmonic level.

---

## HONEST CAVEATS

1. **The flagship is NOT saved by Grant's stated mechanism.** "The LV is A1/longitudinal, so transverse
   experiments are structurally blind" is **REFUTED** — the response is a transverse-T2 permittivity
   saturation (D2), and the Letter itself already classifies the effect as a "preferred-frame
   photon-sector modification" (`main.tex:412`). What actually shields it from EXISTING bounds is that
   it is **NONLINEAR** while the bounded k_F/k_AF are **LINEAR** (D5). This is a weaker and TESTABLE
   escape: a nonlinear-sector LV experiment is not structurally impossible, so Part 2 must genuinely
   check whether such a bound exists at 4.9×10⁻³. If one does, the flagship is in trouble — say so.
2. **What IS confirmed of Grant's picture is real and load-bearing:** the LV is not intrinsic to the
   transverse photon (which is covariant/null); it exists ONLY because the substrate is A1-massive
   (`E_YIELD ∝ mₑc²` anchors the CMB rest frame, D3). So "the LV traces to the A1 compression sector"
   is TRUE **for the frame-anchor**, FALSE **for the response channel**. The split is the honest answer;
   do not let either lane collapse it.
3. **Regime discipline (why the A1 re-engagement does NOT apply here).** The canon statement "the
   longitudinal re-engages at saturation = the electron" (`master-equation.md:18`;
   `historical-precedents`) is a **FULL-saturation (A→1)** statement — the electron/condensed-phase
   regime. The birefringence is **weak-field sub-yield** (A²≈6×10⁻⁷, perturbative tail); the A1 scalar
   has NOT re-engaged. Importing the full-saturation A1 picture into the weak-field birefringence is a
   regime cross-wire; the response there is the T2 permittivity's perturbative tail.
4. **Same kernel, different sector observables.** The universal `S=√(1−A²)` drives BOTH the T2
   permittivity `ε₀·S` (birefringence readout, this result) AND the A1 observables — the Op14 local
   clock `ω_local=ω·(1−A²)^¼` (gravitational time dilation) and the compliance `C₀/S`. The birefringence
   picks off the T2 branch. A genuinely A1-sourced LV signature would live in the CLOCK / dilatation
   channel, not the birefringence — a distinct (and separately interesting) test, out of scope here.
5. **Scope: order + sector + classification, not a full cavity QFT.** The sector is fixed by which
   reactance the kernel modulates (D2) and what anchors the frame (D3); the SME class by field-
   dependence (D5). A complete LV-nonlinear-electrodynamics cavity treatment would refine the
   coefficient, not the sector or the k_F/k_AF exclusion.

---

## PROPOSED INTEGRATION NOTE (auditor/orchestrator LANDS — do NOT edit paper/canon from this lane)

Surfaced for the auditor; not landed here. Two items:

1. **Letter `main.tex:412-415`** currently reads: *"In the language of the Standard-Model Extension, the
   model belongs to the class of preferred-frame photon-sector modifications whose coefficients are
   experimentally bounded [ref]; the estimate above shows that all current photon-sector
   Lorentz-invariance bounds are satisfied…"* — the "bounded coefficients" it invokes are the **LINEAR**
   k_F/k_AF, and the estimate it uses is a **static-B** motional-E figure (A²~7×10⁻²³, O(β²)). Under the
   #579 radiation-pump result (O(β), 4.9×10⁻³) and this sector-trace, the accurate statement is:
   *the model is a NONLINEAR (field-amplitude-keyed) transverse photon-sector preferred-frame effect;
   existing LINEAR k_F/k_AF bounds do not apply; the relevant comparison is a nonlinear/higher-dimension
   photon-sector bound (Part 2).* Flag the LINEAR-bound sentence for re-scoping; do not delete the
   photon-sector classification (it is CORRECT — the effect IS transverse-sector, just nonlinear).
2. **Sector labelling guard.** Anywhere the corpus reads the LV as "longitudinal/A1-sourced" (to argue
   transverse-experiment blindness), correct to: *transverse-T2 response, A1-anchored frame; blindness
   to existing bounds is LINEAR-vs-NONLINEAR, not sector.* Prevents a two-"3"s double-count entering the
   flagship narrative.

---

## PROVENANCE OF NUMBERS

β = v_CMB/c = 370×10³ / 299792458 = 1.234187×10⁻³ (c from `ave.core.constants.C_0`, CODATA-exact;
v_CMB an EXTERNAL astrophysical input). 4β = 4.937×10⁻³; 2β = 2.468×10⁻³ (upstream #579).
`E_YIELD`, `V_SNAP`, `M_E`, `ALPHA`, `L_NODE`, `E_CRIT` from `ave.core.constants`. The
`E_YIELD = √α·E_CRIT = √α·mₑc²/(e·ℓ_node)` chain and `V_SNAP = mₑc²/e` are asserted in
`verify_constants()`. All discriminator outputs reproduced by the driver and pinned in the tests.
