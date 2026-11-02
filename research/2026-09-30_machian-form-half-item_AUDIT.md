# G3: single-auditor audit of the re-posed Machian form-half item

**Status:** audit record, stage G3 of the R61 gravity audit lane. It is not canon and it edits no open item.
**Criteria:** `_orchestration/2026-09-30_wave1-gravity-audit-brief.md@d55401e6e60db50b3a24e24fe57777c4fcac964c, section G3`.
**Object:** `_orchestration/open-items/2026-08-28-machian-form-half-adjudication.md` at `84d6fb3c6f768d80e39d422893242270f5c7533f` (129 lines), PR #1032. The RECORD body and its BLOCK banner are not audited.
**Run:** 2026-11-01, one read-only auditor. Citations in canon are at `origin/main` `cbc668e7`.
**Verified by the launching session, separately from the auditor:** the item text, the §6 caveat, the identity numerics, the H∞ arithmetic, the P23 and README lines, the docket row, and the wall-taxonomy, translation-circuit and omega-leaf cites.

---

## §1. Bin: ITEM-NEEDS-REPAIR

The arithmetic reproduces and the Γ-cell and channel defects are real. The item overstates the classification defect, drops a caveat, and has cite drift. Repairs are in §8.

---

## §2. Self-contradiction

`:26`: "**This needs no physics call. It is documentary, and it is real.**" `:110`: "it decides DECISION 1's physics half."

**Finding: two sub-decisions under one heading, with a scoping slip.** `:26` is true only of the documentary arm. `:110-111` makes the parent-BH audit decide whether "row 7's `Gamma` cell has real content", so the Γ-cell fill cannot be settled until the physics half is read. The channel and pointer defects do not depend on it.

---

## §3. Missing caveat: restore it

`BLIND-AUDIT:240-243`: "**The TL algebra was verified in the lossless uniform-line model the record itself uses; whether the K4 srs lattice's actual dispersion admits that model at cosmic scale was not checked** — if it does not, the record's table is wrong for a different reason and this correction is wrong too."

The item at `:89` says "**So canon's `Gamma = -1` at `R_H` is strictly LOAD-BEARING**" and at `:90-91` "it can, and only a short can", with no condition. This is the defect the same audit charged the routing item with (its B3, `:102`).

The expansion also needs a declared regime. For a shorted line `Z_in = jZ₀ tan(βl) ≈ jωL_p l [1 + (βl)²/3]`, so with `l = R_H` and `v = c` the relative correction is `(ω/H∞)²/3`. The linear statement holds only for `ω ≪ H∞`.

---

## §4. x = x identity

From `src/ave/core/constants.py`: `G` is an input (`:188`, under `:187` "Input 3: The Machian boundary"). `H_INFINITY = 28π m_e³ c G/(ħ²α²)` (`:752`). `R_HUBBLE = c/H∞` (`:755`). `XI_MACHIAN = ħc/(7 G m_e²)` (`:650`).

**Algebra.** `H∞ = K·G`, where `K` holds no `G`. With `ℓ_node = ħ/(m_e c)`, `R_H/ℓ_node = ħα²c/(28π m_e² G)`. Multiplying by `4π/α²` gives `ħc/(7 m_e² G) = ξ_M`. `G`, `α` and `π` cancel.

**Numerics, re-run from the module.** `H∞` = 2.246561628e-18 s⁻¹ = 69.3216 km/s/Mpc. `R_H/ℓ_node` = 3.455699e38. `ξ_M` = 8.154834e43. `4π(R_H/ℓ_node)α⁻²/ξ_M` = 0.9999999999999994. `H∞/G` = 3.3659884e-8, equal to the closed form to rounding.

**Finding.** The agreement is one equation solved for two unknowns and cannot fail. Canon already says so: `constants.py:638` ("Class E circularity (intentional)"), `interlock-register.md:216` ("circular by construction"), and `manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md:37` ("the same algebraic relation written two ways"). The one non-identity is 69.32 against measured H.

The item itself makes no agreement claim. The identity bears on it through DECISION 2: the row "Live `H(t)`, `Gdot/G = -(1+q)H`" follows from `H∞ ∝ G`, which the item never states.

---

## §5. H∞ double-booking

**Definition,** item `:72`: the fixed asymptote is compared with `H₀√Ω_Λ`, given as 55.74, with `Ω_Λ = 1/1.4605`.

| H₀ used | H₀√Ω_Λ | 69.3216 against it |
|---|---|---|
| 67.36 | 55.738 | **+24.37%** |
| 67.4 (the README's Planck) | 55.771 | +24.30% |
| 69.8 (TRGB) | 57.757 | +20.02% |
| 73.0 (the README's SH0ES) | 60.405 | +14.76% |

The item's 55.74 needs H₀ = 67.36, which it does not state. The implied `H₀ = 69.3216/√Ω_Λ = 83.78` matches the item's 83.8. The 0.7% is `|69.3216 − 69.8|/69.8` = 0.685%. `1.2437² = 1.547`, which ties to the "1.54" at `vol3/claim-quality.md:984,:1004`.

**Cross-check on P23,** `manuscript/consistency-manifest.yaml:200-231`: `type: operating_point_projection`, `error_percent: 0.7`, `public_in_readme: true`, and "not four independent percent-error claims". Its name is "H∞ (Hubble asymptote)", while it scores against `TRGB (late-universe)`.

`README.md:238` reads "0.7% vs TRGB | ✅ Sits between Planck (67.4) and SH0ES (73)". It drops P23's Class-E qualifier, and the README's classification note at `:215` lists four kinds of claim, none of them an operating-point projection.

The item omits that `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:91-94` books both readings in one leaf: "**AVE asymptote** | **69.32**" and "$H_\infty$ is the de Sitter asymptote".

---

## §6. DECISION 2 against the docket

`_orchestration/2026-07-10_rulings-docket.md:253`, row `| **G-Ġ** *(stub booking row)*`: "naive-live / flatness-live / fossil / attractor vs `Ġ` bounds", fork "**UNRESOLVED**".

**Finding: a second home for the `Ġ` side of the same fork, plus one new element.**
- **Same:** the item's live-H and fixed-H∞ rows are that fork.
- **Different in base:** the item's multiples are 36× to 3393×, on `(1+q)H` ≈ 3.26e-11/yr. The docket's are ~190× to 7600×, on `~H₀` ≈ 7e-11/yr. The item does not say it departs from the docket.
- **Different in cut:** four branches become two rows, and "both docket rows" (`:77`) are unnamed. By inference they are G-Ġ `:253` and WHEN `:252`.
- **New:** the README and P23 +24.4% consequence is not in the docket.
- **Scope of "every number reproduced" (`:61`):** arithmetic only. `BLIND-AUDIT:245` says the `Ġ` bounds were not fetched against primary sources, and `research/2026-07-11_astro-adjudicator-sweep_result.md:214` marks the 1.5e-13 as UNVERIFIED.

---

## §7. Documentary correction: covered in substance, with limits

The 2026-06-14 G-ruling books ξ as VALUE-fitted (`interlock-register.md:216`, `:222`). It does not name the taxonomy layer. But `wall-taxonomy.md:174` row 7 already carries "⚠ **Class:** $G$ is **MIXED — derived-FORM, calibration-fitted-VALUE**", `:164` says "this leaf promotes nothing", and `:16` declares row 7's phase-state.

So the item's "promote it as physics" and its `:160` charge are overstated for wall-taxonomy. They stand for the Γ cell (which restates the noun), for channel "all" against the `:155` rule, and for `translation-circuit.md:134` and `:522`, which carry no MIXED qualifier (`:522` reads "$\checkmark$ structural").

**Disposition.** Aligning those rows to `ilk-gravmb` is orchestrator polish. The other arm of the sentence, "or does `ilk-gravmb` get revisited", is a Grant call. It is also where the physics half lands, and the item does not say how a parent-BH result would bear on the VALUE classification.

---

## §8. Repairs

1. Scope `:26` to the documentary arm, name the physics half as its own sub-decision, and state that the Γ-cell fill waits on it.
2. Restore the §6 caveat at `:84-91` with the regime `βl ≪ 1` declared. Make "strictly" and "only a short can" conditional.
3. Replace "promote it as physics" with the real defects: the Γ cell, channel "all", and the missing qualifier in translation-circuit. Drop or qualify the `:160` charge.
4. Fix "`wall-taxonomy.md §10.3`": the leaf has §10, §10.1 and §10.2. The quote is `:431`, item 3 of the §10 ruling, and that ruling is scoped to yielded surfaces.
5. State the 55.74 inputs (H₀ = 67.36, `Ω_Λ = 1/1.4605`), and add the `H∞ ∝ G` line with the `hubble-tension.md:37` cite.
6. Name the docket rows, reconcile 36–3393× with 190–7600×, scope "every number reproduced" to arithmetic, and cross-reference the docket instead of presenting a fresh fork.
7. Cite fixes. "`op14:12`" is `op14-cosmic-horizon-profile.md:14` and `:20`. The translation-circuit "`:450`" cited at `wall-taxonomy.md:174` is stale: the means-test row is `:522`. Route, do not fix: `ilk-gravmb` at `:216` cites `constants.py:589` and `:177`, which are now `:650` and `:188`.
8. Carry forward that `omega-freeze-cosmic-grain-cascade.md` (234 lines, zero hits on the item's regex) does contain "Machian impedance integral" at `:19` and `:226`.

**What holds.** The arithmetic. The cites `interlock-register.md:216`, `wall-taxonomy.md:155,:174`, `translation-circuit.md:134`, and the omega-leaf zero-hit claim.
