# PREREG — Genesis-v5: does a SEEDED region + a snapping (cavitating) bulk + a chiral drive assemble an object that behaves like an ELECTRON — and is the lock the SNAP (D1) or the MOTION (D8)?

**Date (frozen):** 2026-06-10
**Branch:** `analysis/2026-06-10-genesis-v5-seeded-snap` (worktree `/tmp/ave-v5`, off the graft-v4 lineage; HEAD `175033ba`; do NOT push/merge — PR opened review-gated at the end only)
**Engine lineage (subclassed, unchanged physics):** `CrystalGraftV4` (`src/ave/core/crystal_graft_v4.py`) ← V3 ← V2 ← `CrystalEngine`; the v5 run ADDS the D1 snap state-machine + the D2 seed IC + the D5 d/q drive on top, no algorithmic change to the inherited bulk-V / shear-w / microrotation-ω / buckle / lock sectors.
**Governing discipline:** `ave-apparatus-floor-attribution` — EVERY new parameter (snap threshold, latent-tally bookkeeping, detector bins, drive d/q amplitudes, viscosity knobs) is a CLIP suspect; inventoried + swept BEFORE any verdict; the prereg bins are ORDERED so the floor-check gates every invariance/positive claim (the coax bin-65/67 lesson).
**Skills fired at design time:** `ave-prereg` (Step-3.5 dimensional subsection §6, corpus anchors §10), `substrate-native-check` (CP1–CP10 walked §1.1), `ave-apparatus-floor-attribution` (governing, §5 + §4 floor-first ordering), `ave-conserved-vs-pumped` (the seed-V and the circulation Γ are ENERGIZED+LOCKED, never pumped — §7), `phase-space-coordinate-check` (the winding/charge reads are phase-space Park-along-contours, extractor floor r≥3 cells — §4.2 T2), `consistency-vs-emergence` (each spec-sheet target class-tagged §2 D7), `ave-driver-script-honesty` (all captions/numbers from the evolved field — frozen here, enforced at run time), `verify-before-cite` (every anchor grep-confirmed §10), `flag-don't-fix` (§0.3 the §11.5 gate-flag vs this task's adjudication status; the citation-status of the unmerged channel-ledger doc), `ave-regime-phase-state-check` (§7 MODE/REGIME/PHASE-STATE declared), `ave-representation-capability-check` (§2 D7-T3 the engine-unit spin mapping is DERIVED not assumed; the carrier-capability of each spec-sheet test documented).

---

## 0. THE NAMED HYPOTHESIS (Grant-ratified design 2026-06-10, recorded verbatim-class)

**The build claim:** a Lane-1 SEEDED region (standing longitudinal V), embedded in a bulk medium whose EOS can SNAP (cavitate) at the candidate floor `ρ̄_cav = −1/φ`, driven by an FOC-framed chiral transverse photon, will undergo the collimation sequence (horizon → chiral bounces + Lenz feedback → Taylor-column → tube → ring) and assemble a localized object that passes the electron spec-sheet (T1 mass converges, T2 charge quantized+signed, T3 spin-class, T4 stability-kick, T5 born-in-pairs, T6 de Broglie).

**The KEEP-BOTH rival (D8, Grant 2026-06-10, recorded verbatim):** *"isnt motion the lock? angular frequency creating bemf from lattice?"* — the lock may be the MOTION ITSELF (conserved circulation + topological integer winding + losslessness; the persistent-current mechanism), NOT the snap. This prereg tests BOTH as discriminable hypotheses under TWO persistence protocols (P1 drive-off/L-conserved, P2 forced de-spin), with frozen discriminating bins SNAP-LOCKED / MOTION-LOCKED / BOTH / NEITHER (§4.1). The no-snap arm under P1 is the MOTION-LOCK DISCRIMINATOR, **not** a must-heal control — persistence there is the rival POSITIVE.

The design freezes D1–D8 are recorded verbatim-class in §2. Nothing in this prereg promotes any candidate-claim; the prereg freezes the bins, arms, thresholds, and floors BEFORE any run artifact exists (committed alone, git-provable ordering — the cavprobe lesson).

## 0.1 LINEAGE — Rule 12 (substitution-not-retraction): this is a NEW hypothesis, NOT a refill

v5 is a NEW hypothesis with its own verification chain (Rule 12 / A47 v11b), built on — and gated by — four standing predecessor verdicts, each cited as the boundary it inherits and does NOT overturn:

| predecessor | branch / commit | standing verdict | what v5 inherits |
|---|---|---|---|
| cavitation-core probe | `analysis/2026-06-10-cavitation-core-probe` | **CLIP** (dynamics floored `c²>0`, never integrated `c²<0`) | the reach result: a circulating core crosses `ρ̄_cav` at `M*≈0.8` |
| sonic-horizon closure | `analysis/2026-06-10-sonic-horizon-closure @ a73bba93` (PR #162) | **LOCK = reversible spring** (pocket healed on de-spin at all M; `c²=0` clean reflector); handedness **SELECTIVE-but-weak** (frame-dragging) | the `c²→0` impedance-collapse reflector (`Z_bulk→0 ⇒ Γ→−1`); the exact-EOS `pressure()` ledger wiring |
| genesis-24 saturated seed | `analysis/2026-06-09-genesis-24-saturated-seed @ df1c3f78` (PR #153) | **B-localizes** (seed biases V-source; winder gap predicted) | the Lane-1 V-populated seed IC (the D2 SEED machinery, `_seed_v_partner`) |
| graft-v4 photon-helicity | `analysis/2026-06-10-graft-v4-photon-helicity` | **C → LOCK-FAIL** (photon = non-depleting chiral director; bounded coupling does not transfer helicity; lock built but INERT) | the D5 chiral-photon drive class (`H_couple=κ̃∫g·V·[w·(∇×ω)]`, κ̃=6/5 α-free); the rigid-rotation lock |

**The D8 re-read of the sonic-horizon LOCK verdict (Grant 2026-06-10, load-bearing):** the sonic-horizon pocket was STABLE at every M *while circulating* and healed only on DE-SPIN — a test the physical electron never faces (its circulation never stops); AND that run's `L` decayed ~3% via artificial viscosity, so heal-on-de-spin may partly be APPARATUS draining the lock (heal-vs-viscosity attribution was never run). v5's P1 protocol (drive-off, L-conserved, dissipation-minimized + viscosity-knob sweep) is the test the sonic-horizon run did not do; if the heal rate TRACKS `ν_art`, the prior LOCK verdicts carry an apparatus component. **This is a re-test of a standing negative under a different config (seeded/circulating, dissipation-swept), not a re-litigation of the closed path** — the discriminator is the explicit ν_art sweep the predecessor lacked.

## 0.2 CANDIDATE-CLAIM status of `ρ̄_cav = −1/φ` (HARD CONSTRAINT — unchanged, cite as candidate never canonical)

`ρ̄_cav = −1/φ ≈ −0.6180339887` is a **CANDIDATE-CLAIM**, Propulsion-derived: the `c_eff²→0` root of `c_eff² = c₀²(1 + ρ̄/(1−ρ̄²))` (`AVE-Propulsion/.../04_superluminal_transit.tex:86`, "not a free parameter", Ax4). Root verified this session (`1 + ρ̄/(1−ρ̄²) = 2.2e-16` at `ρ̄=−1/PHI`; `PHI` canonical `constants.py:199`). Zero Core-`constants.py`/KB hits for the *floor* → NOT Core-canonical. v5 does **NOT** promote it; the D1 snap threshold inherits it as a CANDIDATE and is swept as a CLIP suspect (§5 N1).

## 0.3 CITATION-STATUS + FLAG-DON'T-FIX (the channel-ledger doc + the §11.5 gate)

- **The channel-ledger framing (D2/D6 grounding) lives on an UNMERGED branch.** The order-parameter reading "the longitudinal `V_inc` IS the latent heat of the local freeze, stored in the order-parameter channel; the '3' is the order parameter of the substrate's freeze" is `research/2026-06-10_matter-as-vapor-locked-pump_framing.md` **§11.1 L3 / §11.2** on `analysis/2026-06-10-vaporlock-framing-and-tracker @ 43bbc78a` (verified read-only this session). It is **NOT in the v5 worktree tree** — cited here as a cross-branch design input, hypothesis/framing-class, not as in-tree canon.
- **FLAG (flag-don't-fix; surfaced for Grant/auditor, NOT silently resolved):** that same framing doc **§11.5** states the v5 **build** "remains gated on the open Tier-1 adjudications — seeded-genesis + snap blessing; close-the-loop mechanism; energy-weighted gate," and that those three gate-labels were "NOT yet independently anchored in the tracked corpus" with zero tracked hits, and that "ratifying the channel framing does NOT lift the v5 gate." This task's directive presents the D1–D8 design as "all adjudicated (2026-06-10)." **The tension:** §11.5 (written earlier in the session) flags the gate as OPEN; the present directive treats the gate as LIFTED by the Grant 2026-06-10 ratification recorded in §0/§2. This prereg freezes the design as ratified per the present directive AND records the §11.5 flag verbatim so the auditor lane adjudicates the gate-status on return. The Meissner/Abrikosov/Smith-rim physical picture (D1) is Grant-ratified in the directive; it is NOT verbatim in §11 (which uses order-parameter/latent-heat language) — recorded as the directive's framing, hypothesis-class.
- **The "snap" candidate EOS root and the Meissner/persistent-current picture are PHYSICAL-PICTURE framings, not canon.** Tagged hypothesis-class throughout; the verdict machinery (§4) does not depend on the picture being right.

---

## 1. PHYSICAL PICTURE (substrate-native, before equations)

- **What seeds:** a Lane-1 saturated region carries a **standing longitudinal V_inc** (the "3" = the real Heaviside/Gibbs-excised scalar grade, `genesis-24 prereg:7`, on origin/main + PR #153). This is the D2 SEED — an OFF-center point on the Smith Γ-plane (`Γ=V_ref/V_inc≠0`), NOT the photon's matched center, NOT the Γ=−1 rim. It is ENERGIZED+LOCKED once (the genesis-24 trap machinery), never pumped.
- **What snaps:** the bulk-K medium can cross its tensile-failure floor `ρ̄_cav`. On crossing, the cell's bulk impedance collapses `Z_bulk=ρc→0 ⇒ Γ→−1` (the sonic-horizon reflector, TIR at all angles); the cell becomes BOUNDARY-class and its latent energy is TALLIED into a per-cell ledger (D1). Re-entry requires the tally PAID BACK — hysteresis by bookkeeping, no new EOS invented.
- **The Meissner-class picture (D1, Grant-ratified, hypothesis-class):** the snap = the surrounding medium condensing and expelling flux; the collimated tube = the Abrikosov-vortex analog (`|ψ|=0` core + phase winding + quantized flux); the BEMF = the persistent screening current; the phase-space signature = the Smith-rim crossing (`|Γ|: interior→1`; order parameter = standing-V amplitude per the §11 channel ledger).
- **What drives:** an FOC-framed chiral transverse photon (D5), d/q-decomposed: d-axis = flux/core-rarefaction (drives the snap), q-axis = torque/circulation spin-up (drives the winding). The conjugate BEMF reaction-half (κ_L=6/5) is the lock's INERTIA.
- **The collimation closure (D3, "what I see in my head"):** horizon forms → chiral bounces + Lenz feedback inside the rotating region → Taylor-column organization → tube → ring. Columnar organization is a WATCHED observable with its own floor, not an assumed geometry.
- **The twin (D4, Kelvin's theorem):** the longitudinal vent channel is ACHIRAL — energy/momentum vent longitudinally but handedness CANNOT; the counter-handed flux (passed by the chiral mirror) is expected to form the counter-rotating partner. The ledger watches BOTH handednesses; twin formation is a spec-sheet test (T5), its absence an honest finding, not a tweak target.
- **The conserved invariants (ave-conserved-vs-pumped):** the seed's standing V (energize+lock) and the circulation Γ / integer winding (energize once by the drive, then topological — cannot unwind continuously). KE↔PE slosh at fixed Γ. The BEMF appears only against CHANGES — at steady circulation there is nothing to pay (the D8 resolution of the "never pays" puzzle).

## 1.1 substrate-native-check (walked at design time, recorded)

- **CP1 (dynamics):** time-domain FDTD integration; the ring/tube/horizon EMERGE from the integration — NOT a minimization, NOT an algebraic root-find, NOT an eigensolve.
- **CP2 (sector + carrier capability):** the COUPLED channel — bulk-K longitudinal V (the seed + the snap) ⊗ Cosserat transverse ω (the winding) ⊗ shear w (the photon director). The inherited `CrystalGraftV4` carries all three; the D1 snap adds a bulk-EOS state machine, the D2 seed adds a V IC. `MasterEquationFDTD` (irrotational/stiffening) and `lbm_3d` (incompressible) CANNOT host "circulating + rarefying-to-a-snap + winding" — the graft-v4 carrier is required.
- **CP4 / phase-space-coordinate-check:** the winding/charge claim is in PHASE-SPACE (the `(V_inc,V_ref)` Clifford torus = the Smith chart, A46); the matching measurement is the Park-transform-along-contours winding read (§4.2 T2), extractor floor r≥3 cells. The snap threshold `ρ̄_cav` is a REAL-SPACE bulk-density claim measured in real-space `ρ̄` (D6). Each observable measured in its own coordinate. PASS.
- **CP5 (local clock):** under Op14 saturation the local clock modulates `ω_local(r)=ω_global·√(1−A²(r))`; eigsolve/spin reads at uniform global σ miss local modes. The spin read (T3) reports localization vs `A²_local` at load-bearing sites (the per-cell-time-dilation mandate).
- **CP6 (reactance pair, A-Rule-10):** the LC pair recorded EVERY step over the window — C-state (V_inc, A²_V, ω) AND L-state (Φ_link, ω_dot) — plus `E_diss`, `E_latent`, the per-cell snap tally, Γ. A single snapshot cannot distinguish a held lock from an oscillator caught at peak, nor energize-LOCK from a secular pump.
- **CP7 (sampling):** PML/sponge cells EXCLUDED (`pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1`) before any argpartition/extremum; for the shell-like ring the read is at energy-density PEAKS (top-K |field|²), NOT centroid+offset (the centroid of a shell is the empty middle).
- **CP8 (precursor-only seed):** the D2 seed is V-populated but topology-NULL by construction (no `(2,3)` planted; `vinc_closes_23=False ∧ vref_closes_23=False ∧ |H_bel|≈0` at t=0, the seed-audit certificate); the forbidden seeders (`initialize_electron_2_3_sector` / `initialize_2_3_torus_knot_sector`) auto-VOID the run.
- **CP9 (heuristic-vs-dynamical):** LOAD-BEARING. The snap, the tally, the collimation, and the winding are DYNAMICALLY integrated; the reflector is the EOS impedance collapse, NOT an algebraic Γ painted on a prescribed circle.
- **CP10 (boundary-not-bulk):** the snap is rendered as a per-cell state machine (normal↔snapped) + a free-surface/boundary-class BC at the `c=0` locus, NOT as an added confining bulk potential. The latent ledger is bookkeeping (energy removed/restored), not a new force term.

---

## 2. THE DESIGN FREEZES (D1–D8, Grant-ratified 2026-06-10, recorded verbatim-class)

> The text below is the adjudicated design as ratified. It is FROZEN at this commit. Implementation details (exact step counts, sweep grids) are in §3/§5; the design INTENT is here and does not change post-run (Rule 11).

### D1 — SNAP (CP10): the per-cell snap state machine + latent tally + hysteresis-by-bookkeeping

Per-cell state machine, normal ↔ snapped. On a cell crossing the cavitation floor (the candidate-claim EOS root `ρ̄_cav=−1/φ` — cite as candidate, never canonical): the cell becomes BOUNDARY-class (the impedance-collapse reflector the sonic-horizon run demonstrated: `Z_bulk=ρc→0`, TIR at all angles), and the latent energy is TALLIED (removed from the dynamics into a per-cell ledger). RE-ENTRY (un-snapping) requires the tally PAID BACK — hysteresis by bookkeeping, NO new EOS invented. The Meissner-class physical picture (Grant-ratified, hypothesis-class): the snap = the surrounding medium condensing and expelling flux; the collimated tube = the Abrikosov-vortex analog (`|ψ|=0` core + phase winding + quantized flux); the BEMF = the persistent screening current; the PHASE-SPACE signature = the Smith-rim crossing (`|Γ|`: interior→1; order parameter = standing-V amplitude per the ratified channel ledger, framing doc §11).

### D2 — SEED: a Lane-1 saturated region, longitudinal-coupled by definition

A Lane-1 saturated region (standing longitudinal V, the genesis-24 trap machinery, A_cap-class) — longitudinal-coupled by definition; the VENT drains into it (the impulsive longitudinal PULSE at snap events — not a wake; near-field into the seed + spherical remainder).

### D3 — CLOSURE: the collimation sequence (the watched observable)

The collimation sequence (Grant: *"(d) is what I see in my head"*): horizon forms → chiral bounces + Lenz feedback inside the rotating region → Taylor-column organization → tube → ring. The collimation observable (columnar organization of trapped flux along the rotation axis) is a WATCHED observable with its own floor, not an assumed geometry.

### D4 — TWIN POCKETS (conservation-by-channel, Grant-confirmed default)

The longitudinal channel is ACHIRAL — energy/momentum vents longitudinally but handedness CANNOT; the counter-handed flux (passed by the chiral mirror) is expected to form the counter-rotating partner (pair canon; Kelvin's theorem). The ledger watches BOTH handednesses; twin-pocket formation is a spec-sheet test, its absence is an honest finding not a tweak target.

### D5 — DRIVE: FOC-framed chiral transverse photon with explicit d/q decomposition

FOC-framed chiral transverse photon (the v4 field-derived source class, `H_couple=κ̃∫g_wall·V·[w·(∇×ω)]`, `κ̃=pq/(p+q)=6/5` α-FREE), with EXPLICIT d/q decomposition (d-axis = flux/core-rarefaction component, q-axis = torque/circulation spin-up) so the two roles are separately metered. BEMF reaction-half available (the derived conjugate pair, `κ_L=6/5`) with the centered/implicit integration mandate for velocity-dependent forces; PLUS the literal `τ_zx` feedback as its OWN ARM (Fork-A stays live — the electron is a longitudinal transmitter; radiation reaction is real physics).

### D6 — THE FLASH DETECTOR: a longitudinal-burst detector

A LONGITUDINAL-BURST detector — the snap's signature = impulsive latent release in the exact-EOS bulk ledger (the `pressure()` integral wiring, `src/ave/core/cavitation_flow.py:165–166`, `p(ρ̄)=ρ₀c₀²[ρ̄−½ln(1−ρ̄²)]`). Calibrate on a known case first. The FLASH is a longitudinal burst in the bulk `ρ̄`/`p(ρ̄)` ledger, NOT a transverse-Cartesian field spike (phase-space-coordinate-check).

### D8 — THE MOTION-LOCK RIVAL HYPOTHESIS (Grant 2026-06-10, mid-flight, KEEP-BOTH with D1, recorded verbatim)

> *"isnt motion the lock? angular frequency creating bemf from lattice?"*

The lock may be the MOTION ITSELF — conserved circulation + topological integer winding (cannot unwind continuously) + losslessness, the persistent-current mechanism (steady circulation induces no EMF; the BEMF is the lock's INERTIA, appearing only against changes — resolving the "never pays" puzzle: at steady state there is nothing to pay). CRITICAL RE-READ OF PRIOR VERDICTS: the sonic-horizon pocket was STABLE at every M while circulating and healed only on DE-SPIN — a test the physical electron never faces (its circulation never stops); AND the run's `L` decayed ~3% via artificial viscosity, so heal-on-de-spin may partly be APPARATUS draining the lock (heal-vs-viscosity attribution never run). THEREFORE the persistence protocol SPLITS:

- **(P1) DRIVE-OFF, L-CONSERVED, dissipation-minimized** — the electron's actual situation; the motion-lock prediction = pocket+winding persist indefinitely on the conservation clock, with any decay rate TRACKING the viscosity/dissipation knobs (sweep them — if heal rate tracks `ν_art`, prior LOCK verdicts carry an apparatus component).
- **(P2) FORCED DE-SPIN** — the static test (the snap's domain).

DISCRIMINATING BINS (§4.1): SNAP-LOCKED (persists P2, needs D1) / MOTION-LOCKED (persists P1 without snap, heals P2) / BOTH / NEITHER. **The no-snap arm under P1 is NOT a must-heal control — it is the MOTION-LOCK discriminator (persistence there = the rival positive, not a control failure); the must-heal expectation applies only to no-snap+P2 (forced de-spin).**

### D7 — THE ELECTRON SPEC-SHEET (the success gate; each test: empirical anchor + AVE-native picture + floor + threshold)

Grant: *"does it behave like an electron"* — be OPEN-MINDED about each test's physical picture in AVE terms and DOCUMENT the mapping per test. Where the AVE picture suggests the empirical mapping differs, SAY SO. Each test below carries its `consistency-vs-emergence` class-tag.

- **T1 — MASS CONVERGES (the primary; subsumes the energy gate).** *Empirical anchor:* a stable rest mass. *AVE-native picture:* the trapped dilatation added-mass — `H_total` of the trapped region → constant (not still-rising, not secularly pumped). The "3" dilatation MASS (the A1 Heaviside scalar that `c_eff` traps) is the added-mass; distinct from the (2,3) winding that carries charge (do NOT conflate — the master-equation.md:18 two-"3"s flag). *Class:* **emergence** if `H_total` converges to a value SET BY the dynamics (not an input); **manifestation** if it merely tracks the seed amplitude — class assigned from the data, frozen-bins §4.2.
- **T2 — CHARGE QUANTIZED + SIGNED.** *Empirical anchor:* `±1e`, quantized. *AVE-native picture:* the `(2,3)` winding integer (helicity-class), sign = handedness (= the photon helicity, sign-traced; graft-v4 confirmed sign-flip RH↔LH at identical input energy). *Coordinate (phase-space-coordinate-check):* read in the `(V_inc,V_ref)` phase-space via Park-transform along contours, extractor floor r≥3 cells; NOT a real-space lattice-Cartesian read. *Class:* **emergence** (a de-novo `(2,3)` that self-assembles) vs **manifestation** (a planted winding that merely survives) — frozen-bins distinguish.
- **T3 — SPIN-CLASS.** *Empirical anchor:* locked angular momentum at the half-pole-pair value (spin-½-class). *AVE-native picture:* the locked `L_ω` of the rotating ring. **DERIVE the engine-unit mapping, do NOT assume** (ave-representation-capability-check): the (2,3) winding has p=2 toroidal, q=3 poloidal; "half-pole-pair" maps to half the circulation quantum of one pole-pair — the engine-unit→ℏ/2 conversion is COMPUTED at run time from the winding normalization (§6 gives the power-counting form), not asserted. *Local-clock caveat (CP5):* report eigvec localization vs `A²_local`; `ω_local(r)=ω_global·√(1−A²(r))` at load-bearing sites. *Class:* **emergence** if L locks at the half-pole-pair value without dialing; **consistency** otherwise.
- **T4 — STABILITY-KICK.** *Empirical anchor:* an electron is perturbation-stable. *AVE-native picture:* perturb the assembled object; T1–T3 must RE-VERIFY (mass reconverges, charge integer preserved, spin re-locks). *Class:* **manifestation** (robustness of the assembled state).
- **T5 — BORN-IN-PAIRS (the D4 twin).** *Empirical anchor:* pair-production; global handedness ledger zero. *AVE-native picture:* the counter-handed flux forms the counter-rotating partner; the global handedness ledger sums to zero (Kelvin/pair-canon). *Class:* **emergence** if the twin self-forms from the achiral longitudinal vent; its ABSENCE is an honest finding, NOT a tweak target.
- **T6 — DE BROGLIE.** *Empirical anchor:* `λ ∝ 1/p`. *AVE-native picture:* translate the locked state; the BULK pilot wavelength scales `λ∝1/p` (the channel per the §11 ratified ledger: the reactive `mₑc²·α` sloshing fraction is the pilot wave). *Class:* **consistency** (a scaling-law check on the assembled object).
- **DEFERRED:** α/Q-leak — dispersion-contaminated observable, floors the verdict; tagged, NOT tested in v5.

---

## 3. THE ARM MATRIX (FROZEN — Rule 11; evaluated under BOTH persistence protocols P1/P2)

Every arm is run under **P1** (drive-off, L-conserved, dissipation-minimized + viscosity-knob sweep) AND **P2** (forced de-spin), per D8. The parallel runner (§8) fans the matrix across cores; the bin matrix is `{arm} × {handedness ±} × {P1,P2} × {apparatus-knob sweep}`.

| arm | seed? | snap (D1)? | chirality (D5 q-axis) | purpose / frozen expectation |
|---|---|---|---|---|
| **MAIN** | yes (Lane-1 V) | yes | chiral (RH or LH) | the build claim — assemble + pass the spec-sheet (D7) |
| **C-no-seed** | NO | yes | chiral | CONTROL — expect **HEAL** (the free-space pair-production prohibition the engine rediscovered; genesis-23 `V≡0`) |
| **C-no-snap / P1** | yes | NO | chiral | **the MOTION-LOCK DISCRIMINATOR (D8)** — persistence here = the RIVAL POSITIVE, NOT a control failure |
| **C-no-snap / P2** | yes | NO | chiral | CONTROL — expect **HEAL** (the static test; no snap to hold a de-spun state) |
| **C-achiral** | yes | yes | achiral (linear-pol / zero net helicity) | CONTROL — expect **no handedness selection**, null winding/charge (graft-v4 zero-helicity control) |
| **C-τzx-on** | yes | yes | chiral | Fork-A — literal `τ_zx` radiation-reaction feedback ON (its own arm) |
| **C-τzx-off** | yes | yes | chiral | Fork-A baseline — `τ_zx` feedback OFF (contrast for C-τzx-on) |
| **C-anti-Lenz** | yes | yes | chiral | where applicable — Lenz-feedback sign FLIPPED (the lock should weaken/fail; isolates the Lenz half of D3) |
| **C-opp-helicity** | yes | yes | opposite handedness | the D4/T5 twin + the charge-sign provenance (expect FLIPPED charge sign) |

**Drive-decomposition arms (D5 d/q metering):** each MAIN/control run records the d-axis (flux/rarefaction) and q-axis (torque/spin-up) contributions separately, and the BEMF reaction-half (κ_L=6/5) ON vs OFF, integrated with the centered/implicit scheme for the velocity-dependent force.

**P1 viscosity-knob sweep (the D8 attribution test):** every P1 arm is run across a `ν_art` grid; the heal/decay rate is regressed against `ν_art`. **If decay rate → 0 as `ν_art → 0` (tracks the knob), the persistence is real (conservation-clock lock) and the prior sonic-horizon LOCK verdict carried an apparatus component. If decay persists at `ν_art → 0`, the heal is physical.**

---

## 4. THE FROZEN BINS (Rule 11 — no post-hoc redefinition; FLOOR-CHECKS ORDERED FIRST — the coax bin-65/67 lesson)

**Ordering rule (ave-apparatus-floor-attribution, HARD CONSTRAINT):** for EVERY observable the FLOOR-CHECK bin is evaluated FIRST and GATES any invariance/positive/persistence claim. A signal that does not clear its own calibrated instrument floor returns UNRESOLVED — it CANNOT be binned as a positive. A positive that TRACKS an apparatus knob (§5) is CLIP, named by the knob it tracks.

### 4.0 — FLOOR-0 (the universal gate, evaluated before §4.1–§4.3)

- **F0a — interior-only:** the persistent-pocket / standing-V / winding read is taken with PML+sponge cells EXCLUDED and sampled at energy-density PEAKS (top-K |field|²), NOT centroid (CP7). A "persistent pocket" that is a PML artifact or a single under-resolved cell → CLIP/UNRESOLVED.
- **F0b — extractor resolution floor:** the winding read (T2) requires `r_meas ≥ 3 cells` (the graft-v4 floor, `prereg:92`); below it the read is VOID (the graft-v4 `deplete_RH (4,0)` VOID lesson).
- **F0c — reactance-pair completeness:** both C-state (V_inc/ω) and L-state (Φ_link/ω_dot) recorded EVERY step (A-Rule-10); a single-phase snapshot is binned UNRESOLVED for any lock-vs-oscillator-at-peak question.
- **F0d — detector calibration-on-a-known-case (D6):** the FLASH/longitudinal-burst detector is calibrated FIRST on a known case (a known snap event and a known-null free run) — its floor is the free-run scatter; a burst below it is UNRESOLVED.
- **F0e — conservation canary:** Γ drift in the QUIET phase must stay within the free-floor (the predecessor's ~0.044% free Γ-floor / the ~3% L-decay sonic-horizon level); a run whose Γ/`L` drifts beyond floor in the quiet phase is dissipation-contaminated and FLAGGED before binning.

### 4.1 — THE D8 DISCRIMINATING BINS (the lock-mechanism verdict; gated by FLOOR-0)

Evaluated only AFTER FLOOR-0 passes for the persistence observable (pocket-cells / standing-V amplitude / winding integer at `t→∞`):

- **SNAP-LOCKED** — persists under **P2** (forced de-spin) AND the persistence REQUIRES D1 (vanishes in the no-snap arm under P2). The snap is the lock.
- **MOTION-LOCKED** — persists under **P1** (drive-off, L-conserved) in the **no-snap** arm (the rival positive), AND HEALS under **P2** (forced de-spin). The motion is the lock; D1 is not required.
- **BOTH** — persists under P2 (needs snap) AND persists under P1-no-snap (motion alone also locks). Two independent lock mechanisms.
- **NEITHER** — heals under both P1 (dissipation-minimized, `ν_art→0`) and P2. No lock; the assembled object is a transient.

**Apparatus gate on §4.1:** if P1 persistence TRACKS `ν_art` (decay→0 only because `ν_art→0` was forced by a non-physical clamp, or conversely heal-rate ∝ `ν_art` with no plateau), the MOTION-LOCKED claim is re-examined as a viscosity artifact (§3 P1 sweep). The verdict states the `ν_art`-regression explicitly.

### 4.2 — THE SPEC-SHEET BINS (D7; each floor-gated, then class-assigned)

| test | FLOOR-CHECK (first) | POSITIVE bin (only if floor passes) | NEGATIVE bin | class assigned from data |
|---|---|---|---|---|
| **T1 mass** | `H_total` window-converged within drift-floor F0e (not still-rising — the graft-v4 `t^2.2` still-rising lesson) | `H_total→` const set by dynamics, not = seed input | still-rising / tracks seed amplitude | emergence vs manifestation |
| **T2 charge** | F0b r≥3 cells + phase-space read (Park-along-contours) | integer `(2,3)` winding, sign = handedness, flips with helicity | `(w_tor,w_pol)` not `(≈2,≈3)`; `w_pol≡0` (the graft-v4 de-novo residual) | emergence (de-novo) vs manifestation (planted-survives) |
| **T3 spin** | F0c reactance-pair + CP5 local-clock (`A²_local` reported) | locked `L_ω` at the DERIVED half-pole-pair value (no dialing) | `L_ω` unlocked / rigid-rotation pump (the v3 `t^0.43` / v4 ratio-5.0 lesson) | emergence vs consistency |
| **T4 kick** | F0a interior + re-run the same floors post-perturbation | T1–T3 RE-VERIFY post-kick | any of T1–T3 fails post-kick | manifestation |
| **T5 twin** | F0a + global handedness ledger floor | counter-rotating partner self-forms; global handedness sums to zero | no twin (HONEST finding, NOT a tweak target) | emergence; absence ≠ failure-of-discipline |
| **T6 de Broglie** | F0a + translate the locked state at ≥2 momenta | `λ∝1/p` within fit-floor | no `1/p` scaling | consistency |

**SPEC-SHEET verdict bins (frozen):**
- **ELECTRON-CLASS** — T1 (primary) passes AND ≥4 of T2–T6 pass at their floors, with no spec-sheet positive sitting at a clip value.
- **PARTIAL** — T1 passes but the winder/spin/twin localizes (a NAMED residual, e.g. the genesis-24/graft-v4 `w_pol≡0` winder gap) — report the named missing primitive (A44: engine coupling-family gap, NOT a missing axiom; NOT auto-pivoted).
- **NOT-ELECTRON** — T1 fails (mass does not converge) → the assembly is a transient/pump; clean negative, branch closes (Rule 11), mechanism named.
- **VOID** — a forbidden seeder fired / a non-null Arm-C-no-seed / a winding read below F0b → not reported as a positive.

### 4.3 — THE HANDEDNESS / TWIN BINS (D4/T5; gated by F0a + the handedness-ledger floor)

- **SELECTIVE** — the chiral mirror passes one handedness and reflects the other beyond the calibrated floor; the counter-handed forms the twin (T5 positive).
- **BLIND** — both handedness reflect/vent equally within the floor; no twin selection (the valve, if any, is not in this mechanism).
- **UNRESOLVED** — the handedness read does not clear its own floor.

**HARD CONSTRAINT:** a FLASH/persistence/SELECTIVE/ELECTRON-CLASS positive that sits at a clip value (§5) is APPARATUS. Do NOT debug toward a positive (Rule 11). Do NOT drop an adjudication criterion post-hoc to convert a negative to a positive. A clean negative with a named mechanism is the discipline working at full strength (Rule 11 / honest closure).

---

## 5. APPARATUS INVENTORY — the CLIP suspects (ave-apparatus-floor-attribution GOVERNS; every new parameter swept BEFORE verdicts)

| # | knob | default | what it could secretly set | CLIP signature (the verdict-clearing test) |
|---|---|---|---|---|
| N1 | snap threshold `ρ̄_cav` | `−1/φ` (candidate) | the density at which a cell snaps | pocket-count / persistence tracks the threshold |
| N2 | `Δ_heal` re-entry width (tally pay-back) | `0.0` | the over-pressure a snapped cell needs to un-snap | hysteresis tracks `Δ_heal` (built-in irreversibility) |
| N3 | `χ_shock` latent-tally fraction | `1.0` (physical); `0` = elastic control | fraction of crossing-KE tallied (the snap model) | FLASH/persistence exists only at large χ and scales with it (no plateau) |
| N4 | D6 burst-detection threshold | calibrated on known case (F0d) | the bar a longitudinal burst must clear | burst-count tracks the threshold |
| N5 | snap interface stencil | sharp (1 cell) | how the boundary-class BC is applied | reflectivity / collimation tracks stencil width |
| N6 | detector top-K | calibrated (F0a) | how many density-peak cells are sampled | pocket/winding read tracks K |
| D1 | `lock_eta` (rigid-rotation lock; κ_L=6/5 BEMF) | `0.05`–`0.08` | the rate the global `L_ω` is contracted | **T3 spin-lock value tracks η** (graft-v4: the RATIO should be η-invariant; if the locked VALUE tracks η, CLIP) |
| K1 | `ν_art` artificial viscosity | engine default `5e-4` | the dissipation that drains the lock | **the D8 attribution knob** — P1 heal-rate ∝ `ν_art` ⇒ prior LOCK verdict was apparatus (swept, regressed §3) |
| K2 | `N` grid resolution | held FIXED per run (≈64–72; §8 cost) | pocket / winding / collimation resolution | any signature tracks `N` (the under-resolved single-cell pocket) |
| K3 | `n_steps` / recording window | held FIXED per run | when the run STOPS | **T1 `H_total` "converged" value tracks stop-time** (the graft-v4 stop-time-dependent-trapped lesson — F0e canary) |
| K4 | seed `frac` (saturation depth) | swept `{0.30,0.60,0.85,0.95}` (genesis-24) | the seed's standing-V amplitude | a positive seen ONLY at shallow frac = sub-saturation wrong-regime artifact |
| K5 | `pml_thickness` | engine default | the F0a interior-exclusion band | a "persistent pocket" inside the PML band (F0a) |

**Verdict-clearing rule (HARD CONSTRAINT, ORDER per the directive):** STEP 5 sweeps N1–N6/D1/K1–K5 BEFORE any §4 verdict. A §4 positive that TRACKS any knob is CLIP, named by the knob. A signature ROBUST across the sweep (plateauing; present for all `χ_shock>0`; heal-rate→nonzero as `ν_art→0`) is provisionally physics. The parallel runner (§8) makes this sweep matrix affordable.

---

## 6. ave-prereg Step-3.5 — DIMENSIONAL SUBSECTION (canonical primitives only; arithmetic shown)

**Canonical / candidate primitives (cited verbatim, verified this session):**

| primitive | value | source |
|---|---|---|
| `PHI` | `(1+√5)/2 = 1.6180339887` | `constants.py:199` |
| `ρ̄_cav` (candidate) | `−1/φ = −0.6180339887` | EOS root of `04_superluminal_transit.tex:86`; root-check `1+ρ̄/(1−ρ̄²)=2.2e-16` |
| `ρ_floor = 1+ρ̄_cav` | `0.3819660113` | natural units `ρ₀=1` |
| `κ̃` (coupling) | `pq/(p+q)=6/5=1.2` (α-FREE) | `crystal_graft_v4.py:27` |
| `ν_vac` (c-speed) | `2/7` | `crystal_graft_v4.py:62` |
| `V_yield` | `≡1` (engine natural unit) | `crystal_graft_v4.py:62` |
| `lock_eta` (κ_L=6/5 BEMF) | `0.05`–`0.08` | `crystal_graft_v4.py:85` |

**(1) Snap latent release (the D6 FLASH magnitude).** Vapor pressure at the floor (exact EOS `p(ρ̄)=c₀²[ρ̄−½ln(1−ρ̄²)]`, `cavitation_flow.py:165`): `p(ρ̄_cav)=c₀²[−0.618−½ln(0.382)]=c₀²[−0.618+0.481·... ]`. Evaluated: `½ln(1−ρ̄²)=½ln(0.6180)=−0.2404`, so `p(ρ̄_cav)=c₀²[−0.618+0.240]=−0.3774·c₀²` (TENSION — consistent with a tensile-failure void, sign-correct). The EOS softening slope at the floor `d(c²)/dρ̄|_cav=c₀²(1+ρ̄²)/(1−ρ̄²)²=c₀²(1.382)/(0.382²)=c₀²(1.382)/(0.1459)=9.47·c₀²` (a definite, EOS-fixed approach slope — the snap is sharp, not soft). **Expected `E_latent` per snapped cell ≈ |p(ρ̄_cav)|·(cell volume) ~ O(0.38·c₀²)·dV — resolvable** (not a rounding artifact) against the free-run ledger.

**(2) Crossing KE (the snap-onset budget).** Transonic core `|u|~M·c₀`, `M~0.8` (the inherited reach result), void density `ρ_floor=0.382`: `½ρ|u|²=½·0.382·(0.8)²·c₀²=½·0.382·0.64·c₀²=0.122·c₀²` per unit volume. Over a pocket of a few % of the domain, `E_diss~O(10⁻³)·c₀²·L³` per snap episode — **same order as the predecessor's total PE (~0.016), so the snap latent is a RESOLVABLE fraction of the ledger.**

**(3) T1 mass — the convergence target (power-counting).** The trapped dilatation added-mass `H_total ~ κ̃·∫g·V·(w·∇×ω)` — the graft-v4 trapped `H_bel` was `O(−6)` at input `−291` (a ~2% trap). The CONVERGENCE check is dimensionless: `dH_total/dt → 0` within the F0e drift-floor over the LAST half of the window (the still-rising `t^2.2` graft-v4 failure is the falsifier). **Expected magnitude is NOT pre-committed (it is the emergence target); the FALSIFIER is "still rising at run-end" (stop-time-dependent), frozen.**

**(4) T3 spin — the half-pole-pair value (DERIVED, not assumed; power-counting form).** Locked `L_ω=∫r×π_ω` (engine units). The (2,3) winding has `p=2` toroidal, `q=3` poloidal pole-count. "Half-pole-pair" = `½` the circulation quantum of ONE pole-pair: `L_target = ½·(ρ_floor·R_ring²·Ω_lock)` where `R_ring` is the MEASURED ring radius (F0a top-K) and `Ω_lock` the measured locked angular frequency. The engine-unit→`ℏ/2` conversion is `L_ω(engine)/L_quantum` evaluated at run time from the winding normalization — **the prereg freezes the FORM `L_target ∝ ½·ρ·R²·Ω` and the requirement that the measured `L_ω/L_quantum → ½` WITHOUT dialing `lock_eta` (D1 must be η-invariant); it does NOT pre-commit the engine-unit number** (representation-capability: assuming the number would beg the question).

**(5) T6 de Broglie — the scaling-law (explicit power-counting).** The bulk pilot wave is the reactive `mₑc²·α` sloshing fraction (§11.3.4). Standard dispersion: `λ_dB = h/p ∝ 1/p`. Power-counting in the BULK channel (coordinate-matched): translate the locked state at momenta `p₁,p₂`; the prereg freezes `λ(p₁)/λ(p₂) = p₂/p₁` within the fit-floor as the POSITIVE, and `λ ≠ const/p` as the falsifier. The magnitude (Compton-scale) is SET by the assembled `T1` mass — not independently pre-committed; only the EXPONENT (`−1`) is frozen by power-counting.

**Sanity-check against the canonical anchor:** the seed operating point `frac∈{0.30..0.95}` brackets the genesis-24 deep-saturation band (`A²_V=frac²`, `0.85–0.95`=deep); the candidate floor `ρ̄_cav=−0.618` sits BELOW the seed's intermediate Smith-Γ but is reachable by the centrifugal deficit at `M~0.8` (the inherited reach). The dimensionless `M~0.8` is the canonical empirical anchor (cavitation-probe reach); the design's snap is dimensionally consistent with it. No scaling-law magnitude is committed outside this anchored range.

---

## 7. REGIME / PHASE-STATE + CONSERVED-VS-PUMPED (ave-regime-phase-state-check)

- **MODE:** the COUPLED channel — BULK-K (the seed-V + the snap, longitudinal) ⊗ Cosserat transverse ω (the winding) ⊗ shear w (the photon director). The D6 FLASH detector reads the BULK channel; the T2 charge reads the phase-space `(V_inc,V_ref)` channel. Each observable in its own MODE.
- **REGIME:** near-yield → through-floor (the RUPTURED branch — the snap CAN exist here by construction, NOT a wrong-regime artifact). The seed-V channel is near-yield (deep `A²_V`); the C-no-seed control is the regime-gated null (no seed ⇒ the longitudinal source cannot fire ⇒ HEAL, the genesis-23 `V≡0` rediscovery).
- **PHASE-STATE:** seed (off-center Smith-Γ) → drive → snap (`ρ̄≤ρ̄_cav`, Γ→−1 rim) → (SNAP-LOCKED: persists P2 / MOTION-LOCKED: persists P1-no-snap, heals P2 / NEITHER: heals both).
- **ave-conserved-vs-pumped (HARD CONSTRAINT — energize+lock, never pump):** the seed's standing V is ENERGIZED+LOCKED once (the genesis-24 trap machinery; never a CW free-work pump — that is the Class-C detonation `|V_inc|~t`, the reactive-entrainment artifact). The circulation Γ / integer winding is energized once by the drive then topological (cannot unwind continuously). KE↔PE slosh at fixed Γ; `E_diss`/radiation/the snap-tally are the only sinks. The BEMF (κ_L=6/5) is the lock's INERTIA — it appears only against CHANGES (D8: at steady circulation nothing is paid). A run whose Γ or `H` drifts secularly in the quiet phase is a PUMP (FLAGGED, F0e), not a lock.

---

## 8. SCALE / BUDGET (from the speedup report, verified live this session — verify-before-cite, not trusting quoted numbers)

**Two pre-existing accelerators (both v4 lineage, both verified live):**
1. **`fast_winding_extractor.py`** (`src/ave/utils/fast_winding_extractor.py`) — vectorized `(2,3)` winding MEASUREMENT instrument. Measured **25.8×** (~59.6 ms/call → 2.31 ms/call). Bit-exact equivalence gate PASSES (`max|Δ|=0.00e+00` vs the driver's `extract_2_3_omega` on planted/null/random fields). **float64 mandatory** (an f32 path misses the 1e-12 gate and desyncs the ledger). Accelerates the T2/charge checkpoints.
2. **`genesis_parallel_runner.py`** (`src/ave/utils/genesis_parallel_runner.py`) — ProcessPool harness fanning the arm/bin sweep matrix across cores. Measured **5.0×** at 6 workers/6 runs (sub-linear: spawn/serialize + memory-bandwidth-bound FDTD). Determinism CONFIRMED `serial==parallel True` (per-spec integer seed re-applied in each worker). Default workers = `cpu_count−2 = 12` (14-core box). **This is the real budget multiplier for the §3 matrix** (`{arm}×{handedness}×{P1,P2}×{apparatus-knob}`) — it parallelizes ACROSS independent runs, not within one.

**Three easy wins applied (committed separately on this branch; bit-identical re-verified this session, `max|Δ|=0` on all 8 configs):** `6f40fa2b` cache PML interior_mask; `a409848c` vectorize per-component vector Laplacian; `175033ba` preallocate curl output. NO algorithmic physics change.

**Single-core step-loop factors (accelerated HEAD vs pre-win baseline `50910d77`, fixed seed, N=64):** `CrystalGraftV4` 30.0→**26.8 ms/step** (1.12×); `CrystalEngine` 8.97→7.64 (1.17×); 2D flow ~1.00× (already-optimal `np.roll`). Modest because the engine is memory-bandwidth-bound and already mostly vectorized.

**Cost / memory scaling (explicit FDTD, ~N³):** `~9.4e-8·N³ s/step` — N=48 10.4 / N=64 24.3 / N=80 47.4 / N=96 85.7 ms/step; memory N=64 46 MB / N=96 157 MB / N=128 371 MB per engine. **v5 runs hold N FIXED (≈64–72)** per the cost/memory budget; the matrix breadth comes from the parallel runner, not from per-run size.

**EXCLUDED (recorded for honesty):** f32 dtype reduction — **physically forbidden** (conservation canaries operate at 1e-3, the winding gate needs 1e-12; f32 desyncs the ledger). `np.roll→slicing` — REJECTED (microbenchmarked NEGATIVE on numpy 2.4.3).

---

## 9. FREE PARAMETERS

The physics inputs are: the swept **drive** (FOC d/q amplitude + helicity, energizes Γ once) and the swept seed **frac** (saturation depth, engineering-choice, swept not tuned — genesis-24). `c₀`, the EOS, `ρ̄_cav` (candidate), `κ̃=6/5`, `ν_vac=2/7`, `V_yield≡1` are canonical/candidate-derived. `χ_shock` is the one snap-model coefficient (swept; `χ=1` physical, `χ=0` the elastic control). `lock_eta`, `ν_art`, N1–N6/K-knobs are apparatus (swept §5). **No coefficient is tuned to produce a verdict; no threshold is set to manufacture a positive.**

---

## 10. CORPUS ANCHORS (verify-before-cite, all confirmed 2026-06-10)

- **Engine lineage:** `src/ave/core/crystal_graft_v4.py` (V4←V3←V2←CrystalEngine); `H_couple=κ̃∫g_wall·V·[w·(∇×ω)]`, `κ̃=pq/(p+q)=6/5` α-free (`:27`); lock `π_ω←π_ω−η(Ω×r)` (`:50`). Verified.
- **Predecessors (Rule 12 lineage §0.1):** sonic-horizon `analysis/2026-06-10-sonic-horizon-closure @ a73bba93` (LOCK=reversible spring; SELECTIVE-weak); genesis-24 `@ df1c3f78` PR #153 (Lane-1 seed; B-localizes); graft-v4 (C→LOCK-FAIL; photon = non-depleting director); cavitation-core probe (CLIP). Verified.
- **Candidate EOS root:** `AVE-Propulsion/.../04_superluminal_transit.tex:86` (`c_eff²=c₀²(1+ρ̄/(1−ρ̄²))`, "not a free parameter"); root `ρ̄_cav=−1/φ` (`PHI` `constants.py:199`). Verified numerically this session.
- **Exact-EOS bulk ledger (D6):** `src/ave/core/cavitation_flow.py:165–166` (`p(ρ̄)=ρ₀c₀²[ρ̄−½ln(1−ρ̄²)]`). Verified.
- **Lane-1 standing V_inc (D2 seed):** `research/2026-06-09_genesis-24-saturated-seed_prereg.md:7` (on origin/main + PR #153) — "A saturated mass carries a standing longitudinal V_inc — the '3' is the real Heaviside/Gibbs-excised scalar grade." Verified.
- **Channel ledger / order-parameter (D2/D6 framing, CROSS-BRANCH / UNMERGED):** `research/2026-06-10_matter-as-vapor-locked-pump_framing.md` §11.1 L3 / §11.2 / §11.5, on `analysis/2026-06-10-vaporlock-framing-and-tracker @ 43bbc78a` — NOT in the v5 tree; cited as a cross-branch hypothesis/framing-class input (§0.3 FLAG). The §11.5 v5-build gate-flag is recorded verbatim for auditor adjudication.
- **Extractor resolution floor (F0b):** the graft-v4 `r_meas ≥ 3 cells` (`2026-06-10_graft-v4-photon-helicity_prereg.md:92`). Verified.
- **Two-"3"s (T1 vs T2 distinctness):** `manuscript/ave-kb/.../master-equation.md:18` (the auditor flag: dilatation MASS vs Cosserat WINDING conflated). Recorded for the T1/T2 separation.
- **Accelerators:** `src/ave/utils/fast_winding_extractor.py`, `src/ave/utils/genesis_parallel_runner.py`. Verified live (§8).

**Corpus state:** OPEN. The reach/crossing is established (cavitation-probe, clip-invariant). The kind of lock (SNAP vs MOTION, D8), the spec-sheet electron-class verdict (D7), and the twin/handedness (D4) are unrun. This prereg freezes the bins/arms/floors BEFORE any run artifact (committed alone, git-provable).
