# THE N–P MASS-SPLIT GATE — RESULT

**Date:** 2026-07-13 · **Branch:** `derivation/np-mass-split-gate` · **PR:** `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.
**Frozen prereg (gated on):** `research/2026-07-13_np-mass-split-gate_prereg.md` (freeze commit `b498d89a`, pushed `2026-07-14T01:43:22Z` BEFORE any code — git ordering = freeze proof).
**Driver:** `src/scripts/vol_2_subatomic/np_mass_split_gate.py` · **Tests:** `src/tests/test_np_mass_split_gate.py` (27 passed).

**One-line result:** **bin (iv) CHAIN-INSUFFICIENT** — the canonical neutron construction does not define a computable mass split without new assumptions — **with a genuine, δ_th-free structural sub-finding: the SIGN is forced POSITIVE (neutron heavier).**

---

## INTERPRETATION-DISCIPLINE (read BEFORE the verdict — Grant's care directive, verbatim: "be very very careful upon interpreting the results")

What this gate does and does **not** establish, frozen in the prereg before the run:

1. **A bin-(iv) does NOT falsify the +0.74% bare-topology emergence result.** That result — cold `κ_FS = 8π` → `1849.70 (+0.7377%)` from integers + imported α (`proton-identification.md:13`) — **stands entirely independent** of both δ_th and the neutron construction. This gate speaks only to the **ppm digits** that ride δ_th, and here it cannot even speak to those (see #3). Nothing about the +0.74% result is touched.

2. **A bin-(iv) does NOT confirm the proton-specific-coincidence hypothesis either.** "The corpus never built the neutron-mass instrument" is a statement about the corpus's *completeness*, not about whether δ_th is tuned. The wrong-sign consequence (bin ii) — which *would* have corroborated the coincidence reading — **did not fire**, because no computable split exists to have a sign in the eigenvalue-chain sense. The audit-card provenance findings (R3 pre-git mint, R7, R10 Δ-miss, R12 Lenz-6π⁵) are neither strengthened nor weakened by this gate; they stand exactly where the audit left them.

3. **★ The decisive interpretive fact (disclosed in the prereg, now confirmed by the run): the discriminator, as designed, does NOT actually load δ_th.** The audit card's "same δ_th, difference measurement, only chain structure remains" test presupposes the neutron is a **δ_th-modulated re-evaluation of the same eigenvalue chain** (a `(2,q)`-adjacent rung). **The corpus's canonical neutron is not that.** It is explicitly **NOT a `(2,q)` ladder entry** (`neutron-identification.md:23`) — it is a *composite additive threaded-electron mechanism*: bare proton **+** threaded `0₁` electron rest mass **+** Ax1-forced Borromean elastic-expansion strain. In the difference `m_n − m_p`, the bulk proton mass **and its δ_th correction cancel**, and what remains (the elastic-expansion tension) is **not a δ_th-governed quantity anywhere in the corpus**. So the "does the same δ_th survive a difference measurement?" second shot **cannot be fired against the canonical construction** — the canonical neutron never routes the split through δ_th at all. This is a finding about the *discriminator's design*, surfaced not silently resolved: the cheapest sharp discriminator the audit card named is **structurally mismatched** to the corpus's actual neutron ontology.

4. **The one thing the frozen chain DOES force — the SIGN — is δ_th-free and genuine.** It is reported separately (below) precisely so it is not confused with a δ_th survival claim. The sign result neither certifies nor impugns δ_th; it is a consequence of the composite topology + Axiom 1 alone.

---

## THE VERDICT

### Magnitude: **bin (iv) CHAIN-INSUFFICIENT**

The canonical neutron construction `n = 6₂³ ∪ 0₁` does **not** define a computable mass split from the frozen chain without new assumptions. The frozen chain fixes:

- `m_p` (the bulk proton mass, `1836.1170402290593 m_e`) — which **cancels** in the difference `m_n − m_p`;
- the threaded electron rest mass `= +1.000 m_e` (the `0₁` unknot, Reading X) — one of the two named split components.

The **dominant** component — the elastic-expansion tension (`+1.531 m_e = +0.782 MeV` under Reading X, or the *whole* `+2.531 m_e` under Reading Y) — has **no frozen-chain value**: no literal, no code path, no solver output anywhere in the corpus. The corpus itself says so, verbatim:

- `neutron-identification.md:36`: *"⚠️ MECHANISM derived, MAGNITUDE not — no FS calculation of threaded-knot energy producing 1.293 MeV; corpus uses empirical value as input downstream."*
- `neutron-identification.md:77`: *"the quantitative derivation via Faddeev-Skyrme solver applied to the `6₂³ ∪ 0₁` composite topology is NOT in the corpus."*
- `constants.py:1104`: *"no framework derivation has yet been adopted for the neutron mass."*
- clm-bh9p6s (`proton-neutron-mass-split.md`): computes He-4 binding, `T_nuc`, elastic displacement `Δx`, and the gravity-hierarchy factorisation — **never** the n–p split; the `1.293 MeV` appears only as an asserted attribution.

**Missing choices (verbatim — required to make the split computable; NOT made, per hard rail 3):**

- **C1** — FS field ansatz for the threaded `0₁` unknot inside the `6₂³` cage: no composite configuration exists (`neutron-identification.md:77`).
- **C2** — the threading-lock / boundary coupling energy term: no energy functional term in the corpus.
- **C3** — the Borromean cage elastic stiffness converting the forced radial expansion into strain energy: not derived; `neutron-identification.md:54` FLAGS even the `ℓ_node`-radial-expansion premise as *"not established."*
- **C4** — the mass-accounting convention: is the threaded electron's rest mass additively counted (Reading X) or absorbed into the surplus (Reading Y)? `proton-neutron-mass-split.md:10` leaves this open.
- **C5** — whether δ_th (or a threaded analog) softens the composite's coupling: the neutron construction never invokes a `κ_FS` softening for the split; adopting one would be a new assumption.

This is an **honest instrument gap, NOT a physics verdict**. The gate cannot be fired against the canonical construction because the corpus never built the instrument (the threaded-composite FS calculation).

### Sign: **FORCED POSITIVE (Δm > 0, neutron heavier) — δ_th-free, genuine**

Independent of the magnitude, the canonical construction makes a falsifiable structural claim about the sign, with **no new assumption**:

- neutron = bare proton **+** threaded `0₁` electron (rest mass `≥ 0`) **+** Ax1-forced Borromean expansion (elastic strain energy `≥ 0`: Ax1 forbids the flux tube shrinking below `ℓ_node`, so the ring is *stretched*, not relaxed);
- both named contributions are **positive-definite additions** to the bare-proton energy ⇒ **Δm > 0 (neutron heavier) is structurally forced**;
- this is **δ_th-free and α-free** (the sign comes from composite topology + Ax1, not from the tuned correction), and it is **robust to the mass-accounting ambiguity** (Reading X and Y both give all-non-negative contributions).

**This matches observation (the neutron IS heavier).** It is a real — if weak — structure signal: the corpus's neutron ontology gets the sign of the mass split right for a δ_th-independent mechanical reason. It does **not** certify δ_th (see interpretation-discipline #4).

---

## NO-REFIT / NO-MINT / NO-SEED AUDIT (self-review; the adversarial-review lens re-runs this)

| Rail | Check | Result |
|---|---|---|
| No refit (2) | live `ave.core.constants` consumed set == prereg-frozen HEAD literals (`test_live_constants_equal_frozen_head`, 6/6) | PASS |
| No refit (2) | `PROTON_ELECTRON_RATIO` reproduced live from `I_scalar/(1 − V·p_c) + 1` = `1836.1170402290593` | PASS (rtol 1e-12) |
| Refit plant | mutating any consumed constant by 1 ppm trips the abort (`test_refit_plant_trips_the_abort`, 4 constants) | FIRES |
| No mint (1,3) | fabricated `E_elastic` (provenance `invented`) rejected (`test_mint_plant_is_rejected`) | FIRES |
| No seed (4) | injecting an answer-derived seed (proton ratio / 1.293 / 2.531 / 939.565) rejected (`test_seed_plant_is_caught`) | FIRES |
| Bin fireable | forcing a computable finite split moves the bin off (iv) → (i)/(ii)/(iii) (`test_bin_flip_plant_moves_off_iv`) | FIRES |
| EFT hygiene | `make verify` (verify_universe magic-number gate): driver + test both PASS, "MATHEMATICALLY PURE" | PASS |

Zero hard-coded physics numbers in the driver; the forbidden-seed set is **derived** from the module CODATA anchors (auto-tracks). All 27 tests pass; `make verify` exit 0.

---

## FLAG-DON'T-FIX — canonical-chain ambiguities surfaced (NOT resolved here)

Per Grant's durable flag-don't-fix directive; both are surfaced for adjudication, not silently reframed:

1. **Mass-accounting ambiguity (Reading X vs Y).** `proton-neutron-mass-split.md:10` attributes the **whole** 1.293 MeV surplus to "elastic expansion tension," with **no separate accounting of the threaded electron's rest mass** (0.511 MeV). Reading X (`m_n = m_p + m_e + E_elastic`) leaves `E_elastic = +0.782 MeV` (= the β-decay Q-value) underived; Reading Y (whole surplus = tension) leaves the entire +2.531 m_e underived. The verdict (bin iv, sign +) is **robust to both**; the ambiguity is flagged for Grant, not decided.

2. **The discriminator-design mismatch** (interpretation-discipline #3): the audit card's "same δ_th, difference measurement" second shot presupposes a `(2,q)`-adjacent δ_th-modulated neutron; the corpus's canonical neutron is a composite additive mechanism that does not route the split through δ_th. Surfaced as a finding about the *discriminator*, not a defect in the corpus. **A genuine δ_th second-shot would need a different construction** (e.g. an even-`c` `(2,q)` sibling evaluated through the same eigenvalue chain) — which the corpus explicitly does NOT identify as the neutron. Whether such a construction should be built is a Grant/auditor framing decision, not an implementer choice.

---

## WHAT WOULD ACTUALLY FIRE THE SECOND SHOT (routed, not built)

The gate as designed is structurally unfireable against the canonical neutron. Two honest routes to a *real* second shot on δ_th (both require Grant/auditor adjudication before any build; neither is taken here):

- **Route A — build the threaded-composite FS instrument** (close C1–C5). This is the `neutron-identification.md:77` TBD-pin. It is a multi-session derivation with ≥5 new modelling choices; until those are made value-blind, any number it produces is a fit, not a second shot.
- **Route B — find a δ_th-loaded difference that IS in the corpus.** The Δ(1232) sibling rung (`c=7`) IS a δ_th-modulated eigenvalue and already on record: same δ_th → +2.35% miss (`epic-§40`, "proton-specific tightness = COINCIDENCE"). That is the second shot that already fired — and it points the way the coincidence reading predicts. The n–p split is cheaper only *if* the neutron were a δ_th-eigenvalue; it is not.

---

## BOTTOM LINE

The corpus's canonical neutron is a **composite additive structure**, not a δ_th-corrected eigenvalue-chain rung. The cheapest sharp discriminator the audit card named **cannot be fired against it**: the split's dominant term (elastic-expansion tension) is mechanism-named and magnitude-underived (bin iv), and δ_th does not enter the difference at all. The one thing the frozen chain *does* force — **the sign, Δm > 0, neutron heavier** — is δ_th-free, matches observation, and is a genuine (weak) structure signal that neither certifies nor impugns δ_th. The +0.74% bare-topology emergence result stands untouched. The already-fired δ_th second shot remains the Δ(1232) +2.35% miss.
