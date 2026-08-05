# The LATTICE-REGULATED optical return delay to the `r_sat` wall — FROZEN pre-registration (**turns FORK-3(b) into a TIMING discriminator; SVA pilot case 2**)

**Date:** 2026-08-04
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). Committed **ALONE** and pushed **before any driver code and before any number produced by this instrument exists**.
**Result-doc pointer requirement.** The result doc that resolves these bins MUST carry `Prereg-file: research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file.
**Provenance:** Grant's GO of 2026-08-04 (core session, "delay derivation first"), following his catch on PR #876: the axial RHO-B lane's log-divergent `∫dr/c_shear` is a property of the **CONTINUUM LIMIT**; on the physical lattice the optical path is a **FINITE node-sum cut at the last cell** — *effectively* infinite (log-enhanced), not infinite. This lane derives the regulated version and turns it into a timing discriminator between the two profile branches.
**Written against** `origin/main` = `2877eaa0`.
**SVA pilot:** this is **pilot case 2** of the Standard Vacuum Analysis (`manuscript/ave-kb/common/standard-vacuum-analysis.md`, PILOT v0.1). Its §0 header is filled below, verbatim rows.

---

## §P — WHAT THIS LANE IS, IN ONE PARAGRAPH, AND WHAT IT IS NOT

Two canonical inertia gradings for the shear channel are in open fork (**FORK-3(b)**). Under **RHO-A** (`ρ = ρ_bulk`) the shear speed is `c₀√S` and the saturation wall sits at **FINITE** optical distance; under **RHO-B** (`ρ_eff = ρ_bulk/S³`, `μ`-primary) the shear speed is `c₀S²` and the continuum optical distance **diverges logarithmically**. **This lane computes the LATTICE-REGULATED return delay under both branches, in closed form and by an explicit node sum, and asks whether the two branches are distinguishable by TIMING.** The regulator is the lattice itself: there is no node inside `r_sat` (Regime IV), so the sum terminates.

**It is NOT** an adjudication of FORK-3, **NOT** a re-run or re-score of the axial RHO-B eigenvalue lane, **NOT** an adjudication of FLAG-W, **NOT** a claim that echoes are or are not observed, and **NOT** a repair of any KB leaf. It derives ONE quantity — the round-trip optical delay — under both branches, with its regulator sensitivity measured rather than assumed.

### §P.1 Predecessor state, in order — and the fence that makes "byte-untouched" checkable

| lane | artifact | state |
|---|---|---|
| **2026-06-17 BH shear-echo forward prereg** (MERGED, FROZEN, SHA-pinned `04bcb4ac`) | `research/2026-06-17_bh-shear-echo-forward-prereg.md`, `src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py` | **The RHO-A predecessor.** Prong 1 derives `Δt = 2∫_{r_sat}^{r_out} dr/c_shear` with `c_shear = c(1−ε₁₁²)^{1/4}` (**= RHO-A**) and reports a `3–10 ms` band for a `62 M_⊙` remnant — a band whose width is the **undeclared `r_out`**, i.e. an undeclared reference plane. **This lane's RHO-A row must reproduce that driver exactly (`G-NC`) and then replace the band with a plane-declared number.** |
| **v2.4 axial cold-Q** (MERGED) | `research/2026-08-03_coldq-pole-v2.4-root_*`, `research/drivers/coldq_pole_v2p4_root*` | `ROOT-CERTIFIED` under RHO-A. Supplies this lane's **substrate-native ringdown frequency and damping time**, read PROGRAMMATICALLY. |
| **axial RHO-B** (PR #876, OPEN, DO-NOT-MERGE) | `research/2026-08-04_coldq-axial-rhob_*` | `ROOT-NOT-CERTIFIED`; **wall analysis CERTIFIED**. Source of the derived RHO-B profile statements this lane consumes as THEOREMS. **A core-session correction note is landing on that branch separately; this lane does not touch it.** |

**Predecessor fence, frozen.** `every predecessor file named in section P.1 is BYTE-UNTOUCHED by this lane and the claim is discharged by an empty git diff --stat against the freeze base on each of them; src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py and research/drivers/coldq_pole_v2p4_root_results.json are consumed READ-ONLY and are neither edited nor re-scored`.

**Scope fence, frozen.** `this lane writes under research/ ONLY; it edits no manuscript or KB file, proposes no claim-quality repair, touches no FLAG-W or sign-relativity leaf, and does not touch the PR #876 branch`.

---

## §0 — Standard Vacuum Analysis header (SVA v0.1-pilot)

 1. SECTOR / OWNERSHIP:      The propagating observable is a **transverse shear (T2)** disturbance; the DC grading that slows it is the **A1 radial dilatation** `ε₁₁(r) = 7GM/(c²r)`. A1 owns the bias profile, T2 owns the wave. **Cross-wiring check: the delay is a T2 transit time through an A1-set profile — no bulk (A1) speed, no Cosserat microrotation, and no EM channel enters any number in this lane.** The EM channel is `Z_EM = Z₀` matched and is explicitly NOT the carrier of this delay.
 2. REGIME / PHASE-STATE:    **MODE** = small-signal AC transit-time on a static DC bias. **REGIME** = sub-yield lossless-reactive for `r > r_sat`; `r < r_sat` is Regime IV and is **not in the domain**. **PHASE-STATE** = cold lattice with Op14 ON as a static constitutive grade, `A(r) = r_sat/r`, `A = 1` exactly at `r_sat`. **DC bias point** = the gravitational grading itself. Small-signal is exact because the ringdown amplitude does not move the operating point.
 3. CIRCUIT STATEMENT:       Before any relativity word: **a lossless LC ladder whose per-section delay `√(L_nC_n)` grows without bound toward one end, cut at the last physical section.** The observable is the **two-way group delay** of that ladder measured at a declared plane — a TOTAL observable (round-trip phase slope), not a per-section slot. `T_return = 2·Σ_n ℓ_node/v_g(n)`.
 4. PLANE & PROJECTION:      **PLANE-∞ (PRIMARY):** the delay is reported as the **EXCESS over cold-lattice flight**, `ΔT = 2∫(1/v − 1/c₀)dr` with `r_out → ∞`. This converges (the integrand is `O(1/r²)`, no `1/r` term) and is therefore **plane-INVARIANT** — the free-flight term that carries all plane dependence is subtracted identically. **PLANE-PEAK (SECONDARY):** the DERIVED maximum of the branch's own effective barrier `𝒱(r) = v(r)²U(r)` (§2.6), an ω-independent, substrate-derived radius. **No signed Γ is claimed anywhere in this lane** — the delay is a magnitude, so wall-taxonomy §9's sign discipline is satisfied vacuously and is NOT relied on.
 5. CONSTITUTIVE PROVENANCE: `S(A)=(1−A²)^{1/2}` **DERIVED** (Ax 4). `A(r)=r_sat/r` **DERIVED-FORM / VALUE-IMPORTED** (the `7` rides GR-imported `ν_vac=2/7`). `μ=G_vac S` **DERIVED**. `ρ=ρ_bulk` (RHO-A) vs `ρ_eff=ρ_bulk/S³` (RHO-B) **FORKED (FORK-3(b), OPEN)**. `ℓ_node = ħ/(m_e c)` **IMPORTED-VALUE / DEFINITIONAL** (rides CODATA `ħ`, `m_e`, `c`; `m_e` is definitional per the FORM/VALUE meta-finding). Band top `π√3 ω_C` scalar / `[5.4414, 17.0111] ω_C` vector **DERIVED-FORM, BRACKET OPEN** (pending Grant's single-scale-vs-stiffness-lifted ruling). `ℓ=2` **INPUT**.
 6. ENERGY LEDGER:           **No port is crossed anywhere in this lane and no loss word is used.** The delay is a pure reactive transit time on a lossless ladder; `Re{Z} = 0` at every node by Ax 3. The only port in the problem is the radiative one at infinity, and it is OUTSIDE the interval being timed. **No "absorption", no "dissipation", no "damping" is attributed to the wall by this lane.**
 7. CALIBRATABILITY:         The primary output is the **dimensionless** ratio `c₀ΔT/r_sat`. Its RHO-B value is a **log of a dimensionless length ratio** `r_sat/ℓ_node` — two lengths measured against each other, self-calibratable from inside. The SI-second value is that ratio times `r_sat/c₀`, and its VALUE-class is inherited from `G`, `M`, `ν_vac`, `ℓ_node`. **`α` appears nowhere in the chain.**
 8. DISCRIMINATION CLASS:    **DC→AC coupling** — a DC (gravitational) bias modulating an AC (shear-wave) transit time. Live chord class. **Tautology filter:** the RHO-A number is NOT a restatement of `r_sat/c` (it is `0.802 × r_sat/c₀` only after the profile integral is done; the coefficient is the content). **SM/GR counterfactual, stated in advance:** GR-Kerr predicts NO return at all (horizon absorption); ECO models predict a log-delay `∝ ln(δ/M)` with `δ` a **free knob**. **RHO-B's log law is structurally DEGENERATE with the ECO form and the discrimination rests entirely on AVE having no knob (`ℓ_node` is fixed); this degeneracy is declared HERE, before the number, and is a frozen reporting requirement (§9 FLAG-ECO).**
 9. CERTIFICATION PLAN:      Gates §5 and fireability self-tests §6 frozen before any number exists; **UNRUN ≠ PASSED**; negative control = exact reproduction of the 2026-06-17 predecessor driver's RHO-A delay (`G-NC`); determinism by two-run digest.
10. ADJUDICATION ROUTING:    This lane settles **whether FORK-3(b) is echo-discriminable by TIMING** (BIN-DISC vs BIN-DEGEN) and **whether the regulated RHO-B delay is a parameter-free number or a regulator artifact** (BIN-CUTOFF). It settles **nothing** about which inertia grading canon means, nothing about whether an echo train exists (that needs an outer reflectivity this lane does not compute), and nothing about any observational claim. On every outcome the propagation target is **a research-doc result and a docket fragment only**.

---

## §0.1 — Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity — and this is the checkpoint that CHANGES the answer.** The predecessor lanes ran **CONTINUUM** instruments and were entitled to. **This lane is the opposite: its whole content is that the lattice is discrete**, so the connectivity is load-bearing. Frozen: `the radial path is modelled as a ONE-DIMENSIONAL cascade of node-spaced transmission-line sections, the substrate-native band model for which is the coined-quantum-walk / transmission-line ARCCOS map omega = omega_link*arccos(mu/z) adjudicated at srs-band-structure.md section 2, and NOT the graph-Laplacian omega = sqrt(lambda) map which that same section shows FAILS the 1/sqrt3 velocity gate; the 1D reduction is a DISCLOSED modelling choice for the radial direction and its 3D-srs correction is not computed`.
2. **Cosserat / channel basis.** The shear branch is the **vector / Cosserat-translational** channel. Its band top is a **BRACKET** `[5.4414, 17.0111] ω_C` (`srs-band-structure.md` §3), not a single number, because the arccos map does not cleanly generalize to the vector channel. Frozen: `the band-edge regulator is swept over BOTH ends of the vector band-top bracket [5.4414, 17.0111]*omega_C and the scalar single value pi*sqrt(3)*omega_C = 5.4414*omega_C is the lower end of that bracket, not an independent third reading; no ruling on the single-scale-vs-stiffness-lifted fork is made, implied or relied on`.
3. **Op14 saturation.** Enters as the static grade `S(A) = √(1−A²)` in the modulus for both branches and, **under RHO-B only**, a second time in the inertia. **It also enters a THIRD time, and that is this lane's new content: the LOCAL BAND TOP scales with the LOCAL speed**, `ω_max(r) = π√3·c(r)/ℓ_node`, so Op14 modulates the lattice's own frequency ceiling. Frozen: `the local band edge collapses with the local speed as omega_max(r) = (band-top coefficient)*c(r)/l_node, so an Op14-graded region has a spatially varying frequency ceiling; this is the local-clock-modulation checkpoint applied to a BAND EDGE rather than to an eigenvalue`.
4. **The compactification is the medium's own order parameter.** The radial variable is `A = r_sat/r`, the Ax-4 saturation amplitude itself. `A = 1` IS the wall.
5. **Phase-space vs real-space (A46).** The verdict-class observable `c₀ΔT/r_sat` is a **dimensionless ratio**; the discriminator `T_B/T_A` is a ratio of two such. **α-CLEAN.**
6. **Boundary-not-bulk.** The delay accumulates in the **graded skin**, not in the bulk: §2 makes explicit what fraction of the RHO-B delay comes from the innermost decade of `S`. That fraction is the direct measurement of "the physics lives in the skin" (wall-taxonomy §3).
7. **★ NEW CHECKPOINT forced by this lane: is the transport time set by PHASE velocity or GROUP velocity?** **GROUP** — a delay is a group delay. Frozen: `the transport speed is the GROUP velocity of the substrate-native dispersion, derived in section 2.5 rather than assumed; for the 1D transmission-line cascade the arccos map yields an EXACTLY LINEAR dispersion omega = c_link*k on 0 <= k*l <= pi, hence v_group = v_phase = c(r) identically up to the zone edge, and the group-vs-phase distinction makes NO difference under the adjudicated substrate-native model; the REJECTED lumped/tight-binding model omega = 2(c/l)sin(k*l/2) gives v_group = c*cos(k*l/2) -> 0 at the edge and IS swept as a disclosed robustness variant`.
8. **★ NEW CHECKPOINT forced by this lane: does the wave reach the last node, or turn around at the band edge first?** Undetermined at freeze; §2.7 derives the condition and §7 bins the answer.

---

## §0.2 — Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — this is the question your own catch creates, and I cannot answer it from canon.**
>
> Your correction was that the RHO-B divergence is a continuum artifact and the real path is a finite node sum. I have built that. But building it forces a second question I did not expect, and it is a plumbing question, not a mathematics one.
>
> As I walk inward, each cell's local propagation speed collapses. **A transmission-line section's usable bandwidth collapses with it** — a section that is a hundredth of a wavelength at the top of the graded region becomes a half-wave section deeper in, and below that the ladder is a **cut-off filter**, not a delay line. So there are two candidate "last places the signal reaches":
>
> - **the last NODE** — the innermost intact cell, one `ℓ_node` outside `r_sat`, beyond which there is no lattice (Regime IV); or
> - **the last node where my ringdown frequency is still IN BAND** — where `ω = ω_max(r)`, above which the ladder is evanescent and the wave turns around **before** running out of cells.
>
> **My arithmetic says these two radii land within about a factor of two of each other, at every mass, and the coincidence is not an accident** — a ringdown at the object's own light-crossing frequency has `ω r_sat/c ≈ 1`, which forces both radii to scale as `√(ℓ_node/r_sat)`. So the answer is on a knife edge and the physics differs qualitatively:
>
> - if the **node** wins, the delay is **achromatic** — every frequency in the burst returns at the same time, and the echo is a clean delayed copy;
> - if the **band edge** wins, the delay is **CHIRPED** — `T(ω) ∝ ln(ω_top/ω)` — high frequencies return sooner, and the echo is a swept-frequency tail rather than a copy. **A chirped echo is a completely different search template.**
>
> **My question is: which one does a real ladder do?** In bench terms — when I taper an LC ladder until the last few sections are past cutoff at my drive frequency, does the pulse reflect off the cutoff (a soft, dispersive, frequency-dependent turning point) or does it tunnel the last few sections and reflect off the physical end (a hard, achromatic termination)? The sections are lossless either way, and the evanescent region here is only a handful of cells thick, which is exactly the regime where tunnelling is not negligible.
>
> I have frozen both outcomes as reachable bins and I am **not** choosing by preference. What I need from you is whether the evanescent-tunnelling reading is the honest one for a lossless ladder whose cutoff region is a few cells deep — because if it is, then the band-edge turning point never actually governs, the delay is achromatic, and the "chirp" branch is a mathematical artifact of treating a 3-cell evanescent skin as an infinite one.
>
> **Carried forward and NOT re-asked:** the axial lane's `FLAG-CAUSAL` (is an infinite-electrical-length lossless termination a legitimate Ax-3 radiative port?). **This lane's regulated sum makes that question quantitative but does not answer it** — the electrical length is no longer infinite, it is `~19` radians of `ln`, and whether that is "a port" or "a mirror" is still yours.

---

## §0.3 — Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE any result

| output | rides an imported VALUE? | class |
|---|---|---|
| `c₀ΔT_A/r_sat = 2𝒥_A` (the RHO-A coefficient) | **NO** — a pure number from the profile shape and the Ax-4 kernel | **AXIOM-MANIFESTATION, FORM-class.** The coefficient is forced by `S(A)` and `A=r_sat/r` alone. |
| `ΔT_A` in seconds | **YES** — `r_sat/c₀` carries `G`, `M` and the GR-imported `ν_vac` through the `7` | **VALUE-CONSISTENCY.** May NOT be headlined as value-level emergence. |
| `c₀ΔT_B/r_sat = ln(2r_sat/ℓ_node) + K_disc` | **YES** — the log's argument is `r_sat/ℓ_node`, so it rides BOTH the GR-imported `7` AND the definitional `ℓ_node = ħ/(m_ec)` | **VALUE-CONSISTENCY on the argument, AXIOM-MANIFESTATION on the FORM.** The `ln` and the `1/2` coefficient are forced; the number inside the `ln` is imported. |
| `T_B/T_A` (the fork discriminator) | **partially** — the `r_sat/c₀` scale cancels exactly; the `ln(r_sat/ℓ_node)` does not | **FORM-class with an imported log argument.** This is the honest tag and the result doc must carry it. |
| the turning-point verdict (node vs band edge) | **NO** — it is the sign of `S_turn − S_last`, both `∝ √(ℓ_node/r_sat)` | **FORM-class, DERIVED, and MASS-INDEPENDENT.** |

Frozen tag: `the delay LAWS derived here are FORM-class axiom manifestations of the Ax-4 kernel plus lattice discreteness; every SI-second VALUE they produce is VALUE-CONSISTENCY class because it rides G, M, the GR-imported nu_vac in r_sat = 7GM/c^2, and the definitional l_node = hbar/(m_e*c); no output of this lane may be headlined as value-level emergence and the FORM/VALUE split must be restated in the result headline`.

---

## §1 — THE TARGET AND THE EXPLICIT NON-CLAIMS

### §1.1 The target

**Derive, in closed form and then evaluate by an explicit lattice node sum, the round-trip optical delay from a declared exterior reference plane inward to the innermost node the wave reaches, under BOTH profile branches — and report (i) whether the innermost reached node is the last lattice cell or an ω-dependent band-edge turning point, (ii) the resulting delay law and its frequency dependence, and (iii) the sensitivity of the answer to the regulator.**

### §1.2 The non-claims, written in advance and binding

- **NO adjudication of FORK-3(b).** Frozen: `this lane computes the delay under both branches; it does not prefer RHO-A over RHO-B or RHO-B over RHO-A, and a cleaner number on one branch is not evidence for that branch`.
- **NO claim that an echo TRAIN exists.** Frozen: `an echo train requires an OUTER partial reflector with a computed reflectivity; this lane computes a barrier LOCATION but no reflectivity, no transmission coefficient and no amplitude of any kind, so it states a DELAY and never an echo amplitude, an echo count, or a detectability`.
- **NO observational claim.** Frozen: `no LIGO/Virgo dataset is analysed, no detection or non-detection is asserted, and every observational quantity that appears is an IN-REPO CITED POINTER used as a comparison scale only`.
- **NO adjudication of FLAG-W, of the sign-relativity ruling, or of the claim-quality `:123` echo sentence.** Frozen: `this lane raises the RHO-A-conditionality of vol3/claim-quality.md:123 only by pointer, proposes no edit, and the claim-quality repair is ruling-dependent and explicitly NOT this lane's`.
- **NO re-score of any predecessor.** Frozen: `the 2026-06-17 forward prereg's 3-10 ms band and the v2.4 certified root stand exactly as their own documents left them; G-NC is a REGRESSION CONTROL on this lane's own transcription and is not a re-certification of anything`.

### §1.3 What this lane additionally does NOT do

- **Y1** — does NOT derive `ℓ = 2`. Quadrupole selection is an input.
- **Y2** — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`.
- **Y3** — does NOT compute any eigenvalue, pole, `Q`, or mode. It consumes v2.4's certified root as a **frequency scale** only.
- **Y4** — does NOT build the Cosserat microrotational channel and does NOT treat the polar/spheroidal branch.
- **Y5** — does NOT resolve the single-scale-vs-stiffness-lifted band-top fork; it **sweeps** it.
- **Y6** — does NOT compute the 3D srs correction to the 1D radial cascade.
- **Y7** — does NOT model the Regime-IV interior, and computes nothing at `r < r_sat`.
- **Y8** — does NOT compute a reflectivity, a tunnelling amplitude, or an evanescent-decay length through the cutoff region. **The plumber question of §0.2 is asked, not answered.**
- **Y9** — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry, whatever the outcome.
- **Y10** — does NOT edit `Makefile` recipes belonging to any other lane; it appends its own target only.

---

## §2 — THE DERIVATION, DONE HERE, BEFORE ANY CODE (every statement below is a THEOREM available at freeze)

### §2.1 The two speed profiles, RE-DERIVED from canon rather than imported

**The grading chain, each link cited and re-derived:**

```
eps_11(r) = 7 G M / (c^2 r) = r_sat / r  ==  A(r)      [electron-bh-isomorphism.md:19; index.md:17]
r_sat     = 7 G M / c^2,  eps_11(r_sat) = 1 exactly    [ave-bh-horizon-area-theorem.md:20; 7 = 2/nu_vac]
S(A)      = (1 - A^2)^(1/2)                            [Axiom 4; saturating-modulus-and-backreaction.md:52]
mu(r)     = G_vac * S                                  [saturating-modulus-and-backreaction.md:56-60 sign-lock]
```

**RHO-A** (`ρ = ρ_bulk`, the cold-lattice inertia):

```
c_A = sqrt(mu/rho) = sqrt(G_vac*S/rho_bulk) = c_0 * S^(1/2) = c_0 (1 - A^2)^(1/4)
```

which reproduces the canonical `:60` verbatim *"**SHEAR softens:** $c_{shear}=c_0\sqrt S=c_0(1-A^2)^{1/4}\to0$"* and the predecessor driver's `c_shear(r) = c(1-eps_11^2)^(1/4)`. **This is the `G-NC` handshake: the same formula, re-derived, not transcribed.**

**RHO-B** (`ρ_eff = ρ_bulk/S³`, μ-primary; `saturating-modulus-and-backreaction.md:73`, `interior-singularity-resolution.md:19`):

```
c_B = sqrt(mu/rho_eff) = sqrt(G_vac*S*S^3/rho_bulk) = c_0 * S^2 = c_0 (1 - A^2)
```

**Independently re-derived here and agreeing with the axial lane's frozen §2.2 and the polar lane's §336.** Frozen: `both speed profiles are re-derived in this lane from the Ax-4 kernel, the modulus grading and the branch inertia; neither is transcribed from a brief or from a predecessor document, and the RHO-A form is checked against the 2026-06-17 predecessor driver by G-NC`.

**One-line form, used throughout.** `v(r) = c_0 * S^p` with **`p = 1/2` (RHO-A)** and **`p = 2` (RHO-B)**. Every derivation below is written in `p` so that both branches, and the synthetic `p = 3` self-test profile, run through one code path.

### §2.2 The regulated node sum, and the reference-plane declaration

The physical object is a **finite sum over intact lattice cells**, not an integral:

```
T_return(omega) = 2 * SUM_{n=1..N}  l_node / v_g(r_n),     r_n = r_sat + (n - 1 + theta) * l_node
```

with `theta` the sub-cell placement regulator and `N` fixed by the innermost reached node (§2.7). **The sum terminates because there is no lattice inside `r_sat`** — the interior is Regime IV, ruptured topology, outside the domain (`§0` REGIME row). *This is the whole of Grant's correction, made arithmetic.*

**★ PLANE DECLARATION (wall-taxonomy §9 row 1: no delay travels without its plane).** The bare sum's outer end depends on `r_out`, which is a free knob — exactly the knob that made the predecessor's answer a `3–10 ms` **band** rather than a number. This lane removes it by declaring:

- **PLANE-∞ (PRIMARY, plane-INVARIANT).** Report the **EXCESS over cold-lattice flight**:

```
Delta_T(omega) = 2 * SUM_n l_node * ( 1/v_g(r_n) - 1/c_0 )      ->   2 * INT ( 1/v - 1/c_0 ) dr
```

  **This converges as `r_out → ∞`.** Proof, at freeze: `1/v - 1/c_0 = (S^{-p} - 1)/c_0` and `S^{-p} - 1 = (1-A^2)^{-p/2} - 1 = (p/2)A^2 + O(A^4)`, so the integrand is `O(A²) = O(1/r²)` with **no `1/r` term** — the same short-range statement the axial lane froze for its radiative port. The free-flight term `2(r_out - r_in)/c_0`, which carries **all** the plane dependence, is subtracted identically. Frozen: `the PRIMARY reported delay is the EXCESS over cold-lattice flight with r_out -> infinity; it converges because the graded deviation is O(1/r^2) with no 1/r term, it is therefore INDEPENDENT of the outer reference plane, and it is the quantity in which the two branches are compared`.

- **PLANE-PEAK (SECONDARY, DERIVED, ω-independent).** The maximum of the branch's own effective barrier `𝒱(r)` (§2.6). Total (not excess) round trip from there inward. **This is the observationally-conventional analogue** of "peak-to-reflector" and it is reported so the number can be read against the echo-search convention. Frozen: `PLANE-PEAK is the DERIVED maximum of the branch's own effective barrier V(r) = v(r)^2 * U(r), located numerically per branch and gated by G-PEAK; it is NOT the GR photon sphere (3GM/c^2), which lies INSIDE r_sat and is therefore unavailable as an outer plane in this geometry`.

**Why the barrier plane matters and was missed before.** The 2026-06-17 predecessor recorded, verbatim, that *"there is no parameter-free outer reflector outside `r_sat`"* because both corpus candidates (`r_ph = 3GM/c²`, `r_eff = 49M_g/9`) sit **inside** `7GM/c²`. **That survey omitted the barrier the graded profile builds itself:** the centrifugal term in the effective potential is `∝ v(r)²/r²`, and because `v → 0` at the wall it vanishes at BOTH ends, so `𝒱` necessarily has an interior maximum **outside** `r_sat`. §2.6 derives it. Frozen: `the effective-barrier maximum is DERIVED in this lane from the branch profile and is a parameter-free outer plane OUTSIDE r_sat; the 2026-06-17 statement that no parameter-free outer reflector exists outside r_sat surveyed only imported GR radii and is SURFACED here as incomplete, not repaired, and no edit to that frozen document is proposed`.

### §2.3 RHO-A in closed form — a pure number, and the wall is at FINITE optical distance

With `A = r_sat/r`, `dr = -r_sat dA/A²`, the excess one-way delay is

```
Delta_T_1way = (r_sat/c_0) * INT_{A_out}^{A_in} [ (1-A^2)^{-p/2} - 1 ] dA / A^2
```

Substituting `u = A²` and using `INT_0^1 u^{a-1}[(1-u)^{-q} - 1] du = B(a, 1-q) - 1/a` by analytic continuation at `a = -1/2`:

```
J(p) == INT_0^1 [ (1-A^2)^{-p/2} - 1 ] dA / A^2  =  1 - sqrt(pi) * Gamma(1 - p/2) / Gamma((1-p)/2)
```

**RHO-A (`p = 1/2`):**

```
J_A = 1 - sqrt(pi) * Gamma(3/4) / Gamma(1/4)          [FINITE — a pure number]
Delta_T_return^A  =  2 * (r_sat/c_0) * J_A            [ACHROMATIC, REGULATOR-FREE]
```

**RHO-B (`p = 2`):** `Γ(1-p/2) = Γ(0)` diverges — the integral is log-divergent, exactly as the axial lane derived. The Beta form **contains both branches and shows the divergence as a pole of a Gamma function**, which is the two-method receipt that the RHO-A finiteness and the RHO-B divergence are the same statement evaluated at two exponents.

**Why RHO-A needs no regulator.** Near the wall `A → 1`, `S ≈ √(2x/r_sat)` with `x = r - r_sat`, so `1/v_A ∝ x^{-1/4}`: the innermost-cell contribution scales as `(ℓ_node/r_sat)^{3/4} ~ 10^{-12}` of the total. Frozen: `the RHO-A delay is regulator-INDEPENDENT because the near-wall integrand exponent is -1/4 > -1, so the last-cell contribution scales as (l_node/r_sat)^(3/4) and every regulator variant of section 4.4 must agree to better than 1e-6 relative; a failure of that agreement is a BIN-DA-OPEN outcome and an instrument defect, not physics`.

### §2.4 RHO-B in closed form — an EXACT antiderivative, and the node-regulated law

For `p = 2` the excess integrand collapses:

```
(1/A^2)[ (1-A^2)^{-1} - 1 ]  =  1 / (1 - A^2)
Delta_T_1way^B = (r_sat/c_0) * [ artanh(A_in) - artanh(A_out) ]        EXACT, elementary
Delta_T_return^B (PLANE-inf) = 2 * (r_sat/c_0) * artanh(A_in)          since artanh(0) = 0
```

**The regulated law.** With the innermost node at `r_in = r_sat + theta*l_node`, `1 - A_in = theta*l_node/(r_sat + theta*l_node)`, and `artanh(A) = (1/2)ln((1+A)/(1-A))`:

```
Delta_T_return^B  =  (r_sat/c_0) * ln( 2 r_sat / (theta * l_node) )  *  [1 + O(l_node/r_sat)]
```

**This is the headline symbolic result and it is PARAMETER-FREE in the sense that only `r_sat` and `ℓ_node` appear** — the log argument is a ratio of two canonical lengths. Its VALUE-class is nevertheless VALUE-CONSISTENCY (§0.3), because `r_sat` rides `ν_vac` and `ℓ_node` rides `m_e`.

**In terms of the wall variable.** Since `1 - A ≈ S²/2` near the wall, `artanh(A_in) = ln(2/S_in) + O(S_in²)`, so equivalently

```
Delta_T_return^B  =  2 * (r_sat/c_0) * ln( 2 / S_in )
```

and **every regulator question reduces to "what is `S_in`?"** — which is §2.7. Frozen: `under RHO-B the entire regulator dependence of the delay enters through ln(2/S_in) and is therefore LOGARITHMIC in the regulator; a factor-f ambiguity in the cutoff S_in moves the delay by ln(f)/ln(2/S_in), and the honest test of the parameter-free claim is whether that fraction is small, which is BIN-CUTOFF and is measured rather than asserted`.

**Skin-fraction diagnostic (wall-taxonomy §3, "the physics lives in the skin"), frozen as a reported quantity:** the fraction of `ΔT_return^B` accumulated inside `S < 0.1`, `S < 10⁻³`, `S < 10⁻⁶`, reported as a table. Under a log law each decade of `S` contributes **equally** — `ln 10` per decade — which is a falsifiable structural prediction of the derivation and is gated as `G-DECADE`.

### §2.5 The lattice dispersion `ω(k)` of the graded chain — DERIVED, not assumed

**The substrate-native band model is adjudicated, and it is not the one a physicist reaches for by default.** `srs-band-structure.md` §2 (`clm-bnd5rq`) establishes as its *load-bearing methods fact* that the vacuum's dispersion is the **coined-quantum-walk / transmission-line arccos map**

```
omega_n(k) = omega_link * arccos( mu_n(k) / z ),      omega_link = c_link / l_node
```

and that the lumped graph-Laplacian map `ω = √λ` **FAILS** the canonical `1/√3` velocity gate. This lane uses the adjudicated map.

**For the radial cascade (`z = 2`, one bond each way), the Bloch adjacency eigenvalue is `μ(k) = 2cos(kℓ)`, so**

```
omega(k) = omega_link * arccos( cos(k*l) ) = omega_link * (k*l)      for 0 <= k*l <= pi
```

**— EXACTLY LINEAR.** Therefore

```
v_phase = omega/k = c_link ,    v_group = d(omega)/dk = c_link ,    v_group == v_phase identically
```

up to the zone edge `kℓ = π`, where

```
omega_max = pi * omega_link = pi * c_link / l_node
```

**This is the receipt the brief demanded: the group-vs-phase question is DERIVED and the answer is that under the substrate-native map they coincide, so no group-velocity correction to the delay exists.** It is also the reason the cascade is a **delay line and not a dispersive filter** below cutoff: a cascade of ideal lossless transmission-line sections is non-dispersive, which is the substrate-native content of "no internal gap" in the srs survey.

**The band top in `ω_C` units, and its bracket.** With `c_link = √3 c₀` (the `1/√3` network-velocity projection, `boundary-observables-m-q-j.md:106`), `ω_link = √3 ω_C` and the **scalar** zone-edge cutoff is `π√3 ω_C = 5.4414 ω_C` — the value `srs-band-structure.md` §1 measures as the scalar band top and §2 identifies as the first-Bragg / half-wave-line resonance. The **vector / shear** channel's top is a **BRACKET** `[5.4414, 17.0111] ω_C` (§3, PENDING Grant). Frozen: `the band-top coefficient is swept as beta in {5.4414, 17.0111} (the vector bracket of srs-band-structure.md section 3, whose lower end coincides with the scalar pi*sqrt(3)) and every band-edge result is reported for BOTH ends; no single value is preferred and the pending single-scale-vs-stiffness-lifted ruling is neither used nor anticipated`.

**Under grading, the whole band scales with the local speed:**

```
omega_max(r) = beta * omega_C * ( c(r) / c_0 ) = beta * c_0 * S(r)^p / l_node
```

because `ω_link(r) = c_link(r)/ℓ_node` and the entire dispersion is homogeneous of degree 1 in the local link speed. **This is Op14 local-clock modulation applied to a band edge.**

**The REJECTED lumped model, swept as a disclosed robustness variant.** `ω = 2(c/ℓ)|sin(kℓ/2)|` gives `ω_max = 2c/ℓ` and `v_group = c·cos(kℓ/2) = c√(1 − (ωℓ/2c)²) → 0` at the edge. Frozen: `the lumped/tight-binding dispersion is REJECTED as the substrate-native model per srs-band-structure.md section 2 and is nonetheless swept as robustness variant D2, with its band-edge group-velocity collapse included, so that the reported robustness is not conditional on the adjudication going the way canon says it goes`.

### §2.6 The effective barrier `𝒱(r)`, and PLANE-PEAK — DERIVED

Reduce the toroidal radial system `W'' + (2/r + g)W' + [ω²ρ/μ − ℓ(ℓ+1)/r² − g/r]W = 0`, `g ≡ μ'/μ`, to Schrödinger form by `W = Ψ/(r√μ)` (the exact `exp(−½∫P dr)` transformation with `P = 2/r + g`):

```
Psi'' + [ omega^2/v^2 - U(r) ] Psi = 0 ,      U = l(l+1)/r^2 + 2g/r + g^2/4 + g'/2
```

With `μ = G_vac S` and `A = r_sat/r`: `g = A³/(S²r_sat)`, and collecting in `A` (an exact, checkable algebra step, gated as `G-U`):

```
U * r_sat^2  =  l(l+1) A^2  +  A^4/(2 S^2)  -  (3/4) A^6 / S^4
```

The **ω-independent barrier** whose maximum defines the classical turning point (`ω² = v²U`) is

```
V(A)  ==  v^2 U * (r_sat^2/c_0^2)  =  S^{2p} [ l(l+1) A^2 + A^4/(2S^2) - (3/4) A^6/S^4 ]
```

`𝒱 → 0⁺` as `A → 0` (the `ℓ(ℓ+1)A²` centrifugal tail) and `𝒱 → −∞` (RHO-A) or a finite negative constant (RHO-B) as `A → 1`, **so an interior maximum exists on `0 < A < 1` for both branches, at a radius OUTSIDE `r_sat`.** Its location is found numerically per branch and gated. Frozen: `the barrier maximum is located by a bracketed root of dV/dA with a sign-change bracket and a negative second derivative at the root, per branch, and the located A_peak must satisfy 0 < A_peak < 1 strictly; the peak radius r_peak = r_sat/A_peak is reported in units of r_sat and of GM/c^2 so it can be read against the GR photon sphere at 3GM/c^2 without importing it`.

### §2.7 ★ THE TURNING-POINT QUESTION — the condition, both branches, and the chirp law

A ringdown component at angular frequency `ω` propagates at radius `r` iff `ω < ω_max(r) = β ω_C S(r)^p`. Define the **band ratio**

```
eps == omega / (beta * omega_C)              [dimensionless, and TINY for astrophysical ringdowns]
```

Then the **band-edge turning point** is the radius where `S^p = ε`:

```
S_turn = eps^(1/p)  ==>   S_turn(RHO-A) = eps^2 ,     S_turn(RHO-B) = eps^(1/2)
```

The **last-node** cutoff, from `1 - A = theta*l_node/r_sat` and `S^2 = 1-A^2 ~ 2(1-A)`:

```
S_last = sqrt( 2 * theta * l_node / r_sat )
```

**★ THE COMPARISON, AND WHY IT IS MASS-INDEPENDENT.** A ringdown is at the object's own light-crossing frequency, `Ω ≡ ω r_sat/c₀ = O(1)`. Then `ε = Ω c₀ ℓ_node/(β ω_C r_sat c₀/c₀)`, i.e. using `ω_C = c₀/ℓ_node`,

```
eps = Omega * l_node / (beta * r_sat)
S_turn(RHO-B) = sqrt(Omega/beta) * sqrt(l_node/r_sat)
S_last        = sqrt(2*theta)    * sqrt(l_node/r_sat)
S_turn/S_last (RHO-B) = sqrt( Omega / (2*theta*beta) )        <-- INDEPENDENT OF MASS
```

**Both cutoffs scale as `√(ℓ_node/r_sat)`, so their ratio is a pure number built from the frozen `Ω`, `β` and `θ`, at every mass.** Under RHO-A, `S_turn = ε² ≪ S_last` by ~25 orders of magnitude, so the node always wins and the question is moot (and irrelevant, since RHO-A is regulator-free anyway).

**The verdict rule, frozen:**

```
S_turn <  S_last  ==>  NODE-GOVERNED    : the wave reaches the last cell; delay ACHROMATIC
S_turn >  S_last  ==>  BAND-EDGE-GOVERNED: the wave turns at cutoff;      delay CHIRPED
```

**And the chirp law, derived now so it cannot be fitted later.** If band-edge-governed, substituting `S_in = S_turn = ε^{1/p}` into §2.4:

```
Delta_T_return^B(omega) = 2*(r_sat/c_0)*ln(2/S_turn)
                        = (r_sat/c_0) * [ ln( beta*omega_C/omega ) + 2*ln 2 ]        (p = 2)
d(Delta_T)/d(ln omega)  = - r_sat/c_0                                                (p = 2)
```

**— a logarithmic chirp with slope exactly `−r_sat/c₀` per e-fold of frequency, independent of `β` and of the mass-to-radius conversion.** Frozen: `if BIN-DB-BAND fires, the reported chirp law is dT/d(ln omega) = -(r_sat/c_0)*(2/p) evaluated at the branch exponent, i.e. -r_sat/c_0 exactly for RHO-B, and this slope is a DERIVED prediction available at freeze rather than a fit to the computed curve`.

### §2.8 The discrete-vs-continuum correction, derived at freeze

Near the wall under RHO-B the excess integrand is `1/v ≈ r_sat/(2c₀x)`, so the node sum is a harmonic sum:

```
SUM_{n=1..N} l/v(n*l) = (r_sat/2c_0) * SUM 1/n = (r_sat/2c_0) * [ ln N + gamma + O(1/N) ]
INT_{l}^{N*l} dx/v     = (r_sat/2c_0) * ln N
```

**so the regulated node sum EXCEEDS the continuum integral cut at the same radius by exactly `γ` (Euler–Mascheroni) per one-way pass, to leading order** — a bounded, calculable `O(1)` constant on a total of order `ln(r_sat/ℓ_node)`. Frozen: `the discrete-sum-minus-continuum-integral difference under RHO-B is derived at freeze to be the Euler-Mascheroni constant gamma per one-way pass at theta = 1 (and gamma + 2 ln 2 at theta = 1/2), it is measured by regulator variant R5, and a measured value differing from the derived one by more than 1 per cent is a G-DISC failure`.

---

## §3 — IMPORT LEDGER (every number the instrument consumes, tagged; `substrate-first-for-numbers`)

| # | Input | Value / form | Class | Source (verified two-method at this freeze) |
|---|---|---|---|---|
| **J1** | Saturation-wall radius | `r_sat = 7GM/c²`, `x_sat = 7` | **`[canon]`** — form-derived, **VALUE rides GR-imported `ν_vac = 2/7`** | `ave-bh-horizon-area-theorem.md:20`; `vol3/claim-quality.md:121` |
| **J2** | Saturation-amplitude profile | `A(r) = ε₁₁(r) = r_sat/r`, `ε_yield = 1` | **`[canon]`** | `electron-bh-isomorphism.md:19`; `ch15/index.md:17` |
| **J3** | Ax-4 kernel | `S(A) = (1 − A²)^{1/2}` | **`[canon]` — Axiom 4** | `saturating-modulus-and-backreaction.md:52` |
| **J4** | Shear-modulus grading | `μ(r) = G_vac·S` | **`[canon, μ-primary]`** | `saturating-modulus-and-backreaction.md:56–60` |
| **J5 ★** | Shear inertia — **THE FORK** | `ρ = ρ_bulk` (RHO-A) vs `ρ_eff = ρ_bulk/S³` (RHO-B) | **`[canon, FORKED — FORK-3(b), OPEN]`** | `:73` and `interior-singularity-resolution.md:19` (RHO-B); `three-channel-impedances.md:21` (RHO-A) |
| **J6 ★** | **Node spacing — THE REGULATOR** | `ℓ_node = ħ/(m_e c)`, imported read-only from `ave.core.constants.L_NODE` | **`[IMPORTED-VALUE / DEFINITIONAL]`** — the reduced Compton wavelength; rides CODATA `ħ`, `m_e`, `c`. **NOT substrate-derived.** | `src/ave/core/constants.py:293` |
| **J7 ★** | Band-top coefficient | `β ∈ {5.4414, 17.0111}` in units of `ω_C` — the **vector/shear** bracket | **`[canon, BRACKET OPEN — swept, not chosen]`** | `srs-band-structure.md` §3 (`clm-bnd5rq`); lower end = scalar `π√3` of §1 |
| **J8** | Node cutoff frequency | `ω_C = c₀/ℓ_node`, imported read-only from `ave.core.constants.OMEGA_C` | **`[canon IDENTITY]`** | `src/ave/core/constants.py:305` |
| **J9** | Network-velocity factor | `c_link = √3 c₀` (`1/√3` projection) | **`[canon, Class-B geometric MANIFESTATION]`** | `boundary-observables-m-q-j.md:106`; `chiral_lattice_dynamics.py` `ANALYTIC_NETWORK_FACTOR` |
| **J10 ★** | Substrate-native ringdown frequency | `Ω_v24 = Re(Ω)` read **PROGRAMMATICALLY** from `research/drivers/coldq_pole_v2p4_root_results.json` `certified_root/Omega_re` | **`[IN-REPO CERTIFIED PRIOR-LANE RESULT — a frequency SCALE, never a tolerance or a bin boundary]`** | v2.4 shipped JSON |
| **J11** | Ringdown damping-time comparator | `τ_ring = (GM/c³)/(ω_I M_g)`, `ω_I M_g` read **PROGRAMMATICALLY** from the same JSON `adjudication/omega_I_M_g` | **`[IN-REPO CERTIFIED — used as a RESOLUTION SCALE only]`** | v2.4 shipped JSON |
| **J12** | GR comparator frequency | `ω_R M_g`, `Q_GR` read **PROGRAMMATICALLY** from the same JSON `comparators/` | **`[GR-IMPORTED comparator]`** | v2.4 shipped JSON |
| **J13** | Observational echo-spacing pointer | the Abedi–Dykaar–Afshordi retrospective spacing, cited as an **in-repo POINTER** | **`[EXTERNAL OBSERVATIONAL POINTER — cited, not analysed, not fitted]`** | `existing-experimental-signatures.md:42`, as consumed by `bh_shear_echo_delay.py` |
| **J14** | Masses | `G`, `M_SUN`, `c₀` imported read-only from `ave.core.constants`; mass grid `M/M_⊙ ∈ {1, 10, 62, 100}` with `M_ref = 62 M_⊙` | **`[CODATA/IAU INPUTS + ENGINEERING GRID]`** — `62` is the corpus remnant mass used by the predecessor driver | `constants.py`; `bh_shear_echo_delay.py` |
| **J15** | Angular index | `ℓ = 2` | **`[INPUT, not derived]`** | §1.3 Y1 |
| **J16** | Instrument numerics | `θ`, `N_split`, mpmath `dps`, quadrature tolerances, the regulator-variant set | **`[ENGINEERING CHOICE — tagged, frozen in §4]`** | this lane |

**R8 audit rule (frozen).** `every number the instrument consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no Regge-Wheeler potential, no Zerilli potential, no tortoise coordinate imported from GR, no Planck length and no ECO wall-offset parameter is used as an input, a seed, a comparator or a check`.

**★ Ledger discipline note, stated at freeze.** `J10`, `J11` and `J12` are prior-lane values used ONLY as frequency and time SCALES. Frozen: `no gate tolerance and no bin boundary in this lane is set from any prior-lane MEASURED value; the tolerances are derived in section 4.5 from the arithmetic of the method and the bin boundaries are derived in section 7 from the structure of the delay law`.

---

## §4 — THE METHOD AND ITS FROZEN NUMERICS

### §4.1 The method (frozen)

1. Build `v(r) = c₀ S(A(r))^p` for `p ∈ {1/2 (RHO-A), 2 (RHO-B), 3 (SYNTHETIC, self-test only)}`.
2. **Closed forms first.** Evaluate `𝒥(p) = 1 − √π Γ(1−p/2)/Γ((1−p)/2)` in mpmath for RHO-A; evaluate `artanh(A_in)` in mpmath for RHO-B. Cross-check each against high-precision quadrature of the same integrand (`G-JA`, `G-CF`).
3. **Then the regulated node sum.** `T = Σ_{n=1..N_split} ℓ_node·f(r_n) + ∫_{r_{N_split}+ℓ_node/2}^{∞} f dr` with `f = (1/v − 1/c₀)`, the tail evaluated by the exact antiderivative (RHO-B) or high-precision quadrature (RHO-A). Split-independence gated (`G-SUM`).
4. **Turning point.** Compute `S_turn = ε^{1/p}` and `S_last = √(2θ ℓ_node/r_sat)` per branch, per `β`, per `θ`, per mass; evaluate the frozen verdict rule of §2.7.
5. **Barrier peak.** Bracket and solve `d𝒱/dA = 0` per branch; gate the bracket, the sign change and the second derivative (`G-PEAK`).
6. **Regulator sweep.** Recompute `T` under every variant of §4.4 and report the full spread.
7. **Self-tests.** Run every mutation of §6 and record whether each fires.
8. Ship one JSON; run twice; compare digests.

**No engine file is touched.** Frozen: `src/ave is byte-untouched by this lane; ave.core.constants and the predecessor driver are imported read-only`.

### §4.2 Frozen numerics

| symbol | value | role |
|---|---|---|
| `p` | `{0.5, 2.0}` primary; `3.0` synthetic self-test only | branch exponent |
| `theta` | `{1.0, 0.5}` | sub-cell placement of the innermost node |
| `beta` | `{5.4414, 17.0111}` | band-top coefficient in `ω_C`, both bracket ends (J7) |
| `N_split` | `{1e5, 1e6, 1e7}`, primary `1e6` | exact-sum / integral-tail split |
| `dps` | `50` | mpmath working precision |
| `quad tol` | `1e-30` | mpmath quadrature target |
| mass grid | `M/M_⊙ ∈ {1, 10, 62, 100}`, `M_ref = 62` | reporting grid |
| `ell` | `2` | multipole (barrier only) |
| `A_peak bracket` | `(0.05, 0.999)` | barrier-peak search bracket |

### §4.3 The configuration matrix — frozen, with roles named in advance

| tag | branch | role |
|---|---|---|
| `CFG-A` | RHO-A (`p = 1/2`) | **primary + NEGATIVE CONTROL** against the 2026-06-17 predecessor driver |
| `CFG-B` | RHO-B (`p = 2`) | **primary** — the regulated log delay |
| `CFG-SYN` | synthetic (`p = 3`) | **self-test only** — a power-law-divergent profile that must drive `BIN-CUTOFF` into firing (`FT-CUT`). **No physics is claimed for it and it appears in no bin.** |

**Stop rule, frozen:** `if CFG-A fails G-NC against the 2026-06-17 predecessor driver, the lane STOPS and reports no RHO-B delay at all`.

### §4.4 ★ THE REGULATOR VARIANT SET — frozen BEFORE any number, because BIN-CUTOFF is decided on it

| id | variant | what it perturbs |
|---|---|---|
| **R1** | innermost node at `r_sat + ℓ_node` (`θ = 1`) | **the primary** |
| **R2** | innermost node at `r_sat + ℓ_node/2` (`θ = 1/2`) | sub-cell placement |
| **R3** | innermost radius at the band-edge turning point `S = S_turn` | the ω-dependent cutoff, both `β` ends |
| **R4** | node spacing **strained**: `ℓ_node·(1 + ε₁₁)` , so the innermost node sits at the correspondingly larger offset | whether the lattice pitch itself is graded — an **OPEN constitutive question this lane does not settle** |
| **R5** | continuum integral cut at R1's radius (no discrete sum) | isolates the discrete-vs-continuum `γ` correction of §2.8 |
| **D2** | the REJECTED lumped dispersion `ω = 2(c/ℓ)sin(kℓ/2)`, with its band-edge group-velocity collapse `v_g = c cos(kℓ/2)` | whether the robustness survives the model adjudication going the other way |

Frozen: `BIN-CUTOFF is decided on the FULL SPREAD of T_return over the variant set {R1, R2, R3, R4, R5, D2} at the reference mass, and no variant may be dropped, re-weighted or excluded after a number is seen`.

### §4.5 ★ WHERE EVERY TOLERANCE COMES FROM — derived, with ZERO pre-freeze computation on this instrument

| gate | tolerance | derivation of the number |
|---|---|---|
| `G-NC` | `1e-10` relative | the predecessor driver uses `scipy.integrate.quad` at default tolerance on an integrable-singular integrand; `1e-10` is comfortably above `quad`'s realistic relative accuracy there and comfortably below any physical difference |
| `G-JA` | `1e-20` | mpmath at `dps = 50` against an exact Gamma-function form: 30 digits of headroom |
| `G-CF` | `1e-25` | `artanh` is elementary and exact in mpmath; the comparison is against quadrature of the same integrand at `1e-30` target |
| `G-SUM` | `1e-12` relative | the midpoint-rule error of the integral tail is `O(ℓ²f''/24)` summed `= O((ℓ/x_split)²)`; at the coarsest frozen `N_split = 1e5` that is `~1e-10` of the near-wall contribution and far smaller as a fraction of the total, so `1e-12` on the **split-to-split difference** is a genuine test rather than a formality |
| `G-U` | `1e-30` | a symbolic algebra identity checked at 12 random `A` values in mpmath; a true identity holds to working precision |
| `G-DISP` | `1e-15` | `arccos(cos x) − x` is exact in floating point on `[0, π]` up to rounding |
| `G-PEAK` | bracket + sign change + `d²𝒱/dA² < 0` | boolean structural conditions, no tolerance to size |
| `G-DECADE` | `1e-6` relative | each decade of `S` must contribute `ln 10 · (r_sat/c₀)` exactly under the log law; deviations are `O(S²)` |
| `G-DISC` | `1 %` | §2.8 derives the discrete-vs-continuum offset as `γ` (or `γ + 2ln2`); the derivation is leading-order in `ℓ/r_sat ~ 1e-17`, so 1 % is 15 orders of headroom |
| `G-CANON` | exact equality | `ℓ_node`, `ω_C`, `G`, `c₀`, `M_SUN` must be the imported symbols, checked by recomputing `ω_C·ℓ_node = c₀` and `ℓ_node = ħ/(m_ec)` to machine precision |

### §4.6 Determinism

Frozen: `the driver is run twice end-to-end and the shipped JSON must be byte-identical apart from _runtime_sec; the driver emits NO pass field for the determinism gate — it ships the digest only, and the verdict is obtained solely by the external two-run diff recorded in the result doc; _runtime_sec is machine-dependent and is written WITHOUT back-ticks and is NOT registered in the number check`.

---

## §5 — THE GATES (frozen; an UNRUN gate is NOT a passed gate)

| gate | what it certifies | frozen tolerance |
|---|---|---|
| **G-NC** ★ | **NEGATIVE CONTROL** — this lane's RHO-A total (non-excess) delay `2∫_{r_sat}^{r_out} dr/c_shear` reproduces the 2026-06-17 predecessor driver's value at the SAME `r_out/r_sat` and the SAME mass, for every entry of the predecessor's own `r_out` table | `1e-10` relative, every entry |
| **G-JA** | the RHO-A closed form `𝒥_A = 1 − √π Γ(3/4)/Γ(1/4)` equals high-precision quadrature of its own integrand | `1e-20` |
| **G-CF** | the RHO-B closed form `artanh(A_in) − artanh(A_out)` equals high-precision quadrature of its own integrand | `1e-25` |
| **G-SUM** | node-sum split-independence across `N_split ∈ {1e5, 1e6, 1e7}` | `1e-12` relative |
| **G-U** | the collected `U·r_sat² = ℓ(ℓ+1)A² + A⁴/(2S²) − (3/4)A⁶/S⁴` equals the un-collected `ℓ(ℓ+1)/r² + 2g/r + g²/4 + g′/2` at 12 sampled `A` | `1e-30` |
| **G-DISP** | the substrate-native arccos map on the `z = 2` radial cascade is exactly linear: `ω_link·arccos(cos kℓ) = c_link k` on `[0, π]` | `1e-15` |
| **G-PEAK** | the barrier maximum is bracketed, `d𝒱/dA` changes sign across the bracket, `d²𝒱/dA² < 0` at the root, and `0 < A_peak < 1` strictly, per branch | booleans |
| **G-DECADE** | under RHO-B each decade of `S` inside the near-wall region contributes `ln 10 · (r_sat/c₀)` to the one-way delay | `1e-6` relative |
| **G-DISC** | the measured discrete-minus-continuum offset (variant R5 vs R1) equals the derived `γ` at `θ = 1` and `γ + 2 ln 2` at `θ = 1/2` | `1 %` |
| **G-CANON** | every canonical constant is the imported symbol: `ω_C·ℓ_node = c₀` and `ℓ_node·m_e·c₀ = ħ` to machine precision, and `x_sat = 7` matches the v2.4 shipped `_frozen_numerics/x_sat` | machine precision / exact |

**Frozen:** `a gate that was never run cannot be counted as passed; the result doc must publish a RUN / N-A-BY-CONSTRUCTION / N-A-BY-OUTCOME / UNRUN-BY-OMISSION table per configuration`.

---

## §6 — THE FIREABILITY SELF-TESTS (each MUST fire; a gate that cannot fail is not a gate)

| self-test | mutation | must fire when |
|---|---|---|
| **FT-NC** ★ | scale the predecessor comparison target by `1 + 1e-6` | `G-NC` fails, separation `≥ 1e-7` |
| **FT-JA** | replace `Γ(3/4)/Γ(1/4)` by `Γ(3/4)/Γ(1/4)·(1+1e-9)` | `G-JA` fails, separation `≥ 1e-10` |
| **FT-CF** | replace `artanh(A)` by `artanh(A)·(1+1e-12)` | `G-CF` fails, separation `≥ 1e-13` |
| **FT-SUM** | drop the integral tail entirely at `N_split = 1e5` | `G-SUM` fails, relative separation `≥ 1e-3` |
| **FT-U** | drop the `g²/4` term from the un-collected `U` | `G-U` fails, separation `≥ 1e-6` |
| **FT-DISP** ★ | substitute the REJECTED lumped map `ω = 2(c/ℓ)sin(kℓ/2)` | `G-DISP` fails, max deviation `≥ 1e-2` — **this is the receipt that the model adjudication is load-bearing and not decorative** |
| **FT-PEAK** | evaluate `d𝒱/dA` at `A_peak·(1 + 0.01)` and require it to be non-zero | separation from zero `≥ 1e-4` |
| **FT-DECADE** | evaluate the decade contribution under the RHO-A profile, where no log law holds | `G-DECADE` fails, relative separation `≥ 0.1` |
| **FT-CUT** ★★ | run the **whole regulator sweep on `CFG-SYN` (`p = 3`)**, whose continuum integral diverges as `S^{-2}` | the regulator spread on `CFG-SYN` exceeds `10 %`, i.e. **`BIN-CUTOFF` is demonstrated REACHABLE every run** |
| **FT-EVAN** ★ | multiply `ω` by `1e20` at the reference mass | `BIN-EVAN` fires — **the evanescence bin is demonstrated REACHABLE every run** |
| **FT-TURN** ★ | multiply `ω` by `1e12` at the reference mass | `S_turn > S_last`, i.e. **`BIN-DB-BAND` is demonstrated REACHABLE every run** |
| **FT-CANON** | replace `ℓ_node` by `ℓ_node·(1 + 1e-12)` | `G-CANON` fails |

**Frozen:** `every self-test above MUST fire; if any self-test fails to fire, the affected configuration is DELAY-NOT-CERTIFIED, NO threshold is retuned, and the physics bins for that configuration are reported N/A - NOT ADJUDICATED, exactly as the axial lane did on 2026-08-04`.

---

## §7 — THE OUTCOME CLASSES (frozen; exhaustive; each reachable)

**PRECEDENCE (frozen, evaluated in this order).** `BIN-EVAN` > `BIN-CUTOFF` > `BIN-DA` / `BIN-DB` > `BIN-DISC` / `BIN-DEGEN`. If an earlier bin fires, the later ones are reported `N/A — not adjudicated` and **no verdict language is used about them**. Certification (`DELAY-CERTIFIED` / `DELAY-NOT-CERTIFIED`) is stated **per configuration** and gates every physics bin: **a `DELAY-NOT-CERTIFIED` configuration adjudicates no bin.**

### §7.0 The certification bin

| bin | condition | disposition |
|---|---|---|
| **`BIN-CERT-FAIL`** | `any RUN gate FAILS, or any self-test fails to fire, or any gate is UNRUN by omission, for that configuration` | **`DELAY-NOT-CERTIFIED`** for that configuration. Numbers reported as diagnostics; no physics bin adjudicated; **no threshold retuned**; routes to a successor with a new version number. |
| **`BIN-STOP`** | `CFG-A fails G-NC against the 2026-06-17 predecessor driver` | **THE LANE STOPS.** No RHO-B delay is produced at all. |

### §7.1 `BIN-EVAN` — is the ringdown band evanescent over the whole graded region?

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-EVAN-FIRES`** | `omega > omega_max(r) = beta*omega_C*S(r)^p at EVERY radius in [r_sat + l_node, 1e6*r_sat] at the reference mass, for that branch and that beta` |
| **`BIN-EVAN-CLEAR`** | `there exists a radius at which omega < omega_max(r), and the reported margin is min over the graded region of omega_max(r)/omega` |

**Frozen disposition:** `if BIN-EVAN-FIRES for a branch, that branch predicts NO return in the ringdown band at all — the graded region is a cut-off filter end to end — and the delay laws for that branch are reported as N/A rather than as numbers; this is an HONEST NEGATIVE for that branch's echo claim and must be headlined as such`.

### §7.2 `BIN-CUTOFF` — is the answer regulator-dominated?

`spread ≡ (max − min) / median` of `T_return` over the full variant set `{R1, R2, R3, R4, R5, D2}` of §4.4, per branch, at the reference mass.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-CUTOFF-ARTIFACT`** | `spread > 0.10` |
| **`BIN-CUTOFF-ROBUST`** | `spread <= 0.10` |

**Frozen disposition:** `if BIN-CUTOFF-ARTIFACT fires for a branch, the parameter-free claim on that branch's delay DIES, the number is ARTIFACT-class, and the result doc must say so in its headline rather than in a footnote; the threshold 0.10 is the point at which the regulator ambiguity exceeds the leading digit of the answer, it is frozen here before any number exists, and FT-CUT demonstrates every run that the bin CAN fire by exhibiting a profile (p = 3) on which it does`.

### §7.3 `BIN-DA` — the RHO-A prompt-reflection delay

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-DA-CLOSED`** | `the RHO-A regulated node sum agrees with 2*(r_sat/c_0)*J_A, J_A = 1 - sqrt(pi)*Gamma(3/4)/Gamma(1/4), to better than 1e-6 relative at EVERY mass on the frozen grid, AND the regulator spread on CFG-A is below 1e-6` |
| **`BIN-DA-OPEN`** | `either agreement fails` |

**Frozen reporting requirement:** `BIN-DA-CLOSED means the RHO-A return is PROMPT, ACHROMATIC and REGULATOR-FREE, with the delay a fixed pure multiple of r_sat/c_0; the result doc must report that multiple, its SI-second value on the mass grid, and the explicit statement that the 2026-06-17 predecessor's 3-10 ms BAND is the free-flight term of an undeclared plane and NOT an uncertainty in the substrate prediction`.

### §7.4 `BIN-DB` — the RHO-B log-delayed return, and whether it CHIRPS

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-DB-NODE`** | `S_turn < S_last for BOTH beta ends, BOTH theta values and EVERY mass on the frozen grid` ⇒ **node-governed; delay ACHROMATIC**; the reported law is `T_return^B = (r_sat/c_0)*ln(2*r_sat/(theta*l_node)) + K_disc*(r_sat/c_0)` with `K_disc` measured |
| **`BIN-DB-BAND`** | `S_turn > S_last for BOTH beta ends, BOTH theta values and EVERY mass on the frozen grid` ⇒ **band-edge-governed; delay CHIRPED**; the reported law is `T_return^B(omega) = (r_sat/c_0)*[ln(beta*omega_C/omega) + 2*ln 2]` with slope `dT/d(ln omega) = -r_sat/c_0` |
| **`BIN-DB-SPLIT`** | `the verdict differs across the beta bracket, across theta, or across the mass grid` ⇒ **the turning-point question is NOT settled by this lane**; both laws reported, neither preferred, and the split is routed as an open item |

**Frozen reporting requirement:** `the BIN-DB verdict must be reported together with the measured ratio S_turn/S_last at every sweep point, because a verdict that holds by a factor of two is reported as holding by a factor of two and not as a clean separation`.

### §7.5 `BIN-DISC` / `BIN-DEGEN` — are the two branches distinguishable by timing?

`tau_ring(M) = (G*M/c_0^3) / (omega_I_M_g)` with `omega_I_M_g` read **PROGRAMMATICALLY** from the v2.4 shipped JSON (`J11`) — the substrate-native ringdown damping time, used as the **resolution scale** because two bursts separated by less than one damping time overlap and are not separately resolvable.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-DISC`** | `abs(T_return^B - T_return^A) > tau_ring(M) at EVERY mass on the frozen grid` |
| **`BIN-DEGEN`** | `abs(T_return^B - T_return^A) <= tau_ring(M) at EVERY mass on the frozen grid` |
| **`BIN-DISC-SPLIT`** | `the comparison changes sign across the mass grid` |

**Frozen disposition:** `BIN-DEGEN is an HONEST NEGATIVE and is recorded as one: it would mean FORK-3(b) is NOT echo-discriminable by timing and the timing route to the fork is CLOSED, which is a good outcome and must be written as a clean result rather than as a disappointment`.

**Frozen, and mandatory in the headline whatever the verdict:** `the RHO-B log-delay law T ~ (r_sat/c_0)*ln(r_sat/l_node) is STRUCTURALLY DEGENERATE with the standard ECO / near-horizon-firewall echo law Dt ~ (2 r_s/c)*abs(ln(delta/r_s)); the two differ only in the prefactor and in what sets the cutoff length, so a detected log-form echo delay does NOT by itself select AVE, and the ONLY discriminating content is that AVE's cutoff length l_node is FIXED where the ECO delta is a free knob; this degeneracy is declared at freeze, is not a discovery of the run, and must be stated in the result headline`.

**★ And the corpus statement this collides with, surfaced at freeze rather than at result time.** The 2026-06-17 predecessor's `ave-discrimination-check` reads, verbatim, *"**AVE has no such knob:** its reflector is at the *fixed, parameter-free* radius `r_sat = 7GM/c²`, **outside** `r_s`, with no log-divergence"* (`research/2026-06-17_bh-shear-echo-forward-prereg.md:73`), and the KB banner at `existing-experimental-signatures.md:42` repeats it. Frozen: `that sentence is RHO-A-conditional: under RHO-B the AVE delay IS log-divergent in the continuum and log-enhanced on the lattice, so the predecessor's no-log-divergence discriminator does NOT hold on the RHO-B branch of the open fork; this collision is SURFACED with both file:line pointers and both verbatim quotes, is REPAIRED NOWHERE, and no edit to either document is proposed by this lane`.

### §7.5b — The observational-pointer DIAGNOSTIC (declared at freeze; NOT a bin, NOT a verdict)

**Because the collision above is foreseeable at freeze, the comparison it invites is frozen HERE so that it cannot be constructed post-hoc.** The result doc reports, as a **DIAGNOSTIC**, the ratio of each branch's `T_return` at the reference mass to the in-repo Abedi–Dykaar–Afshordi retrospective spacing pointer (`J13`, `existing-experimental-signatures.md:42`/`:44`), read as a **cited context number and nothing else**.

Frozen: `the observational-pointer ratio is a DIAGNOSTIC and not a bin; no sub-bin, no threshold and no adjudication of any kind attaches to it; a smaller ratio on one branch is NOT evidence for that branch, is NOT a detection, is NOT a validation, and the result doc must carry the sentence that the ~0.29 s spacing is a CONTESTED RETROSPECTIVE re-analysis of somebody else's data, is not an exp- node, and cannot strengthen any AVE claim; the FLAG-ECO degeneracy applies to this diagnostic in full, since any log-form model can be brought to any delay by moving its cutoff length`.

### §7.6 Reachability audit (frozen)

- `BIN-STOP` is reachable: the predecessor comparison either reproduces at `1e-10` or it does not.
- `BIN-CERT-FAIL` is reachable and is **demonstrated reachable every run**: every self-test drives an actual gate into its failing state.
- `BIN-EVAN` is reachable and is **demonstrated reachable every run** by `FT-EVAN`.
- `BIN-CUTOFF-ARTIFACT` is reachable and is **demonstrated reachable every run** by `FT-CUT` on `CFG-SYN`.
- `BIN-DA-OPEN` is reachable: it is a numerical agreement that either holds or does not.
- `BIN-DB-BAND` is reachable and is **demonstrated reachable every run** by `FT-TURN`.
- `BIN-DB-SPLIT` is reachable: the sweep has 16 points per branch and they need not agree.
- `BIN-DISC` / `BIN-DEGEN` / `BIN-DISC-SPLIT` partition the axis with no gaps and no overlaps.
- **No outcome requires a criterion to be relaxed after the fact.**

### §7.7 ★ PREDICTABILITY DISCLOSURE — what this lane knows in advance, stated without flattery

**This lane's derivation is ANALYTIC, so most of its bin outcomes are determined at freeze. That is disclosed here in full rather than discovered in the result.**

- **Known at freeze, as THEOREMS of §2:** the RHO-A delay is finite, achromatic and regulator-free; the RHO-B delay is logarithmic; the RHO-B regulator dependence enters only through `ln(2/S_in)` and is therefore compressed; the group and phase velocities coincide under the adjudicated dispersion; an effective-barrier maximum exists outside `r_sat` on both branches; the chirp slope, IF band-governed, is `−r_sat/c₀`.
- **★ Evaluated BY HAND at freeze and DISCLOSED so the run is read as a check and not as a discovery:** the turning-point verdict follows from the closed-form ratio `S_turn/S_last = √(Ω/(2θβ))`, which contains **no mass**; substituting the frozen `Ω` scale and the frozen `β`, `θ` sets by hand indicates **`BIN-DB-NODE`** at every sweep point. **The result doc must present the turning-point verdict as a CONFIRMED DERIVATION, not as a measurement.** Likewise the order of magnitude of the RHO-B delay is hand-foreseeable from `ln(2r_sat/ℓ_node)`, and the result doc may not present its order as a surprise.
- **NOT known at freeze, and these are the only outputs this lane may present as measurements:** the exact value of `𝒥_A`; the measured discrete-vs-continuum constant `K_disc`; the measured regulator spread and therefore the `BIN-CUTOFF` verdict; the barrier-peak radii; whether `G-NC` reproduces the predecessor; whether every self-test fires; and — **the genuinely open one** — whether `|T_B − T_A|` clears `τ_ring` at every mass, i.e. `BIN-DISC` vs `BIN-DEGEN`.

Frozen: `the derived statements of section 2 and the hand-evaluated turning-point verdict are available before the run and may NOT be presented in the result doc as discoveries of the instrument; only the quantities enumerated in the third bullet of section 7.7 may be presented as measurements`.

---

## §8 — WHAT TRANSFERS, AND WHAT MUST BE RE-EARNED

**Transfers into this lane:** the Ax-4 kernel; the `A = r_sat/r` profile; the `μ = G_vac S` grading; both inertia readings as a declared fork; the arccos band model and its `1/√3` calibration; `ℓ_node` and `ω_C` as imported constants; v2.4's certified root as a frequency scale.

**Must be re-earned by a successor and is NOT established here:** any reflectivity or transmission coefficient at the barrier (hence any echo AMPLITUDE or TRAIN); the tunnelling correction through a few-cell evanescent skin (the §0.2 plumber question); the 3D-srs correction to the 1D radial cascade; whether the lattice pitch is itself strained (variant R4 sweeps it, nothing settles it); the single-scale-vs-stiffness-lifted band-top ruling; and any observational comparison beyond citing an in-repo pointer.

---

## §9 — FLAG-DON'T-FIX: what is raised at freeze and routed, not resolved

1. **★ `FLAG-ECO` — the log-delay form is shared with ECO models.** Declared in §7.5, mandatory in the headline. Routed to the discrimination lane, not resolved here.
2. **★ `FLAG-PLANE-GAP` — the 2026-06-17 predecessor's outer-reflector survey is incomplete.** It surveyed only imported GR radii and concluded no parameter-free outer reflector exists outside `r_sat`; §2.6 derives one from the profile itself. **Surfaced with the verbatim predecessor sentence and its line, repaired nowhere, and no edit to that frozen document is proposed.**
3. **★ `FLAG-CITE-SHIFT` — a stale line cite found while verifying.** `srs-band-structure.md` §6 cites `constants.py:294` for `OMEGA_C`; at `origin/main` `2877eaa0` `OMEGA_C` is defined at `constants.py:305` and `:294` is a comment line. **Pure line-shift class, correct-when-written presumed, NOT repaired by this lane** (KB edits are outside the scope fence). Routed to the auditor lane.
4. **`FLAG-PITCH` — is the lattice pitch itself graded by `ε₁₁`?** Canon writes the strain as a field on the `r` coordinate and does not say whether the node spacing inherits it. **Variant R4 sweeps both readings; neither is preferred and the constitutive question is left open.**
5. **`FLAG-CAUSAL` carried forward from the axial lane, NOT re-asked and NOT answered.** This lane makes the electrical length finite and calculable; whether that termination is a port or a mirror is still Grant's.
6. **`FLAG-CANON` carried forward, untouched.** The `Z_shear` sign tension at `vol3/claim-quality.md:122`/`:124` and the RHO-A-conditionality of `:123`'s *"echoes are predicted"* are cited by pointer only. **No edit is proposed and the claim-quality repair is explicitly not this lane's.**
7. **`FLAG-BRACKET` — the vector band top is a bracket pending Grant.** Swept, not resolved.

---

## §10 — VALIDATION REQUIREMENTS (frozen)

- **`make verify` passes** in the worktree before every commit.
- **Gating number check.** A `research/drivers/echo_delay_regulated_sum_number_check.py` implementing, from the first commit, all six accumulated checker lessons: **(i)** a minimum significant-digits floor of 3 enforced at BOTH the configuration and document ends; **(ii)** PER-SITE rather than global dedup; **(iii)** list-valued registration; **(iv)** a newline-excluding token pattern; **(v)** a completeness guard making any registered key the document never exercises a hard FAIL; **(vi)** a digest classifier. **And one addition this lane makes:** **(vii)** a **MUTATION RECEIPT** — a `--mutation-receipt` mode that perturbs a registered value and asserts the checker returns non-zero, so the checker itself is demonstrated fireable. Frozen: `the gating number check scans the RESULT DOC only; no claim is made anywhere in this lane that this prereg is machine-checked; the checker ships a mutation receipt demonstrating that it can FAIL`.
- **Makefile target** `verify-echo-delay-number-check`, appended as its OWN target and wired into `verify`; no other lane's recipe is edited.
- **Determinism** per §4.6.
- **Engine fence.** `src/ave` byte-untouched, discharged by an empty `git diff --stat`.
- **Predecessor fence** per §P.1, discharged by an empty `git diff --stat` on each named file.
- **Docket fragment** `_orchestration/docket-entries/2026-08-04-echo-delay-regulated-sum.md`, exactly one.
- **PR** titled `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.

---

> **Freeze statement.** `no gate, tolerance, band, frozen numeric parameter, bin boundary, regulator variant or method element in sections 2, 4, 5, 6 and 7 may be changed after any gate result is seen; if a configuration fails certification this lane reports DELAY-NOT-CERTIFIED for that configuration, adjudicates NO physics bin for it, and routes to a successor with a new version number`.
