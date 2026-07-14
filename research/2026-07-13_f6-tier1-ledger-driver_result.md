# F6 tier-1 — two-reservoir ODE ledger DRIVER — RESULT

**Date:** 2026-07-13
**Class:** result (driver run + adjudication against frozen bins). Downstream of
`research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md` (PR #666, binding)
and `research/2026-07-13_f6-tier1-ledger-driver_prereg.md` (FROZEN, pushed before
this driver ran).
**Artifacts:** driver `src/scripts/vol_3_macroscopic/f6_tier1_two_reservoir_ledger.py`;
tests `src/tests/test_f6_tier1_ledger.py`; run output
`src/scripts/vol_3_macroscopic/f6_tier1_two_reservoir_ledger_results.json`.

**Sector header (inherited, CHARTER §0).** MODE: global bookkeeping **ODE ledger, NOT
a field solve** (no `a(t)`; `solve_backreaction` static-elliptic). REGIME **(★QUARANTINE —
Grant-walked input, CHARTER §1.4)**: top-stage cascade port at the cosmic operating
point. PHASE-STATE: a held static store (ρ_latent) draining one-way into the T2 bath.
SECTOR **(★QUARANTINE — Grant-walked input, CHARTER §1.4)**: the **A-class continuous-
drainage** behavior of the LOCAL top port; **NOT** A1 dilatation-mass, **NOT** a
Cosserat-winding claim. The quarantined cascade address is premise-under-test, not
established corpus physics.

**Register:** AVE substrate + EE (two-reservoir exchange, entropic sink, matched-
termination absorption, Ax3-lossless interior). **Consistency-vs-emergence class =
CONSISTENCY (ceiling)** — `κ` is a FREE parameter, not derived from `{ℓ_node, α, G}`.

---

## 1 · VERDICT BOX

> **FROZEN-CRITERIA VERDICT: bin (i) LEDGER-CONSISTENT** — the two-reservoir ledger
> conserves (`ρ̂+Ê_T2` invariant to ~1e-15 ≪ `tol_cons=1e-8`); the transfer passes both
> structural gates (TRILINEAR-PUMP bounded-norm, DIODE-RESURRECTION mechanism-class);
> and the chord's DE-form is separable from the frontier default on the DECORRELATED
> run (`D[ON,FRONTIER] > tol_form=1e-2`: min over κ = **0.057** / **0.053** on the two
> decorrelated histories). By the frozen §4.5 bins this is bin (i).
>
> **★ But the charter's a-priori is FALSIFIED (pre-registered flag §8.2, now CONFIRMED).**
> `D[ON,FRONTIER] > tol_form` **on PHYSICAL histories too** (min over κ = **0.088**, fiducial
> κ=2 → **0.150**). The a-priori (CHARTER §4.7, prereg §8.1: "bin (iii) FORM-DEGENERATE
> EXPECTED on physical; bin (i) reachable ONLY via decorrelated") did **not** hold: the
> physical run was never below `tol_form`, so decorrelation did not "lift a physical
> degeneracy" — the chord is separable on **all** histories. **This is surfaced, not
> fixed** (flag-don't-fix): the bin-(i) landing does **not** carry the meaning the charter
> attached to it. Grant/auditor adjudicate whether it changes the corpus reading.
>
> **What bin (i) certifies (CHARTER §4.5, binding):** CONSERVATION + FORM **only**. It does
> **NOT** certify the transfer is Ax3-entropic (inexpressible in two scalars; cited premise,
> deferred to tier-2, CHARTER §iii). It does **NOT** discharge the three §4.2 sector
> constraints (bias-invariance / electron-no-drain / muon-fence — DEFERRED to tier-2). It
> is **NOT** an EMERGENCE result: `κ` is a free parameter, not derived from `{ℓ_node, α, G}`
> (F6 gate 3, `dark-energy-latent-heat-definition.md:156`); refuse any emergence headline.
> **No magnitude match to ρ_Λ anywhere** — the normalized verdict is scale-invariant to
> 8.1e-13 (MAGNITUDE-TUNE gate); the 10^122 path stays rejected canon.

---

## 2 · Freeze provenance (freeze-by-push preserved)

| Artifact | SHA | Pushed (UTC) |
|---|---|---|
| FROZEN prereg (bins + tolerances) | `a1ed485a` | 2026-07-13 23:12:44 |
| Driver + tests + this RESULT | (this commit) | after prereg push |

The prereg was **pushed before the driver was ever run**. The driver source existed
in the working tree only as unrun code (compiled + imported, **no `D` computed**) until
the prereg push landed. Freeze margin = prereg strictly precedes the first driver run
and the driver commit. Tolerances (`tol_cons=1e-8`, `tol_form=1e-2`), window `τ∈[1,10]`,
grid `N=2001`, and the κ-scan `{0.1…10}` were pinned pre-run and are unchanged here.

---

## 3 · Numeric battery (all arms × histories × κ)

Window `τ ∈ [1,10]`, `N=2001`, `RK45 rtol=1e-11`. `H_INFINITY=2.2466e-18 s⁻¹`,
`H(t₀)=(2/3)H_∞=1.4977e-18 s⁻¹`, `t_ref=4.4512e17 s` — verdict is **scale-free**.
`cons_resid` = max relative `|ρ̂+Ê_T2−1|`; `cf_dev` = max deviation from the frozen
closed form (integrator validation).

### 3.1 PHYSICAL (FRW lock: H∝a^(−3/2), n_matter∝a⁻³)

FRONTIER: conserves (resid 8.9e-16), closed-form dev 5.1e-12, `ρ̂(τ₁)=1.00e-2` (=10⁻²=a⁻³).

| κ | D[ON,FRONTIER] | D[ON,Λ] | cons_resid | bnd | cf_dev | ρ̂_ON(τ₁) |
|---|---|---|---|---|---|---|
| 0.1 | 8.4146e-01 | 7.3674e-02 | 2.2e-16 | ✓ | 6.4e-12 | 9.139e-01 |
| 0.2 | 7.7374e-01 | 1.4162e-01 | 4.4e-16 | ✓ | 1.2e-11 | 8.353e-01 |
| 0.5 | 6.0031e-01 | 3.1546e-01 | 3.3e-16 | ✓ | 2.3e-11 | 6.376e-01 |
| 1.0 | 3.8909e-01 | 5.2669e-01 | 3.3e-16 | ✓ | 1.3e-10 | 4.066e-01 |
| **2.0** (fid) | **1.4984e-01** | 7.6529e-01 | 5.6e-16 | ✓ | 7.8e-10 | 1.653e-01 |
| 5.0 | **8.7742e-02** (min) | 9.5642e-01 | 1.0e-15 | ✓ | 5.3e-11 | 1.111e-02 |
| 10.0 | 1.4491e-01 | 9.8839e-01 | 8.9e-16 | ✓ | 7.6e-12 | 1.234e-04 |

**min_κ D[ON,FRONTIER] = 0.0877 (κ=5) — > tol_form=0.01.** min_κ D[ON,Λ] = 0.0737 (κ=0.1) —
**scan-edge value (argmin at the smallest frozen grid point); the infimum over κ is 0** (κ→0 collapses
ON onto Λ identically). See the NON-FROZEN Λ-degeneracy boundary map, §6.1, for the quantified limits.

### 3.2 DECORR_H_FROZEN (H frozen const, n_matter falls)

FRONTIER: conserves (resid 1.1e-15), closed-form dev 8.2e-13, `ρ̂(τ₁)=1.52e-8` (=exp(−18)).

| κ | D[ON,FRONTIER] | D[ON,Λ] | cons_resid | bnd | cf_dev |
|---|---|---|---|---|---|
| 0.1 | 8.8431e-01 | 7.3674e-02 | 2.2e-16 | ✓ | 6.4e-12 |
| 0.2 | 8.1688e-01 | 1.4162e-01 | 4.4e-16 | ✓ | 1.2e-11 |
| 0.5 | 6.4428e-01 | 3.1546e-01 | 3.3e-16 | ✓ | 2.3e-11 |
| 1.0 | 4.3417e-01 | 5.2669e-01 | 3.3e-16 | ✓ | 1.3e-10 |
| **2.0** (fid) | **1.9529e-01** | 7.6529e-01 | 5.6e-16 | ✓ | 7.8e-10 |
| 5.0 | **5.7141e-02** (min) | 9.5642e-01 | 1.0e-15 | ✓ | 5.3e-11 |
| 10.0 | 1.1144e-01 | 9.8839e-01 | 8.9e-16 | ✓ | 7.6e-12 |

**min_κ D[ON,FRONTIER] = 0.0571 (κ=5) — > tol_form=0.01.**

### 3.3 DECORR_N_FROZEN (n_matter frozen, H falls)

FRONTIER: conserves (resid 8.9e-16), closed-form dev 5.1e-12, `ρ̂(τ₁)=1.00e-2`.

| κ | D[ON,FRONTIER] | D[ON,Λ] | cons_resid | bnd | cf_dev |
|---|---|---|---|---|---|
| 0.1 | 5.7177e-01 | 3.8077e-01 | 4.4e-16 | ✓ | 8.4e-13 |
| 0.2 | 3.9033e-01 | 5.8544e-01 | 4.4e-16 | ✓ | 8.4e-13 |
| 0.5 | 1.6869e-01 | 8.1951e-01 | 8.9e-16 | ✓ | 8.4e-13 |
| **1.0** | **5.3434e-02** (min) | 9.1289e-01 | 4.4e-16 | ✓ | 8.4e-13 |
| **2.0** (fid) | **5.6090e-02** | 9.5743e-01 | 1.1e-15 | ✓ | 8.2e-13 |
| 5.0 | 1.2348e-01 | 9.8319e-01 | 6.7e-16 | ✓ | 6.4e-13 |
| 10.0 | 1.5430e-01 | 9.9163e-01 | 1.0e-15 | ✓ | 6.5e-13 |

**min_κ D[ON,FRONTIER] = 0.0534 (κ=1) — > tol_form=0.01.**

### 3.4 Integrator + conservation summary

- **Conservation:** `cons_resid ≤ 1.1e-15` for every arm/history/κ — ≪ `tol_cons=1e-8`.
  **Not bin (ii).** driver-confirmed via `src/scripts/vol_3_macroscopic/f6_tier1_two_reservoir_ledger.py::gate_conservation`.
- **Closed-form validation:** every evolved `ρ̂` matches the frozen analytic solution
  (prereg §3.4) to `≤ 1.3e-10` — the driver integrates the CHARTER §1.6 transfer laws, not
  a variant. test-locked in `src/tests/test_f6_tier1_ledger.py::test_closed_form_integrator_validation`.

---

## 4 · Audit / gate outcomes (four charter audits — honest PASS + plant TRIP)

Each gate reads the **evolved trajectory**; a sabotage plant (a modified transfer/booking
law integrated through the same ODE) trips it. All are test-locked in `src/tests/test_f6_tier1_ledger.py` (30 tests, all pass).

| Gate (CHARTER) | Honest law | Sabotage plant | Plant result |
|---|---|---|---|
| **IMPOSED-LEAK** — conservation booking (§iii) | resid ~1e-15 ≤ tol_cons ✓ | `plant_imposed_leak(η=0.5)` (bath gains ½ of source loss) | resid ≫ tol_cons → **trips** (bin ii) |
| **TRILINEAR-PUMP** — bounded-norm (§v) | ρ̂ monotone↓, total bounded ✓ | `plant_trilinear_pump(c=10)` (+c·ρ̂·Ê fed to both) | total norm runs away, `success=False` → **trips** |
| **MAGNITUDE-TUNE** — input-provenance (§4.3/§4.4) | clause (b) **both** `D[ON,FRONTIER]` **and** `D[ON,Λ]` invariant under input rescale (spreads ≤ 8.1e-13); clause (a) `gate_input_provenance` asserts `ρ_latent(t₀)==RHO_LATENT_INPUT` exactly ✓ | `plant_magnitude_tune_score` (un-normalized ρ_DE(τ₁) vs fake ρ_Λ) **and** a clause-(a) tuned-input run | score changes under rescale / tuned input `≠ RHO_LATENT_INPUT` → **both trip** |
| **DIODE-RESURRECTION** — mechanism-class (§iv) | reconstructed `g_eff` = declared `κ·n̂_B`, `rel_dev ≤ 1e-3` ✓ | `plant_diode_deadzone(ρ_f=0.5)` (drain freezes below ρ_f) | `g_eff` jumps, `rel_dev=0.42` → **trips** |

The IMPOSED-LEAK **reach limit** (CHARTER §iii) is recorded, not fixed: an honestly-booked
*conserving* friction term (`dρ̂=−γρ̂`, `dÊ_T2=+γρ̂`) conserves and is **NOT** caught —
entropic-vs-dissipative is inexpressible in two scalars and is a cited premise deferred to
a mode-carrying tier-2 test. So bin (i) certifies conservation, never entropic legality.

---

## 5 · A-priori vs actual — the CONFIRMED flag (flag-don't-fix)

### 5.1 What the charter expected vs what the ledger did

| Claim (CHARTER §4.7 / prereg §8.1) | Empirical |
|---|---|
| PHYSICAL: `D[ON,FRONTIER] ≤ tol_form` (bin iii degenerate, EXPECTED) | **FALSE** — min_κ = 0.088, fiducial = 0.150, all κ > tol_form |
| bin (i) reachable **only** via DECORRELATED lift | **FALSE** — chord separable on PHYSICAL too; decorrelation did not cross a threshold |
| DECORRELATED: `D[ON,FRONTIER] > tol_form` (lifts) | TRUE (0.057 / 0.053) — but so is PHYSICAL, so it is not a *lift* |

### 5.2 Mechanism of the falsification (named precisely, per Rule 11)

The frozen closed forms (all integrator-validated to ≤1.3e-10) are:

- ON (PHYSICAL): `ρ̂ = exp(−κ(1−1/τ))` → **plateau exp(−κ)** — Λ-like.
- FRONTIER (PHYSICAL): `ρ̂ = τ⁻² ∝ a⁻³` — matter-tracking.

These are **different functional forms**. On the FRW lock, `n_matter ∝ a⁻³` and `H ∝ a^(−3/2)`
scale with **different powers of a** (`n_matter ∝ H²`), so **no constant κ** makes
`ĝ_ON = κ·a⁻³` proportional to `ĝ_FRONTIER = 2/τ ∝ a^(−3/2)`. The best-mimic κ (κ=5 on PHYSICAL)
leaves an irreducible residual `D=0.088 ≫ tol_form`. **The FRW lock never collapses ON onto
FRONTIER**, so the physical run is not degenerate. This is exactly the tension pre-registered
in prereg §8.2 — the charter's §4.3/bin-(iii) "physical degeneracy" is in conflict with its own
§1.6/§4.7 form-inversion table, and the ledger resolves it against the degeneracy premise.

### 5.3 The §4.7 inversion, made concrete (why the bin-(i) meaning is undercut)

The chord (ON) is separable from FRONTIER by being **MORE Λ-LIKE**, not by tracking matter:
at weak coupling `D[ON,Λ]` is smallest (0.074 at κ=0.1) and `D[ON,FRONTIER]` is largest (0.84);
the **matter-tracking** form (`∝a⁻³`) is carried by the **NON-chord frontier default**. So the
frozen bin-(i) label "the DE-tracks-matter FORM exists" is, at tier-1, a demonstration that the
chord has a **distinct (Λ-trending) form** — **not** that matter-slaving produces matter-tracking
DE. This is the CHARTER §4.7 inversion realized numerically.

### 5.4 Disposition (flag-don't-fix)

Per the pre-committed disposition (prereg §8.2): the driver implemented `D[ON,FRONTIER]`
exactly as frozen and adjudicated on the actual numbers → bin (i) by the frozen §4.5 criteria.
The a-priori falsification is **surfaced with verbatim charter content + the empirical table**,
not resolved by reshaping the driver, retuning `tol_form`, or editing the charter. **Open
question for Grant/auditor:** does the always-separable / §4.7-inverted structure mean the
frozen bin (i) should be read as a genuine tier-1 form-existence result, OR does it mean the
`D[ON,FRONTIER]` metric fails to operationalize the *attribution* degeneracy the charter
conceptually intended (in which case the informative closure is still the CHARTER §4.5(iii)
statement that the homogeneous ledger is the wrong instrument, with the chord's real home the
DESI/Euclid **spatial** cross-correlation, `dark-energy-latent-heat-definition.md:159`)? This
is a framing-level adjudication (auditor + Grant), not an implementer fix.

---

## 6 · Sensitivity ladder (NON-FROZEN — transparency only)

The FROZEN verdict uses `tol_form=1e-2` only. The `min_κ D[ON,FRONTIER]` per history against
the candidate ladder (prereg §4):

| History | min_κ D | ≤1e-3 | ≤1e-2 (FROZEN) | ≤1e-1 | ≤3e-1 |
|---|---|---|---|---|---|
| PHYSICAL | 0.0877 | ✗ | ✗ (separable) | ✓ | ✓ |
| DECORR_H_FROZEN | 0.0571 | ✗ | ✗ (separable) | ✓ | ✓ |
| DECORR_N_FROZEN | 0.0534 | ✗ | ✗ (separable) | ✓ | ✓ |

**Threshold-proximity note (material for adjudication):** the best-mimic separation sits at
`D ≈ 0.05–0.09`. At the frozen `tol_form=1e-2` the chord is **separable** (bin i); at a looser
`tol_form ∈ [0.1, 0.3]` it would read **degenerate** (bin iii) — i.e. the physical-degeneracy the
charter expected reappears one order of magnitude up. The verdict is therefore sensitive to the
threshold within an order of magnitude of the frozen value. This is reported, not used to move the
frozen verdict (Rule 11 — no post-hoc threshold selection).

**Fine-κ + window robustness (adversarial-review addendum, `review:degeneracy-knife`).** The
`min_κ` in the table above is over the FROZEN 7-point scan. An independent fine scan (600 log-points,
`κ ∈ [1e-3, 1e3]`) gives the TRUE **global** min `D[ON,FRONTIER]`: **0.046 (PHYSICAL, κ≈3.3)**, 0.048
(DECORR_H, κ≈4.1), 0.033 (DECORR_N, κ≈1.4) — all still `> tol_form=1e-2`. **No κ makes the physical
run degenerate**, so the a-priori falsification is not a coarse-scan artifact. Window sweep
`τ₁ ∈ {2,3,5,10,20}` gives `min_κ D_physical ∈ [0.024, 0.046]` — **separable throughout** at
`tol_form=1e-2`. The falsification is robust to κ-refinement and window choice. (Live-fire lens
`review:live-fire` independently reproduced every shipped `D` with a different solver `scipy.odeint`
+ different quadrature `scipy.integrate.simpson` to max relative Δ = 3.1e-8.)

### 6.1 · Λ-degeneracy boundary — the two-limits map (NON-FROZEN, 2026-07-13; independent-review R1)

**Beyond-frozen-window transparency — no verdict change.** The frozen bins consume `D[ON,FRONTIER]`
on the frozen window `[1,10]` only; nothing below moves the §1 verdict. This map quantifies *how
Λ-like the chord is* — the exact quantity the §5.4 adjudication (genuine tier-1 form-existence vs
wrong-instrument) turns on — so the reader need not derive it. All numbers reproduced by
`src/scripts/vol_3_macroscopic/f6_tier1_two_reservoir_ledger.py::lambda_boundary_map` (banked in the
NON-FROZEN key of the results JSON; test-locked in `src/tests/test_f6_tier1_ledger.py::test_lambda_boundary_map_two_limits`).
**The two-limits map arms Grant's §5.4 call; it does not make it.**

**(a) Weak-κ limit — the chord collapses onto Λ.** The shipped `min_κ D[ON,Λ]=0.0737` is a **frozen-scan
edge** (argmin at the smallest grid κ=0.1); the true **infimum over κ is 0** (κ→0 shuts the drain off and
ON ≡ Λ). On the frozen PHYSICAL window, **`D[ON,Λ] ≤ tol_form=1e-2` for all κ ≤ 0.013** (floor
`D[ON,Λ]=7.67e-4` at κ=1e-3). So at weak slaving the chord IS a bare cosmological constant in this observable.

**(b) Late-window limit — the chord converges onto Λ (window-START sweep, PHYSICAL, κ_fid=2).** The chord's
separability-from-Λ is anchored to the **drain-turn-on transient**; slide the window to later decades and it
decays:

| window | D[ON,Λ] | D[ON,FRONTIER] |
|---|---|---|
| [1, 10] | 0.7653 | 0.1498 |
| [3, 30] | 0.3954 | 0.5205 |
| [10, 100] | 0.1416 | 0.7737 |
| [30, 300] | 0.0498 | 0.8653 |
| [100, 1000] | 0.0152 | 0.8997 |
| [300, 3000] | **0.0051** (≤ tol_form) | 0.9098 |
| [1000, 10000] | 0.0015 | 0.9133 |

`D[ON,Λ]` crosses `tol_form=1e-2` at window start `τ₀ ≈ 300`: **in any late decade window the chord IS Λ**
in the homogeneous observable (the CHARTER §1.6 "residual constant → Λ-like at late t", made quantitative),
while `D[ON,FRONTIER]` rises toward ~0.91.

**(c) Genuine-form-existence limit — at the frontier-best-mimic κ the chord is FAR from Λ (frozen window).**
Stated with equal prominence:

| History | κ_best (min D[ON,FRONTIER]) | D[ON,FRONTIER] | **D[ON,Λ]** |
|---|---|---|---|
| PHYSICAL | 3.28 | 0.0456 | **0.8952** |
| DECORR_H_FROZEN | 4.13 | 0.0482 | **0.9342** |
| DECORR_N_FROZEN | 1.37 | 0.0327 | **0.9370** |

**Reading (for §5.4, not adjudicated here):** the chord occupies an intermediate band — it is Λ in the
weak-κ (a) and late-window (b) limits, and clearly non-Λ (D[ON,Λ] ≈ 0.90–0.94) at the frontier-best-mimic
κ on the frozen turn-on window (c). Whether the frozen `[1,10]`/κ-scan instrument samples the (c) regime as
a genuine tier-1 form-existence result, or whether (a)+(b) mean the homogeneous ledger is the wrong
instrument (chord's real home = DESI/Euclid **spatial** cross-correlation), is the framing call handed to
Grant/auditor. Implementer surfaces the map; does not decide.

---

## 7 · Quarantine + scope discipline (binding reminders)

- The **cascade address** (F6 = the A-class drainage of the LOCAL top port; `Re(Z)≠0` one-way at
  the Machian-horizon termination) remains a **★QUARANTINE Grant-walked ruling-grade INPUT**
  (CHARTER §1.4) — premise-under-test; **must not** be cited elsewhere as established corpus physics.
- **Sector ⊥:** the transfer axis is the static-sector store ρ_latent → T2. A1 dilatation-mass and
  Cosserat-winding sectors appear only as (tier-2, deferred) constraints, never as the source.
- **CONSISTENCY ceiling, refuse EMERGENCE:** `κ` is free (not from `{ℓ_node, α, G}`); a bin-(i)
  form is *constructed*, not emergent. The AVE-distinct content remains the DEFINITION / MECHANISM
  tag (`dark-energy-latent-heat-definition.md:113`), not a realized DE-tracks-matter chord.
- **No KB-leaf / manuscript edits in this PR.** The empirical finding (a-priori falsified; §4.7
  inversion realized) is surfaced for the auditor lane to land any corpus/manual entry; the
  implementer does not draft it.

---

## 8 · References

- CHARTER `research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md` (§1.6, §4.3, §4.5, §4.7).
- FROZEN prereg `research/2026-07-13_f6-tier1-ledger-driver_prereg.md` (§4 tolerances, §8.2 flag).
- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:113,143,156,159`
  (consistency tag; reading-ii frontier default; F6 gate-3 `{ℓ_node,α,G}`; DESI/Euclid spatial home).
- `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:8,58-62` (10^122 rejected).
