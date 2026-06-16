# RESULT — K=2G crystalline provenance: the z=4 K4 crystal does NOT force K=2G

**Date:** 2026-06-15. **Branch:** `analysis/2026-06-15-k2g-crystalline-provenance`.
**Prereg:** [`2026-06-15_k2g-crystalline-provenance_prereg_FROZEN.md`](2026-06-15_k2g-crystalline-provenance_prereg_FROZEN.md) (Rule-11).
**Driver:** [`src/scripts/verify/k2g_crystalline_provenance.py`](../src/scripts/verify/k2g_crystalline_provenance.py).
**Outcome:** **A** (predicted) — K=2G is NOT a crystalline geometric inevitability.

> **FLAG-DON'T-FIX → Grant.** The provenance verdict (crystalline-forced / GR-imported /
> amorphous-only) is **your call**. This lane brings the moduli computation; it does **not** edit
> any canonical gravity-sector claim. The computation **corroborates** the 2026-06-14 magic-angle
> audit's standing "K=2G **IMPORTED**" grade with an independent forward lattice-dynamics derivation,
> and **closes the vol0-hold-items O3 / Q-G41 gap with a NEGATIVE**: the crystal does not select K=2G.

---

## 1. What was computed

Standard **diamond Keating lattice dynamics** (the canonical z=4-tetrahedral elastic model; the
corpus's own `q_g47_path_b` calls its unit cell "Born-Huang K4"). Two force constants: bond-stretch
`k_a`, bond-bend `k_s`. Diamond's two-atom basis carries an **internal-strain (Kleinman) relaxation**
of C44 (optic modes displace under macroscopic shear). All outputs are **ratios** (K/G, ν) — the
common Keating prefactor cancels, so the result is dimensionless and needs no SI constants.

**Model validated against carbon diamond** (the z=4 reference crystal) before any provenance claim:
inferred (k_a, k_s) from measured C11, C12 → **predicted relaxed C44 = 575.9 GPa vs measured 578.0
(−0.36%)**. The model is correct.

## 2. The five results (all predicted by the frozen prereg)

| # | Result | Value |
|---|---|---|
| 1 | **z=4 is sub-isostatic.** Central-force only (k_s→0): all shear moduli → 0; bulk K stays finite. | G→0, K→k_a |
| 2 | **G is a bond-bending object; K/G is a one-parameter family** in ρ≡k_a/k_s. | K/G(ρ) smooth, monotone |
| 3 | **Real z=4 diamond gives ν≈0.067, K/G≈0.82** (K<G, bending-dominated). | **far from** ν=2/7=0.286 |
| 4 | **K=2G needs a tuned ρ\* that is averaging-dependent and not geometrically forced.** | ρ\* ∈ {3.67, 5.30, 6.62} |
| 5 | **ν=2/7 ⟺ K=2G is exact** — but the *consequent* of K=2G, not a derivation of it. | the one firm link |

**Elastic constants (Keating, prefactor=1):** C11=k_a+3k_s, C12=k_a−k_s, C44(clamped)=k_a+k_s,
**C44(relaxed)=4k_a·k_s/(k_a+k_s)**, K=k_a+k_s/3, C′=(C11−C12)/2=2k_s, G_Voigt=4k_s(4k_a+k_s)/(5(k_a+k_s)).

**The one-parameter family** (Voigt G):

| ρ=k_a/k_s | 0.5 | 1.0 | **1.52** | 2.0 | 3.0 | **5.30** | 7.0 | 10.0 |
|---|---|---|---|---|---|---|---|---|
| K/G | 0.52 | 0.67 | **0.82** | 0.97 | 1.28 | **2.00** | 2.53 | 3.47 |
| ν | −0.085 | 0.000 | **0.068** ◄diamond | 0.117 | 0.190 | **0.286** ◄K=2G | 0.325 | 0.368 |

## 3. Why this settles the fork

The physics is the **Maxwell isostatic count**: in 3D a central-force network needs coordination
z ≥ 2d = 6 to be rigid. **z=4 < 6 → the K4 lattice is floppy in shear with stretching alone.** Shear
rigidity comes *entirely* from bond-bending k_s; bulk rigidity from stretch k_a. Therefore **K/G is a
ratio of two independent constitutive stiffnesses**, not a number the K4 connectivity can fix. The K4
geometry fixes the *form* K/G = f(k_a/k_s); it cannot fix the *value*. To land on K=2G you must
supply ρ\* from outside the geometry — and even "which K=2G" is ambiguous because cubic K4 is
anisotropic (Zener A=1.21≠1), so "a single G" is itself an averaging choice (C44 / C′ / Voigt give
ρ\* = {0.05, 6.62} / 3.67 / 5.30 — they **disagree**, and the C44 branch isn't even single-valued).

This is the **same structure the corpus already exposes** but never closed: `K_0=4k_a+8k_s`,
`G_0=8k_s` ⟹ K=2G ⟺ k_a=2k_s — taken "as given" (`clm-bjceop:1073`). My standard-Keating
normalization differs in prefactors from the corpus's K4-specific one (K=k_a+k_s/3 vs 4k_a/9;
C44_rel=4k_ak_s/(k_a+k_s) vs 2k_ak_s/(k_a+2k_s)), but the **load-bearing structure is identical and
normalization-independent**, and mine is the version validated against a real z=4 crystal (<0.5%).
It also resolves the corpus's flagged **7-vs-2 ratio inconsistency**: that split is the
relaxed-vs-clamped (internal-strain) ambiguity — a *modelling* choice, confirming the operating point
is not geometrically pinned.

## 4. Mapping to the three-way fork

- **(a) crystalline-forced — REFUTED.** The crystal yields a one-parameter family, not K=2G. The
  prereg's flip-falsifier (K/G=2 as a ratio-independent pure number, or a symmetry forcing k_a/k_s)
  **did not occur**. Outcome B did not land.
- **(b) GR-imported — SUPPORTED.** K=2G is the GR trace-reversal condition
  (`q-g47-substrate-scale-cosserat-closure.md:28`, verbatim "required by General Relativity"); the
  substrate's ρ\* is tuned to it. Independent corroboration of the 2026-06-14 audit's "IMPORTED" grade.
- **(c) amorphous-only — STANDS as a consistency illustration.** The FTG-EMT K/G=2 crossing at
  p*=8πα lives on the *amorphous* z₀≈51.25 network and is α-circular by the corpus's own admission
  (`trace-reversal-mechanism.md:22`). It does not transfer to the crystalline z=4 structure.

**The firm residue (unchanged):** *given* K=2G, ν_vac=2/7 is exact, and everything downstream of ν=2/7
(sin²θ_W=2/9, the 2/7-compactness BH forward test) rides on that one firm link — which the audit already
isolated as the chord candidate. This lane does not touch it.

## 5. Honest scope / limits

- The driver is the **harmonic Keating** model. It does not include the LC-tank constitutive content
  that *sets* k_a/k_s in the AVE substrate — but that is the point: **whatever sets ρ is constitutive
  (or a GR match), not geometric.** If a future derivation shows the AVE LC/Cosserat constitutive
  relations independently force ρ=ρ\*(K=2G), that would lift (a) — this lane shows the *geometry alone*
  does not, and there is no such constitutive derivation in the corpus (the only attempt, u₀\*≈0.187,
  was retracted 2026-06-14 as back-fit).
- Chirality: not in this harmonic model, but the corpus's own λ_G=4/21 is chirality-blind to 14 dp,
  so the "K=2G emergent from Chiral LC coupling" claim (`01_appendices.tex:131`) does not rescue a
  geometric K=2G — the chiral sector doesn't move the K/G ratio.

## 6. Recommended adjudication (Grant's call)

The corpus is **already honest** about this post-2026-06-14 (K=2G graded IMPORTED on main). This lane
adds the missing *forward* computation that the audit, vol0-hold-items O3, and Q-G41 all flagged as
open. Recommended dispositions for Grant to choose among:
1. **Ratify (b) + log Q-G41 closed-NEGATIVE** ("K=2G is not a K4 topological inevitability; it is the
   GR trace-reversal operating point, constitutively/GR-set not geometrically forced") — and cite this
   driver as the forward evidence. *(Recommended — matches the standing audit.)*
2. **Keep Q-G41 open** pending a constitutive (LC/Cosserat) derivation of ρ\*, treating this as
   "geometry-alone insufficient, constitutive route untested."
3. Leave the gravity sector untouched (it already reads K=2G as IMPORTED); land only this result doc +
   driver as the corroborating computation.
</content>
