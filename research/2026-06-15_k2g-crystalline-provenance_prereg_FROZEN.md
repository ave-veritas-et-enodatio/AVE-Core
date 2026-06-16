# PREREG (FROZEN, Rule-11) — K=2G crystalline provenance

**Frozen:** 2026-06-15. No post-hoc edits to §Prediction / §Discriminating outcomes / §Falsifier
after the driver runs (Rule-11). Amendments only as dated Rule-12 headers below the freeze line.

**Target (Step 1, precise).** Compute the elastic moduli (bulk K, shear G) of the **crystalline
z=4 K4 / diamond lattice** via lattice dynamics (Born–Huang / Keating model: bond-stretch stiffness
`k_a`, bond-bend stiffness `k_s`; with the diamond two-atom basis → internal-strain relaxation).
Determine whether **K=2G (ν_vac=2/7)** emerges as a **geometric inevitability** of the crystal, or
only at a **non-geometrically-forced operating point** in the stiffness ratio `k_a/k_s`.

## Physical picture (Step 1.5 — mechanical, no equations)

- The vacuum is a **z=4 K4 (diamond-topology) Cosserat crystal**: each node has 4 neighbours,
  6 DOF (3 translation, 3 microrotation). Bonds resist **stretch** (axial, `k_a`) and **bend**
  (angular/shear, `k_s`).
- **z=4 is sub-isostatic.** Maxwell rigidity needs z ≥ 2d = 6 in 3D for a central-force network.
  z=4 < 6 → a stretch-only K4 lattice is **floppy in shear** (zero-energy shear modes). Rigidity in
  shear comes **entirely from bond-bending** `k_s`. So G is a `k_s` object; K is a `k_a` object.
- Therefore **K/G is set by the ratio `k_a/k_s`** — a constitutive (material) ratio of the LC tank,
  not a pure number forced by the K4 connectivity. The geometry fixes the *form* K/G = f(k_a/k_s),
  not the *value*.
- "K=2G" is the GR **trace-reversal** condition (TT graviton: pure deviatoric, traceless wave). It
  selects one point on the f(k_a/k_s) curve. The question is whether the K4 substrate **independently
  lands on that point**, or whether it is **tuned/matched** to it.
- Discrete onset vs smooth curve: there is no knee — K/G(k_a/k_s) is smooth and monotonic. K=2G is a
  single interior point, not a bifurcation the dynamics falls into.

## Corpus state

**OPEN with a known-failed crystalline attempt + a strong "imported" prior.** No forward crystalline
derivation of K=2G exists in any of 9 AVE repos (cross-repo grep 2026-06-15). The one K4 lattice-
dynamics computation (`research/_archive/L3_electron_soliton/127_…:273-300` + `q_g47_path_b_*.py`)
**imposes** K=2G and back-solves the bond ratio. The 2026-06-14 magic-angle audit already grades
**K=2G IMPORTED** (`…provenance-bh-forward-test-audit.md:18`, on main). Q-G41 ("K=2G from K4 topology
as topological inevitability") is an unstarted roadmap row (`closure-roadmap.md:829`).

Prior work cited: `trace-reversal-mechanism.md:20`, `q-g47-substrate-scale-cosserat-closure.md:28,58`,
`vacuum-poisson-ratio.md`, `backmatter/01_appendices.tex:131,186`, `…127_…:273-300`,
`q_g47_path_b_k4_eigenmode.py`, `2026-06-14_magic-angle-provenance-bh-forward-test-audit.md`.

## Dimensional analysis (Step 3.5)

The target is a **dimensionless ratio** K/G (and ν), so there is nothing to evaluate at canonical
SI primitives — K, G, k_a, k_s all carry the same units and the moduli are homogeneous degree-1 in
the spring constants. The only dimensionless control parameter is **ρ ≡ k_a/k_s**. Power-counting:
- Stretch-dominated bulk: K ∝ k_a (leading), weak/zero k_s contribution.
- Bend-set shear: G ∝ k_s with a stretch-coupling correction that **vanishes as k_s→0** (floppy).
- ⟹ K/G ∝ ρ at large ρ; K/G → O(1) finite as ρ→0. K=2G sits at one finite ρ*.
- Isotropy caveat: cubic K4 has **two** shear moduli (C44 and (C11−C12)/2); "a single G" requires
  either elastic isotropy (Zener A=1) or a Voigt/Reuss/Hill average — itself a *choice*, a second
  reason K=2G is not a bare geometric output.

## My prediction

**K=2G is NOT a geometric inevitability of the z=4 K4 crystal.** The lattice-dynamics computation
will yield **K/G = f(k_a/k_s), a smooth one-parameter family**, with:
1. The **central-force-only limit** (k_s→0): relaxed G→0 (sub-isostatic floppy shear) → K/G→∞ →
   confirms z=4 needs bond-bending; G is a bond-bending object.
2. A **generic affine/Cauchy point** near **K=5/3 G (ν=1/4)** (the Cauchy-relation value for
   central-force solids at inversion centres — the corpus's own `01_appendices.tex:186` default),
   NOT K=2G.
3. The real z=4 reference crystal (carbon diamond constitutive ratios) gives **K/G≈0.8, ν≈0.07** —
   bending-dominated, K<G, **far from** K=2G (ν=0.286).
4. K=2G is reached only at a specific **ρ* = (k_a/k_s)\***, which the K4 geometry does **not** fix;
   whatever fixes ρ* is constitutive (LC-tank) content **or** a match to GR's trace-reversal.
5. Chirality / Cosserat couple-stress does **not** move the K/G ratio (corpus: λ_G=4/21
   chirality-blind to 14 dp) — so the "emergent from Chiral LC coupling" claim
   (`01_appendices.tex:131`) will **not** rescue a geometric K=2G.

**Why:** sub-isostatic z=4 ⟹ shear rigidity is purely bond-bending ⟹ K/G is a stiffness-ratio knob,
not a topological invariant. This is the same structure the corpus already exposes
(`K_0=4k_a+8k_s`, `G_0=8k_s` ⟹ K=2G ⟺ k_a=2k_s, taken "as given").

## Discriminating outcomes

- **Outcome A (most likely → fork b/c).** K/G is a one-parameter family; K=2G requires a specific,
  non-geometrically-forced ρ*. The crystal does NOT inevitably give K=2G. ⟹ K=2G is **GR-imported**
  (matched to trace-reversal) with the amorphous FTG-EMT as a separate consistency illustration.
  **Corroborates** the 2026-06-14 audit's "IMPORTED" grade with an independent forward computation,
  and **closes** the vol0-hold-items O3 / Q-G41 gap with a NEGATIVE (crystal does not force it).

- **Outcome B (would flip to fork a).** The K4 lattice-dynamics yields K=2G **independent of the
  stiffness ratio** — i.e. some K4 symmetry/Cosserat constraint forces ρ*=2 (or makes K/G a pure
  geometric number = 2). This would make ν=2/7 a topological inevitability (chord). **Prediction: this
  will NOT happen** (z=4 sub-isostatic forbids a ratio-independent K/G).

- **Outcome C (null/ambiguous).** The "single G" is ill-defined (strong cubic anisotropy A≠1) so
  "K=2G" has no unique crystalline meaning without an averaging choice → reinforces "not a bare
  geometric output," routes to fork (b)/(c) via a different door.

## Falsifier (what would mean MY framing is wrong)

If the relaxed K4 elastic moduli give **K/G = 2 as a pure number independent of k_a/k_s** (or a K4
symmetry identity forces k_a/k_s to exactly the K=2G value with no free constitutive input), then
K=2G **is** crystalline-geometric and my "sub-isostatic ⟹ free ratio" framing is falsified → fork (a).
Equivalently: if the central-force-only z=4 lattice is NOT floppy in shear (relaxed G≠0 at k_s=0),
my sub-isostatic premise is wrong.

---

*Rule-12 amendments (post-freeze, dated) below this line:*
</content>
