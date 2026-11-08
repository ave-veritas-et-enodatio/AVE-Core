# PANEL-AUDIT: the matter sector against canon as written (#1028 + #1029)

**Status:** audit record, stage G1b of the R61 gravity audit lane. It is not canon. It edits no leaf, open item or audited branch, recommends no arm, and rules on no regime.
**Criteria:** `_orchestration/2026-09-30_wave1-gravity-audit-brief.md@d55401e6e60db50b3a24e24fe57777c4fcac964c, section G1`.
**Canon reading:** `research/2026-09-30_gravity-matter-sector_G1a-canon-reading.md` at `9c131d02ccf2dacff2d8eb671e09f8e733b5099d`, pushed and verified before this stage began.
**Objects:** #1028 at `2f19d551`, #1029 at `c0e5fd75`. Canon at `origin/main` `cbc668e7`. All three unchanged across the stage.
**Run:** 2026-11-01. One run of `.claude/workflows/ave-adversarial-pr-review.js` (`wf_eba98525-696`): six lenses, 28 findings, 34 agents, no errors, `refuted_count` = 1.
**Re-run by the launching session, separately from the panel:** the sketch `:63` expansion (sympy), the scalar-arm F by own quadrature (0.16666666, GR control 1.00000035), Mercury and η arithmetic, and 17 sampled census sites at their cited lines. Other values below rest on the panel and its verifiers.

---

## §0. Verdict

**K = K5, REGIME / UNBINNED: a STUCK-POINT for Grant.** **S = S5, NO CONSENSUS.**

**Conditional K, characterization and not verdict: K2 (OVERCLAIM) under every regime reading.** It is not K1: K1 needs Q1 FIXED, and the held Q1 is AMBIGUOUS. So on these bins the printed "Exact match with GR" rests on a choice canon never makes. These bins do not establish a kill on canon as written. Canon offers three routes to a slow bound body:

| Arm | What it is | Result |
|---|---|---|
| `scalar` | `n_scalar` on the Gordon form | F = 1/6. EXCLUDED on Mercury and on LLR. |
| `ntns` | the `(n_t, n_s)` metric the print box cites | Cannot be completed from what canon writes. FAILED, UNTESTABLE. |
| `adopted-gr` | the GR potential the print box says it adopts | CONSISTENT, because it is GR typed in. |

**Separately from the K bin:** the Item-5 sentences at `anomalous-perihelion-advance.md:10` and `:20` name the `n_scalar` route themselves. On that route the derivation they report contains an arithmetic slip, and the route gives F = 1/6 (§4.2). That failure lands on those sentences' own carrier whichever arm canon means.

---

## §1. Assignment

**Held-bin rule (brief, G1).** A bin is held if its own verify verdict is CONFIRMED or DOWNGRADED; `corrected_severity` is ignored. A bin is not held if it is REFUTED or missing. K and S are assigned from held bins only.

**Precedence applied, K4 > K5 > K3 > {K0, K1, K2}.**
1. **K4 does not fire.** Q1 is held. With Q1 AMBIGUOUS the test is whether Q2 or Mercury is not held on any arm under test. Both are held on all three arms (§2).
2. **K5 fires, on two independent clauses.** Q0 is CONFLICTING and held. Separately, a computed control parameter puts Mercury outside Regime I: `g_N/a_0` = 3.69e8 on `A0_LATTICE` = cH∞/2π = 1.0719e-10 m/s² (`src/ave/regime_3_saturated/galactic_rotation.py:56`), Regime IV by `domain-catalog.md:132`. The catalog's own `a_0 ≈ 1.2e-10` (`:127`) gives 3.30e8 and the same regime. The Cassini clause does not fire: Cassini (light) is CONSISTENT.
3. K5 outranks K3 and {K0, K1, K2}, so the K bin is K5. §3 states the conditional bins, as the brief requires.

**Precedence applied, S5 > S3 > the rest.** Q4 is not held, so S5. ARITH = HOLDS, so S3 would not fire in any case. The SN-PRED bins are candidates on two channels, not a verdict on an assigned channel.

---

## §2. Every bin, with its verify verdict

`refuted_count` was 1 in each stage. Both refuted bins are recovered here.

| Bin | Lens | Verdict | Status |
|---|---|---|---|
| Q0 = CONFLICTING | canon-reader (G1a) | CONFIRMED | held |
| Q1 = AMBIGUOUS | canon-reader (G1a) | CONFIRMED | held |
| Q4 = CANON-SILENT | canon-reader (G1a) | **REFUTED**, verifier names AMBIGUOUS, not a listed bin | **not held** |
| Q2[scalar] = REPRODUCED | rederive-scalar | CONFIRMED | held |
| Q3[scalar, Mercury] = EXCLUDED | rederive-scalar | CONFIRMED | held |
| Q3[scalar, LLR-eta] = EXCLUDED | rederive-scalar | CONFIRMED | held |
| REGIME[Mercury, ε11] = Regime I | rederive-scalar | CONFIRMED | held |
| REGIME[Mercury, g_N/a_0] = Regime IV | rederive-scalar | CONFIRMED | held |
| Q2[ntns] = FAILED | rederive-ntns | CONFIRMED | held |
| Q3[ntns, Mercury] = UNTESTABLE | rederive-ntns | CONFIRMED | held |
| Q3[ntns, LLR-eta] = UNTESTABLE | rederive-ntns | CONFIRMED | held |
| REGIME[Mercury, A_gm] = Regime I | rederive-ntns | CONFIRMED | held |
| REGIME[Mercury, τ/τ_yield] = not computable from canon | rederive-ntns | CONFIRMED | held |
| Q2[adopted-gr] = REPRODUCED | rederive-adopted-gr | CONFIRMED | held, scoped to F arithmetic |
| Q3[adopted-gr, Mercury] = CONSISTENT | rederive-adopted-gr | CONFIRMED | held |
| Q3[adopted-gr, LLR-eta] = CONSISTENT | rederive-adopted-gr | CONFIRMED | held |
| REGIME[Mercury, ΔS] = I | rederive-adopted-gr | CONFIRMED | held |
| REGIME[Mercury, Δφ/α] = I | rederive-adopted-gr | CONFIRMED | held, characterizes G1a FLAG 1 |
| ARITH = HOLDS | sn1987a | CONFIRMED | held |
| SN-PRED[scalar] = EXCEEDS | sn1987a | CONFIRMED | held, candidate |
| SN-PRED[light] = WITHIN | sn1987a | CONFIRMED | held, candidate |
| Q3[light, Cassini] = CONSISTENT | sn1987a | CONFIRMED | held |
| CENSUS: 48 sites | census-and-repairs | **REFUTED**, verifier names 60 sites as a floor | **not held** (§7) |

The workflow drops REFUTED findings from its return. Both are recovered from the run journals and `clean_reports`.

---

## §3. Conditional K under each regime reading

**Characterization, not verdict.**

| Reading | Ruler | Computed at Mercury | What the reading does to the arm values | Conditional K |
|---|---|---|---|---|
| A | none named, "II (Yield)" | No ruler computes II. On the Vol 1 Ch.4 ladder Δφ/α is rung I, at most 3.08e-5 on either mapping tried. The row may be a domain tag. | Canon writes no altered index | **K2** |
| B | A_gm | 8.03e-40, Regime I. Reads the spin sector only. | None | **K2** |
| C | ε11 / ΔS | ε11 = 1.785e-7 (2.247e-7 at perihelion), ΔS = 1.59e-14, Regime I | Not on any arm as frozen: `scalar`'s Lagrangian carries no S. If canon's clock kernel were placed on the orbiting body, it would enter at O(U²) and move β only (§11, "What remains live"). | **K2** |
| D | g_N/a_0 | 3.69e8 (range 2.5e8 to 5.9e8) on `A0_LATTICE`, 3.30e8 (2.3e8 to 5.2e8) on the catalog's 1.2e-10 (§1), Regime IV | Gates drag, not the index | **K2** |
| E | τ/τ_yield | Not computable: canon gives no τ(r) | None written | **K2** |

**Why K2 in every row.** Q1 is AMBIGUOUS, and at least one quoted arm is EXCLUDED: `scalar`, on both Mercury and LLR.

**Why no reading moves it.** Every regime effect canon writes either gates drag or enters at O(U²). `γ = 0` on this arm is first order, so an O(U²) term moves β only. F = 1 with η = 0 forces (β, γ) = (1, 1) uniquely, and F = 1 at γ = 0 needs β = −1, hence η = −7. A tuned second-order term can fit Mercury alone (`n = 1 + U + (5/2)U²`) and then fails LLR. A regime reading could change this row only by supplying a first-order index that canon does not write.

**K2 against K3: a decision by the launching session.** K3 reads "Q2 is FAILED ... on an arm that K0–K2 need". Q2[ntns] is FAILED. But K2 needs only "at least one quoted arm is EXCLUDED", which `scalar` supplies, and K0 is already blocked by that same arm. No live bin needs `ntns`, so K3 does not fire. Had `scalar` not been EXCLUDED, K3 would have fired. This is flagged for the orchestrator's review. It is conditional only, because K5 governs.

**Sensitivities, not verdicts.**
- K1 needs Q1 FIXED. It is unreachable on the held Q1.
- K0 needs every quoted arm CONSISTENT. `scalar` blocks it.
- `ntns` moves to CONSISTENT if the arm is redefined to Ch 2's pair: `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex:157` prints a clock with `b2 = 1/2` in an isotropic chart. That site labels itself "a consistency recovery", the pair drops `n_s`, and its companion index is scoped to electromagnetic waves.
- K2's only EXCLUDED witness is `scalar`, so conditional K2 rests on M4 (§11) and with it on the Gordon `g_ij = δ_ij`, the spatial sector canon defers (`claim-quality-closure-roadmap.md:205`; sketch `:80`). That sector alone does not clear the arm. Hold the written `g₀₀` (β = 3/2) and free γ: Mercury's 5σ window on §5's ±0.04 is γ in [1.243, 1.257], LLR's is [2.997, 3.002], and they do not overlap. Re-run by the launching session in the repair pass.
---

## §4. Q2: derivations per arm

**MODE / REGIME / PHASE-STATE, held across routes.** Matter clock of a gapped packet in a slow bound orbit. REGIME from the computed ε11: Regime I, with Q0 CONFLICTING carried and not resolved. Cold, sub-yield, static, single source, test body. Perihelion advance is a conservative O(U) effect, so it can exist here, and this is not a wrong-regime null.

| Arm | γ_matter | β | F | η | Q2 |
|---|---|---|---|---|---|
| `scalar` | 0 | 3/2 | 1/6 | 3 | REPRODUCED |
| `ntns` | not fixed | unwritten | none | none | FAILED, by incompletion |
| `adopted-gr` | 1, input | 1, input | 1 | 0 | REPRODUCED, F arithmetic only |

### §4.1 `scalar`

The arm is `tex 03:54`'s index on the Lagrangian at `claim-quality-closure-roadmap.md:205`. Five routes agree: metric PPN (`−g₀₀ = 1 − 2U + 3U² − 4U³`, `g_ij = δ_ij`), 1PN Lagrangian match, exact Binet ray (`dφ = π q μ/ℓ_p`), Delaunay average, and time-domain Hamilton integration (converging on 1/6 at 0.16666521 by r_p = 20000). Controls return GR's 6π on the same instruments. #1028's §9.4 snippet prints 1.000000289 and 0.1666666632. #1029's driver regenerates a byte-identical JSON. Hand check: `ṙ² = E²(1+Mu)² − 1 − L²u²` has no `u³` term, and its `u²` term gives `πM/p`, which is 1/6 of `6πM/p`.

### §4.2 Divergence step: where canon's Item 5 and F = 1/6 part ways

The working is `research/2026-05-17_hulse-taylor-substrate-native-derivation-sketch.md` on `origin/main`. The leaf (`anomalous-perihelion-advance.md:10`, `:20`) and the roadmap (`:205`) carry its conclusion.

1. **`:60` to `:63` drops a factor of 1/2.** `:60` is `L_z²/(2m r²(1 + φ/c²))`. Its expansion is `−L_z²φ/(2m c²r²)` (launching-session sympy; panel too). `:63` prints `−L_z²φ/(m c²r²)`, and likewise on the φ² term. That slip produces `:73`, "coefficient **1** in both". The correct coefficient is k/2: 1/2 at the AVE k = 1, 3/2 at the GR k = 3.
2. **`:76` discards a term of the same order as the result.** It says the 1/r² term "Does NOT introduce precession by itself". A `D/r²` term gives `dφ = −2πD/L²`, here `−πμ/ℓ_p`. With that term kept, the sketch's own V_eff gives 5π, F = 5/6.
3. **The relay.** The leaf's printed V_eff returns 6π only if read as a Newtonian radial potential with the 1/r² term dropped. So 6π needs both steps. Run exactly, the sketch's Lagrangian gives 1/6. The working also marks what it left out: sketch `:80`, on the spatial-metric contribution, says "This is the load-bearing computation that's been deferred for rigor pass." So the leaf's "CLOSED" exceeds its source on that count too.
4. **A further category slip in canon.** The leaf's "substrate-native gives 3 exactly" attaches Item 5's result, coefficient 1 on `L²/r³`, to the "3" in `V_tidal`, a different term. `V_tidal`'s correction is purely 1/r², which `:76` says cannot precess.

**Departure from both PRs.** Neither names this slip. #1028 says "I could not reproduce the numerals $1/2$ and $3/2$"; both numerals reproduce, as k/2. #1029 says "I am not asserting that canon's arithmetic at that step is wrong"; at sketch `:63` it is. Their chart-mismatch diagnosis stays true and is not the whole of it.

### §4.3 `ntns`

The print box is a conditional, not a derivation: F(1,1) = 1 is arithmetic, and nothing shows the pair yields β = γ = 1.

Canon writes a first-order temporal map only (`eq_gravity_derived.tex:65`, `:67`, `:68`), no map from `n_s` to `g_ij`, none to #1029's knobs for matter, and no `b2` bound to this arm. **Addendum, repair pass 2026-11-01:** a sentence here called the box's pointer to `Vol~3 Ch~1--Ch~2` dead in print. It is struck: the grep behind it could not see an `\input`. Ch 1 carries nothing under the box's label `(n_t, n_s)`. Ch 2 prints that pair through `02_general_relativity_and_gravity.tex:279`, at `translation_gravity.tex:18`, the metric row, with a temporal map and no map from `n_s` to `g_ij`, so FAILED stands on the sentence above. §3's Ch 2 clock and index are a different object and carry neither label. `eq_gravity_derived.tex` is `\input` only at `20_white_dwarf_predictions.tex:188`.

Reader completions give F = 0, 3, 6, 19/6, 1/6, 7/6, 5/6, 2/3 and 1, and nothing canon writes selects among them. Using the defined 9/7 value gives γ = 9/2, 8 or 9 by map; reaching γ = 1 needs the unwritten `g_ij = n_s^(2/9)`, or dropping `n_s`. **Scoring any of these would mint a verdict from a map canon never wrote**, so they are characterization only and the Q3 bins are UNTESTABLE.

**Whether Reading 2 coincides with the light arm: no, not as canon writes it.** It matches `a1 = 2` at O(U) only with `n_s` dropped, `n_t` re-slotted and #1029's asserted `b2`. #1029 says so itself: "the leaf does not say it" (`:206`). The arm's sub-case, Reading 3 (motion sees `n_spatial` alone), breaks Newton by 9 on the Gordon form, or gives F = 17/3 with a slope-1 clock. No bin.

### §4.4 `adopted-gr`

`tex 14:71` is honest about this arm: "adopted as a static potential", "not an independent AVE derivation". γ and β are inputs, and no route derives them. F = k/3 exactly in the printed coefficient, and k is taken from GR. **Competing bin, carried from the run.** FAILED was this bin's strongest rival: if Q2's "Re-derive γ_matter, β" binds an arm defined with inputs, the derivation half of this arm is empty. Its verifier rejected FAILED for three reasons. (1) G1a §8 fixed γ and β as inputs before data, so the arm owes no derivation of them and FAILED would penalise it for its own definition. (2) On the print's own Newtonian host the routes agree on F, which is all the print asserts, and that host is silent on γ and β. (3) FAILED would reach the conditional K bin through an input-defined arm; this reason argues from consequences, not from Q2's text. No K or S moves on either bin: `scalar` still supplies K2, and K5 and S5 read neither. The criterion finding is §12 item 8.

**New coverage neither PR has.** `V_tidal` is not the Schwarzschild 1/r³ term. Its correction is 1/r², the ratio to the Schwarzschild term varies around the orbit (2.5 to 3.75 on the test orbit), and F = 1 holds only on a Newtonian host: in relativistic kinematics the same potential gives F = 7/6 or 5/6. So "redundant re-statement" overclaims.

---

## §5. Q3: data, with carriers fixed before data

| Observable | Arm | Predicted | Observed | Distance | Bin |
|---|---|---|---|---|---|
| Mercury | `scalar` | 7.163 ″/cy | 42.98 ± 0.04: a computed GR coefficient with an unsourced σ | −35.82 ″/cy, about 6 times low | EXCLUDED |
| LLR η | `scalar` | 3 | (4.4 ± 4.5)e-4 | 6.67e3 σ | EXCLUDED |
| Mercury | `adopted-gr` | 42.981 ″/cy | 42.98 ± 0.04: as above | +0.016σ | CONSISTENT |
| LLR η | `adopted-gr` | 0 | (4.4 ± 4.5)e-4 | 0.98σ | CONSISTENT |
| Mercury, LLR η | `ntns` | none | | | UNTESTABLE |
| Cassini γ | light, arm-independent | γ_light = 1 | 1 + (2.1 ± 2.3)e-5 | 0.91σ | CONSISTENT |
| Mercury, sourced value | `scalar`; `adopted-gr` | 7.163; 42.981 ″/cy | 43, "known to about 0.1 percent" (Will, gr-qc/0510072, relaying Shapiro 1990) | −833σ; −0.45σ, reading "about 0.1 percent" as a 1σ of 0.043, which is an assumption | EXCLUDED; CONSISTENT. Bins unchanged. |
- EXCLUDED means more than 5 σ_obs, an engineering choice fixed before this stage. No matter-sector γ was compared with Cassini, and no published β was scored.

**Sources.** Will, Living Rev. Relativ. 9:3 (arXiv:gr-qc/0510072), for the sourced row. Will 2014, Living Rev. Relativ. 17:4 (arXiv:1403.7377), eqs. 65-67. Williams, Turyshev & Boggs 2012 (arXiv:1203.2150). Viswanathan et al., INPOP17a (arXiv:1710.09167). Bertotti, Iess & Tortora 2003, Nature 425, 374, via Will. IAU 2015 nominal GM_sun, from memory and matching #1029's value to 10 digits.

**Caveats that travel with these bins.**
- **The ±0.04 has no primary source** in any paper the panel read; #1028 says the same (U3). The bin does not depend on it: exclusion is lost only if σ_obs exceeds 7.16 ″/cy. The "895σ" figure, this table's headline before the repair pass, does depend on it.
- **42.98 is a computed coefficient at F = 1** (Will eq. 65). So "42.98 against 42.98" on `adopted-gr` is largely GR against GR, and the usable datum is the roughly 0.1% residual.
- **η = 3 is a formula read under the frozen rule, not a derived Nordtvedt effect for AVE composites.** The arm supplies a one-source test-body metric, and eq. 66's preferred-frame terms are ones canon cannot compute. `ζ1 = 9/2` would null it algebraically, but that is a target-tuned conservation-law violation canon never computes, and the frozen formula excludes the term. The engine's `test_nordtvedt_eta.py` is a different object, self-graded as install-class.
- **`adopted-gr`'s CONSISTENT bins are evidentially empty.** The gate consumes its own defining identity: on F = 1, η = 7(γ − 1).

---

## §6. SN1987A

**S = S5.** Q4 is not held, so both channels are candidates and neither is a verdict.

**ARITH = HOLDS.** U = 5.38523e-7, photon excess 65.9498 d, matter excess 32.9749 d = 791 h, ratio 264. Re-derived to every quoted digit.

| Channel | Predicted differential | Against ~3 h | Bin |
|---|---|---|---|
| scalar | 32.97 d on #1029's flat U | EXCEEDS in every model tried: 9.15 d (baryon point mass, 73×) up to 368 d (canon's `Φ_galaxy` held uniform, about 2900×). Rebasing the index to Earth flips the sign and still exceeds, at 12 to 34 d. | EXCEEDS |
| light | gravitational term 0; kinematic 1.5e-5 s at canon's `m_ν` | Far below 3 h | WITHIN |

**WITHIN is by identity.** On that candidate `n_ν = n_γ`, so the gate cannot fire on the gravitational term. It is not evidence for the channel or for the repair.

**Held finding, MAJOR, CONCLUSION-WRONG: #1029's "independent of the Galactic mass model" is false.** The sentence is at `:260`, labelled "the one to quote", and repeated at `:265`, `:558`, `:651`, the driver, the JSON and the open item. Only the predicted 0.5 is model-free. The bound is 3 h over a model-dependent delay, so the violation factor scales with `v_c²`: halving `v_c²` turns 2e-3 into 3.8e-3 and halves the factor. The doc's own factor-2 test contradicts its sentence.

Separately, `U = GM(<r)/c²r` is not the potential. Mass outside r contributes to the index, so the driver's 65.9 d is not the delay of any self-consistent flat-curve model. Quoted correctly: the scalar candidate predicts a fractional difference of 0.5, against a bound between about 1e-4 and 5e-3 depending on the mass model. The direction survives. WITHIN would need a path-sourcing mass of about 8.2e8 Msun or less, about 1/70 of the baryons.

**Not a bin.** `03_neutrino_sector.tex:126` prints a neutrino dispersion relation that neither #1029 nor this panel's scoring carries, and the two-candidate scoring may not be exhaustive, since canon calls the neutrino a "twist wave in the Cosserat sector". Both sharpen the neutrino-channel item. Neither creates a bin.

---

## §7. Q5: site census

**`CENSUS: 48 sites` is REFUTED.** Its verifier names **60 sites as a floor: 53 canon + 7 research-tier.** All 48 listed sites hold; the count does not. The bin is not held, and neither K nor S reads it. The launching session read 17 sampled sites at their cited lines at `cbc668e7`: the twelve additions below, and five of the 48.

**Inclusion rule.** The line asserts or load-bears AVE = GR on massive-body motion, or on a set that covers it. Second method: line sweeps of `manuscript/**`, `claims.jsonl` and the root README, by topic token, agreement verb and general-recovery phrase, then read and classified by hand. Blind spot: single-line regex and hand classification. `README.md` and `manuscript/consistency-manifest.yaml`: 0 sites.

Abbreviations: AP = `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/anomalous-perihelion-advance.md`; CQ = `manuscript/ave-kb/vol3/claim-quality.md`; RM = `manuscript/ave-kb/claim-quality-closure-roadmap.md`; T14 = `manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex`; I14 = `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/index.md`; LM = `manuscript/ave-kb/common/physics-lineage-map.md`.

| Site | Class | Source |
|---|---|---|
| AP:10, AP:20, CQ:307, RM:205 | DERIVATION-CLOSED | seed A1, A2, B2, B3 |
| AP:44, CQ:292, T14:81, T14:23, `orbital-regime-table.md:16` | VALUE | seed A3, B1, C2, C3, C4 |
| T14:71 | PPN-PAIR | seed C1 |
| I14:29 | INDEX | seed C5 |
| sketch :93, :99, :173, :186, :204, :215 | RESEARCH | seed D1-D6 |
| `research/2026-07-20_q1-pulsar-hardening.md:84` | RESEARCH consumer | seed E1 |
| `claims.jsonl:248` | REGISTER | X1 |
| CQ:291, CQ:296 | VALUE | X2, X3 |
| CQ:310 | DERIVATION-PRESUMED | X4 |
| AP:41, T14:77 | RESULT | X5, X6 |
| I14:11, I14:17, `vol3/cosmology/index.md:25`, `:40`, `vol3/index.md:47` | INDEX | X7-X11 |
| AP:8, AP:18, RM:207 | HONEST-SCOPED | X12-X14 |
| LM:100, :103, :197, :484 | GENERAL | X15-X18 |
| `stellar-regime-classification.md:22`, `:16`; `07_stellar_interiors.tex:38`, `:29` | GENERAL | X19-X22 |
| `translation-gravity.md:17`, `translation_gravity.tex:19` | GENERAL-IDENTITY | X23, X24 |
| `gravitomagnetism-frame-dragging.md:17`, `03_macroscopic_relativity.tex:184` | FRAME-DRAG | X25, X26 |
| `vol9/ch15-falsification-tests/index.md:37`, `15_falsification_tests.tex:273` | ECHO-COUNTERFACTUAL | X27, X28 |
| `genesis-chord-falsification-ledger.md:105` | CONSUMER | X29 |
| `substrate-native-terminology.md:58` | GENERAL, weak | X30 |
| CQ:289, CQ:293, CQ:295, T14:70, T14:61, AP:26, T14:67, AP:33 | direct, added by verifier | N1-N8 |
| `gr-ave-translation-dictionary.md:13`, `02_general_relativity_and_gravity.tex:277`, `:285` | general, added by verifier | N9-N11 |
| `03_macroscopic_relativity.tex:200` | frame-drag, added by verifier | N12 |

**Reading the table.** The seed verifies verbatim at every line and understates: it has 11 canon surfaces against at least 53. Its parenthetical "the full set is below" contradicts its own METHOD paragraph; the METHOD paragraph is the accurate one. Contra-site, not counted: `manuscript/frontmatter/00_foreword.tex:111`, "not yet substrate-derived". Removing the three weakest counted sites (X27, X28, X30) still gives 57, so the count does not return to 48. Further arguable sites remain uncounted, which is why 60 is a floor. The hit counts 384 / 195 / 234 are not reproducible, as the patterns were not published; they are not load-bearing.

---

## §8. Q6: repair-round integrity

**Receipts: mostly true at both tips.** The R55 quotes, blame on `eq_axiom_5.tex`, counts, table integrity, driver re-run and `make verify` all hold. Self-repair commits are dated 2026-09-06 local; none carries a 09-07 local date.

**Defects, held at MINOR.**
- **(a) One blanket receipt is false.** `00d0b230` claims "every Mercury / Hulse-Taylor / solar-limb / SN1987A / zone-edge number against the results JSON". The `2.5×10⁷` zone-edge count at #1029 `:436` is not in the JSON and is high by π (8.10e6). The check compares a document with the lane's own JSON, so it cannot catch a mistranscribed external value.
- **(b) Hulse-Taylor datum disagrees across the PRs,** 4.226595(5) against 4.226585(4). Against primaries: #1029's value is a correct transcription of Weisberg & Huang 2016; #1028's matches neither table read. #1029's 3.15σ is an epoch mix, 2010 inputs against the 2016 datum, and not a physics miss. **Sharper:** its repair/GR column is a calibration identity. `M_tot` is the GR inversion of the measured ω̇, so `4.2265976` returns that datum by construction, yet `:22` reads it as a repair result.
- **(c)** `2f19d551` wrote a pointer to `:134` in the commit that moved the row to `:136`.
- **(d)** #1029 `c4ddb753` names tokens neither pass catches ("canon does not carry", "the corpus lacks", "untreated") and ships them in the umklapp item title, `:56`, `:424` and `:436`. The blind spot is disclosed as open, so this is a known residual, not a false certificate.
- **(e)** Cosmetic, `a57920e4`: S departs from 1 continuously, not at unity.

---

## §9. Q7: routed-item numerics

**Finding held at MAJOR, EVIDENCE-VOID.** Only the three Umklapp thresholds reproduce from the tree (1.605351 MeV, 1.173718 MeV, 1.373348 keV). The boost-channel numerics have no driver: #1029 says "I did not re-run L2's or L3's numerics". Re-derived independently: one-way amplitude 2.03e-15, `(kℓ)⁴` = 2.16e-22, A = 1.22955, 10.32%, the two-cone solve, `0.35β²` = 5.33e-7.

**Four narrated items do not reproduce.**
1. **Two-way form.** "`5cos²θ − 1`" holds only with antipodes taken in the preferred frame, which drops aberration. A lab cavity arm is antipodal in the lab, giving `1 + 3cos²θ`. Peak-to-peak is 3.76e-18, not 6.3e-18, and 4.24 orders over `(kℓ)⁴`, not 4.5. The kinematic point survives.
2. **"four orders above the bound".** `5.33e-7 / 1.6e-9` = 333, or 2.52 orders. No reading gives four.
3. **"2.5e7 zone edges".** That is kℓ in radians. In the item's own unit, `q/(π/ℓ)`, it is 8.10e6.
4. **"The thresholds are exact".** True of the momentum. Canon's lattice-mode law puts the edge at 1.022 MeV on the branch the consequence concerns, and canon carries more than one edge figure.

**Wrong-carrier exposure.** The item's "The only thing making it vanish is `ρ_bond = 1`" omits canon's other reading, "free photon is the continuum EM field". Canon has two readings the item does not disclose, so "only" is unsupported. Also, the quote "protected two independent ways" is not at its cited lines, which read "doubly protected".

---

## §10. Framing findings

All five held. Findings 2 to 5 CONFIRMED at MAJOR; finding 1 DOWNGRADED from CRITICAL to MAJOR.

1. **"The ratio is right" (#1029 `:202`, `:525`) is a statement about the imported ν value.** `(1−2ν)/(3ν)` equals 1/2 only at ν = 2/7, and the displayed proof is 7 × 1/7. The title's claim that the fix is graded above CONSISTENCY-CLASS did not hold: the PRs keep that grade. "Was always the clock grading" also contradicts #1029 `:20`, and canon spends the 1/7 as a ray index, a 2:1 consumer the repair does not preserve.
2. **Verdict wording is unconditional, and K1 is unreachable.** #1028's title, F10 and the walkback item's "wrong under **both** readings" drop the assignment caveat that #1028 `:62`, `:131` and `:667` carry. "Both readings" omits `ntns`, `adopted-gr` and every regime reading. Its second leg fails for C3, C4 and C5, which claim no derivation. C1 "contradicts" is unearned: #1028 never builds a metric from `(n_t, n_s)`. Neither result doc mentions `II (Yield)` by that name, `g_N`, `a_0`, `A_gm` or `τ_yield`. For A1, A2, B3, D and E1, F = 1/6 does land on their own carrier.
3. **Headline table scores the matter sector on prohibited carriers** (#1028 `:39`, `:40`, `:548`). ~4.3e4σ is Cassini's sigma applied to a slow-body parameter, and ~4.5e3σ scores a published β. η is never computed. On η both of #1028's arms sit near 6.8e3σ, so the 4.5e3 / 9.1e3 asymmetry is an artifact. "Two gammas" mixes two readers of γ. These figures should not be quoted.
4. **"Independent of the Galactic mass model" is false, and "by canon's own rule" overstates a Q4 that is not held.** See §6. The second limb is weaker: `:264` does call the point open.
5. **Agreement of the two routes is not independent confirmation.** #1029's route gets `(1,1,1)` by projecting onto the Gordon mass shell, and `c_eff² = A/B`, `Ω² = A M²` make the two routes one identity for any (A, B). #1028 `:67`'s "sharing no assumptions" and #1029's "no metric anywhere" overstate, and `:62` and `:67` contradict each other on exactly the axis G1a holds as AMBIGUOUS. `OUT["gordon_forces_a1_eq_b1"] = True` is a literal that cannot fail. F = 1/6 stands as a conditional; what is void is the claim of independent confirmation.

**R61's "The kill stands against canon as written"** is printed in the indicative at decision line 2. This record reads it as depending on the sentence before it, "The audit decides what canon as written fixes.", and on R61 §2, "A gravity walk-back, if the audit supports one, is a separate later ruling." The bins do not give K1, so this record does not use that wording. The reading is this record's own and is flagged for the orchestrator.

---

## §11. Standing constraints applied

**Symmetric standard.** GR gets β = γ = 1 from a field equation solved for `g₀₀` and `g_ij`. Here `γ = 0` is read off an imported form under an asserted assignment, and canon lists the spatial sector as open work (`claim-quality-closure-roadmap.md:205`). Neither F = 1 nor F = 1/6 meets GR's bar. The fair wording for the scalar arm is "follows from canon's Lagrangian as written", not "genuine forward derivation". The bar is still the one canon's own claim invites, and the same instruments return GR's value as the control.

**Both-ways seduction: readings of the negative, tested with the same force.**
- **Wrong regime.** No regime reading supplies a planetary index (§3). On `g_N/a_0` canon writes only a drag consequence: zero at r ≫ 1 (`domain-catalog.md:132`), applied at the solar system through the ruled total-local-field keying (`oort-cloud-saturation-boundary.md:38`, `:40`). Whether that Regime IV label carries rupture or an index effect at Mercury is not written.
- **Wrong carrier.** The J2 needed is 2.8e-4 against (2.2 ± 0.1)e-7. No matter-sector γ met Cassini. `n_spatial` as the neutrino index flips the SN sign and still exceeds.
- **Wrong coordinate.** `g_ij = δ_ij` is already isotropic and the apsidal angle is invariant. Normalization does bite elsewhere: #1029 `:171`'s F = 1/3 for `a1 = b1 = 2` is not Kepler-normalised. Kepler-normalised it is 1/6.
- **What remains live.** The negative stands on the assignment M4, that matter moves on the Gordon metric. No route tests M4. Regime I also does not mean no kernel at β order: `δS/U² = 49/2` at every radius, so "no saturation kernel enters" (#1028) and "`S → 1`" (#1029) are order-of-magnitude statements applied to an order-in-U quantity. This qualifies "β = 3/2 exactly" and does not rescue the arm. Tex 20 and `clm-at7x0y` (solidity 0.52, input only) print that kernel on a clock as a static surface redshift (`20_white_dwarf_predictions.tex:96`, `:103`, `:113`, `:117`). Canon also prints a static local √S clock: Op14 at `op14-local-clock-modulation.md:19` and `:24`, and `temporal-spatial-lattice-decomposition.md:24`, though there √S ≈ 1 − GM/(c²r) is first order in U, so that S may name the clock itself and not the saturation kernel. None of these writes whether the kernel sits on a bound orbiting body's clock, and no arm as frozen carries it. Conditional on placing it on an orbiting body's clock at unit weight, the β shift depends on the form: −49/2 for rate `√A · S` (`:103`), +49/2 for the kernel factor of `:96` read as a rate, −49/4 for a `√S` clock (the engine form, x44 AUDIT `:26`). On `scalar` those give β = −23, 26, −43/4 and F = 25/3, −8, 17/4, each EXCLUDED. This record does not decide whether S(ε11) sits on a bound orbiting body's clock, or in which form.

**Classification of every agreement.** No agreement here is AVE-distinct, and SM/GR predicts each one with the same inputs. In the skill's classes:

| Agreement | Class |
|---|---|
| `adopted-gr` F = 1 | C, calibrated: k imported |
| `adopted-gr` γ, β, η | A, identity: inputs restated |
| Cassini γ_light = 1 | C, calibrated: `Q = ν·(2/ν)` is ν-blind |
| SN-PRED[light] WITHIN | A on the gravitational term |
| The (2, 1, ½) repair | C: `a1` from the GR-imported chain, `b1` from Newton, `b2` asserted |

**The a1 = 2 repair stays CONSISTENCY-CLASS**, because Q1 is not FIXED-LIGHT. **This audit recommends no arm.**

**The regime framing.** R51 §6 says peer-with-GR inside a regime is the expected result. That is what `adopted-gr` delivers, and it is why an honest print box is not the defect. The defect is the set of surfaces that claim more than the box does.

---

## §12. Findings on the frozen criteria (recorded, not re-posed)

1. **The rederive template overflows the workflow's cap.** Three bins plus one REGIME bin per ruler exceeds 5 findings per lens, and the workflow slices the excess silently. The launching session split the REGIME bins across the three lenses in the arm `{{FILL}}` and left the template text unchanged. Each ruler has one verified bin, and all rulers are in the `clean_reports`.
2. **Q2's "the two routes disagree" clause cannot fire on a shared (A, B)** (§10.5). FAILED on `ntns` is by incompletion. The two-route requirement checks arithmetic, not the assignment.
3. **UNTESTABLE has no definition.** It was read as "the arm has no value to score", the only reading compatible with "An arm's values means its REPRODUCED or CORRECTED values".
4. **K3's "need" is undefined when one arm suffices.** See the decision in §3.
5. **Q4 has no AMBIGUOUS bin** (G1a §6). REFUTED is not held either way.
6. **`REGIME[Mercury, τ/τ_yield]` is not a regime label.** It is the honest report of a ruler canon never defined. Scoped: "sub-yield on every proxy" holds for a stress in Pa against 1.04e22 Pa. If τ/τ_yield is identified with `g_N/a_0`, which canon never writes, the printed past-yield is reproduced at 3.69e8 and Reading E collapses into Reading D. That leaves 1.04e22 Pa unable to be the threshold of that transition.
7. **Δφ/α is not a fifth Q0 ruler.** It characterizes G1a FLAG 1.
8. **Q2's "Re-derive γ_matter, β" is ill-posed for an arm defined with inputs.** Q2 covers "each arm under test" with no carve-out, and G1a §8's note, "γ and β are inputs", narrowed it for `adopted-gr`. On `ntns`, FAILED tests a derivation the print box claims ("derivable directly"). The same box calls `V_tidal` "not an independent AVE derivation", so `adopted-gr` has no such claim to fail. The bin stays as verified, scoped to F arithmetic, unless the orchestrator's review decides otherwise. The competing FAILED is in §4.4.
9. **Q3's "primary observational values, with sources" was not met for Mercury.** No carrier-clean primary value with a stated σ was obtained. 42.98 is a computed coefficient, its ±0.04 is unsourced, the sourced 43 is a review relaying a rough figure, and the tighter fits the panel saw (Will 2014; Park et al. 2017, by search listing only) fold in Cassini's γ, which the frozen carriers keep out. The bin does not need the σ: `scalar` stays EXCLUDED unless σ_obs exceeds about 7.16 ″/cy.
---
## §13. Addenda to the G1a record

G1a's frozen text is at `9c131d02`. Its corrections are recorded here. The file has one later edit, the marked post-freeze cite on its Reading D row (`:38`).

1. **§2, Reading D.** "Canon does not print "Regime IV" for planets" needs "on this ruler". `flyby-anomaly-sagnac-operator.md:34` prints "Earth-as-rotor is in Regime IV, not Regime I.", on a different unnamed mass-saturation ruler, scoped to the vacuum within R_earth. This adds to CONFLICTING.
2. **§8, arm `scalar`.** The arm also needs the Lagrangian at `claim-quality-closure-roadmap.md:205`: F = 1/6 depends on `b2 = 1` from it, and `a1 = 1` alone does not fix F.
3. **§2, rendering.** Quotes containing pipes break that table when rendered. Read the raw file.

---

## §14. Duplicates to collapse (recorded, not fixed)

- #1028 `eps11-four-objects` consequence 3 and #1029 `bias-to-index-photoelastic-map` result 3 are one finding. They do not cross-link, and they carry different status.
- #1028's L/C-grading question and #1029's a1 question are one fork, routed twice and not cross-linked.
- #1029's "two knobs" (`c_eff` against Ω) are not the #1020 signed "two knobs" (kernel A against Op19 n). #1029 never cites #1020, so the homonym is undisambiguated.

---

## §15. STUCK-POINT (K5)

**1. Blocker.** `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md:16`, print twin `14_macroscopic_orbital_mechanics.tex:23`: "II (Yield)", no ruler named, no Mercury control value. Against it: `domain-catalog.md:47`, `:50` and `stellar-regime-classification.md:22` (Regime I on ε11), `orbital-lc-friction-paradox.md:14` (Regime I on A_gm), and `domain-catalog.md:128`, `:132` (`g_N/a_0`, computed 3.69e8, Regime IV).

**2. What was tried.** One G1a run, in which a verifier's three attempts to reconcile the row failed. One G1b run, which computed every ruler. Nothing in canon says which ruler the row reads.

**3. The one physical question.** When the Mercury row says "II (Yield)", what meter was it reading: how hard the lattice is strained at the orbit, or only that this effect takes GR-level physics to describe?

**4. Candidate readings.**
- **A, ε11 strain:** the row is wrong; Mercury sits about six orders below the first knee.
- **B, domain tag:** the row means "needs GR-level physics", and it is not an amplitude statement.
- **C, `g_N/a_0`:** Mercury is past onset. Canon writes only a drag consequence on this ruler, and does not write whether that label carries rupture or an index effect at Mercury.
- **D, a ruler canon has not written:** the row needs one before it can be read.

Every candidate leaves the conditional bin at K2 unless it comes with a first-order index canon does not now write.

**Open with it, S5.** The Q4 fork is unresolved: canon's class rule ("A fast-moving massive particle", `02_general_relativity_and_gravity.tex:179`) reaches a neutrino written as massive (`03_neutrino_sector.tex:15`), while canon's geometry ("a propagating open helix") does not fit "isotropic 3D volumetric wave packet".

---

## §16. a1 = 2 banking note

Decision line 2 says a1 = 2 "banks as a new hypothesis with its own prereg", and R61 §3 lists a proposed wave-2 slot for it, an orchestrator proposal and not a ruling.

**Proposal.** A lane-owned item for that hypothesis, KEEP-BOTH with its own prereg, cross-linking #1029's `2026-08-27-two-knob-constitutive-forcing.md`. The item is not created here.

**Flag.** That existing item is `status: ROUTED-TO-GRANT`, `owner: grant`, and its question 2 asks "Does a bound matter packet ride light's own `c_eff(r)`?". R61 says the a1 fork "is not put to Grant as a post-audit pick". The item's status therefore conflicts with decision line 2. The item predates R61.
