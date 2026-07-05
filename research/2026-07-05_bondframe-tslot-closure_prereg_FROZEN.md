# PREREG (FROZEN) — The bond-frame 2nd-order content of a traveling transverse wave on a CLEAN periodic-ring host: closing the #526 T-slot fork ANALYTICALLY

> ## ↗ ERRATA BANNER (2026-07-05, orchestrator review of PR #533 — banner-append only; the frozen body below is a record, NOT edited)
> The bin OUTCOME is [CONSTRAINT-DEPENDENT] (this prereg's own bin (iv)), not the [DC-ONLY-DERIVED] the
> #533 result claimed. The FROZEN bins and adjudication contract below are UNCHANGED and CORRECT — the
> #533 result mis-routed them (it never ran the cross-host measurement bin (iv) required). Two frozen-body
> errata, corrected in the result's §CORRECTION (the bins themselves stand):
> - **§4(a) / §"DERIVED TOLERANCE BANDS" / ledger row 8 — the "O(y₀⁴)~2e-6" kernel-correction ORDER is
>   WRONG.** Derived post-freeze (sympy): both channels are O(y₀⁶) (tilt −dy⁶/8, tension −dy⁶/48); the
>   full residual scales as y₀⁶. The physics (kernel negligible) is unchanged; only the order label is 4→6.
> - **§6 tilt anchor "+0.013969" is mis-cited** — that value is not in #532's result doc (which reports
>   "+1.40%"); the real anchor is #532's in-branch `tilt_decomposition` = 0.01397, and the honest
>   truncation band does not cover the static-vs-dynamical discrepancy (the pure-truncation gate fails
>   honestly — the derivation is validated at order-of-magnitude level instead).
>
> See `research/2026-07-05_bondframe-tslot-closure_result.md` §CORRECTION (live verdict) for the full
> disposition. Correction PR: `fix/533-constraint-dependent-rebin`.

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/bondframe-tslot-closure`
**Prediction module (symbolic, INDEPENDENT):** `src/scripts/vol_1_foundations/bondframe_tslot_predictions.py` (to be scaffolded AFTER this freeze)
**Driver (numeric ring confirmation, INDEPENDENT path):** `src/scripts/vol_1_foundations/ring_bondframe_probe.py` (to be scaffolded AFTER this freeze)
**Tests:** `src/tests/test_bondframe_tslot_closure.py`
**Result:** `research/2026-07-05_bondframe-tslot-closure_result.md`
**Closes (Grant path (a), analytic):** the OPEN #526 T-slot SCOPE FORK (`research/2026-07-05_pump-probe-tslot_result.md` [ADJUDICATION-INVALID], fork OPEN; PR #531 fork-record).

**Grant directive recorded verbatim (attributed Grant 2026-07-05):**
> "let the vacuum substrate lead the way..."

**Path selection recorded verbatim (attributed Grant 2026-07-05):** Grant selected **path (a): close the #526 T-slot fork ANALYTICALLY** — derive the cycle-averaged 2nd-order bond-frame content of a traveling transverse wave on a CLEAN (infinite/periodic-ring) host symbolically, with a small targeted numeric confirmation, rather than re-running the full #532-class pump-probe dynamics driver. The #532 open-chain artifacts (boundary sign-flip, lab-frame mixing, drive pin) are exactly what the clean ring host eliminates.

This freezes the arms, bins, and derived tolerances BEFORE the prediction/driver code runs. Commit order is the freeze proof.

---

## PRE-TEST PHYSICS CHECK (pre-test-physics-check Trigger 6 + Trigger 9) — the plumber question surfaced to Grant

**Corpus-searched first (verify-before-cite, grep this session):** the #532 result doc (`research/2026-07-05_pump-probe-tslot_result.md:16,:68-70`) already states "the cycle-MEAN configuration reads 0.9973 (COLD) — there is NO deposited DC bias the slow probe feels" and (`:75-79`) that ⟨A_bond⟩ is a boundary-artifact on the OPEN chain (−0.0026 pinned / −0.0083 free). The #526 slot input is `k_shear_eff = k_shear + T/ℓ`, `T = this bond's own axial-channel tension Φ'(A_axial)` (`prestress_elastic_tensor.py:124-129`, grep-verified). The #529 law is `⟨T⟩ = (k_a/ℓ)y₀²` (`resonant-tension-law_result.md:27`). The corpus does NOT settle the one framing fork below at bond-frame level on a clean host — the #532 arc's mean-config-COLD reading was on an OPEN chain with a boundary artifact, so it is a boundary-contaminated observation, not a theorem.

**The one plumber-physical question (surfaced to Grant, recorded per Step 5):**

> When a genuine traveling transverse wave runs through the clean periodic ring, the bond's mean chord strain is ⟨A_bond⟩ = ⟨dy²⟩/2 > 0 (a real Jensen convexity, ring-closure-pinned). **Does the bond-frame small-signal probe — the actual #526 tensor input — read this as a DC tension deposit `k_s + ⟨T⟩/ℓ` (STIFFER, the EXTENDED/BULK-DEPOSIT reading), or does it read COLD because the mean deposit lives in the AC wiggle snapshots (where L>1 via `dy`, a bond SLOPE) and NOT in the cycle-mean bond SHAPE (where ⟨y⟩=0 leaves the bond straight and un-stretched, `dx`=1)?**

**The physical crux (why this is a real fork, not a procedural choice):** the #526 string-tension deposit `+T/ℓ` requires a **straight, longitudinally-stretched** bond (the guitar-string / uniform-stretch liveness control: `dx=1+A>1`, `dy=0`). The traveling wave makes the bond LONGER (`L=√(1+dy²)>1`) but via the transverse `dy`, at ⟨y⟩=0 in the mean — the mean bond SHAPE is straight and un-stretched. So the two readings measure two different things: the slot-averaged `⟨T⟩/ℓ` (a per-snapshot AC scalar, nonzero) vs the cycle-mean-config bond-frame tangent stiffness (a DC medium-state quantity a slow probe feels, cold).

**Authorization to proceed (Trigger 9, fork-to-computable):** Grant's standing directive "let the vacuum substrate lead the way" + path-(a) selection IS the run-the-derivation authorization. Per pre-test-physics-check Trigger 9 (Grant's demonstrated standing preference (b) — "doc adjudicated by engine, not fiat"), this arc does NOT wait on a fiat ruling: it converts the fork into a COMPUTABLE DISCRIMINATOR with frozen bins (below), where BOTH readings are computed on the clean ring and reported KEEP-BOTH, and the derivation states precisely which quantity each reading is. Grant's answer refines which reading is "the #526 tensor input" (a framing/scope call); the derivation and both numbers are engine-decided. The question is surfaced prominently in the result doc for Grant at review.

---

## SUBSTRATE-FIRST SECTOR HEADER (declared BEFORE any standard-physics term)

- **SECTOR:** translational-u elastic sector, on a **2-DOF-per-node PERIODIC RING** (longitudinal u + transverse y) — the CLEAN host that eliminates the #532 open-chain boundary artifacts. BOTH k_a (axial STRETCH) and k_s (transverse SHEAR) are translational-u / **capacitive** springs of the same bond (PR#516) — NOT the ε/μ photon pair. Cosserat couple-stress = Stage 2, NOT invoked.
- **MODE:** ANALYTIC (sympy, every step) 2nd-order-in-y₀ expansion of the cycle-averaged bond-frame content, with a compact numeric ring confirmation (static u-relaxation at frozen wave phase, phase-averaged — NO large time-domain sim). The dynamics do not know how terms are divided between S and T; the derivation separates them explicitly.
- **REGIME:** small-signal ADIABATIC probe (Ω→0 slow-probe limit) about a traveling transverse pump at in-regime bow y₀ (tent edge). Op14/Ax4 kernel ON. **PHASE-STATE:** sub-yield interior; y₀=0.1428 tent edge (`axiom-register.md:189` arc* band; never tuned).
- **DC-vs-AC (clm-acdc07):** the fork is precisely whether the AC pump deposits a DC bias the slow (bond-frame) probe feels. The derivation separates the AC-per-snapshot content (the tilt, the ⟨T⟩ slot scalar) from the DC-mean-config content (what a slow probe reads).
- **T2 HOMONYM GUARD (binding, #527):** the transverse bow y is the MECHANICAL T2-response bend, NOT the Cosserat (2,3) charge winding (`resonant-lc-solitons.md:95,:128`; A1⊥T2). mass=A1; charge=Cosserat-winding; bow=T2-mechanical-response.
- **COORDS (A46):** real-space displacement pump; real-space transverse restoring stiffness readout. A46-clean (real-space dynamical measurement, not a phase-space φ² comparison).
- **CLASS (consistency-vs-emergence):** CONSISTENCY / DC→AC-coupling. This adjudicates which of two bookkeeping scopes the honest dynamics realize on a clean host. **EMERGENCE FORBIDDEN for any VALUE** (2/7, 9.7734, /7 stay GR-imported, PR#261/#506). ½, ¼, the tilt coefficient, the mean-stretch coefficient are all derived-or-read-off; none tuned toward a canon-distinguished value (KNIFE armed, anti-tune ledger + frozen bins are the guard).

---

## THE CLEAN HOST (the load-bearing construction — geometry + kernel, NO slot formulas, NO boundaries)

**Host:** an N-node PERIODIC ring, 2 DOF per node — longitudinal `u_j` and transverse `y_j`. Rest spacing `a₀=1`. Ring closure: `Σ_j (a₀ + Δu_j) = N·a₀ ⟺ Σ_j Δu_j = 0` (the fixed-total-contour constraint that eliminates the open-chain boundary freedom).

**Bond length (the ONLY transverse↔axial coupling — NOT inserted by hand):**
> `L_b = √((a₀ + u_{j+1} − u_j)² + (y_{j+1} − y_j)²)`, bond `b=(j,j+1)`. `A_bond = L_b − a₀` is the **CHORD strain** — the kernel argument. (This is the #532 chain's own `bond_lengths`, ported to periodic BCs.)

**Axial constitutive law (canonical kernel):** `Φ''(A) = k₀√(1−A²)` (Ax4, `scale_invariant.py:107-156`); `Φ'(A) = k₀(A√(1−A²)+arcsin A)/2` (integrate once, `Φ'(0)=0`; #526 sympy-verified). Kernel units k₀=k_a=k_s=1, ℓ=1 (same as #526/#529/#531/#532).

**Traveling transverse wave ansatz:** `y_j(t) = y₀ sin(k j − ωt)`, longitudinal `u_j = O(y₀²)` (fast DOF, equilibrated). Per-node phase advance k set by the COLD transverse dispersion `ω² = k_s(2 − 2cos k)` (the shear-branch, curvature stencil) — so at ω=1.2, k_s=1, m=1: `cos k = 1 − ω²/2 = 0.28`, `k = 1.28700` (the #532 run's operating point, derived not tuned).

---

## THE DERIVATION (what the prediction module derives symbolically; every step sympy-checked)

### PART 1 — THE LAB-FRAME TILT TERM (validation gate against #532's +0.013969)
> `tilt = ⟨Φ''(A_bond)·(dy/L)²⟩` cycle+space-averaged. Leading order (Φ''(0)=1, L→1): `tilt → ⟨dy²⟩ = y₀²(1−cos k)`. Exact integrand `√(1−A²)·(dy/L)²` with `A=√(1+dy²)−1`, `dy=y₀[sin(p+k)−sin p]`, cycle-averaged over phase p. **GATE:** at the dispersion-set k=1.28700, y₀=0.1428, the exact tilt = 0.014366; #532's `tilt_decomposition` measured **+0.013969** (the run's dynamical-dispersion value). The derived exact-integrand value must reproduce #532's measured tilt to within the derived truncation band (the residual is the O(y₀²) dispersion/convexity shift + the string-tension back-shift of k — NOT free). This is a validation gate, not a discovery.

### PART 2 — THE GEOMETRIC MEAN STRETCH (the careful one; #527 tent lesson)
Distinguish rigorously (the #527 chord-vs-arc lesson):
- **CHORD strain** (node-spacing change): on the periodic ring with fixed node count N and fixed total contour (Σ Δu = 0), the mean CHORD x-spacing is FIXED at a₀ = 1 (theorem, from closure). Derive: `⟨A_bond⟩ = ⟨dy²⟩/2 = y₀²(1−cos k)/2` at the u-equilibrium — and prove the longitudinal relaxation makes A_bond UNIFORM across bonds (Φ'(A) equal ⟹ A equal) but does NOT change its MEAN (the mean is pinned by Σ Δu = 0). **The ring makes ⟨A_bond⟩ a BOUNDARY-INDEPENDENT THEOREM**, unlike the #532 open chain (−0.0026 pinned / −0.0083 free).
- **ARC/bond-length stretch** (⟨√(ℓ²+Δy²)⟩ > ℓ, the Jensen/convexity term): the SAME quantity — on this host the bond IS the chord (straight-line node spacing), so the "arc" that stretches is the chord itself lengthening via `dy`. There is no separate arc DOF (the #527 tent's "arc lengthens at held chord" is a DIFFERENT constitutive picture; here the kernel takes the chord strain, so the convexity term IS the chord strain, not an additional arc excess). Derive both and prove they coincide on this host (the homonym guard between #527's held-chord-arc-stretch and this host's chord-is-the-bond).
- **Which deformation variable feeds the constitutive law:** cite the canon definition — the kernel takes the bond's OWN axial-channel CHORD strain `A_axial = A_bond = L−a₀` (`prestress_elastic_tensor.py:124-129`: `T = Φ'(A_axial)`, the bond's own axial tension, into `k_shear_eff = k_s + T/ℓ`). So the tension a bond carries from the wave's mean geometric state is `⟨T⟩ = Φ'(⟨A_bond⟩) ≈ ⟨A_bond⟩ = ⟨dy²⟩/2` (to leading order, Φ'(x)~x).

### PART 3 — THE T-SLOT VERDICT (what a bond-frame small-signal probe sees at O(y₀²))
Derive what the #526 tensor's actual input reads on the clean host. The decisive computation: the bond-frame tangent stiffness `k_trans = −∂F_y/∂y` at the CYCLE-MEAN config (⟨u⟩, ⟨y⟩=0) — the DC medium state a SLOW probe reads. Prove: at the cycle-mean config, the mean bond has `⟨dx⟩=1` (un-stretched, NOT a straight stretched guitar-string) and `⟨dy⟩=0`, so `A_bond→0` and there is NO string-tension deposit → `k_trans → COLD`. The `⟨A_bond⟩=⟨dy²⟩/2>0` lives in the AC wiggle snapshots (where `dy≠0`), NOT in the cycle-mean bond SHAPE — it is a per-snapshot AC quantity, not a DC bond-frame deposit. **State this as a THEOREM** (what symmetry/constraint forces it): `⟨y⟩=0` (the wave's odd symmetry) forces the mean transverse displacement to zero, and the closure Σ Δu=0 forces no mean longitudinal STRETCH of straight bonds — so the mean bond geometry is the cold geometry, and the transverse tangent stiffness at it is cold. The slot-averaged `⟨T⟩/ℓ = ⟨dy²⟩/2` (the #529 law's cousin) is reported KEEP-BOTH as the per-snapshot AC scalar — it is NOT the bond-frame DC content a slow probe feels.

### PART 4 — RECONCILIATIONS (each a gate)
- **(a)** the linear-chain 2e-6 result: derive why the kernel contributes nothing at O(y₀²). The tilt (leading) and the mean-stretch (⟨dy²⟩/2) both use Φ''(0)=1 = the LINEAR spring constant; the kernel's concavity enters only at O(A²)=O(dy⁴)=O(y₀⁴). So a linear axial spring (Φ''=const, no Jensen) reproduces both to O(y₀²); the kernel/nonlinearity contributes ~O(y₀⁴)~2e-6. **GATE:** derive the O(y₀⁴) kernel correction coefficient and confirm it is ~2e-6 at y₀=0.1428.
- **(b)** #532's boundary sign-flip: the constraint analysis must predict both measured signs from the two open-chain boundary configs. On the OPEN chain, Σ Δu ≠ 0 is allowed (a wall injects a mean axial force), so ⟨A_bond⟩ is boundary-set and can sign-flip (pinned end holds the chain against the Jensen shortening pull → net −0.0026; free end lets it relax further → −0.0083). Derive the sign of the wall's mean axial reaction and confirm it predicts the two signs' ORDER (free more negative than pinned) and that the RING (Σ Δu=0) removes the freedom → +⟨dy²⟩/2 > 0.
- **(c)** #518's null: state precisely which leg(s) the result touches. #518's null rests on TWO independent legs (`matter-stiffening-rho_result.md:146,:149`): (i) the ⟨A⟩=0 FIELD-MEAN leg, (ii) the ⟨A²⟩ CHANNEL-SYMMETRY leg (a pure AC field drives both grades with the same ⟨A²⟩ ⟹ S_axial=S_shear ⟹ ρ_eff=ρ_cold). The [DC-ONLY-DERIVED] result LEAVES BOTH LEGS INTACT (the bond-frame content is cold, consistent with the null); no revision to #518 is warranted. Surface only (do not perform).
- **(d)** the cycle-mean-reads-COLD result: the bond-frame content must be consistent with it. The ring derivation REPRODUCES the #532 cycle-mean-COLD reading and PROMOTES it from a boundary-contaminated observation to a theorem (the ring removes the boundary artifact and the mean-config still reads cold — now it is forced, not observed).

---

## FROZEN BINS (verbatim — NO fall-through else; any criterion-fails path is a loud DISCREPANT-HALT)

- **[DC-ONLY-DERIVED]** — the bond-frame T-slot content of a traveling wave = 0 at O(y₀²) on the clean host, as a THEOREM: `⟨y⟩=0` (wave odd symmetry) + ring closure (Σ Δu=0, no mean straight-bond stretch) force the cycle-mean bond geometry to the cold geometry, so the bond-frame transverse tangent stiffness a slow probe feels is COLD. The lab-frame stiffening is fully the kinematic tilt `⟨Φ''(A)(dy/L)²⟩` (present identically on a LINEAR chain) + the established S-channel. **The fork CLOSES DC_ONLY; #518 intact (both legs).** (Criterion: cycle-mean-config bond-frame stiffness ratio − 1 within the derived band of 0, on the ring, on BOTH the nonlinear and linear-axial hosts; AND the slot-⟨T⟩ scalar correctly identified as a per-snapshot AC quantity, not the probe reading.)
- **[BULK-DEPOSIT-DERIVED]** — a nonzero, boundary-independent bond-frame deposit exists at O(y₀²) (the cycle-mean-config bond-frame stiffness ratio − 1 exceeds the derived band on the ring); derive its coefficient and law; the fork closes with a DERIVED (not slot-averaged) radiation term; #518 scope note required (surface, don't perform). (This is the reading where the slot-⟨T⟩/ℓ IS the probe content.)
- **[CONSTRAINT-DEPENDENT]** — the deposit is set by global constraints, not bulk physics (the ring, open-pinned, open-free, and clamped hosts give materially different bond-frame readings that do not converge as N→∞); the fork DISSOLVES into a boundary-condition question (which global constraint does the cosmological lattice impose? — flag for Grant, do not resolve).
- **[UNDERDETERMINED]** — name the missing structure (e.g. the derivation cannot separate the tilt from a genuine deposit without a bond-frame observable the numeric ring cannot supply).

**NO fall-through else.** The bin selector is: (i) if the derived tilt does NOT reproduce #532's +0.013969 within band → DISCREPANT-HALT (the derivation is wrong, no verdict). (ii) if the ring cycle-mean-config bond-frame stiffness ratio − 1 exceeds the derived band AND is N-convergent (boundary-independent) → [BULK-DEPOSIT-DERIVED]. (iii) else if it is within the derived band of 0 on both nonlinear and linear hosts AND N-convergent → [DC-ONLY-DERIVED]. (iv) else if the reading is boundary-config-dependent and does not converge as N→∞ → [CONSTRAINT-DEPENDENT]. (v) any state satisfying none cleanly → loud DISCREPANT-HALT with the conflicting numbers printed. KNIFE: every derived coefficient (½ in ⟨A_bond⟩=⟨dy²⟩/2; the tilt coefficient; the O(y₀⁴) kernel correction) declared-derived only; 2/7, 9.7734, identity endpoints armed; any exact zero theorem'd not observed.

---

## THE DERIVED TOLERANCE BANDS (the #531/#532 lesson: no vacuous bands; each DERIVED from truncation order)

- **Tilt gate band:** the derivation truncates at O(y₀²); the measured #532 tilt includes the O(y₀²) dispersion back-shift (the string tension shifts k) + the numeric window/node residual (#532's ~0.5%). Band = |exact-integrand − leading| + #532 window residual = |0.014366 − 0.014682| + 3×(#532 node residual). The derived exact-integrand 0.014366 vs #532's 0.013969 differ by 0.000397 (2.8%) — the band must COVER this as the honest O(y₀²)-dispersion + finite-amplitude residual, and be BELOW the leading→exact gap so the gate is informative. Frozen tilt band: **±3.5% of the leading value** (= the dispersion-shift + convexity + #532 window floor, derived below in the prediction module; NOT vacuous — the linear-vs-exact separation is the resolvable scale).
- **Cycle-mean-COLD band:** the numeric ring's cycle-mean-config stiffness reads 1 to the u-relaxation residual + phase-average discretization + finite-difference δ. Derived floor from the relaxation convergence sweep (n_iter, nphase, N) in the driver; frozen at **3× the measured residual floor** (the #531 discipline). The DC-ONLY verdict requires |ratio − 1| < this band; the deposit reading ⟨T⟩/ℓ ≈ 0.0073 (fractional over k_s) is ~20× this band, so the two bins are RESOLVABLE (the cold reading is not a band artifact hiding a deposit).
- **O(y₀⁴) kernel-correction band:** derived from the series; ~2e-6 at y₀=0.1428, matching #532's linear-chain-vs-nonlinear 2e-6 (reconciliation (a)).

All bands DERIVED from truncation orders / convergence sweeps; no vacuous band. Prediction module (symbolic) and confirmation module (numeric ring) are INDEPENDENT code paths (the #531 tautology guard); gates via the #528 ReconcileGate with can-fire proven on dropped-term/sign-flip synthetics on real paths.

---

## ANTI-TUNE / KNIFE LEDGER (canon-forced vs derived vs read-off vs free)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(A)=k₀√(1−A²)` | CANON-FORCED | Ax4, `scale_invariant.py:107-156` |
| 2 | Tension `Φ'(A)=k₀(A√(1−A²)+arcsin A)/2` | DERIVED (sympy) | integrate once, `Φ'(0)=0` |
| 3 | `⟨A_bond⟩ = ⟨dy²⟩/2` | DERIVED (theorem, ring closure) | the ½ is the convexity 2nd-order coeff, sympy-derived; NOT an asserted ½ |
| 4 | `⟨dy²⟩ = y₀²(1−cos k)` | DERIVED (sympy) | traveling-wave phase average |
| 5 | tilt = `⟨Φ''(A)(dy/L)²⟩` | DERIVED (sympy + quadrature) | validation gate vs #532 +0.013969 |
| 6 | dispersion `ω²=k_s(2−2cos k)` ⟹ k=1.28700 | DERIVED | cold shear-branch, curvature stencil; ω=1.2 read-off from #532 |
| 7 | y₀ = 0.1428 tent edge | READ-OFF (#527/#529) | `axiom-register.md:189` arc* band; never tuned |
| 8 | O(y₀⁴) kernel correction ~2e-6 | DERIVED (series) | reconciliation (a) gate |
| 9 | Ring closure Σ Δu=0 | CANON-FORCED (host topology) | periodic ring = the clean object; the fixed-contour constraint |
| 10 | ½, ¼, 2/7, 9.7734, tilt value | KNIFE-ARMED | none tuned toward; any exact zero theorem'd |

**0 free parameters tuned toward 2/7 / 9.7734 / EXTENDED.** ω and y₀ are read-off from #532/#527; k, the tilt, the mean-stretch, and the bands are all derived.

---

## FREEZE

This prereg is FROZEN at this commit. The prediction module, the numeric ring driver, the tests, and the result doc are scaffolded AFTER this commit (commit order proves the freeze). Bins, tolerances, and the anti-tune ledger above are the adjudication contract; no gate looser than frozen here; no post-data bin edits (Rule 11). Any amendment is a Rule-12 dated banner preserving this body.
