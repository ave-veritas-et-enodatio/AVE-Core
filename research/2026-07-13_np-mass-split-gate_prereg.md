# THE N–P MASS-SPLIT GATE — FROZEN PRE-REGISTRATION

**Date:** 2026-07-13 · **Lane:** implementer — same-frozen-chain derivation + no-refit consistency driver.
**Brief (binding):** the audit card `WHAT WOULD SETTLE IT #1` (m_p/m_e value-blind audit, run `wuvmckx8q`) — Grant GO 2026-07-13 with an explicit interpretation-care directive ("be very very careful upon interpreting the results").
**Branch:** `derivation/np-mass-split-gate` · **PR:** opens `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` (only Grant merges).

**FREEZE-BY-PUSH.** This prereg lands as its OWN commit, PUSHED to origin, BEFORE any driver / derivation / result / test code exists in the tree. The freeze margin is the gap between this push and the first code push — auditable from the GitHub push timestamps. No bin, tolerance, target, hard rail, or verdict-consequence in this document is edited after the first computation runs (Rule 11).

---

## THE ONE-SENTENCE GATE

Same frozen chain, same δ_th, **no refit**: does the corpus's *canonical* neutron construction (`n = 6₂³ ∪ 0₁`) produce the n–p mass split **+1.293 MeV (+2.531 m_e), sign included (neutron heavier)** — the discriminating second shot on the m_p/m_e claim, because a coincidence-tuned δ_th has no reason to survive a *difference* measurement where the bulk proton mass cancels and only chain structure remains?

---

## SECTOR HEADER (declared before any substrate claim)

- **MODE:** derivation-from-canon + no-refit arithmetic consistency driver. **NOT engine-fire.** No new primitive; the instrument evaluates the *existing* canonical proton eigenvalue chain and the *existing* canonical neutron construction, and asks whether the latter defines a computable mass split at all.
- **REGIME:** cold lattice, baryon sector. The proton mass is the self-consistent Faddeev–Skyrme feedback eigenvalue at crossing number `c=5` (`constants.py:954-956`); the neutron is a **composite** — a `6₂³` proton Borromean cage with a `0₁` unknot electron threaded through the central void (`neutron-identification.md:13`). Static rest-mass eigenvalues; no dynamics.
- **PHASE-STATE:** bound topological solitons — proton Borromean cage (three mutually entangled flux loops, `(2,5)` cinquefoil) plus a threaded `0₁` unknot. The mass split is a **rest-energy difference** between two bound configurations.
- **SECTOR:** **A1 (dilatation / mass) is what this measures.** The mass split is an A1-sector energy question (rest mass + elastic strain of the stretched cage), **NOT** a charge-sector question. Charge = Cosserat `(2,3)` winding (untouched); the threaded electron's `−1` is an Ax2 TKI twist that literally cancels the proton's `+1` for net-zero (`neutron-identification.md:24`). A1 ⊥ charge respected throughout; the split is not to be cross-wired to the charge cancellation.

**Phase-space coordinate check:** the measured quantity is the **dimensionless rest-mass ratio / difference in m_e units** — both the corpus target (`+2.531 m_e`) and any computed quantity live in that same real, dimensionless coordinate. Matched. This is NOT a phase-space φ² claim; no real-space-vs-phase-space mismatch is possible here.

**Consistency-vs-emergence tag:** the proton m_p/m_e is a **consistency/manifestation-class** result (α and m_e are imported electron-sector inputs; `proton-identification.md:13`). A *computable* n–p split from the same frozen chain, with **no neutron-CODATA input**, would be an **emergence-class** test (the neutron mass is not an input anywhere in the chain — it appears only as the CODATA anchor `M_N_MEV_TARGET`, `constants.py:1104-1107`, "no framework derivation has yet been adopted for the neutron mass"). If the construction turns out non-computable, the verdict is **instrument-gap-class**, not an emergence pass or fail.

---

## THE FROZEN CHAIN (quoted with receipts — this is the ONLY chain permitted)

### A. The canonical proton eigenvalue chain (`constants.py:954-956`, verified at base `9bfc50ef`)

```
_X_CORE               = I_SCALAR_1D / (1.0 - V_TOROIDAL_HALO * P_C)      # :955
PROTON_ELECTRON_RATIO = _X_CORE + 1.0                                    # :956  → 1836.1170402290593
```

Frozen consumed constants (HEAD literals — the no-refit reference set; any deviation at run time is a finding):

| Constant | Value | Receipt |
|---|---|---|
| `I_SCALAR_1D` | `1161.9870305252678` | `constants.py:910` (FS scalar trace, `c=5`) |
| `V_TOROIDAL_HALO` | `2.0` | `constants.py:951` (dual-reactance count; Grant-adjudicated 2026-06-01) |
| `P_C` | `8.0*pi*ALPHA` ≈ `0.18340` | `constants.py:478` |
| `ALPHA` | `7.2973525693e-3` | `constants.py:163` (imported CODATA) |
| `KAPPA_FS_COLD` | `8.0*pi` ≈ `25.1327` | `constants.py:832` |
| `DELTA_THERMAL` | `1.0/(14.0*pi**2)` ≈ `0.0072137` | `constants.py:893` (the δ_th under audit) |
| `KAPPA_FS` | `KAPPA_FS_COLD*(1-DELTA_THERMAL)` | `constants.py:896` |
| `PROTON_ELECTRON_RATIO` | `1836.1170402290593` | `constants.py:955-956` / ladder literal `:1005` |

**δ_th enters the proton mass through `KAPPA_FS` → `I_SCALAR_1D` (the FS solver at `c=5`).** This is the value whose provenance the audit card flags as pre-git-minted, once-re-tuned (`1/(28π)→1/(14π²)`, ×2/π), single-site, Lenz-6π⁵-adjacent.

### B. The canonical neutron construction (`neutron-identification.md` clm-6kwzot; `proton-neutron-mass-split.md` clm-bh9p6s)

Verbatim canonical identification (`neutron-identification.md:13`, boxed load-bearing finding):

> the neutron in AVE is a **composite structure** — a proton (`6₂³` Borromean linkage) with an electron (`0₁` unknot) topologically threaded through its central structural void: `n = 6₂³ ∪ 0₁`.

The mass split, verbatim, `proton-neutron-mass-split.md:10` (clm-bh9p6s, the asserted-identity leaf):

> Because Axiom 1 dictates that no flux tube can shrink below a transverse thickness of `1 l_node`, forcing an electron tube into the proton's core requires the Borromean rings to stretch outward. This elastic expansion tension accounts for the mass surplus the neutron possesses relative to the bare proton.

**Derivation-status receipts (what the corpus itself says is computed vs asserted):**

- `neutron-identification.md:25` (§1 property 3): *"**Mechanism canonical; quantitative value not derived (TBD).**"*
- `neutron-identification.md:36` (§2 mass-split row): *"⚠️ **MECHANISM derived, MAGNITUDE not** — no FS calculation of threaded-knot energy producing 1.293 MeV; corpus uses empirical value as input downstream."*
- `neutron-identification.md:43` (§2 rest-mass row): *"**PARTIAL** — m_p component is the framework's flagship mass prediction … the Δm ≈ 1.293 MeV addition is empirical input."*
- `neutron-identification.md:54` (§2.1): a structural bound exists but *"does not derive"* the split, and even the bound's `ℓ_node`-radial-expansion premise is 🔴 FLAGGED as *"not established."*
- `neutron-identification.md:77` (§4): *"the quantitative derivation via Faddeev-Skyrme solver applied to the `6₂³ ∪ 0₁` composite topology is NOT in the corpus."*
- `constants.py:1104`: *"no framework derivation has yet been adopted for the neutron mass."*
- clm-bh9p6s (`proton-neutron-mass-split.md`) **computes** He-4 binding, T_nuc, elastic displacement Δx, and the gravity-hierarchy factorisation — but **never computes the n–p split**; the `1.293 MeV` appears only as an asserted attribution, never as a solver output.

**Canonical fact frozen here:** the neutron construction is explicitly **NOT a `(2,q)` torus-knot ladder entry** (`neutron-identification.md:23`: "NOT a different `(2,q)` family entry"). Therefore the split may **NOT** be computed by plugging an even crossing number into `BARYON_LADDER` — the ladder is odd-`c` only and does not represent the neutron.

---

## THE FROZEN BINS (pre-named bands; consequences frozen verbatim)

**Target (named from CODATA anchors — band-naming only, NOT a derivation input):**
`Δm_target = M_N_MEV_TARGET − M_P_MEV_CODATA = 939.565420 − 938.272088 = 1.293332 MeV`
`= 1.293332 / 0.51099895 = +2.531 m_e` (`constants.py:1106-1107`; m_e c² = 0.51099895 MeV CODATA). *(The audit card's `+2.53 m_e` / task's `+2.532 m_e` are the same target to rounding.)*
`2×` band (same sign): `|Δm| ∈ [1.266, 5.062] m_e`.

- **(i) STRUCTURE-SIGNAL.** The frozen chain produces a computable split with **correct sign (Δm > 0, neutron heavier) AND `|Δm|` within 2× of `2.531 m_e`** (i.e. `Δm ∈ [+1.266, +5.062] m_e`). *Consequence:* the ppm precision survives a difference measurement — the tuning hypothesis is made **strictly harder to hold** (NOT: refuted; see interpretation-care).

- **(ii) WRONG-SIGN.** The frozen chain produces a computable split with **proton heavier (Δm < 0)**. *Consequence, frozen verbatim:* **"the ppm precision of the m_p/m_e chain is confirmed a proton-specific coincidence — a δ_th tuned to land the proton on CODATA has no reason to produce the correct sign of a difference measurement, and it did not. This corroborates the epic-§40 Δ(1232) +2.35% miss ('proton-specific tightness = COINCIDENCE')."**

- **(iii) RIGHT-SIGN-WRONG-MAGNITUDE (>2×).** The frozen chain produces a computable split with **correct sign (Δm > 0) but `|Δm|` outside the 2× band** (`< 1.266 m_e` or `> 5.062 m_e`). *Consequence:* **partial** — structure carries the sign but not the scale.

- **(iv) CHAIN-INSUFFICIENT.** The canonical neutron construction **does not define a computable mass without new assumptions.** *Consequence:* an **honest instrument gap, NOT a physics verdict** — the second shot cannot be fired because the corpus never built the instrument (the threaded-composite FS calculation). If (iv), the deliverable is a **verbatim enumeration of every missing choice**, and the sign sub-finding (below) is reported separately as the one thing the construction *does* force.

---

## HARD RAILS (binding — Grant's care directive)

1. **No new parameters minted.** Zero constants introduced beyond frozen set A + the electron rest mass (`M_E`, already canonical, the `0₁` unknot = 1 m_e).
2. **No refit.** `I_SCALAR_1D`, `V_TOROIDAL_HALO`, `P_C`, `ALPHA`, `KAPPA_FS_COLD`, `DELTA_THERMAL` are consumed **as-is from the live module**; the driver diffs each against the HEAD literal table above and aborts on any mismatch.
3. **If the computation requires ANY choice not already canonical → STOP at bin (iv) and ENUMERATE the choices. Do NOT make them.** In particular: any ansatz for the threaded `0₁`-in-`6₂³` FS field, any threading-lock energy term, any Borromean elastic stiffness, any mass-accounting convention (rest-mass-additive vs absorbed), any κ_FS-softening of the composite — all are **new assumptions**; if one is needed, the verdict is (iv) and that choice is listed, never made.
4. **Never seed from `1836`, `1.293`, `2.53`, `2.531`, `2.532`, or `939.565` inside the derivation.** These appear ONLY as target-band names in this prereg and as CODATA anchors in the honest-comparison line — never as inputs the computation reads to produce a result.
5. **Freeze-by-push** — this prereg is its own pushed commit before any code.
6. **DO-NOT-MERGE** — PR opens `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`; only Grant merges.

---

## INTERPRETATION-CARE (frozen BEFORE the run — what each bin does and does NOT establish)

Per Grant's verbatim directive. The verdict section of the RESULT must carry this discipline **before** stating the bin.

- **A bin-(i) pass does NOT certify δ_th's provenance.** It does not convert the pre-git-minted, once-re-tuned, single-site correction into a first-principles constant. It makes the *tuning hypothesis strictly harder to hold* (a difference measurement is a genuinely independent second constraint that a proton-only fit had no reason to satisfy) — but the audit-card provenance findings (R3, R7, R10, R12) stand untouched; a chord on the difference does not retroactively de-tune the level.
- **A bin-(ii) / bin-(iv) result does NOT falsify the +0.74% bare-topology emergence result.** That result — `κ_FS = 8π` (cold) → `1849.70 (+0.7377%)` from integers + imported α — **stands independently** of δ_th and of the neutron construction. It is the genuinely-unusual, gated content (`proton-identification.md:13`); the n–p gate speaks only to the **ppm digits** that ride δ_th, never to the bare-topology result.
- **A bin-(iv) is an instrument gap, not a falsification.** "The corpus never built the neutron-mass instrument" is a statement about the corpus's completeness, not about whether AVE's neutron is right or wrong. It neither confirms nor refutes the proton-specific-coincidence hypothesis — it means the *cheapest sharp discriminator cannot be fired as designed.*
- **★ The load-bearing reframe (disclosed pre-run, flag-don't-fix):** the audit card's imagined test — "same δ_th, difference measurement, only chain structure remains" — presupposes the neutron is a **δ_th-modulated re-evaluation of the same eigenvalue chain** (a `(2,q)`-adjacent rung). **The corpus's canonical neutron is NOT that.** It is a *separate additive threaded-electron mechanism* (rest mass + elastic-expansion strain), and it is explicitly **not** a `(2,q)` ladder entry. In the difference `m_n − m_p`, the bulk proton mass **and its δ_th correction cancel**, and what remains (the elastic-expansion tension) is **not a δ_th-governed quantity anywhere in the corpus.** So the "does the same δ_th survive?" discriminator, as imagined, **does not actually load δ_th** — the canonical neutron does not route the split through δ_th at all. This is surfaced, not silently resolved; it is the reason a bin-(iv) here is *expected* rather than surprising, and it is itself a finding about the discriminator's design.

---

## THE SIGN SUB-FINDING (frozen — reported separately from the magnitude verdict)

Independent of whether the magnitude is computable, the canonical construction makes a **falsifiable structural claim about the SIGN**, with no new assumption:

- The neutron = bare proton **plus** a threaded `0₁` electron (rest mass `≥ 0`) **plus** an Ax1-forced Borromean expansion (elastic strain energy `≥ 0`, since Ax1 forbids the flux tube shrinking below `ℓ_node`, so the ring is *stretched*, not relaxed).
- Both named contributions are **positive-definite additions** to the bare-proton energy ⇒ **the sign is structurally forced to Δm > 0 (neutron heavier).**
- This is a genuine, canonical, **δ_th-free** result: the sign does NOT come from the tuned correction; it comes from the composite topology + Ax1. It is reported as the one thing the frozen chain forces, and it is **robust to the mass-accounting ambiguity** flagged below.

---

## FLAG-DON'T-FIX — canonical-chain ambiguity surfaced (not resolved)

A genuine looseness in the corpus, surfaced for Grant, **not** resolved in this gate:

- `proton-neutron-mass-split.md:10` attributes the **whole** 1.293 MeV surplus to "elastic expansion tension" — with **no separate accounting of the threaded electron's rest mass** (`m_e = 0.511 MeV`). Two readings result:
  - **Reading X (literal composite):** `m_n = m_p + m_e(threaded) + E_elastic`. Frozen chain fixes `+1.000 m_e` (rest mass); the residual `E_elastic = +1.531 m_e = +0.782 MeV` (= the β-decay Q-value `m_n−m_p−m_e`) is the underived part.
  - **Reading Y (corpus prose literal):** the whole `+2.531 m_e` is "elastic tension"; the rest mass is not separately added. Frozen chain fixes *nothing* of the magnitude.
- Both readings leave the **magnitude underived** (`E_elastic` is TBD in both) and both force **Δm > 0**. The verdict is robust to which reading Grant adopts; the ambiguity is flagged for adjudication, not decided here.

---

## DISCLOSED LEANING (I am open to the driver adjudicating otherwise)

My pre-run leaning, from reading the canonical leaves: **bin (iv) CHAIN-INSUFFICIENT**, with the **sign sub-finding (Δm > 0) forced** and the **magnitude non-computable** (the dominant/whole component — elastic-expansion tension — is mechanism-named, magnitude-TBD, and requires a threaded-composite FS calculation the corpus has not built). If the driver surfaces a legitimate frozen-chain path to a *number* for the split (bin i/ii/iii), I report that instead — the substrate adjudicates.

---

## THE INSTRUMENT (what the driver computes — no-refit, fireable)

1. **No-refit reproduction (positive control that CAN fail):** re-derive `PROTON_ELECTRON_RATIO` live from the module and assert `= 1836.1170402290593`; diff every constant in frozen set A against the HEAD literal table; **abort on any mismatch** (this is the gate that fires on a refit-plant).
2. **Sign leg (α-/δ_th-free):** assert both named neutron contributions are positive-definite (rest mass `+1 m_e`; elastic strain `≥ 0` by Ax1) ⇒ report `sign(Δm) = +` as a structural result.
3. **Magnitude-computability leg (the gate):** enumerate every frozen-chain quantity that maps to a split component; show the only one available is the electron rest mass (`+1.000 m_e`, Reading X) or nothing (Reading Y); show the elastic-expansion tension has **no** frozen-chain value (no code path, no literal — `M_N` is a CODATA target, not a derived quantity). Emit **bin (iv)** with the missing-choice enumeration UNLESS a frozen-chain magnitude path exists.
4. **Plant tests (gates that fire):**
   - a **refit plant** (mutate a consumed constant) must trip the no-refit abort;
   - a **seed plant** (inject `1.293`/`2.531`/`939.565` as a computation input) must be caught by the no-seed guard;
   - a **mint plant** (a fabricated `E_elastic` constant with no canonical provenance) must be rejected by the provenance check — the driver refuses to emit a magnitude from a constant not in frozen set A;
   - a **bin-flip plant** (force a computable finite split) must move the reported bin off (iv) — proving (iv) is a physics/corpus verdict, not an instrument that cannot fire.

---

## SKILL-SELECTION PLAN (60-sec, pre-workstream)

APPLIED: **ave-prereg** (this doc), **ave-canonical-leaf-pull** (neutron + proton identification + mass-split leaves pulled + audit card), **verify-before-cite** (every quote grep-confirmed at base `9bfc50ef`; constants at file:line), **substrate-native-check** (A1 mass sector ⊥ Cosserat charge; the split is a rest-energy A1 question, not a κ_FS phase-space quantity), **phase-space-coordinate-check** (measurement in the matched dimensionless m_e-ratio coordinate — no real-space/phase-space mismatch), **consistency-vs-emergence** (proton = consistency; a computable split would be emergence; non-computable = instrument-gap — tagged), **ave-canonical-source** (constants consumed live from `ave.core.constants`, never hard-coded; diffed against HEAD), **ave-discrimination-check** (the sign is a genuine structural claim; the SM has no pure-number n–p split either — symmetric standard noted), **flag-don't-fix** (the mass-accounting ambiguity + the discriminator-design reframe surfaced, not resolved). NOT-fired: engine/loop-gap skills (no engine-fire); pre-test-physics-check dispatch (the one load-bearing reframe — the canonical neutron is not a δ_th-modulated eigenvalue — is surfaced in this prereg's interpretation-care, not deferred).
