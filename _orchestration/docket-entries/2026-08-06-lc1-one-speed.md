# 2026-08-06 — LC-1 ONE-SPEED (multi-messenger) — the Lorentz-compliance arc's lead kill test

**Key:** `lc1-one-speed` · **Branch:** `research/lc1-one-speed` · **PR:** `[DO-NOT-MERGE]`
**Freeze (ALONE, pre-derivation, pre-code):** `992bb5a60230e66f8dd9181d9b3942cdc2b89593`
**Prereg:** `research/2026-08-06_lc1-one-speed_prereg-FROZEN.md` ·
**Result:** `research/2026-08-06_lc1-one-speed_result.md`
**Driver:** `research/drivers/lc1_one_speed_check.py` → `..._results.json`
(digest `590bc7e280d16fac99dd06f900c802137308afe001686f3ba7c6027f30c29405`, double-run)
**Gate:** `make verify-lc1-one-speed-number-check` — 25 numerals, mutation receipt, wired into `verify`.
**Base:** `origin/main` @ `d129e7ac` (PR #910). **SVA v0.2-pilot pass** (does not canonize the leaf).

## Outcome — two axes, both reported

- **PRIMARY (comparator-scoped): `A-COMPLIANT-AT-COMPARATOR`. Kill condition NOT-FIRED. The arc is
  NOT terminated by this lane.**
- **SECONDARY (inherited corpus state): `S2-KILL-INHERITED`, FIRED — and it was declared ENTAILED
  at freeze**, so it fires by demonstration, not adjudication. The framework's standing LIVE
  closed-negative on its gravitational-radiation sector (`q1-reading-A-radiative-bulk-port`,
  promoted LIVE 2026-07-20) is restated at full strength. **LC-1 does not clear it; LC-1 hardens
  it.**

## The three findings

1. **The detected messengers are at $c$, structurally.** $v_T^2 = G/\rho$ identically for all
   moduli, re-derived here from the micropolar energy functional with the gap modulus $G_c$
   cancelling exactly (residual symbolically `0`) — on a functional whose normalization is pinned
   by the canonical gap $4G_c/I_\omega$, so the check is not circular. Predicted difference against
   the retrieved interval $[-3\times10^{-15}, +7\times10^{-16}]$: exactly zero, zero free
   parameters. **Classified EXPECTED-CONSISTENCY (pure-AC), possibly an outright IDENTITY.**
2. **★The superluminal longitudinal channel is forced by the SAME modulus that sets $c$.**
   $v_L^2/v_T^2 = 4/3 + K/G \geq 4/3$ for every $K \geq 0$, so $v_L \geq 1.1547\,c$ **even at
   $K=0$**; $v_L = c$ requires $K = -G/3$ (an unstable medium). **The $K=2G$ GR-import is a
   magnitude knob, not an existence knob** — it moves $1.1547 \to 1.8257$. This closes the last
   modulus-level escape from the standing exclusion, **against the framework**, and is the lane's
   principal derived result. Stronger than what the prereg predicted.
3. **LC-1's own comparator has no power over that channel, for a derived kinematic reason.** A
   superluminal channel hands you the source's PAST, and a chirp's past is at lower frequency. For
   GW170817 the P-channel content arriving coincident with the merger was emitted `59.005` Myr
   earlier, at `2.54e-4` Hz — **`4.896` decades below the ground-based band**, robust across
   $f_{low}\in[10,30]$ Hz, the whole $40^{+8}_{-14}$ Mpc interval, and the whole component-mass
   range. **This is a COMPARATOR-POWER null, explicitly NOT a compliance mechanism** (it cannot
   affect a secular energy-budget readout — which is exactly what the pulsar comparator is).

## Channel enumeration (the deliverable of task b)

| # | channel | speed | sourced? | read by this network? | mechanism |
|---|---|---|---|---|---|
| 1 | EM-transverse photon | $c$ | YES (sGRB) | YES | **AT $c$** |
| 2 | mechanical shear / GW | $c$ (exact, all moduli) | YES | YES | **AT $c$** |
| 3a | A1 bulk PORT column | $\sqrt2 c$ | n/a | n/a | **`NOT-A-WAVE`** (not a Christoffel eigenvalue) |
| 3b | **A1 bulk RADIATIVE (P-wave)** | $\sqrt{10/3}\,c$ | **YES** (inherited, conditional) | **NO** | **`OUT-OF-BAND-AT-ARRIVAL`** ★crux |
| 4 | Cosserat micro-rotation | $\neq c$ (both branches) | NO | n/a | **`GAPPED`** + **`EVANESCENT`**, over-determined 18 + 36 decades |
| 5 | matter messengers ($\nu$) | — | YES | null searches | **`UNDERIVED`** — flagged, not folded in |

## Grant-gated items

1. **★ARC-SCOPE DECISION.** `S2` fired but was entailed; per the prereg's own §7.3 this lane does
   NOT terminate the arc on an inherited kill. Whether a standing *pulsar*-comparator exclusion
   should terminate a *multi-messenger* arc is framing-level and is Grant's. Decision package with
   both arguments at result §6.4.
2. **FLAG-LC1-DISPATCH — arc-brief currency.** The dispatch and the arc brief both describe
   port-register Q1 as *"explicitly-OPEN"* with three candidate answers (gapped/confined/
   sourceless). At HEAD, Q1 is a RULED row, REVERTED 2026-07-20 to Reading-A-live, and all three
   candidate answers were falsified by #761 **before the brief was written**. The 2026-08-06 dated
   currency update did not catch it. Consequence: **the dispatch's bin (i) was unreachable at
   freeze**, which is why the prereg added a comparator-scoped axis.
3. **FLAG-LC1-B — sector-ownership adjudication, live corpus contradiction.**
   `physics-lineage-map.md:63` (*"the A1 grade is non-radiative in free space"*) vs the standing Q1
   state (A1 rides the gapless P-branch, port OPEN). Likely reconciliation is an EM-A1 vs
   mechanical-A1 split that `def-9a4f07` currently forbids by identifying them. Both quoted; neither
   picked.
4. **Q1 NARROWINGS (auditor-lane, three).** (i) the Q1 radiative row has ONE available speed, not
   two — the FLAG-A fork does not reach it; (ii) Q1's exclusion cannot be escaped via the $K$
   import; (iii) the longitudinal branch is micropolar-UNPROTECTED, so a future Reading-B
   suppression must come from outside the micropolar sector. **No register row edited** — routed to
   the reconciliation the register itself already lists as owed.
5. **FLAG-LC1-C / FLAG-LC1-D / FLAG-LC1-E** — one-branch-or-two for register channels 1 vs 2; the
   UNDERIVED limiting speed of a bound matter excitation; and the arc's frozen four-item
   observability vocabulary being incomplete for this substrate (two mechanisms added at freeze).

## Discipline receipts

- Prereg frozen **ALONE** and pushed before any derivation text, driver, JSON or number existed
  (`ave-prereg` v1.8 Step 3.11).
- Comparator **re-retrieved from source** before freeze (Rule zero) and quoted verbatim: ApJL
  848:L13 / arXiv:1710.05834 (speed interval, 1.74 s delay); PRL 119 161101 / arXiv:1710.05832
  (total mass, luminosity distance). The LIGO $f_{low}$ is NOT verbatim-retrievable and was entered
  as a **bracketed engineering input**, flagged as the lane's weakest comparator input, with a
  gated robustness bracket.
- **Step 3.10 entailed-branch check run honestly at freeze** and its finding acted on structurally.
- **Step 3.9** analytic expectations frozen with numbers; prediction 3 (K-independence) came out
  **stronger** than pre-registered and is reported as such.
- 12 gates, all RUN and PASS; 3 fireability self-tests, all FIRE.
- Cross-grade combine member (#905/#907 fence) **declared, then measured**: $|\Delta| = $ `0.0` at
  $S=1$; the source-coupling leg declared NOT member-insensitive and inherited.
- **Mints no `clm-`/`def-`; edits no KB leaf, register, ledger, ruling or solidity.** Engine
  byte-untouched.
