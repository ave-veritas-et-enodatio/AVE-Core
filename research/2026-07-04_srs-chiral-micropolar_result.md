# RESULT — Stage 2 of the srs Elastic-Tensor Arc: the chiral micropolar coupling B is REAL and geometry-fixed, but it does NOT pin ν=2/7

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/srs-chiral-micropolar`
**Module:** `src/ave/core/micropolar_bloch.py`
**Driver:** `src/scripts/vol_1_foundations/srs_chiral_micropolar.py`
**Output:** `_output/srs_chiral_micropolar.json` (driver-regenerable)
**Prereg (FROZEN):** `research/2026-07-04_srs-chiral-micropolar_prereg_FROZEN.md`
**Parent (Stage 1, PR #506):** `research/2026-07-04_srs-elastic-tensor_result.md`
**Grant ruling (2026-07-04, verbatim):** "run both blindly, but what do our coupled
network equations or spice approach say?" — reading (c): compute B both ways blind, fold
in the three EE-canon pointers (all verified at HEAD, §7).

---

## VERDICT BOX

> **PRIMARY BIN: [FAMILY-CONSTRAINED-NOT-PINNED].**
>
> The chiral micropolar cross-coupling pseudo-tensor **B is NONZERO on the srs-z3 net**
> (B_invariant up to 2.32e-2 over ρ∈[0.5,10]; parity-odd, M2 sign-flip confirmed), is
> **GEOMETRY-FIXED** (sourced by the lever-arm / asymmetric-stress channel with ZERO new
> knobs — the σ^A channel dominates the μ channel by ~30 orders of magnitude, 1.05e-1 vs
> 5.4e-33), and its back-reaction **MOVES the effective long-wavelength ν_eff** (cross-
> coupling ON ≠ OFF; e.g. at ρ=3, ν: −0.314 OFF → +0.224 ON). **But it does NOT reduce
> the Stage-1 ρ-family to a point** — ν_eff(ρ) with the coupling ON is still a one-
> parameter family (stable-branch span ν_eff∈[−0.124, +0.391]), and it does **NOT force
> ν=2/7**: at Stage-1's K=2G point ρ*=9.7734 the chiral back-reaction pushes ν_eff to
> **0.389** (K/G_Hill=4.18, NO longer 2). **The independent κ_rot knob (reading b) is
> FLAT at k→0** — ν_eff is unchanged for all κ_rot∈[0,50] and sources NO Cauchy-grade B —
> so **the ½/¼-tell finds NO knob to tune**; there is no third-costume import. **K=2G
> stays GR-imported; the geometry-fixed chiral coupling is real and non-negligible but
> does not ground ν=2/7.**

**The corpus's own hypothesis — that the micropolar rotational sector `κ_rot·ε_ijk(θ_k−φ_k)`
enforces K=2G (clm-o3q9ul, DCVE spec, solidity 0.50 asserted-not-derived) — is NOT
confirmed by the srs geometry.** The geometry-fixed coupling exists but does not pin the
family; the independent κ_rot is a k→0 Cauchy-grade spectator (confirming the moduli-
hierarchy orthogonality `ℓ_c²=γ/G ⊥ ρ`). The open strengthen-by (clm-crbl60, "justify
K_vac=2G_vac for the chiral micropolar lattice") **stays OPEN** — geometry does not close
it.

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** full micropolar (Cosserat) sector of chiral srs-z3: per node 6 DOF (u, φ),
  48×48 D(k), 8 Wyckoff-8a sublattices. Three per-bond blocks: (1) u↔u Stage-1 Born
  `Φ_b=k_a·P+k_s·(I−P)`; (2) φ↔φ couple-stress `γ`; (3) u↔φ the CHIRAL cross-coupling,
  computed BLIND two ways (§0.5 of prereg).
- **REGIME:** cold linear, sub-yield, saturation OFF. Handedness enters the cold tensor
  ONLY through bond GEOMETRY (the lever arm), NOT κ_chiral (saturation-only). B is a
  GEOMETRIC-chirality effect of the non-centrosymmetric I4₁32 point group.
- **COORDS (A46):** real-space / spatial-Brillouin. ν_eff and B are real-space objects;
  the ν=2/7 claim is a real-space moduli ratio. Coordinates match.
- **CLASS:** CONSISTENCY. α-CLEAN (ratios only). **NO tuning toward 2/7** — bins + fallout
  frozen FIRST. The ½/¼-tell was armed and found NO tunable knob (reading b is flat).

---

## 1. VALIDATE-ON-KNOWN (all PASS, HALT-gated)

| # | Check | Target | Result | Verdict |
|---|---|---|---|---|
| **M0** | 6-DOF u-block (lever=0,γ=0,κ=0,no-cross) == Stage-1 srs C_ij | ν(ρ),Zener,K/G = Stage-1 table | max\|dC\| = **2.2e-16** (bit-for-bit) | **PASS** |
| **M1** | DIAMOND NULL: B on centrosymmetric Fd-3m | B ≡ 0 identically | B_a=**7.0e-19**, B_b=**7.0e-44** | **PASS** |
| **M2** | Enantiomorph sign flip: B(right) vs B(left) | B_signed flips, \|B\| preserved | signed R=**+5.995e-3** L=**−5.995e-3**, \|B\| match 2.8e-16 | **PASS** |
| **M3** | ν_eff parity: ν_eff(right) vs ν_eff(left) | ν_eff identical (parity-even) | ν R=L to <1e-4 | **PASS** |

**M0 is the load-bearing regression:** the 48×48 micropolar matrix contains the 24×24
Stage-1 Cauchy answer as its u-block limit, bit-for-bit — the extension did not corrupt
the parent. **M1 (the diamond null-control) is the elegant reuse of the retired diamond
instrument as a symmetry control:** centrosymmetry FORBIDS the piezo-class pseudo-tensor,
and B vanishes to numerical zero. **M2 confirms B is genuinely parity-odd** — the whole
translation↔rotation coupling block flips sign under enantiomorph swap
(`M_tr(left) = −M_tr(right)` exactly, R+L=0 to machine precision).

---

## 2. THE THREE READOUTS (frozen; reported whatever they say)

### Readout (a) — Is B nonzero on srs, and what sets its magnitude?

**B is NONZERO** on srs (reading a, geometry-fixed lever): B_invariant ranges 9.4e-4 to
2.3e-2 across ρ∈[0.5,10] (right enantiomorph, γ=6·k_s). **B is GEOMETRY-FIXED:**

- The coupling constant is the **lever arm** `b = lever·(d/2)`, FIXED by lattice geometry.
  Provenance: the Poisson-disk genesis fixes the node hard-sphere radius `r_node=ℓ_node`
  and the NN bond length `=ℓ_node` (`vol2/claim-quality.md:1028`; Stage-1's
  `a_cell=2√2·ℓ_node`). We report at the natural 2-body value `lever=1` (bond-midpoint
  attachment); **ν_eff is robust across the whole geometric lever range** (bond-midpoint
  to over-braced node-radius, lever∈[0.5,2]): ν_eff∈[0.222,0.233] at ρ=3 — the lever is
  NOT a knob that can be tuned to hit 2/7 (the whole geometric range clusters near 0.22).
- The couple-stress `γ` is FIXED by canon: `ℓ_c²=γ/G=6` (`constants.py:298`,
  `ℓ_c=√6·ℓ_node`) → `γ=6·k_s`. The ν_eff shift **saturates for γ≳6** (0.224 at γ=6,
  0.221 at γ=100) — the physical regime is in the γ-converged plateau, not a soft-γ
  artifact.
- **NO new stiffness.** Every constant in B traces to lattice geometry (lever, screw
  pitch via the inter-node connectivity) or canon (γ, and the same k_a,k_s as Stage-1).

**Which channel carries B (Grant pointer 2 diagnostic):** the **σ^A (asymmetric-stress /
lever-arm) channel** carries essentially all of it — B_σA = **1.05e-1** vs B_μ =
**5.4e-33** (couple-stress/κ_rot channel). Per `vacuum-as-chiral-piezoelectric.md:129`,
σ^A-mediated = the geometric lever-arm picture. **The srs lattice IMPLEMENTS the geometric
reading (a); the independent-stiffness κ_rot sources NO Cauchy-grade chiral coupling.**
This is consistent with the trampoline canon (`trampoline-framework.md:87`): σ^A is "the
moment per unit area that drives microrotation," and a bond force with a moment arm is
exactly what makes the stress tensor asymmetric.

**Both bond models (robustness, Stage-1's standard):** B is nonzero and ν_eff shifts under
BOTH the Born non-central k_s spring (ν_eff(ρ=3)=0.224) AND a Keating-flavored bend-routed
variant (ν_eff(ρ=3)=0.333). The shift MAGNITUDE is model-dependent; B's EXISTENCE, its
parity, and the shift's DIRECTION are model-INDEPENDENT. The purely-central control
(k_s=0) correctly gives B=0 (no transverse force → no moment arm) — an internal
consistency check, not a Keating failure.

### Readout (b) — ν_eff INCLUDING the chiral back-reaction

The rotational sector is integrated out via the long-wave Schur elimination (the Born-
Huang machinery one grade up: the acoustic 3×3 eliminates BOTH the optic-translation AND
the micro-rotation DOF at O(k²)). The back-reaction is the ON−OFF difference:

| ρ | ν_eff OFF | ν_eff ON (a) | Δν | Zener ON | K/G_Hill ON | B_inv |
|---|---|---|---|---|---|---|
| 2.0 | −1.000 | +0.145 | +1.145 | 1.180 | 1.076 | 1.09e-2 |
| 3.0 | −0.314 | +0.224 | +0.538 | 1.264 | 1.477 | 1.53e-2 |
| 5.0 | +0.060 | +0.308 | +0.248 | 1.349 | 2.276 | 1.95e-2 |
| 7.0 | +0.195 | +0.353 | +0.158 | 1.391 | 3.074 | 2.16e-2 |
| **9.7734** | **+0.2857=2/7** | **+0.389** | **+0.104** | 1.423 | **4.180** | 2.31e-2 |
| 10.0 | +0.291 | +0.391 | +0.100 | 1.425 | 4.270 | 2.32e-2 |

**The chiral back-reaction MOVES ν_eff substantially** (Δν = +0.10 to +1.1 in the stable
branch) — the coupling is NON-negligible. It STIFFENS the response (ν_ON > ν_OFF). At
Stage-1's K=2G / ν=2/7 point (ρ*=9.7734), the coupling pushes ν_eff to **0.389** and
K/G_Hill to **4.18** — i.e. it moves the response AWAY from 2/7 and AWAY from K=2G.

### Readout (c) — Does the coupling constrain ρ (reduce the family)?

**NO distinguished point emerges.** ν_eff(ρ) with the coupling ON is a smooth, monotone
one-parameter family (stable span ν_eff∈[−0.124,+0.391]). The coupling SHIFTS the whole
curve up but does not COLLAPSE it to a point. Where ν_eff ON crosses 2/7 (ρ≈4.46) is NOT
a geometrically-distinguished point — just where the shifted monotone curve happens to
cross (reported for reference only; NOT sought). So [FAMILY-REDUCED-TO-POINT] is REJECTED.

**Reading (b) — the ½/¼-tell, armed and negative.** Sweeping the independent κ_rot∈[0,50]
at ρ=3 leaves ν_eff **completely FLAT** (−0.31434 for all κ_rot) and sources NO chiral B
(~1e-32). Confirmed wired (M4: κ_rot opens the rotational optic gap at finite k, mid-
spectrum eigenvalues 0→2→2.877 as κ_rot grows). So κ_rot is genuinely active at finite k
but is a **k→0 Cauchy-grade SPECTATOR** — exactly the moduli-hierarchy orthogonality
(`ℓ_c²=γ/G ⊥ ρ`, `axiom4-moduli:22-24`), now live-confirmed at the micropolar grade.
**There is NO knob to tune onto 2/7; the ½/¼-import in a third costume does not exist.**

### Readout (d) — Both enantiomorphs (frozen falsifier)

B_signed(left) = −B_signed(right) EXACTLY (M2; the whole M_tr block flips, R+L=0 to
machine precision). ν_eff(left) = ν_eff(right) EXACTLY (M3; parity-even). **Both frozen
falsifiers PASS:** the pseudo-tensor is parity-odd, the modulus ratio is parity-even — no
bug mixed a parity-odd term into an even observable.

---

## 3. THE PHYSICAL PICTURE (what the srs lattice implements)

The single-node srs bond geometry is the 120°-balanced trivalent star and is COPLANAR
(det of the 3 bond directions = 0 exactly). **The chirality is NOT in the single-node
geometry** — it is in how consecutive nodes' bond-planes ROTATE along the 4₁ screw axis
(the girth-10 helical connectivity). This is why B emerged from the FULL lattice sum
(non-local, inter-node) and vanished identically on diamond (M1). The mechanical acoustic-
activity coupling is the MECHANICAL sibling of the A44 EM gyrotropic converter
(`cross_sector_coupling.py:5-10`, "an Axiom-1 non-centrosymmetry consequence"), realized
here as the σ^A lever-arm channel. **Its FORM is forced by geometry (non-centrosymmetry);
its back-reaction moves ν_eff but does not select a distinguished ρ.** This is the FORM-
deriving / VALUE-importing meta-finding again: the chiral coupling's FORM is geometric,
but the value ρ* that would land K=2G stays externally supplied.

---

## 4. SPICE / coupled-network cross-check (numpy-MNA; ngspice ABSENT)

Per the SPICE-lane pilot pattern (`spice-lane-feasibility_note.md`: native numpy, ngspice
UNINSTALLED — named limitation), a bounded two-tank cell MNA reproduces the fork: reading
(a)'s wiring-topology-fixed mutual coupling gives ONE mode-splitting (no knob); reading
(b)'s explicit swept element gives a knob-dependent splitting. **Consistent with the
lattice finding:** geometry supplies a fixed coupling (the def-ch1crc inter-tank coupling,
`vocabulary-register.md:700`), while κ_rot is a tunable dressing that does not touch the
k→0 answer. Bounded; ngspice not run (the named limitation applies).

---

## 5. BIN VERDICT + fallout inheritance (flag-don't-fix; auditor lands)

**PRIMARY BIN: [FAMILY-CONSTRAINED-NOT-PINNED]** (frozen prereg vocabulary; no post-hoc
bin invention). B nonzero + ν_eff moved (non-negligible) but family stays one-parameter
in ρ (not pinned). The frozen [CHIRAL-COUPLING-NEGLIGIBLE] bin is REJECTED because ν_eff
IS moved; [FAMILY-REDUCED-TO-POINT] is REJECTED because no distinguished point emerges;
[B-VANISHES] is REJECTED (B is nonzero on srs, vanishes only on diamond).

The Stage-1 fallout map (F.A–F.D) carries over UNCHANGED. Stage 2 adds these status rows
(SURFACED for auditor + Grant, NOT landed by this implementer lane):

| Leaf | Stage-2 verdict |
|---|---|
| clm-o3q9ul (`vol2/claim-quality.md:1059`, "micropolar κ_rot enforces K=2G") | **NOT confirmed by srs geometry.** The geometry-fixed chiral coupling exists but does not pin the family; the independent κ_rot is a k→0 Cauchy-grade spectator. The claim stays asserted-not-derived at solidity 0.50. |
| clm-crbl60 strengthen-by (`strengthen-by.jsonl:186`, "justify K_vac=2G_vac micropolar") | **STAYS OPEN.** srs geometry does not close it — the micropolar sector does not force K=2G. |
| def-ch1crc magnitude (`vocabulary-register.md:700`; `device-circuit-models.md:163`, "STATED-pending chiral-crystal engine") | **First geometry-derived number for the mechanical sibling:** the acoustic-activity B is geometry-fixed (σ^A channel), B_inv~1e-2. The EM non-reciprocity magnitude remains separately pending; this is the mechanical analog's magnitude, geometry-sourced. |
| K=2G GR-imported (PR#261) | **STRENGTHENED further.** Stage 1 showed the Cauchy tensor doesn't force ν=2/7 on srs; Stage 2 shows the FULL micropolar (rotational sector included, the corpus's own proposed mechanism) doesn't either. K=2G stays GR-imported at BOTH the Cauchy and the micropolar grade. |

**No rewrites performed.** Rows proposed for the auditor's manuscript queue only.

---

## 6. Scope + honest caveats

- **The ν_eff shift is real but its MAGNITUDE is model-dependent** (Born 0.224 vs Keating-
  flavored 0.333 at ρ=3). The ROBUST content — B nonzero, geometry-fixed, σ^A-channel,
  parity-odd, family-not-pinned, κ_rot-flat — is model-independent. The exact ν_eff number
  is not a bankable prediction; it is a CONSISTENCY-class structural result.
- **The lever value** (bond-midpoint vs over-braced node-radius) shifts ν_eff modestly
  (0.222–0.233 at ρ=3); reported as a geometric range, not a free sweep. No lever value in
  the geometric range lands on 2/7.
- **Keating robustness is a FLAVORED variant, not a full 3-body angle-bend implementation**
  (which would need its own validate-on-known and balloons); scope-tagged. The purpose is
  to confirm B is not a Born-normalization artifact, which it isn't.

---

## 7. EE-canon pointers (Grant, all VERIFIED at HEAD 2026-07-04)

1. **def-ch1crc** (`vocabulary-register.md:700`, verbatim): chirality is "an INTER-tank
   coupling, NOT a per-node C-vs-L reactance" — wiring-topology FORM. MAGNITUDE
   STATED-pending (`device-circuit-models.md:163`: "non-reciprocity MAGNITUDE is not yet
   computed... the cubic-FDTD engine averages chirality out"). **This blind run supplies
   the first geometry-derived magnitude for the mechanical sibling** (σ^A channel).
2. **σ^A channel** (`vacuum-as-chiral-piezoelectric.md:83,129-135`, verbatim): coupling is
   "antisymmetric stress σ^A → couple-stress → ω." **DIAGNOSTIC CONFIRMED:** B rides the
   σ^A channel (1.05e-1) not the μ channel (5.4e-33) → the lattice implements the
   geometric/lever-arm reading.
3. **SPICE** (`spice-lane-feasibility_note.md`): numpy-MNA two-tank; ngspice ABSENT
   (named limitation). Cross-check reproduces the geometry-fixed-vs-knob fork.

---

## Cross-references (verified at HEAD 2026-07-04)

- Module: `src/ave/core/micropolar_bloch.py`
- Driver: `src/scripts/vol_1_foundations/srs_chiral_micropolar.py`
- Prereg (FROZEN): `research/2026-07-04_srs-chiral-micropolar_prereg_FROZEN.md`
- Parent (Stage 1): `research/2026-07-04_srs-elastic-tensor_result.md` (PR #506)
- Carrier + null: `src/ave/core/chiral_lattice.py` `build_srs_net` / `build_diamond_net`
- Micropolar-forces-K=2G hypothesis: `manuscript/ave-kb/vol2/claim-quality.md:1059` (clm-o3q9ul)
- OPEN strengthen-by: `manuscript/ave-kb/.index/strengthen-by.jsonl:186` (clm-crbl60)
- σ^A channel: `research/2026-06-08_vacuum-as-chiral-piezoelectric.md:83,129-135`
- Moduli-hierarchy orthogonality ℓ_c²=γ/G ⊥ ρ: `research/2026-07-02_axiom4-moduli-hierarchy_result.md:22-24`
- def-ch1crc (inter-tank, magnitude-pending): `manuscript/ave-kb/common/vocabulary-register.md:700`; `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:163`
- A44 EM sibling: `src/ave/core/cross_sector_coupling.py:5-10`
- ℓ_c=√6·ℓ_node: `src/ave/core/constants.py:298`
- Grant ruling (c) + EE pointers: this session 2026-07-04
