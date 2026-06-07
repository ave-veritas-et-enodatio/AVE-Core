# 2nd-shell I4₁32 screw holonomy — is the SU(2) half-twist PATH-INDEPENDENT (intrinsic spin-½) or PATH-DEPENDENT (projected helicity)?

**Status:** RESULT (standalone geometric diagnostic; no genesis sim, no engine import beyond the canonical port-vector geometry). **Date:** 2026-06-07.
**Branch:** `analysis/2026-06-07-2ndshell-screw-holonomy` (off `main` @ `dbb60320`).
**Prereg:** [`2026-06-07_2ndshell-screw-holonomy-prereg.md`](2026-06-07_2ndshell-screw-holonomy-prereg.md) (frozen before running).
**Driver:** [`src/scripts/vol_1_foundations/secondshell_screw_holonomy.py`](../src/scripts/vol_1_foundations/secondshell_screw_holonomy.py).
**Viz:** `src/scripts/vol_1_foundations/_output/secondshell_screw_holonomy.png` (extends prior viz #6).
**Decisive follow-up to:** [`2026-06-07_chiral-orbital-holonomy-result.md`](2026-06-07_chiral-orbital-holonomy-result.md) (verdict II, reflection-EVEN proxy).

> **VERDICT: (II) — PATH-DEPENDENT. This is PROJECTED HELICITY, NOT intrinsic spin-½.** On the genuine reflection-ODD 2nd-shell A/B 4₁ screw (not a knob), a clean SU(2) `−I` (exactly π, `n_steps`-robust, 4π→+I double-cover consistent) is realizable and **requires the chirality** (achiral control = 0/400), **but only for f ≈ 18% of orbits** — and even that fraction is a **commensurate-pitch RESONANCE** (0% outside κ ≈ [½π, 7⁄12 π]), not a topological Z₂ plateau. The π is encircling-conditional AND pitch-conditional → the generic Berry-phase-by-encircling, **more** conditional than the prior reflection-even proxy, not less. Intrinsic, frame-independent spin-½ does **NOT** emerge from orbiting the host in the screw crystal.

---

## §1 What changed from the prior test (both corrections landed)

The prior diagnostic found π chirality-required (0/400 achiral) but path-dependent (127/400), and named the cause: it used a **reflection-even** scalar anisotropy `w_j = 1+ε·s_j` on a single **achiral** host tetrahedron. This test makes both corrections its §7 demanded:

1. **TRUE reflection-ODD chirality.** The `ε`-knob is **gone** (equal Wahba weights). The chirality is now the genuine **2nd-shell A/B 4₁ screw** of I4₁32 (Axiom 1, [`CLAUDE.md` INVARIANT-S2](../manuscript/ave-kb/CLAUDE.md)): each canonical neighbour carries a Cosserat micro-rotation frame `R_screw(x) = Rot(â, κ·(x·â))` — a 4₁ screw (κ>0 native; κ<0 mirror 4₃; κ=0 achiral). Provably reflection-odd: a mirror sends κ→−κ (the 4₃ enantiomorph), not rotation-equivalent — the property the ε-proxy lacked.
2. **Score PATH-INDEPENDENCE.** The discriminator is **f = fraction of orbits returning `−I`** over the 400-orbit plane×radius battery.

**Geometry is canonical, not invented** (ave-canonical-source): host A at origin; 1st shell = 4 B at the port vectors `p_j` ([`k4_tlm.py:111-114`](../src/ave/core/k4_tlm.py)); 2nd shell = 12 A at the canonical two-hop A→B→A `{p_j − p_k}` = perms of (0,±2,±2) ([`k4_tlm.py:115`](../src/ave/core/k4_tlm.py) "B joins A via exact negative vectors"). **Transport is reused verbatim** from the prior driver (`rotation_to_quaternion`, `orbit_plane_basis`, `solid_angle`, the Wahba SVD, continuous SU(2) lift, smooth-transport guard, double-cover check).

## §2 Primary result — the fraction f (the discriminator)

| Run (400 orbits, uniform plane × radius) | f(−I) | smooth | 4π→+I |
|---|---|---|---|
| achiral, 1st-shell only (**= prior ε=0 baseline**) | **0/400 = 0.0%** | 0.0% | ✓ |
| achiral, 1st+2nd shell (**matched control, CP8**) | **0/400 = 0.0%** | 0.0% | ✓ |
| **NATIVE screw 4₁ (κ = +π/2)** | **72/400 = 18.0%** | 11.5% | ✓ |
| MIRROR screw 4₃ (κ = −π/2) | 64/400 = 16.0% | 8.0% | ✓ |

**f_native ≈ 18% — PARTIAL, not ~100%.** The achiral controls both give exactly 0/400: the 1st-only run reproduces the prior achiral baseline (construction validated), and the 1st+2nd achiral run shows the 2nd-shell *geometry alone does nothing* — **the chirality is necessary** (the CP8 matched-baseline falsifier is ruled out: it is the screw, not the added constraints, that produces any `−I`).

**The value, when it appears, is exactly π:** clean `−I` (n_steps-robust, see §3) with `q(4π)=+q(0)` everywhere — a genuine spin-½ double-cover. It is the **fraction** that is partial.

## §3 The decisive datum — the π is a commensurate-pitch RESONANCE, not a topological Z₂

A genuine topological Z₂ holonomy must depend only on **sign κ**, not magnitude: f should be a step-function plateau (0 at κ=0, then constant for all κ>0). It is not.

| κ (rad/step) | 0 | π/4 | 3π/8 | **π/2** | **7π/12** | 2π/3 | 3π/4 | π |
|---|---|---|---|---|---|---|---|---|
| f(−I) | 0% | 0% | 0% | **18.5%** | **25.0%** | 0% | 0% | 0% |

**f is nonzero ONLY in a narrow window around the commensurate 4₁ angle κ ≈ [½π, 7⁄12 π], and 0% everywhere else.** This is a **resonance**, not a topological invariant. Robustness:

- **n_steps-robust** (THE topological check): at κ=π/2, f = 18.5% stable across n_steps = 256→2048. The *smooth* fraction grows toward the total (6.5%→15.5%) as resolution rises — so the `−I` orbits are genuine smooth-transport holonomies converging cleanly, not discretization noise. The effect is **real but conditional**, not an artifact.
- **seed-robust:** f = 18.0 / 17.5 / 16.0 / 21.0% across seeds 1/2/3/7.
- **axis-quasi-independent** *within the window*: f ≈ 14.2 / 13.3 / 12.5% for screw ∥ x̂ / ŷ / ẑ (the three cubic ⟨100⟩ 4₁ axes) — consistent, as a crystal-chirality observable should be.

So even the `−I` that does appear is **doubly conditional**: it needs (a) the orbit to encircle an orientation-degeneracy AND (b) the screw pitch to sit in the commensurate window. The prior reflection-even proxy's `−I` was encircling-conditional only; the true reflection-odd screw's is encircling- **and** pitch-conditional — **more** fragile, not less.

## §4 Path-dependence map

Structured orbit-plane grid (polar θ × azimuth ψ) at r=1, native screw: **f(−I) = 22.8%, both signs present, interface at a near-degeneracy** (min Wahba gap = 0.003). The `−I` set forms **bands gated by a degeneracy locus** (viz Panel B), exactly the Berry-phase-by-encircling signature — **not** the whole-sweep `−I` that path-independence (verdict I) requires. The screw **relocated** the orientation-degeneracy (and gated its existence on pitch); it did not remove the encircling-conditionality.

## §5 Verdict + classification

**Verdict (II): PROJECTED HELICITY, not intrinsic spin-½.** The genuine 2nd-shell I4₁32 screw can host a clean chirality-required π half-twist, but path-**dependently** (encircling- and pitch-conditional, f≈18%). This is the generic Berry-phase-by-encircling / Dirac-monopole mechanism — the **same class** as the prior reflection-even proxy, now instantiated on the true screw. It is **not** the path-independent "every orbit returns π / 720° to close" invariant that verdict (I) and intrinsic, frame-independent spin-½ (the U(1)-fibre γ⁵ phase, [`finkelstein-misner-spin-half-derivation.md:141`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md)) require.

**`consistency-vs-emergence`: framed as EMERGENCE, lands CONSISTENCY-class.** Inputs are pure SO(3)/SU(2) geometry from canonical lattice positions — no CODATA, no `ave.core.constants`, no spin-½ input; the observable is the Z₂ sign and the fraction f. Had f≈100% (path-independent), this would have been genuine **emergence** (Class-D-like: a topological observable from geometric primitives). It is f≈18% pitch-resonant → the geometry is **consistent** with hosting a chirality-required π, but intrinsic spin-½ does not inevitably/robustly emerge from orbiting. The honest headline is the weak one: *"the true chiral screw can host an encircling-conditional, pitch-resonant π half-twist"* — **not** *"crystal chirality delivers intrinsic spin-½ locally."*

**Why (Rule 11 honest closure — single mechanism explains all of it):** orbital-encircling of a host node is **not** the Finkelstein-Misner mechanism. A screw axis is a **translational** symmetry (frame rotation ∝ displacement *along* the axis), not a rotational **disclination** *around* the host — so a single-host orbit does not see a robust Z₂. The canonical intrinsic spin-½ comes from rotating the **extended `0₁` unknot relative to the crystal** ([`finkelstein-misner §2.2`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md)), not from orbiting a host in the perfect lattice. This is consistent with — and sharpens — [`k4-rotation-group.md:123`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) ("A↔B swap needs reflections or some other physical mechanism"): orbital encircling of the 2nd-shell screw is a *candidate* "other mechanism" that **can** produce `−I`, but only conditionally, so it does **not** convert the open caveat into a clean unconditional derivation. **The caveat stands; the FM extended-defect derivation remains the load-bearing spin-½ route.** This matches the prereg's primary prediction (II).

## §6 Coordinate discipline (`phase-space-coordinate-check`)

This is a **real-space** SO(3)→SU(2) holonomy — the coordinate system the FM kink lives in ([`finkelstein-misner §9`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md): "this derivation lives in real-space coordinates"). It is **kept distinct** from the canonical `(2,3)` winding, which is **phase-space** (Clifford torus in `(V_inc, V_ref)`). No real-space result here is compared to the phase-space `(2,3)`; this test neither supports nor contradicts that phase-space claim.

## §7 Answers to the four return questions

1. **Fraction on the TRUE 2nd-shell screw:** **f ≈ 18% (72/400)** — PARTIAL, path-dependent, and itself a commensurate-pitch resonance (0% outside κ≈[½π,7⁄12π]). **NOT ~100%.** → **(II), not (I).**
2. **Verdict + class + intrinsic-or-projected:** **(II), consistency-class. This is PROJECTED HELICITY (encircling-conditional, like S·p̂), NOT the intrinsic, frame/path-independent spin-½ (γ⁵).** Real but not intrinsic.
3. **Is g=2 now computable on this geometry?** **No — g=2 is NOT unblocked by this test.** g=2 unblock was contingent on verdict (I) (the same π double-cover → μ_s = 2μ_B·½ = μ_B). Since this is (II) (projected, not intrinsic), the orbital-holonomy geometry does not supply the intrinsic spin needed for a g=2 derivation. g=2 needs a **separate run** on the FM **extended-`0₁`-unknot** mechanism (rotating the unknot relative to the crystal + its B-core moment), which is the canonical spin-½ route and the explicitly-open work of [`finkelstein-misner §8`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) — not this orbital diagnostic.
4. **Canonical contradiction + does the screw sign bear on e⁻ RH-vs-LH (FLAG 1)?** See §8.

## §8 Canonical flags (flag-don't-fix)

- **FLAG A — bare K4 positions are achiral; the I4₁32 chirality is necessarily a Cosserat-frame decoration.** The canonical `k4_tlm.py` lattice (A=even, B=odd, B=A+(1,1,1), degree-4 tetrahedral) is, **as bare positions**, the achiral diamond embedding (inversion-symmetric): the 1st shell is a regular tetrahedron ([`k4-rotation-group.md:37`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md)) and the 2nd shell is an O_h cuboctahedron (this test's achiral 1st+2nd control = 0/400 confirms it). The I4₁32 reflection-odd chirality (Axiom 1) therefore lives in the **Cosserat micro-rotation decoration** (the screw frame field), exactly as INVARIANT-S2 says ("micropolar nodes … Cosserat rotational DOF … I4₁32"), and is what this test modelled. **Sub-flag (naming):** "K4" in the engine is the **degree-4** tetrahedral (diamond-class) net, whereas the canonical-Laves "K4 crystal" (Sunada srs / (10,3)-a net) is **degree-3** and genuinely chiral as bare positions. Whether the degree-4 diamond embedding + Cosserat-screw decoration is geometrically equivalent to the degree-3 chiral Laves net is an **open canonical-geometry question**, surfaced here, not resolved.
- **FLAG B — the prior merged driver does not reproduce its own "127/400".** The merged `chiral_orbital_holonomy.py` (PR #110) JSON carries only structured sweeps totalling `n_minus_I_total = 33`; it contains **no 400-orbit random battery**. The prior result doc's headline "127/400 (32%)" came from a random-battery scan not kept in the merged driver. This test therefore reconstructs an equivalent seeded battery from scratch (and the achiral 1st-only reproduction = 0/400 matches the prior's reported 0/400 achiral, anchoring the comparison).
- **FLAG 1 — screw sign vs e⁻ RH-vs-LH.** The screw handedness (κ>0 native 4₁ tied to the engine's port handedness {0,2}=RH, vs κ<0 mirror 4₃) **does** select the Berry handedness of the `−I` orbits (native and mirror are distinct configs with comparable f = 18%/16%, as mirror symmetry of a chiral magnitude requires). **But** because the `−I` is **path-dependent (projected)**, the handedness it picks is the sign of a **projected helicity**, not of an intrinsic electron chirality. **On this test's evidence the screw sign does NOT fix the intrinsic e⁻ RH-vs-LH** — that question is properly settled on the FM extended-defect (the ±½ twist orientation of the unknot, [`finkelstein-misner:81`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md)), not on orbital encircling. (Battery-averaged Berry solid-angle of the `−I` set ≈ −0.005π native / −0.008π mirror — both ~0, washed out by the isotropic orbit-normal distribution; the per-orbit handedness flips by construction, but the battery mean is not a clean discriminator.)

## §9 Files

- Driver: [`src/scripts/vol_1_foundations/secondshell_screw_holonomy.py`](../src/scripts/vol_1_foundations/secondshell_screw_holonomy.py)
- Prereg: [`research/2026-06-07_2ndshell-screw-holonomy-prereg.md`](2026-06-07_2ndshell-screw-holonomy-prereg.md)
- Numbers: `src/scripts/vol_1_foundations/_output/secondshell_screw_holonomy.json`
- Viz: `src/scripts/vol_1_foundations/_output/secondshell_screw_holonomy.png`
- Canonical sources cited: [`k4_tlm.py:111-115,215-216,542`](../src/ave/core/k4_tlm.py); [`k4-rotation-group.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) §1/§5/§6; [`finkelstein-misner-spin-half-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) §2/§8/§9; [`water-anomaly-lc-partition.md:44`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md) (Ω_freeze); [`CLAUDE.md` INVARIANT-S2](../manuscript/ave-kb/CLAUDE.md) (I4₁32).
