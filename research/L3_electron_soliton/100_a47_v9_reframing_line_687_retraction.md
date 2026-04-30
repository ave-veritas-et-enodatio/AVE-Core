# L3 Doc 100 — A47 v9 Reframing + Line-687 Retraction (Methodology Artifact)

**Status:** Retraction artifact + methodology lesson. Per Rule 12 (retraction-preserves-body), this doc carries the corrective findings; the originating handoff body is preserved in place with footnote markers pointing here.

**Date:** 2026-04-30
**Lane:** Implementer-drafted, Grant-adjudicated, auditor-concurred.
**Originating artifact:** [`.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md`](../../.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md) (gitignored per Rule 15 lane discipline; .gitignore:71)
**Pattern precedent:** [doc 81 §2.2 line 36](81_l3_followup_questions.md#L36) — Op20+Op22 synthesis-as-corpus correction footnote (commit `35cc818`).

---

## §1 — What was claimed (verbatim from originating handoff)

The handoff at `.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md` (commit `f120ad0`) made four cross-referenced claims about an unimplemented refinement marker in [`src/ave/solvers/radial_eigenvalue.py`](../../src/ave/solvers/radial_eigenvalue.py):

- **§0 line 30 (TL;DR top forward action):** *"Investigate `radial_eigenvalue.py:687` 'not yet implemented' refinement for A47 v9 Li discrepancy resolution (~30 min trace)"*
- **§2.2 line 131 (engine code table):** *"**'not yet implemented' at 687 — A47 v9 root-cause candidate**"*
- **§4.2 line 246 (A47 catalog v9 entry — load-bearing site):** *"root-cause is 'not yet implemented' refinement at radial_eigenvalue.py:687 per Op2 crossing or MCL refinement"*
- **§5.1 line 272 (first immediate action):** *"Investigate `radial_eigenvalue.py:687` 'not yet implemented' comment — what specific refinement (Op2 crossing? MCL?) is missing?"*

The fabrication was load-bearing: §0 listed it as the #1 priority forward action; §5.1 listed it as the first immediate action with `~20 min trace` cost estimate.

---

## §2 — Direct verification (Rule 9 v2: right kind of question?)

**Empirical check 1 — file content at line 687.** Read [`src/ave/solvers/radial_eigenvalue.py`](../../src/ave/solvers/radial_eigenvalue.py) lines 680-695:

```
686    return sol.t, sol.y[0], sol.y[1]
687    [BLANK]
688    [BLANK]
689    # ---------------------------------------------------------------------------
690    # Step 4: ABCD transfer matrix per section (Eq. abcd_section)
691    # ---------------------------------------------------------------------------
```

Line 687 is blank. It is the boundary between `_radial_ode_integrate` and `_abcd_section`.

**Empirical check 2 — full-file grep.** `grep -ni "not.*implement\|TODO\|FIXME\|placeholder\|future work" src/ave/solvers/radial_eigenvalue.py` returns **zero matches across all 1914 lines**.

There is no "not yet implemented" comment anywhere in the file. The four references in the handoff are pinned to a fabricated artifact.

---

## §3 — Empirical re-derivation of A47 v9

Per auditor direction (Rule 9 v2: walk the symptom, not the marker), running the actual computation:

```python
>>> from ave.solvers.radial_eigenvalue import ionization_energy_e2k
>>> ionization_energy_e2k(3)
5.687332  # eV
```

Reference values:

| Source | Li IE (eV) | Error vs CODATA |
|---|:---:|:---:|
| CODATA | 5.392 | — |
| Manuscript table ([ionization-energy-validation.md:18](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md#L18)) | 5.525 | +2.46% |
| Current code (`ionization_energy_e2k(3)` this turn) | 5.687 | **+5.48%** |

**Code-vs-manuscript gap: +2.94%.**

Test harness at [`src/tests/test_radial_eigenvalue.py:35-47`](../../src/tests/test_radial_eigenvalue.py#L35-L47) covers H, He, C, Ge — Li is **omitted from coverage**. The omission is consistent with the code output not reproducing the manuscript value at the test-harness 5% tolerance.

---

## §4 — Reframing of A47 v9

**Original handoff framing (binary):** *"is the refinement implemented?"* — anchored to a non-existent marker.

**Corrected framing (provenance):** *"the manuscript table at ionization-energy-validation.md:18 reports 5.525 eV at +2.46%; the current solver at HEAD outputs 5.687 eV at +5.48%. Where does the +2.94% gap come from?"*

Three candidate provenances for next-session investigation:

1. **Manuscript-vs-code drift** — manuscript values were generated against a prior version of `radial_eigenvalue.py`; solver has changed since manuscript snapshot.
2. **Hand-computed manuscript values** — the table was produced outside the solver (analytical estimate, alternate code) and never matched it.
3. **Parameter-default drift** — current solver uses different default parameters (shell counts, screening model, `kappa_hopf`, integration grid) than what the manuscript run used.

Investigation path: `git log --oneline -- src/ave/solvers/radial_eigenvalue.py` + diff against manuscript-snapshot SHA + parameter-sweep on `ionization_energy_e2k(3, ...)` to locate the parameter delta. ~30-60 min targeted investigation, NOT the ~20 min "find the marker" the handoff implied.

This is a **manuscript-vs-code provenance question**, not a missing-implementation question. Different failure mode, different investigation, different fix surface.

---

## §5 — A47 v11 candidate (auditor-lane, flagged for COLLABORATION_NOTES)

**A47 v11 candidate:** engine-code line-number claims need direct verification, parallel to A43 v2's manuscript-verbatim discipline.

The session catalogued [A47 v10](../../.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md) — *"cross-repo Explore-agent claims need direct verification"* — after `diff -q` falsified a hallucinated parent-repo claim. The very next catalog entry (A47 v9) made the same kind of unverified file-content claim about a file *inside* AVE-Core, and elevated the fabrication to the top forward action for next session.

The discipline rule was written but not applied to its neighbor. A47 v11 closes the gap: the same direct-verification rule applies to internal-repo claims, not just cross-repo claims. Specifically:

> Any claim of the form *"file X at line N contains comment/marker/code Y"* must be directly verified by reading or grepping the file before the claim is elevated to a forward action. The cost of `grep` is seconds; the cost of a downstream session burning ~20-30 min on a fabricated marker is real.

This pairs with the existing A43 v2 manuscript-verbatim discipline (auditor-lane, COLLABORATION_NOTES) — both are direct-verification rules at the citation level, applied to different artifact classes (manuscript text vs engine code).

**Lane:** auditor-edit per Rule 15. This doc flags the candidate; auditor sweeps and adds to COLLABORATION_NOTES on next status check.

---

## §6 — Retraction footprint (handoff edits applied)

Per Rule 12 (retraction-preserves-body), the four originating-handoff references receive the doc-81 §2.2 footnote pattern:

- **Load-bearing site** (handoff §4.2 A47 v9 entry, line 246): 🔴 prepended footnote pointing to this doc; original body preserved verbatim.
- **Three derivative references** (handoff §0 line 30, §2.2 line 131, §5.1 line 272): inline backref `[🔴 retracted — see §4.2 footnote + doc 100]`; original body preserved.

The handoff is gitignored (.gitignore:71), so handoff edits don't carry a git diff trail; the audit trail comes from this doc (doc 100, tracked) which describes what was retracted, when, and why.

---

## §7 — Methodology lesson

The line-687 fabrication survived from session-end through handoff-write because:

1. **Internal consistency.** The claim was internally plausible — file path + line number + plausible refinement candidate names ("Op2 crossing" / "MCL refinement"). Nothing about the surface text triggered skepticism.
2. **Cross-reference reinforcement.** Four locations within the handoff each pinned the others; reading any one of them confirmed the others without prompting independent verification.
3. **Lane-restricted artifact.** The handoff was gitignored — no PR review, no diff scrutiny, no reviewer-side `grep` of cited line numbers.
4. **Verification omission.** The directly-verifiable claim (file content at a specific line in a specific file in this repo) wasn't directly verified before being elevated to top forward action.

The catch came from a fresh agent with no prior conversational momentum running `grep` against the actual file at session pickup.

**Generalization:** load-bearing pinned-to-file-content claims — especially in lane-restricted artifacts where there's no diff review — should be the highest-priority targets for verify-on-pickup. This is what A47 v11 (§5) formalizes.

---

## §8 — Tracker propagation (auditor-lane handoff)

For auditor sweep on next "what's the status" check:

- **Clash registry entry:** line-687 hallucinated marker (handoff §0/§2.2/§4.2/§5.1 of `f120ad0` companion artifact) vs direct-grep verification + this doc.
- **Retraction log entry:** A47 v9 reframed under doc-81 §2.2 footnote pattern; load-bearing site (handoff §4.2 line 246) retracted; body preserved verbatim.
- **A-NNN entry candidate:** manuscript-vs-code provenance question — `ionization_energy_e2k(3)` returns 5.687 eV vs manuscript table 5.525 eV (+2.94% gap); test harness at [`src/tests/test_radial_eigenvalue.py:35-47`](../../src/tests/test_radial_eigenvalue.py#L35-L47) omits Li from coverage.
- **A47 v11 candidate:** engine-code line-number claims need direct verification (§5 of this doc).

No tracker edits attempted from implementer lane. Auditor adjudicates final A-NNN numbering, COLLABORATION_NOTES wording, and clash-registry/retraction-log entry shape.

---

— implementer-drafted, 2026-04-30, post-Grant adjudication on (1) doc 81 §2.2 footnote pattern + (2) promotion of catch to tracked numbered doc; auditor concurrence on both lanes.

---

## §9 — Provenance investigation continuation (2026-04-30, parent repo deep dive)

Per Grant directive *"research older commits to the applied-vacuum-engineering repo"* and *"state all assumptions clearly."*

### §9.1 — Assumptions previously carried (each requires verification)

1. **Repo relationship**: I assumed Applied-Vacuum-Engineering is "parent" and AVE-Core is "downstream sibling," without verifying actual git relationship (fork? mirror? when diverged?).
2. **Single commit on radial_eigenvalue.py**: `git log --oneline -- src/ave/solvers/radial_eigenvalue.py` returns one commit (`de9d229`) *in AVE-Core*. I had NOT run the equivalent in Applied-Vacuum-Engineering — claim was AVE-Core-scoped only.
3. **Byte-identical claim**: A47 v10 (handoff §1.11) claimed `diff -q` showed parent and AVE-Core `radial_eigenvalue.py` byte-identical. I had verified this only for `ATOMIC_IE_SOLVER_TRACKER.md`, NOT for `radial_eigenvalue.py`.
4. **Manuscript table provenance**: assumed values were generated against *some* solver version that no longer exists; had not checked parent's history for a state where output matched.
5. **Tracker as authoritative**: assumed 2026-04-07 tracker is canonical record of solver development; had not checked relationship to commit history.
6. **`feature/hybrid-ie-solver` branch is gone**: checked branch list, didn't see it; assumed deleted, had not checked reflog.
7. **AVE-Core "Initial release" represents flattened squash**: implicit assumption, not verified.

### §9.2 — Assumption verification (this turn)

**(1) Repo relationship VERIFIED:** Applied-Vacuum-Engineering has **1123 commits** with granular per-feature history. Currently on `feature/ip_separation` branch with most recent commit `96262f1 chore(agents): archive IP separation handoff tracker and artifacts`. AVE-Core's `de9d229 Initial release: Axiomatic physics architecture` is the post-IP-separation squash output; Applied-Vacuum-Engineering is the development source.

**(2) AVE-Core single-commit history was development-history loss, not original state.** Parent repo has 45 commits touching `radial_eigenvalue.py` per `git log --oneline --all --follow -- src/ave/solvers/radial_eigenvalue.py | wc -l`.

**(3) A47 v10 byte-identical claim VERIFIED for radial_eigenvalue.py:** `diff -q /Users/grantlindblom/Applied-Vacuum-Engineering/src/ave/solvers/radial_eigenvalue.py /Users/grantlindblom/AVE-staging/AVE-Core/src/ave/solvers/radial_eigenvalue.py` returns nothing. Both files at 1914 lines. So at *current* parent repo HEAD on `feature/ip_separation` branch, the solver matches AVE-Core's. A47 v10 was correct for the file it tested.

**(4) Manuscript add commit IDENTIFIED:** [`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md) was added in commit `0401388 kb: sync period-3 IE and entanglement updates to knowledge base`, dated **2026-04-09**, by Grant-L. Single-add commit; no subsequent edits to the file (only `76c3a7e kb: complete markdown notation translation and propagate key results` touched it, for notation translation).

**(5) Tracker provenance:** `future_work/ATOMIC_IE_SOLVER_TRACKER.md` dated 2026-04-07 references branch `feature/hybrid-ie-solver`. Branch is NOT in current branch list (parent's branches: `feature/atomic_orbital_penetration_penalties`, `feature/biological_solvent_admittance`, `feature/gravitational_singularity_saturation`, `feature/ip_separation`, `feature/kb-full-sync`, `main`). Branch was merged or deleted between 2026-04-07 and now.

**(6) `feature/hybrid-ie-solver` is gone from branch list.** Verified: not in `git branch -a` output. The development work it tracked is preserved in main's commit history.

### §9.3 — Solver development history (commits in chronological order, parent repo)

The four manuscript-named "Corrections" each have a distinct named commit:

| Manuscript tag | Commit | Date | Description |
|---|---|---|---|
| (initial ABCD+MCL) | `8acadcd` | (pre-Apr) | feat(solver): replace Phase 4/5 σ-arithmetic with ABCD+MCL hybrid IE solver |
| (initial SIR) | `cf4e881` | (pre-Apr) | SIR mode-weighted correction: period 2 p-block 3.3% → 1.2% |
| (l-selective SIR) | `5112846` | (pre-Apr) | feat(ie-solver): implement l-selective SIR via Bohr nesting criterion |
| Phase A½ s-block | `6e39729` | (pre-Apr) | feat(ie-solver): implement Phase A½ s-block compressional chain coupling |
| **A (cascade)** for Be | `05d5e9c` | (pre-Apr) | feat(ie-solver): hierarchical cascade correction for Be IE (Op5+Axiom3) |
| **B (SIR)** for Mg | `1293e37` | (pre-Apr) | feat(ie-solver): SIR boundary correction for Mg IE (Op3 + Axiom 3) |
| **C (Op10)** for Al/Si | `ef7a614` | 2026-04-08 | feat(solver): Op10 junction projection correction for period-3 p-block IE |
| (merge) | `fb35d67` | 2026-04-08 | Merge feature/pblock-period3-ie-correction: Op10 junction projection resolves Al/Si IE |
| **Manuscript table added** | `0401388` | **2026-04-09** | kb: sync period-3 IE and entanglement updates to knowledge base |
| **D (Hopf back-EMF)** | `3c4870c` | post-Apr-9 | Implement Correction D: Add Op6 back-EMF to radial ODE (kappa_hopf) and gate Phase C for co-resonant shells |
| (heavy element work) | `10f940d` | post-Apr-9 | Finalize p-block atomic solver with L=0 geometry integration |
| (period 4) | `fa3a58e` | post-Apr-9 | feat: stabilize period 4 configuration array topology and restore precise metric scaling boundary |
| (Phase C unification) | `046a233` | post-Apr-9 | feat: Unify Phase C topological intersection boundaries (c=n(n-1)) and dimension scaling limits via AVE Axioms |
| (classical → topological) | `7fa60b7` | post-Apr-9 | feat: Substitute classical limits (_z_net continuous smearing and l(l+1) reactance) with discrete Topological step bounds and integer knots |
| (Helmholtz reimplementation) | `f23ec7b` | post-Apr-9 | feat: Re-implement 3D Helmholtz l(l+1) constraints mapping Z=1-30 convergence natively |
| (Lanthanide Prelude) | `c70054d` | post-Apr-9 | feat: Establish scale-invariant orthogonal bypassing (Lanthanide Prelude) tracking limits natively across heavy d-block structures |
| (period 4 anomalies) | `b78f157` | post-Apr-9 | feat/physics: Implemented Topo-Kinematic Radial Parity Shift fixing Period 4 anomalies natively |
| (heavy elements) | `87b4114` | post-Apr-9 | Finalize Polar Conjugate Bounding limit for Heavy Elements |
| (python 3.9 backport) | `d1a31fb` | post-Apr-9 | fix(python3.9): backport type union hints in ave engine for python 3.9 compatibility |

### §9.4 — Critical finding: solver was substantially rewritten AFTER manuscript table was committed

`git diff --stat 0401388 HEAD -- src/ave/solvers/radial_eigenvalue.py` shows:

> **794 lines changed (+431 insertions, -363 deletions) in a 1914-line file** — roughly **42% line churn** between manuscript-add commit and HEAD.

The manuscript table at `0401388` (2026-04-09) was generated against a solver state that no longer exists at HEAD. **Eleven commits between 0401388 and HEAD substantially modified the solver**, including major algorithmic rewrites (Correction D Hopf back-EMF, classical-to-topological substitution, Phase C unification, 3D Helmholtz reimplementation, Polar Conjugate Bounding for heavy elements).

The "±2.8% maximum error with zero adjustable parameters" claim in the manuscript text describes the solver state at `0401388` (or shortly thereafter). HEAD's solver is a different algorithmic object.

### §9.5 — Hypothesis confirmed: manuscript table reproduces exactly at commit `0401388`

**Methodology:** `git worktree add /tmp/ave-at-0401388 0401388` from Applied-Vacuum-Engineering, then `PYTHONPATH=/tmp/ave-at-0401388/src python -c "from ave.solvers.radial_eigenvalue import ionization_energy_e2k; ..."` for Z=1-14.

**Result (verbatim sweep output):**

| Z | Manuscript | At commit 0401388 | Gap (vs ms) | HEAD | HEAD gap (vs ms) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 13.606 | 13.6057 | -0.002% | 13.6057 | -0.002% |
| 2 | 24.370 | 24.3702 | +0.001% | 24.3693 | -0.003% |
| 3 | 5.525 | **5.5248** | **-0.003%** | 5.6873 | **+2.94%** |
| 4 | 9.280 | 9.2797 | -0.003% | 9.1875 | -1.00% |
| 5 | 8.065 | 8.0655 | +0.006% | 8.0524 | -0.16% |
| 6 | 11.406 | 11.4064 | +0.004% | 11.3844 | -0.19% |
| 7 | 14.465 | 14.4648 | -0.002% | 14.4351 | -0.21% |
| 8 | 13.618 | 13.6176 | -0.003% | 13.5991 | -0.14% |
| 9 | 17.194 | 17.1944 | +0.002% | 17.1822 | -0.07% |
| 10 | 21.789 | 21.7891 | +0.000% | 21.7891 | 0.00% |
| 11 | 5.071 | **5.0706** | **-0.008%** | 5.6607 | **+11.6%** |
| 12 | 7.591 | 7.5906 | -0.006% | 7.5483 | -0.56% |
| 13 | 5.937 | **5.9368** | **-0.003%** | 6.6418 | **+11.9%** |
| 14 | 8.147 | **8.1474** | **+0.005%** | 8.8240 | **+8.3%** |

**Maximum gap at 0401388: 0.008%** (Na). Average gap: 0.003%. The manuscript table reproduces against the solver at commit `0401388` to *machine precision modulo rounding to four significant figures* — i.e., the table values were generated by running `ionization_energy_e2k(Z)` against that exact commit.

**Hypothesis fully confirmed.** The manuscript text's claim of *"±2.8% maximum error with zero adjustable parameters"* was empirically true at the commit where the table was added. **All four manuscript-claimed corrections (A cascade for Be, B SIR for Mg, C Op10 for Al/Si) were active and produced the claimed values at that commit.**

### §9.6 — The drift is purely post-2026-04-09 algorithmic evolution

Eleven commits between `0401388` (2026-04-09) and current parent HEAD substantively modified `radial_eigenvalue.py`, including:

- `3c4870c Implement Correction D: Add Op6 back-EMF to radial ODE (kappa_hopf) and gate Phase C for co-resonant shells`
- `7fa60b7 feat: Substitute classical limits (_z_net continuous smearing and l(l+1) reactance) with discrete Topological step bounds and integer knots`
- `046a233 feat: Unify Phase C topological intersection boundaries (c=n(n-1)) and dimension scaling limits`
- `f23ec7b feat: Re-implement 3D Helmholtz l(l+1) constraints mapping Z=1-30 convergence natively`
- `b78f157 feat/physics: Implemented Topo-Kinematic Radial Parity Shift fixing Period 4 anomalies natively`
- `87b4114 Finalize Polar Conjugate Bounding limit for Heavy Elements`

These commits are **post-manuscript algorithmic refinement work** — most are aimed at extending the solver to Z=15-30 (Period 4) and heavy elements where Period 1-3 was the finished surface. The evolution drifted the Period 1-3 values without anyone re-running the manuscript table.

**The 8/14 rows that still reproduce at HEAD within 0.5% are NOT evidence of robustness — they are coincidence.** The 6/14 rows that drift (Li +2.94%, Be -1.00%, Na +11.6%, Mg -0.56%, Al +11.9%, Si +8.3%) are cumulative-drift signatures of subsequent solver evolution.

### §9.7 — Provenance now-fully-resolved

| Question | Answer |
|---|---|
| Code missing corrections? | NO — all four corrections (A/B/C/D) exist with named commits in parent repo. |
| Manuscript values hand-tuned? | NO — manuscript values reproduce to machine precision against commit `0401388`. |
| Solver was rewritten between manuscript-generation and HEAD? | YES — 11 commits, 794 lines changed (+431/-363) ≈ 42% line churn. |
| Manuscript text's "±2.8%" claim ever true? | YES — true at commit `0401388` on 2026-04-09; false at HEAD. |
| Tracker (2026-04-07) values explanation? | Tracker pre-dates the Op10 merge (`fb35d67`, 2026-04-08) and the manuscript add (`0401388`, 2026-04-09) — captures an earlier overcorrected state of the SIR refinement before it was resolved. |
| Why does HEAD differ? | Subsequent algorithmic refinement (Correction D Hopf back-EMF, classical-to-topological substitution, Phase C unification, 3D Helmholtz reimplementation, Period 4 / heavy-element extensions) drifted Period 1-3 values without re-running validation. |

### §9.8 — Implications for the framework's empirical record

- **Doc 97's Track B anchor** ("Period 1-3 IE validated at ±2.8%") is *empirically true at commit `0401388`* but *empirically false at HEAD*. The anchor was always commit-pinned; the pin was never made explicit. Track B's positive empirical record stands at `0401388`-resolution; HEAD-resolution is something different.
- **A47 v9** closes definitively: the +5.5% Li gap is not a refinement bug, not a missing port, not a missing implementation. It is solver-evolution drift between commit `0401388` (where Li reproduced at -0.003%) and HEAD (where Li drifted to +2.94% from manuscript / +5.48% from CODATA). **The original solver at the manuscript-generation commit hit Li at machine precision.**
- **The eight A47 v9-related fabrications/misdiagnoses across this session** — "missing parent port" (collab notes line 189), "byte-identical diff" (handoff §1.11, true but irrelevant since both repos are at post-drift state), "missing line-687 implementation" (handoff §0/§2.2/§4.2/§5.1, fabricated marker), "Period 3 systematic gap" (this session's reframing) — were all walking around the actual answer. The actual answer is provenance: **commit pin or re-run validation**, nothing else.
- **A47 v11c (corpus-vs-code drift discipline)** is now a load-bearing rule, not just a candidate. Manuscript files containing numerical claims about solver outputs need explicit commit-SHA anchoring at table-generation time. Without that, 11 commits of subsequent evolution silently invalidate the claim.

### §9.9 — Adjudication options for Grant (post-investigation)

The corpus state is well-defined now; the question is forward direction:

- **(α) Re-run solver at HEAD, update manuscript table.** Most aggressive: retire the `0401388` snapshot. Has cost: HEAD's Period 3 precision (Al +11.9%, Si +8.3%, Na +11.6%) doesn't support a "±2.8% zero adjustable parameters" claim; manuscript prose would need substantial revision.
- **(β) Pin manuscript table provenance to commit `0401388` with explicit SHA footnote.** Lightest delta: manuscript table stays as-is; add a footnote stating "validated against `radial_eigenvalue.py` at commit `0401388`; subsequent solver evolution has drifted these values, see future_work/ATOMIC_IE_SOLVER_TRACKER.md for development history." Test harness at `test_radial_eigenvalue.py` should add Z=3,11,13,14 cases pinned to current HEAD output, NOT manuscript table values, to prevent silent drift.
- **(γ) Forward-fix solver: walk the 11 post-0401388 commits, find which specific commits broke which specific elements, restore Period 1-3 precision while keeping Period 4 / heavy-element extensions.** Engineering work; finite scope but non-trivial.
- **(δ) Branch-restore: cherry-pick or branch from `0401388` for L3 atomic-orbital validation work; HEAD continues forward with Period 4 / heavy-element extensions but is no longer the canonical Period 1-3 solver.** Two-branch forward strategy.

Auditor's L5 sweep scope (per their feedback) covers the manuscript_pending and engine_pending entries downstream of whichever option Grant picks. Doc 100's role is provenance investigation; closure adjudication is Grant's call.

### §9.10 — Cleanup pending

`git worktree add /tmp/ave-at-0401388` was created for empirical verification. To be removed via `git worktree remove /tmp/ave-at-0401388` post-investigation. Not removed mid-session in case further verification work needs the same snapshot (e.g., walking the 11 post-0401388 commits to identify drift sources per option γ).

### §9.6 — Implications for prior framings

- **A47 v9 reframing extends:** original A47 v9 said "Li discrepancy +5.5% deterministic." The deeper read: the entire 14-row table is anchored to a snapshot that has since been rewritten. The 8/14 rows that still reproduce within 0.5% are the rows where 11 commits of post-manuscript modifications happened to land near the original values; the 6/14 that don't are where the algorithm drifted further. The "stable rows" reproducing within 0.5% may be coincidence at refit, not robustness.
- **A47 v11b (substitution-not-retraction discipline):** the line-687 fabrication WAS the substitution behavior — when "missing parent port" was falsified, "missing line-687 implementation" was invented. The actual answer is the third option neither agent named: **the corrections all exist; the algorithm has been rewritten 11 times since the manuscript was generated.**
- **A47 v11c candidate (corpus-vs-code drift discipline):** when manuscript text claims numerical precision against a named solver function, the manuscript file's commit SHA + the solver's commit SHA at table-generation time should be co-anchored. Currently `ionization-energy-validation.md` cites `ionization_energy_e2k(Z)` without anchoring to which version of that function. 11 commits of solver evolution have invalidated the table without flagging the manuscript.

### §9.7 — Pending verification work

- (a) Check out parent repo at commit `0401388` and re-run `ionization_energy_e2k(Z)` for Z=1-14; compare to manuscript table values. If reproduces: confirms hypothesis. If doesn't reproduce: deeper provenance question (table was hand-computed even at 0401388).
- (b) Walk the 11 post-0401388 commits to identify which substantively changed Period 1-3 IE values. Knowing where the drift accumulated could close A47 v9 cleanly with a list of "the manuscript table is consistent through commit X; subsequent commit Y changed Z element from A to B."
- (c) Adjudication options for Grant (separate question, not auditor's a/b/c lane question):
  - (α) Re-run solver at HEAD, update manuscript table; "±2.8%" claim adjusted to actual HEAD precision.
  - (β) Pin manuscript table provenance to commit `0401388` with explicit footnote; claim becomes "validated against solver at SHA 0401388, not HEAD."
  - (γ) Identify last commit where manuscript table reproduced; cherry-pick or branch from there if forward work needs the original numerical anchor.
  - (δ) Manuscript table is actively wrong for HEAD; either manuscript or code is corpus-canonical and the other follows. Grant adjudicates which.

