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

The same message said of #1076 (verbatim): "Its title still says DO-NOT-MERGE until you say otherwise". It also recommended that #1076 land first. That recommendation lapsed the same evening: #1069 merged at 2026-11-07T03:58Z, which put #1076's regeneration behind main.

**Why this entry exists:** a ruling relayed through the orchestrator session gets a docket receipt (the R59 precedent, generalised in R60). The PRs named below cite this entry as the authority for the edits it allows.

## §1 — THE RULING (R63)

1. **#1074, third VN-F4 leaf.** The VN-F4 cite fix `cvr_model.py:161` → `:170` extends to a third KB leaf, `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:207`. This widens R61 §2's "in two KB leaves" for this one cite. The edit is one token.
2. **#1079, RETARGETED.** The inbound-cite checker keeps RETARGETED in its narrow form only: a re-pin past the base end counts as retargeted only onto text the diff added. A re-pin onto content that was deleted, or that only looks alike, is not retargeted. The past-end boundary counts lines without the trailing-newline phantom.
3. **#1078, contested votes.** A 2–1 vote toward fence-excluded is contested. Contested records stay `unsure — not picked`, as the pass's body already states. The 33 records decided that way move to unsure, and the unsure list Grant receives grows from 132 sites to 156.
4. **#1039, R3 wording.** "Printed-precision agreement" is rejected as the R3 replacement wording, since the printed digits differ at the fifth decimal (about 60 ppm). The ppm strikes stand, and no number or precision claim is substituted.
5. **Merging.** The Orchestrator may merge a PR once it is CLEARED for merge. No PR merges on the strength of this entry alone.

## §2 — What R63 does NOT rule

- **#1038:** whether "the flip is in scope, propagate it to :198 and :217" are Grant's words, and which K=2G record stands, board `:46-55` or the PR's AWAITING GRANT section. The recommendation above says so, and Grant's answer does not reach it.
- **The preservation fence:** whether the 2026-08-03 ppm strike reaches lines inside Rule-12 preserved spans (nine R3 lines on #1039), whether the leaf-head banner at `form-deriving-value-importing.md:11` fences `:63` (#1073), and whether R43 dated notes stand like R40 notes. Item 4 does not decide the nine lines inside preserved spans.
- **#1078's other questions:** `00_foreword.tex:112` against `vol_1/04:103`, the F-C7 clause order, the reach of F-C5, A1 cage self-formation as a K3 route, the three-reader read, `17_engine_requirements.tex:157`, and whether §0 reaches `:153`.
- **#1072's physics flags:** whether S(ε11) sits on a bound orbiting body's clock, `r_s` against `r_h`, row 7's phase-state, and the reading of "The kill stands". The K5 stuck-point stays open.
- **#1037, #1071 and #1054:** whether `vol_5/06` is Class A, whether the true Class A set is re-derived, and `manuscript/ave-kb/README.md:24`.
- No claim, grade, band or physics number moves on the strength of this entry.
