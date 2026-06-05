# Experimental Round-2 Hardening — Capstone Synthesis (2026-06-04)

> **What this is.** The readable, external-review-grade narrative of the round-2 experimental-protocol hardening arc. The *detail* lives in the adjudication ledger ([`_orchestration/experimental/2026-06-04_round2-adjudications.md`](../_orchestration/experimental/2026-06-04_round2-adjudications.md)), the epic spine ([`_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md`](../_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md)), and the `closure-roadmap §0.5` changelog. This is the *story*.

## The question

It started with one: **"What's the status of our experimental protocols — the top ones by rigor, math, claims, and ability to falsify?"** Answering it honestly meant not just ranking the board but *re-attacking* it.

## The arc

**survey → ranked board → round-1 hardening (4 protocols) → round-2 hardening (4 protocols) → 7 adjudications → auditor-gate → 7 merges → corrections.**

Round-1 (2026-06-03) deflated the headlines once. Round-2 (2026-06-04) re-aimed the *same* adversarial discipline at the survivors — *"is the surviving discriminator form-shared with classical theory, or anchored on a conflation?"* — and where it found a conflation, it removed it and asked whether the test survives without it.

## What round-2 found, per protocol

| Protocol | Verdict | What survives |
|---|---|---|
| **Cleave-01** | **SURVIVES + upgraded** | Round-1's "SM predicts exactly 0.0" was *false* (contact-potential-difference mimics the floor on magnitude + polarity). Cured by the **gap-independence corner** → a 4-corner symmetry discriminator {linear ∧ polarity-odd ∧ material-indep ∧ gap-indep} no single classical mechanism fakes. The flagship GO ($7.7k). |
| **Birefringence-E4** | **SURVIVES, reframed** | The corpus had it *backwards*: a √ε conflation labeled the permittivity depth (1−S) as the index shift (√S−1 = −A²/4), and shipped a **false-falsifier** ("E² slope falsifies AVE") in the datasheet. Both are E²-leading — the real discriminator is the **coefficient** (AVE δn ~10⁶× QED at facility laser fields). The corpus had *undersold* it. |
| **Q-G42 (V²-sign)** | forward discriminator | The +sign (vacuum softens) is robust to the √α uncertainty; feasibility gated on the per-node reachability fork + Fowler-Nordheim destruction. |
| **HOPF** | C3/C4 retire | Medium-independence + enantiomer-sign are textbook reciprocal-Pasteur (classical). Surviving leg: a cheap 2-port S₂₁-vs-S₁₂ **reciprocity** sweep (the one classically-forbidden residue). |
| **IVIM** | structure survives, magnitude undetectable | V⁴ discrimination sound; re-scoped to interferometric (7.6 yr to SNR=1; the apparatus field-emits first). |
| **Sagnac** | RETIRE | Corroborative-null (RLG-excluded 7e4×) + a real Ch.6 eq.80 10⁶ arithmetic fix. |

## The throughline (confirmed end-to-end)

**The tests that survive are SYMMETRY, SIGN, or zero-free-parameter discriminators; the ones anchored on a MAGNITUDE or the per-node conflation deflate.**

- Survive: Cleave (4-corner symmetry), Q-G42 (V²-sign), birefringence-E4 (coefficient ratio).
- Deflate: HOPF cheap legs (form-shared), IVIM/Sagnac (magnitude/already-excluded), PONDER-05 (conflation).

This is the same throughline as the opening status answer — and it held across all seven adjudications, which is the strongest evidence it's real and not a framing artifact. It also ties back to the α-close: since α⁻¹ = 4π³+π²+π is a *named geometric identification* (not derived), any test whose discriminator IS α or rides a √α magnitude is only as firm as that identification — so the falsifiers that survive the α being undecided are exactly the sign/symmetry/zero-free-parameter ones.

## The deepest finding: the per-node conflation

`V_yield ≈ 43.65 kV` is a **per-node** voltage — the yield across *one* lattice cell (ℓ_node = 0.386 pm), i.e. the yield *field* E_yield ≈ 1.13×10¹⁷ V/m. It numerically *looks* benchtop-reachable, which seduced a corpus-wide reading error: treating an apparatus voltage as if it were the per-node ratio (off by d_gap/ℓ_node ≈ 2.6×10⁸). The signature: **PONDER-05's "27.4% ε-collapse at V_DC/V_yield = 0.687, 30 kV"** — reaching 0.687 would require the 30 kV to drop across **1.0 node-lengths**. It can't; across real quartz the per-node A is 10⁻⁷–10⁻¹⁰, so the 27.4% is the **quartz's own voltage-coefficient** (a Class-II ceramic varactor), *not* the vacuum kernel. PONDER-05 was reclassified **material/consistency-class** across INVARIANT-S2, ≥11 KB leaves, and the EE-mapping skill — and its cascade was followed: a *closed* Class-2 emergence result (the NA-aperture κ₃/κ₄) lost its empirical anchor (the "0.707 within 3% of 0.687" was a spurious coincidence) while its **derivation survived** (Op17 matched-impedance, PONDER-05-independent).

## The shipped false-falsifier

The vol_9 datasheet falsification table shipped *"AVE: Δn ∝ E⁴; E² slope falsifies AVE."* That's wrong: AVE's vacuum index shift is **E²-leading** (δn = −A²/4 − …), same order as QED — so measuring E² scaling is exactly what AVE predicts, and that "falsifier" would have wrongly killed the framework. Killed and replaced with the correct coefficient discriminator. A framework that ships its own falsification criteria has to get them right; this one was caught and fixed.

## The auditor-gate earned its keep

Two read-only `ave-auditor` passes, split by risk, ran before *any* correction touched the corpus. They caught **three orchestrator scope-errors** (an over-reached SM≠0.0 target; a mis-attributed provenance; a 5-sites-not-2 blast radius) **and** independently verified the shipped false-falsifier — before a single leaf was edited. The deflation was never taken on trust; it was verified.

## Where the program stands

- **Cleave** is the clean near-term GO ($7.7k, weeks) — the one protocol that got *stronger* under attack.
- **Q-G42** is the best forward test (V²-sign), pending the reachability-fork resolution.
- **Birefringence-E4** is a genuine — and underappreciated — **facility-class** discriminator (high-intensity laser, ~10⁶× QED).
- **HOPF** has one cheap surviving probe (the 2-port reciprocity sweep) on existing hardware.
- The rest deflated honestly: IVIM/Sagnac/Casimir off the near-term track; the magnitude tests are facility-class or already-excluded.

The honest summary: the experimental program is **smaller and sharper** than it looked. The "cheap tabletop falsifier" framing took real damage; what's left is a few clean symmetry/sign tests and a set of facility-class coefficient tests — which is a more truthful, more falsifiable surface than the pile we started with.

## Documentation trail

- **Spine** (state): the epic doc §1–§12 + Execution phase.
- **Ledger** (reasoning): the 7 adjudications, each EE-mapped + skill-disciplined, with decisions.
- **Corpus deltas**: the re-scoped leaves + INVARIANT-S2 + the corrected datasheet + the EE-skill.
- **Audit trail**: 11 `audit/2026-06-04_*` tags; all branches merged + deleted.
- **Capstone**: this doc.

## Remaining follow-on

- A dedicated `.tex` echo sweep — 13 vol_9/backmatter/vol_3 rendered-volume files still carry the per-node-conflation framing (the canonical KB `.md` is corrected; the `14_phase_diagrams.tex` self-contradiction is fixed).
- The facility-class tests (birefringence-E4, Q-G42, IVIM-interferometric) await a partner facility; the near-term bench track is Cleave + the HOPF reciprocity sweep.
