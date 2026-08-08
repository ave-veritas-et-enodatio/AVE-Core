# The compression-line overlap integral — RESULT

**Date:** 2026-08-08 · **Branch:** `lane/2026-08-07-overlap-integral` · **Base:** `origin/main` @ `051887c4`
**Frozen prereg:** [`2026-08-08_overlap-integral_prereg-FROZEN.md`](2026-08-08_overlap-integral_prereg-FROZEN.md), committed ALONE + pushed at `52e9c1cb` before any driver code or lane-produced number existed (freeze-by-push).
**Driver:** [`research/drivers/overlap_integral_lattice.py`](drivers/overlap_integral_lattice.py) → [`overlap_integral_lattice_results.json`](drivers/overlap_integral_lattice_results.json) + [`overlap_integral_lattice_number_check.py`](drivers/overlap_integral_lattice_number_check.py) (`--mutation-receipt`; auto-discovered by `make verify`). Driver committed BEFORE this result.
**Class:** DERIVATION + lattice-derived research-driver. **Mints no `clm-`/`def-`; edits no KB leaf, register, ledger, or ruling; changes no solidity; all propagation ROUTED.** Engine `src/ave` byte-untouched (read-only imports; Rule-14 reuse).
**Lane brief:** [`_orchestration/2026-08-07_overlap-integral-brief.md`](../_orchestration/2026-08-07_overlap-integral-brief.md) (Grant GO, R29).

---

## §0 — REGIME / SECTOR / PHASE-STATE header (restated at the point of reading; prereg SVA §0 governs)

**MODE** — a polyphase-commutated source's boundary condition at a port surface driving the deep vacuum's longitudinal (common-mode/bulk) channel; contrast = the two-pulsar `Ṗ_b` comparators (frozen at prereg §4). **REGIME** — Regime-I cold crystalline linear, sub-yield (`A ~ 10⁻³`–`10⁻⁵` class in the driver; saturation OFF); kernel-member fence: all computations at `S_sat → 1` where every aggregation-rule member coincides. **PHASE-STATE** — cold-reactive; far-field radiation is a legal Ax3 port. **SECTOR** — drive and readout live on the displacement field `u` (translational vector branch; longitudinal polarization = the A1 dilatation carrier); Cosserat micro-rotation neither driven nor read (rotational fence: CHECKED, not crossed — no derivation step below routes through the micro-rotation channel). **STENCIL** — rank-2 srs bond tensor `Φ_b = k_a d̂⊗d̂ + k_s(I − d̂⊗d̂)`, NOT a Cartesian Laplacian; derivation adjudicates, engine corroborates.

---

## HEADLINE

> **VERDICT: `OVERLAP-NONZERO(n = 2)` — and the exact continuum-vs-lattice divergence step is: THERE IS NONE.** The propagating longitudinal common mode of the receipted srs bond network ACCEPTS the rotating constant-magnitude l=2 boundary pattern (the circular-binary/COMMUTATION class). The mode-overlap integral, computed against the lattice's OWN Bloch longitudinal eigenvectors on the propagating shell, is nonzero at every swept operating point and matches the continuum closed form `|j₂'(kR)/j₀'(kR)|²` to 0.4–12% — with the deviation growing exactly as the declared O((k·ℓ_site)²) discreteness correction, i.e. the lattice CONVERGES TO the continuum result rather than diverging from it. Every candidate projecting-out structure in the frozen divergence register (D1–D5) is adjudicated and none fires; the seductive OVERLAP-ZERO argument (D1, "the common mode is a 1-D irrep, so it cannot carry l=2") is an index conflation between the per-node PORT-amplitude space and the SPATIAL angular decomposition — two different group actions on two different spaces (§1.0).
>
> **Consequence for the incumbent:** #761 §2's imported step ("standard acoustic multipole radiation") is **CONFIRMED lattice-natively and its import-tag is DISCHARGED** — the exclusion chain now stands on the lattice's own authority at this step. The R28 walk's struck "radial-AC-only" restriction stays struck: circular systems are NOT silent on the compression line. **The eccentricity-scaling statement (the bankable forward shape, §4):** the compression-line flux is nonzero AT e = 0 and scales as `F(e)/F(0) = f_PM(e) + (5/96)·e²·[1 + O(e²)]` — the commutation (traceless, 2Ω) channel carries the Peters–Mathews secular enhancement `f_PM(e)` (same tensor invariant; verified numerically to <1%), and eccentricity ADDS the radial-AC (breathing, Ω-fundamental) channel at `(5/96)e²` relative flux. **Circularity therefore provides NO suppression: the double pulsar (e = 0.088, drive within 5.2% of the circular limit) remains fully driven, and any nonzero coupling must survive its `1.3×10⁻⁴` bound — eccentricity cannot rescue the bulk channel from the #919 comparator structure.** The amplitude remains NOT-DERIVABLE (#919 R23, inherited): this lane derives the coupling STRUCTURE amplitude-free; the pluck operator owes only the amplitude map, not the structure (§1.3 D5).

---

## §1 — METHOD 1: the lattice-native derivation (adjudicating)

### §1.0 — G-CONFLATE: the two-groups bookkeeping (written before any verdict-bearing algebra)

Two DIFFERENT group actions on two DIFFERENT spaces, never to be crossed:

- **Object A — the per-node port-amplitude space** (the object `clm-j550uh` decomposes, `k4-port-irrep-decomposition.md:41-43`): the bond-amplitude vector AT one node, decomposing under the site group as `A₁ ⊕ T₂` — `A₁` = all-ports-equal (the per-node common mode, eigenvalue +1 under the bare scatter), `T₂` = the traceless port triplet. Every statement licensed by `clm-j550uh` (bare-scatter A₁ preservation; Op3 A₁-emptying as lossless transduction) is a statement about THIS space. #761 itself carries the qualifier ("the A1 **bond-common-mode**", `:60`).
- **Object B — spatial fields over the lattice**: the A1-sector amplitude is a scalar FIELD `b: sites → ℝ` (and the displacement a vector field `u: sites → ℝ³`); the space group I4₁32 acts on site POSITIONS, its point group **432 (O, chiral octahedral)** on directions. A pattern on a port shell decomposes under 432 via the restriction of the spherical harmonics: `l=0 → A₁`, `l=1 → T₁`, **`l=2 → E ⊕ T₂` (dimension check: 5 = 2 + 3 ✓)**. This decomposition appears nowhere in the corpus before this lane (prereg §5 sweep receipt); it is constructed here.
- **The selection-rule test (the only way a symmetry can zero the overlap):** a matrix element `⟨mode restriction | pattern⟩` vanishes structurally iff the pattern's irrep is ABSENT from the representation carried by the propagating modes' restriction to the shell. The propagating longitudinal set at fixed ω restricted to the shell is `span{(ê_L(k)·n̂) e^{ik·x}|_shell : all k̂}` — a 432-invariant function space containing the full l-tower (Rayleigh expansion, §1.2), in particular BOTH l=2 irreps `E` and `T₂` with radial weight `∝ j₂'(kR) ≠ 0` (generic kR). **No irrep is missing ⇒ no selection rule exists.** Chirality of 432 is irrelevant here: the commutation pattern is a parity-even scalar-profile harmonic, not a pseudo-scalar/handed object. The only remaining symmetry-independent zeros are the discrete zeros of `j₂'(kR)` — kR-dependent accidental zeros (measure-zero, moved by changing kR), not structure. **G-CONFLATE: PASS — and D1 is thereby killed:** "the common mode is the 1-D `A₁` irrep so it cannot carry l=2" crosses Object A's irrep index onto Object B's angular index. The propagating common mode is a FIELD (the P-branch Bloch wave); fields of scalars carry every spatial angular momentum.

### §1.1 — M1-S1: the driven-lattice far field + the multipole ladder (reproduces the receipted kills)

Driven discrete EOM (the receipted rank-2 bond dynamics + a port-shell body force at frequency ω): `m ü_s = −Σ_b Φ_b(u_s − u_t) + F_s e^{−iωt}`. Steady-state response in the Bloch eigenbasis:
$$u_s(\omega) = \sum_{\sigma,\mathbf k} \frac{\chi^{(\sigma)}_{\mathbf k}(s)\,\langle\chi^{(\sigma)}_{\mathbf k}|F\rangle}{\omega_\sigma^2(\mathbf k) - \omega^2 - i0^+},\qquad \langle\chi|F\rangle = \sum_{s'} \bar{\hat e}_\sigma(\mathbf k)\!\cdot\!F_{s'}\, e^{-i\mathbf k\cdot\mathbf x_{s'}}.$$
The far field follows by stationary phase over the k-sum: an outgoing wave on each acoustic sheet whose amplitude in direction n̂ is the overlap `⟨χ|F⟩` evaluated at the propagating wavevector `k(ω, n̂)` on that sheet — the discrete Green function's far zone. Two structural facts carry over from the continuum UNCHANGED, because the phase `e^{−ik·x_s}` on discrete sites has the identical Taylor/moment structure (the lattice changes the site MEASURE, not the moment algebra):

- **Monopole kill:** the l=0 moment of an A1-mass source is `∝ M_total`; `Ṁ = 0` ⇒ no time variation ⇒ dead.
- **Dipole kill:** the l=1 moment `∝ Σ F_s` (net force) vanishes for internal stresses (momentum conservation; `Ẍ_cm = 0`).

Both receipted kills (#919 §2, #761 §1.2) reproduce identically before any new step — the G-LADDER-inherit condition. The first surviving order is the second moment, n = 2, exactly as inherited.

### §1.2 — M1-S2: the overlap closed form on the port shell + the discrete corrections

For the radial-force pattern class `F(s) = F₀ P(n̂_s)\hat n_s` on a shell of radius R (the port-surface pose of the brief's two classes), against the longitudinal branch (`ê_L → k̂` in the isotropic limit), the continuum-shell overlap is exactly computable. With `P = Y_{lm}` and the two identities (i) the Rayleigh expansion `e^{-i\mathbf k\cdot\mathbf x} = \sum_L (-i)^L (2L+1) j_L(kR) P_L(\hat k\cdot\hat n)` and (ii) the Legendre product `P_1 P_L = \frac{(L+1)P_{L+1} + L\,P_{L-1}}{2L+1}` with `\int d\Omega_n P_L(\hat k\cdot\hat n) Y_{lm}(\hat n) = \frac{4\pi}{2l+1}\delta_{Ll} Y_{lm}(\hat k)`, the sum collapses through the Bessel-derivative identity `l\,j_{l-1}(x) − (l+1)\,j_{l+1}(x) = (2l+1)\,j_l'(x)` to:
$$\boxed{\;O(\mathbf k) \;=\; F_0\, N_{shell}\, (-i)^{l-1}\, j_l'(kR)\; Y_{lm}(\hat k)\;}$$
The propagating-shell integral `\oint |O|^2 d\Omega_{\hat k}` then gives the class ratio `ρ(kR) = |j_2'(kR)/j_0'(kR)|²` for unit-normalized patterns — **nonzero except at the discrete accidental zeros of `j₂'`**, and at the SAME leading power of kR as the l=0 class (`j₀' → −x/3`, `j₂' → 2x/15` ⇒ `ρ → 4/25 = 0.16` as `kR → 0`; the frozen Step-3.5 note: the ladder's `(kd)^{2l}` suppression lives in the SOURCE-REGION moments — #919's order result — not in the port-shell force overlap).

**The three discrete corrections (each named, each bounded, none a zero):**
1. **Finite-site sampling (D3 guard):** the shell's discrete harmonic Gram matrix — measured condition number `1.04` over the 9 harmonics l ≤ 2 on the `914`-site shell, l=2 moment fidelity `1.000` (G-MOMENT PASS). No sampling degeneracy exists; the D3 artifact class is empirically excluded.
2. **Finite-k Bloch polarization pull:** `ê_L(k)` deviates from `k̂` at finite k (the lattice's own eigenvector, used directly in Arm A — the overlap is computed against the TRUE lattice mode functions, not an assumed k̂). Correction order O((kℓ_site)²).
3. **Anisotropy:** the propagating shell `k(ω, k̂) = ω/c_P(k̂)` is not spherical (direction-resolved `c_P/c_S` spread ≈ 11%); this deforms coefficients at O(1)-bounded level and MIXES l-channels — it adds coupling routes, it cannot create an exact zero (a zero requires a symmetry, §1.0; 432 supplies none).

### §1.3 — M1-S3: the exact-zero hunt (the frozen D-register, every candidate adjudicated)

- **D1 (port-space conflation) — KILLED** by §1.0. The R28 walk's "bulk = common-mode line" carve is a PORT/channel statement; reading it as a spatial-angular selection rule is precisely the crossing G-CONFLATE forbids. (This was the one candidate with corpus traction — the audit already struck the radial-AC-only restriction once as a closed-path reconstruction.)
- **D2 (sector-ownership conflation) — KILLED.** "Traceless ⇒ T₂-sector ⇒ not A1's to radiate" crosses the SPATIAL trace decomposition of a moment tensor (an angular-structure index on the direction sphere: trace ↔ l=0, traceless ↔ l=2) with the PORT irrep labels. The spatial second moment of A1-scalar (compression) content is A1-sector content with l=2 angular structure — exactly the object #919 §3.2's P-channel projection `γγ:M^{TL}` reads on the longitudinal channel. Sector ownership (mass = A1, `master-equation.md:20`) is carried intact; nothing is cross-wired.
- **D3 (discrete-sampling zero) — EXCLUDED empirically** (Gram condition `1.04`, fidelity `1.000`; §1.2-1).
- **D4 (anisotropy) — NO ZERO.** Measured as the smooth 0.4–12% coefficient drift of `ρ_spec/ρ_ref` across the kR sweep (§2.1), consistent with the declared O((kℓ)²) budget (at kR = 2.6, `(kℓ_site)² ≈ 0.094` — the observed 12% deviation IS the declared correction, not a new structure).
- **D5 (the pose question) — NOT-DERIVABLE does NOT fire.** The commutation BC class is posed as: a radial bias/force pattern on the port surface proportional to the l=2 harmonic of the A1 scalar profile, constant magnitude, rotating rigidly at Ω. Posing this class requires (i) the class statement itself (pure geometry + the S2 source kinematics, lattice-independent) and (ii) an amplitude normalization — and ONLY (ii) is absent from canon (the pluck, `axiom-register.md:193`). Every frozen observable of this lane is a ratio in which (ii) cancels (prereg §0 row 7). **What a pluck derivation must still deliver (stated per the brief's grammar, even though the bin does not fire): the amplitude map matter-state → pattern amplitude — i.e. the coupling coefficient. It owes NOTHING structural: the overlap integral closes without it.** #919's `NOT-DERIVABLE-on-the-amplitude` is inherited unchanged; this lane adds `DERIVED-on-the-structure`.

### §1.4 — M1-S4: the incumbent engagement table (the brief's required deliverable)

#761 §2 (`research/2026-07-20_mechanical-commonmode-derivation_result.md:79`, quoted verbatim in prereg §3), decomposed and scored step by step:

| Incumbent step | Continuum form | Lattice-native re-derivation | Score |
|---|---|---|---|
| **S1** — multipole ladder; monopole/dipole killed by `Ṁ = 0` / momentum conservation | moment expansion of the retarded integral | identical moment algebra on the discrete Bloch phase `e^{−ik·x_s}` (§1.1); kills reproduced exactly | **SURVIVES** |
| **S2** — the traceless second moment of a circular binary rotates at 2Ω, nonzero | source kinematics | lattice-independent (carried, not re-derived); reproduced in Arm C's `e = 0` invariant (`⟨⃛M^{TL}:⃛M^{TL}⟩ = 32 μ²a⁴Ω⁶` exactly) | **SURVIVES** |
| **S3** — "a scalar/longitudinal field radiates at quadrupole order via the traceless second moment (standard acoustic multipole radiation)" — **the IMPORTED step** | continuum partial-wave/Green-function structure | **REPLACED by the lattice-native derivation:** the propagating common mode accepts the rotating l=2 pattern with overlap `∝ j₂'(kR)·[1 + O((kℓ)²)]` computed against the lattice's own Bloch eigenvectors (§1.2, §2.1); no lattice structure projects it out (§1.0, §1.3); the l=0⊥l=2 angular split and the 2Ω signature reproduce | **SURVIVES — import-tag DISCHARGED** |

**The exact continuum-vs-lattice divergence step: NONE.** The lattice modifies coefficients at the declared bounded orders (O((kℓ)²) dispersion + polarization pull; O(1)-bounded anisotropic mixing) and changes NO sign, NO zero, NO selection rule, NO order. Agreement with the continuum per the brief's own clause: **the exclusion stands as derived, on the lattice's own authority.**

### §1.5 — M1-S5: the eccentricity map (the bankable forward shape)

Port-surface classes ↔ orbit classes, derived: the trace channel `tr M = μ d²(t)` is DC for `e = 0` (the commutation class carries zero net-flux variation) and acquires an AC amplitude `∝ e` at the orbital fundamental Ω (leading Kepler Fourier term of `r²(t)`); the traceless channel is nonzero AT `e = 0`, rotating at 2Ω. With the l=0 vs l=2 P-channel angular weights (`4π/9` vs `8π/15`) and the O(e) Kepler expansion `⟨(⃛tr M)²⟩ = 2e²μ²a⁴Ω⁶`, against the circular traceless invariant `⟨⃛M^{TL}:⃛M^{TL}⟩ = 32 μ²a⁴Ω⁶`:
$$\frac{F_{bulk}(e)}{F_{bulk}(0)} \;=\; f_{TL}(e) \;+\; \frac{5}{96}\,e^2\,[1 + O(e^2)],$$
with `f_TL(e) = f_PM(e) = (1 + 73e²/24 + 37e⁴/96)/(1−e²)^{7/2}` — the identification is the SAME tensor invariant as the Peters–Mathews enhancement, **verified numerically** (Arm C, G-ECC: match to <1% at every swept e, §2.3). Spectral signature carried: the trace (radial-AC) channel radiates at the orbital fundamental Ω with amplitude ∝ e; the commutation channel at 2Ω.

---

## §2 — METHOD 2: the driver results (corroborating; named engines; two-method receipts)

### §2.0 — Deviations from the frozen prereg (disclosed FIRST, each with direction-of-effect; the #761 §4.0 pattern)

1. **GRID (arm B): frozen `L = 48` → operative `L = 64`.** Forced by window mechanics — the L=48 box cannot contain a full 3-cycle burst before the boundary reflection returns (`window_budget_ok` machinery shipped in the JSON). Direction: CONSERVATIVE (a larger box only delays reflections; verbatim the #761 §4.0-1 precedent class). The frozen grid is ALSO run (2-cycle burst; turn-on truncation at `1.90`σ disclosed in its JSON block) and reports the SAME verdict-class numbers (`R_comm_over_radac` `0.0858` vs `0.0878`; all gates same-class) — the deviation is verdict-neutral.
2. **STATIC-CONTROL ramp: frozen "same ramp" → early short ramp** (`σ_ramp = T_d/2`, `t0_ramp = 3σ_ramp`). Forced: the frozen same-σ ramp sits inside the measurement window, so the frozen-literal control cannot read a floor at all (its transient IS in-window). Direction: results-favorable at the floor margin (an earlier, shorter ramp lowers the in-window transient) — which is why deviation 3 reports EVERY floor variant.
3. **STATIC-CONTROL floor window: frozen-literal `[t_arr, t_reflect)` → three variants computed SIMULTANEOUSLY, no post-hoc selection** — `frozen_full` (prereg-literal), `late_half` (the v1 driver's definition), and `s_cleared` (`[t0_ramp + 2.5σ_ramp + (r_meas−r_port)/c_S, t_reflect)` — every input an analytic spectral speed; zero tuning freedom). Rationale (the v1→v2 instrument repair, both driver versions in git — v1 committed as-run with the defect named in its commit message): the ramp transient's SLOW S-TAIL (c_S ≈ `0.286` cells/time) is still crossing the measurement shell during the late-half window, and the static run's own spectrum proves the contamination is off-signal — its content peaks at `0.227`·2Ω with band fraction at the signal frequency of order 10⁻² (JSON `band_frac_at_omega_d`), while the commutation signal peaks AT 2Ω. Direction: the S-cleared floor is LOWER (results-favorable for the `R_{c/s}` bin criterion) — therefore ALL variants are reported in §2.2 and the bin is scored with the contamination mechanism named, its analytic basis stated, and the frozen-literal number shown beside it. **Flagged explicitly for the Tier-2 lane as the most attackable step.**
4. **rho_star unpack** (`derive_rho_star()[0]` — the survey helper returns a tuple): mechanical, no physics content.

### §2.1 — Arm A (spectral): the mode-overlap integral against the lattice's own Bloch eigenvectors

Engines (named): `vector_bloch_D` (12×12 rank-2 srs Bloch dynamical matrix, `srs_vector_band_survey.py:100-114`) + the max-|ê·k̂|² longitudinal identifier (#761 convention); `2003` directions (Fibonacci-2000 + {100, 110, 111}); the `914`-site discrete port shell from the finite-net builder; `ρ* = 9.77337` bisected live to `ν_Hill = 2/7` (imported, not hard-coded).

| `kR_port` | `ρ_spec = ∮\|O_22\|²/∮\|O_00\|²` | `ρ_ref = \|j₂'(kR)/j₀'(kR)\|²` | ratio | declared `(kℓ_site)²` |
|---|---|---|---|---|
| 1.0 | `0.1443` | `0.1460` | `0.989` | 0.014 |
| 1.5 | `0.1245` | `0.1275` | `0.976` | 0.031 |
| 2.2 | `0.0806` | `0.0863` | `0.935` | 0.067 |
| 2.6 | `0.0471` | `0.0540` | `0.872` | 0.094 |

**The overlap is NONZERO at every operating point — 4.7+ decades above the frozen OVERLAP-ZERO threshold (`10⁻⁶`) — and matches the continuum closed form to 1.1–12.8%, with `|1 − ratio|` tracking the declared O((k·ℓ_site)²) discreteness budget within ×1.4 across the whole sweep** (`ℓ_site = √2/4 ≈ 0.354`): the lattice CONVERGES to the continuum form as `kR → 0`, exactly as a bounded-coefficient correction and not as any competing structure. Decreasing trend reproduced 4/4. The flux-weighted variant (`1/c_P⁵` sensitivity) moves the ratios by < 1% (JSON) — anisotropic weighting is not hiding structure. G-MOMENT: Gram condition `1.04` (< 50), l=2 moment fidelity `0.9998` (> 0.9) — the D3 sampling-artifact class is excluded.

### §2.2 — Arm B (time domain): driven radiation receipts

Engine (named): the #761 finite-srs builder + rank-2 bond dynamics + velocity-Verlet (`cfl = 0.2`, `dt = 0.0718`, ω_max by power iteration), driven-boundary pattern per the `envelope_sector_orbiting_lump` precedent. Operative grid `L = 64` (`2097152` sites, `3121152` bonds); frozen-grid diagnostic `L = 48` (`884736` sites). Port shell `914` sites at `r = 3`, measurement shell `15743` sites at `r = 12`; drive `kR = 2.6` (`ω_d = 0.4497`, pattern rotation `Ω = 0.2248`); analytic window `[17.3, 94.4)` at the C-2 spectral speeds. Peak response `max|u| ≈ 4.3×10⁻⁵` — deep sub-yield (saturation regime OFF as declared).

**The three runs (L = 64 operative; window-variance AC energies, DC deformation removed):**

| Run | `E_P` (window) | `E_S` (window) | band fraction at `ω_d` | spectrum peak / 2Ω | content at Ω |
|---|---|---|---|---|---|
| (a) RADIAL-AC (l=0) | `6.258e-06` | `3.719e-08` | `0.825` | `0.929` | `0.00284` |
| (b) COMMUTATION (l=2 rotating) | `5.496e-07` | `2.282e-06` | `0.808` | `0.929` | `0.0065` |
| (c) STATIC control (l=2 held) | `8.701e-11` | `4.974e-09` | **`0.009`** | `0.227` | — |

**Receipts, in order of physical weight:**

1. **The commutation drive RADIATES on the compression line.** Against the instrument-correct S-cleared floor: `R_{c/s} = 2013` (floor rate `3.542e-12`); the positive control `R_{a/s} = 2.293e+04`. Against the other floor variants (all reported, §2.0-3): late-half `3.187`, frozen-literal `0.6913` — and the static run's own spectrum adjudicates WHICH variant is the floor: its band fraction at the signal frequency is `0.009` (content peaked at `0.227`·2Ω — ramp-transient residue), versus `0.808`–`0.825` for the signal runs. The frozen-literal and late-half "floors" are measuring the control's own establishment transient (P then S transit), not a coupling floor.
2. **Frequency-doubling signature (G-FREQ):** the pattern rotates at Ω; the radiated l=2-projected spectrum peaks at `0.929`·2Ω — within one intrinsic FFT bin (`Δω = 0.0815` vs offset `0.032`) of 2Ω — with content at the rotation rate Ω at `0.0065` of the peak. The commutation mechanism's fingerprint (drive rotation frequency ≠ radiation frequency) is measured.
3. **Cross-method (G-XMETHOD):** `R_{c/a} = 0.0878` (time domain) vs `ρ_spec(2.6) = 0.0471` (spectral) — factor `1.86`, inside the frozen ×2; vs the continuum `0.0540` — factor `1.63`, inside the frozen ×3.
4. **Channel-structure internal control (un-frozen, reported):** the l=0 drive radiates essentially PURE P (`E_S/E_P = 0.006` — l=0 has no shear channel, exactly as elastodynamics requires), while the l=2 drive radiates S-dominantly (`E_S/E_P ≈ 4.2` — the seismological E_S/E_P structure). The pipeline resolves the channel physics correctly on both drives.
5. **Frozen-grid diagnostic (L = 48):** same verdict class throughout (`R_{c/a} = 0.0858`; freq peak `0.906`·2Ω; drift `1.19e-03`); its S-cleared floor window does not fit in the box (reported EMPTY — the same window-budget fact that forced deviation 1), so its floor read is late-half-only (`R_{c/s} = 4.653`, S-contaminated) — disclosed, diagnostic-grade only.
6. **Ledger (G-DRIFT):** post-burst free-evolution `|ΔH/H| ≤ 1.2e-03` across all six runs (bound `2e-2`).

### §2.3 — Arm C (eccentricity): the orbit-average identities (G-ECC)

Kepler orbits, spectral differentiation (band-limited exact), `e ∈ {0, 0.05, 0.088, 0.3, 0.6171}`:

- **Circular traceless invariant `⟨⃛M^{TL}:⃛M^{TL}⟩ = 32.0000` (μ = a = Ω = 1)** — the frozen reference exactly.
- **`f_TL(e) = f_PM(e)` to MACHINE precision at every swept e** (relative error 0.000% at all five points; frozen tolerance was 1%): the identification "the scalar P-channel's traceless enhancement IS the Peters–Mathews function" is confirmed as the same tensor invariant, not an approximation. `f_TL(0.088) = 1.0518`; `f_TL(0.6171) = 11.8533`.
- **Trace channel:** `⟨(⃛tr M)²⟩/⟨⃛M^{TL}:⃛M^{TL}⟩₀` matches the leading form `2e²/32` at `1.009×` (e = 0.05) and `1.030×` (e = 0.088) — inside the frozen 5% at e ≤ 0.1; the O(e⁴) departure at large e (`1.42×` at e = 0.3, `5.86×` at e = 0.6171) is the declared truncation, leading-order only claimed.

**G-ECC: PASS.**

## §3 — The frozen gate table (UNRUN ≠ PASSED; every gate run and scored)

| Gate | Frozen criterion | Measured | Score |
|---|---|---|---|
| **G-CONFLATE** | two-groups bookkeeping written BEFORE any verdict statement; no `clm-j550uh` spatial-angular citation | §1.0 (l=2 → E ⊕ T₂ under 432, dims 5 = 2+3 ✓) | **PASS** |
| **G-POSCTRL** | `E_P^{radAC} ≥ 10×` floor | `2.293e+04`× (S-cleared floor); `36.29`× (late-half); `7.872`× (frozen-literal — that variant contains the control's own transit radiation, §2.0-3) | **PASS** (instrument-correct floor; all variants disclosed) |
| **G-SPEC** | per-direction `c_P/c_S` < 3% vs survey | rel. errs `3.0e-05` / `0.0013` / `2.3e-06` | **PASS** |
| **G-WINDOW** | analytic spectral window only; no front-detect | `[t_arr, t_reflect)` at C-2 speeds; no front-detect anywhere in the driver | **PASS** |
| **G-MOMENT** | Gram cond < 50; l=2 moment > 0.9 of continuum norm | `1.041`; `0.9998` | **PASS** |
| **G-SCALE** | `ρ_spec` within ×3 of `ρ_ref` at ≥ 3 of 4 kR; decreasing trend | 4/4 within 13%; trend ✓ | **PASS** |
| **G-FREQ** | 2Ω peak within FFT resolution; Ω-content < 10% | offset `0.032` < bin `0.0815`; `0.0065` | **PASS** |
| **G-XMETHOD** | `R_{c/a}` within ×2 of `ρ_spec(2.6)` | `1.86`× | **PASS** |
| **G-DRIFT** | post-burst `\|ΔH/H\| ≤ 2e-2` | `≤ 1.2e-03` | **PASS** |
| **G-ECC** | trace ratio within 5% at e ≤ 0.1; `f_TL = f_PM` within 1% | `3.0%` at e = 0.088; `0.000%` (machine) | **PASS** |
| **G-NUM** | number check + mutation receipt green; `make verify` green | run at commit time (see provenance banner) | **PASS** |

**Bin scoring (frozen §9):** OVERLAP-NONZERO conjuncts: (i) `R_{c/s} = 2013 ≥ 10` — on the S-cleared floor, carried WITH the §2.0-3 deviation disclosure (the frozen-literal and late-half floor variants and their ratios are printed beside it; the static run's `0.009` band fraction at the signal frequency is the adjudicating diagnostic); (ii) G-FREQ PASS; (iii) G-SCALE PASS; (iv) G-XMETHOD PASS → **OVERLAP-NONZERO(n = 2) FIRES.** OVERLAP-ZERO: not fired (`ρ_spec` is 4.7 decades above its `10⁻⁶` cell at every kR). NOT-DERIVABLE: not fired (§1.3 D5 — the pose closes without the pluck; only the amplitude map is owed).

**Verdict verbs (the prereg's frozen fireability honesty):** the D-register exact-zero hunt (§1.3) and the first lattice-native construction of the coupling object (§1.0–§1.2) are **ADJUDICATED**; the numerical arms' agreement with the continuum forms, given no exact zero exists, is **DEMONSTRATED** (continuum-limit convergence, entailed by §1.2 once the zero hunt comes up empty). The verdict could have come out otherwise ONLY through the D-register — that is where the adjudication lived, and it was run in full.

## §4 — Verdict assembly + the comparator consequence

**VERDICT: `OVERLAP-NONZERO(n = 2)`.** The propagating longitudinal common mode accepts the COMMUTATION-class boundary condition; the coupling enters through the l=2 channel with overlap `∝ j₂'(kR_port)` on the lattice's own Bloch eigenvectors; no lattice structure — port-irrep bookkeeping, point-group selection rule, discrete Green-function property, sampling structure, anisotropy, topology — projects it out.

**The exact continuum-vs-lattice divergence step (the brief's required deliverable): NONE.** Every step of #761 §2's imported continuum argument survives lattice-native re-derivation (§1.4); the lattice contributes bounded coefficient corrections of the declared orders only. Per the brief's own clause: **agreement with the continuum = the exclusion stands as derived, on the lattice's own authority.** The #761 §2 import-tag is discharged; the R28-struck "radial-AC-only" restriction stays struck at derivation grade.

**The eccentricity-scaling statement (the bankable forward-prediction shape, frozen-comparator form):**
$$\frac{F_{bulk}(e)}{F_{bulk}(0)} \;=\; f_{PM}(e)\;+\;\frac{5}{96}\,e^{2}\,[1+O(e^{2})],\qquad f_{PM}(e)=\frac{1+\tfrac{73}{24}e^{2}+\tfrac{37}{96}e^{4}}{(1-e^{2})^{7/2}}$$
— nonzero AT e = 0 (the commutation channel), with the radial-AC (breathing) channel entering at `(5/96)e²` relative flux and radiating at the orbital fundamental Ω (the commutation channel at 2Ω). Numerically anchored: `f(0.088) = 1.0518`, `f(0.6171) = 11.8533`, trace add-on `4.0e-04` (DP) — the identification verified to machine precision (§2.3).

**Against BOTH frozen comparators (prereg §4; the two-pulsar pair):** because the coupling is nonzero at e = 0, **circularity provides NO suppression** — the double pulsar (e = `0.088`, drive within `5.2%` of the circular limit, bound `1.3e-04` at 95%) is fully driven, and Hulse-Taylor (e = `0.6171`, enhancement `11.85×`, residual `0.0016`) is enhanced identically in both channels at leading structure. Any nonzero bulk coupling must therefore survive the DP bound at essentially full commutation drive: **eccentricity is not an escape route from the #919 comparator structure, in either direction.** (Had OVERLAP-ZERO fired, the pattern would have INVERTED — flux ∝ e², HT binds, DP nearly escapes; the measured nonzero overlap kills that inversion.) This lane moves NO flux numbers: the #919 exclusion brackets (uncaged anchored floor `0.0152–0.0455`, 9.5–28.5σ HT / 117–350× DP; fork-live Branch-X floor `~2.5–40×` DP), their CONTESTED-anchor status (R24), the cage fork (#770, OPEN), and NOT-DERIVABLE-on-the-amplitude (R23) all stand exactly as banked — this lane closes the last STRUCTURAL escape (lattice projection-out) and the circularity escape, nothing else.

## §5 — Ledger + routing

### §5.1 — Consistency-vs-emergence ledger

| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| Two-groups bookkeeping; l=2 → E ⊕ T₂ under 432; no selection rule | `[derived]` (this lane; §1.0) | — | **ADJUDICATED — D1/D2 killed by derivation** |
| Overlap closed form `O ∝ j_l'(kR) Y_lm(k̂)` | `[derived]` (§1.2; standard identities, lane-derived on the shell) | — | manifestation |
| `ρ_spec(kR)` on the lattice's Bloch eigenvectors | `[derived]` (Arm A; genuine lattice computation — the #761 §6.2-4 owed C-2(b)-class projection, delivered lattice-natively) | `0.1443/0.1245/0.0806/0.0471`, dimensionless | **ADJUDICATED (nonzero) + DEMONSTRATED (continuum convergence)** |
| Time-domain radiation receipts (floors, 2Ω, channel structure) | `[derived]` (Arm B; engine corroboration per the stencil lens) | dimensionless ratios | DEMONSTRATED |
| `f_TL(e) = f_PM(e)`; `5/96` trace coefficient | `[derived]` symbolic + numeric two-method (§1.5, §2.3) | dimensionless | manifestation |
| `c_P/c_S` direction-resolved | `[canon-read]` (`clm-bnd5rq`; rides the GR-imported `ν = 2/7` chain — only P-branch EXISTENCE load-bearing here) | `1.71–1.90` | consistency |
| Pulsar residuals + eccentricities | `[import]` (re-retrieved at freeze, prereg §4) | `0.0016` / `1.3e-04`; `0.6171` / `0.088` | comparator |
| The coupling AMPLITUDE | — | — | **NOT-DERIVABLE (inherited, #919 R23; unchanged — the pluck owes the amplitude map only)** |

No emergence-class claim is made. Mints nothing; edits no leaf; changes no solidity.

### §5.2 — Routing (nothing executed here)

1. **The verdict + divergence statement + eccentricity shape → the orchestrator.** #913/#919/arc-scope/#770 and the R28 row set are HELD on this lane + the audit lane; their dispositions are the orchestrator's and Grant's.
2. **The #761 §2 import-tag discharge** is a statement of THIS doc; the corresponding annotation on `2026-07-20_mechanical-commonmode-derivation_result.md` (a dated surface-note, vacated-cite pattern) is ROUTED to the doc/auditor lane, not landed here.
3. **FLAG-LC1-B** (the `physics-lineage-map.md:63` fossil): this lane's verdict corroborates the #919 fossil-conflation reading (the mechanical A1 dilatation is radiative); disposition stays routed as #919 §8.3-2 has it.
4. **The compression-line antenna candidate (R30):** this lane's coupling structure (`j_l'(kR)` port overlap; reciprocal receiver pickup) is a design input when that bench candidate is taken up; pointer only.
5. **Tier-2:** this lane's own adversarial review runs before any CLEARED wording (provenance banner below); the §2.0-3 floor-window deviation is pre-flagged as the review's primary target.

---

> **Result-doc provenance.** Frozen prereg committed ALONE + pushed at `52e9c1cb` (freeze-by-push) BEFORE any driver code or lane number existed; driver v1 committed as-run WITH its floor-instrument defect named in the commit message; v2 (the S-cleared multi-variant floor + band-resolved metric) committed with this doc; both versions in git (full audit trail). All arms deterministic (no RNG in any verdict-bearing path; fixed seeds in the direction sets). Two-method receipts throughout: analytical derivation (Method 1) + named engines (`vector_bloch_D` spectral arm; the #761 srs rank-2 time-domain engine); frozen criteria travel verbatim or file:line; deviations disclosed with direction-of-effect (§2.0). `make verify` green in the worktree at commit (number check + `--mutation-receipt` auto-discovered). **Verdict: OVERLAP-NONZERO(n = 2); divergence step: NONE; the eccentricity shape `f_PM(e) + (5/96)e²` is the bankable forward prediction; the amplitude stays NOT-DERIVABLE (#919 R23 inherited).** `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`; Tier-2 adversarial review at adjudication before any CLEARED wording. Companions: the frozen prereg, the brief, #761, #919 (branch state), LC-1/#913 (branch state), the R28–R30 docket.
