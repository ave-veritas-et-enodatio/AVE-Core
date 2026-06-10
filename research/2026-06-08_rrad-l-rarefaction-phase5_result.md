# Result — counter-propagating opposite-handed chiral pair / rarefaction vacuum-pump drive (dark-wake thrust, Phase 5, the suction half)

**Date**: 2026-06-09
**Branch**: `analysis/2026-06-08-rrad-l-darkwake` (Phase 5; same branch as Phases 1–4)
**Prereg**: [`2026-06-08_rrad-l-rarefaction-phase5_prereg.md`](2026-06-08_rrad-l-rarefaction-phase5_prereg.md)
**Driver**: [`src/scripts/vol_4_engineering/rrad_l_counterprop_chiral.py`](../src/scripts/vol_4_engineering/rrad_l_counterprop_chiral.py)
**Phase-4 result (the negative this continues)**: [`2026-06-08_rrad-l-phased-array-phase4_result.md`](2026-06-08_rrad-l-phased-array-phase4_result.md) (OUTCOME B, all sectors; missing ingredient = a TEMPORAL symmetry-breaker)
**Canonical leaves**: [pair-production-axiom-derivation.md:51,77,96](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) (counteracting chirality → sideways shatter → contra-rotating LH+RH dipoles; pair-tear at A²=1) · [04_chiral_impedance_matching.tex:11](../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_chiral_impedance_matching.tex) (Polarization-Mismatch knob) · [04_superluminal_transit.tex:86](../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_superluminal_transit.tex) (rarefaction relation `c_eff² = c₀²(1 + ρ̄/(1−ρ̄²))`)

> 🟠 **2026-06-09 REGIME-RESCOPE (Rule 12 — header-only addition; every line of the body below is PRESERVED VERBATIM).**
> **Governing discipline:** `ave-regime-phase-state-check`. **Adjudication:** Grant, 2026-06-09 (regime / phase-state discipline).
>
> **(a) This OUTCOME-B is a SUB-YIELD-LINEAR SHEAR/CHIRAL-ω regime null = a WRONG-REGIME ARTIFACT, not a falsification.** Rate-asymmetry / rectification can live ONLY in the BULK NEAR-YIELD (ruptured) regime. This driver runs counter-propagating opposite-handed chiral-ω drives deep sub-yield (A²_focal = 0.05 ≪ 1, §3) — the sub-yield-linear regime — where the Axiom-4 kernel is instantaneous and even-in-A (achromatic + reversible → ∮ = 0 *by construction*). A null in a regime that forbids the effect is uninformative as a falsification (`ave-regime-phase-state-check`: a null where the effect cannot exist is an artifact, not a falsification).
>
> **(b) The rectification question WAS subsequently closed in the correct (bulk near-yield) regime — by derivation.** Branch `analysis/2026-06-09-thixotropy-bulk-derivation` (2026-06-09, tip `5969bda1`; UNMERGED — cited by branch + date, not a HEAD path), **Outcome B**: the bulk relaxation time τ_bulk(ρ̄) = τ₀/√(1+ρ̄/(1−ρ̄²)) depends on the INSTANTANEOUS ρ̄ ONLY — no sign(dρ̄/dt) memory — so the bulk sat/desat channel has NO rate-asymmetry and cannot rectify a symmetric cyclic drive (dead-by-derivation; clm-7tynm2 walk-back upgrades from empirical → STRUCTURAL for the bulk channel). The "temporal symmetry-breaker" this doc flags as the one open door (§7 FLAG) is exactly what that derivation tests — and finds structurally absent in the bulk channel.
>
> **(c) The in-doc mechanism finding REMAINS CORRECT.** The structural symmetric-null (equal-amplitude opposite-handed pair → linear standing polarization → zero injected helicity) + chiral-vs-push (|J_chiral|/|push| = 0.73 < 1) diagnosis below is still the right EXPLANATION of WHY this regime nulls. The rescope is of the FALSIFICATION-STRENGTH interpretation, **not** the mechanics. The substrate-derived cavitation floor ρ̄_cav = −1/φ ≈ −0.618 (§2.1) and the mundane-suction finding are UNAFFECTED.
>
> **(d) Read all "DEAD too" / "deflated across the full dipole" / "refuted across the full dipole"-strength language in this doc as REGIME-SCOPED per this header.** These sub-yield nulls do NOT themselves carry a regime-independent falsification; the conclusion that the exotic *mechanical-rectification* (warp) route is unsupported SURVIVES, but its load-bearing basis is the bulk-near-yield derivation in (b), NOT these artifacts. Specific phrases swept (preserved verbatim in-body): the HEADLINE "the counteracting-chirality / rarefaction route is **DEAD too**"; §6 "now deflated across the **full dipole**" and "Both halves, both sectors, the latch route AND the counteraction route — all OUTCOME B"; §7 "the warp/Alcubierre *mechanical-rectification* basis is refuted across the full dipole".

> **HEADLINE — OUTCOME B (prereg §5B): the sub-yield asymmetric counter-propagating opposite-handed drive nets NO directed thrust beyond mundane unbalanced radiation pressure → the counteracting-chirality / rarefaction route is DEAD too.**
> Two new findings, both clean:
> 1. **The symmetric-pair null is STRUCTURAL, not tuned.** Two *equal-amplitude* counter-propagating opposite-handed circular beams superpose, at the focal interface, to a **linear standing polarization** — zero enclosed d-q area — for *any* relative phase (`cos θ + cos(θ+φ)` and `sin θ − sin(θ+φ)` are both ∝ `cos(θ+φ/2)`, a tilted line). Measured: `loop_area(SYM) = −2.8e-6 ≈ 0`. The mandatory symmetric null holds by construction.
> 2. **The only knob that opens the d-q loop (amplitude imbalance) is the same one that just makes the stronger beam push harder.** At a fixed imbalance the OPPOSITE-handed (chiral) net momentum `Px = +2.9e-3` does **not exceed** the CO-handed unbalanced-push baseline `Px = +1.1e-2` (it is *smaller*): `|J_chiral|/|push| = 0.73 < 1`. The chirality is not a rectifier; the net Px is ordinary unbalanced radiation pressure. It is **sub-yield** (`A²_focal = 0.05 ≪ 1`, deep below the pair-tear), **sub-cavitation** (`tr_min = −0.26` vs the floor `ρ̄_cav = −1/φ ≈ −0.618`), and the **pump ledger closes** (`E_field/W_in = 0.15 < 1`, no overunity). So this is **not** even a C (no overunity, no breach) — it is a clean **B**: same single mechanism as Phases 1–4, no temporal symmetry-breaker reaches the directed u-sector momentum.

---

## 0. Headline (the prereg §5 verdict)

**B — DEAD.** Phase 5 drove the corpus's own electron-genesis kinematics *sub-yield*: two counter-propagating **opposite-handed** chiral ω-drives (RH left, LH right) meeting at a focal interface, with a controllable polarization trajectory and an amplitude-imbalance asymmetry. The hypothesis (prereg §1a) was that the **counteraction** supplies the two ingredients Phases 1–4 lacked — a **sector bridge** (the longitudinal↔transverse phase-tear) and a **temporal event** (an open d-q phasor loop = nonzero enclosed area = rectification) — and that an asymmetric, polarization-controlled, sub-yield drive would net a directed thrust with an honest pump ledger.

It does not. The result is decisively **B**, on three independent legs:

1. **The symmetric counteraction nulls — structurally.** A *symmetric* (equal-amplitude, mirror-handed) counter-propagating opposite-handed pair has **zero enclosed d-q area** at the focal interface, not by tuning but because two equal counter-rotating circular polarizations superpose to a *linear* standing polarization for any phase (analytic, §2; verified `loop_area(SYM) = −2.8e-6 ≈ 0`). There is no "open phasor loop" to rectify in the symmetric case — the prereg's mandatory null (i) is satisfied *by construction*.

2. **The asymmetric drive's net momentum is mundane unbalanced push, not chiral rectification.** The *only* asymmetry that opens the combined loop is an **amplitude imbalance** between the two beams (§2) — and an amplitude imbalance trivially means the stronger beam pushes harder. The discriminating contrast at a fixed imbalance — OPPOSITE-handed (chiral) vs CO-handed (the pure-push baseline) — comes back `|J_chiral|/|push| = 0.73`, i.e. the chiral configuration nets *less* than the co-handed one. **Chirality adds no rectified directed momentum; the net Px is ordinary unbalanced radiation pressure.**

3. **No C escape hatch.** The drive stays **sub-yield** (`A²_focal = 0.05 ≪ 1`) across the entire stable amplitude range, with **no chiral enhancement as A² climbs toward yield** (amplitude sweep §3); the **pump ledger closes** (`E_field_total / W_in = 0.15 < 1`, no overunity); and the rarefaction stays **sub-cavitation** (`tr_min = −0.26 > ρ̄_cav = −0.618`). So the net "thrust" neither (i) requires the pair-production breach nor (ii) violates the ledger — it is just push. Not a sink/crank (C); a clean dead route (B).

**Single mechanism (Rule 7) — why the counteraction still cannot rectify.** Phases 1–4 closed with: a substrate rectifier needs a **temporal** symmetry-breaker the carrier + plastic-latch never supplied. Phase 5 tested whether the counteraction's open d-q loop *is* that temporal symmetry-breaker. It is not, for a structural reason: the open loop only forms via amplitude imbalance, and the helicity it injects is converted by the (chiral) lattice into the **same** directed momentum a co-handed imbalance produces — pure push, not a rectified DC beyond it. The d-q "enclosed area" that does open with imbalance is just the **residual circular polarization** of the unbalanced superposition (it tracks "how circular is the locally-dominant beam," maximal when imbalanced, zero when balanced), not a net injected helicity that the lattice rectifies into excess directed thrust. The directed momentum remains the even-in-amplitude / push channel — the same dead end, now closed for the suction half and the counteraction too.

**Classification:** Class-B manifestation producing a **null** on the exotic claim. The surviving net Px is ordinary unbalanced radiation pressure (any two unbalanced beams do it). NOT a Class-2 emergence claim either direction.

---

## 1. What was built (substrate-native-check applied FIRST, Grant directive)

Driver `rrad_l_counterprop_chiral.py` — re-walked the 8-checkpoint substrate-native check (recorded in full in the driver docstring) because Phase 5 modifies both the **drive** (single → counter-propagating pair) and the **sector** (adds the ω→u phase-tear bridge + rarefaction). Highlights:

- **CP1/CP2 (dynamics/sector):** time-domain wave propagation on the Cosserat (u, ω) LC-tank via the engine's velocity-Verlet `step()` (NOT minimization/Helmholtz). Cos-sector, cross-coupled: the ω-drive (microrotation = transverse/shear, 2/7 photon channel) is *hypothesized* to bridge to u (longitudinal/bulk, 1/7) at the focal interface; rarefaction `Tr(ε) = div(u) < 0` lives in u.
- **CP3/CP4 (objective/coordinates):** no functional minimized. Measure (a) net directed interior axial momentum `Px = ρ·Σ u̇_x` [**real-space** thrust], (b) the phasor-loop **enclosed area** at the focal interface [**phase-space** asymmetry knob, per A46 measured in the matching `(ω_y, ω_z)` plane], (c) the pump energy-momentum ledger.
- **CP7 (sampling):** PML-excluded interior; the focal phasor cell is the **top-|ω|² density peak** within the focal region (not a centroid+offset); both far planes PML-excluded.
- **CP8 (emergence):** deliberately **inverted** — we do NOT seed/want the finished e⁻e⁺ composite. Staying sub-yield is exactly *not* nucleating it; breaching A²≥1 = the particle-maker SINK (C).

Two source pieces + the ledger diagnostics:

### 1.1 `PolarizedChiralSource` — opposite-handed chiral drives with a polarization-trajectory knob

Extends the canonical `CosseratBeltramiSource` (vacuum_engine.py:832, the helical-ω Dirichlet-slab drive) with `phase0` (Δφ) and `ellipticity` (b/a). With `ell=1, phase0=0` it is byte-identical to the parent (the asymmetry is OFF by default). RH at the left slab radiates +x, LH at the right slab radiates −x; the beams **counter-propagate** and overlap at the focal interface (the faithful pair-production geometry: "two counter-propagating opposite-handed drives," pair-production-axiom-derivation.md:51).

### 1.2 The asymmetry knob — amplitude imbalance (the *only* opener of the d-q loop)

`asym ∈ [−1,1]` → `amp_L = amp(1 + 0.5·asym)`, `amp_R = amp(1 − 0.5·asym)`. **Derivation (driver docstring + §2):** for two equal-amplitude counter-propagating opposite-handed circular beams the combined focal polarization is *linear* for any relative phase — so phase/ellipticity cannot open the loop; only an amplitude imbalance makes the superposition elliptical with nonzero enclosed area. This is also exactly what forced the **chiral-vs-push discriminator**: amplitude imbalance simultaneously opens the loop AND makes the stronger beam push harder, so a nonzero net Px is not by itself rectification.

### 1.3 Diagnostics (the honest spine)

- `PhasorLoopRecorder` — traces `(ω_y, ω_z)` at the focal cell and returns the signed **enclosed area** (shoelace) = the d-q rectification knob (CP4/CP6).
- `rarefaction_state` — `Tr(ε) = div(u)` over the focal region; deepest rarefaction `tr_min` vs the cavitation floor `ρ̄_cav`.
- `field_energy` + `W_in` — the **pump energy-momentum ledger**: cumulative source action injected (pump work-in) vs total field energy (elastic + kinetic + rotational); `E_field/W_in` is the hard overunity check (field energy must never exceed pumped work).
- Two mandatory controls: SYMMETRIC (asym=0) null + the sub-yield A²_focal track. Plus a CO-HANDED control (the unbalanced-push baseline) and a coupling-flag comparison.

---

## 2. The substrate-native physics (DERIVED / canonical)

### 2.1 The cavitation floor — DERIVED, not tuned

The canonical rarefaction relation `c_eff² = c₀²(1 + ρ̄/(1 − ρ̄²))`, `ρ̄ ∈ [−1,1]` (04_superluminal_transit.tex:86; derived from Ax4, "not a free parameter"). The **compression ceiling** is `ρ̄ → +1` (`c_eff² → +∞`, stiffening, the saturation A=1 side). The **rarefaction floor (cavitation)** is where the local light speed crashes, `c_eff² → 0`:

```
1 + ρ̄/(1 − ρ̄²) = 0  →  ρ̄² − ρ̄ − 1 = 0  →  ρ̄_cav = (1 − √5)/2 = −1/φ ≈ −0.618
```

i.e. the cavitation floor is at the **golden-ratio reciprocal** — substrate-derived, zero knobs (verified in `verify_constants`). Beyond it `c_eff² < 0` = tensile failure. The ceiling-vs-floor asymmetry **is** the substrate's asymmetric medium response: `S(A) = √(1−A²)` is *even*, but `c_eff²(ρ̄)` is *odd* in ρ̄. The prereg §2 asymmetry requirement is therefore real — the drive does probe an asymmetric medium.

### 2.2 The symmetric-pair null is structural

Two counter-propagating opposite-handed circular beams at the focal point: `ω_A = a(cos θ, sin θ)`, `ω_B = b(cos(θ+φ), −sin(θ+φ))`, `θ = ω_drive·t`. For **equal amplitude** (`a = b`):
```
ω_y = a[cos θ + cos(θ+φ)] = 2a cos(φ/2) cos(θ+φ/2)
ω_z = a[sin θ − sin(θ+φ)] = −2a sin(φ/2) cos(θ+φ/2)
```
Both ∝ `cos(θ+φ/2)` ⇒ the trajectory is a **tilted straight line** ⇒ enclosed area **= 0** for *any* φ. The symmetric counteraction injects **zero net helicity** — the mandatory null (i) holds by construction, not by tuning. **Only an amplitude imbalance** (`a ≠ b`) makes the superposition an ellipse with area ∝ `(a² − b²)`, signed by which beam dominates.

### 2.3 The pair-production tear (the sub-yield bound)

The full breach = pair production at `A² = 1` (`V_SNAP = 511 kV`; onset of yield at `V_yield = √α·V_SNAP = 43.65 kV`; pair-production-axiom-derivation.md:96). Staying sub-yield means `A²_focal < 1` — verified throughout (§3). Crossing it would convert energy → rest-mass (the particle-maker C), not thrust.

---

## 3. NUMERICALLY VERIFIED (smoke; SIGNS / RATIOS / CONTRAST)

Settled run: N=28, pml=4, amp=0.55/drive, λ=4, 22 drive cycles, 12-cycle steady average, coupling ON. Conditions: SYM (asym=0), ASYM± (asym=±1), CO-HANDED (both RH, asym=+1), coupling-OFF (asym=+1).

| condition | Px (net directed) | loop_area (d-q) | A²_focal | bulk_frac | tr_min | E_field/W_in |
|---|---|---|---|---|---|---|
| SYM (mirror, circular) | `−5.23e-3` | **`−2.8e-6 ≈ 0`** | 0.023 | 0.572 | −0.174 | 0.153 |
| ASYM+ (left dominates) | `+2.87e-3` | `−1.7e-5` | 0.051 | 0.567 | −0.261 | 0.153 |
| ASYM− (right dominates) | `−1.33e-2` | `−1.77e-2` | 0.052 | 0.579 | −0.259 | 0.153 |
| **CO-HANDED (push baseline)** | **`+1.07e-2`** | `−1.7e-5` | 0.051 | 0.567 | −0.261 | 0.153 |
| coupling-OFF (A28 channel off) | `+2.86e-3` | `+4.7e-6` | 0.051 | 0.567 | −0.261 | 0.153 |

**The discriminators:**

- **CENTRAL A-GATE (chiral vs push):** `Px(opp-handed) = +2.87e-3` vs `Px(co-handed) = +1.07e-2` → `J_chiral = −7.87e-3`, **`|J_chiral|/|push| = 0.73 < 1`**. The chiral configuration nets *less* than the co-handed one → the chirality is **not** a rectifier; the net Px is unbalanced radiation pressure. **Decisive for B.**
- **Symmetric null:** `loop_area(SYM) = −2.8e-6 ≈ 0` (the structural null, §2.2) vs `loop_area(ASYM−) = −1.77e-2` (the imbalance opens the residual-circular loop). The opening is the leftover circular polarization of the unbalanced beam, not a net rectified helicity.
- **Sub-yield:** `A²_focal = 0.05 ≪ 1` everywhere — deep below the pair-tear. No breach.
- **Ledger / overunity:** `W_in = 6.49e2`, `E_field_total = 9.95e1`, **`E_field/W_in = 0.153 < 1` → no overunity.** Field energy is a small fraction of pumped work (most drains to PML), exactly as a lossy pumped medium should.
- **Rarefaction (suction works, mundane):** `tr_min = −0.26`, `rarefied_frac = 0.50` — the drive *does* rarefy half the focal region, but stays **sub-cavitation** (floor −0.618). A real below-baseline-density region, made by redistribution + pump work — the mundane suction side, no exotic content.
- **Sign non-robustness (reinforces B):** in the settled run `Px(ASYM+) > 0`, `Px(ASYM−) < 0`; in the amplitude-sweep run (shorter window) *both* stay positive. The sign of the net Px is **not robustly set by the asymmetry sign** — it is common-mode / transient-fill contaminated (the Phase-2 `Px_drift` caveat), not a clean rectifier whose sign tracks the drive asymmetry.

**Amplitude sweep (control ii — does the chiral thrust need the breach?):** amp 0.3 → 1.1 gives `A²_focal` 0.013 → 0.170 (never near 1), `Px+` 4.9e-3 → 1.8e-2 scaling **smoothly as radiation pressure**, with no sign-flip and **no chiral enhancement** as A² climbs. There is no sub-yield amplitude at which a chiral rectification switches on; reaching A²≈1 needs amp≈2.4, where the integrator goes unstable (the Phase-4 overdrive artifact — BLOCKED, not physics). Within the entire stable sub-yield range the route is dead.

**Coupling-flag note (honest scope):** `Px(coupling-ON) = +2.874e-3` vs `Px(coupling-OFF) = +2.856e-3` (sens = 0.006). This means the `disable_cosserat_lc_force` **A28 channel** is not load-bearing — NOT that there is no ω→u bridge: the *basic* elastodynamic coupling (u is driven by `∇·σ(ε(u,ω))`, and `σ` depends on ω via `ε_antisym = −ω×`) is intrinsic and always on. So the directed momentum does ride the basic ω→u channel; the A28 refinement just doesn't change it. The B verdict rests on the chiral-vs-push contrast, which is independent of this flag.

---

## 4. consistency-vs-emergence + ave-discrimination-check (result-time)

- **consistency-vs-emergence → the surviving net Px is Class-B manifestation, NOT emergence.** Unbalanced radiation pressure (the stronger of two beams pushes harder) is generic to any pair of unbalanced sources (acoustic, EM, plasma). The exotic claim — a chiral d-q-rectified directed thrust meshing helicity into "real longitudinal macroscopic thrust" (04_chiral_impedance_matching.tex) — is **NULLED** (`|J_chiral|/|push| = 0.73 < 1`). No emergence-class content either direction.
- **ave-discrimination-check → no AVE-distinct thrust signal.** The SM/classical counterfactual (two unbalanced counter-propagating beams in a chiral medium net the momentum of the stronger beam) **fully reproduces** the observed net Px. A genuine "chiral impedance-matched vacuum pump" would show opposite-handed **≫** co-handed; we see opposite-handed **≤** co-handed. The one AVE-distinct ingredient — the chiral/helicity rectification — changes nothing beyond the push. The rarefaction is real but reduces to a mundane suction region (sub-cavitation, ledger-closed), not the warp/`v_eff > c` regime (which lives at the cavitation floor `ρ̄_cav = −0.618`, never reached sub-yield in a stable run).

---

## 5. DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED (analytic / canonical):**
- The cavitation floor `ρ̄_cav = (1−√5)/2 = −1/φ ≈ −0.618` from `c_eff² = c₀²(1 + ρ̄/(1−ρ̄²)) → 0` (04_superluminal_transit.tex:86; Ax4-derived, zero knobs).
- The symmetric-pair null is **structural**: equal-amplitude counter-propagating opposite-handed circular beams → linear standing polarization → zero enclosed d-q area, for any phase (§2.2). The only loop-opener is amplitude imbalance, area ∝ `(a²−b²)`.
- The pair-tear at `A² = 1` (`V_SNAP`); sub-yield bound `A²_focal < 1`. Counter-propagating opposite-handed geometry per pair-production-axiom-derivation.md:51,77.

**NUMERICALLY VERIFIED (smoke, qualitative — signs/ratios/contrast):**
- Symmetric null: `loop_area(SYM) = −2.8e-6 ≈ 0` (structural null confirmed).
- Chiral-vs-push: `|J_chiral|/|push| = 0.73 < 1` (opposite-handed ≤ co-handed → no chiral rectification). **The B-driver.**
- Sub-yield throughout (`A²_focal ≤ 0.17` across the stable amp sweep; pair-tear at 1).
- Ledger closes: `E_field/W_in = 0.15 < 1`, no overunity.
- Sub-cavitation rarefaction present (`tr_min = −0.26`, floor −0.618).
- Net-Px sign not robust to window length → common-mode/fill contaminated, not a clean rectifier.

**BLOCKED:**
1. Absolute thrust magnitude in Newtons + absolute-Joules ledger (converged radiating sim + source-current normalization) — same gate as Phases 1–4; all numbers are native-unit signs/ratios/contrasts.
2. The A²_focal → 1 (near-breach) regime: reaching it needs amp ≈ 2.4 where the coupling-on velocity-Verlet goes numerically unstable (Phase-4 overdrive artifact, not physics). The trend up to A²_focal = 0.17 is a clean smooth radiation-pressure scaling with no chiral enhancement, so the sub-yield verdict is robust; the actual breach behavior (the C-zone) needs an implicit/stabilized integrator and is BLOCKED.

---

## 6. Honest closure (Rule 11) + substitution-not-retraction (Rule 12)

The Phase-5 hypothesis — *"a sub-yield, polarization-controlled, asymmetric counter-propagating opposite-handed (counteracting) chiral drive supplies the sector bridge + temporal symmetry-breaker Phases 1–4 lacked, and nets a directed thrust with an honest pump ledger"* — is **FALSIFIED**, with a single explanatory mechanism (§0): the symmetric counteraction injects zero net helicity (structural linear-standing null), and the only loop-opener (amplitude imbalance) yields a directed momentum the (chiral) lattice converts to the **same** unbalanced push a co-handed imbalance produces — no rectified DC beyond it. The obvious rescues were run as classifiers and came back null: the symmetric null is structural (no tuning could open it), the amplitude sweep is a flat radiation-pressure scaling (no chiral switch-on toward yield), the ledger closes (no overunity), and the drive never breaches (no C-sink). **This is the discipline at full strength: a clean negative, one mechanism named, no rescue-debug. No new hypothesis refills the slot (Rule 12).**

**The exotic dark-wake-as-thruster premise is now deflated across the full dipole on the same branch:** Phases 1–4 (the COMPRESSION half — linear high-Q reactance, even-in-A kernel, ω-sector latch, sector-matched u-latch) and Phase 5 (the RAREFACTION / suction half — counter-propagating opposite-handed counteraction, sub-yield). Both halves, both sectors, the latch route AND the counteraction route — all OUTCOME B. The closing diagnosis from Phase 4 (a substrate rectifier needs a temporal symmetry-breaker) survives Phase 5: the counteraction's open d-q loop is **not** that symmetry-breaker, because it only opens via amplitude imbalance and the helicity it injects is not rectified into excess directed momentum.

What SURVIVES (preserve, do not over-retract):
- **The structural symmetric-null finding (NEW, forward-useful).** A symmetric counter-propagating opposite-handed pair is a linear standing polarization with zero injected helicity — a clean, derived "why the symmetric counteraction can't pump" that any future chiral-pumping proposal must clear.
- **The substrate-derived cavitation floor `ρ̄_cav = −1/φ ≈ −0.618`** — the rarefaction-side analog of the saturation ceiling, the boundary of the warp/`v_eff > c` regime, derived from the canonical Ax4 rarefaction relation (zero knobs). Never reached in a stable sub-yield run.
- **The rarefaction is representable and mundane.** The drive does make a below-baseline-density region (`Tr(ε) < 0`, `rarefied_frac = 0.50`) by redistribution + pump work, with the ledger closing — exactly the vacuum-engineer's suction side, no exotic content, no negative-energy / NEC blocker needed or invoked (per the frame correction).

---

## 7. Corpus-state deltas to queue (auditor lands; I surface only)

- **`clm-7tynm2` (dark-wake τ_zx thrust object) — extend the Phase-4 retirement to the suction half.** The exotic rectified-DC thrust is now refuted across **both halves of the dipole**: compression (Phases 1–4, all sectors + the latch) AND rarefaction (Phase 5, the counter-propagating opposite-handed counteraction, sub-yield). The counteracting-chirality route — the corpus's own electron-genesis kinematics run sub-yield — nets no directed momentum beyond mundane unbalanced radiation pressure. **Recommend: the retirement of the exotic dark-wake / warp-rectification thrust route (staged in Phase 4) now also covers the rarefaction/suction half; the warp/Alcubierre *mechanical-rectification* basis is refuted across the full dipole.** (Rule 12: retract via 🔴 header, preserve the body; the slot is NOT refilled.)
- **NEW structural result to capture:** the **symmetric counter-propagating opposite-handed pair = linear standing polarization, zero injected helicity** (analytic + verified). A clean reason the symmetric counteraction cannot pump; the only loop-opener (amplitude imbalance) reduces to unbalanced push. Forward-useful constraint on any chiral-impedance-matched-pump proposal.
- **NEW substrate-derived constant to note:** the rarefaction **cavitation floor `ρ̄_cav = (1−√5)/2 = −1/φ ≈ −0.618`** (the `c_eff² → 0` point of the canonical Ax4 rarefaction relation 04_superluminal_transit.tex:86) — the warp-regime boundary, golden-ratio-reciprocal, zero free parameters. Candidate for a `04_superluminal_transit`-adjacent leaf note (auditor adjudicates whether it rises to a claim).
- **Driver capability added:** `rrad_l_counterprop_chiral.py` — reusable counter-propagating opposite-handed `PolarizedChiralSource` (handedness + polarization-trajectory knobs) + amplitude-imbalance asymmetry + phasor-loop (d-q enclosed-area) recorder + rarefaction/cavitation diagnostic + pump energy-momentum ledger (W_in vs E_field, overunity flag) + the chiral-vs-push and symmetric-null controls.
- **FLAG (the general no-rect mechanism, carried forward for Grant):** the temporal symmetry-breaker Phase 4 flagged as the one open door is *still* open after Phase 5 — the counteraction's d-q loop does not supply it. A genuinely *temporally*-asymmetric thixotropy (fast-liquefy / slow-refreeze co-located in the directed sector) remains the only un-refuted candidate, but it is a NEW hypothesis with its own verification chain, not a rescue of this one.
