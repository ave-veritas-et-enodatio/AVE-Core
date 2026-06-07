# Prereg: 2nd-shell I4₁32 screw holonomy — does the TRUE crystal chirality make spin-½ intrinsic (path-independent π) or projected (path-dependent π)?

**Status:** FROZEN PREREG (predictions registered before running). 2026-06-07.
**Branch:** `analysis/2026-06-07-2ndshell-screw-holonomy` (off `main` @ `dbb60320`, which carries the merged prior result via PR #110).
**Driver (to be written):** `src/scripts/vol_1_foundations/secondshell_screw_holonomy.py`.
**Decisive follow-up to:** [`research/2026-06-07_chiral-orbital-holonomy-result.md`](2026-06-07_chiral-orbital-holonomy-result.md) (verdict II — π chirality-required but path-dependent, 127/400).

---

## §0 Why this test (the two corrections the prior test needs)

The prior chiral-orbital-holonomy diagnostic found a clean SU(2) `−I` (exact π) that was **necessary on chirality** (0/400 achiral) but **path-dependent** (127/400, encircling-conditional). Its own §7 named the load-bearing limitation:

> "The chirality injected here (`w_j = 1+ε·s_j`) is a **reflection-even scalar anisotropy** along ŷ, NOT a manifestly reflection-odd I4₁32 handedness. The *true* crystal chirality … lives in the **second shell** — the screw relation between the A- and B-sublattice tetrahedra … **That is the next test**."

Two corrections, both load-bearing:

1. **TRUE chirality (reflection-ODD), not a reflection-even knob.** The 1st-shell tetrahedron `{p₀…p₃}` is geometrically **achiral** ([`k4-rotation-group.md:37`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md): "Regular tetrahedron inscribed in cube"). The real reflection-odd `I4₁32` handedness (Axiom 1, [`CLAUDE.md` INVARIANT-S2](../manuscript/ave-kb/CLAUDE.md): "3D chiral Laves K4 Cosserat crystal … I4₁32 chiral space group") lives in the **2nd-shell A/B-sublattice screw**. Drop the `ε`-anisotropy knob; decorate the neighbours with the genuine 4₁ screw frame field.

2. **Score PATH-INDEPENDENCE, not just "is it π."** Per the intrinsic-vs-projected distinction: helicity `S·p̂` is path-dependent by nature; intrinsic `γ⁵` spin-½ (the U(1) fibre phase of SU(2) per [`finkelstein-misner-spin-half-derivation.md:141`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md)) is frame/path-INDEPENDENT. The **discriminator is the FRACTION of orbits returning `−I`**.

## §1 Claim under test

The 2nd-shell I4₁32 screw IS the local projection of `Ω_freeze` (cosmic K4 crystallization into the I4₁32 chiral ground state, [`water-anomaly-lc-partition.md:44`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md)). **Grant's hypothesis:** the cosmically-sourced handedness makes a single electron's spin **intrinsic/robust** — every orbit returns `−I` (path-independent π) → spin-½ is the bulk chirality delivered locally → VERDICT (I), emergence-class. **Alternative:** the screw, like the prior anisotropy, only conditions where Berry degeneracies sit → partial `−I` fraction → projected helicity → VERDICT (II).

## §2 Corpus state (ave-prereg corpus survey)

- **Closed / canonical (cite, don't re-derive):**
  - Canonical spin-½ mechanism = Finkelstein–Misner kink on the **extended** `0₁` unknot ([`finkelstein-misner-spin-half-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md), clm-salw2h). §8: "**Does NOT** provide a discrete-lattice computation of the FM kink on K4 … flagged as open work." §9: the FM kink lives in **real-space**; the (2,3) winding lives in **phase-space** — different coordinate systems.
  - `K4 → A4 → 2T ⊂ SU(2)` chain; 2π → `−I`, 4π → `+I` ([`k4-rotation-group.md` §6](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md), clm-rkisb8).
  - Pure rotations (T = A₄) preserve A/B separately; A↔B swap "needs reflections (full T_d) **or some other physical mechanism**" ([`k4-rotation-group.md:123`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md), clm-7pvh9i). Orbital encircling of the **2nd-shell screw** is the candidate "other mechanism."
- **Canonical geometry (ave-canonical-source — mirror, don't invent):** port vectors `p₀=(+1,+1,+1) p₁=(+1,−1,−1) p₂=(−1,+1,−1) p₃=(−1,−1,+1)` ([`k4_tlm.py:111-114`](../src/ave/core/k4_tlm.py)); sublattices A = all-even, B = all-odd, B = A+(1,1,1) ([`k4_tlm.py:215-216`](../src/ave/core/k4_tlm.py)); port handedness {0,2} RH, {1,3} LH, B-sites helicity-inverted ([`k4_tlm.py:542-547`](../src/ave/core/k4_tlm.py)).
- **Open (this test):** the discrete-lattice / orbital-encircling question on the *genuine* 2nd-shell screw (verdict I vs II for the chirality claim). Prior test = green-field machinery now merged (PR #110); **reuse its transport, extend the geometry**.

## §3 Substrate-native-check walk (fired before scaffolding)

| CP | Resolution |
|---|---|
| 1 dynamics | **Holonomy / parallel transport** in SO(3)→SU(2). NOT energy-min / gradient-descent / Hessian. The Cosserat frame field (Axiom 1 micro-rotation) is parallel-transported around an orbit. |
| 2 sector | **Cos-sector, real-space** — the SO(3) orientation/micro-rotation field. Chirality = the I4₁32 screw decoration. NOT V-sector phase-space. |
| 3 objective | AVE-native = **Z₂ holonomy of π₁(SO(3))**. "Preferred orientation" = Wahba/Kabsch alignment to neighbour directions (geometry, no free parameter, no energy functional). |
| 4 coordinates | **REAL-SPACE** holonomy (FM kink is real-space, `finkelstein-misner §9`). The (2,3) winding is **phase-space** (Clifford torus) — KEPT DISTINCT (phase-space-coordinate-check). This test does **not** compare its real-space holonomy to the phase-space (2,3). |
| 5 local clock | N/A — pure geometry, no Op14 saturation / field amplitude. |
| 6 reactance pair | N/A — not a time-domain LC run. |
| 7 sampling | N/A — no field-density / PML extraction; construction from canonical lattice **positions** only. |
| 8 emergence | This IS an emergence test. **Generative precursor** = the bare chiral neighbourhood (screw-decorated 2nd shell) + orbiting loop; NOT a planted finished spin-½ defect tested for persistence. **Matched control** = the *achiral* (screw κ=0) neighbourhood (same neighbour positions, same 16 vector constraints, zero handedness): emergence means `−I` out-performs the achiral baseline BECAUSE of the reflection-odd screw, not because of added constraints. |

## §4 Method (extends prior; transport REUSED verbatim)

- **REUSE** from [`chiral_orbital_holonomy.py`](../src/scripts/vol_1_foundations/chiral_orbital_holonomy.py): `rotation_to_quaternion` (SO(3)→SU(2) lift, w≥0 branch + continuous-sign parallel transport), `orbit_plane_basis`, `solid_angle`, the SVD/Wahba pattern, the continuous-lift + smooth-transport guard, the double-cover (4π → +I) check, the 400-orbit battery cadence.
- **NEW geometry:** host A at origin; 1st shell = 4 B-neighbours at `p_j`; 2nd shell = 12 A-neighbours at the cuboctahedron positions reached via the B-intermediaries (canonical two-hop A→B→A, NOT invented). Each neighbour `n` carries a Cosserat frame `R_screw(xₙ) = Rot(â, κ·(xₙ·â))` — the genuine 4₁ screw (handedness = sign κ: κ>0 = I4₁32 native 4₁; κ<0 = I4₃32 mirror 4₃; **κ=0 = achiral control**). `â` ∈ cubic ⟨100⟩ (default ẑ; sweep all three).
- **The connection (replaces the ε-knob):** at orbit azimuth φ the loop's preferred orientation = Wahba alignment of the **screw-decorated** references `R_screw(xₙ)·ĥₙ` to the observed bond directions `(xₙ−p(φ))/|·|`, **equal weights** (NO reflection-even anisotropy). κ=0 + 1st-shell-only reduces EXACTLY to the prior ε=0 baseline.
- **Reflection-odd verification (built in):** mirror(config) must map the native `−I` map to the opposite-handedness map (the observable flips) — the property the ε-proxy did NOT have.
- **Sweeps:** orbit plane (uniform-on-sphere, 400 orbits) × radius; screw pitch κ (Z₂ must be pitch-independent); screw axis (3 cubic axes); shells (1st-only vs 1st+2nd); handedness (native / mirror / achiral).

## §5 Discriminator (frozen)

Let **f = fraction of swept orbits returning `−I`** with the native screw (κ>0, 1st+2nd shell).

- **f ≈ 100% (π for ALL paths)** → PATH-INDEPENDENT → intrinsic spin-½ EMERGES → **VERDICT (I), emergence-class.** The chiral crystal makes the real, frame-independent spin-½; the g=2 follow-up unblocks.
- **f partial / encircling-conditional (like prior 127/400)** → PATH-DEPENDENT → projected helicity only → **VERDICT (II), consistency-class.** Real but not the intrinsic spin-½.
- **f ≈ 0% with native screw but the achiral control also ≈ 0%** → the genuine screw does NOT host the `−I` at all → **VERDICT (III):** the reflection-even proxy's 32% was an artifact of the anisotropy degeneracies; the true screw removes them. (Mechanism: screw "combs" the field, no disclination around a single host.)

Report: f, the path-dependence map (is the `−I` set the whole sweep or still boundary-gated by a degeneracy locus?), pitch/axis/n_steps robustness, and the reflection-odd flip.

## §6 Prediction (honest pre-registration)

**Primary (my prior): VERDICT (II) — partial f, path-dependent.** Reasoning: a screw axis is a **translational** symmetry (frame rotation ∝ displacement *along* the axis), not a rotational **disclination** *around* the host. The FM intrinsic spin-½ arises from rotating the **extended unknot relative to the crystal** (`finkelstein-misner §2.2`), NOT from orbiting a single host node in a perfect crystal. So I expect the genuine screw to relocate/clean the Berry degeneracies but not convert encircling-conditional π into every-orbit π. Plausible f in the 0–50% band; possibly cleaner than 32% but not ~100%.

**Alternative under test (Grant's hypothesis): VERDICT (I) — f ≈ 100%.** If the 2nd-shell A/B screw genuinely makes the host's orientation field a chiral Z₂ defect that every loop sees, intrinsic spin-½ emerges from bulk chirality delivered locally.

**Held loosely — the test MEASURES.** Both (I) and (II) are honest outcomes (per the brief). Wrong reaction would be to tune κ/axis/shell-weighting to manufacture f≈100%; right reaction is faithful screw + measured f.

**Falsifier of the test framing:** if the achiral control (κ=0, 1st+2nd shell) ALSO gives a large `−I` fraction, then the 2nd-shell *geometry* (not the *chirality*) drives the result — the reflection-odd screw is not the operative ingredient and the "chirality makes spin intrinsic" framing is not what's being measured. (The matched-baseline guard, CP8.)

## §7 Classification (consistency-vs-emergence, pre-result)

- **Target:** the Z₂ holonomy sign `±I` (dimensionless homotopy invariant) and the fraction f ∈ [0,1]. **No CODATA, no `ave.core.constants`, no target observable as input** — pure SO(3)/SU(2) geometry from canonical lattice positions. ave-prereg Step 3.5 (dimensional-analysis-of-scaling-law) is N/A: the observable is a topological sign, not a magnitude; the "dimensional discipline" analog is the **pitch/n_steps/axis robustness** check (a genuine Z₂ invariant must be independent of all three).
- **Class (framed):** EMERGENCE test (does intrinsic spin-½ emerge from chiral geometry, with no spin-½ input?). **Class (result-contingent):** emergence-class IF (I); consistency-class IF (II) (geometry CAN host a chirality-required π but does not inevitably produce intrinsic spin); (III) would be a clean negative on the orbital-encircling mechanism for the true screw.

## §8 Files

- This prereg: `research/2026-06-07_2ndshell-screw-holonomy-prereg.md`
- Driver: `src/scripts/vol_1_foundations/secondshell_screw_holonomy.py` (to be written)
- Result: `research/2026-06-07_2ndshell-screw-holonomy-result.md` (to be written)
- Viz: `src/scripts/vol_1_foundations/_output/secondshell_screw_holonomy.png` (extends prior viz)
