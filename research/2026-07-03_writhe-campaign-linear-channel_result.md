# RESULT — Writhe arc STAGE (a): the linear-channel |F|-ratio campaign

**Status:** RUN-COMPLETE + ADJUDICATED. **FINAL VERDICT: COULOMB-RECOVERY (CONSISTENCY-class)** — the engine-derived interaction leg of Axiom 2 (like windings repel / unlike attract with Coulomb sign structure, mediated by the gapped ω sector). Minted `clm-wcoul2` (§9). The parity-odd |F|-ratio CHORD is **RESOLVED-TO-CONSISTENCY** (not falsified): the winding-force question produced the Ax2 interaction leg instead of an AVE-distinct chord. Magnitude-R = **BLOCKED** (Grant's C). Stage-(b) = **MOOT** (no classical degeneracy fired the successor; the sign resolved by mapping adjudication).
**Adjudication (Grant, 2026-07-03):** *"A full, and C"* → then, on the §4 tension, *"i agree with a"* = **(α) SNR-scoped gate + COULOMB-RECOVERY consistency-class bin**. See §4 (KEEP-BOTH: the mechanical ILL-DEFINED strict-letter reading is preserved alongside the α ruling).
**Prereg (FROZEN):** [`2026-07-03_writhe-campaign-linear-channel_prereg.md`](2026-07-03_writhe-campaign-linear-channel_prereg.md)
**Driver:** [`src/scripts/vol_4_engineering/writhe_campaign_linear_channel.py`](../src/scripts/vol_4_engineering/writhe_campaign_linear_channel.py)
**Results:** `src/scripts/vol_4_engineering/writhe_campaign_linear_channel_results.json`
**Minted claim:** `clm-wcoul2` — [`manuscript/ave-kb/vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md)
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

**Reading of the table (Grant-adjudicated, §4.2 — the Coulomb-recovery mechanism, NOT a chord):**
- vs **circulation** (current-loop knife): the quantized sign is the OPPOSITE of the classical current-loop rule (co-directed circulations attract; the quantized winding pair co-REPELS). **This inversion is the MECHANISM fact, not a chord:** it says the winding pair interacts as a *charge* pair, NOT a *current* pair — "winding-acts-as-charge-not-current." Under signed-Coulomb, like charges repel; the quantized co-REPEL / anti-ATTRACT is exactly the signed-Coulomb rule (§4.2).
- vs **charge-like** (Coulomb-recovery knife): the achiral scalar hedgehog has NO parity-odd distinction (co = anti exactly). This baseline **could not adjudicate the winding=charge mapping** — it correctly showed the quantized pattern is not reducible to an achiral *scalar* interaction, but a *signed* (achiral-magnitude-but-sign-carrying) charge is what Axiom 2 maps the winding onto, and the achiral hedgehog carries no sign to test that. Construction limitation, not a defect (§4.2b).

**The honest content (Grant-adjudicated):** the quantized sign structure (co-REPEL / anti-ATTRACT) **MATCHES signed-Coulomb under Axiom 2's winding=charge mapping** (anti-handed = opposite charge sign ⇒ attract). By the symmetric standard, an SM-shared sign structure cannot be booked as SM-divergent. So this is **Coulomb-recovery (CONSISTENCY-class)** — the engine-derived Axiom-2 interaction leg — **NOT** an AVE-distinct parity chord. See §4.2.

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

## 4. Adjudication (Grant, 2026-07-03) — α gate-scope + COULOMB-RECOVERY bin (KEEP-BOTH)

### 4.0 The tension (preserved — the strict-letter reading stays visible)

**The MECHANICAL bin is ILL-DEFINED** because the frozen §8 classifier applies G-plane across the entire §1 measurement domain {34, 38, 44}, and d=44 fails it. This strict-letter record is KEPT (KEEP-BOTH). The tension is between two clauses of the SAME frozen prereg:
- §1 froze the domain {34, 38, 44} (all Gate-0-stable), for separation-scaling.
- §3 froze that the signal is Yukawa-screened and NOISE-LIMITED at the far separation.
They collide at d=44: a valid STABILITY point but a noise-limited FORCE point. The §8 G-plane gate carried no SNR precondition, so it failed mechanically on the one separation §3 said would be noise-limited. This tension was **internal to the frozen document, not post-hoc** — both clauses were frozen before the run.

### 4.1 Gate-scope ruling: (α) — the G-plane gate carries the SNR precondition

**Grant ruled (verbatim "i agree with a"): option (α).** The G-plane sign-invariance gate is evaluated only where |F| is above the noise floor. Provenance argument (why this is not a post-hoc criterion drop): the d=44 anti noise-limit was frozen in **§3 of the same prereg** (the Yukawa magnitude-blocker) — a dead-instrument condition established before the run, not a result-driven exclusion. Therefore:
- **d=44 books OUT-OF-SCOPE** for the sign gate — a **dead-instrument cell, not a verdict cell** (the force is 5 OOM into the numerical floor; §3.1).
- **Verdict domain = d ∈ {34, 38}** (both pass every gate: plane-invariant, enantiomorph-consistent, window-invariant, α-invariant), with **d=44-co (the repulsive co-handed reading, +2.71e-8, still sign-consistent) as SUPPLEMENTARY** (it retains the co-REPEL sign even at the floor; only the anti reading is noise-jittered).

KEEP-BOTH: the §4.0 mechanical ILL-DEFINED record and this §4.1 α-scoped record both stand in the doc.

### 4.2 Bin adjudication: COULOMB-RECOVERY, CONSISTENCY-class (NOT the parity chord)

Under (α) the sign is well-defined on {34,38}. Grant ruled the bin is **COULOMB-RECOVERY (CONSISTENCY-class)**, NOT the AVE-distinct parity chord. Rationale (honest, symmetric-standard-applied):

- **(a) The quantized sign MATCHES signed-Coulomb under Axiom 2's own winding=charge mapping.** Axiom 2 maps the winding onto charge; anti-handed = opposite charge sign. Signed Coulomb then predicts exactly **like repels / unlike attracts** = **co-REPEL / anti-ATTRACT** — which is precisely the quantized pattern. The **symmetric standard** (do not book an SM-shared structure as SM-divergent) forbids calling this a parity divergence: a signed-charge Coulomb interaction is SM-shared. So the sign is a *consistency* result, not a chord.
- **(b) The achiral charge-like baseline could not adjudicate the winding=charge mapping — a construction LIMITATION, not a defect.** The hedgehog is achiral (no sign to carry), so co = anti (it correctly showed the pattern is not reducible to an achiral *scalar* interaction). But Axiom 2 maps the winding onto a *signed* charge, and an achiral scalar carries no sign to test the like/unlike distinction. So baseline (ii) rules out "achiral scalar" but cannot itself confirm-or-deny "signed Coulomb" — that adjudication is the Axiom-2 mapping (a), not the numerical hedgehog.
- **(c) Supporting mechanism prose.** A **massive-vector-like exchange through the gapped ω (rotation) sector** gives like-repel / unlike-attract; a scalar mediator would give *universal* attraction (like AND unlike attract). The observed like-repel/unlike-attract signs therefore indicate the **rotation sector mediates the winding interaction ELECTRICALLY** (vector-mediator sign structure), not gravitationally/scalar. The classical-circulation INVERSION (§2) is the concrete mechanism fact: the winding **acts as a charge, not a current** — a current pair would follow the current-loop rule (co-attract), and the winding does the opposite, i.e. it couples through the electric (charge) channel of the rotation sector, not the magnetic (current) channel.

**Verdict: COULOMB-RECOVERY (CONSISTENCY-class).** Minted as `clm-wcoul2` (§9): the engine-derived interaction leg of Axiom 2. The parity |F|-ratio CHORD is **RESOLVED-TO-CONSISTENCY** — not falsified; the winding-force question produced the Ax2 interaction leg instead of an AVE-distinct chord.

### 4.3 Stage-(b) = MOOT

The stage-(b) successor (the κ_chiral saturation channel, prereg §9) fires ONLY on classical DEGENERACY with no AVE-distinct residue. **It does NOT fire:** the sign is not degenerate-with-noise (it is a clean, Axiom-2-consistent Coulomb sign at d=34/38). The sign question was resolved by **mapping adjudication** (§4.2a), not by a classical-degeneracy finding. So **stage-(b) is MOOT** — the successor condition was never met. Recorded per prereg §9 (the successor is retired unfired, not pending).

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

The register §2.4 "dimensionless ratio" objective gets this honest status change (landed this branch): **magnitude-R = BLOCKED** (knot-overlap non-conservative integral + Yukawa screening); the **sign observable = RESOLVED-TO-CONSISTENCY** (Coulomb-recovery, the minted `clm-wcoul2`); the **"highest-value unbuilt FORM chord" designation = CLOSED** (resolved-to-consistency, not falsified). See §4.2 + the register §2.4 status-history block.

---

## 6. ω_gap provenance (G4 ledger — prereg §6)

**ω_gap = 1.0 is a HOST KNOB, not a substrate-derived constant.** It is a default parameter of the host (`crystal_graft_v2.py:65`), set as a literal in the S1 `_CFG` (`s1_winding_conservation_gate.py:55`). The canonical substrate mass-gap `OMEGA_C = C_0/L_NODE` (`constants.py:294`) exists but is NOT what the host uses. **Consequence:** the Yukawa range ξ = 0.548 cells is an ARTIFACT-SCALE (lattice units), not a physical prediction. The short-range/screened CHARACTER is qualitatively robust (a gapped field gives a Yukawa force); the range MAGNITUDE rides a host knob — so **no bench-scale range is predicted from the linear channel.**

---

## 7. Bench-reachability note (the chord did NOT land — Coulomb-recovery is consistency-class)

The bin is COULOMB-RECOVERY (§4.2), NOT the parity chord — so the prereg §8-bin-1 prior-art / bench-reachability mapping does **not** apply (there is no AVE-distinct force to map against torsion-balance / Eöt-Wash bounds). For completeness: even had the chord landed, the range is artifact-scale/short (§6, ω_gap is a host knob), so it would have been a FORM result, likely NOT bench-reachable. As a consistency result, the content is the SIGN STRUCTURE (like-repel/unlike-attract), whose robust part is the Axiom-2-consistent Coulomb sign, not a magnitude or a range.

---

## 8. What the campaign establishes / does NOT establish

**Establishes (CONSISTENCY-class, robust at d ∈ {34, 38}):**
- The quantized (2,3) winding pair interacts with a **Coulomb sign structure** — like windings REPEL, unlike windings ATTRACT — plane-invariant, enantiomorph-consistent, window- and α-invariant at the signal-bearing separations.
- This **matches signed-Coulomb under Axiom 2's winding=charge mapping** (§4.2a) — the **engine-derived interaction leg of Axiom 2**, the first engine-derived winding-pair interaction (minted `clm-wcoul2`, §9).
- **Mechanism (§4.2c):** the classical-circulation inversion shows the winding **acts as a charge, not a current** (co-REPEL, opposite to the current-loop rule); the like-repel/unlike-attract signs indicate a massive-vector-like (electric) exchange through the gapped ω rotation sector, not a scalar (universally-attractive) mediator.

**Does NOT establish:**
- **NO parity chord** — the sign is SM-shared (signed-Coulomb), so by the symmetric standard it is NOT AVE-distinct (§4.2). The parity |F|-ratio chord is RESOLVED-TO-CONSISTENCY, not confirmed.
- **NO magnitude-R** (§5 named blocker — ill-defined: knob-riding + noise-limited).
- **NO bench-reachable range** (§6 — ω_gap is a host knob; the range is artifact-scale; the mediator "mass"/screening scale is not a substrate prediction).
- All results are on the LINEAR buckle-OFF host; the κ_chiral saturation channel (stage-b) is **MOOT** (§4.3), not merely untested — its successor condition (classical degeneracy) was never met.

---

## 9. Minted claim (CONSISTENCY-class)

**`clm-wcoul2`** (landed this branch, `manuscript/ave-kb/vol4/claim-quality.md`): *"Engine-derived interaction leg of Axiom 2 — like windings repel / unlike attract with Coulomb sign structure, mediated by the gapped ω (rotation) sector; the first engine-derived winding-pair interaction."* Consistency-class. Caveats in the claim body: ω_gap = host knob (the screening scale / mediator "mass" is artifact-scale; the SIGN STRUCTURE is the robust content); linear/buckle-OFF host (κ_chiral / stage-b MOOT — the sign question was resolved by the Axiom-2 mapping, no classical degeneracy fired the successor). See `vol4/claim-quality.md` for the full quality block + scope history.
