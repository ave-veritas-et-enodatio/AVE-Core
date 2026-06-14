[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Diagnostic map of failed genesis / chord efforts (consistency-vs-emergence: a falsification ledger, not a new claim). Consolidates ~10 finished negatives from held analysis branches into a tagged, diagnosed, recoverable record so future work does not re-walk dead ends. Each entry carries a discrimination-check tag (GENUINE-FALSIFICATION vs WRONG-CARRIER/REGIME vs INCONCLUSIVE vs SMOKE-FAIL) and a recovery pointer (branch @ tip, pushed to origin). Cross-links l3-synthesis §8 (the electron-soliton-specific negatives) + the closure-roadmap. Originates no derivation."
-->

# Genesis / Chord Falsification Ledger — the Diagnostic Map of Dead Ends

A consolidated, **tagged and diagnosed** record of finished negative efforts across the genesis (electron self-assembly), chord (α / engineered-gravity), and motion-stability arcs. The value of a negative is its **diagnostic** — *why* it failed and what it rules out or redirects to — so the next attempt does not re-walk it. Every entry's full work is recoverable from its pushed branch.

> ↗ See also: [L3 Electron-Soliton Synthesis §8](../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) — the electron-soliton-closure-specific negatives (the 10 Mode-III tests + the three-layer refutation); this ledger is the broader cross-arc map.
> ↗ See also: [Claim-Quality Closure Roadmap](../claim-quality-closure-roadmap.md) — the meta-tracking doc this ledger feeds.

## Tag legend (per `ave-discrimination-check` — the load-bearing distinction)

- **GENUINE-FALSIFICATION** — the hypothesis is physically ruled out; the route is closed. A real asset.
- **WRONG-CARRIER / WRONG-REGIME** — the null is an *artifact* of testing the wrong carrier or regime (an engine-architecture or IC choice), **NOT** a physical falsification. A re-test is specified. **Must not be canonized as a falsification.**
- **INCONCLUSIVE** — partial / null; the test did not decide, usually blocked by a known engine limitation (e.g. the ω≡0 Q0 fixed point).
- **SMOKE-FAIL** — failed a smoke gate; the build is dead *as implemented*, though a partial insight may survive.

---

## Genesis (electron self-assembly) negatives

### genesis-omega-wave — the ω-shear photon does not self-trap (III)
- **Hypothesis:** the canonical ω-shear photon (transverse Cosserat-ω wave) self-traps into the electron under Axiom-4 saturation — the "right object, right mechanism."
- **Verdict:** III — no self-trap, in both engine realizations.
- **Diagnostic:** in the standalone saturated-Cosserat field the ω-wave **disperses** (below a curvature threshold) or **collapses in finite time** (above) — never confines; in `VacuumEngine3D`, saturation is routed **only to the K4 V-sector, never the ω dynamics**, so the ω-photon evolves as a bare linear wave. The engine has **no wave-dynamics path coupling saturation to ω** — this is the architecture, not a physical null. The **A1 / V-sector (dilatation) carrier DOES self-trap** (the v14 Mode-I breather). (Positive sub-result: the chiral ω-wave carries coherent charge = Beltrami helicity, sign-flipping with χ.)
- **Tag:** 🔴 **WRONG-CARRIER / WRONG-REGIME** — re-test the **A1 / V-sector (T2-precursor → A1 dilatation)** carrier on the v14 engine (which self-traps). Do **not** canonize as "self-trap falsified."
- **Recovery:** `analysis/2026-06-06-genesis-omega-wave` @ `cc19416d` (pushed)

### genesis-armB-flywheel-seed — the bare ω-flywheel does not collimate into the (2,3) (III)
- **Hypothesis:** the electron is just three numbers `{ω, R, chirality}` — a bare collimated B-flywheel (Lundquist force-free flux rope in the Cosserat ω field) relaxes under force-free dynamics into the `(2,3)` electron.
- **Verdict:** III — no collimation into `(2,3)`.
- **Diagnostic:** the seed was the **ω/B-flywheel alone** — the inductive microrotational-B / **charge-"3"** half. But the electron is the **A1 dilatation-MASS "3" carrying the (2,3) charge-winding "3"** (two orthogonal objects; [master-equation.md](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). Seeding only the charge-half, with no A1 mass, is an **incomplete IC** — the force-free relaxation has nothing to confine.
- **Tag:** **WRONG-CARRIER / SUPERSEDED** by the two-"3"s — the electron needs the A1 mass too; the three-numbers-from-the-flywheel-alone framing is the pre-two-"3"s picture.
- **Recovery:** `analysis/2026-06-06-genesis-armB-flywheel-seed` @ `5cf1a03e` (pushed)

### electron-genesis-drop — pinch-off geometry hosted, (2,3) not (III)
- **Hypothesis:** driving the pure-V photon route to the A→1 pinch-off (the ingredient missing from the 2026-06-04 sub-pinch-off run) nucleates the sub-V_yield `(2,3)` electron.
- **Verdict:** III — pinch-off geometry hosted; the `(2,3)` electron-state not.
- **Diagnostic:** at A→1 the pure-V route **does** pinch off into ℓ_node droplets (single→1, pair→**2** = the geometric e⁺e⁻ split — a positive sub-result), but the droplets stay **over-yield** (V/V_yield ≈ 8–11, lossy), the `(2,3)` does **not** assemble, the chirality split is not captured, and the **Cosserat ω stays exactly 0** in every run — the **Q0 fixed point** (the even-in-ω parametric coupling cannot seed ω from zero, amplitude-independent).
- **Tag:** **INCONCLUSIVE** — the geometry is hosted; the `(2,3)` is blocked by the ω≡0 Q0 fixed point (an engine ω-seeding limitation), not a physical falsification.
- **Recovery:** `analysis/2026-06-06-electron-genesis-drop` @ `71fdb9a2` (pushed)

### screened-winding-probe — the v6 w_pol≡0 absence is genuine (exonerated)
- **Hypothesis:** the genesis-v6 null (`w_pol ≡ 0`, the poloidal "3" never forms) might be an **apparatus screen** (a reader that cannot see the winding inside the snap shell), not a genuine absence.
- **Verdict:** BIN = NO-SCREENING — the absence is genuine.
- **Diagnostic:** the apparatus reads a **known-planted** `(2,3)` ω-winding **faithfully through a formed snap shell** → the prior v6 verdict stands and is **exonerated of the screening confound**. `w_pol ≡ 0` is a real absence, not a blind reader.
- **Tag:** **GENUINE-FALSIFICATION** (methodological) — confirms the genesis-v6 `(2,3)`-self-assembly null is physical, not an artifact.
- **Recovery:** `analysis/2026-06-11-screened-winding-probe` @ `836ee6de` (pushed)

### crystal-k4-graft — real-space trap and phase-space winding decouple (SMOKE-FAIL)
- **Hypothesis:** grafting the `c_eff(V)` bond-Γ wall + the conserved ADD-2 port-rotation converter onto the K4 4-port traps the longitudinal monopole **and** assembles the `(2,3)` winding coherently.
- **Verdict:** SMOKE-FAIL on SMOKE-3 — the real-space trap and the phase-space winding are **decoupled** (SMOKE-1/2 pass).
- **Diagnostic:** progress over the scalar-bulk Outcome C — the K4 `(V_inc,V_ref)` phase-space **is** a genuine winding carrier — but the real-space trap ⊥ phase-space winding **do not co-locate**; the full α-emergence run is refused by the frozen guard (no `(2,3)` → no α).
- **Tag:** **SMOKE-FAIL / SUPERSEDED** — the specific graft is dead as built; the surviving insight is "the K4 phase-space is a genuine winding carrier."
- **Recovery:** `analysis/2026-06-09-crystal-k4-graft` @ `09bb22d1` (pushed)

## Chord (α / engineered-gravity) negatives

### a2mu-vs-Q-crux — A²_μ does not scale with Q (WALL, not KNOB)
- **Hypothesis:** the K4↔Cosserat / Op14 trace-reversal microrotation `A²_μ` scales with the resonant Q — Q is a **knob** that pumps the pair-nucleation gate.
- **Verdict:** WALL, not KNOB — the resonant-Q-compensation hypothesis is falsified.
- **Diagnostic:** there is **no dynamical K4→microrotation pump that scales with Q** (WALL-engine); the dynamically-evolved `A²_μ` peaked at 0.012 (K4→Cosserat coupling weakness); the cold-start floor is the framework-predicted **traceless-photon null** (WALL-physics). The algebraic chirality factor `(1+κ·h)` is a ≤0.88 % modulation and cannot move the verdict.
- **Tag:** **GENUINE-FALSIFICATION** (of Q-as-knob) — with the WALL-engine caveat (the K4→ω pump is absent in the engine, not merely small).
- **Recovery:** `analysis/2026-06-09-a2mu-vs-Q-crux` @ `430194d8` (pushed)

### pathc-z0-amorphous-emt — amorphous z₀ does not derive α (Outcome D)
- **Hypothesis:** coordination-preserving amorphous disorder of the K4 lattice derives the EMT `z₀ = 51.25` (→ α) **α-free**.
- **Verdict:** Outcome D — α not derived (directional signal only).
- **Diagnostic:** disorder **does** reduce `z₀` into a band `[50.87, 51.67]` straddling 51.25 (α-free, via 4-ring formation merging 2-hop endpoints), but **no α-free principle selects 51.25** — the value is set by the (free) disorder strength; the disorder-independent high-disorder steady-state lands at `z₀ ≈ 51.65` (1/α = 138.0), not 51.25. Hitting 51.25 needs an un-derived disorder amount.
- **Tag:** **GENUINE-FALSIFICATION** — the amorphous-z₀ route to α is model-dependent (Outcome D), not a fixed point.
- **Recovery:** `analysis/2026-06-08-pathc-z0-amorphous-emt` @ `e9976bfc` (pushed)

### rectifier-stage1-biased-diode — engineered-gravity chord falsified by chromaticity (Outcome C)
- **Hypothesis:** a biased leaky-diode substrate rectifier produces the achromatic `n > 1` engineered-gravity metric (the engineered-gravity chord).
- **Verdict:** Outcome C — a real but **mundane** rectifier; the chord is falsified at Stage 1.
- **Diagnostic:** the bias breaks the memristive-loop half-period symmetry (`∮directed ≠ 0`, a real charge-pump with an honest ledger), **but** the rectifying element is a **static-E single-sector (ε-only) load**, whose induced `n(r)` is **chromatic** (∝ λ², `n < 1`) → ordinary plasma rectification / radiation pressure, **not** the achromatic `n > 1` gravity metric (§6a chromaticity).
- **Tag:** **GENUINE-FALSIFICATION** — the engineered-gravity chord is falsified at Stage 1; the ε-only load gives the wrong (chromatic, n<1) index.
- **Recovery:** `analysis/2026-06-09-rectifier-stage1-biased-diode` @ `b8e6b022` (pushed)

## Motion-stability negatives

### motion-stability-bemf — stability-from-motion not supported (NULL)
- **Hypothesis:** the moving electron is stabilized by its motion via BEMF (stability **from** motion), in the full-vector Maxwell FDTD engine.
- **Verdict:** NULL (leaning CONTRADICTS) — not supported.
- **Diagnostic:** the base transverse-photon self-trap is validated (retention 0.580 vs 0.389 matched baseline), but the boosted/moving configuration shows no motion-stabilization signature. The PML-clean co-moving re-run (the first was PML-confounded) leaves it NULL — the observable does not cleanly decide.
- **Tag:** **INCONCLUSIVE / NULL** (leaning CONTRADICTS) — regime/observable-limited; see the cleaner companion below.
- **Recovery:** `analysis/motion-stability-bemf` @ `059ae318` (pushed)

### motion-stability-bemf-cosserat — stability-from-motion contradicted via PIN
- **Hypothesis:** Grant's stability-FROM-motion — the saturated `(2,3)` knot's stability comes from its motion (BEMF), on the durable VacuumEngine3D Arm-C host.
- **Verdict:** CONTRADICTS-via-PIN — cleanly (the boost was fixed + validated on a linear pulse first).
- **Diagnostic:** on the engine the saturated knot is **pinned** (native `τ_zx` shear holds it in place) — its stability is **the pin, not the motion**. The validated coherent-phasor boost confirms the probe works; the decisive run contradicts the hypothesis.
- **Tag:** **GENUINE-FALSIFICATION** — stability-from-motion is contradicted; the knot's persistence is the pin (native shear), not its motion.
- **Recovery:** `analysis/motion-stability-bemf-cosserat` @ `c6613c26` (pushed)

---

## Not a ledger entry — flagged for merge-assessment

- **`analysis/2026-06-08-vacuum-z4-coordination-walkback` @ `28026bed`** (pushed) — this is **not a negative**; it is a Tier-C corpus **walk-back** that re-grounds 9 gate-independent claims and **edits 5 canon KB leaves** (`delta-cp-violation.md`, `op14-local-clock-modulation.md`, `k4-tlm-simulator.md`, `first-principles-bond-force-constants.md`, + the neutrino-sector index). The record *is* the walk-back. **Merge-assessment** (does it belong on main?), not a dead-end — held for Grant/auditor, separate from this ledger.

---
