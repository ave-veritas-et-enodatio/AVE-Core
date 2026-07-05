# PREREG (FROZEN) — The PILOT-FIELD arc: does a LOCALIZED traveling wavetrain on the 2-DOF ring carry a CO-MOVING 2nd-order longitudinal contraction companion (Grant's "pilot field" / longitudinal back-EMF), demoting the fixed/free trichotomy to closure-scale bookkeeping?

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/pilot-field-comoving-companion`
**Prediction module (symbolic, INDEPENDENT):** `src/scripts/vol_1_foundations/pilot_field_predictions.py` (scaffolded AFTER this freeze)
**Driver (numeric time-domain wavetrain, INDEPENDENT path):** `src/scripts/vol_1_foundations/pilot_field_wavetrain.py` (scaffolded AFTER this freeze)
**Tests:** `src/tests/test_pilot_field_comoving_companion.py`
**Result:** `research/2026-07-05_pilot-field-comoving-companion_result.md`
**Consumes by import (#533/#534 machinery):** `src/scripts/vol_1_foundations/ring_bondframe_probe.py` (the `RingChain` 2-DOF host + `_free_equilibrium_u` + the bond-frame cycle-mean-config probe, canon-pinned per #534). The #528 `ReconcileGate` (`src/ave/validation/reconcile_gate.py`) gates every control.
**Builds on (verify-before-cite, grep-verified at HEAD c5dd2c62 this session):** PR #534 [CONSTRAINT-DEPENDENT] three-host table (`research/2026-07-05_bondframe-tslot-closure_result.md`:76-78: ring 1.000000 / pinned 0.999978 / free 0.992563 soft by ⟨dy²⟩/2, BULK N-independent); PR #533 scoped traveling-mode theorem (same doc:105-114, THREE premises); PR #532 methods (`research/2026-07-05_pump-probe-tslot_result.md`).

---

## GRANT'S HYPOTHESIS UNDER TEST (recorded VERBATIM per Grant "go" 2026-07-05)

**Grant "go" (verbatim, attributed Grant 2026-07-05):** the pilot-field arc is authorized ("go"), Grant's framing = *"pilot wave + back-EMF."*

**The hypothesis (verbatim, Grant 2026-07-05):**

> A photon does not cross a passive medium — it carries a CO-MOVING 2nd-order longitudinal contraction companion (the "pilot field": du≈−dy²/2 under the envelope, the free-host reading realized LOCALLY), with the compensating stretch spread over the unoccupied lattice, so the fixed-vs-free trichotomy demotes to closure-scale bookkeeping. The companion is the longitudinal sector's back-EMF response to the transverse drive.

---

## PRE-TEST PHYSICS CHECK (pre-test-physics-check Trigger 6 — the plumber question surfaced to Grant)

**Corpus-searched first (verify-before-cite, grep this session):** the #534 three-host table is a STATIC/quasi-static equilibrium reading (relax u at frozen wave phase, phase-average) — it establishes that a FILLED ring reads COLD (whole-loop closure absorbs the contraction) while a FILLED free chain reads SOFT (the wave pulls its own free ends in). The corpus has NOT run the *localized-wavetrain time-domain* case: whether a contraction develops LOCALLY under a moving envelope on a CLOSED host and TRAVELS WITH it (the co-motion Grant's "pilot" needs). The back-EMF longitudinal channel is real corpus physics (`research/2026-06-04_motion-stability-bemf-longitudinal-result.md`; `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md`), but that arc studied a SATURATED self-trap knot (pinned), NOT a sub-yield linear-radiation wavetrain.

**The one plumber-physical question (surfaced to Grant, recorded):**

> On a LONG closed ring, most of the loop is EMPTY. Grant's picture is that the contraction (du≈−dy²/2) develops LOCALLY under the wavetrain envelope — the free-host reading realized where the wave IS — while the compensating stretch (that the whole-loop closure `Σdu=0` demands) spreads THINLY over the unoccupied lattice (amplitude ~ −⟨dy²⟩·L_env/2N → 0 as the ring lengthens). If true, a bond-frame probe reads FREE-LIKE (soft) UNDER the envelope and COLD far from it, and the fixed/free trichotomy is just where the compensating stretch is booked — a closure-SCALE distinction, not a bulk-physics one. **Does the closed host actually realize this local free-like reading under a moving envelope, or does the global constraint act LOCALLY (fixed-like everywhere, no local well)?** The #534 filled-ring reads COLD because ⟨dy²⟩ is spatially HOMOGENEOUS (the #533 3rd premise); a localized envelope BREAKS that homogeneity — which is exactly the regime the theorem does not cover.

**Authorization to proceed (Trigger 9, fork-to-computable):** Grant's "go" + "pilot wave + back-EMF" framing IS the run-the-computation authorization. This arc converts the fork into a COMPUTABLE DISCRIMINATOR with frozen bins (below): launch a localized wavetrain on a long ring in the TIME DOMAIN, measure the contraction profile, its co-motion, the local probe reading under vs far, and the leakage. The engine decides; Grant's framing names the physical picture the numbers either realize or falsify.

---

## SUBSTRATE-FIRST SECTOR HEADER (declared BEFORE any standard-physics term)

- **SECTOR:** translational-u elastic sector on a **2-DOF-per-node PERIODIC RING** (longitudinal u + transverse y). BOTH k_a (axial STRETCH) and k_s (transverse SHEAR) are translational-u / **capacitive** springs of the same bond (PR#516) — NOT the ε/μ photon pair. Cosserat couple-stress = Stage 2, NOT invoked. This is the same 2-DOF Cauchy host as #532/#533/#534 (the `RingChain` class, imported).
- **MODE:** NUMERIC TIME-DOMAIN (leapfrog/velocity-Verlet integration of the full 2-DOF equations of motion) — a launched LOCALIZED wavetrain that ACTUALLY TRAVELS. This is the new capability the pilot hypothesis needs (co-motion and leakage are DYNAMICAL — the #533/#534 static probe cannot see them). A SYMBOLIC prediction module (the local free-host coefficient −⟨dy²⟩/2, the compensating-stretch dilution law, the group velocity) is the INDEPENDENT path (the #531 tautology guard: the dynamics module never imports the prediction module).
- **REGIME:** small-amplitude sub-yield radiation (y₀=0.1428 tent edge, `axiom-register.md:189` arc* band; never tuned). Op14/Ax4 kernel ON. **PHASE-STATE:** sub-yield interior, linear-radiation regime (NOT the saturated self-trap knot of the 2026-06-04 back-EMF arc). No PML (the ring is closed and periodic; boundedness/leakage is measured on the ring itself, not at an absorber).
- **THE SONIC SUBTLETY (declared, per mission):** at the Ax3 photon point k_long=k_shear (ρ_bond=1) the longitudinal and transverse SPEEDS are EQUAL — a co-moving longitudinal source riding the transverse envelope is exactly SONIC (Cherenkov/resonance threshold). This is EXPECTED at ρ_bond=1 and MUST NOT be reported as a discovery (KNIFE). The stiffness ratio k_long/k_shear ∈ {0.5, 1, 2, 4} is SWEPT to map subsonic/sonic/supersonic companion behavior; the sonic case is treated with care (secular growth watched).
- **DC-vs-AC (clm-acdc07):** the companion is the DC-mean-config longitudinal response (du) to the AC transverse drive (dy²). The measurement separates the co-moving DC contraction (what a slow bond-frame probe under the envelope reads) from the AC wiggle.
- **T2 HOMONYM GUARD (binding, #527):** the transverse bow y is the MECHANICAL T2-response bend, NOT the Cosserat (2,3) charge winding (`resonant-lc-solitons.md:95,:128`; A1⊥T2). mass=A1; charge=Cosserat-winding; bow=T2-mechanical-response. The "back-EMF" here is the MECHANICAL longitudinal-sector reaction to the transverse drive (the du companion), NOT a QED/Maxwell EMF.
- **COORDS (A46):** real-space displacement wavetrain; real-space longitudinal contraction profile du(x,t) and real-space transverse restoring stiffness readout. A46-clean (real-space dynamical measurement, NOT a phase-space φ² comparison — the claim under test is itself a real-space local-contraction claim).
- **CLASS (consistency-vs-emergence):** CONSISTENCY / geometric-kinematic. The companion coefficient −⟨dy²⟩/2 is a DERIVED convexity ½ (the #534 backbone). **EMERGENCE FORBIDDEN for any VALUE** (2/7, 9.7734, /7 stay GR-imported, PR#261/#506). The ½ is declared-derived; no value tuned toward a canon-distinguished target (KNIFE armed).

---

## THE SCALE HIERARCHY (declared AND swept — carrier λ ≪ L_env ≪ N)

The localized wavetrain is `y_j(0) = y₀ · G((j−j₀)/L_env) · sin(k j)` where `G` is a smooth (Gaussian or raised-cosine) envelope of characteristic length `L_env`, carrier wavenumber `k` from the cold shear dispersion `cos k = 1 − ω²/(2 k_s)` (ω=1.2 read-off → k=1.28700, MANY carrier wavelengths per envelope). The three-scale hierarchy is DECLARED and SWEPT so no conclusion rides on one ratio:
- **carrier wavelength** λ = 2π/k ≈ 4.88 nodes (many oscillations under the envelope).
- **envelope length** L_env — swept ∈ {40, 80, 160} nodes (≫ λ; many carriers inside).
- **ring size** N — swept ∈ {512, 1024, 2048} nodes (≫ L_env; the empty lattice is the majority).
The KEY convergence the pilot hypothesis predicts: as **L_env/N → 0** (envelope fraction shrinks), the LOCAL contraction under the envelope converges to the free-host −⟨dy²⟩/2, and the compensating stretch amplitude (∝ L_env/N) → 0. This is the [PILOT-CONFIRMED] convergence, quantified in bin criteria below.

---

## THE #533/#534 MACHINERY CONSUMED (by import) + THE NEW CODE

**Imported (consume, do not re-derive):**
- `RingChain(n_nodes, k_a, k_s, linear_axial)` — the 2-DOF periodic host: `force_x`, `force_y`, `bond_lengths`, `energy` (the saturation-consistent Φ(A) potential — the #532 no-linear-proxy flag), `trans_tangent_stiffness` (the bond-frame probe). Canon-pinned per #534.
- `_free_equilibrium_u(y)` — the analytic free-host T=0 equilibrium `du_b = √(1−dy²)−1 ≈ −dy²/2` (control (b) reference).
- The three-host baseline (`three_host_table`) — control (a)/(b) references (ring 1.000000 / pinned 0.999978 / free 0.992563).

**New code (my modules, my additions):**
- **Time-domain integrator** on `RingChain`: velocity-Verlet of the full 2-DOF EOM (both u and y evolve; the existing module only STATICALLY relaxes u at frozen y). Longitudinal stiffness ratio `k_long/k_shear` a swept parameter (the sonic sweep). A saturation-consistent energy functional (`RingChain.energy`) tracks the ledger — NO linear proxies (the #532 flag).
- **Localized-envelope launcher** + **co-moving-window analysis** (cross-correlation of du profile vs envelope over time; group-velocity fit).
- **Local-vs-far bond-frame probe** (the #526/#534 cycle-mean-config tangent stiffness, sampled UNDER the envelope peak and FAR from it — density-peak sampling, not centroid: the envelope is localized).
- **Leakage diagnostic:** longitudinal energy OUTSIDE a co-moving window around the envelope, vs time (bound vs radiating).

---

## FROZEN BINS (verbatim — NO fall-through else; any criterion-fails path is a loud DISCREPANT-HALT)

- **[PILOT-CONFIRMED]** — the co-moving contraction develops at the locally-free amplitude, travels with the envelope, compensating stretch is global, probe reads free-like under / cold outside, converging as envelope/ring→0 ⟹ the trichotomy demotes to closure scale; the photon carries its own well.
- **[FIXED-LIKE]** — no local contraction on the closed host regardless of localization ⟹ the global constraint acts locally.
- **[RETARDATION-LIMITED / LEAKY]** — the companion develops but lags or radiates; report the measured law (speed-ratio dependence from your sweep).
- **[UNDERDETERMINED]** — name what's missing.

**NO fall-through else. The bin selector (frozen; each criterion DERIVED below):**
1. If the SYMBOLIC free-host coefficient and the numeric contraction depth do NOT reconcile on the free-chain control (b) within the derived band → DISCREPANT-HALT (the prediction is wrong, no verdict).
2. Else if a LOCAL contraction du_min under the envelope develops on the CLOSED ring with |du_min − (−⟨dy²⟩/2)|/(⟨dy²⟩/2) within the derived band AND the du-profile↔envelope cross-correlation peak co-moves at v_group within the derived band AND the compensating-stretch amplitude scales as ∝ L_env/N (→0) AND the bond-frame probe reads soft-under / cold-far AND all these CONVERGE as L_env/N→0 → **[PILOT-CONFIRMED]**.
3. Else if NO local contraction develops on the closed ring at any localization (|du_min| within the cold band everywhere, closed-host reads cold under the envelope too) → **[FIXED-LIKE]**.
4. Else if the contraction develops but LAGS the envelope (co-motion cross-correlation peak offset exceeds the derived band) OR longitudinal energy leaks out of the co-moving window above the derived floor → **[RETARDATION-LIMITED / LEAKY]** with the measured speed-ratio law reported.
5. Any state satisfying none cleanly → loud DISCREPANT-HALT with the conflicting numbers printed.

**KNIFE (armed):** the ½ in dy²/2 is the DERIVED convexity coefficient (declared; the #534 backbone R4) — NOT an asserted ½. Exact speed coincidences at the sonic point k_long=k_shear are EXPECTED there and MUST NOT be reported as a resonance discovery. 2/7, 9.7734, /7, identity endpoints (0/1) armed; no value tuned toward. Any exact zero theorem'd (symmetry/constraint), not observed.

---

## THE DERIVED TOLERANCE BANDS (no vacuous bands — each DERIVED from truncation order / discretization)

- **Free-host coefficient band (control (b) + bin criterion 2):** the contraction depth −⟨dy²⟩/2 is O(y₀²); the O(y₀⁴) correction (the kernel + higher envelope harmonics) is the truncation. Derived free-host residual band = **±10% of the local −⟨dy²⟩/2 depth** (envelope-edge finite-gradient + carrier-vs-envelope commensurability + the O(y₀⁴) kernel term ~few %; the local reading under a finite envelope is intrinsically softer-bounded than the infinite-homogeneous free chain's exact 0.992563). This band is derived in the prediction module from the envelope form factor and the y₀⁴ series; frozen as ±10% here, sharpened (not loosened) in-module if the sweep supports it.
- **Co-motion band:** the du-profile↔envelope cross-correlation peak must track the transverse GROUP velocity v_g = dω/dk (cold shear branch) within the derived band = **±1 node per carrier period** (the spatial-sampling + envelope-width discretization floor). Derived from Δx_sample/Δt_frame.
- **Compensating-stretch dilution band:** the far-field mean stretch amplitude must scale as ∝ L_env/N within **±20%** across the (L_env, N) sweep (the finite-envelope form-factor spread). A dilution that does NOT shrink with N ⟹ the constraint acts locally (bin 3 evidence).
- **Leakage floor:** longitudinal energy in the co-moving window must stay ≥ (1 − derived_floor) of the initial companion energy over the recording window, floor = **5% per envelope-transit** (the integrator energy-drift + discretization-radiation floor, derived from the energy-ledger dt-convergence sweep; NOT the physical leakage — a physical leak exceeds this). Distinguishes bound (bin 2) from leaky (bin 4).
- **Sonic-point exclusion:** at k_long=k_shear the companion is exactly sonic; secular growth is EXPECTED (KNIFE) and the leakage/boundedness verdict at ρ=1 is reported as SONIC-SPECIAL, not folded into the generic verdict. The subsonic (ρ=2,4) and supersonic-longitudinal cases carry the generic verdict.

All bands DERIVED from truncation orders / discretization / convergence sweeps; no vacuous band. Prediction (symbolic) and dynamics (numeric time-domain) are INDEPENDENT code paths (the #531 tautology guard); gates via the #528 ReconcileGate with can-fire proven on dropped-term/sign-flip synthetics on real paths.

---

## CONTROLS (all HALT-gated via the #528 ReconcileGate; derived tolerances; can-fire on real paths)

- **(a) FILLED-ring limit** (envelope → whole ring, L_env → N): must recover #534's ring reading (COLD, uniform, ratio → 1.000000). Gate: |filled-ring cyclemean bond-frame ratio − 1| within the #534 cold band (3×10⁻³). The homogeneous-⟨dy²⟩ limit re-enters the #533 theorem regime.
- **(b) OPEN-FREE-chain envelope** (an envelope on an OPEN FREE chain): must recover the free reading LOCALLY under the envelope (0.9926-class, soft by ⟨dy²⟩/2). Gate: |local-under-envelope bond-frame ratio − 0.992563| within the free-host coefficient band. This is the LOCAL free reading the pilot picture claims the closed host realizes.
- **(c) LINEAR-axial control** (`linear_axial=True`, the kernel OFF): the contraction is GEOMETRIC (√(1−dy²)−1), not from the concave kernel. Expected: the linear-axial ring reproduces the contraction profile to O(y₀⁴) (the merged O(y₀⁶) result — kernel contributes ~nothing at O(y₀²)). Gate: |du(nonlinear) − du(linear-axial)|/|du| ≤ derived O(y₀⁴/y₀²)=O(y₀²) band. Measures the kernel's role (expected ~nothing).
- **(d) ENVELOPE/RING SWEEP with LOCAL-reading CONVERGENCE quantified** (the (L_env, N) grid): the local contraction depth → −⟨dy²⟩/2 and the compensating-stretch amplitude → 0 as L_env/N → 0. Convergence quantified: report the local depth and the far-stretch amplitude across the grid; the [PILOT-CONFIRMED] verdict REQUIRES both convergences within band.
- **(e) ENERGY-MOMENTUM LEDGER closure (the crank check):** the companion's momentum + the wave's + the constraint forces book to zero on the ring. Use the SATURATION-CONSISTENT energy functional (`RingChain.energy` — the #532 flag: NO linear proxies on saturating springs). Gate: total H (kinetic + Φ-potential + shear) conserved within the derived integrator floor over the recording window; total longitudinal momentum Σ m u̇ conserved (closed ring, no external force) within the floor. A ledger that does NOT close ⟹ the companion is not a self-consistent bound object (evidence against bin 2).

**Prediction module (symbolic) and dynamics module (time-domain) = INDEPENDENT code paths (the tautology guard). No self-verifying gates.** Mean-level (⟨du⟩ over the envelope) vs per-bond-level (du_j profile) claims explicitly distinguished (the #533 lesson: a mean can be cold while per-bond is patterned, and vice-versa).

---

## THE srs K<0 FLAG (surfaced, NOT resolved — per mission, cite the K<0 canon)

**Declared open question at the srs level (flag-don't-fix):** this 2-DOF Cauchy chain hosts a REAL (mechanically-stable, K>0) longitudinal sector at every ρ_bond=k_long/k_shear in the sweep, so the companion here is a real acoustic contraction. But on the **srs photon operating point** (ρ_bond=1, the Ax3 zero-reflection point, k_s=k_a), the bulk sector has **K<0 (lossless-reactive, mechanically unstable for ρ<2)** — verbatim canon: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md`:71,:74 ("the photon's zero-reflection point is a lossless-reactive operating point … K<0 for ρ<2 … NOT a stable static elastic solid"); `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`:50; `manuscript/ave-kb/vol4/claim-quality.md`:167. **On the real srs photon point the physical companion may be EVANESCENT-BOUND (a reactive, non-propagating longitudinal well keyed to the moving envelope) — a character this real-K, propagating-longitudinal chain CANNOT host.** So a [PILOT-CONFIRMED] verdict on THIS chain is a SUFFICIENCY demonstration (the co-moving well is realizable on a real-K host), NOT a claim about the srs photon point — where the K<0 lossless-reactive character is the open question. This flag is stated in the result; it is NOT resolved here (out of scope for the 2-DOF Cauchy chain).

---

## ANTI-TUNE / KNIFE LEDGER (canon-forced vs derived vs read-off vs free)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(A)=k₀√(1−A²)` | CANON-FORCED | Ax4, `scale_invariant.py:107-156` (via imported RingChain) |
| 2 | Free-host contraction `du = √(1−dy²)−1 ≈ −dy²/2` | DERIVED (convexity) | the ½ is the 2nd-order coeff (#534 backbone R4); NOT asserted |
| 3 | `⟨dy²⟩ = y₀²(1−cos k)` | DERIVED | traveling-wave phase average (#534) |
| 4 | dispersion `ω²=k_s(2−2cos k)` ⟹ k=1.28700 | DERIVED | cold shear branch; ω=1.2 read-off (#532) |
| 5 | v_group = dω/dk (cold shear) | DERIVED | co-motion reference (analytic branch derivative) |
| 6 | y₀ = 0.1428 tent edge | READ-OFF (#527/#529) | `axiom-register.md:189`; never tuned |
| 7 | k_long/k_shear ∈ {0.5,1,2,4} sonic sweep | SWEPT (declared) | subsonic/sonic/supersonic map; ρ=1 = sonic (expected) |
| 8 | L_env ∈ {40,80,160}, N ∈ {512,1024,2048} | SWEPT (declared) | scale hierarchy λ≪L_env≪N |
| 9 | Compensating-stretch dilution ∝ L_env/N | DERIVED | whole-loop closure Σdu=0 (the pilot prediction) |
| 10 | srs K<0 lossless-reactive at ρ=1 | CANON-CITED (flag) | `parent-condition-match-forces-balance.md`:71,74; NOT resolved |
| 11 | ½, ¼, 2/7, 9.7734, sonic coincidences | KNIFE-ARMED | none tuned toward; sonic at ρ=1 expected not discovery |

**0 free parameters tuned toward 2/7 / 9.7734 / PILOT-CONFIRMED.** ω and y₀ read-off; k, v_group, the free coefficient, the dilution law, and all bands derived; L_env, N, ρ_bond swept.

---

## FREEZE

This prereg is FROZEN at this commit. The prediction module, the time-domain dynamics driver, the tests, and the result doc are scaffolded AFTER this commit (commit order proves the freeze). Bins, tolerances, controls, and the anti-tune ledger above are the adjudication contract; no gate looser than frozen here; no post-data bin edits (Rule 11). Any amendment is a Rule-12 dated banner preserving this body. Grant's hypothesis and "go" are recorded verbatim above.
