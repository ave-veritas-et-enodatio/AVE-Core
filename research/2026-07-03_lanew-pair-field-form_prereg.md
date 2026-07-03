# FROZEN PRE-REG — LANE W: the pair-field FORM test (massless channel)

**Status:** FROZEN pending orchestrator review. Committed BEFORE the decisive pair-runs driver (Chern-arc / standing-gate discipline). Validation + controls may run; the DECISIVE dynamical pair runs fire only after orchestrator review.
**Fired:** Grant 2026-07-03 (*"fire!"*). **Branch:** `analysis/lanew-pair-field-form` (off `origin/main` @ `96b5f82e`). NO self-merge — push + PR REVIEW:pending-orchestrator.
**Epic:** EM-readout derivation — the LAST live lane. **Lane W** (winding pairs), the FORM question (the robustness-ladder's winning end).
**THE QUESTION:** does the massless-channel field between two winding solitons carry the **COULOMB FORM** (unscreened 1/r-class interaction), mediated by the A44 gyrotropic neutral texture — or the MULTIPOLE FORM (dipole/quadrupole, 1/r³-or-steeper) that a globally-neutral compact texture generically gives?

**Built on (verify-before-cite, all re-read at HEAD `96b5f82e` this session):**
- `research/2026-07-03_jcoupling-divergence-derivation_note.md` (PR #488, MERGED) — the β arc: the A44 gyrotropic converter (`f_V = −κ̃·g·Ω_w`, `Ω_w=(∇×w)·x̂`) sources a GLOBALLY-NEUTRAL local charge texture around a single winding (`sum ρ = 0` exact, Gauss-no-boundary; `Q(r)` rises to ±0.6 then returns to 0 — a polarization/form-factor, NOT a monopole). The mechanism candidate for Lane W.
- `clm-wcoul2` + `research/2026-07-03_writhe-campaign-linear-channel_result.md` — the pair force in the GAPPED ω channel is Yukawa-screened (ξ≈0.548 cells, a host knob) with Coulomb SIGN structure (like-repel/unlike-attract). The MASSLESS-channel FORM is what Lane W opens.
- `research/2026-07-03_writhe-gate0-pair-feasibility_result.md` — the pair seeding machinery (`_seed_pair`, RR/RL/LL/LR via `mirror_A/mirror_B`) + the stable d-window (d∈{34,44} STABLE; d=24 near-contact UNSTABLE).
- `research/2026-07-03_lanez-fluxoid-step0_note.md` — Z's `[DOORWAY-NO-PINNING]`: net monopoles are closed (the pair/relational formulation is the honest frame; the β note §6 residue).

**Classification (`consistency-vs-emergence`):** the PAIR-COULOMB-FORM bin (if it fired) would be a FORM result, EMERGENCE-adjacent only at the FORM grade (magnitude = echo, never headlined); the MULTIPOLE-FORM bin is the honest charge-FORM negative (CONSISTENCY-with-the-neutral-texture-mechanism). Tagged per-bin (§4). No promotion past what the run shows.

**Disciplines (skill-selection plan, written before scaffolding):** `substrate-native-check` (§0 — the texture is computed from the ω winding carrier's own microrotation, srs/Cosserat-native, not a Cartesian-inserted charge; walked before the first probe) · `phase-space-coordinate-check` (§0.1 — winding label phase-space, separation + interaction real-space, matched) · `consistency-vs-emergence` (per-bin, §4) · `verify-before-cite` (§8 ledger) · `flag-don't-fix` (§2.3 the SCALAR-vs-COVARIANT texture fork surfaced with both exponents; §3.8 the periodic-box exponent-steepening artifact surfaced and fixed with an open Green's-fn pipeline).

---

## 0. Sector header + regime declaration

- **SECTOR.** T2 / Cosserat micro-rotation ω-sector winding, read into the A1/E-sector via the A44 gyrotropic converter (the shear→bulk mode-conversion, `cross_sector_coupling.gyrotropic_converter_forces`, adjudicated A44 as an Axiom-1 non-centrosymmetry consequence). The E-sector charge texture is `ρ = f_V = −κ̃·g·Ω_w` — a bound-charge / vacuum-polarization form-factor around the winding, NOT a net monopole (β note §5.2). **The "charge" is computed ONLY via the A44 form from the ω field — no integer inserted, no point charge planted, Gauss diagnostic-only.**
- **HOST / REGIME.** The S1 isolated-knot host (`_build_isolated_knot`: `CrystalGraftV4`, buckle OFF, photon OFF, lock ON, κ̃=6/5 α-clean). Reused verbatim from Gate-0 + the linear-channel campaign. **The MASSLESS channel** = the A44 texture's Poisson/1-r-class field, which is NOT gapped (unlike the ω-sector Yukawa force of `clm-wcoul2`): the E-sector potential φ solves `∇²φ = −ρ`, a massless (unscreened) Green's function. That is why Lane W is a genuinely DIFFERENT channel from the gapped-ω `clm-wcoul2` force.
- **PHASE-STATE.** For Step-0 (§3): FROZEN seeded (2,3) knots (analytic, no dynamics — the cheapest-decisive form check). For the DECISIVE runs (§5, HELD): seeded quasi-stationary breathing knots evolved under the engine's real `step()`, cold parity-even inter-knot medium, the texture recomputed at each step.

### 0.1 Coordinate declaration (`phase-space-coordinate-check`, A46)
The (2,3) winding label is PHASE-SPACE (ω-tank LC quadrature + toroidal ω-polarization), read per-knot in its native phase-space coords (roll-to-center). The pair separation d, the texture ρ(r), the potential φ(r), and the interaction energy U(d) are all REAL-SPACE (lattice-Cartesian). The winding label and the real-space observables are never cross-compared: the FORM observable (the exponent of U(d)) is a real-space power law, matched to the real-space Poisson field of the real-space texture. The corpus claim being tested — "the massless pair field carries the Coulomb FORM" — is itself a real-space claim (a 1/r interaction), so real-space measurement is the matching-coordinate test (A46 satisfied: this is NOT a phase-space φ² prediction measured in real-space).

---

## 1. THE OUTCOME BINS (frozen — the robustness ladder: EXPONENT primary, sign secondary, magnitude echo)

The **interaction exponent** `p` in `U(d) ~ d^p` (equivalently the force `|F| ~ d^(p−1)`) is the PRIMARY (FORM) observable. Sign structure is SECONDARY. Magnitude is ECHO territory — reported, never headlined (per the robustness ladder's winning end).

- **[PAIR-COULOMB-FORM]** — interaction exponent `p ≈ −1` over the stable d-window, UNSCREENED (no exponential cutoff), with sign structure reproducing `clm-wcoul2`'s like-repel/unlike-attract. **The Coulomb FORM derives in the massless channel.** This is the EMERGENCE-adjacent FORM chord (magnitude still echo). Would require a SURVIVING MONOPOLE moment — which the β note proved is zero (`sum ρ = 0`, Gauss-no-boundary). So this bin fires ONLY if a monopole is restored by something the neutral-texture analysis missed (candidate: the overlap/interpenetration regime, the harmonic/meridian coupling of Z's Δb₁=+1, or a log/1-r form from the 2-complex dimensionality — assessed in §3).
- **[MULTIPOLE-FORM]** — exponent `p ≤ −2.5`-ish (dipole-dipole → `p=−3`; quadrupole-quadrupole → `p=−5`). **The massless pair force is NOT Coulomb.** Book honestly as the charge-FORM negative — no rescue (Rule 11). This is the STEP-0 NULL EXPECTATION (§3): a globally-neutral compact texture interacts at its lowest surviving multipole, which is dipole-or-higher.
- **[SCREENED-MASSLESS]** — an unexpected exponential screening in the massless channel (a Yukawa cutoff where the Poisson field should be unscreened). Structural surprise — surface to Grant (would mean the E-sector is secretly gapped).
- **[BELOW-FLOOR / NO-INTERACTION]** — the massless-channel interaction is below the reliable numerical floor across the whole clean window (no exponent readable). A different negative (the texture couples too weakly to read a form).
- **[STUCK-FRAMING → Grant]** — a fork the analysis cannot settle (e.g. SCALAR-vs-COVARIANT texture-form ambiguity, §2.3, cannot be adjudicated by the substrate alone).

**Adjudication discipline (Rule 11 / no criterion-drop):** the bin is chosen by the exponent read on the CLEAN window (§3.8 overlap + floor bounds), against the LIVENESS-certified pipeline (§3.8). The MULTIPOLE-FORM verdict, if it fires, is booked as the clean charge-FORM negative with the single mechanism (globally-neutral texture ⇒ no monopole ⇒ lowest surviving moment is dipole/quadrupole) named — NOT debugged toward a Coulomb rescue.

---

## 2. THE FORM OBSERVABLE — the massless-channel interaction exponent

### 2.1 The texture (computed ONLY via the A44 form — no inserted charge)

The E-sector charge density around a winding is the A44 gyrotropic converter's `f_V` source (the engine's ACTUAL bulk-acceleration source term, `crystal_engine.py:244`, `crystal_graft_v4._buckle_forces`):

```
ρ(r) = f_V = −κ̃ · g(A) · Ω_w ,   Ω_w = (∇×ω)·n̂ ,  n̂ = x̂ (photon propagation axis)
```

with `g(A)` the saturation-front window (`saturation_front_window`, thin shell at A≈R_II) on the strain amplitude `A` built from the winding's own microrotation energy `|ω|²` (the S1 buckle-OFF host has no live director `w`; the winding's own ω is the rotational field the converter curls — consistent with the β note's `curl_adj(ω)`). `κ̃ = 6/5` is α-free (verified: α absent from the texture path). **No Q_link integer, no planted point charge, no inserted monopole** — the texture is the pure A44 form of the ω field. Gauss (`sum ρ`) is DIAGNOSTIC-ONLY (it confirms neutrality, it does not source anything).

### 2.2 The interaction (the massless-channel pair energy)

The massless-channel potential solves `∇²φ_B = −ρ_B` (unscreened Poisson — the E/A1 sector Green's function, NOT the gapped ω Green's function). The two-texture interaction energy is:

```
U(d) = ∫ ρ_A(r) · φ_B(r) d³r          (texture A in the massless potential of texture B)
```

at a range of real-space separations `d` (the two knots translated to XC∓d/2 along x). The **FORM observable is the exponent** `p` in `U(d) ~ d^p`, fit on the clean window (§3.8). Cross-checked by the single-texture far-field `|φ|(r) ~ r^m` exponent (overlap-independent) and — for the DYNAMICAL runs (§5) — the energy-route force `F(d) = −dU/dd` AND the `T^{0i}` momentum-flux route (`mass_sector_field_momentum_T0i`, the mass-sector two-body machinery, as a cross-check).

### 2.3 THE TEXTURE-FORM FORK (flag-don't-fix — surfaced, both carried)

The A44 converter's `f_V` hard-projects along n̂=x̂ (`Ω_w = (∇×ω)·x̂`, `crystal_engine.py:213-219`: "the shear microrotation about the propagation direction"). Two readings of "the winding's charge texture", carried side-by-side, NOT silently collapsed:
- **(S) SCALAR** `ρ_S = −κ̃·g·(∇×ω)·x̂` — the engine's LITERAL `f_V` source term (what `step()` actually adds to `a_V`). The x̂ is the physical photon propagation axis n̂, not a gauge pick. Verified physical: rotating the winding 90° about z FLIPS `p_S` on x̂ (it is locked to n̂=x̂, not the winding body frame — a real axis-selected dipole).
- **(D) COVARIANT** `ρ_D = −κ̃·∇·(g·∇×ω)` — the β-note DEC form `ρ = div J, J = W(A)⊙curl_adj(ω)` transcribed to the real-space lattice (no axis pick). Verified: its DIPOLE VANISHES (`|p_D| ~ 1e-17`), lowest surviving moment is the QUADRUPOLE (`||Q|| ≈ 13.5`).

BOTH are assessed in §3. **The fork does not change the bin** (both give exponent steeper than −1 — S gives dipole −3, D gives quadrupole/steeper), so it is a flag, not a STUCK-FRAMING; but if the two ever disagreed on the BIN, that would route to Grant (§1 last bin).

---

## 3. STEP-0 — THE MULTIPOLE ANALYSIS (analytic, DECISIVE — done BEFORE any build)

**The null expectation, from the mechanism.** A globally-neutral compact texture generically interacts at its lowest SURVIVING multipole: monopole-monopole would be `1/r` (Coulomb) but the monopole is ZERO (β note: `sum ρ = 0` exact, Gauss-no-boundary on the closed complex, re-confirmed §3.1); so the interaction is dipole-dipole (`1/r³`) if a dipole survives, or quadrupole-quadrupole (`1/r⁵`) or worse if symmetry kills the dipole. Coulomb FORM (`1/r`) would require a surviving MONOPOLE — which requires a NET charge the neutral texture does not carry. **So the pre-registered null is MULTIPOLE-FORM, and Coulomb-form would require something specific** (§3.6 candidates). This section computes the actual multipole content and the interaction exponent on FROZEN seeds.

### 3.1 Monopole moment = 0 (forced, re-confirmed)
`sum ρ (interior, PML-excluded) = −5.6e−17` for the SCALAR form; `−6.6e−18` for the COVARIANT form — machine zero, robust across tolerances. **The monopole is forced zero** (β note §4.2: `sum(div J) = 1ᵀ(−∂₁)J = −(grad 1)ᵀJ = 0`, Gauss-no-boundary). Running `Q(r)` = the enclosed charge within radius r of the centroid returns to 0 at every radius on the symmetric center (the ±0.6 excursion of the β note is the off-center bound-charge form-factor, a polarization signature, not a monopole). **No monopole ⇒ PAIR-COULOMB-FORM cannot fire from a monopole moment.**

### 3.2 Dipole moment (the fork, §2.3)
- **SCALAR** `ρ_S`: `p_S = (1.588, 0, 0)` — NONZERO, locked to n̂=x̂ (rotating the winding 90° about z gives `p_S = (−1.588, 0, 0)` — flips on x̂, does NOT rotate to y). The A44 converter's x̂-projection selects an axis-aligned dipole. Characteristic charge-separation length `|p_S|/sum|ρ| = 3.58` cells.
- **COVARIANT** `ρ_D`: `p_D = (1.4e−17, ...)` — VANISHES. The covariant (axis-pick-free) texture has NO dipole; symmetry of the (2,q) seed kills it. Lowest surviving moment is the quadrupole.

### 3.3 Quadrupole moment
- **SCALAR** `ρ_S`: `||Q||_F ≈ 0.99` (a yz off-diagonal), subdominant to the dipole.
- **COVARIANT** `ρ_D`: `||Q||_F ≈ 13.5`, a clean axial quadrupole `Q ≈ diag(−9.53, +9.53, 0)` — the LOWEST surviving covariant moment. Traceless (`tr Q = −4e−15`).

### 3.4 THE DIMENSIONAL ANALYSIS (Step 3.5 discipline — the exponent each moment forces)
For two textures with lowest surviving moment of order ℓ, separated by d, the interaction energy scales as `U(d) ~ d^{−(2ℓ+1)}` (each texture's field falls as `r^{−(ℓ+1)}`, and the interaction couples moment-ℓ to moment-ℓ):

| lowest surviving moment ℓ | single-texture field `|φ| ~ r^m` | pair interaction `U ~ d^p` | force `|F| ~ d^{p−1}` |
|---|---|---|---|
| monopole (ℓ=0) — **Coulomb** | m = −1 | **p = −1** | −2 |
| dipole (ℓ=1) | m = −2 | **p = −3** | −4 |
| quadrupole (ℓ=2) | m = −3 | **p = −5** | −6 |

The PAIR-COULOMB-FORM bin lives at `p = −1` (monopole). Every neutral-texture multipole gives `p ≤ −3`. **The dimensional gap between the Coulomb bin (−1) and the nearest neutral-texture bin (−3, dipole) is 2 full powers of d — decisive if the measured exponent lands cleanly.**

### 3.5 THE MEASURED EXPONENT (open Green's-fn pipeline, overlap-bounded — §3.8)
Frozen-seed interaction `U(d) = Σ_ij ρ_A(i)ρ_B(j)/(4π|r_i−r_j|)` (open-domain Coulomb Green's fn, no periodic-box confound — §3.8), fit on the CLEAN non-overlap above-floor window d∈{28,32,36,40}:

| texture form | single `|φ|` exponent m | pair exponent p | reads as |
|---|---|---|---|
| **SCALAR** (engine `f_V`) | −1.42 (off-axis) | **−2.996** (robust across tol 2e-3/3e-3/5e-3) | **DIPOLE-DIPOLE** |
| **COVARIANT** (β DEC) | −2.56 | (−34, floor-limited by d=32 — see §3.8) | QUADRUPOLE (from `|φ|` = −2.56 → ℓ≈2) |

The SCALAR form (the engine's ACTUAL source term) gives a clean, tolerance-robust **`p = −3.0` = dipole-dipole**. The COVARIANT form's single-texture `|φ|` exponent (−2.56, → quadrupole) is even steeper; its pair `U(d)` collapses into the numerical floor by d=32 (the quadrupole field is weak) so its pair exponent is not reliably readable past d=28 — but its far-field `|φ|` exponent unambiguously places it at quadrupole (steeper than the SCALAR dipole). **Both forms are STEEPER than Coulomb; neither is `p = −1`.**

### 3.6 THE COULOMB-CANDIDATE CHANNELS (assessed honestly — what COULD give 1/r)
The mission required assessing each candidate that could restore a 1/r-class interaction:
- **(a) Overlap / interpenetration at small d.** At d ≤ 24 the two R=11 tori interpenetrate (support-overlap fraction > 0.02); the near-contact `U` is huge and its "exponent" is meaningless (probe blows up to −25..−32). This is NOT a Coulomb monopole — it is the two neutral textures' bound-charge shells physically overlapping (a contact/exchange energy, not a long-range 1/r). It is EXCLUDED from the form fit (§3.8) and does not restore a monopole. **Not a Coulomb channel — a contact artifact.**
- **(b) The harmonic / meridian coupling (Z's Δb₁=+1).** Z's `[DOORWAY-NO-PINNING]` established the punctured-core exterior carries ONE harmonic meridian DOF, but its flux value is UNPINNED (`ξ_topo`-echo) and it is a LOOP-HOLONOMY (linking flux), div-free, invisible to the `∇·E` monopole channel (β note §4.4). It is NOT a monopole source and cannot give a 1/r interaction through the E-sector Poisson field. **Not a Coulomb channel — a holonomy, not a charge.**
- **(c) A log / 1-r form from the 2-complex dimensionality.** A genuinely 2D (log-potential) or reduced-dimension channel would change the exponent; but the massless E-sector Poisson field is solved in the FULL 3D real-space lattice (the texture lives in 3-space), and the measured `|φ| ~ r^{−1.4..−2.6}` is 3D multipole falloff, not a 2D log. **Not a Coulomb channel — the field is 3D.**

**None of the three candidates restores a monopole or a 1/r interaction.** The neutral-texture null holds.

### 3.7 STEP-0 VERDICT (DECISIVE — surfaced BEFORE build, per the cheapest-decisive rule)
**The A44 gyrotropic-neutral texture around a (2,3) winding has monopole = 0 (forced), and its lowest surviving multipole is a DIPOLE (SCALAR form, engine `f_V`) or a QUADRUPOLE (COVARIANT form). The frozen-seed pair interaction exponent is `p = −3.0` (dipole-dipole, SCALAR) or steeper (quadrupole, COVARIANT) — NOT `p = −1` (Coulomb). None of the three Coulomb-candidate channels (overlap, harmonic-meridian, 2-complex log) restores a monopole.**

**⇒ Step-0 lands the [MULTIPOLE-FORM] bin at the analytic (frozen-seed) grade.** The massless-channel pair force is NOT Coulomb; it is the multipole interaction of a globally-neutral polarization form-factor — exactly the null expectation the mechanism predicts. This is the honest charge-FORM negative (Rule 11): a single mechanism (globally-neutral texture ⇒ zero monopole ⇒ dipole/quadrupole-lowest) explains the whole result. **The corpus's Coulomb FORM does NOT derive in the massless winding-pair channel via the A44 texture.**

Per operating-principle 7 and the mission's cheapest-decisive rule, this frozen-seed decisiveness is SURFACED here before the dynamical build. The DYNAMICAL runs (§5) can in principle differ (a dynamically-evolved texture could develop a monopole the frozen seed lacks) — but the monopole is forced zero by Gauss-no-boundary at EVERY instant (a topological, not a dynamical, fact), so the analytic verdict is expected to be dynamically robust. The dynamical driver is the CONFIRMATORY grade, HELD for orchestrator review (§5).

---

## 3.8 LIVENESS + STRUCTURAL-DEGENERACY (Step 3.8 — the controls that certify the pipeline)

**PLANTED CONTROL (liveness — RAN this session, PASS).** Two IMPOSED opposite point sources (a +q and a −q Gaussian blob) through the IDENTICAL Poisson + U(d) pipeline MUST read the known Coulomb interaction:
- open Green's-fn pipeline: UNLIKE (+q,−q) → `p = −1.000` (attract, U<0); LIKE (+q,+q) → `p = −1.000` (repel, U>0). **The pipeline reads Coulomb `−1` for a true monopole pair.** A planted DIPOLE pair reads `p = −2.95 ≈ −3`. So the pipeline resolves −1 (monopole), −3 (dipole) cleanly — the A44 texture's `−3.0` is a REAL dipole-form, not a pipeline artifact.

**STRUCTURAL-DEGENERACY 1 — periodic-image contamination (surfaced + fixed, flag-don't-fix).** An FFT-on-periodic-box Poisson solve STEEPENS every exponent (the periodic/Ewald Green's fn is not 1/r at d comparable to the box): the planted Coulomb pair read `−2.82` (not −1) in the periodic pipeline. **FIX:** the form fit uses the OPEN-domain Coulomb Green's fn `1/(4π|r_i−r_j|)` (direct double-sum over significant cells), which reads the planted Coulomb pair at `−1.000` exactly. The periodic-box result is DISCARDED for the exponent; the open Green's fn is the pipeline of record. The usable d-window is bounded BELOW by overlap (d ≥ 28, §3.6a) and ABOVE by the numerical floor (the covariant texture floors by d=32; the scalar texture is clean through d=40).

**STRUCTURAL-DEGENERACY 2 — global-neutrality bookkeeping (the jellium).** The texture is globally neutral (`sum ρ = 0`); the FFT Poisson solve requires zero net charge (a uniform jellium background is implicitly subtracted). Since the texture is ALREADY neutral, no artificial jellium is added (`ρ − mean(ρ)` shifts by ~1e-17). The open Green's-fn pipeline needs no jellium at all (it sums pairwise 1/r directly). **The neutrality is diagnostic-only, not imposed.**

**STRUCTURAL-DEGENERACY 3 — enantiomorph consistency guard (the Chern-arc guard).** The DYNAMICAL runs (§5) must satisfy `R(RR) = R(LL)` and `R(RL) = R(LR)` (the exponent + sign are enantiomorph-symmetric — a violation is a handedness leak into a parity-even observable, surfaced to Grant). At the frozen-seed grade the mirror texture has `sum ρ_mir = 0` and `p_mir = −p_S` on x̂ (dipole flips sign under mirror, as a real dipole must) — consistent.

**Per-term ledger discipline.** Every printed exponent is fit on an explicit d-window with the overlap fraction and floor status reported per point (the driver prints `d, overlap-frac, U, [clean/OVERLAP/floor]` per separation). The texture is computed ONLY via the A44 form (no integer, no inserted charge); Gauss is diagnostic-only.

---

## 5. THE DYNAMICAL DECISIVE RUNS (spec — HELD for orchestrator review; NOT run pre-review)

Recorded per the standing sequence. **NOT fired until orchestrator review of §3.7.** If the orchestrator concurs the frozen-seed Step-0 is decisive, the dynamical runs are CONFIRMATORY (expected to reproduce −3-or-steeper) and may be skipped or run at low priority. If the orchestrator wants the dynamical confirmation:

- **Pair seeding:** `_seed_pair(d, mirror_A, mirror_B)` (reused verbatim from the Gate-0 driver) — RR/RL/LL/LR + unknot controls (a winding vs a null-ω sphere: one source inert ⇒ U ≈ 0, the additivity control) at 3+ separations in the stable window d ∈ {28, 34, 40} (bounded below by overlap d ≥ 28, above by the box/floor; d=44 from Gate-0 wraps the tail into the PML at N=96 — bound the window explicitly).
- **Texture per step:** the A44 `ρ = f_V` computed per winding AND jointly at each `step()`, the massless potential `φ` solved by the open Green's fn (not the periodic FFT).
- **Interaction readout (two routes, cross-checked):**
  - **Energy route (primary):** `U(d) = ∫ρ_A φ_B`, exponent fit on the clean window — the direct FORM observable.
  - **T⁰ⁱ momentum-flux route (cross-check):** the mass-sector two-body machinery (`mass_sector_field_momentum_T0i`, `research/2026-06-23_mass-sector-two-body-scattering_T0i`). **CRITICAL caveat (that result's §2, load-bearing):** the mid-gap transported-flux M2 is SYMMETRY-FORCED to zero for a mirror-symmetric (RR/LL) pair — the DELIVERED-momentum M1 (P_L−P_R) on the parity-ODD RL/LR configs is the non-symmetry-forced discriminator. The energy route is primary BECAUSE it is not symmetry-zeroed; the T⁰ⁱ route is the cross-check on the parity-odd configs.
- **STOP at the hold-point** after validation + controls. Decisive dynamical pair runs fire only after orchestrator review (the standing sequence).

---

## 8. verify-before-cite ledger (all re-verified at HEAD `96b5f82e` this session)

| Anchor | Verification |
|---|---|
| `cross_sector_coupling.py:66-90` | `gyrotropic_converter_forces`: `f_V = −κ̃·g·Ω_w`, `Ω_w=(∇×w)·x̂`; `KAPPA_TILDE=6/5` α-free ✓ |
| `crystal_engine.py:213-219,221-250` | `_microrotation_x`: `Ω_w=(∇×w)·n̂`, n̂=x̂ = "shear microrotation about the propagation direction"; A44 "Axiom-1 non-centrosymmetry consequence" ✓ |
| `crystal_graft_v4.py:138-172,229-271` | `_buckle_forces` `f_V=−κ̃ g[w·∇×ω]`; buckle-OFF/photon-OFF S1 host; linear ω wave eq `a_ω=c_ω²∇²ω−ω_gap²ω` ✓ |
| `crystal_graft_v4.py:296-324` | `seed_omega_known_2_3`: θ=q·ψ poloidal winding, Gaussian tube env, R/r geometry ✓ |
| β note §4.2, §5.2 | `sum ρ=0` exact (Gauss-no-boundary); neutral polarization texture, `Q(r)`→±0.6→0; NO net monopole ✓ |
| Z note §2, §4.4 | Δb₁=+1 meridian DOF is loop-holonomy (linking), div-free, invisible to ∇·E; `[DOORWAY-NO-PINNING]` ✓ |
| `writhe-campaign-linear-channel_result.md` §4.2,§6 | gapped-ω pair force Yukawa-screened (ξ≈0.548 host-knob) w/ Coulomb SIGN; `clm-wcoul2` consistency-class ✓ |
| `writhe-gate0-pair-feasibility_result.md` §2 | `_seed_pair` machinery; d∈{34,44} STABLE, d=24 UNSTABLE (stable window) ✓ |
| `mass-sector-two-body-scattering_T0i_result.md` §2 | M2 transported-flux SYMMETRY-FORCED zero for symmetric pair; M1 delivered-momentum is the discriminator ✓ |
| Step-0 probes (scratch, this session) | monopole=0 robust; SCALAR dipole `p=−3.0` (tol-robust); COVARIANT quadrupole; controls read −1 (Coulomb)/−3 (dipole) on open Green's fn ✓ |

**Disciplines applied:** substrate-native-check (§0, texture from ω winding carrier, Cosserat-native) · phase-space-coordinate-check (§0.1, matched real-space) · consistency-vs-emergence (per-bin §1) · verify-before-cite (this ledger) · flag-don't-fix (§2.3 SCALAR/COVARIANT fork carried; §3.8 periodic-box artifact surfaced + fixed) · Rule 11 (§3.7 honest closure, single mechanism named). **Step-0 DECISIVE at frozen-seed grade → [MULTIPOLE-FORM]. Dynamical runs HELD for orchestrator review.**
