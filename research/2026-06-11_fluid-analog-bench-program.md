# Fluid-Analog Bench Program — real tabletop fluid experiments mapped to live AVE arcs

**Date:** 2026-06-11
**Status:** **DRAFT-FOR-GRANT-AND-KEITH** — DOC-ONLY (no hardware, no execution, no corpus mutation). Review-gated; nothing freezes until Grant + Keith schedule bench time and ratify the class-tags.
**Author lane:** implementer (research-doc scaffold). The auditor lane reviews; Grant + Keith adjudicate the physics framing.
**Disciplines applied:** `verify-before-cite` (every corpus anchor grep-verified this session — ledger §9), `consistency-vs-emergence` (class-tag binding — every experiment is CONSISTENCY-CLASS), `pre-test-physics-check`, `substrate-native-check` (CP10 boundary-not-bulk reading carried into each falsifiable surface), `phase-space-coordinate-check` (frozen observables stated in the coordinates the corpus claim lives in), `flag-don't-fix`, `ave-apparatus-floor-attribution` (the shared-DAQ validation ladder, §8).

---

## §0 — The governing law of this program (read first)

**Every experiment below is CONSISTENCY-CLASS. None of them tests the vacuum.**

Each AVE arc *borrows* a mechanism class from classical continuum fluid dynamics — vortex reconnection, drive-biased symmetry breaking, pilot-wave guidance, rotation-collimation, vapor-lock hysteresis, inertial-collapse saturation, transcritical analog horizons. These are all **published classical physics**. The bench tests **whether the borrowed mechanism class actually behaves the way the corpus assumes it does** — nothing more.

A positive result **constrains the analogy** (the borrowed mechanism is real and behaves as relied upon). A positive result **never confirms AVE**: water is not the vacuum, the Navier-Stokes continuum is not the K4 + Cosserat substrate, and a surface-gravity wave is not a longitudinal V-sector pressure. Per `consistency-vs-emergence`, no entry here may be headlined as a manifestation- or emergence-class result. The tag is **identity-of-the-borrowed-class**, tested in water.

Two sentences are mandatory in every entry and are stated explicitly: **"what a positive means"** and **"what it does NOT mean."** If those two cannot be cleanly separated for an experiment, the experiment is not ready to run.

---

## §1 — VORTEX-RING COLLISIONS (Keith's domain) — RANK 1

**Bench setup.** Water tank (≥ 0.5 m cube, optical-grade side wall). Two piston-cylinder "ring guns" (solenoid- or pneumatic-driven, synchronized to a common trigger) fire dyed vortex rings. **Arm A (annihilation analog):** the two guns face each other head-on and are configured to launch **opposite-circulation** rings (counter-rotating about their common axis). **Arm B (leapfrog control):** co-axial, **same-handed** rings launched in sequence so the trailing ring threads and overtakes the leader (the classic leapfrog). Dye + high-speed camera + stroboscopic backlight; PIV optional.
**Materials class:** off-the-shelf tank, two ring generators, food-dye/fluorescein, high-speed camera. **Difficulty:** moderate — the hard part is firing-synchronization and matched circulation/Reynolds number between the two guns.

**AVE arc it maps to.** The annihilation-evaporation arc — live branch `analysis/2026-06-11-annihilation-evaporation` (in-flight, **not yet merged to corpus**; cited as a live arc, not a corpus leaf). Its standing corpus footings: **Kelvin pair-shedding / collapse→confinement** at [`the-abandoned-interior.md:50`](../manuscript/ave-kb/common/the-abandoned-interior.md) ("the moving-`Γ=−1`-boundary converts collapse→confinement … Kelvin resumed is a hypothesis with a working confinement step and an open self-assembly step"; class CONSISTENCY-CLASS over a HYPOTHESIS-CLASS object), and the **twin-pocket prediction** at [`2026-06-10_novel-objects-report.md:110`](2026-06-10_novel-objects-report.md) — **N8, the geometric twin-pocket RH/LH split**, registered candidate-physics and flagged **"explicitly not a chiral observable"** (`:117`).

**The falsifiable surface (what would CONTRADICT the mechanism class).** The class the corpus borrows is: *two opposite-orientation topological structures meeting head-on shed their circulation into small-scale daughter structures and reconnect (the annihilation analog), while same-orientation structures leapfrog without reconnection (the control).* Two ways a fluid result CONTRADICTS it:
- **(C1)** opposite-handed head-on and same-handed leapfrog produce **statistically identical** daughter-ring spectra and reconnection behavior → relative orientation is *not* the discriminating variable, and the borrowed "annihilation = orientation-selective reconnection cascade" class fails.
- **(C2)** the daughter spectrum shows a **chiral** signature (changes under a global mirror reflection of the apparatus) → this would CONTRADICT N8's own `:117` tag that the twin-pocket split is *geometric, not chiral*. Instructive either way and a clean flag to Grant.

**5-line prereg skeleton.**
1. **Frozen observable:** `N_daughter` (count of secondary rings shed) and `n_azi` (azimuthal wavenumber of the reconnection instability), measured as a function of relative handedness {opposite, same} at matched `Re` and matched ring spacing.
2. **Bin CONSISTENT:** opposite-handed head-on yields `N_daughter` and visible reconnection **exceeding** the same-handed leapfrog control beyond a pre-set threshold.
3. **Bin CONTRADICT (C1):** no statistically-significant {opposite vs same} difference at fixed `Re`.
4. **Bin FLAG (C2):** daughter spectrum differs under global mirror → chiral signature where the corpus expects none.
5. **Stop rule:** N ≥ 10 firings/arm at ≥ 3 `Re`; freeze bins before the first dyed run.

**What a positive (Bin CONSISTENT) means.** The continuum-fluid mechanism class is real: opposite-orientation head-on topological collisions reconnect and shed daughter structure where like-orientation leapfrog does not. The borrowed reconnection-cascade picture behind the annihilation analog is physically instantiated in a real fluid.
**What it does NOT mean.** It does **not** show vacuum pair-annihilation proceeds by vortex reconnection; does **not** confirm the twin-pocket prediction *in the vacuum* (N8 is candidate-physics, and explicitly geometric-not-chiral — water rings cannot test the vacuum's chirality book-keeping); does **not** confirm the (2,3) self-assembly (still an open step per `the-abandoned-interior.md:50`); does **not** validate the live annihilation-evaporation branch. Water rings are a borrowed mechanism-class analog; the vacuum object is K4 + Cosserat, untouched here.

## §2 — KONDEPUDI STIRRED CRYSTALLIZATION — RANK 2

**Bench setup.** Saturated aqueous sodium chlorate (NaClO₃) solution — achiral in solution, optically active (L or D) in crystal form. Crystallize by slow evaporation/cooling. **Arm A:** vigorously stirred (magnetic stir bar, fixed rpm). **Arm B:** unstirred control. Harvest the crystals and count L vs D under **crossed polarizers** (each crystal rotates the plane of polarization one way or the other; a polarimeter or rotating analyzer gives the sign).
**Materials class:** NaClO₃ reagent, beaker, stir plate, crossed-polarizer rig / polarimeter. **Difficulty:** low-to-moderate — this is the most accessible experiment in the program; the canonical result is undergraduate-reproducible.

**Literature class.** Kondepudi, Kaufman & Singh 1990 (*Science*), "Chiral Symmetry Breaking in Sodium Chlorate Crystallization": **stirred** → near-total single-handedness per batch (autocatalytic secondary nucleation amplifies the first crystal's handedness); **unstirred** → ~50/50 Bernoulli statistics across batches.

**AVE arc it maps to.** The rotation-at-freeze handedness mechanism class:
- **Ω̂_freeze canon** — [`trampoline-framework.md:97-105`](../manuscript/ave-kb/common/trampoline-framework.md): "During lattice formation … the crystallizing region is rotating with angular velocity `Ω_freeze`. … At the moment of crystallization, bond rest lengths lock at the rotating-frame equilibrium value … **Direction of `Ω_freeze` → direction of bowing → right-handed chirality** … Mirror-image freeze-in gives left-handed universe with identical magnitude `|u_0|`."
- **The driven-vs-stochastic falsifier** — archive doc 59 [`59_memristive_yield_crossing_derivation.md`](_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md), §5.3 (`:252-267`): **"Driven origin (external source imposes handedness) … Single-handedness fills the driven region deterministically"** vs **"Stochastic origin (thermal cooling, no external drive)"** → domain walls / 50-50; the experimental implication is spelled out at `:394` (vary cooling rate; measure topological-defect vs chirality-domain-wall density).

**The falsifiable surface.** The class is: *a single coherent drive applied during the freeze biases handedness toward a single domain; an undriven freeze gives stochastic 50/50 with domain walls.* A fluid result CONTRADICTS it if **stirred NaClO₃ gives the same 50/50 batch statistics as unstirred** (the drive does not bias handedness), or if **unstirred gives single-handedness** (global bias with no drive).
**Load-bearing honest subtlety (flag-don't-fix).** Kondepudi stirring breaks symmetry by autocatalytic **secondary nucleation** — it produces a single domain per batch but the **sign is still random** batch-to-batch; stir *direction* (CW vs CCW) does **not** select which handedness wins in the canonical result. The corpus Ω_freeze claim is *stronger*: `trampoline-framework.md:105` says rotation **direction** sets the handedness **sign** (right-hand rule on centrifugal × bond-axis). So Kondepudi is a clean test of *single-domain-ness* but is **sign-blind**, and the gap between "drive → single domain" (testable here) and "drive direction → sign" (NOT tested by canonical Kondepudi) is exactly the distinction to surface to Grant. **This gap is the discriminator, not a footnote.**

**5-line prereg skeleton.**
1. **Frozen observable:** enantiomeric excess `ee = (N_L − N_D)/(N_L + N_D)` per batch, and its batch-to-batch distribution, for {stirred-CW, stirred-CCW, unstirred} at matched supersaturation + cooling rate.
2. **Bin CONSISTENT (single-domain):** stirred `|ee| → ~1` per batch, **sign random** across batches.
3. **Bin STRONGER (direction-sets-sign):** stirred `ee` **sign correlates** with stir direction → would speak to the Ω_freeze right-hand-rule claim (NOT expected from canonical Kondepudi).
4. **Bin CONTRADICT:** stirred `ee` distribution = unstirred 50/50.
5. **Stop rule:** N ≥ 20 batches/arm; freeze bins before counting.

**What a positive (Bin CONSISTENT) means.** A coherent macroscopic drive during freeze converts stochastic handedness into single-domain handedness — the corpus's "freeze-while-spinning gives a single-handed region" has a real tabletop instance of the mechanism class.
**What it does NOT mean.** Bin CONSISTENT does **not** confirm that rotation *direction sets the sign* (the stronger Ω_freeze claim — only the rarely-seen Bin STRONGER would, and canonical Kondepudi is sign-blind); does **not** test the vacuum K4 freeze; does **not** confirm the `u_0 = ρΩ²r²/2K_0` derivation. Honest carry: NaClO₃ secondary-nucleation autocatalysis is a *different microscopic mechanism* from centrifugal bond-stretch — same mechanism **class** (drive → single domain), different mechanism.

## §3 — WALKING DROPLETS (Couder-Fort) — RANK 3

**Bench setup.** A bath of silicone oil vibrated vertically just **below** the Faraday instability threshold. A millimetric droplet bounces on the surface and self-propels, guided by the standing-wave field it itself creates each bounce — a hydrodynamic pilot-wave "walker."
**Materials class:** silicone oil, electromagnetic shaker, function generator + amplifier, precision accelerometer, high-speed camera, stroboscope. **Difficulty:** **HIGH** — sub-Faraday acceleration must be held flat to ~1%; this is the hardest rig in the program to make quantitatively clean.

**Literature class (CARRY THE DISPUTE HONESTLY).** Couder & Fort, ~2005 onward — walking droplets as a macroscopic pilot-wave analog; robustly reproduce **orbital quantization, Zeeman-like level splitting, and tunneling statistics** in several geometries. **BUT** the celebrated Couder-Fort 2006 single-particle **double-slit diffraction/interference** claim has **FAILED independent replication**: careful re-runs (Andersen et al. 2015; Pucci, Harris, Bush, and the Bohr/Andersen group) found **no** robust QM-matching interference for single walkers passing slits — the original apparent "diffraction" is attributed to boundary/systematic effects. **The double-slit statistics claim specifically is contested.** This program does not treat it as established.

**AVE arc it maps to.** The **pilot-mode fork** and the **moving-defect double-slit** arc:
- **Pilot-mode fork (Grant-gated, OPEN)** — [`2026-06-10_pilotwake-bhphase-survey_note.md`](2026-06-10_pilotwake-bhphase-survey_note.md) §2: the corpus disagrees with itself about which sector the pilot's wake lives in — **transverse-inductive** ([`ohmic-decoherence-born.md:11`](../manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md)) vs **longitudinal-bulk** ([`de-broglie-standing-wave.md:50`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)). Surfaced verbatim, adjudication pending Grant.
- **The discriminating sim was NEVER run** — same note §3: no extant sim isolates a *dynamically moving defect that simultaneously carries a near-field store AND radiates a far-field wake*; named there as **not-yet-run**.
- **The double-slit EE mapping** — [`double-slit-ee-mapping.md`](../manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md) §5: the AVE discriminating content is a **continuous** visibility curve `V(Z_det)` (Ohmic-tap decoherence) where Copenhagen predicts a binary step.

**The falsifiable surface (double-edged, and that is the point).** The class is: *a localized excitation co-moving with a real physical guiding-wave field reproduces interference statistics.* The honest surface has two edges:
- **(i)** for the class to support the AVE pilot picture, a walker must build up multi-fringe interference statistics from its pilot field; **but**
- **(ii)** the replication dispute means the most-cited positive (slit statistics) does **not** robustly reproduce. A clean re-run that **again** fails slit-statistics is the **expected, honest** outcome — and it is **instructive for sim design**: it warns that a classical pilot-wave does **not** generically yield QM slit-statistics, so the AVE moving-defect sim must *earn* its `V(Z_det)` signature, not assume interference falls out of a guiding field for free.

**5-line prereg skeleton.**
1. **Frozen observable:** transverse landing-position distribution `P(x)` for walkers passing a single aperture and a double aperture, accumulated over N ≥ 500 passes; compared against the QM Fraunhofer pattern AND the corpus continuous-decoherence prediction.
2. **Bin (i) CONSISTENT-with-pilot:** `P(x)` shows statistically-significant multi-fringe structure tracking QM (note: replication risk — pre-commit the systematic-controls list).
3. **Bin (ii) EXPECTED-NULL:** `P(x)` single-lobe / no robust fringes — matches the contested re-runs; *constrains* the AVE sim (classical pilot ≠ QM statistics for free).
4. **Bin (iii) NEW DISCRIMINATOR:** fringe visibility varies **continuously** with a controllable boundary/damping analog → matches the AVE `V(Z_det)` continuous-decoherence prediction.
5. **Stop rule:** freeze the systematic-controls list (boundary reflections, air currents, bath-depth gradient) **before** the first run; N ≥ 500/configuration.

**What a positive (Bin iii) means.** A hydrodynamic pilot wave can exhibit *continuously-tunable* decoherence — supporting the mechanism class behind the AVE continuous-`V(Z_det)` prediction (the discriminating content vs Copenhagen's binary collapse).
**What it does NOT mean.** Does **not** resolve the pilot-mode fork (water is single-sector — it cannot tell transverse-inductive from longitudinal-bulk); does **not** confirm the vacuum is a pilot-wave medium; does **not** validate the contested Couder-Fort double-slit claim (carried as **DISPUTED**). The deepest value here is **methodological**: it disciplines the moving-defect sim to not assume QM statistics emerge automatically from a classical guiding field — the dispute itself is the lesson.

## §4 — TAYLOR COLUMNS — RANK 4

**Bench setup.** A tank of water on a turntable spun up to solid-body rotation. Place a small obstacle on the bottom (or tow one slowly across the floor). At low Rossby number the dye reveals a **Taylor-Proudman column** — a stagnant fluid column above the obstacle that translates *rigidly with it*, the flow self-organizing into two-dimensional columns aligned with the rotation axis even with no physical wall confining them.
**Materials class:** turntable / rotating platform, cylindrical tank, dye, small obstacle. **Difficulty:** moderate — requires steady solid-body rotation and genuinely low Rossby number; spin-up transients must be allowed to decay.

**Literature class.** Taylor-Proudman theorem; G.I. Taylor's 1920s rotating-tank column experiments. Geostrophic, columnar, quasi-2D self-organization at low Rossby number.

**AVE arc it maps to.** The **rotation-axis collimation / self-organization** mechanism class:
- **Polar-impedance jet collimation** — [`first-principles-predictions.md:16-29`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/first-principles-predictions.md): "the rotation axis is the only direction where the azimuthal Op14 topological strain gradient (`ε_{11,rot}=0`) vanishes … the polar axis is the 'least strained' escape channel … The predicted jet opening angle scales with `a_*`." Engine `black_hole_jets.py`.
- **Ω_freeze imposed-rotation genesis** — [`trampoline-framework.md:97-105`](../manuscript/ave-kb/common/trampoline-framework.md) (the rotation imposed at freeze, §2 above).
- **⚠ VERIFICATION FLAG (flag-don't-fix):** the parent framing for this entry — *"the collimation sequence (D3) self-organization the imposed-rotation sim couldn't test"* — **did NOT verify as a named corpus arc.** A whole-repo grep finds no leaf/research-doc "D3 collimation sequence" and no "imposed-rotation sim" documented as having a self-organized-collimation gap; the `D3` row in `divergence-test-substrate-map.md:462` is **D3-GEOM-ENTROPY** (geometric entropy — *unrelated*). This entry therefore stands on the **verified** polar-impedance-collimation anchor (`first-principles-predictions.md:16-29`) + Ω_freeze; the "D3/imposed-rotation-sim-gap" label is carried as **parent-framing, UNVERIFIED**, and surfaced for Grant to either point at the real arc or strike the label. See ledger §9.

**The falsifiable surface.** The class is: *imposed rotation forces flow to self-organize into structures collimated along the rotation axis (columns/jets) without an explicit guiding wall.* A fluid result CONTRADICTS it if, at low Rossby number, the flow does **not** form rotation-axis-aligned columns, or if column coherence-length is **independent** of rotation rate. (Taylor-Proudman is textbook-robust, so a flat contradiction would be surprising — the real value is **quantitative**: does column coherence-length scale with `Ω` the way the corpus jet-opening-vs-`a_*` analog implies?)

**5-line prereg skeleton.**
1. **Frozen observable:** axial coherence length `L_col` of the columnar structure above the obstacle, and whether the column translates *rigidly* with the obstacle, as a function of Rossby number `Ro = U/(2ΩL)`.
2. **Bin CONSISTENT:** `L_col` grows as `Ro → 0` and the column moves rigidly with the obstacle.
3. **Bin CONTRADICT:** no column forms, or `L_col` independent of `Ω`.
4. **Bin QUANTITATIVE:** record `L_col(Ω)` scaling exponent; compare to the corpus jet-opening-angle-vs-`a_*` analog.
5. **Stop rule:** ≥ 4 `Ro` values spanning the geostrophic regime; allow spin-up transient to decay before each run.

**What a positive means.** Imposed rotation self-organizes flow into axis-aligned collimated structure — the borrowed picture behind the corpus's rotation-collimates-the-jet prediction is real and quantifiable in a continuum fluid.
**What it does NOT mean.** Does **not** confirm that BH jets collimate by polar-impedance matching (Taylor-Proudman is incompressible-geostrophic; the corpus mechanism is saturation-impedance — same **class**, different mechanism); does **not** confirm the Ω_freeze genesis; does **not** test the vacuum. And it does **not** retroactively validate the unverified "D3/imposed-rotation-sim" label — that remains a flag for Grant.

## §5 — PUMP-LOOP VAPOR LOCK — RANK 5

**Bench setup.** A **closed** fluid loop (tubing) with a circulation pump and a localized heater. Raise heater power until the working fluid boils locally and the vapor pocket blocks flow (vapor lock). Record the **snap** (flow-stall onset), the **latent plateau**, and the **refill hysteresis** — does flow resume at the same heater power it stalled, or only at a lower power (a hysteresis loop in the `Q`-`ṁ` plane)?
**Materials class:** circulation pump, tubing, cartridge heater, flow meter, thermocouples; working fluid (water, or a low-boiling-point fluid for accessible powers). **Difficulty:** moderate — this is *closed-loop plumbing*, squarely the electron-plumber's home turf.

**Literature class.** Vapor lock / two-phase flow-boiling instability: the **Ledinegg instability** and **density-wave oscillations** in heated channels; classical boiling/cavitation hysteresis. Canonical thermal-hydraulics, pure physics.

**AVE arc it maps to.** The snap/latent/refill hysteresis = the **rim-PE barrier class**:
- **The LOCK-is-mass-conservation mechanism** — [`2026-06-10_sonic-horizon-closure_result.md:202`](2026-06-10_sonic-horizon-closure_result.md) & `:232`: *"the LOCK mechanism is mass-conservation: the rim over-pressure (a PE reservoir) refills the void; the horizon dissipates KE but does not vent the rim PE. … A genuine vapor-LOCK would require the rim mass to LEAVE the system (radiate away) or a hardened `Γ=−1`-type topological wall that forbids refill."* The closure verdict was **LOCK = reversible spring**.
- **FLASH-vs-LOCK undecided** — [`2026-06-10_cavitation-core-probe_result.md:173`](2026-06-10_cavitation-core-probe_result.md): the crossing is *smooth and reversible*; the irreversibility "is NOT in the candidate EOS and must come from a separate, named, dynamical mechanism."
- **The vapor-locked-pump framing (hypothesis-class)** — [`2026-06-10_matter-as-vapor-locked-pump_framing.md`](2026-06-10_matter-as-vapor-locked-pump_framing.md): "the FLASH detector = a longitudinal-burst detector" (`:278`); the rim-PE reservoir is **bulk** (`:267`).

**The falsifiable surface.** The class is: *a tensile/boiling pocket in a bounded pumped loop is either a REVERSIBLE spring (rim PE refills the void when drive is removed) or an IRREVERSIBLE lock (needs the pocket mass to leave, or a hard wall to freeze it).* The corpus claim is that **in a mass-conserving system the pocket is reversible** (rim PE refills it). The **sharp** contradiction: a sealed loop **conserves mass**, so per the corpus a vapor lock there *should* heal. If a simple heated closed loop shows **irreversible** hysteresis (stalls at power `P_up`, resumes only at `P_down ≪ P_up`) **with no mass leaving and no hard geometric trap**, that CONTRADICTS the corpus "mass-conservation refills the void" mechanism — the rim mass is still in the loop, yet the lock does not heal.

**5-line prereg skeleton.**
1. **Frozen observable:** the hysteresis area in the (heater power `Q`, mass-flow `ṁ`) plane — specifically `P_up` (stall onset) and `P_down` (resume on cool-down), and whether the latent plateau shows a discontinuous step.
2. **Bin REVERSIBLE:** `P_down = P_up`, smooth refill → CONSISTENT with the corpus rim-PE-refill / sonic-horizon LOCK verdict.
3. **Bin CONTRADICT:** `P_down < P_up`, finite hysteresis loop in a *sealed* loop → flags that rim-PE-refill is not the whole story even with mass conserved.
4. **Bin FLASH-PROBE:** a discontinuous latent step at stall → probes the FLASH-vs-LOCK distinction the cavitation-core probe left undecided.
5. **Stop rule:** sweep `Q` up and down ≥ 5 cycles; verify loop is genuinely sealed (no vapor venting) before scoring hysteresis.

**What a positive (Bin REVERSIBLE) means.** Supports the corpus mechanism class that a mass-conserving bounded pocket is a reversible spring (rim PE refills it) — the sonic-horizon LOCK verdict has a tabletop analog.
**What Bin CONTRADICT would mean, and what it does NOT mean.** Bin CONTRADICT would CONTRADICT the borrowed reversibility-from-mass-conservation argument — a genuine flag for Grant. But it does **not** prove the *vacuum* vapor-locks irreversibly: two-phase boiling hysteresis carries its own nucleation/superheat physics absent from the vacuum EOS. Either way this does **not** confirm "matter is a vapor-locked pump" (hypothesis-class, untested per `matter-as-vapor-locked-pump_framing.md`); does **not** test the vacuum. It tests **whether the borrowed reversibility argument is generically true in a real bounded loop** — a clean, bounded question.

## §6 — SINGLE-BUBBLE SONOLUMINESCENCE — RANK 6

**Bench setup.** Degassed water in an acoustic resonator driven at its standing-wave resonance (~20-30 kHz) by piezo transducers. A single Ar-seeded gas bubble is trapped at a pressure antinode; it collapses each acoustic cycle and emits a picosecond flash. Measure flash timing/intensity (PMT) and the wall trajectory `R(t)` (Mie scattering).
**Materials class:** degassed water, piezo transducers, function generator + power amplifier, PMT, photodiode for Mie `R(t)`. **Difficulty:** **HIGH** — degassing, single-bubble trapping, and acoustic tuning are finicky, but the apparatus is extremely well-documented (Gaitan/Crum/Putterman lineage).

**Literature class + CANONICAL CORPUS ANCHOR.** Single-bubble sonoluminescence (SBSL) / Rayleigh-Plesset collapse (Gaitan, Crum, Putterman et al.). This is **already canonical in the corpus** — Vol 3 Ch 14: [`sonoluminescence-derivation.md`](../manuscript/ave-kb/vol3/applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md), **claim `clm-91adfe`** (registered [`vol3/claim-quality.md:390`](../manuscript/ave-kb/vol3/claim-quality.md)). The corpus mechanism: the **Saturated Rayleigh-Plesset ODE** with `ρ_eff = ρ_0/(1−M²)^{3/2}`, `M = |Ṙ|/c_sound`; as `M → 1`, `ρ_eff → ∞`, `R̈ → 0`, and the collapse "autonomously halts before `R = 0`" — the acoustic instantiation of `m_eff = m_0 γ`.

**⚠ THE FIREWALL (state explicitly — this is the load-bearing discipline of this entry).** SBSL is **the firewall's OTHER mechanism.** Per [`double-slit-ee-mapping.md:101`](../manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md) (verbatim, verified this session): *"the sonoluminescence cavitation bubble proper is a DIFFERENT mechanism — saturated Rayleigh-Plesset inertia (`ρ_eff = ρ_0/(1−M²)^{3/2}`), NOT the `Γ=−1` impedance cavity. The three must never merge."* So this experiment tests the **RP-inertial-saturation mechanism class ONLY**. It is firewalled from **(a)** the electron's `Γ=−1` impedance cavity (the matter core) and **(b)** the **tensile pocket** of the cavitation-core / vapor-lock arc (§5). **RP inertial collapse ≠ the tensile pocket.** (Minor cite-hygiene flag, ledger §9: the same firewall text is duplicated in `_orchestration/double-slit-ee-mapping.md` at a *different* line number; the sonic-horizon prereg cites the `_orchestration` copy as `:92`. The **canonical KB leaf** carries it at `:101` — cited here.)

**AVE arc it maps to.** Vol 3 Ch 14 sonoluminescence (`clm-91adfe`) — the **Axiom-4 saturation-as-inertial-halt** mechanism class (`ρ_eff → ∞` halts collapse before `R = 0`).

**The falsifiable surface.** The class is: *as the collapsing wall Mach number `M = |Ṙ|/c_sound → 1`, the effective inertia diverges and the collapse autonomously halts before `R = 0`, the halt set by the `M → 1` saturation rather than by gas-pressure stiffness alone.* A fluid result CONTRADICTS it if the measured minimum radius `R_min` and the halt timing are **fully** explained by ordinary gas compression (a van-der-Waals hard core) with **no** Mach-saturation contribution — i.e., the deceleration near minimum shows no inertial-divergence signature beyond gas stiffness. The discriminating observable is whether the deceleration onset tracks `M → 1` *independently* of gas-content variation.

**5-line prereg skeleton.**
1. **Frozen observable:** `R_min` and the wall-deceleration profile `Ṙ(t), R̈(t)` near minimum radius, vs drive amplitude and dissolved-gas content; specifically whether deceleration onset tracks `M = |Ṙ|/c_sound → 1`.
2. **Bin CONSISTENT:** deceleration onset tracks `M → 1` saturation, robust to gas-stiffness variation.
3. **Bin CONTRADICT:** `R_min` + halt fully accounted by gas-compression van-der-Waals core, no `M`-saturation signature.
4. **Bin PARTITION:** both contribute → measure the partition.
5. **Stop rule:** vary dissolved-gas content across ≥ 3 levels at fixed drive; freeze bins before fitting `R(t)`.

**What a positive means.** The SBSL collapse-halt mechanism class — diverging effective inertia at `M → 1` preventing the RP singularity — has a real tabletop instance, supporting the Axiom-4 saturation-as-inertial-halt *borrowing* (`clm-91adfe`).
**What it does NOT mean.** Does **not** confirm vacuum Axiom-4 saturation (water acoustic saturation ≠ vacuum lattice saturation — consistency-class only); does **not** confirm the electron `Γ=−1` cavity (**FIREWALLED** — different mechanism); does **not** confirm the tensile-pocket / vapor-lock arc of §5 (**FIREWALLED** — RP inertial collapse ≠ tensile pocket, per `double-slit-ee-mapping.md:101`). The firewall is the load-bearing discipline here — a positive on RP inertia says nothing about the other two cavities.

## §7 — FLUME ANALOG HORIZON — RANK 7

**Bench setup.** An open-channel water flume with a controllable obstacle (bump/weir) creating a **transcritical** flow region where the local flow speed crosses the surface-gravity-wave speed. Surface waves sent upstream cannot propagate past the point where flow speed = wave speed — an **analog horizon**. Drive with a wave maker; measure wave-blocking and mode-conversion (the stimulated-emission "partner" wave). A **draining-vortex** (bathtub) variant gives a *rotating* horizon.
**Materials class:** flume + recirculation, wave maker, profiled obstacle, surface-elevation probes / optical free-surface measurement. **Difficulty:** **HIGH** — the canonical setup is a serious flume rig with careful free-surface metrology.

**Literature class.** Weinfurtner, Tedford, Penrice, Unruh & Lawrence 2011, "Measurement of stimulated Hawking emission in an analogue system" (water-channel analog horizon). The analog-horizon class.

**AVE arc it maps to.** The **sonic-horizon class** — [`2026-06-10_sonic-horizon-closure_result.md`](2026-06-10_sonic-horizon-closure_result.md) (+ [`_prereg.md`](2026-06-10_sonic-horizon-closure_prereg.md)): the `c²=0` surface forms a clean **reflecting** horizon (`Z_bulk → 0 ⇒ Γ → −1`), verdict **LOCK = reversible spring**; the **rotating-horizon handedness arm is UNRESOLVED** — the `±m` OAM probe was **degenerate** (`sonic_horizon_flow.py:184` set `cos(mφ)`, even in `m`, so `m=+1` and `m=−1` were bit-identical: `R_co = R_counter` to 18 digits). Related rows in [`divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md).

**The falsifiable surface.** The class is: *a flow region where local flow speed crosses the wave speed forms an analog horizon that blocks and mode-converts incident waves (a reflecting horizon).* A flume result CONTRADICTS it if the analog horizon does **not** reflect/mode-convert — waves pass through the crossing unimpeded. **The handedness sub-test is where the flume can do what the sim could not:** a draining-vortex (rotating) horizon supplies a genuine `e^{imφ}` surface-mode probe — does it show **frame-dragging-selective** transmission for co- vs counter-rotating modes (`m=+1` vs `m=−1`)? The corpus sim's `BLIND` was a **probe artifact** (even-in-`m`), so a non-degenerate flume probe **RESOLVES** what the sim left UNRESOLVED.

**5-line prereg skeleton.**
1. **Frozen observable:** the reflection/mode-conversion coefficient `R(ω)` of surface waves incident on the transcritical region (blocking ratio + converted-partner amplitude); for the draining-vortex horizon, the co-vs-counter transmission asymmetry `A_m`.
2. **Bin CONSISTENT:** clean blocking + partner-mode conversion at the crossing.
3. **Bin CONTRADICT:** no blocking — waves transmit through the crossing.
4. **Bin RESOLVE-HANDEDNESS:** `A_m ≠ 0` for the rotating horizon → frame-dragging-selective (resolves the sim's UNRESOLVED arm with a non-degenerate probe); `A_m = 0` → handedness-blind, but now from a genuine `e^{imφ}` probe.
5. **Stop rule:** verify the `e^{imφ}` probe is genuinely chiral (NOT a `cos(mφ)` standing pattern — the exact degeneracy that nulled the sim) before scoring `A_m`.

**What a positive means.** Confirms the mechanism class that a transcritical flow forms a wave-blocking analog horizon — and, with a rotating horizon, supplies the **non-degenerate `±m` probe the sim could not build**.
**What it does NOT mean.** Does **not** confirm the vacuum `c²=0` horizon (analog ≠ vacuum — consistency-class); a flume `A_m` measures **frame-dragging acoustic selectivity ONLY**, exactly as the sim's *repaired* probe would — it does **not** test the **I4₁32 cholesteric-Bragg lattice selection rule**, the OTHER, **non-representable** chirality mechanism (that needs the chiral-crystal engine, not a flume, per the sonic-horizon result's representation-capability flag). So a flume cannot speak to the cholesteric mechanism even with a perfect chiral probe.

## §8 — Shared instrumentation + the validation ladder

One instrument kit serves the whole program. The point of a shared kit is that the **DAQ chain is validated once, against known references, and then reused** — so a fluid result is never confused with an instrument artifact (`ave-apparatus-floor-attribution`).

**The kit.**
- **High-speed camera** — vortex-ring daughter spectra (§1), walker landing-statistics (§3), Taylor-column dye structure (§4), SBSL `R(t)` via Mie scattering (§6), flume free-surface (§7).
- **Strobe / stroboscopic illumination** — phase-locks the walker bounce sub-Faraday (§3), freezes vortex-ring timing (§1), gates the phase-locked SBSL flash (§6).
- **Polarimeter / crossed polarizers** — L/D crystal sign and optical-rotation counts for Kondepudi (§2).
- **cRIO as DAQ** — NI cRIO-9014 + NI-9263 (4ch AO, ±10 V, 100 kS/s) + NI-9215 (4ch AI, ±10 V, 100 kS/s) = a **DC-40 kHz, 4×4 phase-coherent lock-in**. It drives the piezo transducers (SBSL §6) and the Faraday shaker (§3), reads the PMT / flow meter / thermocouples (§5, §6), and does quadrature lock-in extraction. This is the same bench Grant owns for the first real-hardware electrical experiment.

**The validation ladder (cross-link: PR [#181](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/181)).** PR #181 (the cRIO `C_eff(V)` saturation-onset prereg) fixes the discipline: **never read physics through an unvalidated chain.** Its three-rung ladder — applied here **per fluid bench**, on the *fluid* side, before any physics read:

| Rung | Generic (PR #181) | Fluid-bench instance |
|---|---|---|
| **A — known-null** | linear cap, flat `C(V)` to ≤ 0.1% floor | a config where the effect *cannot* exist (e.g. same-handed leapfrog with rings far apart §1; unstirred-and-uncooled §2; off-resonance acoustic drive §6) → must read flat |
| **B — known-positive** | Class-2 MLCC / varactor, recover datasheet | a textbook-robust positive (Taylor column at deep low-`Ro` §4; SBSL at canonical Ar-seed drive §6) → must recover the literature result |
| **C — instrument floor** | open/short/stable-ref; report `σ` drift BEFORE any read | report camera/PMT/probe noise floor + drift over the integration window BEFORE scoring any bin |

This is `ave-apparatus-floor-attribution` applied to fluids: **validate-on-known-null, then known-positive, then quote the floor first** — exactly the cRIO "validate-on-known-cap" discipline. A bench that has not cleared rungs A-C does not get to score CONSISTENT/CONTRADICT.

## §9 — Cost / difficulty matrix + program framing + verification ledger

### §9.1 Cost / difficulty matrix (ranking rationale)

Ranked by **(discriminating value) × (feasibility) × (fit to the existing kit + Keith's fluids arm)**. Vortex rings lead because they are Keith's domain and ride a *live* arc; the three HIGH-difficulty rigs (walking droplets, SBSL, flume) rank last not for low value but for build cost.

| Rank | Experiment | Materials cost | Build difficulty | Keith-domain fit | Discriminating value | Live-arc coupling |
|---|---|---|---|---|---|---|
| 1 | Vortex-ring collisions | low-moderate | moderate (sync) | **high** | high (orientation-selective reconnection) | **live** (annihilation-evaporation, in-flight) |
| 2 | Kondepudi crystallization | **low** | **low** | moderate | high (driven-vs-stochastic; sign-blind gap) | canon (Ω_freeze) |
| 3 | Walking droplets | moderate | **HIGH** | high | high but **contested** (replication dispute) | open (pilot-mode fork) |
| 4 | Taylor columns | low-moderate | moderate | high | moderate-high (quantitative `L_col(Ω)`) | canon + **flagged label** |
| 5 | Pump-loop vapor lock | low-moderate | moderate | high (plumbing) | high (sealed-loop reversibility test) | recent (rim-PE / sonic-horizon) |
| 6 | Single-bubble sonoluminescence | moderate | **HIGH** | moderate | high (RP saturation; firewalled) | canon (`clm-91adfe`) |
| 7 | Flume analog horizon | moderate-high | **HIGH** | high | high (supplies the non-degenerate `±m` probe) | recent (sonic-horizon) |

**Suggested first build:** §2 (cheapest, undergraduate-robust, validates the polarimeter + the whole DAQ ladder on a forgiving system) in parallel with §1 (Keith's domain, live arc). Defer the three HIGH-difficulty rigs until the kit + ladder are proven on §1/§2.

### §9.2 Program framing — the falsification lab, extended to the bench

The AVE identity is a **standing falsification lab**, not a campaign to prove AVE right. This program extends that identity from sim and corpus to **real hardware**, with **Keith's fluids expertise as the program's experimental fluid arm** and Grant's plumbing/thermal-hydraulics instinct anchoring §5/§8. The bench's job is to **try to break the borrowed mechanism classes** — every entry above states the fluid result that would CONTRADICT the class the corpus relies on.

The governing law (§0) is what keeps this honest: **every experiment is consistency-class.** A positive constrains the *analogy* (the borrowed mechanism behaves as assumed); it never confirms the vacuum. The program's value is **asymmetric and negative-leaning**: a CONTRADICT result is a real, transferable flag against a corpus mechanism class (e.g. §5's sealed-loop irreversibility would directly challenge the sonic-horizon LOCK argument); a CONSISTENT result merely *fails to break* the borrowed analogy and earns it continued use. That asymmetry is the falsification-lab discipline doing its job.

### §9.3 Verification ledger (verify-before-cite — all anchors grep-checked 2026-06-11)

| Anchor | Cited as | Status |
|---|---|---|
| `trampoline-framework.md:97-105` | Ω_freeze freeze-in handedness (§2, §4) | **VERIFIED** verbatim |
| archive `59_…:252-267` + `:394` | driven-vs-stochastic falsifier (§2) | **VERIFIED** (§5.3 dichotomy + experimental implication) |
| `the-abandoned-interior.md:50` | Kelvin pair-shedding / collapse→confinement (§1) | **VERIFIED** verbatim (CONSISTENCY-CLASS tag confirmed) |
| `novel-objects-report.md:110,117` | twin-pocket N8 (§1) | **VERIFIED** — carried honestly as *geometric, not chiral* (`:117`) |
| `pilotwake-bhphase-survey_note.md` §2,§3 | pilot-mode fork + sim-never-run (§3) | **VERIFIED** verbatim |
| `double-slit-ee-mapping.md:101` | SBSL firewall (§6) | **VERIFIED** verbatim — *minor flag:* `_orchestration/` duplicate carries it at a different line; sonic-horizon prereg cites `:92` (the duplicate). Canonical KB = `:101`. |
| `sonoluminescence-derivation.md` + `clm-91adfe` (`vol3/claim-quality.md:390`) | SBSL canonical anchor (§6) | **VERIFIED** — claim id registered |
| `sonic-horizon-closure_result.md:202,232` | rim-PE LOCK = mass-conservation (§5, §7) | **VERIFIED** verbatim |
| `cavitation-core-probe_result.md:173` | FLASH/LOCK undecided (§5) | **VERIFIED** verbatim |
| `matter-as-vapor-locked-pump_framing.md:267,278` | vapor-locked-pump hypothesis-class (§5) | **VERIFIED** — hypothesis-class tag confirmed |
| `first-principles-predictions.md:16-29` | polar-impedance jet collimation (§4) | **VERIFIED** verbatim |
| PR #181 | cRIO validation ladder (§8) | **VERIFIED** — OPEN, A/B/C ladder confirmed in PR body |
| **"collimation sequence (D3) / imposed-rotation sim couldn't test it"** | parent framing for §4 | **❌ FAILED VERIFICATION** — no named corpus arc; the `D3` row in `divergence-test-substrate-map.md:462` is **D3-GEOM-ENTROPY** (geometric entropy), unrelated. §4 stands on the verified polar-collimation anchor; the D3/imposed-rotation-sim label is surfaced to Grant to point at the real arc or strike it. |

---

*End of DRAFT. Nothing here freezes until Grant + Keith ratify the class-tags and schedule bench time. Per lane discipline: the auditor lands any manual/COLLABORATION_NOTES entry; this doc surfaces the empirical program, it does not adjudicate it.*
