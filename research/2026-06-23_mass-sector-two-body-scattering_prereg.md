# PREREG — Mass-Sector Two-Body Scattering: validate-on-known (gravity) on the scalar A1 Master Equation

**Date (frozen):** 2026-06-23
**Status:** DRAFT — awaiting Grant observable-confirmation (one plumber-physical question surfaced per Rule 16 / pre-test-physics-check; see §0.5). Do NOT run until §0.5 resolved.
**Branch:** `analysis/soliton-mass-scattering` (worktree `/tmp/lane-scattering`, off `origin/main`). Do NOT push/merge directly — PR for orchestrator audit + Grant merge pending. `main` PROTECTED, NO self-merge.
**Lane:** Implementer LANE A (re-scoped to MASS-SECTOR per Grant ruling, this session). The prior session held at the Rule-16 gate and correctly caught the sector mismatch (electron-electron Coulomb is a category error on the scalar A1 engine — A1 ⊥ T2, no Cosserat winding → no charge). Grant ruled: do (a) honest mass-sector scattering FIRST on the validated scalar engine; (b) charge-sector on the Cosserat engine LATER, only if fundamentally needed.

**Engine (inherited physics UNCHANGED — read-only use, no subclass):** `MasterEquationFDTD` (`src/ave/core/master_equation_fdtd.py`). The canonical scalar A1 Master Equation `∂²V/∂t² = (c₀²/S(A))·∇²V`, `S(A)=√(1−A²)`, `A=V/V_yield`. Mode-I bound state = the A1 **dilatation-mass blob** (master-equation.md:20, :24-25). This driver only *reads* the engine; it does not modify `src/ave/core/`.

---

## §0 — What this test IS and IS NOT

**IS:** a two-prong validate-on-known on the scalar A1 engine — does a pair of Mode-I dilatation-mass bound states (a) interact attractively (matching AVE-gravity's mass-mass sign), AND (b) phase-INDEPENDENTLY (→ gravity-like) or phase-DEPENDENTLY (→ generic nonlinear-soliton interaction, which would mean this is NOT testing gravity)?

**IS NOT:** a charge-sector / Coulomb test (that needs the Cosserat (2,3) engine — deferred-conditional follow-on, NOT built here). NOT an emergence/chord claim: AVE-gravity is FORM-derived / VALUE-imported (MIXED, `optical-refraction-gravity.md:52`, G-ruling 2026-06-14 `ilk-gravmb`), so a clean phase-independent attraction is a two-body gravity **CONSISTENCY** check (Class C), NOT a chord. See §9 for the chord-watch (where an AVE-distinct FORM feature could hide).

---

## §0.5 — Rule-16 GATE (open): the observable question to Grant

**Surfaced before freeze, per pre-test-physics-check Step 3.** The precedent driver (`annihilation_evaporation_run.py:46-50`, DEV-6) confirms this engine lineage admits **zero subluminal rigid transport** ("the imprinted KE radiates instead of convecting the trap... ZERO centroid motion over 17k steps"). A kinematic closing-collision therefore cannot run. The force-readout must be **static, at t≈0**.

**Question:** On the scalar A1 engine, is the right mass-mass force observable the *initial relative acceleration of the two saturation cores' centroids* at t≈0 (a static-force readout), or an actual closing-trajectory collision — and if static, is centroid-drift-toward-neighbor the gravity signature you'd accept, or do you want the c_eff-refractive-gradient (A²-field overlap) between the cores as the primary observable?

**Provisional design pending answer:** record BOTH — centroid-drift-at-t≈0 as the force verdict, A²-saturation-gradient at the midplane as the corpus-mechanism witness — at both phases. Frozen design below assumes this; will be amended to Grant's call before run.

---

## §0.6 — EMPIRICAL FINDINGS surfaced at driver-time (Rule 10, flag-don't-fix) — 2026-06-23

Two load-bearing findings emerged from running the driver early (Rule 10), BEFORE the frozen verdict. Both are flagged, not silently fixed. The frozen §2-§9 design below is preserved; these findings sit above it.

**FINDING 1 — SEED-SPEC mismatch in the brief (corrected, not a bug).** The brief's stated "canonical Mode-I seed" (N=32, amp=0.95·V_yield, R=2.0, sech, r10 Test C:262-263) does **NOT** pass r10 Test C's own persistence gate on current HEAD: reproducing r10 Test C exactly gives `V_center_ratio = −0.089` (Test C1 PASS threshold |ratio|>0.5 → **FAIL**; the bare sech seed disperses — Vmax 41469→7790 by step 50, FWHM 81→1139 cells). The ACTUAL validated canonical Mode-I (`src/tests/test_master_equation_v14_mode_i.py`, **5/5 PASS on HEAD**, verified this session) is the **breathing soliton** at N=24, DX=0.5, V_yield=1.0, amp=0.85, R=2.5, measured by **V_peak** (the max, tracking the breathing core) over a post-200-transient window — NOT by the center-cell V (which oscillates through zero as the breather breathes, the source of r10's −0.089). The driver was corrected to the **validated** config. *This is a brief seed-spec error, NOT an engine regression — engine + validated Mode-I are sound.*

**FINDING 2 — the centroid-drift force readout (O1) is swamped by the radiation floor on this transport-less engine.** Single-blob control (O0): an isolated breather's centroid wanders **2.34 cells** over the recording window purely from radiation/breathing asymmetry (zero initial velocity → all wander is jitter, not force). At separations 5-9 cells, the two-body net centroid drift (smoke: +0.88 in-phase, −1.34 out-phase) is **below** this 2.34-cell floor → classifier returns **NULL/BELOW-FLOOR**. This corroborates DEV-6 (`annihilation_evaporation_run.py:46-50`, zero subluminal rigid transport) at integrator time: **the scalar A1 engine cannot transduce a two-body force into measurable centroid motion.** The O1 (centroid-drift) prong is therefore not a viable gravity readout on this engine.

**FINDING 2-corollary — the only field-side signal (O2 A²-midplane) is manifestly PHASE-DEPENDENT.** Smoke O2: in-phase midplane A²≈0.69 (constructive fill); out-phase A²≈1.7e-3 (destructive cancel). This is the textbook **generic-soliton coherent-overlap signature** (the guard's P2-refute), NOT phase-independent gravity. The A²-overlap difference is field interference, not a transduced force — so even O2 does not rescue a gravity reading.

**Consequence for the verdict:** on this engine, the validate-on-known leans toward **NULL/BELOW-FLOOR (O1)** with a **phase-DEPENDENT field-overlap (O2)** — i.e., the engine cannot measure mass-mass gravity via two-body scattering, and the only measurable two-body field signal is generic-soliton interference. This is reported as a WALL-engine capability finding (the scalar engine lacks the transport channel to convert the optical-refraction gradient into a force), NOT as a gravity falsification. **This is precisely why the §0.5 question to Grant is load-bearing:** if Grant wants a different observable (e.g. a momentum-flux / stress-tensor readout that doesn't require rigid transport), the test could still discriminate; with centroid-drift + A²-overlap, it cannot.

---

## §1 — Substrate-native-check walk (recorded BEFORE code, per skill)

| Checkpoint | Resolution for this test |
|---|---|
| CP1 dynamics | Wave propagation (leapfrog FDTD), NOT minimization. Force emerges from the c_eff(V)·∇²V dynamics; no energy-basin, no gradient descent. |
| CP2 sector | V-sector / A1 dilatation-mass. Mode-I bound state = the mass blob (`master-equation.md:20,24-25`). NO Cosserat winding. |
| CP3 objective | AVE-native force readout = relative centroid acceleration of the two saturation cores + the c_eff(V) refractive gradient (`optical-refraction-gravity.md:13-17`). NOT energy-functional minimization. |
| CP4 coords | **Real-space lattice-Cartesian IS load-bearing here** (rare): the A1 mass is a real-space dilatation blob and the corpus gravity claim (refractive gradient → diffraction → "fall") lives in real-space (R,r), NOT phase-space φ². No A46 violation — this is NOT a (2,3) phase-space-torus claim. |
| CP5 local clock | Op14 saturation active; `c_eff(r)=c₀/√S(A(r))`. The gravity mechanism IS this modulation. Report A²_local at the cores. |
| CP7 sampling | PML-excluded top-K |V|² for centroid (`pml_thickness ≤ {i,j,k} ≤ N−pml−1` BEFORE argpartition). A1 blob is density-PEAKED (not shell-like) → centroid-of-blob valid here. |
| CP8 hosting | N/A — not an emergence/hosting test; the Mode-I blob is a *validated* configuration (r10 Test C), and we measure a *property* (the two-body force), not whether the engine hosts the blob. |
| CP10 boundary | A_cap/S_min clip handles the saturation wall internally; this driver adds NO bulk confining force. |

**The phase guard, made substrate-explicit.** In this REAL SCALAR engine, "relative phase" between two additively-superposed sech blobs = the **SIGN** of the second blob:
- **in-phase** = both seeds `+SEED_AMPLITUDE` (V adds constructively in the overlap region);
- **π-out-of-phase** = second seed `−SEED_AMPLITUDE` (V cancels in the overlap region).

The gravity mechanism is driven by `A²(r)=|V|²/V_yield²` — the **saturation depth**, an ENVELOPE (sign-blind) quantity. So a true gravity-like force must be **sign-independent**. Generic bright-soliton interaction lives in the coherent `c_eff·∇²V` overlap term, which IS sign-dependent (in-phase attracts, out-of-phase repels — the textbook NLS-soliton result). **The sign-flip comparison IS the gravity-vs-generic discriminator.**

---

## §2 — Frozen configuration (from canonical Mode-I seed; reused, not re-derived)

All constants imported from `ave.core.constants` (ave-canonical-source). Seed-reuse reference: `r10_master_equation_v14.py` Test C (lines 243-300).

| Parameter | Value | Source |
|---|---|---|
| `N` (grid) | 32 | canonical Mode-I (r10 Test C) |
| `DX` | 1.0 | r10 Test C |
| `V_YIELD` | `constants.V_YIELD` (≈43651.85) | constants.py:460 |
| `C0` | 1.0 | r10 Test C (natural units) |
| `PML` | 4 | engine default |
| `A_CAP` | 0.99 | engine default (stay in Regime II) |
| `S_MIN` | 0.05 | engine default |
| `SEED_AMPLITUDE` | `0.95 · V_YIELD` | r10 Test C:262 |
| `SEED_RADIUS` | 2.0 | r10 Test C:263 |
| seed profile | `sech(r/R)` | r10 Test C:268 |
| impact parameter `b` | **0** (head-on) | brief |
| separation `d₀` | center-to-center along x, swept {6, 8, 10} cells | see §2.1 |
| relative phase | **{in-phase (+,+), π-out (+,−)}** — BOTH, b=0 | the load-bearing guard |
| n_steps (force window) | t≈0 force window: first `N_FORCE` steps before radiation contaminates; `N_FORCE` calibrated in §3 from a single-blob control | radiation-floor calibration |

### §2.1 — Separation sweep rationale
Three separations {6, 8, 10} cells (each blob FWHM ≈ 2·SEED_RADIUS = 4 cells, so cores do not initially overlap at d₀≥6; PML at 4 cells from each face leaves interior ≥ d₀+2·FWHM clearance at N=32). A monotone force-vs-separation trend (force falls with d₀) is a secondary mechanism witness; a single d₀ is sufficient for the sign+phase verdict.

---

## §3 — Observables (all FROM the evolved field; ave-driver-script-honesty)

**Primary force observable (O1 — centroid drift):** for each blob, track the PML-excluded top-K |V|² centroid of its half-volume. At t≈0 both centroids are at rest (`V_prev = V`, zero initial velocity — set by `inject_localized_blob`). The SIGN of `d²(separation)/dt²` over the force window:
- separation DECREASES (cores drift together) → **ATTRACTION**;
- separation INCREASES → **REPULSION**.
Each blob's centroid is sampled within its own half-space `x < N/2` vs `x ≥ N/2` to avoid one blob's tail biasing the other's centroid; PML cells excluded.

**Mechanism witness (O2 — c_eff refractive gradient / A²-saturation overlap):** the midplane (x=N/2) saturation depth `A²(midplane)` and the `n_shear(r)=S(A)^(−1/2)` refractive field between the cores. The corpus mechanism (`optical-refraction-gravity.md:13-17`) predicts each blob raises the other's local refractive index → wavefronts refract toward the neighbor. O2 is the *mechanism*; O1 is the *force verdict*. O2 being phase-independent (A² is sign-blind) while O1 tracks it is the positive gravity signature.

**Local-clock witness (O3):** A²_local at each core peak and `ω_local = ω_global·√(1−A²)` (CP5 reporting requirement). Confirms the cores stay in Regime II (A² < A_cap²) over the force window.

**Radiation-floor calibration (O0 — control):** a SINGLE-blob run at the same seed. The single blob's centroid should stay put (no neighbor → no force; modulo radiation jitter). `N_FORCE` = the step count over which the single-blob centroid drift stays below a fixed jitter floor (e.g. < 0.1 cell). The two-body O1 verdict is read ONLY within `[0, N_FORCE]`, where any net drift is force-driven not radiation-driven. **This control is the honesty gate**: net two-body drift must exceed the single-blob radiation jitter to count.

---

## §4 — Pre-registered predictions (BEFORE the run)

**Validate-on-known target:** AVE-gravity = Machian/SYM mass-mass ATTRACTION via optical refraction (`optical-refraction-gravity.md:13`, Machian coupling :50). Two A1 dilatation-mass blobs are two masses. Pre-registered expectation: **attraction** (O1 separation decreases).

**P1 (sign):** in-phase pair → ATTRACTION (separation decreases beyond the O0 radiation floor).

**P2 (phase-independence — THE LOAD-BEARING PREDICTION):** the out-of-phase (+,−) pair shows the **SAME SIGN** force (also attraction) and **comparable magnitude** to in-phase. If gravity is the mechanism, flipping the second blob's sign (which leaves A²(r) — the saturation depth — unchanged) must NOT flip the force.

**P2-refute (the guard's null):** if the out-of-phase pair REPELS (or the force magnitude changes sign/order with phase), the interaction is generic nonlinear-soliton coherent overlap, NOT gravity. The in-phase "attraction" would then be an artifact of constructive field overlap, and the "attraction = gravity" reading is FALSE on this engine.

**P3 (mechanism, secondary):** O2 midplane A² is phase-independent (sign-blind envelope); if O1 tracks O2 (force follows the A²-gradient regardless of phase), the gravity mechanism is corroborated.

**P4 (separation trend, secondary):** force magnitude decreases with d₀ (monotone falloff). Direction/falloff-law is a chord-watch item (§9), not a pass/fail gate.

### Dimensional / magnitude sanity (per ave-prereg v1.1)
Force is read as a centroid acceleration in lattice-units/dt². No CODATA magnitude is asserted (natural units, V_yield=engine value). The test is SIGN + PHASE-PARITY, not a magnitude-match — so no leading-order CODATA dimensional pin is required. The only magnitude gate is the **relative** one (O1 net drift vs O0 radiation jitter), which is dimensionless-by-ratio.

---

## §5 — Outcome bins (frozen; the two-pronged verdict)

Read O1 sign at BOTH phases, gated by O0 (net drift must exceed radiation jitter).

| Bin | in-phase O1 | out-of-phase O1 | Verdict |
|---|---|---|---|
| **GRAVITY-CONSISTENT** | attract | attract (same sign, comparable mag) | Phase-INDEPENDENT attraction → **validate-on-known PASSES**: two-body gravity CONSISTENCY check (Class C). Proceed to σ(b,v) sweep proposal (§8). |
| **GENERIC-SOLITON** | attract | repel (sign flips with phase) | Phase-DEPENDENT → **NOT gravity**. The in-phase attraction is generic NLS coherent-overlap. "Attraction = gravity" reading FALSIFIED on this engine. Branch closes honest-negative (Rule 11); do NOT debug toward a rescue. |
| **REPULSIVE-BOTH** | repel | repel | Phase-independent REPULSION → sign contradicts AVE-gravity. SURFACE the conflict (flag-don't-fix): engine output vs corpus mass-mass-attraction claim, both verbatim. Grant adjudicates. |
| **NULL / BELOW-FLOOR** | no drift > O0 | no drift > O0 | No measurable two-body force within the transport-less window. Report as engine-capability finding (the scalar engine may not transduce the refractive gradient into centroid motion — a WALL-engine result, not a physics negative), NOT a gravity falsification. Pairs with the DEV-6 zero-transport finding. |
| **MIXED / AMBIGUOUS** | any | any, but O0-marginal or d₀-inconsistent | Inconclusive; report honestly, propose N↑ / longer window / spectral-force readout. |

**Referential-integrity check (ave-prereg v1.2 Step 3.6):** every §4 falsifier routes to a bin. P1→GRAVITY-CONSISTENT/REPULSIVE-BOTH; P2-refute→GENERIC-SOLITON; O0-gate-fail→NULL/BELOW-FLOOR. No orphaned falsifier; the load-bearing P2-refute (the generic-soliton negative the whole test exists to catch) has a dedicated home (GENERIC-SOLITON) that cannot masquerade as GRAVITY-CONSISTENT (the sign-flip is the explicit discriminator).

---

## §6 — Honest-negative discipline (Rule 11) pre-commitment

If the result lands in GENERIC-SOLITON (phase-dependent), that is the discipline working: the guard caught a generic-soliton-attraction masquerading as gravity. The correct reaction is to RECORD the falsification, name the mechanism (NLS coherent overlap), and report that this engine's two-body interaction is NOT a gravity test — NOT to re-tune SEED_AMPLITUDE / d₀ / window to rescue an "attraction = gravity" headline. The adjudication criteria above are frozen; they will NOT be dropped post-hoc to convert a phase-dependent result into a gravity pass.

---

## §7 — CONSISTENCY vs CHORD label (ave-discrimination-check)

**Pre-committed label: CONSISTENCY (Class C), not CHORD.** AVE-gravity is FORM-derived / VALUE-imported (MIXED — `optical-refraction-gravity.md:52` G-ruling `ilk-gravmb`; the Machian ξ is back-solved from empirical G). A clean phase-independent attraction reproduces the *sign* of mass-mass gravity via the engine's c_eff(V) refraction — a two-body consistency check on the gravity ontology, NOT independent AVE-distinct evidence.

**SM-counterfactual (Step 2):** Newtonian gravity ALSO predicts two masses attract. The sign alone does not discriminate AVE from Newton. So the headline is "consistency check," not "STRONG POSITIVE." The AVE-distinct content, IF any, lives in the FORM (§9 chord-watch), not the sign.

**Discriminator-axis (Step 2.5):** AVE shares the FORM (attraction, ~1/r-ish) with Newton → a sign/ratio claim is non-discriminating; any discrimination would be in a FORM-deviation (short-range S(A)-saturation correction to 1/r, or a velocity dependence) — a MAGNITUDE/shape feature, not the sign. That's the chord-watch, not this validate-on-known.

---

## §8 — Forward proposal (PROPOSE, do not build) — conditional on GRAVITY-CONSISTENT

If validate-on-known PASSES (phase-independent attraction): propose a forward mass-sector **σ(b, v_rel) sweep** — vary impact parameter b and (within transport limits / via the static-force-at-separation map F(d₀)) build the effective two-body potential V_eff(r) and its scattering character. The transport-less constraint (DEV-6) means this is a *static-force-map* σ, read as F(d₀,b) → V_eff(r), not a ballistic cross-section. The chord-watch (§9) is the payload: does V_eff(r) deviate from 1/r at short range where S(A) saturates?

## §9 — Chord-watch (where an AVE-distinct FORM feature could hide)
- **Short-range S(A)-saturation correction to 1/r:** as the cores approach and A²→A_cap, the refractive gradient saturates (c_eff caps at c₀/√S_min). A Newtonian 1/r has no such cap. A measured F(d₀) flattening / turnover at small d₀ would be an AVE-distinct FORM feature (the saturation kernel's fingerprint on gravity). FLAG if seen; do NOT headline without the §7 SM-counterfactual + ave-discrimination-check.
- **Velocity dependence:** N/A on this transport-less engine (deferred to a transport-capable engine).

## §10 — Deferred-conditional follow-on (NOTE only, do NOT build)
**(b) charge-sector scattering on the Cosserat engine** is the deferred-conditional follow-on for the bankable e-e (electron-electron Coulomb) prize. It requires the (2,3) Cosserat winding carrier (charge = Beltrami helicity), which the scalar A1 engine does NOT have. Build only if fundamentally needed, in a LATER session, per Grant's ruling. This prereg does not scope it.



