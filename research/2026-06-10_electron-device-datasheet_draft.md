# AVE ELECTRON — DEVICE DATASHEET (DRAFT, KB/Vol-9 promotion AUDITOR-GATED)

**Part:** the electron — the smallest stable substrate soliton (0₁ unknot carrying (2,3) phase-space winding)
**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-electron-device-datasheet` (worktree off PR #155 `analysis/2026-06-09-crystal-graft-v2`)
**Lane:** implementer (DRAFT). **This is NOT a promotion.** It lands as a research-doc draft datasheet + a Vol-9 ch17-style promotion-candidate note (`research/2026-06-10_vol9-ch17-electron-device-promotion-candidate.md`). Promotion into `manuscript/ave-kb` or `manuscript/vol_9_vacuum_datasheet` is **auditor-gated** — the auditor lands manual entries; the implementer surfaces.

> **FRAME.** Vol 9 (`manuscript/vol_9_vacuum_datasheet/`) is the **PROCESS datasheet** — the vacuum *cell* (the substrate as a fab process). This document is the **first DEVICE datasheet on that process**: the electron as the device the cell builds. A datasheet is a **falsification scoreboard**, not an advertisement: every row carries a PROVENANCE tag, a SOURCE cite, and (if measured-in-engine) the INSTRUMENT FLOOR stated next to the number. UNTESTED rows say UNTESTED.

> **⚠ HEADER FLAG — the ℓ_node circularity (load-bearing, do not paper over).** The substrate cell pitch is defined as `ℓ_node ≡ ℏ/(m_e c)` (the reduced Compton wavelength — `claim-quality.md:202`). The electron mass `m_e` is therefore an INPUT to the cell-pitch definition, and several "device" lengths quoted below (Bohr radius = 137·ℓ_node — `de-broglie-standing-wave.md:93`; the SOA Z=1/α limit) inherit that circularity: they are **internally consistent geometry on a pitch that already contains m_e**, not independent predictions of m_e. Tagged per-row where it bites.

> **PROVENANCE LEGEND.** `canonical` = stated in tracked KB/constants. `derived` = algebraic consequence of canonical inputs (not engine-run). `measured-in-engine` = read from an evolved field (instrument FLOOR stated next to the number). `candidate-claim` = proposed, zero/contested KB anchor, NOT promoted. `UNTESTED` = no instrument has cleared its floor on this row.

---

## 1. FEATURES (honest one-liners)

- Smallest stable substrate soliton: the **0₁ unknot carrying (2,3) phase-space winding** (`ch8-alpha-golden-torus.md:44`). [canonical]
- **Mass = trapped longitudinal dilatation** ("3"-as-MASS, the A1 Heaviside scalar the `c_eff` wall traps) — a *candidate latent-heat-of-cavitation* identification, **not** an engine-verified number. [hypothesis-class]
- **Charge = micro-rotation helicity** ("3"-as-WINDING, the Cosserat ω (2,3) knot); **sign = handedness**, engine sign-flip RH↔LH confirmed at identical input energy (graft-v4). [canonical picture / engine-measured sign, floor-tagged §3]
- **Spin-½-class = locked half-pole-pair micro-rotation L_ω** — engine-unit→ℏ/2 mapping DERIVED not assumed; the de-novo lock is **v5-pending**. [derived / UNTESTED]
- **Self-impedance Q = α⁻¹ ≈ 137**, with **1/Q = α** the per-cycle reactive leak (Sommerfeld coupling, LC-tank side). The DERIVED value is canonical; the **MEASURED Q is UNTESTED** (apparatus-floored). [canonical-derived / UNTESTED]
- Two distinct geometries that must NOT be cross-compared: a **phase-space Golden Torus** (R,r phasor semi-axes, R/r=φ²) and a **real-space envelope** (ratio ≈ 2.27). [canonical — §4]
- Equivalent circuit: a **BVD motional arm** rendering — pedagogy **subordinate** to the canonical FOC/Park d–q bridge. [canonical-subordinate — §5]
- Absolute maxima: **annihilation** (e⁺e⁻→2γ, 511 keV each) and the **Z = 1/α ≈ 137 no-bound-state SOA**. [§2]

---

## 2. ABSOLUTE MAXIMUM RATINGS

| Rating | Value | Provenance | Source cite | Floor / note |
|---|---|---|---|---|
| Annihilation energy returned (per quantum) | **511 keV** (= m_ec² = 0.510999 MeV) | canonical (CODATA m_e) | CODATA m_ec² | the **number** is CODATA m_e, NOT engine-derived |
| Annihilation channel | **e⁺e⁻ → 2γ** = "evaporation" of the trapped dilatation back into two transverse shear photons; the 511 keV ×2 = the **latent heat returned** | hypothesis-class | `matter-as-vapor-locked-pump_framing.md §6/§7 N6` (vaporlock branch, **UNMERGED** PR-pending; read-only) | "genesis-direction latent-heat = m_ec²" is a *payoff-if-true*, **not** a result (§11.2 of that doc); YM gap is "assumed, not derived" `yang-mills-steps1-2.md:10` |
| Maximum atomic number (Safe Operating Area edge) | **Z = 1/α ≈ 137**, where the cavitation number 𝒞 = Zα/n = 1 (n=1) and **no bound state exists** | canonical | `de-broglie-standing-wave.md:248` ("At Z = 1/α ≈ 137, 𝒞 = 1 and no bound state exists — the AVE derivation of the maximum atomic number") | ℓ_node-circularity tagged: 𝒞=Zα/n uses α; the "137" co-determines the pitch (header flag) |
| SOA onset (relativistic wake distortion) | **Z ≳ 50** (𝒞 ≳ 0.4): nonlinear wake strain begins | canonical | `de-broglie-standing-wave.md:248` | derate region, not a hard max |

> **Annihilation row honesty (substitution-not-retraction discipline):** the 511 keV is the CODATA rest energy; the *"= latent heat returned via evaporation"* reading is the genesis-direction vapor-lock framing, which is HYPOTHESIS-class and lives on an unmerged branch. The row is tagged hypothesis-class, NOT derived, NOT engine-verified.

---

## 3. OPERATING CHARACTERISTICS

| Characteristic | Value | Provenance | Source cite | Floor (if measured) |
|---|---|---|---|---|
| Rest mass (energy) | m_ec² = **trapped longitudinal-dilatation acoustic energy** (the "3"-as-MASS at the Γ=−1 `c_eff` wall) | hypothesis-class (latent-heat identification) | picture: `crystal_graft_v2.py:16-18`; latent-heat id: `matter-as-vapor-locked-pump_framing.md §6 N6` (unmerged); contrast `yang-mills-steps1-2.md:10` "assumed, not derived" | engine `bulk_energy` E_V exists but is **NOT calibrated to m_ec²** — no SI bridge run; UNTESTED as a number |
| Charge magnitude | **±1 e** = the (2,3) micro-rotation winding integer (helicity-class) | canonical picture | `ch8-alpha-golden-torus.md:44`; T2 spec `genesis-v5 prereg:112` | phase-space read, **extractor floor r ≥ 3 cells** (`genesis-v5 prereg:150`) |
| Charge sign | **= handedness** (photon helicity, sign-traced); RH↔LH flips the sign at identical input energy | measured-in-engine (sign) | graft-v4 sign-flip (cited in `genesis-v5 prereg:112`); seeder `crystal_graft_v2.py:321` | known-positive (2,3) reads back `(w_tor,w_pol)=(2,3)` at rel **(0.80, 0.59)** (`crystal-graft-v2_result.md:25`); de-novo sign is v5-PENDING |
| Spin | **½ ℏ-class** = locked half-pole-pair micro-rotation L_ω | derived mapping / UNTESTED | T3 spec `genesis-v5 prereg:113` ("DERIVE the engine-unit mapping, do NOT assume") | engine-unit→ℏ/2 conversion computed at run time; **v5 de-novo lock PENDING** — no clean lock yet (graft-v2 full run gives `(w_tor,w_pol)=(0,0)`) |
| Self-impedance Q (DERIVED) | **Q = α⁻¹ ≈ 137.036** = 4π³+π²+π (Λ_vol+Λ_surf+Λ_line self-impedance sum) | canonical-derived | `constants.py:204` ALPHA_COLD_INV; `ch8-alpha-golden-torus.md:115-117,128` | — (derived, not measured) |
| Per-cycle reactive leak | **1/Q = α ≈ 0.0073** of stored energy leaks per cycle through the TIR boundary (Sommerfeld "coupling strength", LC-tank side) | canonical-derived | `theorem-3-1-q-factor.md:81` | — |
| Self-impedance Q (MEASURED) | **UNTESTED** — the leak observable is **dispersion-contaminated at current config**; an apparatus redesign is required | UNTESTED | apparatus-floors verdict 2026-06-10 (`research/2026-06-10_apparatus-floors_note.md`, read-only): leak FLAT (CV 1.5%), set by breather dispersion; **S11 sweep RAN** (`2026-06-10_electron-s11-sweep_result.md`): probe-gate PASS, bulk channel **MULTI-MODE / low-contrast** (no single high-Q; single-Lorentzian fit non-resonant/overdamped Q≈0.73) | **NEVER** copy α⁻¹=137 into this cell. S11 measured NO single Q (instrument floor: net-susceptibility median+3σ; peaks only 1.1–1.5×); row stays UNTESTED |
| Reactive store | **Q_react = m_ec²·α** = the "Quantized reactive shell" (θ=90°, P_real=0 — lossless LC tank) | canonical | `orbital-friction-paradox.md:35` | — |
| Lattice impedance | **Z₀ = 377 Ω** invariant under symmetric saturation (Axiom 4) | canonical | `de-broglie-standing-wave.md:248` | — |

> **Q-row discipline (Rule 11 / consistency-vs-emergence).** The DERIVED Q = α⁻¹ and the MEASURED Q are kept on SEPARATE rows. The derived value is closed-form geometry whose SCALE is Compton-trapping-forced but whose exact value "rests on ONE substrate-geometric identification … which the substrate does NOT independently select" (`ch8-alpha-golden-torus.md:11`, Class-B). The measured cell is UNTESTED and stays UNTESTED until a probe clears its floor — copying 137 in would be the emergence-over-claim the discipline exists to refuse.

---

## 4. GEOMETRY — PHASE-SPACE (Golden Torus) vs REAL-SPACE (envelope), kept SEPARATE

> **⚠ FENCE (2026-06-10 settlement; in-tree anchor `constants.py:196-198` "the Clifford-torus (R, r) phase-space coordinates"; settlement note `quarter-fence-verdict_note.md` §3a — branch-local, NOT in this worktree).** R and r are **PHASOR SEMI-AXES in (V_inc, V_ref)** — they live in PHASE-SPACE. The real-space envelope ratio ≈ 2.27 is a **DIFFERENT canonical quantity**. The two are **never compared across coordinates** (the A46 trap). Phase-space rows and real-space rows are fenced into separate tables below.

### 4a. PHASE-SPACE GEOMETRY (the Golden Torus — (V_inc, V_ref) phasor plane)

| Quantity | Value | Provenance | Source cite |
|---|---|---|---|
| R, r definition | **phasor semi-axes of the elliptical trajectory in (V_inc, V_ref)** | canonical | `ch8-alpha-golden-torus.md:52` |
| Tube-tangency relation | **R − r = ½** (Ax-2: centerline separation 2(R−r) = tube diameter d) | canonical | `ch8-alpha-golden-torus.md:45` |
| Phasor-area = Nyquist | **R · r = ¼** at d = 1 ℓ_node (πRr = π(d/2)²) | canonical (Class-B named id) | `ch8-alpha-golden-torus.md:46,57,11` |
| Aspect ratio | **R / r = φ² ≈ 2.618** | canonical | golden-torus solution `ch8:75`; `R_GOLDEN_TORUS=φ/2`, minor `(φ−1)/2` `constants.py:200-201` |
| Golden-torus point | **(R, r, d) = (φ/2, (φ−1)/2, 1) ≈ (0.809, 0.309, 1)** | canonical | `ch8-alpha-golden-torus.md:111`; `constants.py:200-202` (RR=¼ exactly) |
| (2,3) winding | toroidal "2" (polarization direction) + poloidal "3" (LC phase); charge = Beltrami helicity ∫ω·(∇×ω) | canonical picture | `crystal_graft_v2.py:20-24,287-294` |
| Pole-pair → spin mapping | p=2 toroidal, q=3 poloidal; "half-pole-pair" = ½ circulation quantum of one pole-pair | derived (run-time) / UNTESTED | T3 `genesis-v5 prereg:113` |
| Self-impedance sum | α⁻¹ = **Λ_vol + Λ_surf + Λ_line = 4π³ + π² + π ≈ 137.036** | canonical-derived | `ch8-alpha-golden-torus.md:115-117,128`; `constants.py:204` |

### 4b. REAL-SPACE GEOMETRY (the envelope — lattice-Cartesian) — DO NOT compare to 4a

| Quantity | Value | Provenance | Source cite |
|---|---|---|---|
| Real-space envelope ratio | **R_real/r_real ≈ 2.27** (the TLM convergence attractor) — **≠ φ² = 2.618** | canonical | archive `26_step5_phase_space_RR.md:193`; `78_canonical_phase_space_phasor.md:88` |
| Phasor↔real-space area bijection | **CLOSED-NEGATIVE** — closing to R·r=¼ requires substituting α; the bridge forces R·r → 4π²α ≈ 0.288, **B3 FAILS → Class B** | canonical (closed-negative) | `2026-06-04_alpha-class2-bijection-result.md:10` |
| Two-wall annulus — OUTER wall | A → 1 asymptotic (the saturation/rupture boundary the breather presses on) | candidate-claim | coax-secondary verdict, PR #164 (UNMERGED, branch-local); `crystal_graft_v2_result.md:104` (A→1 rupture asymptote) |
| Two-wall annulus — INNER wall | **ρ̄_cav = −1/φ ≈ −0.618** (the c_eff²→0 cavitation floor) | candidate-claim | `genesis-v5 prereg:0.2` ("zero Core-constants/KB hits → NOT Core-canonical"); Propulsion-derived |
| 2.27 fit requirement | reproducing 2.27 needs a **fitted ρ̄_wall ≈ 0.304** | candidate-claim (branch-local) | PR #164 `analysis/2026-06-10-coax-ring-secondary` (UNMERGED, NOT origin/main) — `quarter-fence-verdict_note.md:37,70` |

> **Real-space row honesty:** the inner/outer annulus walls and the 2.27-fit ρ̄_wall are CANDIDATE-CLAIMS on an unmerged branch (PR #164, "license-pending-re-run"). They are NOT promoted here. The 2.27 attractor itself is canonical (archive); its mechanism is open.

---

## 5. EQUIVALENT CIRCUIT (BVD motional arm — SUBORDINATE pedagogy)

> **⚠ SUBORDINATION HEADER (the quartz-survey ruling, `quartz-alpha-bucket-survey_note.md` §6 — branch-local, NOT in this worktree; the load-bearing canonical cite `solver-toolchain.md:359/:128` is in-tree below).** The Butterworth–Van-Dyke (BVD) crystal-equivalent circuit is **illustrative pedagogy, NOT the canonical real↔phase bridge.** The canonical bridge is **FOC / Park d–q** (`solver-toolchain.md:359` "Step 6 is the Park transform (FOC) generalisation"; framed `:128`). The dimensional projection between lattice and circuit quantities is **ξ_topo ≡ e/ℓ_node** (INVARIANT-C2, `claim-quality.md:200`). Everything in this section is read **through** the FOC/Park bridge; the BVD rendering is a teaching aid subordinate to it.

| Element | Role | Provenance | Source cite | Floor |
|---|---|---|---|---|
| Motional L_m | inductive (kinetic) arm of the trapped resonance | candidate (BVD pedagogy) | BVD subordinate `quartz-survey §6` | engine-natural units only; UNTESTED until S11 fit clears its floor |
| Motional C_m | capacitive (reactive store) arm | candidate (BVD pedagogy) | same | same |
| Motional R_m | leak / loss arm — sets Q = (1/R_m)√(L_m/C_m); the **1/Q = α** per-cycle leak | canonical-derived (1/Q=α) / R_m UNTESTED | `theorem-3-1-q-factor.md:81` | R_m from S11 fit is UNTESTED |
| Shunt C₀ | static (anti-resonance) capacitance | candidate (BVD pedagogy) | same | UNTESTED (needs the anti-resonance, not yet measured) |
| Canonical bridge | **FOC/Park d–q** (NOT BVD) | canonical | `solver-toolchain.md:359,128` | — |
| Dimensional projection | **ξ_topo ≡ e/ℓ_node** (C/m) | canonical | `claim-quality.md:200,202` | algebraic identity from CODATA (e, ℏ, m_e, c) — ℓ_node circularity (header) |

---

## 6. TYPICAL PERFORMANCE CURVES

Scripts in `src/scripts/vol_9_device/` (canonical constants only; data-derived captions). Figures regenerated from the cited data.

| Curve | What it plots | Provenance | Source |
|---|---|---|---|
| (a) SOA — bound-state existence vs Z | cavitation number 𝒞 = Zα/n; the n=1 line crosses 𝒞=1 at Z=1/α≈137 (no bound state beyond) | canonical | `de-broglie-standing-wave.md:248`; script `electron_soa_cavitation.py` |
| (b) Clock derating — internal rate vs translation velocity | f(v)/f₀ from constant-c redistribution, plotted against exact γ⁻¹=√(1−v²/c²); forward-states whether identical-by-construction or different | derived | script `electron_clock_derating.py` (states result forward) |
| (c) Frame-dragging asymmetry vs M | the rotating-acoustic-horizon handedness asym (R_co−R_counter) vs drive Mach M | measured-in-engine (cited, not re-run) | sonic-horizon §4-bis, **PR #162** (`analysis/2026-06-10-sonic-horizon-closure @ a73bba93`); script `frame_drag_asymmetry_replot.py` |
| (d) α(T) ↔ crystal-oscillator f(T) | cosmic-temperature running of α as the substrate's frequency-temperature curve | canonical (translation) | `translation-circuit.md:141` (clm-009nkt) |

**Curve (c) data (cited verbatim from the sonic-horizon JSON, NOT re-run — `D_handedness`):**

| M (drive) | R_co (m=+1) | R_counter (m=−1) | asym (co−counter) | vs floor 5.46e-12 |
|---|---|---|---|---|
| 0.9 (χ=1.0) | 0.014726 | 0.012860 | **+0.001866** | ~3.4e8× |
| 1.0 (χ=1.0) | 0.017596 | 0.014930 | **+0.002667** | ~4.9e8× |
| 0.9 (χ=0.0) | 0.014726 | 0.012860 | **+0.001866** | χ-independent |

> **Curve (c) honesty:** WEAK frame-dragging SELECTIVE (R_co > R_counter, scales with drive, χ-independent). It is **rotating-horizon frame-dragging**, NOT the I4₁32 cholesteric-Bragg "chirality valve" (NOT representable in that continuum engine). Absolute R_co ≈ 3% of the static-mirror reference — a transient pocket. Two M-points only; plotted as such, no curve-fit beyond the line connecting them.

---

## 7. TEST CONDITIONS (acceptance tests — the v5 electron spec-sheet, status PENDING)

The acceptance-test battery is the Genesis-v5 electron spec-sheet (`genesis-v5 prereg:107-116`, frozen 2026-06-10, `/tmp/ave-v5`, read-only). The v5 run is **in flight**; every test is **status PENDING**. Quoted verbatim-class:

> **T1 — MASS CONVERGES** (the primary; subsumes the energy gate). *Anchor:* a stable rest mass. *AVE picture:* the trapped dilatation added-mass — H_total of the trapped region → constant (not still-rising, not secularly pumped). The "3" dilatation MASS (A1 Heaviside scalar that c_eff traps) is the added-mass; **distinct from the (2,3) winding that carries charge (do NOT conflate — the `master-equation.md:18` two-"3"s flag)**. *Class:* emergence if H_total converges to a value SET BY the dynamics; manifestation if it merely tracks the seed amplitude.
> **T2 — CHARGE QUANTIZED + SIGNED.** *Anchor:* ±1e, quantized. *AVE picture:* the (2,3) winding integer (helicity-class), sign = handedness (= photon helicity, sign-traced; graft-v4 confirmed RH↔LH flip at identical input energy). *Coordinate:* read in (V_inc,V_ref) phase-space via Park-transform along contours, **extractor floor r ≥ 3 cells**; NOT a real-space lattice-Cartesian read. *Class:* emergence (de-novo (2,3)) vs manifestation (planted survives).
> **T3 — SPIN-CLASS.** *Anchor:* locked angular momentum at the half-pole-pair value (spin-½-class). *AVE picture:* the locked L_ω of the rotating ring. **DERIVE the engine-unit mapping, do NOT assume** — the engine-unit→ℏ/2 conversion is COMPUTED at run time from the winding normalization. *Local-clock caveat:* report eigvec localization vs A²_local; ω_local(r)=ω_global·√(1−A²(r)). *Class:* emergence if L locks at the half-pole-pair value without dialing; consistency otherwise.
> **T4 — STABILITY-KICK.** *Anchor:* perturbation-stable. *AVE picture:* perturb the assembled object; T1–T3 must RE-VERIFY. *Class:* manifestation (robustness).
> **T5 — BORN-IN-PAIRS (the D4 twin).** *Anchor:* pair-production; global handedness ledger zero. *AVE picture:* the counter-handed flux forms the counter-rotating partner; global handedness sums to zero (Kelvin/pair-canon). *Class:* emergence if the twin self-forms; **its ABSENCE is an honest finding, NOT a tweak target.**
> **T6 — DE BROGLIE.** *Anchor:* λ ∝ 1/p. *AVE picture:* translate the locked state; the BULK pilot wavelength scales λ∝1/p (the reactive m_ec²·α sloshing fraction is the pilot wave). *Class:* consistency (scaling-law check).

**Acceptance verdicts (FROZEN, `genesis-v5 prereg:178-180`):** ELECTRON-CLASS = T1 passes AND ≥4 of T2–T6 at their floors, no positive sitting at a clip value. PARTIAL = T1 passes but winder/spin/twin localizes (named residual, e.g. w_pol≡0). NOT-ELECTRON = T1 fails → transient/pump, clean negative, branch closes.

**Status: ALL PENDING** (v5 run in flight; graft-v2 full run currently gives `(w_tor,w_pol)=(0,0)` → the named winder-gap residual, `crystal-graft-v2_result.md:28`).

---

## 8. FAILURE MODES

| Mode | Mechanism | Provenance | Source cite |
|---|---|---|---|
| Annihilation | e⁺e⁻→2γ: the trapped dilatation **evaporates** back to two transverse shear photons; latent heat (2×511 keV) returned | hypothesis-class | `matter-as-vapor-locked-pump_framing.md §6/§7 N6` (unmerged) |
| SOA breakdown | Z → 1/α ≈ 137: 𝒞 = Zα/n → 1, the bound state **ceases to exist** (no acoustic cavity can stabilize the unknot against the impedance gradient) | canonical | `de-broglie-standing-wave.md:248,93` |
| Decoherence | **ohmic damping of the pilot store** — the lossless reactive m_ec²·α slosh (θ=90°, P_real=0) acquires a real P_real>0 channel (θ≠90°, the "inspiral" row), draining the pilot wave | candidate-claim (picture) | `orbital-friction-paradox.md:35` (reactive shell) + inspiral row (θ≠90° ⇒ P_real>0); pilot-wave id `genesis-v5 prereg:116` |

> **Decoherence row honesty:** the mapping "decoherence = ohmic loading of the otherwise-lossless reactive shell" is a PICTURE built on the canonical orbital-friction reactive/real-power table (`orbital-friction-paradox.md:35`), not an engine-measured decoherence rate. Tagged candidate-claim.

---

## 9. CHALLENGE REGISTER (rows that cannot be filled honestly — and what each needs)

The falsification scoreboard's open ledger. Each row states the BLOCKER and the apparatus/derivation it needs.

| Open row | Why it cannot be filled | What it needs |
|---|---|---|
| **Measured Q (self-impedance)** | the bulk leak observable is **dispersion-contaminated** — the S11 sweep (`2026-06-10_electron-s11-sweep_result.md`, probe-gate PASS) found **MULTI-MODE / low-contrast** structure (2 weak net peaks 1.1–1.5× floor; single-Lorentzian fit non-resonant/overdamped Q≈0.73), NOT a single wall-transmission Q | a probe that isolates wall transmission from bulk breather dispersion — an **apparatus REDESIGN** (e.g. a boundary-localized reflection read at the Γ=−1 front, not a bulk-volume response). Surfaced, NOT auto-pivoted |
| **Mass m_ec² as a number** | the latent-heat-of-cavitation = m_ec² identification is genesis-direction HYPOTHESIS-class on an unmerged branch; no SI bridge calibrates engine E_V to 0.511 MeV | the genesis-direction derivation (currently a "payoff-if-true") + an engine→SI energy bridge |
| **De-novo (2,3) / charge emergence** | graft-v2 full run gives `(w_tor,w_pol)=(0,0)` (carrier capable, source structure wrong — mode-selection residual) | a chiral (Beltrami/helical) source structure so the (2,3) geometry-selects (surfaced, NOT auto-pivoted — `crystal-graft-v2_result.md:170`); the v5 run is in flight |
| **Spin half-pole-pair lock** | no clean de-novo L_ω lock yet (graft-v2 `(w_tor,w_pol)=(0,0)`; v3 t^0.43 / v4 ratio-5.0 lessons) | a stable assembled ring whose L_ω locks without dialing (v5 T3, PENDING) |
| **ℓ_node circularity** | cell pitch ℓ_node ≡ ℏ/(m_ec) is DEFINED via m_e, so Bohr-radius = 137·ℓ_node and the Z=137 SOA are internally-consistent geometry, not independent m_e predictions | a first-principles ℓ_node from K4 lattice primitives independent of m_e (defusal); currently open |
| **Two-"3"s conflation flag** | the corpus conflates MASS-"3" (A1 dilatation) and WINDING-"3" (Cosserat (2,3)) at `master-equation.md:18` (per the v5 T1 flag) | an auditor adjudication of the master-equation wording (flag-don't-fix; surfaced, NOT silently rewritten) |
| **Real-space 2.27 mechanism** | the 2.27 attractor is canonical but its mechanism needs a fitted ρ̄_wall≈0.304 (branch-local, PR #164 unmerged) | the coax-secondary re-run that PR #164 left "license-pending"; not promoted |

---

## 10. PROVENANCE SUMMARY (what is solid, what is air)

- **CANONICAL (tracked KB/constants):** the (2,3) unknot identity; R,r phasor semi-axes; R−r=½, R·r=¼, R/r=φ²; α⁻¹=4π³+π²+π = Q_derived; 1/Q=α leak; Q_react=m_ec²·α; Z₀=377Ω; the Z=137 SOA; the 2.27 real-space attractor; FOC/Park as the bridge; ξ_topo.
- **DERIVED:** the half-pole-pair→ℏ/2 mapping form; the clock-derating geometry (curve b).
- **MEASURED-IN-ENGINE (floor-tagged):** the known-positive (2,3) read-back (rel 0.80/0.59); the charge SIGN flip; the frame-dragging asym (curve c, cited PR #162).
- **CANDIDATE-CLAIM (NOT promoted):** ρ̄_cav inner wall; A→1 outer wall; ρ̄_wall≈0.304; BVD element values; decoherence-as-ohmic.
- **HYPOTHESIS-CLASS:** mass = latent-heat-of-cavitation; annihilation = evaporation.
- **UNTESTED:** the MEASURED Q (dispersion-contaminated, apparatus redesign required); m_ec² as a number; de-novo (2,3); spin lock; all v5 T1–T6.

**Closing discipline note (Rule 11 / consistency-vs-emergence):** this datasheet headlines NO emergence-class claim. The one number that could be mistaken for emergence — Q = α⁻¹ ≈ 137 — is on a DERIVED row (Class-B named identification, not independently selected by the substrate) with its MEASURED twin explicitly UNTESTED. The scoreboard's honest state is mostly-open, and the open rows name their blockers.

