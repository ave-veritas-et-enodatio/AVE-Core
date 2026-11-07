# R63 — Review-pass recommendations on #1039, #1074, #1078 and #1079 accepted; cleared PRs may merge (2026-11-06)

### ENTRY 2026-11-06-ruling-r63-review-pass-recs

*(Number provisional: R63 is the next free ruling number. R61 is the last on `origin/main` `f88f49e9`, and open PR #1075 carries R62 in `2026-10-29-ruling-gridfix-option-a.md`. No docket fragment on main or on any open-PR branch carries R63. The Orchestrator confirms the number at merge.)*

**Grant, verbatim (the ruling, 2026-11-06, in the orchestrator session, answering the recommendations below). This fragment is its docket record. No primary artifact by Grant exists in the repo at the time of writing; a comment by Grant on the PR that lands this file, quoting the ruling, would make this record self-verifying:**
- *"I agree with your recs, let's implement/merge away"*

**The recommendations he answered, verbatim as presented on 2026-11-06.** They were presented in the orchestrator session, which is not a durable home, so the text exists in the repo only as quoted here:

> **The rulings that would clear the most PRs**, with my recommendation:
> - **#1074:** allow the one-token fix to `device-circuit-models.md:207` (the third leaf). Yes.
> - **#1079:** keep only the narrow form of RETARGETED, noting that the past-end boundary moved one line. Yes.
> - **#1078:** two judges should not be able to outvote the checker toward fence-excluded. Sending the 33 back to unsure makes your list 156 sites.
> - **#1039:** reject "printed-precision agreement"; the digits differ by about 60 ppm.
> - **#1038:** whether "the flip is in scope, propagate it to :198 and :217" are your words, and which K=2G record stands. These two need your memory and your call; I can't recommend either way.

The message ended with one more sentence, not quoted here, pointing to the session's earlier recommendations and to a review ledger held outside the repo. Those earlier recommendations covered the same four PRs (#1039, #1074, #1078, #1079). This receipt reads R63 as the five bullets above. A comment from Grant can widen that reading.

The same message said of #1076 (verbatim): "Its title still says DO-NOT-MERGE until you say otherwise". It also recommended that #1076 land first. That recommendation lapsed the same evening: #1069 merged at 2026-11-07T03:58Z, which put #1076's regeneration behind main.

**Why this entry exists:** a ruling relayed through the orchestrator session gets a docket receipt (the R59 precedent, generalised in R60). The PRs named below cite this entry as the authority for the edits it allows.

## §1 — THE RULING (R63)

1. **#1074, third VN-F4 leaf.** The VN-F4 cite fix `cvr_model.py:161` → `:170` extends to a third KB leaf, `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:207`. This widens R61 §2's "in two KB leaves" for this one cite. The edit is one token.
2. **#1079, RETARGETED.** The inbound-cite checker keeps RETARGETED in its narrow form only. A re-pin past the base end counts as retargeted only when it lands on text the diff added, and the content the cite held at base is seen and has not moved. A re-pin away from a base line whose content is gone, or onto a line that matches content the diff removed elsewhere, is not retargeted and stays reported. The past-end boundary counts lines without the trailing-newline phantom.
3. **#1078, contested votes.** A 2–1 vote toward fence-excluded is contested, and a contested record stays `unsure — not picked`. The records decided that way move to unsure. The quoted recommendation's 33 records and 156 sites were measured at the reviewed head `194f815a`, and repairs since then have moved records. R63 fixes the rule, not the counts: the pass reports the counts it measures after the move.
4. **#1039, R3 wording.** "Printed-precision agreement" is rejected as the R3 replacement wording on #1039, since the printed digits differ at the fifth decimal (about 60 ppm). The ppm strikes stand, and no number or precision claim is substituted.
5. **Merging.** The Orchestrator may merge a PR once it is CLEARED for merge. No PR merges on the strength of this entry alone.

## §2 — What R63 does NOT rule

- **#1038:** whether "the flip is in scope, propagate it to :198 and :217" are Grant's words, and which K=2G record stands, `_orchestration/2026-08-02_manuscript-reconciliation-board.md:46-55` or the PR's AWAITING GRANT section. The recommendation above says so, and Grant's answer does not reach it. Also not ruled: extending the card's edit to `vol3/claim-quality.md:202`, the vocabulary edits that wait on W5, and who retargets the gating row in `gamma_census_adjacency_number_check.py`.
- **The reach of item 4:** whether the same call reaches leaf `q-g19a:14` or `06_electroweak_and_higgs.tex:536-537`, `:702-703`. Item 4 rules on #1039's R3 lines only.
- **The preservation fence:** whether the 2026-08-03 ppm strike reaches lines inside Rule-12 preserved spans (nine R3 lines on #1039), whether the leaf-head banner at `form-deriving-value-importing.md:11` fences `:63` (#1073), and whether R43 dated notes stand like R40 notes. Item 4 does not decide the nine lines inside preserved spans.
- **#1039:** whether to wire the generator instead of retiring the "Dynamic Output" label.
- **#1073:** whether the R48 correction applies at `form-deriving-value-importing.md:63`, and whether the four-axioms sites gain "+ the source law".
- **#1078's other questions:** `00_foreword.tex:112` against `vol_1/04:103`, the F-C7 clause order, the reach of F-C5, A1 cage self-formation as a K3 route, the three-reader read, `17_engine_requirements.tex:157`, whether §0 reaches `:153`, whether a bulk-channel Γ=−1 wall counts as the F-C7 and F-C8 corpse, and the pass's own three questions.
- **#1072's physics flags:** whether S(ε11) sits on a bound orbiting body's clock, `r_s` against `r_h`, row 7's phase-state, the reading of "The kill stands", and the optional cross-scale table. The K5 stuck-point stays open.
- **#1037:** whether `vol_5/06` is Class A, and whether `translation-circuit.md:784` and `:459` are rewritten.
- **#1071:** whether the true Class A set is re-derived, whether the digit edit widens to the four `7.21e-3` sites, and whether `02_organic_circuitry.tex:734` follows the category flip.
- **#1054:** `manuscript/ave-kb/README.md:24`.
- No claim, grade, band or physics number moves on the strength of this entry.
