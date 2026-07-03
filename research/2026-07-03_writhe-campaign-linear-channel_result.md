# RESULT — Writhe arc STAGE (a): the linear-channel |F|-ratio campaign

**Status:** RUN-COMPLETE. **Mechanical bin: ILL-DEFINED** (the frozen G-plane gate fails — but ONLY at the noise-limited d=44 that the prereg's own §3 magnitude-blocker predicted). **The parity-odd SIGN chord-candidate is CLEAN and fully-armed at d=34 and d=38, noise-limited at d=44.** A prereg-internal tension is surfaced to Grant (§4) rather than resolved by dropping d=44 (Rule 7 — no post-hoc criterion drop).
**Prereg (FROZEN):** [`2026-07-03_writhe-campaign-linear-channel_prereg.md`](2026-07-03_writhe-campaign-linear-channel_prereg.md)
**Driver:** [`src/scripts/vol_4_engineering/writhe_campaign_linear_channel.py`](../src/scripts/vol_4_engineering/writhe_campaign_linear_channel.py)
**Results:** `src/scripts/vol_4_engineering/writhe_campaign_linear_channel_results.json`
**Grant ruling built on:** "A full, and C" (2026-07-03).
**Branch:** `analysis/writhe-campaign-linear-channel` (PR for audit + Grant merge; NO self-merge).

---

## 1. Validation gates (the honest floor — runs first)

| gate | requirement | measured | PASS? |
|---|---|---|---|
| S1 static planted floor | Q_link=3, w_tor=2, null=0 | Q_link=3, w_tor=2 | ✅ |
| live single knot N=96 | reads (2,3) | (2, 3) | ✅ |
| classical baseline (i) validate-on-known | current-loop: co-ATTRACT / anti-REPEL | co −9.77e-2 ATTRACT / anti +1.27e-1 REPEL | ✅ |

The classical circulation baseline reproducing the textbook current-loop rule (co-directed attract, counter repel) is the baseline's own validate-on-known — it passes, so the baseline is trustworthy as a discriminator.

---

## 2. The 2-baseline sign table (the discrimination result — d=34, plane XC0)

Self-subtracted interaction force F_int; sign convention F>0 REPULSIVE / F<0 ATTRACTIVE (frozen prereg §2.1).

| field class | co-handed | anti-handed | parity-odd? |
|---|---|---|---|
| **QUANTIZED (2,3)** | +7.07e-3 **REPULSIVE** | −2.02e-3 **ATTRACTIVE** | YES (sign flip) |
| **CLASSICAL circulation** | −9.77e-2 **ATTRACTIVE** | +1.27e-1 **REPULSIVE** | YES — but **OPPOSITE** to quantized |
| **CHARGE-like (achiral)** | +8.70e-5 REPULSIVE | +8.70e-5 REPULSIVE | **NO** (co = anti, `|co−anti|/max = 0.000`) |

**The quantized winding is DISCRIMINATED from both baselines:**
- vs **circulation** (current-loop knife): the quantized sign structure is the OPPOSITE of the classical current-loop rule — the quantized winding pair does co-REPEL / anti-ATTRACT, whereas classical co-directed circulations attract. **Not classically degenerate.**
- vs **charge-like** (Coulomb-recovery knife): the achiral charge pair has NO parity-odd distinction (co = anti exactly) — so the quantized sign's parity-oddness is genuinely sourced by the winding handedness, not by geometry/charge. **Coulomb recovery is what the achiral control does, and the quantized winding does NOT reduce to it.**

This is the strongest content of the campaign: **at the separations where signal exists (d=34, d=38), the parity-odd SIGN is a genuine discriminator** — distinct from the current-loop circulation (opposite sign) and from achiral charge (no distinction).

---

## 3. Per-separation, per-config force + invariance gates

Self-subtracted F_int(XC0) and the plane-sign-invariance gate (prereg §4):

| d | RR (co) | LL (co) | RL (anti) | LR (anti) | plane-inv (co/anti) | enantiomorph |
|---|---|---|---|---|---|---|
| 34 | +7.07e-3 REP | +7.07e-3 REP | −2.02e-3 ATT | −2.02e-3 ATT | ✅ / ✅ | ✅ (RR=LL, RL=LR) |
| 38 | +1.10e-4 REP | +1.10e-4 REP | −2.29e-5 ATT | −2.29e-5 ATT | ✅ / ✅ | ✅ |
| 44 | +2.71e-8 REP | +2.71e-8 REP | +3.95e-9 REP | +3.95e-9 REP | ✅ / ❌ | (co=anti, both +) |

Other gates (at d=34): window-invariance RR {150:+,250:+,350:+} ✅, RL {150:−,250:−,350:−} ✅; α-invariance ✅ (α absent from the force path, κ̃=6/5 literal, dF/F under α→2α = 0 exactly).

### 3.1 Why d=44 fails plane-invariance — it is NOISE-LIMITED (the §3 blocker's own prediction)

The G-plane gate fails ONLY at d=44, and ONLY for the anti (RL/LR) config. The per-plane RL forces at d=44 are `{−3: −7.6e-10, −1: +2.7e-9, 0: +3.95e-9, 1: +2.7e-9, 3: −7.6e-10}` — **all within ~4e-9 of zero**. This is not a physical sign flip; it is **sign jitter of an exponentially-screened signal sunk into the numerical floor.** The d=44 anti magnitude (3.95e-9) is **5 orders of magnitude below the d=34 anti magnitude** (2.02e-3). The falloff |F_co|(34)/|F_co|(44) = **2.6×10⁵** confirms Yukawa screening (prereg §3 reason 2, §6): the ω field is gapped, so the pair force is short-range and by d=44 the signal is at noise.

**This noise-limited d=44 was PREDICTED by the prereg's own §3 magnitude-blocker** (Yukawa screening ⇒ no signal at the far edge of the Gate-0 window). The G-plane gate, applied uniformly across all three separations including the noise-limited one, therefore fails on d=44 by construction — not because the SIGN is physically ill-defined (it is clean and plane-invariant at d=34 and d=38), but because d=44 carries no signal to define a sign.

By contrast the d=34 and d=38 anti signals (2.02e-3, 2.29e-5) are 5–6 OOM above the d=44 floor and clean-signed (all 5 planes negative) — plane-invariant, enantiomorph-consistent, window- and α-invariant.

---

## 4. The prereg-internal tension — SURFACED to Grant (NOT resolved here; Rule 7)

**The mechanical bin is ILL-DEFINED** because the frozen §8 classifier applies G-plane across the entire §1 measurement domain {34, 38, 44}, and d=44 fails it. But d=44 fails for a reason the prereg's OWN §3 blocker predicted (Yukawa noise), while the chord observable is clean at d=34/38.

**This is a genuine tension between two frozen prereg clauses:**
- §1 froze the measurement domain as {34, 38, 44} (all Gate-0-stable), for the separation-scaling check.
- §3 froze that the signal is Yukawa-screened and NOISE-LIMITED at the far separation (the magnitude blocker's second derived reason).

These two clauses collide at d=44: it is a valid STABILITY point but a noise-limited FORCE point. The §8 G-plane gate does not carry a signal-to-noise precondition, so it fails mechanically on the one separation §3 said would be noise-limited.

**I am NOT resolving this by dropping d=44** (Rule 7 forbids dropping an adjudication criterion post-hoc to convert ❌→chord; and Rule 11 forbids debugging toward a rescue). The honest options are Grant's to rule:

- **(Ruling option α) The G-plane gate carries an implicit SNR precondition** (evaluate sign-invariance only where |F| is above the noise floor). Then d=44 is out-of-scope for the sign gate (noise-limited, as §3 booked), d=34/38 pass all gates, and the bin becomes **PARITY-ODD-SIGN-CHORD-CANDIDATE**. This is a plausible reading — §3 already established d=44 as noise — but it is a criterion REFINEMENT, so it needs Grant's explicit ruling, not my unilateral call.
- **(Ruling option β) The frozen gate stands as literally written** ⇒ **ILL-DEFINED** is the verdict, recorded as-is: the sign is not uniformly plane-invariant across the frozen domain. Clean, honest, closes the linear channel's magnitude AND leaves the sign as "clean-at-close-range, noise-limited-at-range, not uniformly gated." Under this reading the stage-(b) successor question is whether the noise-limited far field disqualifies the chord.

**My lean (stated as a lean):** option α is the physically honest reading — the sign chord IS armed where signal exists, and d=44's failure is the already-booked Yukawa noise, not a physics sign-flip. But because collapsing {34,38,44}→{34,38} for the sign gate is exactly the kind of domain-narrowing Rule 7 warns against, I will not make that call. **Surfaced for Grant's adjudication.**

---

## 5. The magnitude-R named blocker (Grant's C — reported, tagged BLOCKED)

Per prereg §3, R = |F|_co/|F|_anti is formally BLOCKED (ill-defined at current engine capability). Reported for transparency:

| d | \|F_co\| | \|F_anti\| | R | status |
|---|---|---|---|---|
| 34 | 7.07e-3 | 2.02e-3 | 3.510 | BLOCKED (knob-riding) |
| 38 | 1.10e-4 | 2.29e-5 | 4.817 | BLOCKED (knob-riding) |
| 44 | 2.71e-8 | 3.95e-9 | 6.863 | BLOCKED (noise-limited) |

**Two derived reasons (confirmed by the run):**
1. **Knot overlap ⇒ no plane-conservative integral.** The magnitude spread across integration planes is 4.7–9.5× (result table §3, "mag spread") — R read at any single plane is knob-riding. R also drifts with d (3.51 → 4.82 → 6.86) as the signal sinks toward noise.
2. **Yukawa screening ⇒ no source-free far-field.** |F_co| falls 2.6×10⁵ over d=34→44; ξ = c_ω/ω_gap ≈ 0.548 cells. There is no far-field surface with nonzero signal.

The register §2.4 "dimensionless ratio" objective gets this honest status change: **the magnitude-ratio target is ill-defined in the linear channel at current engine capability** (auditor lands the register edit).

---

## 6. ω_gap provenance (G4 ledger — prereg §6)

**ω_gap = 1.0 is a HOST KNOB, not a substrate-derived constant.** It is a default parameter of the host (`crystal_graft_v2.py:65`), set as a literal in the S1 `_CFG` (`s1_winding_conservation_gate.py:55`). The canonical substrate mass-gap `OMEGA_C = C_0/L_NODE` (`constants.py:294`) exists but is NOT what the host uses. **Consequence:** the Yukawa range ξ = 0.548 cells is an ARTIFACT-SCALE (lattice units), not a physical prediction. The short-range/screened CHARACTER is qualitatively robust (a gapped field gives a Yukawa force); the range MAGNITUDE rides a host knob — so **no bench-scale range is predicted from the linear channel.**

---

## 7. Bench-reachability + prior-art note (auditor-marked, per prereg §8 bin 1)

*IF Grant rules option α (§4) and the chord-candidate lands:* the prior-art mapping goes here, auditor-marked. Even under the chord reading, the range is artifact-scale/short (§6), so the expected classification is a **FORM result (a parity-odd interaction sign/direction), likely NOT bench-reachable** — the torsion-balance / Eöt-Wash spin-dependent-force bound classes apply only after a physical range is established, which the linear channel does not provide (ω_gap is a host knob). **[AUDITOR: land the register §2.4 status + the prior-art bound-class mapping only after Grant's §4 ruling.]**

---

## 8. What the campaign establishes / does NOT establish

**Establishes (robust, at d=34/38 where signal exists):**
- The quantized (2,3) winding pair has a **parity-odd interaction sign** (co-REPEL / anti-ATTRACT), plane-invariant, enantiomorph-consistent, window- and α-invariant at the signal-bearing separations.
- This sign is **DISCRIMINATED from both classical baselines**: opposite to the current-loop circulation rule, and absent-of-distinction in the achiral charge control. The classical circulation baseline passes its own current-loop validate-on-known.

**Does NOT establish:**
- **NO magnitude-R** (§5 named blocker — ill-defined, knob-riding + noise-limited).
- **NO bench-reachable range** (§6 — ω_gap is a host knob; the range is artifact-scale).
- **NO uniform-domain sign verdict** — the sign fails plane-invariance at the noise-limited d=44 (§3.1); whether this disqualifies the chord or is out-of-scope-by-SNR is the §4 tension surfaced to Grant.
- All results are on the LINEAR buckle-OFF host; the κ_chiral saturation channel (stage-b) says nothing until fired.

**Stage-(b) trigger (prereg §9):** fires only if the sign books classically-degenerate. It does NOT — the sign discriminates from both baselines at d=34/38. So the stage-(b) successor is NOT triggered by the physics; the open question is purely the §4 gate-scope ruling, which is a domain/SNR adjudication, not a classical-degeneracy finding.
