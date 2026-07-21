# RESULT — v1 spin-mapping frozen adjudication: **MIXED (ω_R matches primary; τ fails at ~−5%)**

**Lane:** v1-spin-mapping-adjudication (routed follow-on of PR #774's § FORK-REOPEN)
**Date:** 2026-07-20 (τ verdict corrected 2026-07-20 per PR #776 review — see "Frozen-plan deviations disclosed")
**Prereg (frozen, criteria set before run):** [`2026-07-20_v1-spin-mapping-adjudication_prereg-FROZEN.md`](2026-07-20_v1-spin-mapping-adjudication_prereg-FROZEN.md)
**Driver (deterministic):** [`2026-07-20_v1-spin-mapping-adjudication_rerun.py`](2026-07-20_v1-spin-mapping-adjudication_rerun.py)
**Upstream:** PR #774 (`fix/kerr-qnm-table-correction`) — **MERGED** into main as `01924a96` (2026-07-21); every #774 cite below is tagged `[canon #774]` and resolves to bit-identical canon (commit `7aaec46c` landed unchanged). (PR #772 ringdown-systematics also MERGED, `eb9e33bc`.) *Currency-refresh 2026-07-20 per PR #776 review findings 2/7: the prereg-FROZEN's original `[canon #774]`/"UNMERGED — do not assume merged" tags are byte-frozen and now stale; this result carries the merged-canon resolution.*

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
> - **τ — V1 FAILS on damping; the ω_R and τ verdicts split.** Two AVE damping models, both **computed
>   in the driver** (not narrated):
>   - **Model A — cold topological `Q = ℓ = 2`** (`qnm-quality-factor.md`, clm-395gps; fully specified,
>     spin- & v1/v2-independent): v1 (and v2) **FAIL decisively** at catalog spins, `D̄_Q = −38.18%`
>     (AVE Q = 2 vs corrected-Kerr Q rising 3.07→3.49).
>   - **Model B — spin-refined `ω_I = (ω_R − mΩ)/2ℓ` at `r_Ω = r_ph·√(1+ν_vac)`** (v1's *actual* corpus
>     τ prediction, the KB τ = 3.5/2.7/1.2 ms): **τ-FAILS at `D̄_Q = −5.44%`** (Resultbox form; **−4.57%
>     marginal** under the exact-equatorial-ZAMO variant — sensitivity flagged). Ω is **corpus-derived,
>     not fabricated**: the Ch.2 frame-dragging Resultbox `ω(r) = 2Mar/(r²+a²)²` (clm-rd9cjm,
>     `frame-dragging-impedance-convolution.md:15`; equated to Ω_LT in `gravitomagnetism-frame-dragging.md:15`)
>     evaluated at the pinned `r_Ω` (`ave-merger-ringdown-eigenvalue.md:85`). The forward chain
>     **regenerates the asserted KB τ table to rounding** (3.44/2.67/1.19 ms Resultbox, 3.47/2.69/1.21 ms
>     ZAMO vs asserted 3.5/2.7/1.2) — empirical proof this chain is what generated the originals.
>
>   🔴 **CORRECTION (PR #776 review, finding 0 — DOWNGRADED-MAJOR).** The pre-correction verdict said
>   Model B "is ~~**UNDETERMINED** — its frame-dragging rate Ω is **not numerically pinned anywhere in the
>   corpus**~~ (the τ values were asserted at initial release, not coded)." That was a **grep-completeness
>   false-negative** — a numeric-literal grep (driver: "grep: no numeric Ω / r_Ω") cannot see a *formula*
>   pin (Grant's explicitly-banked failure mode); the branch's own prereg §3 already quotes the `r_Ω`
>   formula. The corpus **does** determine Ω (chain above; register clm-395gps `depends-on` lists
>   clm-rd9cjm, the Ch.2 Resultbox claim). Declining to **fabricate** Ω was correct (anti-seduction);
>   declining to **derive** what the banked resultboxes determine was the evidence gap. Corrected:
>   **Model B τ-FAILS at ~−5% (variant-sensitive), not undetermined.** The overall MIXED bin is unchanged.

So the ω_R rescue of the reopened fork is **real** (primary MATCH, secondary marginal); the τ side is
**where the rescue does not carry** — it fails under **both** damping models (decisively cold, `−38%`;
near-miss spin-refined, `~−5%`, variant-sensitive). v1's full picture is a **coherent near-match**
(ω_R +2.63% / τ ≈ −5%) — far from the cold-model `−38%`, but still outside the frozen bands on τ. The
ω_R and τ verdicts split, which is the frozen **MIXED** bin.

---

## Leg 1 — corrected Kerr re-verified in-lane (second method: BCW-2006)

The corrected Kerr (2,2,0) reference `[canon #774]` (qnm/Stein-2019 high-precision Leaver) is
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
| GW170104 | 0.64 | 0.51955 | 0.46456 | 0.50819 | **+2.24%** | −8.59% | qnm `[canon #774]` |
| GW150914 | 0.67 | 0.53284 | 0.47208 | 0.51986 | **+2.50%** | −9.19% | qnm `[canon #774]` |
| GW151226 | 0.74 | 0.56910 | 0.49191 | 0.55163 | **+3.17%** | −10.83% | qnm `[canon #774]` |
| **PRIMARY mean** | | | | | **+2.63%** | **−9.53%** | |
| GW190521 (2nd) | 0.72 | 0.55786 | 0.48587 | 0.54373 | **+2.60%** | −10.64% | BCW-fit `[in-lane]` `[IMPORT: GWTC-2 a*]` |
| GW170729 (2nd) | 0.81 | 0.61610 | 0.51623 | 0.59169 | **+4.13%** | −12.75% | BCW-fit `[in-lane]` `[IMPORT: GWTC-1 a*]` |
| **SECONDARY mean** | | | | | **+3.36%** | **−11.70%** | |

The **+2.63% primary mean reproduces #774's § FORK-REOPEN table exactly** (per-event +2.24 / +2.50 / +3.17)
`[canon #774]` — two-method agreement (this lane's independent driver + #774's review computation).
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
flagged the *overtone* disagreement — *"Q = ℓ disagrees with GR overtone structure **for ℓ > 2**"*
(claim-quality.md:217) — and **separately** recorded a *claimed* refined-fit "sub-2%" **fundamental**
Kerr-Q match for `a* = 0.3–0.8` (claim-quality.md:204). Leg 3's `−38%` is the **cold fundamental
(2,2,0)** mode at exactly those spins, so it is **genuinely new adverse content** — *not* the pre-priced
ℓ>2 overtone caveat, consistent with the "THE NEW CONTENT" header. Corrected 2026-07-20 per PR #776
review finding 3: the earlier "already flagged this" mis-scoped the register.)

**Model B — spin-refined `ω_I = (ω_R − mΩ)/(2ℓ)` at `r_Ω = r_ph·√(1+ν_vac)`** (this is v1's *actual*
corpus τ prediction, the KB τ = 3.5/2.7/1.2 ms): **τ-FAILS at `D̄_Q = −5.44%`** (Resultbox form; **−4.57%
marginal** under the exact-equatorial-ZAMO variant — sensitivity flagged). Ω is **corpus-derived, not
fabricated** — the driver now computes the forward chain:

| event | a* | r_Ω | Ω·M | Q_v1 (B) | Q_v2 (B) | Q_Kerr | **v1 Q dev** | v2 Q dev |
|---|---|---|---|---|---|---|---|---|
| GW170104 | 0.64 | 2.4051 | 0.08024 | 2.894 | 3.055 | 3.071 | **−5.76%** | −0.49% |
| GW150914 | 0.67 | 2.3452 | 0.08880 | 3.000 | 3.206 | 3.176 | **−5.53%** | +0.96% |
| GW151226 | 0.74 | 2.1957 | 0.11274 | 3.312 | 3.693 | 3.487 | **−5.02%** | +5.89% |
| **mean** | | | | | | | **−5.44% → τ-FAILS** | +2.12% (τ-matches) |

`Ω(a*)` is pinned by the corpus: `Ω = ω(r_Ω)` with the **Ch.2 frame-dragging Resultbox**
`ω(r) = 2Mar/(r²+a²)²` (clm-rd9cjm, `frame-dragging-impedance-convolution.md:15`; the register entry for
clm-395gps lists clm-rd9cjm in its own `depends-on`), evaluated at the Poisson-augmented photon sphere
`r_Ω = r_ph⁺(a*)·√(1+ν_vac)` (`ave-merger-ringdown-eigenvalue.md:85`), and Ch.3
(`gravitomagnetism-frame-dragging.md:15`) explicitly equates that Resultbox to the observed Ω_LT. **Proof
this chain generated the asserted KB τ table:** the same forward chain at source-frame masses regenerates
`τ = 3.44/2.67/1.19 ms` (Resultbox) / `3.47/2.69/1.21 ms` (exact-ZAMO) vs the asserted 3.5/2.7/1.2 ms — to
2-sig-fig rounding. So v1's actual spin-refined τ model is a **coherent near-miss that FAILS the frozen
band** at ~−5%, *not* an open specification gap.

Note the **mirror-image split** in the table: applying the same Model-B chain to **v2**'s ω_R gives
`D̄_Q = +2.12%` (τ-matches) — but v2's ω_R *fails* at −9.53%. So **neither mapping matches on both axes**:
v1 wins ω_R and near-misses τ; v2 near-matches τ (partly by compensating errors — low ω_R and low ω_I) and
fails ω_R. The banked sub-percent τ_v2 = −0.47% "match" remains void (it rode frame- + ω_I-table
contamination); it is *not* the same object as this dimensionless Model-B +2.12%.

🔴 **CORRECTION (PR #776 review, finding 0).** The pre-correction text said Model B was
"~~**UNDETERMINED** — the frame-dragging rate Ω is **not numerically pinned anywhere in the corpus** — grep
returns no numeric Ω / r_Ω~~." That corpus-completeness claim was **false**: a numeric-literal grep cannot
see a *formula* pin (a banked failure mode), and the branch's own prereg §3 already quotes the `r_Ω`
formula. Declining to **fabricate** Ω was correct; declining to **derive** the corpus-pinned Ω was the
evidence gap this repair closes.

> **Flag (don't fix) — the Q three-way tension, still open for Grant/auditor.** (1) ~~v1's τ prediction
> cannot be frozen-adjudicated until Ω is derived — the corpus under-specifies the spinning damping.~~
> **Superseded (PR #776 finding 0):** Ω *is* corpus-pinned and Model B is now frozen-adjudicated (τ-FAILS
> at −5.44%, marginal −4.57% ZAMO). The residual open work is not an Ω gap but a **Q self-consistency**
> question. (2) Three corpus statements about Q still need reconciling: `qnm-quality-factor.md` says
> `Q = ℓ` (spin-independent); `ave-merger-ringdown-eigenvalue.md` says Q *"increases with spin"*; Phase-5
> (`ligo-ringdown-driver-design.md` §10) says Q is *v1/v2-invariant*. Model A instantiates the first,
> Model B the second; they give −38% and −5% respectively, so the two are **not the same physics** and the
> three-way tension is real. A single pinned τ story needs these reconciled first. Surfaced, not resolved.

## Leg 4 — v1-provenance grade

The v1 spin mapping `x_sat,v1 = 7·r_ph⁺/3M` is the **Kerr extension of claim clm-395gps** (canonical
`vol3/claim-quality.md`; hosted `ave-merger-ringdown-eigenvalue.md` + `qnm-quality-factor.md`).
Register grade (queried via `kb_cmd show clm-395gps`):

- **solidity 0.55** (confidence 0.80), **build_status: "use as input only, don't build deeper"** (band `input-only`).
- Rationale (verbatim key phrase): the cold Schwarzschild eigenvalue `18/49` is a *"genuine 1.7%-error
  category-(iv) derived prediction"* (clean, zero-free-parameter: `r_sat = 7M` from Ax 4, `r_eff = 49M/9`
  via Poisson ν_vac, `ω_R = ℓc/r_eff`); the band is *"held below 0.9 because the Kerr extension rests on a
  **disclosed phenomenological** photon-sphere shift + Cosserat back-reaction fit **(v2, refined post-hoc
  against LIGO)**, and Q = ℓ disagrees with GR overtone structure **for ℓ > 2**"*.

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

The a*=0.95 numbers reproduce #774's **+6.5% / −20.1%** `[canon #774]`. Analytic a* → 1 limit
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
| ω_R secondary (a*=0.72–0.81) | **+3.36%** (marginal, 3–5%) | −11.70% (FAILS) | v1 (but drifting high) |
| ω_R spin-trend | overshoots, grows with spin | undershoots, grows with spin | v1 (smaller, right-side of 3% near catalog) |
| near-extremal (a*→1) | → 54/49 (+10%, qual. correct) | → 54/77 (−30%, qual. wrong) | **v1** |
| τ / Q (fully-specified model A, cold Q=ℓ) | FAILS (−38%) | FAILS (−38%, same) | tie (both fail) |
| τ / Q (v1's actual model B, Ω corpus-pinned) | **FAILS at −5.44%** (Resultbox; −4.57% marginal ZAMO) | +2.12% (τ-matches, but ω_R fails) | split — neither passes both axes |
| provenance (register) | disclosed phenomenological, sol 0.55 | disclosed phenomenological, sol 0.55 | tie (both phenomenological) |

**Net:** v1 is the clearly-better ω_R mapping (MATCH band on the primary catalog, marginal on the secondary
higher-spin set, and the qualitatively-correct extremal limit) — this is the reopened fork's real content
and it favors v1 on ω_R. **But the whole ringdown "both ω_R AND τ match" story does NOT return with v1:**
the τ side fails under **both** damping models — decisively for the cold Q=ℓ model (−38%) and as a
**coherent near-miss** for v1's actual spin-refined mΩ model (−5.44% Resultbox / −4.57% marginal ZAMO,
Ω now corpus-derived, *not* undetermined). The honest forward state is **"the spin-mapping fork favors v1
on ω_R (+2.6% primary / +3.4% secondary-marginal) with a qualitatively-correct extremal limit, while v1's
τ model is a ~−5% near-miss that FAILS the frozen band"** — *not* "v1 fully matches Kerr," and *not* "τ is
an open specification gap." Note the mirror image: v2 near-matches τ (+2.12%) only by compensating ω_R/ω_I
errors while its ω_R fails, so **no mapping matches on both axes**. The banked sub-percent ω_R+τ FULL PASS
is void under either mapping.

**No silent re-bank.** This research doc does not edit the KB leaf or the matrix (the re-bank awaits Grant's
fork ruling). The cold a*=0 eigenvalue (−1.69%) survives independently of everything here.

## Frozen-plan deviations disclosed (PR #776 review)

The prereg is **byte-frozen**; the deviations from the frozen plan are recorded here (not in the prereg),
per the review. None flips the overall MIXED bin.

1. **Model B computed, not declared UNDETERMINED (findings 0/9).** The prereg froze Model B's τ as
   UNDETERMINED on the (mistaken) basis that Ω is "not numerically pinned anywhere in the corpus." The
   review established that the corpus **does** pin Ω — the Ch.2 frame-dragging Resultbox
   `ω(r) = 2Mar/(r²+a²)²` (clm-rd9cjm) at `r_Ω = r_ph·√(1+ν_vac)` (merger leaf:85), with clm-395gps's
   register `depends-on` listing clm-rd9cjm. The driver now computes Model B under the same frozen C-τ
   comparator: **τ-FAILS at −5.44% (Resultbox) / −4.57% (exact-ZAMO, marginal)**. Disclosed deviation in
   the *adverse* direction (v1 looks worse on τ — no resurrection-seduction harm); the false
   corpus-completeness claim is struck (Rule-12 correction in Leg 3 + the ★ block).

2. **Primary a\* provenance relabel (finding 1).** The prereg §4 labels the primary imports "a\* imports
   per GWTC-1," but the shipped values **0.67 (GW150914) / 0.64 (GW170104) / 0.74 (GW151226) are the
   discovery-paper / KB-legacy remnant spins** (verbatim at initial-release `de9d2293`), *not* GWTC-1's
   updated finals (GW150914 ≈ 0.69, GW170104 ≈ 0.66; GW151226 = 0.74 matches both, non-discriminating).
   Using the banked-catalog spins is *required* to reproduce #774's two-method comparator apples-to-apples.
   **Sensitivity:** recomputing the primary mean at GWTC-1-consistent {0.66, 0.69, 0.74} moves D̄_ωR from
   +2.63% to ≈ +2.4–2.8% — still inside `|D̄| < 3%`, no bin change (0.67/0.64 sit within GWTC-1's own
   ±0.05 posterior widths). Correct label: *banked-catalog legacy (= discovery-paper) spins*, not "per
   GWTC-1." (The secondary imports — GW170729 a\*=0.81 per GWTC-1, GW190521 a\*=0.72 per GWTC-2 — check out.)

3. **Secondary Kerr source: BCW-fit, not "(interp)" (finding 8).** The prereg's frozen reference table
   marks the secondary Kerr rows (a\*=0.72/0.81) "(interp)"; the driver uses the in-lane BCW-2006 fit
   (`kerr_ref` falls through to `BCW-fit[in-lane]` for non-tabulated spins). **Bin-invariant:** grid-interp
   of the shipped qnm grid gives +2.90% / +3.62% (mean +3.26%) vs the shipped BCW +2.60% / +4.13% (mean
   +3.36%) — both land in the frozen 3–5% marginal band, MIXED verdict unchanged. (The BCW-2006 fit is
   itself an interpolating fit to the Kerr QNM spectrum, so "(interp)" was a defensible-but-ambiguous
   placeholder; reconciled here.)

4. **Currency (findings 2/7).** #772 and #774 are **MERGED** (into main as `eb9e33bc` / `01924a96`,
   2026-07-21); the prereg's "UNMERGED — do not assume merged" riders are byte-frozen and now stale
   (conservative direction — `7aaec46c` landed unchanged, so every cite resolves to bit-identical canon).
   This branch merges origin/main; body tags flipped `[branch @ 7aaec46c]` → `[canon #774]`.

## Environment / reproduction

Deterministic, no network, no `qnm` import at run time (the corrected reference is hard-coded qnm-verified
`[canon #774]`; the in-lane second method is the analytic BCW fit computed in the driver). Imports
only `math`/`sys`/`pathlib` + `ave.core.constants` (`C_0`, `G`, `M_SUN`, used for the frame-independence
sanity note only — the adjudication is dimensionless). Run:
`PYTHONPATH=src python3 research/2026-07-20_v1-spin-mapping-adjudication_rerun.py`.
