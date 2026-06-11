# RESULT — THE SCREENED-WINDING PROBE: `w_pol ≡ 0` is a GENUINE absence, NOT an apparatus screen

**Date:** 2026-06-11
**Branch:** `analysis/2026-06-11-screened-winding-probe` (off `origin/analysis/2026-06-10-genesis-v6-transducer` @ `7484dd0b`)
**Prereg (FROZEN, committed ALONE @ `dbb67e72`):** [`research/2026-06-11_screened-winding-probe_prereg.md`](2026-06-11_screened-winding-probe_prereg.md)
**Driver:** `src/scripts/vol_1_foundations/screened_winding_probe_run.py`
**Results JSON:** [`research/2026-06-11_screened-winding-probe_results.json`](2026-06-11_screened-winding-probe_results.json)
**Scale:** N=32, N_form=1300, seed=20260611 (MODEST scale — declared engineering choice per §5/§210; the v6 MAIN was N=48. FROZEN bins/thresholds UNCHANGED.)

---

## VERDICT (written FROM the evaluated gate booleans — Rule 11)

# **BIN = NO-SCREENING.**

The apparatus reads a known-planted `(2,3)` ω winding FAITHFULLY through a formed snap shell. The prior v6 product verdict — **the poloidal "3" never forms (`w_pol ≡ 0`)** — therefore **STANDS, and is now EXONERATED of the screening confound.** The absence is a genuine absence, not a reader that cannot see inside the shell.

`keeper.passes=True` · `G_CAL=True` · `ARM1=NO-SCREENING` · `ENVELOPE_overlay=None`

> **PANEL-DEMOTED (2026-06-11 — see §8, appended; §1–§7 preserved as written).** The BIN stands at GATE level, but the headline "reads a planted (2,3) FAITHFULLY through a formed shell / EXONERATED" is demoted: ARM 1 is a tautological calibration (transducer-OFF ⇒ the ω read channel is structurally decoupled from everything the snap touches, so T≡1.0 BY CONSTRUCTION), the plant sat AT the shell's outer edge (`R=R_shell=shell_rho_max`, nominal), and no ARM-1 field map was rendered. The genuine-absence conclusion rests on **ARM 2 interior reads + the code-proven snap/ω decouple**, NOT on ARM 1. Empirical through-shell screening in a COUPLED config: **UNTESTED**. Panel not clean (1/2 lenses refuted) ⇒ branch NOT pushed.

---

## 1. THE APPARATUS CONFESSION + SNAP-ERASURE INVENTORY — CONFIRMED AT THE ARRAY LEVEL

**The confession (verify-before-cite, exact cites @ `7484dd0b`, re-grepped this session):**

| field | snap action | line |
|---|---|---|
| `u_adv` (bulk advective velocity) | **→ 0.0** at every snapped cell, every step | `unified_genesis_engine.py:396` (`self.u_adv[cm]=0.0`, `cm=snap_mask` @ `:385`) |
| `u_adv` (newly-snapped) | `*= (1 − chi_shock)` (full removal, `chi_shock=1.0`) | `:344` |
| `rho_bar` (bulk density) | **clamped to the void floor** | `:393` (conservative) / `:395` (legacy) |
| `omega`, `pi_omega`, `w`, `V` | **NEVER WRITTEN** by the snap (grep `_tally_latent_and_snap`/`_snap_step` `:304–419` → ZERO writes) | — |

The parent `CrystalGraftV4.step()` (`unified_genesis_engine.py:852`, `super().step()`) evolves `ω/V/w` UNCHANGED. The `(2,3)` extractor reads ONLY `ω` and `π_ω`.

**CONFIRMED in-run (ARM 1 `decouple` block, all three shell thicknesses):**

| measurement | thin (M=2.6) | nominal (M=2.8) | thick (M=3.4) | meaning |
|---|---|---|---|---|
| `median \|u_adv\|` in snapped cells | **0.00e+00** | 0.00e+00 | 0.00e+00 | `:396` zeroes it — confirmed |
| `median \|ω\|` in snapped cells | **4.54e-05** | 6.10e-05 | 4.99e-05 | ω PRESERVED inside the shell — confirmed |
| `max\|ω(snapON) − ω(snapOFF)\|` | **0.00e+00** | 0.00e+00 | 0.00e+00 | the READ channel is byte-identical |
| `max\|w_…\|`, `max\|V_…\|` (on−off) | 0.00e+00 | 0.00e+00 | 0.00e+00 | photon + longitudinal byte-identical |
| snap-OFF control bulk nonfinite cells | **13824 / 13824** | 0 | 13824 / 13824 | the snap-OFF bulk DETONATES (v5 behavior) |

The bulk sectors diverge **maximally** (the snap-OFF control bulk detonates to nonfinite across the entire 24³ interior; the snap-ON bulk is clamped finite) — yet `ω`, `w`, `V` are **bit-identical**. With the transducer OFF, the ω read channel is **dynamically decoupled** from the snap-controlled bulk sector. The naive read of the directive's confession — *"any circulation entering the shell is erased by bookkeeping"* — is **EXACTLY TRUE for the bulk `u_adv` circulation (Γ=∮u·dl)** and **EXACTLY FALSE for the Cosserat ω winding (the read channel)**, precisely as the §1 inventory predicted (the two homonymous circulations).

---

## 2. ARM 1 — THE SCREENING CALIBRATION (the never-run KNOWN-POSITIVE)

**Procedure:** ATTEMPT-A fired (plant AFTER forming the shell; the snap never writes ω so the plant survives). A validated `(2,3)` (`seed_omega_known_2_3`, R=R_shell, r=R_shell/φ², amplitude 0.40) planted co-located with the snapped shell into BOTH a snap-ON engine and a byte-paired snap-OFF control. Read at the §5 contour-radius sweep `{0.5,0.7,0.9,1.0,1.15,1.3,1.6}×R_shell`. Keeper (`verify_equivalence`) PASSED (planted→is_2_3, null→(0,0), ≤1e-12 vs reference).

**The screening transfer T(r) = w_pol_rel(snap-ON) / w_pol_rel(snap-OFF), per contour radius (the §1 same-contour screening model):**

| frac × R_shell | 0.5 | 0.7 | 0.9 | 1.0 | 1.15 | 1.3 | 1.6 |
|---|---|---|---|---|---|---|---|
| **T(r)** | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| byte-identical on/off | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| OFF `is_2_3` | F | F | **T** | **T** | **T** | F | F |

`all_radii_byte_identical=True`, `max|T−1| = 0.00e+00`, across thin/nominal/thick (T at the natural radius = 1.0 for all three; `T_tracks_shell_thickness=False`). The planted `(2,3)` reads `is_2_3=True` **inside (frac 0.9), at (frac 1.0), and outside (frac 1.15) the shell** — byte-identically with the shell present or absent (see [`fig_swp_arm1_transfer.png`](figures/fig_swp_arm1_transfer.png)).

**Frozen §3 gate booleans (nominal M=2.8 shell, t0 read):**
`G_CAL=True` (read_c is_2_3, rel=0.146 ≥ REL_MIN=0.10) · `G_IN=True` (read_b inside frac0.9 is_2_3, T_b=0.872 ≥ 0.70) · `G_OUT_T=True` (read_a outside frac1.15 is_2_3, T_a=2.224 ≥ 0.70) · `G_OUT_S=False` → **ARM1 = NO-SCREENING.** Per-radius corroboration: `T_b=T_a=1.0000`, `ARM1_perradius=NO-SCREENING`. Both agree.

---

## 3. ARM 2 — INTERIOR READS ON THE PRODUCT (the v6 transducer, rebuilt)

The v6 product (`bulk_density_on`, `snap_on`, `transducer_on` all True) rebuilt at N=32, `omega_recipient_frac` swept `{0.0, 0.5, 1.0}`. Reads at the §5 radius sweep; raw-field meridian maps dumped (the money figure).

| omega_recipient_frac | 0.0 | 0.5 | 1.0 |
|---|---|---|---|
| `prod_best_rel` (best contour reliability) | 0.81334 | 0.81334 | 0.81334 |
| `any_is_2_3` over all radii | **False** | **False** | **False** |
| `omega_med_in` (inter-shell annulus) | 7.00e-05 | 7.01e-05 | 7.02e-05 |
| `G_PROD_NULL` | False | False | False |

`OMEGA_FLOOR = 2.081e-04` (3× transducer-OFF baseline 6.938e-05). The interior ω is at the known-null floor (`omega_med_in 7e-05 < OMEGA_FLOOR`). **`w_pol = 0` at EVERY radius, EVERY `omega_recipient_frac`** — the poloidal "3" never forms. The product's readable ω is a topologically-trivial **core blob** (see the money figure [`fig_swp_arm2_interior_fields.png`](figures/fig_swp_arm2_interior_fields.png): `|ω|` peaks at the core, ~0 at the shell walls where the snap clamps ρ̄ and zeroes `u_adv`; [`fig_swp_arm2_product_read.png`](figures/fig_swp_arm2_product_read.png)).

---

## 4. ARM 3 — TIME-RESOLVED (phase-locked vs settled)

`settled_avg_rel=0.154`, `settled_avg_is_2_3=False`. `G_ENV=False` for all `N_phase ∈ {1,4,8,16}` — no phase resolves a `(2,3)` the settled average hid (consistent: there is no readable `(2,3)` to be phase-hidden). See [`fig_swp_arm3_envelope.png`](figures/fig_swp_arm3_envelope.png).

**§210 DEVIATION (declared):** the in-run internal oscillator (`wall_photon_intensity`) showed **no clean dominant period** in the recording window (FFT peak landed at ≈1/window ⇒ `f0_well_defined=False`, `T0` fell back to the window length 1100). The prereg's expected `f₀≈0.052`→`T₀≈500 steps` is **NOT confirmed at N=32**. The envelope test is therefore inconclusive-but-moot (no readable winding to phase-resolve); it does not change the BIN.

---

## 5. THE EXECUTABLE DECISION TREE (§4.2 — evaluated, not narrated)

```
keeper.passes = True                          → not HALT
G_CAL = True                                  → not HALT
ARM1: G_IN ∧ G_OUT_S = False ; G_OUT_T = True → ARM1 = NO-SCREENING
G_PROD_NULL (all omega_frac) = False
  ⇒ (ARM1==NO-SCREENING ∧ prod_null_all)=False → not ALL-NULL
  ⇒ ARM1==NO-SCREENING                          → BIN = NO-SCREENING
G_ENV = False                                   → no ENVELOPE overlay
```

**BIN = NO-SCREENING.** The apparatus is faithful; the product read is the real verdict, and it reads `w_pol = 0`.

---

## 6. FLAGS (flag-don't-fix — surfaced, NOT silently reconciled)

1. **The §0.5 CHANNEL-MISMATCH is RESOLVED and dissolved.** The prereg flagged that "screening" and "wrong-channel" were confounded in the product. ARM 1 proves the snap does NOT screen the ω read (byte-identical). ARM 2 proves the product read does NOT track `omega_recipient_frac` (`prod_best_rel` = 0.81334 identical to 6 sig figs across 0/0.5/1.0) — so even routing 100% of the transduced helicity into the ω read channel produces **no** readable `(2,3)`. **Neither screening NOR channel-routing explains the absence.** The winding genuinely does not form at this scale; the transducer's deposit into the readable ω structure is negligible.

2. **The frozen §3 `T_b`/`T_a` are CROSS-RADIUS** (read at one radius ÷ control at the natural radius), so they fold the bare plant's radial reliability PROFILE into the ratio (a non-screening effect). Per §1 the screening is the **SAME-contour** snap-ON/OFF ratio = **1.0000 exactly**. Both the frozen formula and the confound-free per-radius transfer give `ARM1=NO-SCREENING`; the result is robust to the ambiguity. Reported, not reconciled.

3. **`G_PROD_NULL` gate semantics.** The product reads `w_pol=0` on RELIABLE contours (`best_rel=0.813`). The frozen gate `G_PROD_NULL = (best_rel < REL_MIN) ∧ (omega_med_in ≤ OMEGA_FLOOR)` does NOT fire (0.813 > 0.10), so the tree returns NO-SCREENING rather than ALL-NULL. But "a reliable contour reads ZERO winding" IS the strongest form of the prior verdict (genuinely absent). **NO-SCREENING and ALL-NULL coincide in substance here:** the apparatus reads faithfully AND what it faithfully reads is `w_pol=0`. The gate distinguishes "no reliable contour" from "reliable contour reads zero"; the substantive finding is the latter.

---

## 7. CORPUS STATE + ADJUDICATION

- **consistency-vs-emergence tag: MANIFESTATION/consistency-class.** This probe tested whether the apparatus faithfully reads a KNOWN-PLANTED invariant through a shell. No emergence claim; no CODATA/manuscript target compared.
- **A44:** NO-SCREENING is an APPARATUS-reach finding (the reader CAN see inside the shell). It is NOT a missing axiom and NOT an engine-violates-Ax3 bug. No Ax5 candidate drafted.
- **Rule 11 (honest closure):** ARM 1 = NO-SCREENING (proven byte-identical) and ARM 2 = `w_pol≡0` (read faithfully). This is the CLEAN strongest form of the prior verdict — recorded, branch closed, NOT debugged toward a screening rescue.
- **Rule 12:** the prior `w_pol≡0` verdict is NOT retracted — it STANDS, now exonerated of the screening confound. No 🔴 re-scope header is warranted (SCREENED-READ-CONFIRMED did not fire). No slot refilled.
- **Lane:** implementer surfaces the empirical finding + the §6 flags; the auditor lands any manuscript / `COLLABORATION_NOTES` entry.

**Figures:** `research/figures/fig_swp_arm1_transfer.png`, `fig_swp_arm2_interior_fields.png` (the money figure), `fig_swp_arm2_product_read.png`, `fig_swp_arm3_envelope.png`.

---

## 8. PANEL ADJUDICATION (2026-06-11) — VERDICT DEMOTED (appended per Rule 12; §1–§7 preserved as written)

**Panel: 2 lenses. CALIBRATION INTEGRITY → refuted=TRUE. TIME-RESOLUTION + RE-SCOPE DISCIPLINE → refuted=FALSE.** Panel NOT clean ⇒ per the panel-clean rule this branch is **NOT pushed, NO PR**. The demotion below is the final honest verdict. All panel cites re-verified against driver + JSON this session (verify-before-cite).

### 8.1 What the panel refuted (lens 1 — three findings)

1. **ARM 1 is a TAUTOLOGY, not an empirical screening calibration.** With the transducer OFF, the ω read channel has zero back-coupling to the snap-controlled bulk (the §1 decouple proof: `max|Δω|=0.00e+00` while the snap-OFF control bulk detonates 13824/13824 nonfinite). The snap-ON/OFF transfer is therefore forced to T≡1.0000 **BY CONSTRUCTION**; the thickness sweep (thin/nominal/thick, §210-executed) **cannot discriminate** (`T_tracks_shell_thickness=False`, T=1.0 at all three). ARM 1 is hereby **re-labeled: a code-level decouple proof (the snap writes ZERO to ω/π_ω/w/V — `unified_genesis_engine.py:304–419`), NOT an empirical through-shell read calibration.**
2. **The plant was AT the shell edge, not INSIDE it.** Driver `screened_winding_probe_run.py:175`: `seed_omega_known_2_3(R=R_shell, …)`; JSON nominal `R_shell = 6.9642 = shell_rho_max` (the OUTER edge of the 6.04–6.96 snapped band); thin (M=2.6) is degenerate (`shell_rho_min = shell_rho_max = R_shell = 6.5192`, zero radial thickness); thick (M=3.4) puts the plant at the INNER edge (`R_shell = 6.5192 = shell_rho_min`). "Planted INSIDE a formed shell" is **not certified**.
3. **No ARM-1 field map exists.** `dump_fields` fires only at driver `:366` inside `arm2()` on the PRODUCT engine (transducer ON, no plant) — the rendered fields figure is of a different engine than the one carrying the plant. The plant-in-shell geometry is asserted, not shown.

Corollary (extends §6 flag 2): the frozen cross-radius `T_a=2.224` clears `G_OUT_T` only via cross-radius normalization, and the same-contour T=1.0 corroboration is itself **vacuous** — the snap-OFF "control" ω field is byte-identical to the snap-ON field, so it is not an independent free-space control.

### 8.2 The DEMOTED verdict

- **BIN = NO-SCREENING stands at GATE level** (Rule 11: the frozen gates fired as frozen; no post-hoc criterion drop). The HEADLINE claim is demoted into three honest tiers:
  1. **CODE-PROVEN (stands):** the snap erases the bulk circulation Γ=∮u_adv·dl (`:396` `self.u_adv[cm]=0.0`; `:344` shock strip at crossing) and clamps ρ̄ (`:393`/`:395`) — and writes **nothing** to ω/π_ω/w/V (`:304–419`; array-confirmed `max|Δω|=max|Δw|=max|ΔV|=0.00e+00`). The directive's "circulation erased by bookkeeping" is **exactly true for `u_adv` and exactly false for the Cosserat ω read channel**.
  2. **EMPIRICALLY UNTESTED (the demotion):** through-shell read of a winding in a **COUPLED** config (transducer ON — the only bulk→ω path in this engine). ARM 1 ran in the one regime where indirect screening is identically zero; no known-positive was run coupled. "The apparatus does not screen" is over-generalized as stated in the §-headline.
  3. **LOAD-BEARING EMPIRICAL CONTENT (stands, re-attributed to ARM 2):** the coupled product itself reads `w_pol=0` on **reliable** contours (`best_rel=0.813`) at ALL radii **including interior fracs 0.5/0.7/0.9 — interior reads cannot be through-shell screened** — and the read is insensitive to `omega_recipient_frac` to 6 significant figures across 0/0.5/1.0, with inter-shell `median|ω|=7.0e-05` at the transducer-OFF floor. Genuine absence rests on **ARM 2 + tier 1**, not on ARM 1's tautological transfer.

- **Honest corpus entry (per panel residual-risk):** *"snap writes zero ω (code-proven); the v6 product's readable ω is a topologically-trivial core blob reading w_pol=0 on reliable interior contours; empirical through-shell screening untested in any coupled config."* Do **NOT** propagate the "EXONERATED" framing to manuscript / `COLLABORATION_NOTES` until ARM 1 is either re-run in a coupled regime or re-rendered with a plant-in-shell field map (plant moved interior: `R < shell_rho_min`).

- **Scope boundary the demotion makes explicit (the v8-relevant question):** this probe answered the **READ** question (is a formed winding hidden from the extractor?). It did NOT answer the **FORMATION** question — whether the snap's `u_adv` erasure at the wall (`:396`) *prevents* orbital circulation from ever twisting into poloidal winding. The prior `w_pol≡0` verdicts stand as READ verdicts (the winding truly is not in the ω field); apparatus-caused formation-suppression remains open.

### 8.3 What stands of §4/§7 (lens 2 — PASS)

- **ARM 3 stands as declared-moot** (§210 deviation honestly disclosed; `f0_well_defined=False`, FFT peak = 1/window). `G_ENV=False` is **not** evidence of "no envelope structure" — do not cite it as such. A probative re-run requires the internal oscillator resolved (period ≪ window) at N=48 BEFORE phase-binning.
- **Rule 12 unchanged:** no 🔴 re-scope header (SCREENED-READ-CONFIRMED did not fire); prior `w_pol≡0` verdicts (v5–v7) STAND — supported by ARM 2 interior reads + the tier-1 code decouple.
- **Disposition:** committed on-branch, `make verify` green, **unpushed, review-gated** (panel not clean).
