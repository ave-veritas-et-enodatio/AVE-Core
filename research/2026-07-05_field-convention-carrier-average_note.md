# Field convention for the birefringence Letter's Table I — peak vs cycle-averaged (Phase-0 item 1)

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/letter-v2-phase0`
**Class:** CONVENTION DERIVATION + FLAGGED EXPOSURE (flag-don't-fix). Triggered by Keith's Phase-0
review item 1: the Letter (`papers/2026_birefringence_letter/main.tex`) nowhere states whether the
Table I fields are PEAK or CYCLE-AVERAGED, and Keith notes the probe crosses many pump cycles so
`<E^2> = E0^2/2`. This note DERIVES the convention from the actual pump-probe geometry, states what
it does (and does not) move, and surfaces a deeper mixed-footing exposure in the anchored ratio for
**[GRANT-ADJUDICATE]** — NOT unilaterally resolved.

> ⚠️ **This note does NOT edit the anchored v1 numbers.** The v1 table + ratio are Bitcoin-anchored
> (`claim-prereg-ots/claims_by_hash.md`, SHA f34e7559; v1 content private, hash public). Any number
> change is a documented v2 with v1 preserved verbatim. The mixed-footing finding in §3 is a
> **flagged exposure for Grant**, not an implementer edit.

---

## 0. What the Letter's Table I fields ARE (verified against the driver)

**Verified:** the field `E = 8.68e13 V/m` in every demonstrated-pump row of Table I is the **PEAK
carrier amplitude** `E0 = sqrt(2 I / (c eps0))` at `I = 1e21 W/cm^2`.

- Driver: `src/scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py:112` `field_from_intensity_wcm2`,
  docstring "Peak E-field [V/m] from intensity I [W/cm^2]. E = sqrt(2 I / (c eps0))".
- Live check: `sqrt(2 * 1e21*1e4 / (c*eps0)) = 8.6802e13 V/m` — matches Table I's `8.68e13` to 0.002%.
- The RMS/cycle-averaged field would be `E0/sqrt2 = 6.14e13 V/m`; Table I does NOT use that.
- So `A^2 = (E0_peak/E_yield)^2 = 5.90e-7` (Table I) is the **peak-field** dimensionless amplitude.

This is the anchored v1 convention. It is currently UNSTATED in the Letter — item 1's fix is to
state it explicitly.

## 1. The geometry that sets the convention (LoI arXiv:2405.18063, verified pages)

The pump is a linearly-polarized optical wave `E(t) = E0 * envelope(t) * cos(w t)` (LoI Eq.23, p.10),
`lambda = 800 nm`, `tau_FWHM = 30 fs`, counter-propagating (head-on, `theta_coll = pi`) against the
X-ray probe in the conventional two-beam scenario (LoI Fig.8, p.10). The LoI's "peak intensity"
`I_peak = 8 sqrt(2/pi) W/(pi w0^2 tau)` (Eq.23 caption) is the peak of the Poynting flux, i.e. the
cycle-averaged `(1/2) c eps0 E0^2` at the envelope peak.

- Pump carrier period `T = lambda/c = 2.67 fs`.
- Probe transit through the `z = 10 um` focus: `z/c = 33.3 fs` → the probe crosses **~13 carrier
  cycles** during transit.

**Consequence Keith is right about:** because the birefringence is quadratic in the LOCAL
instantaneous field, the accumulated retardance `Delta phi = (2 pi/lambda) INT delta_n(t) dz` samples
`E^2(t) = E0^2 cos^2(w t)`, whose carrier average is `<E^2> = E0^2/2`. The physically-read retardance
is the carrier-averaged one, not the peak-instantaneous one. This applies to **both** the SVE leg and
the QED leg — the carrier average is a property of the measurement integral, not of either medium.

## 2. The QED leg's coefficient already carries the carrier average (the load-bearing fact)

The QED leg in the driver is `delta_n_qed_electric_pvlas(E, geometry="propagating") = (alpha/15pi)(E/E_crit)^2`
(`src/ave/bench/birefringence.py:252,276`). **This coefficient is defined on the LoI's INTENSITY**
(cycle-averaged) form, verified two independent ways:

- **LoI Eq.16 (p.6):** `Dn = (8 alpha^2/15)(I_L/m^4)` with `I_L` the intensity `= <E^2> = E0^2/2`.
  Converting to `(E0_peak/E_crit)^2` units (natural units, `e^2 = 4 pi alpha`, `E_crit = m^2/e`):
  `Dn = (8 alpha^2/15) * (E0_peak/E_crit)^2/(8 pi alpha) = (alpha/15pi)(E0_peak/E_crit)^2`. **EXACT**
  (live: ratio `= 1.0000000000`).
- **LoI Eq.19 (p.7):** `N'/N = (4 alpha^2/225)(I_L/I_S)^2 (z/lambda)^2` with `I_S = 4.7e29 W/cm^2`.
  Back-out `Dn = (2 alpha/15pi)(I_L/I_S)`; at `I_L = 1e21` this gives `6.590e-13`, versus the
  `alpha/15pi (E0_peak/E_crit)^2 = 6.663e-13` — agree to **1.1%** (the residual is the LoI rounding
  `I_S` to `4.7e29` vs the exact `c eps0 E_crit^2 = 4.648e29 W/cm^2`; note `I_S` matches the NO-1/2
  static-field convention, confirming the intensity reading).

So: **`alpha/15pi * (E0_peak/E_crit)^2` IS the cycle-averaged QED birefringence, written in a
peak-field parametrization.** The factor `1/2` (the `cos^2` average) is folded into the coefficient
`alpha/15pi` (vs the instantaneous coefficient `2 alpha/15pi`, see §3).

## 3. THE FLAGGED EXPOSURE — a mixed footing in the anchored ratio [GRANT-ADJUDICATE]

Carrying item 1 to its logical end surfaces a factor-of-2 that is NOT what Keith flagged, is larger
than a Table-I rescaling, and touches the **anchored ratio**. Per flag-don't-fix I surface it with the
full derivation and do NOT edit any anchored number.

**The SVE leg is peak-INSTANTANEOUS; the QED leg is cycle-AVERAGED. The anchored ratio pairs them.**

- The SVE differential `delta_n_bir = -1/2 (E/E_c)^2` is the raw Axiom-4 kernel response — an
  INSTANTANEOUS local response to the field (corpus derivation quotes it "vs peak field",
  `research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md:77,228`; no carrier average
  baked in). Its instantaneous coefficient on `(E/E_crit)^2` is `1/(2 alpha)` (via the substrate
  identity `(E_crit/E_c)^2 = 1/alpha`).
- The QED `alpha/15pi` is the cycle-AVERAGED coefficient (§2). Its INSTANTANEOUS coefficient is
  `2 alpha/15pi` (double, because `<cos^2> = 1/2`).

The anchored ratio `7.5 pi/alpha^2 = [1/(2 alpha)] / [alpha/15pi]` divides an INSTANTANEOUS SVE
coefficient by a CYCLE-AVERAGED QED coefficient — a **mixed footing**. On a **consistent single
footing** the ratio is HALF that:

| footing (both legs same) | SVE coeff on (E/E_crit)^2 | QED coeff on (E/E_crit)^2 | ratio |
|---|---|---|---|
| both peak-instantaneous | `1/(2 alpha)` | `2 alpha/15pi` | `3.75 pi/alpha^2 ≈ 2.21e5` |
| both cycle-averaged | `1/(4 alpha)` | `alpha/15pi` | `3.75 pi/alpha^2 ≈ 2.21e5` |
| **anchored v1 (mixed)** | `1/(2 alpha)` (peak) | `alpha/15pi` (cyc-avg) | `7.5 pi/alpha^2 ≈ 4.42e5` |

**Both consistent footings give `3.75 pi/alpha^2 ≈ 2.21e5` — exactly half the anchored `7.5 pi/alpha^2 ≈ 4.42e5`.**
(Live-derived three independent ways this session; all converge.)

**GENEALOGY — the mixed-footing x2 and the documented propagating-vs-static x2 are the SAME
`<cos^2> = 1/2` carrier average through two doors.** The QED-normalization correction
(`research/2026-07-03_birefringence-qed-normalization-correction.md §1`) documented a
static->propagating x2 taking `alpha/30pi -> alpha/15pi`. That x2 DECOMPOSES (verified live,
`x4 * 1/2 = x2` exactly):
- **x4 (head-on collision geometry):** `alpha/30pi -> 2 alpha/15pi`. Pump-probe cross terms of the
  field invariants (a single on-shell plane wave has `S = P = 0`); the `(1-cos theta_coll)^4`-maximized
  head-on value.
- **x1/2 (temporal `<cos^2>` carrier average):** `2 alpha/15pi -> alpha/15pi`. Static endpoint is DC
  (no carrier); the headline is cycle-averaged.

The `1/2` in THIS decomposition is the SAME `<cos^2> = 1/2` that makes the QED coefficient
cycle-averaged while the SVE `-1/2(E/E_c)^2` stays peak-instantaneous — i.e. the documented
"propagating-vs-static x2" and the "mixed-footing x2" are ONE temporal average, entering the ledger
through two different doors (the geometry-normalization door in 2026-07-03, and the SVE-footing door
here). This is why the composite label "propagating-versus-static geometry factor" is imprecise: the
factor is `x4 geometry x 1/2 temporal`, and the temporal half is exactly the footing asymmetry.

**FORWARD DOUBLE-COUNT TRAP — documented shut.** If a future pass treats `alpha/15pi` as an
INSTANTANEOUS coefficient and applies a `<cos^2> = 1/2` carrier average to it AGAIN, it reconstructs
`alpha/30pi` and a ratio `15 pi/alpha^2` — the WRONG door (that is the DC static coefficient, not a
cycle-averaged propagating one). `alpha/15pi` is ALREADY cycle-averaged (§2); it must NOT be averaged
a second time. The correct instantaneous QED coefficient is `2 alpha/15pi`; the correct cycle-averaged
one is `alpha/15pi`. Any consistent-footing resolution uses ONE of these, never both-then-average.

**What this is and is not:**
- It is **not** what Keith flagged (he flagged the absolute Table-I field convention; this is a
  ratio-normalization footing that his question exposed on follow-through).
- It is exactly the class of item the Letter's own honesty ledger already anticipates (§II.B item
  (iv)): "a different but still alpha-rooted convention shifts the numerical ratio, not the order of
  magnitude." A factor of 2 is such a shift. The order of magnitude (`~10^5`, `~5-6 OOM` above QED)
  and every falsifier verdict are **unchanged** either way.
- It does **not** rescue or threaten anything: the SVE flip-prob stays `~10^-3` (still `~7 OOM` above
  the `2.4e-10` floor), the QED co-prediction stays `~10^-14`, the kill criterion (`P < 1e-8`) is
  untouched. It is a normalization-of-the-headline-ratio question only.

**[GRANT-ADJUDICATE] the resolution — three arms, Grant owns the call:**
1. **KEEP v1 mixed footing `7.5 pi/alpha^2`** as the anchored value, and add ONE honest sentence to
   the Letter's honesty-item (iv) noting the peak-vs-cycle-averaged normalization carries a factor-2
   that is folded into the α-rooted-convention caveat already stated. (Minimal; preserves the anchor;
   the order-of-magnitude claim is unaffected.) Anchored v1 stands; no v2.
2. **MOVE to the consistent single footing `3.75 pi/alpha^2`** as a documented v2 (v1 preserved
   verbatim, dated changelog in `provenance.md §8`, OTS anchor noted on v1). Table I QED and SVE legs
   both shift onto the same footing; the SVE `~10^-3` and QED `~10^-14` move by O(1) but the verdict
   holds. Stronger internal consistency; costs a v2 of an anchored document.
3. **Something I have wrong** — the SVE kernel is meant to be read cycle-averaged from the start (in
   which case Table I's `A^2 = 5.90e-7` is peak but the coefficient already absorbs the average, and
   arm 1 applies with a wording tweak). This is a physics-of-the-kernel question about whether the
   Axiom-4 permittivity responds to the instantaneous or the envelope field — a substrate question
   Grant/the auditor owns, not the implementer.

**Recommendation (structure only, NOT a ruling):** arm 1 for THIS Letter-v2(phase-0) round — it keeps
the anchor intact, states the field convention (peak) truthfully, and folds the footing factor into
the honesty ledger's existing α-rooted-convention caveat, which already promises "shifts the ratio,
not the order of magnitude." The sharper arm-2 v2 (or arm-3 physics ruling) is a SEPARATE adjudication
that should not ride inside a Phase-0 exposition PR. This is the KEEP-BOTH discriminator posture:
preserve the anchored legacy, flag the new axis, let Grant land the resolution.

## 4. What item 1 actually changes in the Letter (this round, arm-1 posture)

Per the recommendation, the Letter edits for item 1 are:
- **State the field convention explicitly:** add one sentence to §III.A (readout chain) / Table I
  caption that the tabulated fields are the **peak carrier amplitude** `E0 = sqrt(2 I / (c eps0))`,
  and that both the SVE and QED legs are evaluated through the identical single-pass chain at that
  same peak field (like-for-like; the field-independent ratio does not depend on the choice).
- **Fold the footing factor into honesty-item (iv):** one clause noting the peak-vs-cycle-averaged
  normalization is one of the α-rooted convention choices that shifts the numerical ratio by an O(1)
  (factor-2-class) amount but not its order of magnitude.
- **Table I numbers do NOT move** under arm 1 (peak-field footing = the anchored v1). No v2 of the
  anchored table this round; the v2/arm-2 question is flagged in §3 for Grant.

## 5. Discipline tags + provenance
- **flag-don't-fix:** the §3 mixed-footing exposure is surfaced with full derivation + both file
  paths; NOT silently resolved. Precedent: `research/2026-05-18_q-g27-q-g19a-systemic-conversion-error-finding.md`
  ("surfaced the factor-2 inconsistency cleanly; did NOT unilaterally edit any corpus location").
- **substitution-not-retraction (Rule 12):** v1 anchored value preserved verbatim; no anchored number
  edited; the v2/arm-2 path (if Grant picks it) gets its own dated changelog with v1 alongside.
- **consistency-vs-emergence:** CONSISTENCY-class throughout; the ratio magnitude (either `7.5 pi/alpha^2`
  or `3.75 pi/alpha^2`) is an α-echo for BOTH frameworks (symmetric standard); the chord is the FORM
  (tree-O(1) saturation), untouched by the footing.
- **verify-before-cite:** every number live-derived against `ave.core.constants` and the driver this
  session; LoI Eq.16/19/22/23 read from arXiv:2405.18063 pp.5-10 (verified pages).
- Anchored v1: `claim-prereg-ots/claims_by_hash.md` SHA f34e755998a9 — `P_flip = 5.39e-3 / 4.28e-3 /
  9.28e-3`, ratio `7.5 pi/alpha^2 ~ 4.42e5`. PRESERVED.
