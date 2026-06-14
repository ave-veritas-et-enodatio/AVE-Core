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

### genesis-omega-wave — the ω-shear photon does not self-trap under wave dynamics (III)
- **Hypothesis:** the canonical ω-shear photon (transverse Cosserat-ω wave) self-traps into the electron under Axiom-4 saturation — the "right object, right mechanism."
- **Verdict:** III — no self-trap, in both engine realizations.
- **Diagnostic (source's own, §2/§3/§6):** the **object and the kernel are right** (the ω-shear wave + Axiom-4 saturation) — the failure is the **wrong DYNAMICS CLASS**. Standalone, the saturated curvature energy `E_curv(κ)=γ(κ²−κ⁴/ω_yield²)` is **non-convex** (negative curvature-stiffness past the inflection), so energy-conserving wave dynamics **disperse** (sub-inflection) or **collapse in finite time** (super-inflection) — never confine; coupled `VacuumEngine3D` routes saturation **only to the K4 V-sector, never the ω dynamics** (`cos.use_saturation=False`; ω-coupling force zero under `disable_cosserat_lc_force=True`, `:427-428`), so the ω-photon is a **bare linear wave** and the seeded pure-ω run leaves the **V-sector dark** (`V_inc_max=0.0`, §3). The **wave-dynamics self-trap is thereby decisively falsified** (§6, full sub-yield→over-yield bracket, both engines) — but the **broader corpus ω-photon→electron claim is *not* refuted**: only *this* dynamics class fails, and the boundary-confinement operator that could realize it is **untested** (§5/§6 — an engine-mechanism gap, not a missing axiom). (Positive sub-result, §4: the chiral ω-wave carries coherent charge = Beltrami helicity, sign-flipping with χ, beating the matched baseline.)
- **Tag:** 🔴 **GENUINE-FALSIFICATION — scoped to the wave-dynamics self-trap** (§6: "Falsified (decisively)" across the full sub-yield→over-yield bracket, both engines). The source's own §6 failure label is **"right object + right kernel, wrong dynamics class"** — the falsified item is the *energy-conserving wave-dynamics realization*, **not** the ω-photon→electron route itself. **Re-test (source's own re-aim, §5/§6, pending Grant):** impose the saturation-TIR as a **boundary-impedance / moving `Γ=−1` wall** (boundary condition), not an emergent energy minimum — a *different, untested* mechanism (the `genesis2-wt` `saturation-tir-moving-boundary` thread). **Do not over-read as "the ω-photon does not self-trap"** — only the wave-dynamics route is closed; the boundary-impedance route is open (§6: the corpus claim is not shown wrong). *Later layered re-interpretation (NOT this source's own diagnosis):* in the two-"3"s framing the ω-shear wave is the microrotational-B **charge-"3"** carrier, so self-assembly is re-aimed to the **A1 dilatation-MASS "3"** carrier — the v14 Mode-I breather (a **separate, later** result; **this** source's own V-sector run is **dark**) is the *basis* for that reframe, not a finding of this doc.
- **Recovery:** `analysis/2026-06-06-genesis-omega-wave` @ `cc19416d` (pushed)

### genesis-armB-flywheel-seed — the bare ω-flywheel does not collimate into the (2,3) (III)
- **Hypothesis:** the electron is just three numbers `{ω, R, chirality}` — a bare collimated B-flywheel (Lundquist force-free flux rope in the Cosserat ω field) relaxes under force-free dynamics into the `(2,3)` electron.
- **Verdict:** III — no collimation into `(2,3)`.
- **Diagnostic (source's own finding, §4/§6):** the seeded force-free Beltrami flux rope is **NOT a dynamical attractor** — under the engine's own dynamics the energy-weighted force-free residual **grows** (electron-pt 0.60→0.92; even the well-collimated `k·R=3` control 0.20→0.82): a localized flywheel **de-collimates and disperses**, it does not tighten. It carried the right *quantities* (≈3× the mass, ≈70× the coherent L of the matched baseline) but never a quantized soliton. The source names the failure as **right sector (ω), wrong geometry (flywheel vs WAVE), wrong mechanism (force-free relaxation vs saturation-confinement)**; its immediate re-aim was "seed the ω-shear WAVE" → the **genesis-omega-wave** entry above (which then also returned III).
- **Tag:** **WRONG-CARRIER / SUPERSEDED.** Source's own carry-forward: re-aim to the canonical ω-shear-WAVE genesis (done — also III). The deeper cross-arc lesson, **in the *later* two-"3"s framing** ([master-equation.md](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20): the ω-flywheel is the microrotational-B **charge-"3"** half, and self-assembly needs the **A1 dilatation-MASS "3"** carrier (cf. the genesis-omega-wave entry's "re-test the A1/V-sector"). The three-numbers-from-the-flywheel-alone framing is the pre-two-"3"s picture — a re-interpretation layered on top of the source, not the source's own diagnosis.
- **Recovery:** `analysis/2026-06-06-genesis-armB-flywheel-seed` @ `5cf1a03e` (pushed)

### electron-genesis-drop — pinch-off geometry hosted, (2,3) not (III)
- **Hypothesis:** driving the pure-V photon route to the A→1 pinch-off (the ingredient missing from the 2026-06-04 sub-pinch-off run) nucleates the sub-V_yield `(2,3)` electron.
- **Verdict:** III — pinch-off geometry hosted; the `(2,3)` electron-state not.
- **Diagnostic:** at A→1 the pure-V route **does** pinch off into ℓ_node droplets (single→1, pair→**2** = the geometric e⁺e⁻ split — a positive sub-result), but the droplets stay **over-yield** (V/V_yield ≈ 8–11, lossy), the `(2,3)` does **not** assemble, the chirality split is not captured, and the **Cosserat ω stays exactly 0** in every run — the **Q0 fixed point** (the even-in-ω parametric coupling cannot seed ω from zero, amplitude-independent).
- **Tag:** **INCONCLUSIVE** — the geometry is hosted; the `(2,3)` is blocked by the ω≡0 Q0 fixed point (an engine ω-seeding limitation), not a physical falsification.
- **Recovery:** `analysis/2026-06-06-electron-genesis-drop` @ `71fdb9a2` (pushed)

### screened-winding-probe — v6 `w_pol≡0` READ-absence genuine; through-shell screening UNTESTED (panel-demoted)
- **Hypothesis:** the genesis-v6 null (`w_pol ≡ 0`, the poloidal "3" never forms) might be an **apparatus screen** (a reader that cannot see the winding inside the snap shell), not a genuine absence.
- **Verdict:** BIN = NO-SCREENING **at the GATE level** (Rule 11 — the frozen gates fired as frozen), but the §0 headline ("reads a planted `(2,3)` faithfully through a formed shell / **EXONERATED**") was **PANEL-DEMOTED** (source §8, appended; 1/2 lenses refuted ⇒ branch review-gated).
- **Diagnostic — three honest tiers (per the source §8.2):**
  - **CODE-PROVEN (stands):** the snap writes **ZERO** to `ω/π_ω/w/V` (`unified_genesis_engine.py:304–419`; array-confirmed `max|Δω|=max|Δw|=max|ΔV|=0.00e+00`) — it erases the **bulk `u_adv` circulation** (`:396`) but does **not** screen the **Cosserat-ω read channel**. The "circulation erased by bookkeeping" directive is exactly true for `u_adv`, exactly false for the ω read.
  - **LOAD-BEARING (stands, re-attributed to ARM 2):** the coupled v6 product itself reads `w_pol=0` on **reliable interior contours** (`best_rel=0.813`, fracs 0.5/0.7/0.9 — interior reads cannot be through-shell-screened), insensitive to `omega_recipient_frac` to 6 sig figs. The **read-absence is genuine**.
  - **EMPIRICALLY UNTESTED (the demotion):** through-shell read of a winding in a **COUPLED** config. ARM 1's "exoneration" ran **transducer-OFF**, where the ω channel is decoupled from the snap **by construction** → its transfer is forced to `T≡1.0` (a **tautology**, not a screening calibration); the plant sat **AT** the shell edge, not inside; no ARM-1 field map exists. **Do NOT propagate the "EXONERATED" framing.**
- **Tag:** 🟡 **INCONCLUSIVE / PARTIAL** — the v6 `w_pol≡0` **read**-absence is genuine (ARM 2 interior reads + the code-decouple), but the *screening exoneration* is panel-demoted: coupled through-shell screening is **UNTESTED**, and apparatus-caused **formation-suppression** (does the `:396` `u_adv` erasure at the wall prevent orbital→poloidal twist from ever forming?) remains **OPEN**. **NOT a GENUINE-FALSIFICATION.**
- **Recovery:** `analysis/2026-06-11-screened-winding-probe` @ `836ee6de` (pushed as an **archival recovery pointer**; the source's own disposition is **unpushed / review-gated — panel not clean**, so this is *not* a merge candidate).

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
- **Tag:** **GENUINE-FALSIFICATION** of the *topological-random* (WWW) amorphous selection of 51.25 — the maximally-randomized ensemble's steady-state lands at `z₀ ≈ 51.65`, not 51.25 (Outcome D, model-dependent, not a fixed point). **Scope caveat (source "Path forward" §1 + Caveat #1):** the **energy-relaxed CRN** (Keating/WWW strain-minimized a-Si-class network) is the *decisive* Path-C test and is **NOT yet run** — this first pass is explicitly its "scaffold + null bracket." The topological-random route is closed; all of Path C is **not**.
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
- **Diagnostic:** the base transverse-photon self-trap is validated (retention 0.580 vs 0.389 matched baseline), but the boosted/moving config shows **no motion-stabilization signature**. The co-moving retention *does* rise with v — but a sub-saturation **LINEAR control rises as much**, so the rise is **generic transport, not the back-EMF** (the AVE-distinct discriminator fails); meanwhile saturation depth *falls* with v and `τ_zx` **anti-correlates** with the gain (−0.81). NULL on the transport metric, leaning CONTRADICTS on every trap-integrity metric. **Engine-scoped:** `fdtd_3d.py` carries only the **E/H projection** of the Cosserat `τ_zx` — a Cosserat-sector back-reaction would be invisible here, which is exactly what the native-carrier companion below re-ran.
- **Tag:** **INCONCLUSIVE / NULL** (leaning CONTRADICTS) — regime/observable-limited (E/H-projection engine); the cleaner native-carrier companion below resolves it to GENUINE-FALSIFICATION (CONTRADICTS-via-PIN).
- **Recovery:** `analysis/motion-stability-bemf` @ `059ae318` (pushed)

### motion-stability-bemf-cosserat — stability-from-motion contradicted via PIN
- **Hypothesis:** Grant's stability-FROM-motion — the saturated `(2,3)` knot's stability comes from its motion (BEMF), on the durable VacuumEngine3D Arm-C host.
- **Verdict:** CONTRADICTS-via-PIN — cleanly (the boost was fixed + validated on a linear pulse first; all four forward-predicted signs confirmed).
- **Diagnostic:** under the validated coherent-phasor boost a sub-saturation **LINEAR pulse advects** (sign-symmetric ±0.053 cell/τ) but the saturated `(2,3)` self-trap **does not move** — its residual velocity is boost-direction-independent self-drift (no sign-flip, 0.10× the linear response). The knot is **pinned by its own frozen clock**: the deeply-saturated core (A²≈3.07 ≫ 1 ⇒ `S=√(1−A²)=0` ⇒ `c_eff=c·√S→0`) **cannot advect**. Retention does not rise with v, and the native back-EMF **does not** stabilize: `corr(τ_zx, gain) = −0.40 ≤ 0` — the large `τ_zx ≈ 6×10⁵` is the **static rupture-floor stress** of the frozen core, *not* a motion-induced stabilizer.
- **Tag:** **GENUINE-FALSIFICATION** — stability-from-motion is contradicted; the knot's persistence is the **frozen-clock pin** (`S=0 ⇒ c_eff→0`, it is stable *because it is static*), **not** its motion — and not `τ_zx`, which anti-tracks stability. The native-`τ_zx` engine agrees with the Maxwell-projection companion below.
- **Recovery:** `analysis/motion-stability-bemf-cosserat` @ `c6613c26` (pushed)

---

## Not a ledger entry — flagged for merge-assessment

- **`analysis/2026-06-08-vacuum-z4-coordination-walkback` @ `28026bed`** (pushed) — this is **not a negative**; it is a Tier-C corpus **walk-back** that re-grounds 9 gate-independent claims and **edits 5 canon KB leaves** (`delta-cp-violation.md`, `op14-local-clock-modulation.md`, `k4-tlm-simulator.md`, `first-principles-bond-force-constants.md`, + the neutrino-sector index). The record *is* the walk-back. **Merge-assessment** (does it belong on main?), not a dead-end — held for Grant/auditor, separate from this ledger.

---
