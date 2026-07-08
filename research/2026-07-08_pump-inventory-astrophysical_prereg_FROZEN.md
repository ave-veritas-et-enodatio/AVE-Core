# PUMP INVENTORY — astrophysical pump audit of the AVE nonlinear birefringence — FROZEN PREREG

**Date:** 2026-07-08 · **Lane:** implementer · **Branch:** `analysis/pump-inventory`
**Tree base:** `origin/main` @ `5219a0b0`. **Contention:** P6 of the paper-hardening ledger
(the final make-or-break gate for the sidereal Lorentz-violation flagship).
**Freeze discipline:** this prereg is committed BEFORE the driver exists. Git ordering = freeze proof
(the driver commit is a strictly later object). ONE blocking driver run after freeze.

---

## THE QUESTION (frozen)

The AVE vacuum birefringence is **NONLINEAR** and needs a **pump** (`δn ∝ (field/yield)²`), and its
sidereal Lorentz-violation modulation (~`4.9e-3`, the `4β` radiation-Doppler order, P6 result) survives
existing **LINEAR** LV bounds only because those bounds do not reach a field-dependent effect. The
remaining threat is **astrophysical**: photons (GRB, CMB, magnetar X-rays) cross strong ambient fields
and radiation. **IF** any astrophysical environment pumps the AVE nonlinearity to an observable level,
existing observations (IXPE magnetar birefringence, GRB polarization, cosmic birefringence) become real
bounds — and a magnetar is naively "pumped harder than the lab" (`(B/B_dual)² ~ 7e-4` at `1e7` T vs the
lab pump `~6e-7`). **Does an astrophysical pump exist, or does AVE's own physics make space
transparent?**

## SECTOR HEADER (declared before any physics — mandatory)

- **Which sector?** The birefringence lives in the **two EM reactance grades**, NOT the A1
  dilatation-mass sector and NOT the Cosserat (2,3) winding-charge sector:
  - **ε-grade** (transverse-T2 permittivity varactor): keys on the **potential coordinate**
    `A_V = |E|/E_YIELD`, **charge-keyed / mean-square, DC-included** (round-3
    `[DERIVED: CHARGE-KEYED]`, `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md`).
  - **µ-grade** (permeability relativistic inductor): keys on the **circulation / rate coordinate**
    `A_I = |∮H·dℓ|/I_max = ℓ_node²|∇×H|/I_max`, **NOT on |B| magnitude** (P5,
    `research/2026-07-08_p5-radiative-far-field-keying_RESULT.md`; `S_B = √(1−A_I²)`).
- **Does the engine carry that DOF?** Yes. `S_ε = √(1−A_V²)` and `S_B = √(1−A_I²)` are Axiom-4
  specializations; `ave.bench.birefringence` carries the E-keyed `δn_ave = (1−A²)^¼ − 1` (leading
  `−¼A²`) and the par-perp birefringence `δn_bir = −½A²`. `I_max = ξ_topo·c = e·c/ℓ_node ≈ 124.4 A`.
- **Cold vs saturated (REGIME discipline).** On the **actual keying coordinate**, every clean
  observational path is **cold/linear**: static B ⇒ `A_I = 0` (no circulation); astrophysical
  radiation ⇒ `A_V ≪ 1`. The magnetar B **magnitude** exceeds the AVE magnetic saturation scale
  `B_SNAP ≈ 1.9e9` T — this is the **anti-tautology hinge** (below): IF the µ-grade keyed on
  magnitude, a magnetar would be **super-yield / ruptured**, an observationally-absurd prediction;
  only circulation-keying (FORK-1) keeps it transparent.
- **Phase-space vs real-space (A46).** The keying coordinates are **phase-space reactance coordinates**
  (`A_V` potential, `A_I` circulation), NOT the real-space `|B|` magnitude. FORK-1's entire content is
  that the real-space magnitude is the **wrong coordinate** for the µ-grade. This audit measures in the
  matching phase-space coordinates.

## THE KEYING FUNCTIONALS (grounded, NOT re-derived here — cited)

1. **µ-grade (magnetic):** `S_B = S_µ(A_I) = √(1 − A_I²)`, `A_I = |∮H·dℓ|/I_max = ℓ_node²|∇×H|/I_max`,
   `I_max = ξ_topo·c = e·c/ℓ_node`. **Static B ⇒ ∂_tB = 0 ⇒ ∮H·dℓ = 0 ⇒ A_I = 0 ⇒ S_B = 1 ⇒ δn_µ = 0**
   (P5 RESULT, Eq (6) endpoint; `(kr)²` near-zone suppression for slow AC). This is **FORK-1**.
2. **ε-grade (electric):** `S_ε = √(1 − A_V²)`, `A_V = |E|/E_YIELD`, keys on the **mean-square** of `|E|`
   (DC-included, charge-keyed). A **static E LOADS** locally; a spatially-**uniform** held bias
   self-cancels on readout (INVARIANT-S2 gauge / PHASE-ONLY); a **non-uniform** static E is readable and
   loads (round-3 RESULT).
3. **Birefringence observable:** `δn_bir = −½A²` on the loaded coordinate; AVE coefficient is `~10⁶×`
   the QED Euler–Heisenberg coefficient (`ave.bench.birefringence`, coefficient discriminator). The QED
   static-B baseline `δn_QED,mag = 3·A_e·B²`, `A_e ≈ 1.32e-24 T⁻²` (LITERATURE) is a **separate**
   effect present in both theories.

## ENVIRONMENTS TO ENUMERATE (all field/luminosity values tagged EXTERNAL astrophysical input)

| # | environment | dominant field | static/radiation | EXTERNAL value (frozen) |
|---|---|---|---|---|
| E1 | magnetar surface B | magnetic dipole | **static** (rot. period s) | `B ~ 1e10–1e11` T (`1e14–1e15` G) |
| E2 | ordinary neutron-star / pulsar B | magnetic dipole | **static** | `B ~ 1e8` T (`1e12` G) |
| E3 | galactic B | magnetic | **static** | `B ~ 1e-10` T (µG) |
| E4 | intergalactic B | magnetic | **static** | `B ~ 1e-13` T (nG upper) |
| E5 | pulsar/magnetar polar-cap gap E | electric (parallel) | **quasi-static** | `E ~ 1e13–1e15` V/m (unscreened gap) |
| E6 | interstellar / intergalactic medium E | electric | static | `~0` (quasi-neutral plasma, Debye-screened) |
| E7 | magnetar thermal surface X-ray | EM radiation | **radiation** | `T ~ 0.5` keV, `F = σT⁴` at surface |
| E8 | magnetar giant-flare peak | EM radiation | radiation (transient) | `L ~ 1e40` W (`1e47` erg/s) at `R_NS ~ 1e4` m |
| E9 | accreting NS / ULX inner region | EM radiation | radiation | `L ~ 1e31–1e39` W at `r ~ 1e5–1e7` m |
| E10 | GRB prompt emission | EM radiation | radiation | `L_iso ~ 1e45` W at `r ~ 1e11` m |
| E11 | CMB | EM radiation (thermal bath) | radiation | `u ~ 4e-14` J/m³ (`T ≈ 2.725` K) |
| E12 | interstellar radiation field (ISRF) | EM radiation | radiation | `u ~ 1e-13` J/m³ |

The task's stated "magnetar `1e6–1e7` T" is **below** standard literature magnetar surface fields
(`1e10–1e11` T); this prereg uses the **larger, less favorable** literature values (magnitude-keying
would rupture even harder) — the conservative choice for an honest null.

## METRICS TO COMPUTE (per environment)

- **µ-grade active coordinate** `A_I`: for a **static** B, computed from `∇×H` of the sampled field
  (must EMERGE `= 0` for a source-free static field — NOT asserted); for **radiation**, `A_I = E_rms/E_YIELD`
  (a traveling wave has `A_I = A_V`, P5 table).
- **ε-grade active coordinate** `A_V = |E|/E_YIELD`: for radiation `E_rms = √(I/(ε₀c))`,
  `I = L/(4πr²)` or `σT⁴`; for static E via the EXTERNAL field value.
- **AVE-active response** `A²` = the loaded coordinate squared (`A_I²` for magnetic, `A_V²` for
  electric/radiation). This is the **pump strength**.
- **AVE birefringence** `δn_ave` (via `delta_n_ave_differential_exact`), and the **QED baseline**
  `δn_QED` for the magnetic case (IXPE comparison).
- **Anti-tautology counterfactual** `A²_mag = (B/B_SNAP)²` and `(B/B_dual)²`: what the µ-grade response
  WOULD be if it keyed on magnitude. For a magnetar this must be shown `> 1` (super-yield) to prove the
  [PUMP-SAFE] null is NOT vacuous (the alternative makes a live, falsified prediction).

## VERDICT BINS (pre-registered — thresholds frozen BEFORE compute)

Let `A²_active(env)` = the AVE-active (correctly-keyed) response of each environment on a **clean
observational path**, and `A²_lab ≈ 6e-7` = the flagship lab pump.

- **[PUMP-SAFE]** ⟺ ALL of:
  1. every strong static B (E1–E4) gives `A_I < 1e-9` (machine-zero) ⇒ `δn_µ < 1e-16` (FORK-1 holds);
  2. no non-uniform static E on a clean long-baseline path (E5 screened/short-path, E6 = 0);
  3. every radiation environment on a clean observational path has `A²_active < A²_lab` OR, where
     `A²_active ≥ A²_lab` (near-source transients E8/E9), the geometry is self-pump/collinear
     (projection-suppressed) AND no existing polarization bound reaches it.
  ⇒ flagship closes clean; CMB coincidence spurious.
- **[PUMP-CONSTRAINED]** ⟺ some environment has `A²_active` producing an AVE `δn·path` that an existing
  observation (IXPE / GRB polarization / cosmic birefringence) would ALREADY have seen, i.e. AVE `δn`
  exceeds the observed/allowed value on that path. Report environment + observation + OOM.
- **[PUMP-KILLED]** ⟺ [PUMP-CONSTRAINED] by `≳ 3` OOM with no geometric escape.
- **FORK-1-BREAK (flag, itself a finding)** ⟺ computed `A_I > 1e-6` for a static B at magnetar strength
  (`S_B ≠ 1`). Would mean static magnetar B DOES pump ⇒ re-route to [PUMP-CONSTRAINED]/[PUMP-KILLED]
  against IXPE.

## ANTI-TAUTOLOGY COMMITMENTS (frozen)

1. **COMPUTE `S_B(magnetar B)`, do NOT assume.** `A_I` for a static uniform B at `1e11` T is computed
   from `∇×H` of the sampled field; the null must EMERGE. A non-uniform (dipole) static B must converge
   to the same null as `O(h²)` (not a hard-coded zero).
2. **Genuinely search for a radiation pump.** Compute `E_rms` for E7–E12 and the near-source transients
   E8/E9 without prejudice. If any clean-path radiation environment has `A²_active ≥ A²_lab` AND a bound
   reaches it → report [PUMP-CONSTRAINED] plainly.
3. **The magnitude-keyed counterfactual must fire.** Show `(B_magnetar/B_SNAP)² > 1`: magnitude-keying
   predicts vacuum rupture around magnetars (excluded) — so the null is informative, not a dead zero.
4. **Symmetric standard.** A magnetar pumped harder than the lab is a REAL threat; only FORK-1 saves it,
   so FORK-1 must actually hold at that field. No dropping of the IXPE comparison to reach [PUMP-SAFE].

## CMB COINCIDENCE (frozen decision procedure)

The AVE sidereal `4.9e-3` (`= 4β`, radiation-Doppler order of the CMB velocity boost, P6) ≈ detected
isotropic cosmic birefringence `~5.2e-3` rad (`~0.3°`, EXTERNAL). Decide **spurious vs real** from the
computed inventory: cosmic birefringence requires a pump along the intergalactic CMB path. If E4
(intergalactic B, static ⇒ `A_I = 0`), E6 (IGM E ≈ 0), and E11 (CMB radiation, `A²_active ≪ A²_lab`) are
ALL non-pumping ⇒ intergalactic space is AVE-transparent ⇒ **no AVE cosmological rotation** ⇒ the
proximity is **SPURIOUS** (`4β` velocity ratio vs an unrelated rotation angle, no shared mechanism).
Only route to **REAL**: some ambient pump on the CMB path with `A²_active` projecting onto the observed
`5.2e-3`.

## CONSISTENCY-VS-EMERGENCE CLASSIFICATION (tagged)

- **FORK-1 static-B transparency** (`A_I = 0 ⇒ δn_µ = 0`) = **MANIFESTATION** of Axiom-4 + Ampère–Maxwell
  (`∮H·dℓ = ε₀∂_t∫E·dA`, static ⇒ 0) — α-clean, form-level.
- **Absolute `A_I` / `A_V` magnitudes** ride `I_max = e·c/ℓ_node` and `E_YIELD = √α·E_crit` (α-echo at
  value) — **CONSISTENCY-class**, not headlined.
- **All astrophysical field/luminosity values** = **EXTERNAL** literature inputs, tagged; not
  AVE-derived. Cited by result, never by person.
- **Verdict** = structural comparison (`max A²_active` vs thresholds), scale-invariant in the α-echo.

## DISCIPLINE

- ave-canonical-source: constants imported from `ave.core.constants`; birefringence functions from
  `ave.bench.birefringence`; a canonical self-check asserts `E_YIELD ≈ 1.13e17`, `I_max ≈ 124.4 A`,
  `B_dual = E_YIELD/c ≈ 3.77e8 T`, `B_SNAP ≈ 1.89e9 T`.
- ave-prereg: this doc frozen before the driver (git ordering).
- pure-AVE-corpus: NO external attribution (no reviewer/envelope/names); astrophysics values cited by
  result only.
- ONE blocking driver run; house-WHITE figure; `make verify` green; NO edit to paper/ledger/canon
  (result doc + proposed integration note only); NO self-merge (push branch, open DO-NOT-MERGE PR).

## THE ONE PLUMBER-PHYSICAL QUESTION (pre-test-physics-check — surfaced to Grant)

*A magnetar's static B magnitude EXCEEDS the AVE magnetic saturation scale `B_SNAP` (`~1e11` T vs
`1.9e9` T). Is the vacuum inductor's saturation set by the DC bias current through it — of which a
source-free static B carries NONE (`∇·B = 0`, no monopole ⇒ no static operating-point bias for the
rate-keyed inductor; `∇×H = 0` ⇒ zero circulation) — or by the flux magnitude? FORK-1 says the former:
however strong, a static B supplies zero circulation and does not saturate the inductor, so the vacuum
around a magnetar stays transparent (`S_B = 1`).* The test answers it by COMPUTING `A_I` from `∇×H` at
`1e11` T. If magnitude-keying were right, every magnetar would be a ruptured-vacuum region — which we do
not observe. Surfaced for Grant, not decreed.
