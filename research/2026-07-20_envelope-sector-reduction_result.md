# Envelope-Sector Reduction — RESULT (the frozen-bin verdict; slow dynamics of the saturable lattice; the gravitational-band coupling κ)

**Date:** 2026-07-20
**Class:** DERIVATION + lattice-derived research-driver (research-doc; **forms derived, values calibration/observation-imported and tagged; mints no `clm-`, propagates to no KB/tex leaf**). Resolves the frozen bins of the pre-registration (`research/2026-07-20_envelope-sector-reduction_prereg-FROZEN.md`).
**Provenance:** Grant-fired 2026-07-20 (`"fire the lane"` `[sic]`). The forward derivation following the #761 NONE-DERIVES carrier-level verdict (`[branch:#761 @ d17a2248]`). Frozen prereg committed + pushed ALONE first (`e27cc5e0`); analytic Legs 0/A/B in `research/2026-07-20_envelope-sector-reduction_derivation.md` (`b25fb9d5`); Leg-C driver `research/drivers/envelope_sector_orbiting_lump.py` (+ `_results.json`, white figure), `ave.core.*` read-only, engine BYTE-UNTOUCHED.
**Lane fences:** DERIVATION lane only. Engine byte-untouched; **no** `manuscript/`/`ave-kb/` leaf edits; **no** port-register edit; **no** un-revert; **no** falsification-ledger edit — regardless of outcome (held). Every `[canon]` input content-verified two-method at base HEAD `f84b622b`; `[branch @ d17a2248]` for #761; pulsar figures `[import]`.

> **★FROZEN-BIN VERDICT: BIN 1 — ENVELOPE-RADIATES (the pulsar kill is confirmed one level down), with the mechanism DERIVED and NAMED.** The mass = the ENVELOPE of the A1 breather; but the envelope reframe does NOT rescue Reading B — it confirms the #761 carrier-level kill at the slow-sector level, and explains *why* the suppression Reading-B always owed cannot exist. The frozen criteria's outputs:
>
> - **`κ_max² = δ_DP = 1.3×10⁻⁴`, `κ_max = 0.0114`** (double-pulsar binding; §1 of the prereg, recomputed from the banked q1 §2.2 numbers).
> - **Derived far-field structural coupling `κ_env² = A_ang(c_S/c_P)⁵ = 0.034`** (Leg A analytic = the q1 value, UNSHIFTED by the envelope reframe; Leg C finite-size-free spectral color-check reproduces `0.034` at the lattice `c_P/c_S = 1.813`). `κ_env²/κ_max² = 262` — **the compression port is open at `262×` the double-pulsar bound** (`κ_env = 0.184 = 16× κ_max`).
> - **Mechanism (derived, two-part).** (i) *Gaplessness defeats the adiabatic hope (Leg A / Fork F1):* the orbital-band radiation is the mass-quadrupole ponderomotive coupling of `|A|²` into the **gapless** P-branch (#761 `clm-bnd5rq` 0.8); the scale separation `Ω/ω₀ ~ 10⁻²⁴` suppresses only the *carrier* band (at `ω₀`, gapped), never the gapless acoustic channel at `2Ω`. (ii) *`K=2G` grade-locking forbids a channel asymmetry (Legs 0/B / Fork F2):* the mechanical bulk and shear channels grade together under `S(A)` (`Γ_shear=Γ_bulk=−1` at the wall, `lattice-extreme-bh-rationality.md:37` `[canon]`) and the `c_P/c_S` RATIO is saturation-invariant (degree-0, `electron-bh-isomorphism.md:38`/PR#521 `[canon]`), so every candidate suppression is channel-symmetric ⇒ silencing compression silences the observed GW too. (iii) *`mass=A1-dilatation` fixes the multipole order (Fork F3):* the compression monopole (`Ṁ=0`) and dipole (`Ẍ_cm=0`) are killed, so compression starts at quadrupole — SAME order as shear — with `Δℓ=0` (no `(Ω/ω_ref)^{2Δℓ}` suppression).
> - **★CONSISTENCY GATE: PASS (and it is what forecloses BIN 2).** The observed T2-shear (GW) radiates at the GR rate (gapless, quadrupole; Leg C far-field is shear-dominated, `f_long → 0.033`-continuum trend). Every mechanism that would suppress compression is channel-symmetric on the mechanical sector, so it would suppress shear too (→ BIN 3, forbidden by observation). BIN 2 is therefore **structurally unreachable** — exactly as the gate intended.
> - **Leg C empirical anchor (the genuinely NEW content beyond #761): SATURATION-INVARIANCE.** An orbiting SATURATED (Op14-ON, `A₀=0.5`) mass-texture radiates compression IDENTICALLY to the cold case (cold vs saturated agree to `<0.2%` at both drive frequencies: `f_long = 0.762` cold / `0.762` sat at `Ω=0.15`; `0.628`/`0.629` at `Ω=0.30`; `κ²` ratio `0.997`). The coefficient/envelope reframe changes NOTHING about the partition — confirming the degree-0 frozen-ratio (Leg 0) empirically.
>
> **CONSEQUENCE (unchanged from #761, one level deeper): the standing Reading-A exclusion + the reverted Q1 ruling STAND.** The envelope framing is NOT falsified (shear survives; NOT BIN 3), and no derived suppression exists (NOT BIN 2). This is a clean, bankable NEGATIVE (Rule 11 honest closure): the discipline working at full strength — the envelope reframe was the last structural place a Reading-B suppression could have lived, and the derivation shows it cannot. **Routed to Grant/auditor; NOT executed here** (READ-ONLY fence held).

---

## §0 — REGIME / SECTOR / PHASE-STATE header (fired before the integration)

**MODE.** Non-relativistic compact binary (HT B1913+16, J0737-3039A/B) as a source; contrast = observed `Ṗ_b` matched to GR shear-quadrupole `[import]`. **REGIME.** Regime-I cold-linear far field; SATURATED source (Op14 ON in the lump; `A₀=0.5·A_yield`). **PHASE-STATE.** Cold-reactive far field, saturated core. **SECTOR.** Under test = A1 bulk/compression (P-branch, `c_P/c_S≈1.71–1.90`); observed GW = T2 shear. **A46 coordinate:** longitudinal (radial, `∇·u`) vs transverse (tangential, `∇×u`) radiated-energy partition; `κ² = F_bulk/F_shear` in that channel basis — matching the corpus channel-radiation claim, not a `φ²` proxy.

---

## §1 — LEG 0 (sign check) — the compression channel grades WITH shear, ratio frozen `[canon-read + derived]`

Full derivation in `..._derivation.md §1`. Outputs: `dc_P/dA < 0` (softens, index up, converging region); `Z_bulk = ρc_P ∝ √S → 0` ⇒ `Γ_bulk → −1`, **together** with `Γ_shear → −1` (`lattice-extreme-bh-rationality.md:37` `[canon]`, verbatim *"`Γ=−1` reflection is **shear + bulk** (`G_shear→0`, `c_bulk→0`, `Γ_shear=Γ_bulk=−1`) while EM stays matched"*). The **dimensionless `c_P/c_S` ratio is FROZEN** under saturation magnitude (`electron-bh-isomorphism.md:38`/PR#521 `[canon]`: `ν`, Zener, `K/G` are *"homogeneous degree-0 in the bond stiffnesses … unshifted by saturation magnitude"*). ⇒ the compression/shear partition `κ² = A_ang(c_S/c_P)⁵` does NOT shift with saturation depth. This pre-resolves Fork F2 (mechanical channels grade-locked ⇒ symmetric) and Fork F3-ratio (saturation-invariant), and it is EMPIRICALLY confirmed by Leg C (§4, cold≈saturated).

---

## §2 — LEG A (multiple-scales) — the orbital band couples to the gapless P-branch at quadrupole order `[derived]`

Full derivation in `..._derivation.md §2`. Outputs:
- The carrier envelope obeys an **NLS-class** (parabolic/Schrödinger) equation about the cold vacuum — the carrier band sits at `ω₀ ± nΩ` (node scale), gapped, adiabatically suppressed by `ε = Ω/ω₀ ~ 10⁻²⁴`. **The envelope's own band offers no new low-frequency radiative channel.**
- The far-field radiation at `2Ω` is the **ponderomotive back-reaction** of the carrier intensity `|A|²` (= the mass-energy density, `master-equation.md:20` `[canon]`) onto the low-frequency acoustic field, sourced by the mass quadrupole `Q_ij ∝ ∫x_ix_j|A|²`. **Fork F1 resolved:** whether `|A|²` is a *source* (RHS) or a *coefficient* (the moving well the envelope rides), the far-field object is the same mass quadrupole at `2Ω`; the adiabatic suppression protects only the gapped carrier band, NOT the **gapless** P-branch (#761). *The #761 gaplessness result is exactly what defeats the envelope framing's suppression hope.*
- **Fork F3 resolved by `mass=A1-dilatation`:** compression monopole `∫∇·u ∝ M` (`Ṁ=0`, dead), dipole `∫x∇·u ∝ MX_cm` (`Ẍ_cm=0`, dead), quadrupole `∫x_ix_j∇·u = Q_ij` (`⃛Q^{TL}≠0`, radiates). Compression starts at quadrupole — SAME order as shear — `Δℓ=0`. ⇒ `κ_env² = A_ang(c_S/c_P)⁵ = (2/3)(c_S/c_P)⁵`, the q1 value, unshifted by the envelope reframe.

---

## §3 — LEG B (channel asymmetry) — SYMMETRIC; the consistency gate forecloses BIN 2 `[derived]`

Full derivation in `..._derivation.md §3`. Outputs: the observed GW is carrier-shear sourced by the mass quadrupole's traceless part at `2Ω` — a **gapless** acoustic branch ⇒ **radiates at the GR rate ⇒ consistency gate PASS for shear.** The derived structure is **SYMMETRIC**: the two mechanical channels are grade-locked (Leg 0), so every candidate suppression (adiabatic gap / emergent `Γ=−1` shell / `√S` softening) is channel-symmetric on the mechanical sector and CANNOT suppress compression without suppressing shear (→ BIN 3, forbidden by observation). The only asymmetric channel is EM (`Γ_EM=0`), which gravity does not use (sector-ownership). **BIN 2 is structurally unreachable** — the envelope-level analog of #761's "structurally BLOCKED."

### §3.1 — ★Adjudication of the walk's image-cancellation (Lloyd-mirror) BIN-2 candidate `[derived]`
The Grant-led envelope-boundary walk RECORD (`research/2026-07-20_envelope-boundary-walk_RECORD.md` §6-3, merged to `origin/main` #765 concurrent with this lane) names **image-cancellation** as the "candidate mechanism for the envelope lane's bin-2 route": a compression source against its own `Γ=−1` boundary has its long-wavelength radiative moment cancelled by its inverted image (Lloyd-mirror class), residuals suppressed by `(k·r_core)²`, while the static texture `∝ M` is untouched. The RECORD routes this to this lane; this lane REFUTES it as a BIN-2 route, TWO independent ways:

1. **The `Γ=−1` boundary is channel-SYMMETRIC (Leg 0 / F2).** `lattice-extreme-bh-rationality.md:37` `[canon]`: the saturated wall is `Γ_shear=Γ_bulk=−1` — the SAME sign for BOTH mechanical channels. So IF an image-cancellation suppressed the compression quadrupole by `(k·r_core)²`, it would suppress the **shear** quadrupole by the SAME factor ⇒ the observed GW would vanish (→ BIN 3, contradicting observation). Image-cancellation cannot selectively silence compression; it is symmetric ⇒ either both cancelled (BIN 3, falsified by observed GW) or both radiate (BIN 1).

2. **★The actual pulsar sources are NEUTRON STARS, which have NO `Γ=−1` shell (the decisive, source-specific refutation).** The `Γ=−1` mirror requires a FULLY-saturated contour `A = A_yield` (`S=0`); this forms only at the BH saturation radius `r_sat = 7GM/c²` (`lattice-extreme-bh-rationality.md:77` `[canon]`). Hulse-Taylor and J0737 are **neutron-star** binaries with surface compactness `2GM/rc² ~ 0.35` ⇒ vacuum operating point `A₀ ~ 0.6–0.8 < A_yield=1` — **sub-yield, no `S=0` contour, NO `Γ=−1` mirror exists at the source.** With no mirror there is no image to cancel against; the mass quadrupole radiates freely into BOTH gapless acoustic branches at the q1 partition. **The image-cancellation candidate does not apply to the systems the kill-line is measured on.** (It could only ever engage for a fully-saturated BH source — where `Γ=−1` is symmetric anyway, refutation 1.)

**Both refutations are independent and both point to BIN 1.** The walk's strongest BIN-2 candidate is refuted with canon, not hand-waved — the mandate to let the derivation refute any walk candidate, discharged.

---

## §4 — LEG C (numerical, saturated regime) — the coefficient-coupling test

Driver: `research/drivers/envelope_sector_orbiting_lump.py` (+ `_results.json`, white figure). Engine byte-untouched (Rule-14 reuse of the #761/`srs_band_survey` rank-2 bond model + derived `ρ*=9.77337`). **FALLBACK scope (declared in prereg §3, held):** a self-bound saturated soliton is INFEASIBLE (electron-lock arc); this tests the COEFFICIENT-coupling question — a driven/pinned saturated dilatation texture in a dipole-free rotating BINARY, translated through the lattice — NOT envelope self-consistency.

### §4.1 — the three frozen measurements
- **Model S — BREATHING control (positive control).** A single fixed core with oscillating amplitude (the #761 source class). `f_long = 0.993` — reproduces #761's ≈98–99% longitudinal (the pipeline correctly sees a compression source). Control PASS.
- **Model C — ORBITING binary (the envelope test), cold AND saturated.** Two counter-placed dilatation textures rotating at `Ω` (quadrupole at `2Ω`, dipole-free). Measured at the `r_meas=6` shell:

  | drive `Ω` | `λ_P(2Ω)` (cells) | `f_long` cold | `f_long` sat | `κ²=F∥/F⊥` cold | `κ²` sat |
  |---|---|---|---|---|---|
  | `0.15` | `10.9` | `0.7624` | `0.7618` | `3.209` | `3.197` |
  | `0.30` | `5.4` | `0.6275` | `0.6288` | `1.684` | `1.694` |

  **★Saturation-invariance (the decisive, finite-size-INDEPENDENT result):** cold vs saturated agree to `<0.2%` at both `Ω` (`κ²` ratio `0.997`). The moving saturated operating-point texture radiates compression IDENTICALLY to cold — the coefficient/envelope reframe changes nothing, confirming Leg 0's degree-0 frozen-ratio empirically.
- **Spectral C-2 (finite-size-FREE anchor; #761-parity).** From the cold Bloch `D(k)`: `c_P/c_S = 1.813` isotropic, direction-resolved `[100]1.711 / [110]1.855 / [111]1.904` — reproduces the survey (self-consistency PASS). The far-field structural partition (continuum multipole formula at the lattice speeds) `F_bulk/F_shear = (2/3)(c_S/c_P)⁵ = 0.034` — matches q1's `0.0329` and #761's `0.033`; `≫ κ_max² = 1.3×10⁻⁴` (`262×`).

### §4.2 — finite-size honesty (declared fallback invoked)
The time-domain `r_meas=6` shell is in the **near/intermediate zone** for the orbiting quadrupole (`λ_P(2Ω) = 5.4–10.9` cells `≳ r_meas=6`), so the absolute `f_long`/`κ²` there is **compression-enriched by the moving dilatation-texture's own near field** (a pure-`∇·u` source is radially dominated in the near zone). This is confirmed by (i) the sub-quadrupole `Ω`-scaling exponents (`n_∥=0.86`, `n_⊥=1.79`; a clean far-field quadrupole would give `≈6`) and (ii) the **physical near→far trend**: as `Ω` doubles (`λ_P` shrinks below `r_meas`), `f_long` DECREASES (`0.762 → 0.628`), the transverse/shear content growing toward the far field — trending to the continuum shear-dominated `f_long = 0.033`. **Per the frozen prereg's declared finite-size fallback, the absolute near-zone `κ²=3.2` is QUARANTINED from the verdict (post-hoc characterization); the verdict rests on the finite-size-FREE spectral color-check (`0.034`), the robust saturation-invariance ratio, and the Leg-A/B analytic.** The `L=20`, `r_meas=6`, `dt=0.2·dt_CFL` grid ran as frozen; NO grid deviation. Determinism: reruns bit-identical.

---

## §5 — FROZEN-BIN VERDICT + consistency gate + anti-seduction fence check

| Leg | Frozen outcome | Decisive step |
|---|---|---|
| **0 — sign** | compression grades WITH shear (`Γ_shear=Γ_bulk=−1`); `c_P/c_S` ratio FROZEN (degree-0) | forecloses BIN-2-via-F2; saturation does not shift the partition (canon `:37`, `:38`/PR#521) |
| **A — reduction** | orbital band = mass-quadrupole coupling into the GAPLESS P-branch; `Δℓ=0` | gaplessness defeats the adiabatic hope (F1); `mass=A1` kills monopole+dipole (F3); `κ_env²=(2/3)(c_S/c_P)⁵` |
| **B — asymmetry** | SYMMETRIC; shear survives at GR rate; BIN 2 structurally unreachable | every mechanical suppression is channel-symmetric ⇒ silences shear too (→ BIN 3, forbidden) |
| **C — numerical** | orbiting saturated texture RADIATES compression; cold≈saturated (`<0.2%`); spectral `κ_env²=0.034 ≫ κ_max²` | saturation-invariance (Leg-0 confirmed); `c_P/c_S` gate PASS; near-zone `κ²` quarantined (finite-size) |

**Overall frozen-bin verdict: BIN 1 (ENVELOPE-RADIATES).** `κ_env² = 0.034 > κ_max² = 1.3×10⁻⁴` (by `262×`); the compression channel is a gapless port the orbiting mass-quadrupole couples to at the q1 coupling, and no derived channel-asymmetric suppression exists (the mechanical sector is grade-locked). **BIN 2 is structurally unreachable, NOT merely un-derived** — this is the envelope-level analog of #761's structural block.

**★Consistency gate: PASS.** The observed T2-shear (GW) radiates at the GR rate (gapless, quadrupole; the far-field is shear-dominated). The framing is NOT falsified (shear lives ⇒ NOT BIN 3), and the suppression that BIN 2 needs is exactly the thing the gate forbids (it would kill shear too).

**★Anti-seduction fence check (both ways, per the frozen prereg).** (i) The walk narrative WANTED BIN 2 (rescue); the derivation returns BIN 1 — the seductive direction is NOT taken. (ii) The #761 momentum WANTED BIN 1 (kill-completion); this is the returned bin, so the completion-bias must be explicitly guarded: the verdict cites ONLY the frozen criteria's outputs (`κ_max²` §1; the far-field-structural `κ_env²=0.034` finite-size-free; the saturation-invariance ratio; the Legs-0/A/B analytic). The near-zone time-domain `κ²=3.2` — which would OVERSTATE the compression dominance — is QUARANTINED as post-hoc finite-size characterization, NOT used to headline the exceedance. The verdict's `262×` uses the conservative finite-size-free `0.034`, not the near-zone value. Reverse-seduction (a make-or-break lane seduced by a clean kill): the mechanism is NAMED with `clm`/solidity inline (gaplessness — `clm-bnd5rq` 0.8; grade-locking — `lattice-extreme-bh-rationality.md:37`/`electron-bh-isomorphism.md:38` PR#521; multipole — `master-equation.md:20`), and the consistency gate is independently evaluated (shear survives).

**Contradiction with the standing ruling (flag-don't-fix).** Grant's Q1 ruling was RULED-CONDITIONAL Reading-B; #761 already returned NONE-DERIVES at the carrier level, reverting it. This lane confirms the revert one level down (the envelope reframe does not rescue it). **Both surfaced with file:paths + verbatim content; neither reframed.** Grant adjudicates; the auditor lands any port-register/ledger edit. This lane touched NO KB/tex leaf (fence held).

---

## §6 — Calibration-vs-derived ledger + owed follow-ons

### §6.1 — Ledger (`consistency-vs-emergence` tags)
| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| `κ_max² = δ_DP = 1.3×10⁻⁴`, `κ_max = 0.0114` | `[derived]` `=√δ` | `[import]` (Kramer 2021 `δ_DP`) | manifestation given import (the kill-line) |
| `c_P/c_S` ratio frozen under saturation (degree-0) | `[canon-read]` (`electron-bh-isomorphism.md:38`/PR#521) | `1.813` dimensionless | CONSISTENCY (`K=2G` GR-imported) |
| `Γ_shear=Γ_bulk=−1` at the wall (grade-locked) | `[canon-read]` (`lattice-extreme-bh-rationality.md:37`) | — | the structural block on BIN 2 |
| carrier band parabolic (gapped); orbital band = ponderomotive coupling into the gapless P-branch | `[derived]` (multiple-scales) + `[canon-read]` (#761 gaplessness `clm-bnd5rq` 0.8) | — | manifestation — Fork F1 resolved |
| compression monopole+dipole killed (`Ṁ=0`, `Ẍ_cm=0`); quadrupole radiates | `[derived]` + `[canon-read]` (`mass=A1`, `master-equation.md:20`) | `Δℓ=0` | manifestation — Fork F3 resolved |
| `κ_env² = (2/3)(c_S/c_P)⁵` | `[derived]` = q1 value; Leg-C spectral color-check | `0.034` dimensionless | the far-field structural coupling |
| Leg-C saturation-invariance (cold≈sat) | `[derived]` (lattice driver; ratio, finite-size-free) | `<0.2%` diff | manifestation — Leg-0 confirmed |
| Leg-C near-zone `κ²=3.2` | `[derived]` (lattice, near-zone) | `3.2` | QUARANTINED — finite-size characterization, not a verdict input |
| pulsar exclusion (banked) | — | `[import]` (Weisberg-Huang 2016; Kramer 2021) | import (banked, #761/q1) |

No emergence-class claim headlined. The deliverable is the frozen-bin verdict (BIN 1) + `κ_env² = 0.034` vs `κ_max² = 1.3×10⁻⁴`, riding on the derived reduction + the finite-size-free lattice measurement.

### §6.2 — Owed follow-ons (fenced; NOT executed here — Rule 12; slot NOT refilled)
1. **NO rescue derivation for Reading B** — per honest closure (Rule 11) + substitution-not-retraction (Rule 12), the BIN-1 branch is closed; the slot is not refilled. Any future closure must overcome BOTH structural blocks (gaplessness of the compression channel + `K=2G` grade-locking of the mechanical sector) and gets a new version + its own verification chain.
2. **The Q1 revert + falsification-ledger promotion** were already routed by #761 (NONE-DERIVES); this lane's BIN-1 confirms the same consequence one level deeper. *Grant-gated; auditor lands the port-register/ledger edit; this lane surfaces, does not land.*
3. **The `master-equation.md:20` sector-ownership wording tightening** (routed by #761 §6.2-2) — unchanged; this lane relied on the physical (acoustic compression) identification, which stands.
4. **NOT owed:** a finite-size-free time-domain far-field κ measurement — the spectral C-2 color-check + the analytic Leg A already give the far-field structural partition; a bigger-box time-domain far-field run is a nice-to-have, verdict-neutral (the near-zone quarantine already handles the finite-size honesty).

---

> **Corpus-state note (2026-07-20).** Base HEAD `f84b622b`. `origin/main` advanced to `60b30b4b` during this lane: **#761 MERGED** (PR #761; the mechanical-commonmode NONE-DERIVES is now on main — cited here as `[branch @ d17a2248]`, the identical merged branch head), and the **Grant-led envelope-boundary walk RECORD landed** (`research/2026-07-20_envelope-boundary-walk_RECORD.md`, PR #765), which explicitly names THIS lane as the adjudicator of its walk candidates ("the lane's frozen-bin result wins") and routes its image-cancellation candidate here (adjudicated §3.1). My branch's merge-base is `f84b622b`; my changes are purely additive (research docs + docket append); no rebase needed for the DO-NOT-MERGE PR. The RECORD is RECORD-class canon I did not edit (fence held).
>
> **Result-doc provenance.** Fired by Grant 2026-07-20 (`"fire the lane"` `[sic]`). Frozen prereg committed + pushed ALONE first (`e27cc5e0`); analytic Legs 0/A/B (`b25fb9d5`); Leg-C driver reproduced by `research/drivers/envelope_sector_orbiting_lump.py` (+ `_results.json`, white figure), `ave.core.*` read-only, engine byte-untouched, reruns bit-identical. All `[canon]` citations content-verified two-method at base `f84b622b`; #761 `[branch @ d17a2248]`; pulsar figures `[import]`. FORMs `[derived]` by multiple-scales + multipole/conservation algebra; the far-field partition is the finite-size-free spectral color-check + the analytic q1 value; the Leg-C saturation-invariance is lattice-measured. Mints no `clm-`; propagates to no leaf; READ-ONLY on KB; port-register untouched. **Verdict: BIN 1 — ENVELOPE-RADIATES. `κ_env² = 0.034 > κ_max² = 1.3×10⁻⁴` (262×); the envelope reframe confirms the #761 carrier-level kill one level down and DERIVES why the Reading-B suppression cannot exist — the compression channel is gapless (no adiabatic gap for the orbital band) and the mechanical bulk/shear channels are `K=2G` grade-locked (no channel-asymmetric structure for a compression-only suppression; the consistency gate forecloses BIN 2). A clean, bankable NEGATIVE (Rule 11). Consequence routed to Grant/auditor; no leaf touched.** Companions: the frozen prereg (`_prereg-FROZEN.md`), the analytic legs (`_derivation.md`), `[branch:#761 @ d17a2248]`, the q1 hardening (`research/2026-07-20_q1-pulsar-hardening.md`), the port register Q1 row, and the docket continuation (`### ENTRY 2026-07-20-envelope-sector`).
