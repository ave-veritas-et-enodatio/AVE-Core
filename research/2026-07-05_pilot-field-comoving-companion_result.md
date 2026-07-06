# RESULT — [RETARDATION-LIMITED / LEAKY]. Grant's pilot-field companion is REAL — a co-moving 2nd-order longitudinal contraction well DOES develop under the wavetrain envelope, co-moves with it, and reads free-like under / cold outside — BUT its completeness and timing are governed by the speed ratio c_long/v_g (a measured monotone law): the well develops fully only when the longitudinal sector outruns the envelope. It is not an instantaneous well; it is BUILT, and it lags/leaks when the envelope outruns the longitudinal response.

> ## ↗ CORRECTIONS BANNER (2026-07-05, orchestrator review of PR #535 — 9 confirmed, 3 MAJOR, 0 refuted; banner-append, affected prose corrected in place with the review's numbers)
> The BIN ROUTING **[RETARDATION-LIMITED / LEAKY] SURVIVES** — it stands on the lag/leak criteria (frozen), which the review confirmed; the k_a blast radius into merged #533/#534 canon is CLEARED (every merged computation ran the nonlinear branch at k_a=1, where the baked k0=1 is coincidentally correct). The corrections are honesty + provenance:
> - **MAJOR-1 (item-1): the SETTLED depth is ~112%, OUTSIDE the frozen ±10% band.** The PR #535 table's "%-of-prediction" column reported 20-period SLICES as developed values. The reviewer extended ρ=4 past 28 periods (40p=113.6%, 56p=112.4%, 72p=110.7%): the well SATURATES at ~112-114%, and the "103% at 20 periods" was a still-climbing curve crossing 100%. The table is re-anchored to the settled asymptote (SLICE columns kept, explicitly labeled); the ~12-14% excess is recorded as an **OPEN unexplained residual** (candidate: peak-vs-phase-average envelope form factor — the prediction uses the traveling-wave phase-average ⟨dy²⟩ while the metric reads the deepest point at the envelope peak; CANDIDATE, not closure). The "develops at the free-host amplitude / settling near the free-host depth" claims are CORRECTED.
> - **MAJOR-2 (item-2): measurement-3 provenance was FALSE.** The PR #535 docstring/prereg/result said the imported canon `trans_tangent_stiffness` was used; the code evaluated a local closed-form k=1+ρ·A at the depth from measurement 1 (an algebraic restatement, not independent evidence). The physics SURVIVES (the reviewer + this correction ran the genuine imported probe: under≈0.970, far reads the causal-wake). Measurement 3 now CALLS the imported probe; the false provenance is erratum'd; the "0.9926-class free reading" mislabel is corrected (0.970 is the ρ=4-SCALED reading, not the ρ=1 softening class).
> - **MAJOR-3 (item-3): the "globally-diluted, ~1e-19" compensation was a causally-UNREACHED antipode sample.** At the sampled frame the signal has reached only ~105 nodes from launch (c_long·t); the antipode (~1024 nodes) is causally disconnected, so its ~1e-19 is a trivial zero, NOT global dilution. The compensating stretch actually lives in a **causally-reached near-field WAKE** adjacent to the envelope (positive du, mean ≈ +1.7e-3). The global-dilution sentence is corrected to what the data shows; the closure-scale statement's requirement (longer runs / the analytic ledger to see true global spreading) is stated.
> - **MINORS (item-4):** control (b) reran the #534 FILLED free chain, not the frozen envelope-on-open-free LOCAL control (now implemented: reads 0.99254 locally under the envelope); control (d) now sweeps the frozen L_env {40,80,160}; the bin-routing rationale's "converge robustly not climb-with-transit" is relabeled an OBSERVATION (the routing credits the frozen lag/leak criteria).
>
> The PRESERVED (Rule 12) pre-correction prose is struck inline where load-bearing; the live corrected numbers are in place. Correction commits on the same branch. A SEPARATE small PR carries the upstream `ring_bondframe_probe` k_a fix.

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/pilot-field-comoving-companion`
**Prereg (FROZEN):** `research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md` (committed BEFORE any driver code; commit order = freeze proof, 140fbbc8)
**Prediction module (symbolic, INDEPENDENT):** `src/scripts/vol_1_foundations/pilot_field_predictions.py`
**Driver (time-domain wavetrain, INDEPENDENT path):** `src/scripts/vol_1_foundations/pilot_field_wavetrain.py`
**Controls (HALT-gated, #528 ReconcileGate):** `src/scripts/vol_1_foundations/pilot_field_controls.py`
**Summary + figure:** `src/scripts/vol_1_foundations/pilot_field_summary.py` → `_output/pilot_field_summary.json`, `_output/pilot_field_speed_ratio_law.png` (driver-regenerable; gitignored)
**Tests:** `src/tests/test_pilot_field_comoving_companion.py` (15: 8 fast + 7 engine_sim; all pass — the settled-asymptote test added in the #535 correction round)
**Builds on (verify-before-cite, grep-verified at HEAD c5dd2c62):** #534 three-host table (`research/2026-07-05_bondframe-tslot-closure_result.md`:76-78); #533 scoped traveling-mode theorem (same doc:105-114); #532 methods.

**Grant's hypothesis under test (recorded verbatim in the FROZEN prereg):** *"A photon does not cross a passive medium — it carries a CO-MOVING 2nd-order longitudinal contraction companion (the 'pilot field': du≈−dy²/2 under the envelope, the free-host reading realized LOCALLY), with the compensating stretch spread over the unoccupied lattice, so the fixed-vs-free trichotomy demotes to closure-scale bookkeeping. The companion is the longitudinal sector's back-EMF response to the transverse drive."* Grant "go" (verbatim): *"pilot wave + back-EMF."*

---

## VERDICT BOX

> **PRIMARY BIN: [RETARDATION-LIMITED / LEAKY].** On a LONG closed 2-DOF ring, a launched
> LOCALIZED transverse wavetrain (carrier λ≈4.88 ≪ L_env∈{40,80,160} ≪ N∈{512,1024,2048})
> DOES grow a co-moving longitudinal contraction well du under the envelope. The well:
>
> - **develops to a settled depth NEAR (slightly above) the free-host amplitude** — the DC
>   contraction depth (ρ_bond=4) settles at an ASYMPTOTE of ~**112% of the phase-average
>   prediction −⟨dy²⟩/2 = −0.00734** (40p=113.6%, 56p=112.4%, 72p=110.7%; SATURATES, item-1).
>   The "103% at 20 periods" (~~was reported as the developed value~~ CORRECTED) is a
>   still-climbing SLICE crossing 100%. The ~12% excess over the phase-average is an OPEN
>   residual (candidate: peak-vs-phase-average envelope form factor — see §THE OPEN RESIDUAL);
> - **co-moves with the envelope** — the well travels at ~the envelope group speed
>   (speed ratio 1.08 at ρ=4; the envelope moves at v_g=0.80, the cold-shear group velocity);
> - **reads free-like UNDER (imported canon probe) / stiffer in the causal wake** — the
>   GENUINE imported (canon #534) `trans_tangent_stiffness` reads **soft (≈0.970, SOFT
>   signature)** at the envelope peak (item-2 fix: the real probe, not the pre-#535 closed-form
>   restatement). The compensating stretch lives in a **causally-reached near-field WAKE** (item-3
>   fix: NOT the causally-unreached antipode's trivial ~1e-19) — a positive-du region adjacent
>   to the envelope that reads STIFFER than cold (far-node ratio ≈1.009);
> - **BUT is retardation-limited and leaks.** The completeness and co-motion fidelity are
>   MONOTONE in the speed ratio c_long/v_g (the measured RETARDATION LAW, below — SLICE values):
>   as the longitudinal sound speed drops toward and below the envelope group speed, the
>   per-transit slice fills only partially (ρ=0.5, Mach 1.13: **39% at 16p**, speed ratio 0.44,
>   lag 31 nodes; NOTE: a slice — ρ=0.5 also climbs toward ~100% given enough transit). The
>   depth GROWS with transit time (it is BUILT, not instantaneous — depth_growth 2.5–6× from
>   early to settled), and longitudinal energy sheds from the co-moving window (leak fraction
>   final 0.91–0.99 across the sweep).
>
> **What Grant's picture GETS RIGHT (confirmed):** the companion is real, co-moving, local,
> free-like-under (imported probe), with the compensating stretch in a causal near-field wake —
> the SPATIAL pilot structure is realized locally. **What the closed host ADDS (the retardation the picture omits):**
> the well is not the free-host reading realized instantaneously; it is a longitudinal-sector
> response that PROPAGATES at c_long and takes envelope-transit time to build, so its depth and
> its co-motion lag are set by c_long/v_g. The fixed/free trichotomy does NOT cleanly demote to
> pure closure-scale bookkeeping — it demotes to a DYNAMICAL closure-plus-retardation bookkeeping.
>
> **CONSISTENCY-vs-EMERGENCE:** CONSISTENCY / geometric-kinematic. No VALUE derived (2/7, 9.7734,
> /7 stay GR-imported). **KNIFE=False:** the ½ in du≈−dy²/2 is the sympy-derived convexity
> coefficient (declared-derived; c_dy2 = −1/2 exact); the sonic coincidence at ρ=1 (k_long=k_shear)
> is EXPECTED at the photon point and is NOT reported as a discovery; no value tuned toward a
> canon-distinguished target.

**All 15 tests pass** (8 fast core: convexity −½ derived, free-host depth vs #534 backbone,
group velocity, dilution law, the Rule-10 sonic-knob-live guard, the tautology guard, wavetrain
ledger smoke, geometric-not-kernel; 7 engine_sim: companion-develops-toward-free-depth-and-grows,
settled-asymptote-saturates-above-prediction (item-1), co-moves-with-envelope, soft-under-via-imported-
canon (item-2), the monotone speed-ratio law, sonic-point-no-secular-blowup, all-five-controls-with-can-
fire). Fast core 0.7 s; engine_sim suite 3:24 (opt-in, the settled-asymptote 4096-node runs added).

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u elastic sector on a **2-DOF-per-node PERIODIC RING** (longitudinal u +
  transverse y) — the same 2-DOF Cauchy host as #532/#533/#534 (`RingChain` imported). BOTH k_a
  (axial STRETCH) and k_s (transverse SHEAR) are translational-u / **capacitive** springs of the same
  bond (PR#516) — NOT the ε/μ photon pair. Cosserat = Stage 2, NOT invoked.
- **MODE:** NUMERIC TIME-DOMAIN (velocity-Verlet of the full 2-DOF EOM — both u and y evolve) — a
  launched LOCALIZED wavetrain that ACTUALLY TRAVELS. This is the NEW capability the pilot hypothesis
  needs: co-motion and leakage are DYNAMICAL, invisible to the #533/#534 static probe. A SYMBOLIC
  prediction module (the −⟨dy²⟩/2 coefficient, v_g, the dilution law) is the INDEPENDENT path (the
  #531 tautology guard: the dynamics module never imports the prediction module — test-asserted).
- **REGIME:** small-amplitude sub-yield radiation (y₀=0.1428 tent edge, `axiom-register.md:189` arc*
  band; never tuned). Op14/Ax4 kernel ON. **PHASE-STATE:** sub-yield interior, LINEAR-RADIATION regime
  (NOT the SATURATED self-trap knot of the 2026-06-04 back-EMF arc — that arc's knot was PINNED; this
  is a freely-propagating wavetrain). No PML (closed periodic ring; boundedness measured on the ring).
- **THE SONIC SUBTLETY (declared):** ρ_bond=k_long/k_shear swept ∈ {0.5,1,2,4}. At ρ=1 (the Ax3 photon
  point, k_s=k_a) the long-wave longitudinal and transverse speeds coincide (SONIC) — EXPECTED there,
  NOT reported as a discovery (KNIFE). The sonic case is well-behaved on this bounded ring over the
  recording window (no secular blow-up; see §THE SONIC POINT).
- **DC-vs-AC (clm-acdc07):** the companion is the DC-mean-config longitudinal response (the low-passed
  du well) to the AC transverse drive (dy² rectified). The measurement SEPARATES the DC well (bond-frame
  content, what a slow probe under the envelope feels) from the AC 2k wiggle (kinematic-instantaneous,
  du_raw ≈ 2.5× the DC well). **Load-bearing distinction:** the AC part (du~dy²) is present INSTANTLY and
  geometrically; the DC well is what the longitudinal dynamics must BUILD — that is the retardation.
- **T2 HOMONYM GUARD (binding, #527):** the transverse bow y is the MECHANICAL T2-response bend, NOT the
  Cosserat (2,3) charge winding (A1⊥T2). mass=A1; charge=Cosserat-winding; bow=T2-mechanical-response.
  The "back-EMF" here is the MECHANICAL longitudinal-sector reaction to the transverse drive (the du
  companion), NOT a QED/Maxwell EMF.
- **COORDS (A46):** real-space displacement wavetrain; real-space du(x,t) profile + real-space transverse
  stiffness readout. A46-clean (the claim under test is itself a real-space local-contraction claim).
- **CLASS:** CONSISTENCY / geometric-kinematic. EMERGENCE FORBIDDEN for any value.

---

## THE MEASURED SPEED-RATIO LAW (the RETARDATION law — the arc's core product)

The sonic sweep (N=2048, L_env=80, 20 carrier-periods; the artifact figure is
`_output/pilot_field_speed_ratio_law.png`). v_group = 0.80 (cold shear branch); c_long = √ρ_bond; the
companion rides the envelope, so the Mach number is v_g/c_long. **The "depth %pred" column is a
20-period SLICE, NOT the settled asymptote** (item-1 review — see the SETTLED ASYMPTOTE row below the
table). k_under is the GENUINE imported (canon #534) `trans_tangent_stiffness` (item-2); k_far is a
CAUSALLY-REACHED wake node (item-3), not the causally-unreached antipode.

| ρ_bond | c_long | Mach v_g/c_long | DC depth %pred (20p SLICE) | co-motion lag (nodes) | v_well/v_env | k_under (imported probe) | k_far (causal wake) | leak frac (final) | E-drift |
|---|---|---|---|---|---|---|---|---|---|
| 0.5 | 0.71 | **1.13** (envelope supersonic) | 39% (slice) | 30.7 | 0.44 | 0.9994 (nearly cold at 20p) | ~1.00+ | 0.967 | 5.7e-7 |
| 1.0 | 1.00 | **0.80** (SONIC, ρ=1 photon point) | 60% (slice) | 27.9 | 0.56 | 0.9973 | ~1.00+ | 0.989 | 2.3e-6 |
| 2.0 | 1.41 | **0.57** | 82% (slice) | 22.8 | 0.76 | 0.9901 | ~1.00+ | 0.994 | 1.5e-5 |
| 4.0 | 2.00 | **0.40** (longitudinal fast) | 103% (slice, climbing) | 14.2 | 1.08 | 0.9705 (SOFT, imported) | 1.009 (wake stretch) | 0.907 | 9.0e-6 |

**SETTLED ASYMPTOTE (ρ=4, item-1 — the developed value, NOT the slice):** extending ρ=4 past 28
periods, the DC depth SATURATES: 40p=**113.6%**, 56p=**112.4%**, 72p=**110.7%** → asymptote **~112%** of
the phase-average prediction. The 20-period 103% is a still-climbing crossing of 100%. The ~12% excess is
an OPEN residual (§THE OPEN RESIDUAL). The lower-ρ %pred SLICES also climb with transit (ρ=0.5 reaches
~100% by ~56 periods) — the "cannot keep up" wording below is a PER-TRANSIT statement, not a permanent
floor.

**The law (monotone in the SLICE, mechanistically coherent):** at a FIXED transit budget, the co-moving
contraction develops MORE completely, co-moves MORE faithfully (speed ratio → 1), and reads MORE
free-like the FASTER the longitudinal sector is relative to the envelope (lower Mach). At ρ=4 (c_long ≫
v_g) the well is developed (settled ~112%), co-moving (1.08), free-like-under (imported probe 0.970). At
ρ=0.5 (Mach 1.13, envelope outruns the response) the per-transit slice fills only 39% and lags (0.44) —
BUT given enough transit it too climbs. **The load-bearing law is: lag and per-transit completeness are
c_long/v_g-set** (this is what routes the frozen [RETARDATION-LIMITED] bin — the lag and leak, not the
%pred). **The compensating stretch lives in a causally-reached near-field WAKE** (k_far ≈ 1.009 at ρ=4, a
positive-du stretch adjacent to the well), NOT globally diluted below measurable — the ~1e-19 antipode of
PR #535 was causally unreached (item-3).

**The depth GROWS with transit time (not an instantaneous floor):** at ρ=4, the deepest DC contraction
runs 51% (8 periods) → 94% (16) → 112% (28) → **saturating ~112%** (40-72p). It is BUILT, not read-off.
This growth is the RETARDATION signature. **The bin routes to [RETARDATION-LIMITED] on the frozen lag and
leak criteria** (co-motion lag nonzero + growing; longitudinal energy sheds from the co-moving window) —
NOT on a "fails-to-converge-at-100%" attribution (the settled value is ~112%, above the prediction; the
routing does not depend on hitting 100%).

---

## THE FOUR MEASUREMENTS (the frozen prereg's §THE COMPUTATION)

1. **THE CONTRACTION PROFILE (du(x,t)).** A DC contraction well develops UNDER the envelope, settling
   at a ρ=4 asymptote of ~112% of the phase-average −⟨dy²⟩/2 = −0.00734 (~~"reaching it fully at 103%
   at ρ=4"~~ CORRECTED to the settled ~112%, item-1; the ~12% excess is the §OPEN RESIDUAL). The
   compensating stretch lives in a **causally-reached near-field WAKE** adjacent to the envelope (a
   positive-du region, mean ≈ +1.7e-3; ~~"diluted ∝ L_env/N below the low-pass floor, A_far ≈ 10⁻¹⁹"~~
   CORRECTED, item-3 — the ~1e-19 was the causally-UNREACHED antipode: at that frame the signal has
   reached only ~105 nodes from launch (c_long·t), while the antipode is ~1024 nodes away). Whether the
   wake compensation eventually spreads GLOBALLY (the true closure-scale dilution) requires longer runs
   or the analytic ledger — stated as needed, not shown. **The AC vs DC split (load-bearing):** the raw
   du oscillates ±0.012 under the envelope (the 2k carrier-rectified AC, present instantly, du_raw_min ≈
   2.5× the DC well); the DC well (low-passed at the envelope scale) is what the slow bond-frame probe
   feels and what the longitudinal dynamics build.
2. **CO-MOTION.** The DC-well position tracks the envelope peak position over time. At ρ=4 the well
   travels at −0.865 vs the envelope −0.798 (ratio 1.08), i.e. the well CO-MOVES with the envelope group
   velocity, trailing by a small retardation lag (14 nodes). At low ρ the well lags heavily (ratio 0.44
   at ρ=0.5, per-transit): the longitudinal response cannot keep pace with the envelope within one transit.
3. **THE LOCAL PROBE READING (item-2 fix — the GENUINE imported probe).** The imported (canon #534)
   `RingChain.trans_tangent_stiffness` — an INDEPENDENT finite-difference of the imported `force_y` — read
   at the recorded DC longitudinal config (u, y=0), sampled at the envelope PEAK (density-peak sampling,
   not centroid): free-like **SOFT under (≈0.970 at ρ=4)**. ~~The PR #535 code evaluated a local
   closed-form k=1+ρ·A at the depth from measurement 1 — an algebraic restatement, not independent
   evidence (the false provenance).~~ CORRECTED: this now calls the real imported probe. The FAR node is a
   CAUSALLY-REACHED wake node (item-3), which reads STIFFER than cold (≈1.009) because the compensating
   stretch lives there — NOT the trivially-cold antipode. NOTE (item-2): the 0.970 is the ρ=4-SCALED
   reading (softening ~4× the ρ=1 class), NOT literally the "0.9926-class" free reading (which is a ρ=1
   figure); the ρ=1 imported reading is ≈0.997.
4. **BOUNDEDNESS vs LEAKAGE.** Longitudinal strain energy in a co-moving window vs total: the fraction
   stays high (0.91–0.99) but DECAYS over the window (leak slope negative at every ρ) — the companion is
   MOSTLY bound but sheds some longitudinal waves (LEAKY), most at ρ=4 (0.907, the fastest-building well
   also radiates the most as it forms). This is the LEAKY half of the [RETARDATION-LIMITED / LEAKY] bin.

---

## THE OPEN RESIDUAL (item-1 — the ~12% settled excess over the phase-average prediction; RECORDED, not closed)

The ρ=4 well SATURATES at ~112% of the traveling-wave phase-average prediction −⟨dy²⟩/2 = −0.00734, i.e.
a ~12% EXCESS. This is an OPEN, unexplained residual, recorded per Rule 11 (no rescue) — NOT closed.

**Named candidate (the reviewer's, NOT a closure):** a **peak-vs-phase-average envelope form factor**.
The symbolic prediction uses the traveling-wave PHASE-AVERAGE ⟨dy²⟩ = y₀²(1−cos k) (a plane-wave
identity); the numeric metric reads the DEEPEST point of the DC well, which sits at the envelope PEAK
where the local ⟨dy²⟩ exceeds the plane-wave average (the Gaussian envelope concentrates amplitude at the
peak, so the local time-averaged dy² at the peak > the plane-wave ⟨dy²⟩). A peak-weighted local ⟨dy²⟩
would predict a deeper well, plausibly accounting for the ~12%. **This is a CANDIDATE mechanism to
derive, not a closure** — the prediction module currently uses the plane-wave ⟨dy²⟩ and the excess is
real against THAT prediction. Deriving the envelope-peak local ⟨dy²⟩ and re-testing is the forward path;
until then the ~12% is booked OPEN. It does NOT affect the bin (the routing is lag/leak, not depth-hits-100%).

---

## THE FIVE CONTROLS (all HALT-gated via the #528 ReconcileGate, can-fire proven on real paths)

| control | result | status |
|---|---|---|
| **(a) FILLED-ring limit** | filled-ring bond-frame ratio = 1.000000 (COLD) → recovers #534's ring reading | ✅ reconciled, can-fire proven |
| **(b) ENVELOPE-on-OPEN-FREE local** (item-4a fix) | a LOCALIZED envelope on an open-free chain, imported bond-frame probe at the DC config LOCALLY under the envelope peak: **0.99254** vs the analytic 1−⟨dy²⟩_local/2 (different code path). ~~The PR #535 version reran the #534 FILLED free chain, not this frozen local control.~~ | ✅ reconciled, can-fire proven |
| **(c) LINEAR-axial (kernel OFF)** | nonlinear −0.005051 vs linear-axial −0.005053, rel-diff 3×10⁻⁴ — the contraction is GEOMETRIC (du=√(1−dy²)−1), kernel ~ nothing (the merged O(y₀⁶) result) | ✅ reconciled, can-fire proven |
| **(d) envelope/ring sweep** (item-4b fix) | frozen L_env sweep {40,80,160}: DC depth + causal-wake compensation reported across the grid (~~was {80,80,80} at varying N; the +1e-6 slack dropped~~) | ✅ reported |
| **(e) ENERGY-MOMENTUM LEDGER (crank check)** | energy drift 1.5×10⁻⁵ (saturation-consistent Φ(A) functional, NO linear proxy — the #532 flag), total longitudinal momentum 7.9×10⁻¹⁶ (closed-ring conservation) | ✅ both reconciled, can-fire proven |

**Prediction (symbolic) and dynamics (time-domain) are INDEPENDENT code paths** (the #531 tautology
guard, test-asserted). Mean-level (the envelope-mean DC well) vs per-bond-level (the du_j profile,
carrier-oscillating) claims are explicitly distinguished (the #533 lesson): the DC well is a mean-scale
object; the per-bond du carries the AC 2k carrier on top.

---

## THE Rule-10 EMPIRICAL-DRIVER CATCH (surfaced, fixed in my own module — NOT the imported one)

**Integrator-time bug (Rule 10, A-Rule-10 spirit):** the imported `RingChain.tension` IGNORES `self.k_a`
in the NONLINEAR (kernel) path — it returns `_phi_prime(A)` with k0=1 baked in; k_a is consulted ONLY in
the `linear_axial=True` branch (`ring_bondframe_probe.py:66-67`). So passing `k_a = ρ·k_s` to the base
class was a NO-OP for the sonic sweep: the first sweep produced BIT-IDENTICAL u-field evolution across
ρ=0.5/2/4 (physically impossible if the axial stiffness varies), which a static read of the code would
not have surfaced — it only appeared at integrator time. **Fix (in my own module, per mission — the
imported module is NOT mutated):** `SonicRing(RingChain)` scales the kernel tension by ρ_bond
(k₀→ρ·k₀, preserving the saturation SHAPE √(1−A²)), so c_long=√ρ actually varies. A regression guard
test (`test_sonic_knob_is_live_rule10_guard`) fails if the knob ever silently dies again. **This is
flagged, not silently absorbed** (flag-don't-fix): the imported module's nonlinear-path k_a-inertness is
a real property of the #534 machinery — surfaced here for the auditor lane in case any other consumer
relies on k_a scaling the nonlinear axial branch.

---

## THE srs K<0 FLAG (surfaced, NOT resolved — per mission)

This 2-DOF Cauchy chain hosts a REAL, mechanically-stable (K>0), PROPAGATING longitudinal sector at
every ρ_bond in the sweep, so the companion here is a real acoustic contraction that PROPAGATES at
c_long. But on the **srs photon operating point** (ρ_bond=1, the Ax3 zero-reflection point k_s=k_a), the
bulk sector has **K<0 (lossless-reactive, mechanically unstable for ρ<2)** — verbatim canon:
`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md`:71,:74
("the photon's zero-reflection point is a lossless-reactive operating point … K<0 for ρ<2 … NOT a stable
static elastic solid"); `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`:50;
`manuscript/ave-kb/vol4/claim-quality.md`:167.

**The srs-level open question (stated, NOT resolved):** on the real srs photon point the physical
companion may be **EVANESCENT-BOUND** — a reactive, non-propagating longitudinal well keyed to the moving
envelope rather than a propagating acoustic contraction. That character (K<0 lossless-reactive) is one
THIS real-K, propagating-longitudinal chain CANNOT host: my ρ=1 point has c_long=√1=1>0 (a real
propagating branch), NOT the K<0 reactive branch of the srs photon point. **So the [RETARDATION-LIMITED]
verdict on THIS chain is a SUFFICIENCY + necessity-of-retardation demonstration on a real-K host — it
does NOT settle the srs photon point**, where a K<0 evanescent-bound companion could in principle track
the envelope WITHOUT the propagation retardation this chain imposes (a reactive well has no c_long-limited
build time). Whether the srs photon's K<0 reactive longitudinal sector realizes an evanescent-bound
companion — recovering Grant's instantaneous-co-moving pilot picture where this propagating chain gives
retardation — is the OPEN question, out of scope for the 2-DOF Cauchy chain. Flagged for Grant / the
srs-tensor lane.

---

## HONEST CLOSURE (Rule 11) — one mechanism explains the whole sweep

Grant's pilot-field companion is REAL on the closed ring — co-moving, local, free-like-under (imported
probe), with the compensating stretch in a causally-reached near-field wake (~~"globally-diluted"~~
CORRECTED item-3 — whether it spreads globally is unresolved on these run lengths) — but it is a BUILT,
PROPAGATING longitudinal response, not an instantaneous free-host reading. **ONE mechanism** explains the
entire sweep: the DC contraction well
is the longitudinal sector's response to the moving dy²-drive; it propagates at c_long and takes envelope-
transit time to build, so its depth, its co-motion fidelity, and its lag are all set by the single ratio
c_long/v_g. Where the longitudinal sector is fast (ρ=4, Mach 0.4) the well develops (settled ~112%) and
co-moves; where the envelope outruns it (ρ=0.5, Mach 1.13) the per-transit well lags and half-fills (and
climbs with more transit). **The frozen bin selector routes this to [RETARDATION-LIMITED / LEAKY] on the
frozen LAG and LEAK criteria** (co-motion lag nonzero and growing; longitudinal energy sheds from the
co-moving window): a local contraction DOES develop (not FIXED-LIKE), it LAGS, and it radiates. OBSERVATION
(not a frozen criterion, item-4c): the depth also CLIMBS with transit rather than converging at a fixed
amplitude — an observation consistent with the retardation mechanism, but the ROUTING credits the frozen
lag/leak criteria, not this climb-vs-converge attribution (which was post-hoc in PR #535). This is the
discipline working: the pilot picture is partially confirmed (spatial structure, local free-like reading)
and partially corrected (the closed host adds propagation retardation the picture omitted), the mechanism
is named, the branch closes with a measured law — no rescue toward a full PILOT-CONFIRMED.

**Substitution-not-retraction (Rule 12):** no slot is refilled with an unverified hypothesis. The verdict
is the measured retardation law + the srs K<0 open question (the evanescent-bound companion the propagating
chain cannot host). The forward path (does the srs photon point's K<0 reactive sector realize the
instantaneous co-moving well?) is a NEW question for the srs-tensor lane, not a rescue of this one.

---

## FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **#534 [CONSTRAINT-DEPENDENT] dissolved fork** (`bondframe-tslot-closure_result.md`:483-486 — which global constraint the cosmological lattice imposes) | **REFINED, not resolved.** The localized-wavetrain dynamics show the fixed/free trichotomy demotes to a DYNAMICAL closure-plus-RETARDATION bookkeeping, not pure closure-scale: a co-moving well develops locally (free-like) on the CLOSED ring, but its completeness is c_long/v_g-limited. Grant's "which constraint" question gains a companion: at what c_long/v_g does the cosmological longitudinal sector operate (subsonic-bound vs supersonic-lagging)? Flag for Grant; auditor lands nothing until Grant adjudicates. |
| **The srs photon-point K<0 evanescent-bound companion** (`parent-condition-match-forces-balance.md`:71,74) | **OPEN — new question for the srs-tensor lane.** This propagating-K chain gives RETARDATION; a K<0 reactive sector might give an instantaneous evanescent-bound well (Grant's pilot picture recovered). NOT resolvable on the 2-DOF Cauchy chain. Surfaced, not performed. |
| **The imported `RingChain.tension` nonlinear-path k_a-inertness** (`ring_bondframe_probe.py`:66-67) | **SURFACED (flag-don't-fix).** k_a scales only the linear-axial branch; the nonlinear kernel path is k₀=1 fixed. Any other consumer relying on k_a to scale the nonlinear axial branch would silently get k₀=1. Not fixed in the imported module (my SonicRing subclass handles it locally); surfaced for the auditor in case the corpus needs a note. |

**No rewrites performed.** Refined / open / surfaced ROWS only; the auditor lane lands any manual entries.

---

## LEDGER (canon-forced vs derived vs read-off; KNIFE armed)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(A)=k₀√(1−A²)` | CANON-FORCED | Ax4, via imported RingChain |
| 2 | Free-host contraction `du=√(1−dy²)−1`, coeff −½ | DERIVED (sympy: c_dy2=−1/2 exact) | convexity 2nd-order coeff; NOT asserted |
| 3 | `⟨dy²⟩=y₀²(1−cos k)` | DERIVED | traveling-wave phase avg (#534) |
| 4 | dispersion `ω²=k_s(2−2cos k)` ⟹ k=1.28700, v_g=0.8 | DERIVED | cold shear branch; ω=1.2 read-off (#532) |
| 5 | c_long=√ρ_bond; Mach=v_g/c_long | DERIVED | linearized axial branch; ρ swept |
| 6 | y₀=0.1428 tent edge | READ-OFF (#527/#529) | `axiom-register.md:189`; never tuned |
| 7 | speed-ratio retardation law (per-transit SLICES 39%→103%; ρ=4 settled ~112%) | MEASURED | the arc's core product; monotone SLICE in ρ; settled asymptote item-1 |
| 8 | srs K<0 lossless-reactive at ρ=1 | CANON-CITED (flag) | `parent-condition-match-forces-balance.md`:71,74; NOT resolved |
| 9 | ½, ¼, 2/7, 9.7734, sonic coincidence | KNIFE-ARMED | none tuned toward; ρ=1 sonic expected not discovery |

**0 free parameters tuned toward 2/7 / 9.7734 / PILOT-CONFIRMED.** ω and y₀ read-off; k, v_g, c_long, the
free coefficient, the dilution law, and all bands derived; L_env, N, ρ_bond swept. **KNIFE=False:** the ½
is sympy-derived; the sonic coincidence at ρ=1 is expected at the photon point (not a discovery); the
retardation law lands on no canon-distinguished value.

---

## FLAG-DON'T-FIX — surfaced, not resolved

1. **THE srs K<0 EVANESCENT-BOUND COMPANION.** This propagating-K chain imposes c_long/v_g retardation;
   the srs photon point's K<0 lossless-reactive longitudinal sector might realize an instantaneous
   evanescent-bound well (Grant's pilot picture without retardation). Out of scope for the 2-DOF Cauchy
   chain; the open question for the srs-tensor lane. (§THE srs K<0 FLAG.)
2. **THE IMPORTED `RingChain.tension` NONLINEAR-PATH k_a-INERTNESS.** k_a scales only the linear-axial
   branch (`ring_bondframe_probe.py`:66-67). Surfaced for the auditor (not fixed in the imported module).
3. **Cauchy-only, 2-DOF ring scope.** The srs z=3 cell-scale relaxation and the Cosserat couple-stress
   carrier (Stage 2) are out of scope; this is the minimal honest carrier of the transverse↔longitudinal
   co-moving companion, matching the #532/#533/#534 Cauchy scope.

---

## Cross-references (grep-verified at branch HEAD this session)

- Prereg (FROZEN): `research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md`
- Prediction / driver / controls / summary / tests: see header
- #534 three-host table + [CONSTRAINT-DEPENDENT] + dissolved fork: `research/2026-07-05_bondframe-tslot-closure_result.md`:76-78,:105-114,:483-486
- #533 scoped traveling-mode theorem (three premises): same doc:105-114
- #532 methods (lab-frame tilt, boundary artifact): `research/2026-07-05_pump-probe-tslot_result.md`
- srs K<0 lossless-reactive canon: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md`:71,:74; `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`:50; `manuscript/ave-kb/vol4/claim-quality.md`:167
- back-EMF longitudinal (prior art, saturated-knot regime, distinct): `research/2026-06-04_motion-stability-bemf-longitudinal-result.md`; `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md`
- imported machinery: `src/scripts/vol_1_foundations/ring_bondframe_probe.py` (RingChain, _free_equilibrium_u); `src/ave/validation/reconcile_gate.py` (#528)
