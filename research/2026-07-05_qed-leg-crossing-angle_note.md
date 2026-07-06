# QED co-prediction leg at the TRUE BIREF@HIBEF crossing geometry (Phase-0 item 2)

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/letter-v2-phase0`
**Class:** VERIFICATION (does the QED leg's O(1) geometry factor move the numbers?). Triggered by
Keith's Phase-0 item 2: re-derive the Euler-Heisenberg comparison leg at the ACTUAL BIREF crossing
geometry per Karbstein-Gies-Reuter-Zepf, PRD 92, 071301(R) (2015), and update the Letter's QED numbers
if the O(1) geometry factor (angle + polarization dependence, the 15pi-class prefactors) moves them.

**RESULT (headline): the geometry factor does NOT move the QED leg. The driver's `alpha/(15 pi)`
propagating value IS the correct head-on (counter-propagating, `theta_coll = pi`) crossing-geometry
coefficient. It reproduces the LoI's own crossing-geometry signal (Eq.19) to 1.1%. The corpus's
21.8x = 1/(2 pi alpha) correction (`7.5 pi/alpha^2`) is CONFIRMED, not regressed.**

---

## 0. The instruction and the guard

Item 2 asks: re-derive the QED leg at the real crossing geometry; the O(1) geometry factor (the
15pi-class prefactors, the angle + polarization dependence) may move it. **Guard (do-not-regress):**
the corpus already rebuilt this leg once — the `1/(2 pi alpha) ≈ 21.8` correction that took the
understated `(3/45) alpha^2` up to the arbiter-anchored `alpha/(15 pi) = 2.908 alpha^2` propagating
leg, giving the ratio `7.5 pi/alpha^2 ≈ 4.42e5`
(`research/2026-07-03_birefringence-qed-normalization-correction.md`, PR #498). Item 2 must VERIFY
against that chain, not undo it.

## 1. The true BIREF@HIBEF crossing geometry (LoI arXiv:2405.18063, verified pages)

- **Collision geometry (conventional two-beam, Fig.8 p.10):** the optical ReLaX pump and the X-ray
  probe **counter-propagate** — head-on, `theta_coll = pi`. The LoI states the polarization-flip
  signal scales as `(1 - cos theta_coll)^4` (p.10), "As the attainable signal photon number scales
  with (1 − cos vartheta_coll)^4 ... the counter-propagating geometry is favoured." Head-on maximises
  it; `theta_coll = pi` is the registered scenario.
- **Polarization geometry (Eq.15 p.6):** "Choosing the optimal scenario of a 45° angle between probe
  and laser polarisations, one may use the textbook formulae ... to find the forward-flip amplitude"
  `f(0) = M(0)/(8 pi sqrt s) = (4 alpha^2/15 pi)(w*/m)^3 (1/m)`. The **15 pi** and the **45°
  polarization** are the O(1) geometry factors Keith names — and they are the LoI's registered
  scenario, i.e. exactly the geometry the Letter's Table I is stated for.
- **The KGRZ 2015 result (Karbstein, Gies, Reuter, Zepf, PRD 92, 071301(R)):** the LoI's Sec 3.1 /
  Eq.24-26 signal photon formula `N_perp = ...` (the `sqrt(3/pi)(c1-c2)^2 m^8 (W_L w*/m^2)^2
  (lambda_e/w0L)^4 sqrt(g(0)) ...` form, p.11) is the KGRZ head-on pulsed-paraxial result [LoI refs
  100,101]; its leading coefficient reduces, in the plane-wave / infinite-Rayleigh limit, to the
  same `Delta n = (8 alpha^2/15)(I_L/m^4)` of Eq.16. The 45°-polarization + head-on O(1) factors are
  already inside the `(c1-c2)` combination and the `15 pi` prefactor.

## 2. The QED leg coefficient at the true geometry, derived (matches the driver EXACTLY)

The LoI's crossing-geometry birefringence, in the `(E/E_crit)^2` form the Letter uses:

- **From Eq.16 (head-on, 45° pol):** `Dn = (8 alpha^2/15)(I_L/m^4)`, `I_L = <E^2> = E0^2/2`. Natural
  units (`e^2 = 4 pi alpha`, `E_crit = m^2/e`): `(E/E_crit)^2 = 4 pi alpha (E/m^2)^2`, so
  `Dn = (8 alpha^2/15) * (E0_peak/E_crit)^2/(8 pi alpha) = (alpha/15 pi)(E0_peak/E_crit)^2`. **EXACT**
  (live: `Dn_Eq16 / [alpha/15pi (E0/Ecrit)^2] = 1.0000000000`).
- **From Eq.19 (the crossing-geometry signal formula):** `N'/N = (4 alpha^2/225)(I_L/I_S)^2
  (z/lambda_X)^2` → `Dn = (2 alpha/15 pi)(I_L/I_S)`. At `I_L = 1e21 W/cm^2`, `I_S = 4.7e29 W/cm^2`:
  `Dn = 6.590e-13`, vs driver `alpha/15pi (E0_peak/E_crit)^2 = 6.663e-13` — **agree to 1.1%** (the
  residual is the LoI's rounding of `I_S` to `4.7e29`; exact `c eps0 E_crit^2 = 4.648e29`).

**Both routes land on `alpha/(15 pi) = 2.908 alpha^2` for the propagating head-on 45° geometry — the
value already in `src/ave/bench/birefringence.py:276` (`geometry="propagating"`) and already used by
the campaign drivers.** The O(1) crossing-geometry factor is therefore ALREADY BAKED IN; it does not
move the QED numbers.

## 3. Why the geometry factor was already correct (the 21.8x correction did the work)

The `alpha/(15 pi)` propagating leg is precisely the crossing-geometry-correct value because the
2026-07-03 correction anchored it to two external arbiters that both encode the geometry:
- **PVLAS `A_e` via `E<->cB` duality** → static-field `alpha/(30 pi)`; a **propagating** plane-wave
  pump (both invariants active, head-on) DOUBLES it to `alpha/(15 pi)` — the factor-2 IS the head-on
  propagating-vs-static geometry factor (`birefringence.py:252-282`,
  `research/2026-07-03_birefringence-qed-normalization-correction.md §1`).
- **LoI Eq.19** (the KGRZ crossing-geometry signal) — reproduced to 1.1% (§2 above).

The pre-fix `(3/45) alpha^2 = 0.0667 alpha^2` was understated by `1/(2 pi alpha) = 21.81` (it was a
single-mode/differential mislabel, NOT a geometry error). The fix already moved the leg onto the
crossing-geometry-correct arbiter. **Item 2's re-derivation confirms it: no regression, no further
move.**

## 4. What this means for the Letter (item 2 outcome)

- **QED numbers do NOT change.** `delta_n_QED = (alpha/15 pi)(E/E_crit)^2`, `P_qed ~ 2.76/2.19/4.75e-14`
  (demonstrated rows), ratio `7.5 pi/alpha^2 ~ 4.42e5` — all UNCHANGED. Table I QED column stands.
- **The Letter should CITE Karbstein 2015 properly for the crossing geometry.** `Karbstein2015` is
  already in `refs.bib` (PRD 92, 071301, DOI 10.1103/PhysRevD.92.071301) and cited in §I and §III.
  Item 2's contribution is to make the crossing-geometry provenance explicit in §III.A: the QED leg
  is the head-on (`theta_coll = pi`), 45°-polarization value of KGRZ 2015 / LoI Eq.16-19, not a
  duality estimate alone. One added clause + the existing citation.
- **The static-vs-propagating factor of 2** (already flagged in the QED-normalization note §1, and in
  the Letter's §III.B parenthetical) IS the geometry factor between the PVLAS static arbiter and the
  HIBEF propagating head-on geometry. The Letter already quotes the larger propagating value
  `7.5 pi/alpha^2` as the conservative headline; item 2 confirms this is the geometrically-correct
  choice for the HIBEF pump.

> **Cross-reference to the field-convention note (item 1):** the `alpha/15pi` coefficient is a
> CYCLE-AVERAGED (intensity) coefficient in a peak-field parametrization — see
> `research/2026-07-05_field-convention-carrier-average_note.md §2-3`. That note flags a mixed-footing
> factor-2 in the anchored ratio for [GRANT-ADJUDICATE]. Item 2 does NOT resolve it; item 2 only
> establishes that the QED coefficient at the true crossing geometry is `alpha/15pi` (whatever the
> footing decision, the QED coefficient's geometry is correct).

## 5. Discipline tags + provenance
- **verify-before-cite:** LoI Eq.15/16/19/22, Fig.8, `(1-cos theta)^4` scaling read from
  arXiv:2405.18063 pp.6-11 (verified pages this session); `alpha/15pi` value + Eq.16/Eq.19 match
  live-derived against `ave.core.constants`.
- **do-not-regress guard: PASSED.** The `7.5 pi/alpha^2` (21.8x-corrected) leg is confirmed, not
  undone. `research/2026-07-03_birefringence-qed-normalization-correction.md` chain intact.
- **no-strawman:** both legs ride the identical `delta_n -> dphi -> flip` chain; only `delta_n`
  differs; the QED leg is the LoI's own crossing-geometry value (not a weakened baseline).
- **Karbstein2015:** PRD 92, 071301 (2015), DOI 10.1103/PhysRevD.92.071301, arXiv:1507.01084 —
  already in `refs.bib`, verified. The head-on pulsed-paraxial vacuum-birefringence result the LoI's
  Eq.24-26 signal formula is built on.
