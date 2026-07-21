# RESULT — v1 spin-mapping frozen adjudication: **MIXED (ω_R matches, τ does not)**

**Lane:** v1-spin-mapping-adjudication (routed follow-on of PR #774's § FORK-REOPEN)
**Date:** 2026-07-20
**Prereg (frozen, criteria set before run):** [`2026-07-20_v1-spin-mapping-adjudication_prereg-FROZEN.md`](2026-07-20_v1-spin-mapping-adjudication_prereg-FROZEN.md)
**Driver (deterministic):** [`2026-07-20_v1-spin-mapping-adjudication_rerun.py`](2026-07-20_v1-spin-mapping-adjudication_rerun.py)
**Upstream:** PR #774 (`fix/kerr-qnm-table-correction` @ `7aaec46c`, UNMERGED — all #774 cites tagged `[branch @ 7aaec46c]`).

> **This is the reopened fork's evidence brief, not the ruling.** The v1↔v2 fork RULING remains
> Grant's (standing authorization: derivation-class proceeds; the fork verdict is his). Every number
> below ships with its computation in the committed driver (anti-seduction, prereg §0).

---

## ★ Frozen-bin verdict (prereg §5)

> **OVERALL: MIXED (ω_R vs τ split).**
> - **ω_R — V1-MATCHES (primary), marginal (secondary).** On the frozen C-1 dimensionless comparator,
>   v1 sits **+2.63% mean** on the primary banked catalog (inside the `|D̄| < 3%` MATCH band), vs v2's
>   **−9.53%** (FAILS). On the secondary higher-spin extension v1 is **+3.36% mean** (marginal, 3–5%),
>   vs v2's **−11.70%**. v1 outperforms v2 at every spin; its overshoot *grows monotonically with spin*
>   (crosses +3% near a* ≈ 0.73, +5% near a* ≈ 0.88).
> - **τ — V1 does NOT clean-match; the ω_R and τ verdicts split.** Under the ONE fully-specified AVE
>   damping model (cold topological `Q = ℓ = 2`, `qnm-quality-factor.md`, clm-395gps), v1 (and v2)
>   **FAIL** at catalog spins: `D̄_Q = −38.18%` (AVE Q = 2 vs corrected-Kerr Q rising 3.07→3.49).
>   v1's *actual* corpus τ prediction (the spin-refined `ω_I = (ω_R − mΩ)/2ℓ` giving the KB τ =
>   3.5/2.7/1.2 ms) is **UNDETERMINED** — its frame-dragging rate Ω is **not numerically pinned anywhere
>   in the corpus** (the τ values were asserted at initial release, not coded). The lane **declines to
>   fabricate Ω** to manufacture a τ match (anti-seduction).

So the ω_R rescue of the reopened fork is **real**; the τ side is **where the rescue does not carry** —
either it fails (fully-specified cold model) or it is undetermined (the spin-refined model whose Ω was
never derived). The ω_R and τ verdicts split, which is the frozen **MIXED** bin.

---

## Leg 1 — corrected Kerr re-verified in-lane (second method: BCW-2006)

The corrected Kerr (2,2,0) reference `[branch @ 7aaec46c]` (qnm/Stein-2019 high-precision Leaver) is
re-verified in-lane by the **Berti-Cardoso-Will 2006 analytic fits** (Phys.Rev. D73 064030), computed in
the driver so the cross-check ships with the verdict:

- ω_R: `ω_R·M = 1.5251 − 1.1568(1−a*)^0.1292`
- Q:   `Q = 0.7000 + 1.4187(1−a*)^−0.4990`,  `ω_I·M = ω_R·M/(2Q)` — **independently reproduces the
  corrected ω_I table**, which the #772 digest did not separately verify.

Worst |BCW − qnm| over the adjudicated spins {0.64, 0.67, 0.74, 0.90, 0.95} = **0.97%** (both observables;
frozen assertion < 1.5% → PASS). The a*=0 row is the exact Schwarzschild anchor (BCW is known ~1.4–2.3%
low at zero spin, #774 §0). The extremal ZDM analytic limit (ω_R·M → m/2 = 1, ω_I·M → 0 as a* → 1) is the
third, table-free cross-check the in-repo table grossly violated. **Both corrected tables confirmed by a
second independent method.**

## Leg 2 — ω_R (C-1 dimensionless, frame- & mass-independent)

| event | a* | v1 ω_R·M | v2 ω_R·M | Kerr ω_R·M | **v1 dev** | v2 dev | Kerr src |
|---|---|---|---|---|---|---|---|
| GW170104 | 0.64 | 0.51955 | 0.46456 | 0.50819 | **+2.24%** | −8.59% | qnm `[br@7aaec46c]` |
| GW150914 | 0.67 | 0.53284 | 0.47208 | 0.51986 | **+2.50%** | −9.19% | qnm `[br@7aaec46c]` |
| GW151226 | 0.74 | 0.56910 | 0.49191 | 0.55163 | **+3.17%** | −10.83% | qnm `[br@7aaec46c]` |
| **PRIMARY mean** | | | | | **+2.63%** | **−9.53%** | |
| GW190521 (2nd) | 0.72 | 0.55786 | 0.48587 | 0.54373 | **+2.60%** | −10.64% | BCW-fit `[in-lane]` `[IMPORT: GWTC-2 a*]` |
| GW170729 (2nd) | 0.81 | 0.61610 | 0.51623 | 0.59169 | **+4.13%** | −12.75% | BCW-fit `[in-lane]` `[IMPORT: GWTC-1 a*]` |
| **SECONDARY mean** | | | | | **+3.36%** | **−11.70%** | |

The **+2.63% primary mean reproduces #774's § FORK-REOPEN table exactly** (per-event +2.24 / +2.50 / +3.17)
`[branch @ 7aaec46c]` — two-method agreement (this lane's independent driver + #774's review computation).
v1 lands **inside the frozen MATCH band on the primary set**; the secondary higher-spin set pushes it to
**marginal** because v1's overshoot grows with spin. This primary-vs-secondary drift is itself a component
of the MIXED bin (prereg §5).

## Leg 3 — τ / damping (THE NEW CONTENT: v1's τ vs the corrected ω_I table)

The comparator is the dimensionless quality factor `Q = (ω_R·M)/(2·ω_I·M)` (frame- & mass-independent,
parallel to C-1). Corrected-Kerr Q rises with spin: **3.07 (a*=0.64) → 3.18 (0.67) → 3.49 (0.74)**.

**Model A — cold topological `Q = ℓ = 2`** (`qnm-quality-factor.md`, clm-395gps; FULLY SPECIFIED,
spin- and v1/v2-independent):

| event | a* | Q_AVE (A) | Q_Kerr | ω_I·M AVE | ω_I·M Kerr | **Q dev** |
|---|---|---|---|---|---|---|
| GW170104 | 0.64 | 2.000 | 3.071 | 0.12989 | 0.08275 | **−34.87%** |
| GW150914 | 0.67 | 2.000 | 3.176 | 0.13321 | 0.08185 | **−37.02%** |
| GW151226 | 0.74 | 2.000 | 3.487 | 0.14228 | 0.07909 | **−42.65%** |
| **mean** | | | | | | **−38.18% → τ-FAILS** |

The spin-independent `Q = ℓ = 2` cannot spin up; corrected Kerr Q rises to ~3.5 at catalog spins, so the
one fully-specified AVE damping model **fails decisively on τ**. (The register rationale for clm-395gps
already flagged this: *"Q = ℓ disagrees with GR overtone structure"* — Leg 3 quantifies it against the
corrected ω_I.)

**Model B — spin-refined `ω_I = (ω_R − mΩ)/(2ℓ)` at `r_Ω = r_ph·√(1+ν_vac)`** (this is v1's *actual*
corpus τ prediction, the KB τ = 3.5/2.7/1.2 ms): **UNDETERMINED.** The frame-dragging rate `Ω(a*)` is
**not numerically pinned anywhere in the corpus** — grep returns no numeric Ω / r_Ω; the τ values were
asserted at initial release (`de9d2293`), never coded. Per the anti-seduction clause the lane declines to
fabricate Ω. A **disclosed, non-frozen** reverse-engineering of the rounded KB τ (at source-frame masses)
gives Q_v1(implied) ≈ {2.92, 3.05, 3.33} vs Kerr Q {3.07, 3.18, 3.49} — suggestively close (~4%), **but**
it is 2-sig-fig-rounding-limited AND rides the very source-frame masses #774 flagged as contaminated, so
it is **not frozen-adjudicable**. That the mΩ model *can* be brought near Kerr Q only by a hand-tuned Ω is
exactly why the banked τ_v2 = −0.47% "match" (frame- + ω_I-table-contaminated) is not evidence.

> **Flag (don't fix) — a τ specification gap + an internal tension for Grant/auditor.** (1) v1's τ
> prediction cannot be frozen-adjudicated until Ω is derived (or the KB τ values re-derived) — the
> corpus under-specifies the spinning damping. (2) Three corpus statements about Q need reconciling:
> `qnm-quality-factor.md` says `Q = ℓ` (spin-independent); `ave-merger-ringdown-eigenvalue.md` says Q
> *"increases with spin"*; Phase-5 (`ligo-ringdown-driver-design.md` §10) says Q is *v1/v2-invariant*.
> A proper τ adjudication needs these three pinned first. Surfaced, not resolved.

## Leg 4 — v1-provenance grade

The v1 spin mapping `x_sat,v1 = 7·r_ph⁺/3M` is the **Kerr extension of claim clm-395gps** (canonical
`vol3/claim-quality.md`; hosted `ave-merger-ringdown-eigenvalue.md` + `qnm-quality-factor.md`).
Register grade (queried via `kb_cmd show clm-395gps`):

- **solidity 0.55** (confidence 0.80), **build_status: "use as input only, don't build deeper"** (band `input-only`).
- Rationale (verbatim key phrase): the cold Schwarzschild eigenvalue `18/49` is a *"genuine 1.7%-error
  category-(iv) derived prediction"* (clean, zero-free-parameter: `r_sat = 7M` from Ax 4, `r_eff = 49M/9`
  via Poisson ν_vac, `ω_R = ℓc/r_eff`); the band is *"held below 0.9 because the Kerr extension rests on a
  **disclosed phenomenological** photon-sphere shift + Cosserat back-reaction fit … and Q = ℓ disagrees
  with GR overtone structure"*.

**Grade for the fork:** the register **already** classifies BOTH v1 and v2's spin corrections as *disclosed
phenomenological* — neither is a first-principles derivation. v1's provenance is therefore **not more
derived than v2's**; v1 is the *simpler* phenomenology (single-component whole-cavity-compliant geometric
photon-sphere ratio) and v2 the two-component post-hoc fit. What the cold anchor cleanly derives — `x_sat = 7`
(Ax 4) and `ν_vac = 2/7` (GR-imported VALUE via K=2G / PR #261, FORM-derived) — is **shared by both**; the
`/3M` is the Schwarzschild photon sphere `r_ph,Schw = 3M`. The combined `7/3` is thus (saturation radius /
photon-sphere radius), a ratio of two distinct geometric radii — **not** a member of the PPN `/7`-coupling
family; the shared object is only the Ax-4 saturation multiplier `7` (the same `7` in `g_* = 7³/4`).
**Connection noted; no new claim minted.**

> **Flag (don't fix) — stale register rationale.** clm-395gps's rationale cites *"the spinning-remnant
> comparisons (10–18% pre-Kerr-correction) are the disclosed weak edge"*. That "10–18%" is v1's
> **frame-mixed artifact** (#774), not a dimensionless comparison to true Kerr — against corrected Kerr,
> v1 is +2.63% (primary). The register rationale is stale on this number; auditor/Grant lands the
> correction after the fork ruling (research-doc only this lane; no KB edit).

## Leg 5 — near-extremal (v1 vs v2 vs exact ZDM) — a routed organizer candidate

| a* | v1 ω_R·M | v2 ω_R·M | Kerr ω_R·M | v1 dev | v2 dev |
|---|---|---|---|---|---|
| 0.90 | 0.70741 | 0.55944 | 0.67161 | **+5.33%** | −16.70% |
| 0.95 | 0.79496 | 0.59655 | 0.74632 | **+6.52%** | −20.07% |

The a*=0.95 numbers reproduce #774's **+6.5% / −20.1%** `[branch @ 7aaec46c]`. Analytic a* → 1 limit
(r_ph⁺ → M): **v1 → 54/49 = 1.102 (+10.2% vs ZDM m/2 = 1)**; **v2 → 54/77 = 0.701 (−29.9% vs ZDM)**.
v1 **rises toward** the exact zero-damped-mode limit (overshoots by +10%), while v2 **floors at 0.70**
(qualitatively wrong — it cannot approach the ZDM limit because the rigid `ν_vac` skeleton fraction bounds
`x_sat` from below). So v1's near-extremal behavior is *qualitatively correct* and v2's is *qualitatively
wrong* — a second axis on which v1 is the surviving candidate.

> **Routed to Grant (organizer candidate; NOT banked).** v1 predicts `ω_R·M → 54/49 ≈ 1.102` as a* → 1,
> a clean rational overshooting the GR ZDM limit `m/2 = 1` by +10.2% — an AVE-distinct near-extremal
> forward prediction, testable once LIGO/LISA detects a near-extremal (a* > 0.9) ringdown. Route, don't
> bank (no near-extremal event is in the catalog).

---

## What this does to the reopened fork (evidence summary for Grant's ruling)

| axis | v1 (retired) | v2 (retained) | who wins |
|---|---|---|---|
| ω_R primary (a*=0.64–0.74) | **+2.63%** (MATCH band) | −9.53% (FAILS) | **v1** |
| ω_R secondary (a*=0.72–0.81) | +3.36% (marginal) | −11.70% (FAILS) | v1 (but drifting high) |
| ω_R spin-trend | overshoots, grows with spin | undershoots, grows with spin | v1 (smaller, right-side of 3% near catalog) |
| near-extremal (a*→1) | → 54/49 (+10%, qual. correct) | → 54/77 (−30%, qual. wrong) | **v1** |
| τ / Q (fully-specified model A) | FAILS (−38%) | FAILS (−38%, same) | tie (both fail) |
| τ / Q (v1's actual model B) | UNDETERMINED (Ω unpinned) | UNDETERMINED | — |
| provenance (register) | disclosed phenomenological, sol 0.55 | disclosed phenomenological, sol 0.55 | tie (both phenomenological) |

**Net:** v1 is the clearly-better ω_R mapping (matches the primary catalog + has the qualitatively-correct
extremal limit) — this is the reopened fork's real content and it favors v1. **But the whole ringdown
"both ω_R AND τ match" story does NOT return with v1:** the τ side either fails (fully-specified cold Q=ℓ)
or is undetermined (v1's spin-refined mΩ model has an Ω that was never derived). The honest forward state
is **"the spin-mapping fork favors v1 on ω_R (+2.6% primary) with a qualitatively-correct extremal limit,
while the τ side is a genuine open specification gap"** — *not* "v1 fully matches Kerr." The banked
sub-percent ω_R+τ FULL PASS is void under either mapping.

**No silent re-bank.** This research doc does not edit the KB leaf or the matrix (the re-bank awaits Grant's
fork ruling). The cold a*=0 eigenvalue (−1.69%) survives independently of everything here.

## Environment / reproduction

Deterministic, no network, no `qnm` import at run time (the corrected reference is hard-coded qnm-verified
`[branch @ 7aaec46c]`; the in-lane second method is the analytic BCW fit computed in the driver). Imports
only `math`/`sys`/`pathlib` + `ave.core.constants` (`C_0`, `G`, `M_SUN`, used for the frame-independence
sanity note only — the adjudication is dimensionless). Run:
`PYTHONPATH=src python3 research/2026-07-20_v1-spin-mapping-adjudication_rerun.py`.
