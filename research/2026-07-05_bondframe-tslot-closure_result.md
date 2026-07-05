# RESULT — [DC-ONLY-DERIVED]: the bond-frame T-slot content of a traveling transverse wave = 0 at O(y₀²) on the CLEAN periodic ring, as a THEOREM. The #526 fork CLOSES DC_ONLY; #518 intact (both legs). The lab-frame stiffening is fully the kinematic tilt + established S-channel.

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/bondframe-tslot-closure`
**Prereg (FROZEN):** `research/2026-07-05_bondframe-tslot-closure_prereg_FROZEN.md` (committed BEFORE the prediction/driver code; commit order = freeze proof)
**Prediction module (symbolic, INDEPENDENT):** `src/scripts/vol_1_foundations/bondframe_tslot_predictions.py`
**Driver (numeric ring, INDEPENDENT path):** `src/scripts/vol_1_foundations/ring_bondframe_probe.py`
**Tests:** `src/tests/test_bondframe_tslot_closure.py` (24 pass: 18 fast + 6 engine_sim)
**Output:** `src/scripts/vol_1_foundations/_output/ring_bondframe_probe.json` (driver-regenerable; gitignored)
**Closes (Grant path (a), analytic):** the OPEN #526 T-slot SCOPE FORK (`research/2026-07-05_pump-probe-tslot_result.md` [ADJUDICATION-INVALID], fork OPEN; PR #531 fork-record).
**Grant directive (verbatim, attributed Grant 2026-07-05):** *"let the vacuum substrate lead the way..."* · **Path selection (verbatim, Grant 2026-07-05):** path (a) — close the #526 T-slot fork ANALYTICALLY on a clean host.

---

## VERDICT BOX

> **PRIMARY BIN: [DC-ONLY-DERIVED].** On the CLEAN periodic-ring host, the bond-frame small-signal
> probe — the actual #526 tensor input — reads the O(y₀²) content of a traveling transverse wave as
> **COLD**, as a **THEOREM**. Two constraints force it:
>
> 1. **`⟨y⟩ = 0`** (the wave's odd symmetry: `∫₀²π sin(p+k) dp = 0`, backbone R7) ⟹ the cycle-mean
>    transverse displacement is zero.
> 2. **Ring closure `Σ Δu = 0`** (fixed total contour, N fixed) ⟹ the u-equilibrium makes `A_bond`
>    UNIFORM across bonds (equal tension) but pins its MEAN, and — critically — leaves **no mean
>    longitudinal STRETCH of straight bonds** in the cycle-mean config: `⟨dx⟩ = 1.0000000000`,
>    `⟨A_bond at mean config⟩ = −2×10⁻¹⁷`.
>
> So the cycle-mean bond geometry IS the cold geometry, and the transverse tangent stiffness at it
> reads **1.0000000000** (bit-exact, keying B) on the ring, N-convergent (N=120/240/480 all 1.0000).
>
> **The lab-frame stiffening is fully the kinematic tilt + the established S-channel.** The lab-frame
> observable (the #532 artifact) reads **1.02152** — stiffer than cold by the derived tilt term
> `⟨Φ''(A)·(dy/L)²⟩ = 0.01439` (the axial spring felt through the instantaneous bond SLOPE). A
> **LINEAR-axial ring** (no kernel, no Jensen) reproduces the lab-frame value to **4.5×10⁻⁷** — the
> effect is KINEMATIC, not the concave kernel (reconciliation (a)).
>
> **The `⟨A_bond⟩ = ⟨dy²⟩/2 = 0.00729 > 0` is REAL and boundary-independent on the ring — but it is a
> per-snapshot AC quantity** (it lives in the wiggling snapshots where `L = √(1+dy²) > 1` via `dy`),
> **NOT a DC bond-frame deposit** (the #526 string-tension `+T/ℓ` requires a straight, longitudinally-
> stretched bond `dx > 1`, which the transverse wave does NOT produce). The slot-averaged
> `⟨T⟩/ℓ = 0.00729` (the #529-cousin) is reported KEEP-BOTH as the AC scalar — it is NOT the bond-frame
> content a slow probe feels.
>
> **The #526 T-slot fork CLOSES DC_ONLY. #518's null is INTACT (both legs, §RECONCILIATION (c)).**
>
> **CONSISTENCY-vs-EMERGENCE:** CONSISTENCY / DC→AC-coupling. No VALUE derived (2/7, ρ*=9.7734, /7
> stay GR-imported, PR#261/#506). **KNIFE=False:** the derived ½ (in ⟨A_bond⟩=⟨dy²⟩/2) is the convexity
> 2nd-order coefficient (sympy backbone R4, declared-derived); the exact-zero deposit is THEOREM'd (not
> observed) via ⟨y⟩=0 + closure; the tilt 0.01439 lands on no canon-distinguished value.

**All 24 tests pass** (8 symbolic exact-zero residuals; the tilt validation gate vs #532's +0.013969
within the derived band; the DC-ONLY cycle-mean-COLD gate bit-exact on the ring; N-convergence; the
linear-vs-nonlinear kernel reconciliation; the open-chain boundary-artifact reconciliation; the #528
ReconcileGate can-fire proven on dropped-term/sign-flip synthetics on real paths; the no-fall-through
bin selector with reachable BULK-DEPOSIT / CONSTRAINT-DEPENDENT / HALT branches).

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u elastic sector on a **2-DOF-per-node PERIODIC RING** — the CLEAN host that
  eliminates the #532 open-chain boundary artifacts (drive pin, absorber, boundary sign-flip). BOTH k_a
  (axial STRETCH) and k_s (transverse SHEAR) are translational-u / **capacitive** springs of the same
  bond (PR#516) — NOT the ε/μ photon pair. Cosserat = Stage 2, NOT invoked.
- **MODE:** ANALYTIC (sympy, every step) 2nd-order-in-y₀ expansion + a compact NUMERIC ring confirmation
  (static u-relaxation at frozen wave phase, phase-averaged — NO large time-domain sim). Two INDEPENDENT
  code paths (the #531 tautology guard: the numeric module never imports the symbolic one).
- **REGIME:** small-signal ADIABATIC probe (Ω→0) about a traveling transverse pump at y₀=0.1428 (tent
  edge, `axiom-register.md:189` arc* band; never tuned). Op14/Ax4 kernel ON. Sub-yield interior.
- **DC-vs-AC (clm-acdc07):** the AC→AC fork — does the AC pump deposit a DC bias the slow (bond-frame)
  probe feels? The derivation separates the AC-per-snapshot content (the tilt, the ⟨T⟩ slot scalar) from
  the DC-mean-config content (what a slow probe reads). Verdict: no DC bias in the mean config.
- **T2 HOMONYM GUARD (binding, #527):** the transverse bow y is the MECHANICAL T2-response bend, NOT the
  Cosserat (2,3) charge winding (`resonant-lc-solitons.md:95,:128`; A1⊥T2). mass=A1;
  charge=Cosserat-winding; bow=T2-mechanical-response.
- **COORDS (A46):** real-space displacement pump; real-space transverse restoring stiffness readout.
  A46-clean.
- **CLASS:** CONSISTENCY / DC→AC-coupling. EMERGENCE FORBIDDEN for any value.

---

## THE DERIVATION (symbolic — every step sympy-verified; 8 exact-zero residuals)

### PART 1 — THE LAB-FRAME TILT TERM (validation gate vs #532's +0.013969)

The lab-frame transverse tangent stiffness `⟨−∂F_y/∂y⟩` on a live wiggling config feels the axial
spring through the instantaneous bond SLOPE `dy/L`. The tilt integrand (the #532 `tilt_decomposition`
term, ported to the ring) is:

> **tilt = ⟨Φ''(A_bond)·(dy/L)²⟩**,  A_bond = L−1, L = √(1+dy²) (u = O(y₀²)), dy = y₀[sin(p+k) − sin p].

- **Leading order** (Φ''(0)=1, L→1): `tilt → ⟨dy²⟩ = y₀²(1 − cos k)` (backbone R3, R8; ⟨dy²⟩/y₀² =
  1−cos k, sympy exact). At the cold shear-branch dispersion `ω² = k_s(2−2cos k)`, ω=1.2, k_s=1, m=1:
  `cos k = 1 − ω²/2 = 0.28`, **k = 1.2870022** (DERIVED, read-off ω from #532; not tuned). Leading tilt
  = **0.01468212**.
- **Exact integrand** (retaining the convexity): `√(1−A²)·(dy/L)²` cycle-averaged = **0.01436554**
  (symbolic quadrature). The convexity pulls the leading value DOWN by 2.2%.

> **VALIDATION GATE:** #532's `tilt_decomposition` measured **+0.013969** (`pump-probe-tslot_result.md:16,
> :73`). The derived exact-integrand tilt **0.014366** reproduces it within the **derived band**
> (±3.5% of leading = ±5.1×10⁻⁴): |0.014366 − 0.013969| = 3.97×10⁻⁴ < 5.14×10⁻⁴. The residual is the
> O(y₀²) dynamical-dispersion back-shift (the string tension shifts the actual dynamical k slightly
> below the cold k) + #532's own window/node residual (~0.5%). **The tilt is DERIVED, not a discovery —
> this is the gate that proves the derivation is right.** (The numeric ring reproduces it at
> **0.01438863** at the ring-commensurate k=1.2828, consistent.)

### PART 2 — THE GEOMETRIC MEAN CHORD STRETCH (the careful one; #527 tent lesson)

Distinguish rigorously (the #527 chord-vs-arc lesson, `bond-force-sign-rule_result.md:80-91`):

- **CHORD strain** (node-spacing change). On this host the bond IS the chord (the straight-line node
  spacing) — the kernel takes `A_bond = L − a₀ = √((1+Δu)² + Δy²) − 1`. On the periodic ring with fixed
  node count N and fixed total contour (`Σ Δu = 0`), the mean CHORD x-spacing is FIXED at a₀ = 1
  (theorem, from closure). At the u-equilibrium: `A_bond = Δu + Δy²/2 + O(y₀⁴)` (backbone: L−1 series);
  the force balance makes Φ'(A_bond) UNIFORM ⟹ A_bond = A* CONSTANT; the closure `Σ Δu = 0` with
  `Δu = A* − Δy²/2` gives **A* = ⟨Δy²⟩/2** (backbone R6, `N·A* = ½ Σ Δy²`). So:

  > **⟨A_bond⟩ = ⟨dy²⟩/2 = y₀²(1 − cos k)/2** (backbone R4, R5; the ½ is the DERIVED convexity 2nd-order
  > coefficient, NOT an asserted ½). = **0.00734106** (symbolic), **0.00728670** (numeric ring, at the
  > commensurate k). **The longitudinal relaxation makes A_bond UNIFORM but does NOT change its MEAN —
  > the mean is pinned by the ring closure.** This makes ⟨A_bond⟩ a **BOUNDARY-INDEPENDENT THEOREM** on
  > the ring, unlike the #532 open chain (§RECONCILIATION (b)).

- **ARC/bond-length stretch** (⟨√(ℓ²+Δy²)⟩ > ℓ, the Jensen/convexity term). On this host the "arc" that
  stretches IS the chord itself lengthening via `dy` — there is no separate arc DOF. This is the CRUX
  homonym guard against the #527 tent: the #527 tent's "arc lengthens at HELD chord" is a DIFFERENT
  constitutive picture (a bowing strut whose end-to-end chord is clamped while its material arc
  lengthens). **On this host the kernel takes the CHORD strain** (`prestress_elastic_tensor.py:124-129`,
  the bond's OWN axial-channel chord `A_axial = A_bond = L − a₀`), so the convexity term IS the chord
  strain, not an additional arc excess. The two coincide here (Jensen of `√(1+dy²)` = the chord's own
  lengthening); on the #527 tent they do NOT (the arc there is a separate material length). This is the
  #527 tent lesson applied: **name which deformation variable feeds the constitutive law.**

- **The tension the wave's mean geometric state carries in the BOND frame:** `⟨T⟩ = Φ'(⟨A_bond⟩) ≈
  ⟨A_bond⟩ = ⟨dy²⟩/2` (Φ'(x)~x for small x). `⟨T⟩/ℓ = 0.00728750` (the slot-averaged scalar). **This is
  the per-snapshot AC scalar — NOT the DC content a slow probe feels (Part 3).**

### PART 3 — THE T-SLOT VERDICT (what a bond-frame small-signal probe sees at O(y₀²))

The decisive computation: the bond-frame transverse tangent stiffness `k_trans = −∂F_y/∂y` at the
CYCLE-MEAN config (⟨u⟩, ⟨y⟩=0) — the DC medium state a SLOW probe reads. On the ring:

> **k_trans at cycle-mean config / cold = 1.0000000000** (bit-exact, keying B, N=120/240/480).

**THEOREM (what forces it):** at the cycle-mean config, `⟨y⟩ = 0` (wave odd symmetry, backbone R7) and
ring closure (`Σ Δu = 0`, no mean straight-bond stretch) force `⟨dx⟩ = 1.0000000000` (un-stretched) and
`⟨A_bond at mean config⟩ = −2×10⁻¹⁷` — the mean bond geometry IS the cold geometry, so the transverse
tangent stiffness at it is COLD. **The derived bond-frame DC deposit = 0 at O(y₀²).**

**Why the `⟨A_bond⟩ = 0.0073 > 0` does NOT stiffen it:** the #526 string-tension deposit `+T/ℓ`
requires a **straight, longitudinally-stretched** bond (the guitar-string / uniform-stretch liveness
control: `dx = 1+A > 1`, `dy = 0`; that control correctly reads k_s+T/L = 1.078606, #532 (b)). The
traveling wave makes the bond LONGER (`L = √(1+dy²) > 1`) but via the transverse `dy`, at ⟨y⟩=0 in the
mean — the mean bond SHAPE is straight and un-stretched. So `⟨A_bond⟩ = ⟨dy²⟩/2` is a per-snapshot AC
quantity (it lives in the wiggle where `dy ≠ 0`), NOT a DC deposit in the mean bond shape. The
slot-averaged `⟨T⟩/ℓ = 0.0073` is the AC scalar; it is NOT the bond-frame DC content a slow probe feels.

> **This is NOT the slot-averaged ⟨T⟩ of #529.** The #529 law `⟨T⟩ = (k_a/ℓ)y₀²` is the AC per-snapshot
> scalar (which this arc reproduces as `⟨T⟩/ℓ = ⟨dy²⟩/2`, KEEP-BOTH). The bond-frame content a slow
> probe feels — the actual #526 tensor input — is a DIFFERENT quantity (the cycle-mean-config tangent
> stiffness) and it is COLD. The fork closes DC_ONLY on the BOND-FRAME reading, not by adopting the #529
> slot scalar.

---

## THE CONSTRAINT ANALYSIS (the load-bearing physics — why the ring is the clean object)

The ring's ⟨A_bond⟩ = ⟨dy²⟩/2 > 0 is a **theorem** because the closure `Σ Δu = 0` removes the boundary
freedom. On the OPEN chain the freedom returns and the reading becomes boundary-set and
position-dependent:

| Host | Σ Δu constraint | ⟨A_bond⟩ | boundary-dependence |
|---|---|---|---|
| **RING** (this arc) | `Σ Δu = 0` (closure, forced) | **+⟨dy²⟩/2 = +0.00729** UNIFORM | **NONE** (theorem; N=120/240/480 identical) |
| open, pinned both ends | `Σ Δu` unconstrained; wall injects mean axial force | +0.00732 (near-uniform) | position gradient 3.6×10⁻⁵ |
| open, free far end | far u free | +0.00615 (chain mean), profile min +7×10⁻⁵ | position gradient **7.2×10⁻³** (200× the pinned) |

The **ring closure `Σ Δu = 0` is the specific global constraint** that makes the mean chord strain a
bulk theorem rather than a boundary-set number. On the open chain the wall can inject an arbitrary mean
axial force, so ⟨A_bond⟩ is position-dependent (the #532 −0.0026 pinned / −0.0083 free artifact). **The
ring reading is N-CONVERGENT and UNIFORM ⟹ [DC-ONLY-DERIVED], NOT [CONSTRAINT-DEPENDENT]:** the
bond-frame COLD verdict is a bulk theorem, boundary-independent.

---

## RECONCILIATIONS (each a gate — all four PASS)

### (a) the linear-chain 2e-6 result — why the kernel contributes nothing at this order — ✅ PASS
The tilt and the mean-stretch both use **Φ''(0) = 1 = the LINEAR spring constant**; the kernel's
concavity enters only at O(A²) = O(dy⁴) = O(y₀⁴) or higher. The tilt-channel kernel correction is
`[Φ''(A) − 1]·(dy/L)² ≈ −(A²/2)(dy/L)² ≈ −dy⁶/8 = O(y₀⁶)` — the derived `kernel_correction_o4` =
**−9.5×10⁻⁷**, scaling as y₀⁶ (halving y₀ cuts it 62×, test-locked). So a **LINEAR-axial ring**
reproduces the lab-frame stiffening to **4.5×10⁻⁷** (numeric, `linear_axial=True`) — matching #532's
CRITICAL-1 (a linear chain reproduces the pump verdict to ~2e-6; the full lab-frame stiffness also
carries the O(y₀⁴) mean-stretch channel, hence 2e-6 vs the tilt-only 4.5e-7). **The kernel contributes
nothing at O(y₀²); the effect is KINEMATIC.**

### (b) #532's boundary sign-flip — predict both signs from the two boundary configs — ✅ PASS (structure)
The constraint analysis predicts the #532 STRUCTURE: on the open chain, ⟨A_bond⟩ is boundary-set and
POSITION-DEPENDENT (the wall injects a mean axial force). The free-far-end config has a **200× larger
position gradient** (7.2×10⁻³ vs 3.6×10⁻⁵) than the pinned config, and its whole-chain mean is
materially different (0.00615 vs 0.00732) — reproducing the #532 finding that ⟨A_bond⟩ is
"boundary-concentrated, sign-varying along the chain" (`pump-probe-tslot_result.md:77`). **SCOPE
(flag-don't-fix, §FLAGS-1):** this static-relaxation model reproduces the #532 GRADIENT STRUCTURE and
its boundary-config sensitivity, NOT #532's exact −0.0026 node-200 value (that requires #532's full
traveling-wave TIME-DOMAIN dynamics with the absorbing sponge — out of scope for the analytic path (a)).
The load-bearing reconciliation is the CONTRAST: open = position-dependent / boundary-set / sign-varying
(the artifact); ring = uniform / boundary-independent / positive (the theorem). **The ring removes the
freedom that produces the sign-flip.**

### (c) #518's null — which leg(s) touched, which stand — ✅ PASS (both legs INTACT)
#518's null rests on TWO independent legs (`matter-stiffening-rho_result.md:146,:149`): (i) the **⟨A⟩=0
FIELD-MEAN leg**, (ii) the **⟨A²⟩ CHANNEL-SYMMETRY leg** (a pure AC field drives both grades with the
same ⟨A²⟩ ⟹ S_axial=S_shear ⟹ ρ_eff=ρ_cold). **[DC-ONLY-DERIVED] LEAVES BOTH LEGS INTACT:** the
bond-frame content is COLD, fully consistent with the null; the nonzero AC scalar ⟨T⟩ is NOT a
stiffness deposit (Part 3), so it does not bear on either leg. **NO revision to #518 is warranted.** (The
#532 arc already RETRACTED its earlier "up-for-revision on the 2nd-order strain moment" row —
`pump-probe-tslot_result.md:464` — because the ⟨A_bond⟩ deposit was a boundary artifact; this arc
CONFIRMS that retraction and promotes it: on the clean ring the deposit is real but bond-frame-COLD, so
still no revision.) Surface only (do not perform); the auditor lane lands any manual note.

### (d) the cycle-mean-reads-COLD result — consistency — ✅ PASS (promoted to theorem)
The ring REPRODUCES #532's cycle-mean-COLD reading (#532 open chain: 0.9973; ring: 1.0000000000 —
cleaner, boundary removed) and PROMOTES it from a boundary-contaminated observation to a THEOREM: the
ring's boundary-free cycle-mean config STILL reads COLD, so the COLD result is forced (⟨y⟩=0 + closure),
not observed. This is the derivation's core consistency check with #532's own re-analysis.

---

## THE #528 RECONCILE-GATE (symbolic vs numeric ring, INDEPENDENT paths; can-fire proven)

The symbolic tilt (`bondframe_tslot_predictions.tilt_exact`) and the numeric-ring tilt
(`ring_bondframe_probe.measure_ring`) are two INDEPENDENT code paths (the #531 tautology guard,
test-asserted: the numeric module never imports the symbolic one). They reconcile through the #528
ReconcileGate (`reconcile_gate.py`) with the can-fire self-test running FIRST (proves the halt plumbing
is live), band = 6% (ring-commensurate-k snap + phase discretization, DERIVED). Can-fire proven on
**dropped-term** (claim=cold vs the real nonzero tilt → fires) and **sign-flip** (claim=−tilt vs +tilt →
fires) synthetics on the real comparator+halt path; vacuous-band gates refused at registration.

---

## LEDGER (canon-forced vs derived vs read-off; KNIFE armed)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(A)=k₀√(1−A²)` | CANON-FORCED | Ax4, `scale_invariant.py:107-156` |
| 2 | Tension `Φ'(A)=k₀(A√(1−A²)+arcsin A)/2` | DERIVED (sympy R1) | integrate once, `Φ'(0)=0` (R2) |
| 3 | `⟨A_bond⟩ = ⟨dy²⟩/2` | DERIVED THEOREM (R4/R5/R6) | convexity ½ + ring closure; NOT asserted ½ |
| 4 | `⟨dy²⟩ = y₀²(1−cos k)` | DERIVED (sympy R3) | traveling-wave phase average |
| 5 | tilt = `⟨Φ''(A)(dy/L)²⟩` = 0.01437 | DERIVED (quadrature) | validation gate vs #532 +0.013969 ✅ |
| 6 | dispersion `ω²=k_s(2−2cos k)` ⟹ k=1.28700 | DERIVED | cold shear-branch; ω=1.2 read-off (#532) |
| 7 | y₀ = 0.1428 tent edge | READ-OFF (#527/#529) | `axiom-register.md:189`; never tuned |
| 8 | O(y₀⁶) kernel correction −9.5×10⁻⁷ | DERIVED (series) | reconciliation (a) ✅ |
| 9 | Ring closure Σ Δu=0 | CANON-FORCED (host topology) | the clean-object constraint |
| 10 | bond-frame DC deposit = 0 | DERIVED THEOREM (Part 3) | ⟨y⟩=0 + closure ⟹ cold mean geometry |
| 11 | ½, ¼, 2/7, 9.7734, tilt value | KNIFE-ARMED | none tuned toward; exact zero theorem'd not observed |

**0 free parameters tuned toward 2/7 / 9.7734 / EXTENDED.** ω and y₀ read-off; k, tilt, mean-stretch,
bands, and the zero deposit all derived. **KNIFE=False:** the ½ is the convexity coefficient
(declared-derived); the tilt 0.01439 lands on no canon-distinguished value; the exact-zero deposit is
theorem'd (⟨y⟩=0 + closure), not observed.

---

## HONEST CLOSURE (Rule 11) — the fork closes DC_ONLY on a derived theorem; one mechanism explains all

The #526 T-slot fork asked whether a traveling transverse wave deposits a bond-frame tension the slow
probe feels (EXTENDED) or nothing (DC_ONLY). On the clean ring the answer is **DC_ONLY, as a theorem**:
the wave's odd symmetry (⟨y⟩=0) plus ring closure (no mean straight-bond stretch) force the cycle-mean
bond geometry to the cold geometry. **ONE mechanism** explains everything: the lab-frame stiffening is
the kinematic tilt `⟨Φ''(A)(dy/L)²⟩` (an AC-slope oscillation, identical on a linear chain); the
nonzero ⟨A_bond⟩ is a per-snapshot AC quantity, not a DC deposit; the #532 open-chain sign-flip was the
boundary freedom the ring removes. This is the discipline working: a clean analytic closure, mechanism
named, no rescue. The #532 [ADJUDICATION-INVALID] verdict correctly kept the fork OPEN; this arc closes
it on the clean host the #532 open-chain artifacts obscured.

**Substitution-not-retraction (Rule 12):** this does NOT refill any slot with an unverified hypothesis.
It derives the bond-frame content and reports both the DC verdict (cold) and the AC scalar (⟨T⟩/ℓ,
KEEP-BOTH). No new claim about a "pump-loaded operating point" is asserted.

---

## FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **#526 prestress T-slot scope fork** (`prestress-tensor_prereg_FROZEN.md`:64-78; #531 fork-record; #532 [ADJUDICATION-INVALID] OPEN) | **RESOLVE-DC_ONLY (candidate, Grant confirms the framing):** on the clean periodic ring the bond-frame O(y₀²) content of a traveling transverse wave is COLD, as a theorem (⟨y⟩=0 + ring closure ⟹ no DC deposit in the cycle-mean bond geometry). The #526 T-slot's DC-only scope MATCHES the clean-host dynamics at 2nd order. The lab-frame stiffening #532 measured is the kinematic tilt, not a bond-frame deposit. Provenance: `bondframe-tslot-closure_result.md`. |
| **#518 §7 radiation null** (`matter-stiffening-rho_result.md:146,:149`) | **UNTOUCHED — the null STANDS (both legs).** [DC-ONLY-DERIVED] is fully consistent with both the ⟨A⟩=0 field-mean leg AND the ⟨A²⟩ channel-symmetry leg. NO revision warranted. Confirms + strengthens the #532 retraction of the "2nd-order strain moment" revision. |
| **#529 [RADIATION-CONTAMINATED]** (`resonant-tension-law_result.md`) | **CONSISTENT / independent.** The #529 law ⟨T⟩=(k_a/ℓ)y₀² is the AC per-snapshot scalar (this arc reproduces it as ⟨T⟩/ℓ=⟨dy²⟩/2, KEEP-BOTH). This arc shows that scalar is NOT the bond-frame content a slow probe feels — corroborating #529's own finding that the slot-⟨T⟩ cannot serve as a matter/radiation discriminator (it stiffens both). No new adjudication. |
| **The pre-test-physics-check framing fork** (bond-frame probe reading: cycle-mean-config vs slot-⟨T⟩) | **ENGINE-DECIDED (Trigger 9):** the two readings ARE two different quantities (Part 3); the derivation states which is the #526 tensor input (the cycle-mean-config tangent stiffness a slow probe feels) and reports both. Grant's framing call refines which is "the probe" for the corpus; the numbers are engine-decided. Surfaced for Grant at review (§FLAGS-2). |

**No rewrites performed.** Resolve / untouched / consistent / engine-decided ROWS only; the auditor lane
lands the manual entries.

---

## FLAG-DON'T-FIX — surfaced, not resolved

1. **THE OPEN-CHAIN SIGN RECONCILIATION SCOPE (reconciliation (b)).** My static-relaxation open-chain
   model reproduces the #532 GRADIENT STRUCTURE and boundary-config sensitivity (free-end gradient 200×
   the pinned), but NOT #532's exact −0.0026 (pinned) / −0.0083 (free) node-200 *negative* values. My
   clamped-standing static relaxation gives positive whole-chain means; #532's negatives come from the
   full traveling-wave time-domain dynamics with a specific probe node down the boundary gradient. The
   LOAD-BEARING point (open = boundary-set/position-dependent; ring = boundary-free theorem) is robust,
   but the exact sign-and-magnitude match to #532 is OUT OF SCOPE for the analytic path (a) and would
   need the #532 time-domain driver. Surfaced, NOT force-matched (flag-don't-fix).

2. **THE BOND-FRAME-PROBE FRAMING FORK (Grant's to confirm).** The verdict rests on identifying "the
   #526 tensor input" as the cycle-mean-config bond-frame tangent stiffness (COLD) rather than the
   slot-averaged ⟨T⟩/ℓ (nonzero AC scalar). The derivation shows these ARE two different quantities and
   that the #526 slot form `k_s + T/ℓ` requires a straight-stretched bond (which the wave does not
   produce). This is a framing/scope call surfaced for Grant per pre-test-physics-check Trigger 9;
   the engine decides the numbers, Grant confirms which quantity the corpus calls "the probe." A ruling
   toward the slot-⟨T⟩ reading would re-bin to [BULK-DEPOSIT-DERIVED] with the DERIVED coefficient
   ⟨T⟩/ℓ = ⟨dy²⟩/2 (reported KEEP-BOTH, ready if Grant rules that way).

3. **Cauchy-only, 2-DOF ring scope.** The srs z=3 cell-scale relaxation and the Cosserat couple-stress
   carrier (Stage 2) are out of scope; this is the minimal honest clean carrier of the transverse↔axial
   coupling, matching the #526/#532 Cauchy scope.

---

## Cross-references (grep-verified at branch HEAD this session)

- Prereg (FROZEN): `research/2026-07-05_bondframe-tslot-closure_prereg_FROZEN.md`
- Prediction / driver / tests / output: see header
- #532 [ADJUDICATION-INVALID] (the fork this closes): `research/2026-07-05_pump-probe-tslot_result.md`:16,:73,:77,:464
- #531 fork-record: `research/2026-07-05_channel-resolved-loading_result.md`
- #526 T-slot scope + slot form: `research/2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78; `prestress_elastic_tensor.py`:124-129 (`k_shear_eff = k_shear + T/ell`, `T = Φ'(A_axial)`)
- #529 ⟨T⟩ law: `research/2026-07-04_resonant-tension-law_result.md`:27
- #527 chord-vs-arc tent lesson: `research/2026-07-04_bond-force-sign-rule_result.md`:80-91
- #518 null (both legs): `research/2026-07-04_matter-stiffening-rho_result.md`:146 (field-mean), :149 (channel-symmetry)
- Kernel: `src/ave/axioms/scale_invariant.py`:107-156
- ReconcileGate (#528): `src/ave/validation/reconcile_gate.py`
- arc* tent band (y₀ read-off): `manuscript/ave-kb/common/axiom-register.md`:189
- T2 homonym guard: `resonant-lc-solitons.md`:95,:128 (A1⊥T2, Grant-ratified 2026-06-14)
