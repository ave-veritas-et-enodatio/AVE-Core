# THE N–P MASS-SPLIT GATE — RESULT

**Date:** 2026-07-13 · **Branch:** `derivation/np-mass-split-gate` · **PR:** `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.
**Frozen prereg (gated on):** `research/2026-07-13_np-mass-split-gate_prereg.md` (freeze commit `b498d89a`, pushed `2026-07-14T01:43:22Z` BEFORE any code — git ordering = freeze proof).
**Driver:** `src/scripts/vol_2_subatomic/np_mass_split_gate.py` · **Tests:** `src/tests/test_np_mass_split_gate.py` (41 passed). · **Adversarial review:** 11 findings confirmed (1 MAJOR→narrowed, 0 refuted, freeze verified clean); repairs banked 2026-07-14.

**One-line result:** **bin (iv) CHAIN-INSUFFICIENT** — the canonical neutron construction does not define a computable mass split without new assumptions **TODAY** (the composite FS instrument does not exist) — **with a genuine, δ_th-free structural sub-finding: the SIGN is forced POSITIVE (neutron heavier), and the stronger β-decay-downhill floor Δm > 1.000 m_e.** Post-review narrowing (R1): δ_th-loading of the split is **FORK-OPEN (C5-undetermined), not "never"** — the corpus's own TBD-pin route (Route A) resurrects the audit-card second shot once built value-blind.

---

## INTERPRETATION-DISCIPLINE (read BEFORE the verdict — Grant's care directive, verbatim: "be very very careful upon interpreting the results")

What this gate does and does **not** establish, frozen in the prereg before the run:

1. **A bin-(iv) does NOT falsify the +0.74% bare-topology emergence result.** That result — cold `κ_FS = 8π` → `1849.70 (+0.7377%)` from integers + imported α (`proton-identification.md:13`) — **stands entirely independent** of both δ_th and the neutron construction. This gate speaks only to the **ppm digits** that ride δ_th, and here it cannot fire that discriminator **today** (bin iv — the instrument is unbuilt); Route A could, once built (see #3). Nothing about the +0.74% result is touched.

2. **A bin-(iv) does NOT confirm the proton-specific-coincidence hypothesis either.** "The corpus never built the neutron-mass instrument" is a statement about the corpus's *completeness*, not about whether δ_th is tuned. The wrong-sign consequence (bin ii) — which *would* have corroborated the coincidence reading — **did not fire**, because no computable split exists to have a sign in the eigenvalue-chain sense. The audit-card provenance findings (R3 pre-git mint, R7, R10 Δ-miss, R12 Lenz-6π⁵) are neither strengthened nor weakened by this gate; they stand exactly where the audit left them.

3. **★ The decisive interpretive fact — NARROWED post-review (2026-07-14, findings R1; the pre-review over-reach is preserved KEEP-BOTH below).** Two things are separable here, and only the first is corpus-forced:
   - **Ontology (corpus-correct, stands):** the audit card's "same δ_th, difference measurement" test presupposes the neutron is a **δ_th-modulated re-evaluation of the same eigenvalue chain** (a `(2,q)`-adjacent rung). **The corpus's canonical neutron is not that** — it is explicitly **NOT a `(2,q)` ladder entry** (`neutron-identification.md:23`); it is a *composite additive threaded-electron mechanism* (bare proton **+** threaded `0₁` rest mass **+** Ax1-forced Borromean strain). In the difference `m_n − m_p` the **bulk proton mass and its δ_th correction cancel exactly.** No eigenvalue-chain neutron reading exists in the corpus.
   - **δ_th-transparency of the *residual* (NARROWED — this is where the pre-review claim over-reached):** whether the *strain term* that survives the cancellation carries δ_th is **C5-UNDETERMINED, not "never."** The corpus's OWN named completion route — `neutron-identification.md:36`/`:77` TBD-pin, *"derive 1.293 MeV from FS solver applied to threaded 0₁-in-6₂³ topology. Same shape as proton mass eigenvalue derivation … adding to the FS energy integral"* — instructs a **proton-shaped FS derivation, and that solver consumes the δ_th-softened `κ_FS = 8π(1−δ_th)` (`constants.py:896`).** A live-fire check confirms the instrument is δ_th-sensitive: `i_scalar(c=5) = 1161.987` (warm) vs `1170.586` (cold 8π), the 0.74% shift. `E_FS(composite;κ_FS) − E_FS(bare;κ_FS)` cancels only the proton's own FS energy; the residual strain term is generically `κ_FS`-dependent, hence **δ_th-carrying under this pinned route** — so `κ_FS` carry-over is arguably the **canonical default**, not a new assumption. **FORK (open):** a competing linear-elastic-stiffness bound route (`neutron-identification.md:54`) may instead be δ_th-free. Unresolved until C1–C3 are built. **Net:** the discriminator is **unfireable TODAY (bin iv stands — the composite FS does not exist, C1), and δ_th-loading is FORK-OPEN**, NOT "structurally cannot load δ_th."
   - 🔴 **KEEP-BOTH — superseded pre-review framing (2026-07-13):** *"what remains (the elastic-expansion tension) is not a δ_th-governed quantity anywhere in the corpus … the canonical neutron never routes the split through δ_th at all … structurally mismatched to the corpus's actual neutron ontology."* This over-reached: it inferred permanent δ_th-transparency from the bulk-cancellation, ignoring that the corpus's pinned FS completion route is `κ_FS`-consuming. Corrected above per findings R1.

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
- **C5** — whether δ_th softens the composite's coupling is **UNDETERMINED** (narrowed post-review R1): the corpus's own `neutron-identification.md:36`/`:77` TBD-pin instructs a proton-shaped FS derivation, which **consumes the δ_th-softened `κ_FS`** (`constants.py:896`) — so `κ_FS` carry-over is arguably the **canonical default**, not a new assumption; a competing linear-elastic route (`:54`) may be δ_th-free (FORK-OPEN). *(Pre-review framing "never invokes a `κ_FS` softening; adopting one would be a new assumption" preserved KEEP-BOTH in the driver's `MISSING_CHOICES` C5.)*

This is an **honest instrument gap, NOT a physics verdict**. The gate cannot be fired against the canonical construction because the corpus never built the instrument (the threaded-composite FS calculation).

### Sign: **FORCED POSITIVE (Δm > 0, neutron heavier) — δ_th-free, genuine.** Strengthened post-review (R2) to **Δm > 1.000 m_e**.

Independent of the magnitude, the canonical construction makes a falsifiable structural claim about the sign. Two justifications; the second is stronger and immune to the C2 caveat:

- **(1) Positivity of the two CANONICAL terms:** neutron = bare proton **+** threaded `0₁` electron (rest mass `≥ 0`) **+** Ax1-forced Borromean expansion (elastic strain energy `≥ 0`: Ax1 forbids the flux tube shrinking below `ℓ_node`, so the ring is *stretched*, not relaxed) ⇒ two **positive-definite additions** ⇒ **Δm > 0**. **CONDITIONALITY (R2):** this forces the sign only if the two named terms are exhaustive; the driver's own **C2** (threading-lock / boundary coupling energy) is enumerated missing with **sign undetermined**, and composite binding *can* reduce mass in this leaf family (He-4 is 28.3 MeV bound below its constituents, `proton-neutron-mass-split.md:28`). So (1) is "no assumption **beyond the two named terms**," conditional on C2 not being large-and-negative — not a flat "no assumption."
- **(2) β-decay-downhill energetics (canonical, C2-immune, STRONGER):** `neutron-identification.md:26` property 4 makes free-neutron β-decay **spontaneous** (the tensioned electron slips its lock and is ejected). A spontaneous decay is exothermic, so `m_n c² > (m_p + m_e) c² + KE + E_ν̄ ≥ (m_p + m_e) c²`, i.e. **Δm > 1.000 m_e** — a *global* final-state-rest-mass bound that **subsumes any C2 coupling term** and uses only the canonical fact that decay occurs (property 4), **not** the measured 1.293 MeV Q-value (no seed).
- Both are **δ_th-free and α-free** (`sign_leg` consumes zero module constants), and robust to the Reading X/Y mass-accounting ambiguity.

**This matches observation (the neutron IS heavier, and Δm ≈ 2.53 m_e > 1.000 m_e).** A real — if weak — structure signal: the corpus's neutron ontology gets both the sign AND the `> m_e` floor of the split right for a δ_th-independent reason. It does **not** certify δ_th (see interpretation-discipline #4).

---

## NO-REFIT / NO-MINT / NO-SEED AUDIT (self-review; the adversarial-review lens re-runs this)

Gate wiring hardened post-review (R3/R5/R6/R8): `run_gate()`'s own live path now diffs against an **independent** frozen HEAD table (the committed JSON sidecar `np_mass_split_gate_frozen_head.json`), not a self-snapshot — so a **source-level refit of `DELTA_THERMAL` / `KAPPA_FS_COLD`** (the audit's focal constants, formerly vacuous on the driver path) now trips the driver's own abort. The mint+seed guards are wired into the **emitted** component (`_guarded_component` gateway), not plant-only. A corpus-state detector flips off (iv) if a derived neutron mass appears.

| Rail | Check | Result |
|---|---|---|
| No refit (2) | live `ave.core.constants` consumed set == frozen HEAD — two independent anchors: `test_live_constants_equal_frozen_head` (6/6) **and** the JSON sidecar `run_gate()` diffs against | PASS |
| No refit (2) | `run_gate()` own live path aborts on a source-level `DELTA_THERMAL` / `KAPPA_FS_COLD` refit (`test_run_gate_aborts_on_source_level_refit_of_focal_constants`) | FIRES |
| No refit (2) | `KAPPA_FS == KAPPA_FS_COLD·(1−δ_th)` consistency + `PROTON_ELECTRON_RATIO` reproduced from `I_scalar/(1 − V·p_c) + 1` = `1836.1170402290593` | PASS (rtol 1e-12) |
| Refit plant | mutating **any of all 6** consumed constants by 1 ppm trips the abort (`test_refit_plant_trips_the_abort`, 6 constants) | FIRES |
| No mint (1,3) | fabricated `E_elastic` rejected on the **live emitted-component path** (`_guarded_component`) + plant test | FIRES |
| No seed (4) | a component whose VALUE = the answer (proton ratio / 1.293 / 2.531 / 939.565) rejected on the live path + plant test | FIRES |
| Detector (R6c) | bin (iv) flips if a derived neutron-mass symbol appears in the module (`test_detector_fires_if_derived_neutron_mass_appears`) | FIRES |
| Bin fireable | forcing a computable finite split moves the bin off (iv) → (i)/(ii)/(iii) (`test_bin_flip_plant_moves_off_iv`) | FIRES |
| EFT hygiene | `make verify` (verify_universe magic-number gate): driver + test both PASS, "MATHEMATICALLY PURE" | PASS |

Zero hard-coded physics numbers in the driver; the forbidden-seed set is **derived** from the module CODATA anchors (auto-tracks). All 41 tests pass (27 pre-review + 14 post-review gate-wiring); `make verify` exit 0.

---

## FLAG-DON'T-FIX — canonical-chain ambiguities surfaced (NOT resolved here)

Per Grant's durable flag-don't-fix directive; both are surfaced for adjudication, not silently reframed:

1. **Mass-accounting ambiguity (Reading X vs Y).** `proton-neutron-mass-split.md:10` attributes the **whole** 1.293 MeV surplus to "elastic expansion tension," with **no separate accounting of the threaded electron's rest mass** (0.511 MeV). Reading X (`m_n = m_p + m_e + E_elastic`) leaves `E_elastic = +0.782 MeV` (= the β-decay Q-value) underived; Reading Y (whole surplus = tension) leaves the entire +2.531 m_e underived. The verdict (bin iv, sign +) is **robust to both**; the ambiguity is flagged for Grant, not decided.

2. **The discriminator-timing finding** (interpretation-discipline #3, narrowed post-review R1): the audit card's second shot presupposes a `(2,q)`-adjacent δ_th-modulated eigenvalue neutron; the corpus's canonical neutron is a *composite additive* mechanism (the ontology part is corpus-correct). But the second shot is not permanently retired — it is **premature**: **Route A, the corpus's own `neutron-identification.md:77` TBD-pin (composite FS on threaded `0₁`-in-`6₂³`), IS the δ_th second shot against the CANONICAL neutron once built value-blind** — its proton-shaped FS solver consumes the δ_th-softened `κ_FS`, so a `κ_FS`-carry-over is arguably the canonical default (FORK: the `:54` linear-elastic route may be δ_th-free). Whether to build it is a Grant/auditor framing decision. *(Pre-review framing "would need a different construction … an even-`c` `(2,q)` sibling" preserved KEEP-BOTH in git; it wrongly retired the audit-card discriminator when the corpus's own TBD-pin route resurrects it.)*

---

## WHAT WOULD ACTUALLY FIRE THE SECOND SHOT (routed, not built)

The gate as designed is structurally unfireable against the canonical neutron. Two honest routes to a *real* second shot on δ_th (both require Grant/auditor adjudication before any build; neither is taken here):

- **★ Route A — build the threaded-composite FS instrument** (close C1–C5). This is the `neutron-identification.md:77` TBD-pin, and per the post-review narrowing (R1) it **IS the δ_th second shot against the canonical neutron**, not a different construction. It is a multi-session derivation with ≥5 new modelling choices; until those are made value-blind, any number it produces is a fit, not a second shot — but the instrument, once built, fires the discriminator the audit card wanted.

  **ROUTE A CHARTER CANDIDATE (Grant-gated; the review's real payoff).** Build the composite FS solve per the TBD-pin (threaded-electron constraint in the FS energy integral), **value-blind**, with frozen bins on the split: **{sign, magnitude band, δ_th-sensitivity ablation}**. The ablation is the two-for-one: **run the composite-minus-bare FS energy difference at BOTH the warm `κ_FS = 8π(1−δ_th)` AND the cold `κ_FS = 8π`; the DIFFERENCE of the two runs directly measures how much of the split rides δ_th** (resolving the C5 FORK empirically — FS-route δ_th-carrying vs linear-elastic-route δ_th-free). One build yields **both** the split prediction (the sign/magnitude gate) **and** the δ_th-loading measurement (the resurrected second shot on the R3/R7/R10/R12 provenance findings). Charter to be drafted and adjudicated by Grant/auditor, not this lane.
- **Route B — the δ_th-loaded difference that IS already in the corpus.** The Δ(1232) sibling rung (`c=7`) IS a δ_th-modulated eigenvalue and already on record: same δ_th → +2.35% miss (`epic-§40`, "proton-specific tightness = COINCIDENCE"). That is a second shot that already fired — and it points the way the coincidence reading predicts. It remains the operative fired δ_th second shot until Route A is built.

---

## BOTTOM LINE

The corpus's canonical neutron is a **composite additive structure**, not a `(2,q)` δ_th-eigenvalue rung. The audit card's cheapest sharp discriminator is **unfireable TODAY (bin iv)** — the split's dominant term (elastic-expansion tension) is mechanism-named and magnitude-underived because the composite FS instrument does not exist (C1). It is **premature, not permanently retired**: the corpus's own `neutron-identification.md:77` TBD-pin (Route A), built value-blind, IS that second shot — its proton-shaped FS solver consumes δ_th-softened `κ_FS`, so **δ_th-loading of the split is FORK-OPEN (C5-undetermined), not "never"** (narrowed post-review R1). The one thing the frozen chain *does* force — **the sign, and the stronger β-decay-downhill floor Δm > 1.000 m_e** — is δ_th-free, matches observation, and is a genuine (weak) structure signal that neither certifies nor impugns δ_th. The +0.74% bare-topology emergence result stands untouched. The operative fired δ_th second shot remains the Δ(1232) +2.35% miss, until Route A is built.
