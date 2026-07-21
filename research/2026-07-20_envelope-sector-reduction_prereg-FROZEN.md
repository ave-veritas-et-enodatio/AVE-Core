# Envelope-Sector Reduction — FROZEN pre-registration (slow dynamics of the saturable lattice; the gravitational-band coupling κ)

**Date:** 2026-07-20
**Class:** DERIVATION + lattice-derived research-driver (research-doc; **forms derived, values calibration/observation-imported and tagged; mints no `clm-`, propagates to no KB/tex leaf**). This is COMMIT 1 — the pre-registration ALONE, frozen and pushed before any derivation or driver code (the #761 frozen-first discipline).
**Provenance:** Grant-fired 2026-07-20 (verbatim `[sic]`: `"fire the lane"`). The forward derivation following the #761 NONE-DERIVES verdict (`research/2026-07-20_mechanical-commonmode-derivation_result.md`, CLEARED at branch head `d17a2248`, un-merged — cited `[branch:#761 @ d17a2248]`). #761 killed the **carrier** level (a cold breathing source radiates ≈98% longitudinal P-branch). This lane relocates the gravitational-band question **one level down**, to the **envelope** sector: the mass is the ENVELOPE of the A1 breather (`master-equation.md:20` `[canon]`: "the A1 breather; `mₑc²` = trapped acoustic compression energy") — a fast internal carrier (`ω_e`-class, node-scale) under a slow spatial envelope `A(r)`. The orbital band (`2Ω ~ 10⁻⁴ Hz`) is ~24 decades below the carrier. Derive the envelope sector's OWN dynamics and answer: what does an orbiting envelope-lump radiate, in which channel, at what derived coupling `κ`, against the banked pulsar bound?
**Lane fences:** DERIVATION lane only. Engine `src/ave` **BYTE-UNTOUCHED** (imports read-only; the saturated-envelope dynamics, if needed, live in the driver under `research/drivers/`). **No** `manuscript/` or `manuscript/ave-kb/` `.tex`/`.md` leaf edits; **no** port-register edit; **no** un-revert; **no** falsification-ledger edit — regardless of outcome. Every `[canon]` input content-verified two-method at base HEAD `f84b622b` (verify-before-cite). #761 content cited `[branch @ d17a2248]`. Pulsar figures `[import]`-tagged.

> **FREEZE STATEMENT.** This document freezes: (i) the KILL-LINE `κ_max` derived from the banked q1 §2.2 numbers (§1); (ii) the four verdict BINS + the CONSISTENCY GATE + the ANTI-SEDUCTION FENCE (§2); (iii) the per-LEG criteria, including the Leg-C observable/grid/window/tolerance and the imposed-texture FALLBACK scope (§3); (iv) the UNDETERMINED fork guard (§4). Nothing below §4 is a result — the derivation and driver land in later commits. The verdict may cite ONLY the frozen criteria's outputs.

---

## §0 — REGIME / SECTOR / PHASE-STATE header + substrate-native walk (fired before any envelope algebra)

**MODE.** A non-relativistic compact binary in the inspiral (Hulse-Taylor B1913+16, `v/c ~ 10⁻³`; double pulsar J0737-3039A/B, `v/c ~ 2×10⁻³`) as a **source** driving the deep vacuum. Each star is a mass = an A1-dilatation envelope-lump. Contrast column: the observed orbital decay `Ṗ_b`, matched to the GR shear-quadrupole `[import]`.

**REGIME.** **Regime I** — deeply linear far field (`V_GW/V_snap ~ 10⁻²⁵`); the propagating far field is cold-linear/lossless. **BUT** — and this is the substrate-native distinction from #761 — the SOURCE (the mass-lump itself) is a **SATURATED** structure (`A` near `A_yield`; Op14 ON *inside the lump*). #761 injected a COLD sub-yield breathing pulse (saturation OFF everywhere). The envelope framing requires the lump to be a saturated operating-point texture whose *coefficients* (`c_eff(A) = c₀√S` / `c₀/S`, `ε_eff = ε₀S`, `μ_eff = μ₀S`) are modulated, with the far field still cold-linear. The saturated lump is a **graded-index / graded-operating-point region**, not a cold breathing monopole.

**PHASE-STATE.** **Cold-reactive far field** (Ax3-lossless-reactive; `eq_axiom_3.tex:24` `[canon]`), **saturated core** (Op14). Far-field radiation is a legal Ax3 loss channel (port-not-valve), so a radiating envelope mode does NOT violate Ax3.

**SECTOR.** The observed GW = **T2 transverse shear** at `c`. The channel under test = **A1 bulk/compression** (the mass sector), radiative P-branch (`c_P/c_S ≈ 1.71–1.90`, `srs-band-structure.md:120` `[canon]`, direction-resolved `[100]1.71/[110]1.85/[111]1.90`). **Sector-ownership discipline (do NOT cross-wire):** A1 owns compression/mass/dilatation; T2 owns shear/GW. The masses ARE the A1-dilatation content (`master-equation.md:20` `[canon]`).

**SUBSTRATE-NATIVE + PHASE-SPACE-COORDINATE CHECK (A46).** The corpus claim is a *channel-radiation* claim (does an orbiting mass-envelope open a far-field COMPRESSION port?). The matching test coordinate is the **longitudinal (`∇·u`, radial) vs transverse (`∇×u`, tangential) displacement-energy partition of the RADIATED field** — the same channel basis the vector survey + #761 use, NOT a scalar `φ²` proxy, NOT lattice-Cartesian. The coupling `κ` is measured as `F_bulk/F_shear` in that channel basis (§1). A46-clean.

**SUBSTRATE-NATIVE WALK (fired before scaffolding the Leg-C driver; the 8-checkpoint walk, prose-derivation trigger 6 active).**
1. **K4 connectivity.** Reuse the #761 / `srs_band_survey` rank-2 bond model on the chiral srs-z3 net (`ave.core.chiral_lattice._SRS_8A/_NN`, `Φ_b = k_a d̂⊗d̂ + k_s(I−d̂⊗d̂)`, derived `ρ* = 9.77337` from `ν_Hill = 2/7`). Rule-14 reuse; no new stencil, NOT a Cartesian Laplacian.
2. **Cosserat / channel basis.** Partition the radiated field into radial (longitudinal, P) AND tangential (transverse, S) — the S-branch is the observed-GW analog and its survival is the consistency gate.
3. **Op14 saturation — THE distinction from #761.** The lump is an imposed SATURATED bias texture `A(r)` (near `A_yield`) that modulates the local bond stiffness via `S(A) = √(1−(A/A_yield)²)` (`eq_axiom_4.tex:7` `[canon]`); local clock `ω_local(r) = ω_global·√(1−A²(r))`. #761's cold breathing source is the SOURCE-on-RHS picture; this lane's saturated bias texture is the COEFFICIENT picture (§4 fork).
4. **Phase-space vs real-space (A46).** Observable = channel-basis energy partition (above); NOT a `φ²` real-space proxy.
5. **Checkpoint 8 (emergence/hosting) — the FALLBACK constraint.** A self-bound saturated soliton is **INFEASIBLE** on the lossless engine (electron-lock arc, `research/2026-07-08_electron-lock-arc_CLOSE.md`: FILLS-BUT-DECAYS; "on a lossless / Axiom-3 substrate, nothing holds itself by a reactive mechanism"). So this lane does NOT plant a finished soliton and test persistence. The honest fallback: IMPOSE / pin a saturated bias texture, translate/orbit it, measure cold far-field radiation — scoped as the COEFFICIENT-coupling test, NOT envelope self-consistency (declared, §3 Leg C).
6. **Checkpoint 10 (boundary-not-bulk).** Saturation rendered as a bounded operating-point BIAS on the coefficients (graded index), NOT a bulk force term that detonates at the wall.

**PRE-TEST PHYSICS CHECK (Rule 16; the one plumber-physical question surfaced to Grant BEFORE the framing locks).** *Grant — plumber-physically: when a mass-lump (a saturated compression well) orbits, does the far-field lattice see it as (a) a **breathing pressure source** oscillating on the wave-equation RHS — the #761 picture, which radiates compression — or (b) a **slowly-moving bias on the coefficients** (the local operating point / refractive index) that the wave-equation's medium properties ride on, so the fast carrier is adiabatically dragged and only the envelope's quadrupole (at `2Ω`) couples out?* This source-vs-coefficient split is the whole verdict (§4 fork); the lane derives it and lets the substrate decide, but the ontology is surfaced now, not after the run.

---

## §1 — THE KILL-LINE `κ_max` (derived from the banked q1 §2.2 numbers; recomputed, not chat-imported)

**Effective-coupling definition (frozen).** Define `κ` ≡ the effective far-field amplitude coupling of the orbiting envelope-lump's mass moment into the **bulk/compression (P) channel**, normalized so that the EXTRA fractional orbital-energy-loss rate the pulsar over-determines is

$$\frac{\Delta\dot P_b}{\dot P_b}\;=\;\frac{F_{\rm bulk}}{F_{\rm shear}}\;\equiv\;\kappa^2 .$$

(An amplitude coupling appears squared in a radiated-power ratio; this makes `κ²` = the channel-basis flux ratio Leg C measures directly — A46-matching-coordinate.)

**The over-determined-`Ṗ_b` bound (q1 §2.1 `[branch/canon]`).** In a binary pulsar the masses are pinned INDEPENDENTLY by the conservative post-Keplerian parameters; the radiative `Ṗ_b` is then an over-determined consistency check. Any EXTRA radiative fraction is bounded by the fractional agreement `δ`:

$$\kappa^2 \;=\; \frac{F_{\rm bulk}}{F_{\rm shear}} \;\le\; \delta .$$

**The frozen numbers (`[import]`, WebFetch-verified in q1 §2.2; recomputed by this lane's driver from these two figures — NOT from chat arithmetic):**

| Bound | `δ` (frac.) | `κ_max² = δ` | `κ_max = √δ` | Source `[import]` |
|---|---|---|---|---|
| **Double pulsar J0737 (BINDING)** | `1.3×10⁻⁴` | **`1.3×10⁻⁴`** | **`0.0114`** | Kramer et al. 2021, PRX 11, 041050 (arXiv:2112.06795) |
| Hulse-Taylor B1913+16 (cross-check) | `1.6×10⁻³` | `1.6×10⁻³` | `0.0400` | Weisberg & Huang 2016, ApJ 829, 55 (arXiv:1606.02744) |

$$\boxed{\ \kappa_{\max}^2 \;=\; \delta_{\rm DP} \;=\; 1.3\times10^{-4}\,,\qquad \kappa_{\max} \;=\; 0.0114\ \ \text{(double-pulsar, binding)}\ }$$

**Equivalent structural suppression bar (relative to the Reading-A elastic default #761 confirmed radiates).** The Reading-A default flux fraction is `F_A = A_ang·(c_S/c_P)⁵` with `A_ang = 2/3`: `F_A = 0.0329` (P-wave `√(10/3)·c`) / `0.1179` (port `√2·c`); i.e. `κ_A = √F_A = 0.181` (P-wave). To survive `κ_max`, a derived mechanism must suppress the compression coupling **amplitude** by

$$\sigma \;\equiv\; \frac{\kappa_{\rm env}}{\kappa_A} \;\le\; \sqrt{\frac{\delta_{\rm DP}}{F_A}} \;=\; 0.063\ (\sqrt{10/3}\,c)\ \big/\ 0.033\ (\sqrt2\,c),$$

i.e. `σ² ≤ 4.0×10⁻³ / 1.1×10⁻³` (power) — the derived envelope compression coupling must sit **≥ 16–30× below** the elastic default (`≥ 250–900×` in flux). That is the bar bin 2 must clear; it is intentionally hard.

---

## §2 — THE FROZEN BINS + consistency gate + anti-seduction fence

**BIN 1 — ENVELOPE-RADIATES (kill confirmed one level down).** The slow sector carries a gapless compression-class radiative mode that the orbiting-lump couples to, AND the derived `κ_env² > κ_max² = 1.3×10⁻⁴` (equivalently `σ` above the bar) ⇒ the pulsar exclusion holds at the envelope level too. The #761 carrier-level kill is confirmed one level down. *Consequence: the standing Reading-A exclusion stands; the reverted ruling stands reverted. Routed, not executed.*

**BIN 2 — ENVELOPE-SUPPRESSED (Reading-B mechanism DERIVED).** Derived `κ_env² ≤ κ_max²` WITH the mechanism NAMED and DERIVED (parametric/coefficient-class coupling; image-cancellation against the emergent Γ boundary; envelope-sector gap; multipole-order asymmetry; or other) — AND the CONSISTENCY GATE (below) passes. ⇒ Reading B gains its owed derived mechanism. *CONSEQUENCE ROUTED TO GRANT ONLY — this would ground a re-open of the reverted ruling; this lane executes NOTHING (no port-register edit, no un-revert).*

**BIN 3 — FRAMING-FALSIFIED.** The same reduction kills the OBSERVED shear channel too (the suppression mechanism silences BOTH channels, or the envelope framing predicts no far-field GW at all) ⇒ the envelope framing contradicts observed GW ⇒ banked as wrong-level framing; the carrier-level #761 verdict stands untouched.

**BIN 4 — UNDETERMINED.** An unforced verdict-controlling choice in the reduction (ansatz, scale ordering, which channel owns the observed GW, source-vs-coefficient ontology, which Γ the emergent boundary presents to each channel) that is not forced by the substrate ⇒ STOP, state the fork precisely (§4), do NOT pick by fiat.

**★THE CONSISTENCY GATE (frozen).** Any derived suppression MUST leave the observed shear-channel radiation intact at the GR rate (`[import]`-tagged, per q1 §2's banked `Ṗ_b` data: the observed decay IS the GR shear-quadrupole). A mechanism that silences BOTH channels fails into BIN 3, not BIN 2. Operationally: the derived / measured shear coupling must reproduce the GR-rate shear flux to within the same `δ` band it is tested against; if the mechanism drops the shear flux below `(1−δ)×` GR, it is BIN 3. This gate is what makes BIN 2 hard to reach — intentional.

**★ANTI-SEDUCTION FENCE, BOTH WAYS (frozen).** (i) The walk narrative WANTS BIN 2 — it rescues the framework (the seductive direction). (ii) The #761 momentum WANTS BIN 1 — kill-confirmation completes a clean arc (the completion-bias direction). This lane is inside BOTH blast radii. **The verdict section may cite ONLY the frozen criteria's outputs (§1 `κ_max`, §2 bins + gate, §3 leg criteria).** Every other measurement is POST-HOC CHARACTERIZATION, labeled and quarantined from the verdict section. Reverse-seduction check (a make-or-break lane can be seduced by a clean kill OR a clean rescue): the derivation must NAME the mechanism with `clm-`/solidity inline whichever way it lands, and the consistency gate must be independently evaluated.

---

## §3 — FROZEN LEG CRITERIA

### Leg 0 — sign check (compression-channel grade under S(A))
Derive the compression-channel speed/impedance grade under saturation `S(A)`: which constitutive combination softens, and which way the index grades (the soft-mode direction the BH story uses). Cite with claim-ids + solidity. **Frozen deliverable:** the sign of `dc_P/dA` and `dZ_bulk/dA` at the operating point, and whether the saturated lump is a converging (index-up) or diverging (index-down) region for the P-branch. `[canon-read]` anchors: `eq_axiom_4.tex:7` (kernel), the C_eff/ε split (KB CLAUDE.md Ax4 sector-split), `Z_bulk→0 ⇒ Γ_bulk=−1` at the cage (`master-equation.md` sibling / `lattice-extreme-bh-rationality.md`). **No verdict weight** — orients Legs A/B.

### Leg A — analytic reduction (multiple-scales / two-timing)
From the K4/Cosserat elastic Lagrangian with the Ax4 kernel, two-timing: fast carrier at the node resonance `ω₀`, slow envelope `A(x,T)`. **Frozen deliverables:**
1. The envelope evolution equation (NLS-class or other) and its linearized mode content about (a) the cold vacuum (`A=0`) and (b) a saturated lump's tail.
2. Classification: does a compression-class ENVELOPE mode propagate? Gapless? Parabolic (Schrödinger-class) vs hyperbolic (acoustic)? Its dispersion.
3. What a translating/orbiting lump sources: the carrier-band sidebands (`ω₀ ± nΩ` — where do they land?) AND the envelope-band content (at `2Ω`), and the **effective `κ` presented to whichever channel reaches the far field at the orbital frequency**.
4. The multipole order at which the compression couples (monopole `∫∇·u` and dipole `∫x∇·u` constraints from `mass = A1-dilatation` + conservation laws — killed or alive?). If compression starts at a HIGHER multipole order than shear, `κ_env² ∝ (Ω/ω_ref)^{2Δℓ}` is a derived suppression → candidate BIN 2; if same order, `κ_env → ` the q1 `(2/3)(c_S/c_P)⁵` → BIN 1.
**Frozen bin-map:** compression-envelope mode present + orbiting lump couples at same multipole order as shear + `κ_env² > κ_max²` ⇒ BIN 1; a derived same-mechanism suppression of ONLY compression to `κ_env² ≤ κ_max²` ⇒ candidate BIN 2 (pending gate); suppression of BOTH ⇒ BIN 3.

### Leg B — channel asymmetry (feeds the consistency gate)
The same reduction applied to the **T2 shear** channel. **Frozen deliverables:** whether the observed GW is (i) carrier-shear sourced by envelope motion, or (ii) an envelope-texture shear wave; and whether the derived structure is **ASYMMETRIC** (shear radiates at GR rate, compression suppressed) or **SYMMETRIC** (both live / both dead). **Frozen gate-map:** ASYMMETRIC with shear-at-GR-rate + compression-below-`κ_max` ⇒ BIN 2 candidate CONFIRMED by the gate; SYMMETRIC-both-dead ⇒ BIN 3; SYMMETRIC-both-live-above-`κ_max` ⇒ BIN 1.

### Leg C — numerical, saturated regime (FEASIBILITY-ASSESSED; criteria frozen before running)
**Feasibility (assessed, frozen).** A self-consistent saturated soliton is INFEASIBLE (§0 checkpoint 5; electron-lock arc). **FALLBACK (declared, scoped):** impose a pinned SATURATED bias texture `A(r) = A₀·exp(−r²/2σ_s²)` (`A₀ = 0.5·A_yield`, saturation ON in the core), and drive its collective coordinate on a slow oscillating/orbiting trajectory `X(t)`; measure the COLD far-field carrier-band radiation partition. **This fallback tests the COEFFICIENT-coupling question (does a slowly-moving saturated operating-point texture radiate compression, and at what `κ`), NOT envelope self-consistency.** The verdict is scoped accordingly: Leg C can confirm/refute the coefficient-coupling half of the §4 fork; it cannot certify a self-bound envelope.

**Discriminator design (frozen).** Two source models on the SAME shipped srs net, SAME driven frequency, SAME multipole content:
- **Model S (source-on-RHS, #761 replica):** a cold breathing pulse (∂ₜ amplitude oscillating). Expected `f_long ≈ 0.98` (reproduces #761 — a positive control that the pipeline sees compression).
- **Model C (coefficient, the envelope test):** a saturated (Op14-ON) rigid bias texture translated/oscillated on `X(t)`; measure `f_long` and `κ_env² = F_∥/F_⊥`.

**Frozen observables + tolerances:**
- `f_long = E_∥/(E_∥+E_⊥)` and `κ_env² = F_∥/F_⊥`, energy-integrated over the reflection-free Poincaré window.
- **Window mechanics FROZEN from SPECTRAL speeds (the #761 R2 lesson — NEVER front-detect from energy crossings):** window `[t_P, t_reflect)` with `t_P = r_meas/c_P`, `t_reflect = (2·L/2 − r_meas)/c_P`, `t_S = r_meas/c_S`, all at the C-2 spectral `c_P`, `c_S` (isotropic Bloch long-wave). Report `t_S` inside the window.
- **Multipole-order check (frozen):** measure `F_∥` and `F_⊥` at ≥2 driven frequencies `Ω` and fit the power-law exponent of each; if the P and S channels share the same `Ω`-scaling exponent, `κ_env² = F_∥/F_⊥` is `Ω`-independent (structural) and directly comparable to `κ_max²`; if the exponents DIFFER by `2Δℓ`, that is itself the derived asymmetry (report `Δℓ`).
- **Grid FROZEN:** `L = 20` supercell (`64000` sites), `r_meas = 6` cells, `dt = 0.2·dt_CFL`, seed/texture `∇×u = 0` by construction (report the seed transverse fraction), energy-drift `|ΔH/H|` reported (bounded-Verlet, ≤ ~1% precedent).
- **Frozen bin-map:** Model C `κ_env² > κ_max² = 1.3×10⁻⁴` (finite-size correction disclosed) AND same-multipole-order as shear ⇒ supports BIN 1. Model C `κ_env² ≤ κ_max²` via a resolved higher-multipole-order suppression (`Δℓ ≥ 1`) WITH the S-channel resolvable above the drift floor ⇒ supports BIN 2 (pending Leg-B gate). Both channels below the resolvable drift floor ⇒ finite-size scope caveat, fall back to the Leg-A/B analytic verdict (declared).
- **Determinism (frozen):** fixed seed; reruns bit-identical.

---

## §4 — THE UNDETERMINED FORK GUARD (state precisely; do NOT pick by fiat)

The verdict-controlling unforced choice this lane must watch (BIN 4 if the substrate does not force it):

**Fork F1 — source vs coefficient (the pre-test-physics question).** Is the orbiting star on the **RHS** of the carrier wave equation (a forcing source term at some frequency ⇒ power-law radiation, #761 picture ⇒ BIN 1) or in its **COEFFICIENTS** (a slowly-varying operating-point/index the envelope-soliton adiabatically follows ⇒ radiation suppressed by the scale separation `Ω/ω_e ~ 10⁻²⁴` ⇒ candidate BIN 2)? **Frozen resolution rule:** the reduction FORCES one iff the multiple-scales expansion places the external field unambiguously on the RHS or in the coefficients at leading order; if both orderings are self-consistent and give different bins, that is BIN 4 (state the fork; do not pick).

**Fork F2 — which Γ does the emergent boundary present to each channel (Grant's image-cancellation walk).** If the saturated lump has an emergent Γ boundary (the fully-saturated shell), is it `Γ=−1` (pressure-release/soft) for the P-branch AND for the S-branch (⇒ both image-cancelled ⇒ BIN 3), or `Γ=−1` for compression but a DIFFERENT sign/magnitude for shear (⇒ asymmetric image-cancellation ⇒ candidate BIN 2), or `Γ=0` (Z-preserving, no cancellation ⇒ BIN 1)? **Frozen resolution rule:** derive `Γ_bulk` and `Γ_shear` at the saturated shell from the constitutive `Z_bulk(S)`, `Z_shear(S)` grades (Leg 0); if the substrate forces distinct signs, the asymmetry is derived; if the sign is an unforced modeling choice, BIN 4.

**Fork F3 — multipole order of the compression coupling (Leg A deliverable 4).** Whether `mass = A1-dilatation` + conservation laws kill the compression monopole AND dipole (⇒ compression starts at quadrupole, same as shear ⇒ q1 ratio ⇒ BIN 1) or leave a lower-order compression moment alive (⇒ ENHANCED compression ⇒ BIN 1 reinforced) or force a higher-order start (⇒ suppressed ⇒ BIN 2). This is DERIVED, not chosen — but if the derivation is ambiguous, BIN 4.

---

## §5 — Calibration-vs-derived ledger (tags frozen) + owed follow-ons fence

**Ledger tags (`consistency-vs-emergence`, frozen).** `κ_max` is `[derived]` from `[import]` pulsar `δ` (MANIFESTATION given the imports). The envelope equation FORM is `[derived]` (theorem of the multiple-scales reduction). Any speed/modulus VALUE (`c_P/c_S`, `K=2G`) is CONSISTENCY-class (GR-imported, PR#261) — no emergence-class claim headlined. The Leg-C partition is `[derived]` (lattice-measured, dimensionless). The deliverable is the frozen-bin verdict + `κ_env` vs `κ_max`, riding on the derived reduction + lattice measurement, not a hidden calibration.

**Owed follow-ons (fenced; NOT executed here — Rule 12; slot NOT refilled with an assertion).**
1. If BIN 2: the mechanism becomes a NEW derivation with its own version + verification chain; the re-open of the reverted Q1 ruling is Grant's alone; the auditor lands any port-register/ledger edit. This lane executes none.
2. If BIN 1: the standing Reading-A exclusion + reverted ruling stand; no edit owed (already banked by #761's routed consequence).
3. If BIN 3: banked as wrong-level framing; the #761 carrier verdict stands; no rescue derivation is minted (honest closure).
4. If BIN 4: the fork is stated; corpus + Grant consulted before any methodology pivot (Rule 16); no fiat pick.

---

> **Pre-registration provenance.** Fired by Grant 2026-07-20 (`"fire the lane"` `[sic]`). This is COMMIT 1 — the prereg ALONE, frozen and pushed before any derivation or driver (the #761 frozen-first discipline). All `[canon]` citations content-verified two-method at base HEAD `f84b622b` (verify-before-cite); `[branch @ d17a2248]` for #761; pulsar figures `[import]`. Kill-line `κ_max = 0.0114` (`κ_max² = 1.3×10⁻⁴`, double-pulsar binding) recomputed from the banked q1 §2.2 numbers by this lane's driver, not chat. Mints no `clm-`; propagates to no leaf; engine byte-untouched; port-register untouched regardless of outcome. Companions: `[branch:#761 @ d17a2248]` (`research/2026-07-20_mechanical-commonmode-derivation_result.md`), the Q1 hardening (`research/2026-07-20_q1-pulsar-hardening.md`), the port register (`manuscript/ave-kb/common/port-register.md` Q1 row), and the docket continuation (`### ENTRY 2026-07-20-envelope-sector`).
