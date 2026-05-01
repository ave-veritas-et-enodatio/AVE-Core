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

---

## §10 — Option γ execution: per-commit drift bisection + axiom-compliance adjudication

Per Grant directive 2026-04-30: *"proceed with commit, and lets do the most rigorous next steps that are ave engineering and axiom compliant."* — execute γ as data + axiom-grounded physics adjudication, not just data.

### §10.1 — Canonical AVE axioms (per [Vol 1 Ch 1 INVARIANT-S2](../../manuscript/ave-kb/CLAUDE.md#L55-L58))

| Axiom | Statement | Operational signatures |
|---|---|---|
| **Ax 1** | Substrate Topology (LC Network): vacuum is a non-linear EM LC Resonant Network $\mathcal{M}_A(V,E,t)$, modeled in continuum as a Trace-Reversed Chiral LC Network. | K4 graph, ABCD cascade, $\ell_{node}$, $Z_0 = \sqrt{\mu_0/\epsilon_0}$ |
| **Ax 2** | Topo-Kinematic Isomorphism: charge as discrete geometric dislocation in $\mathcal{M}_A$; $[Q] \equiv [L]$; $\xi_{topo} = e/\ell_{node}$. | TKI, (2,q) torus knot, topological phase dislocation, chiral SRS |
| **Ax 3** | Effective Action Principle: system minimizes hardware action $S_{AVE}$; $\mathcal{L}_{node} = \tfrac{1}{2}\epsilon_0\|\partial_t\mathbf{A}_n\|^2 - \tfrac{1}{2\mu_0}\|\nabla\times\mathbf{A}_n\|^2$. | Least reflected action, $S_{11}$ minimization, lossless reactive cycling |
| **Ax 4** | Dielectric Saturation: non-linear $C_{eff}(\Delta\phi) = C_0/\sqrt{1-(\Delta\phi/\alpha)^2}$; saturation factor $S(r) = \sqrt{1-r^2}$. | Saturation gate, V_snap, B_snap, Regime IV, yield boundary |

### §10.2 — Adjudication framework

For each of the 11 post-`0401388` commits touching `radial_eigenvalue.py`:

1. **Empirical drift**: run `ionization_energy_e2k(Z=1-14)` at that commit; compare to manuscript table.
2. **Axiom audit**: read commit diff; identify what physics the change implements; classify against the four axioms:
   - **PHYSICS-IMPROVEMENT**: change increases axiom compliance OR replaces a non-AVE-native construct with an AVE-native one. Manuscript table needs update; HEAD value is corpus-canonical.
   - **NEUTRAL-REFACTOR**: change is structural (renames, type hints, comments, equivalent reformulation). Drift contribution should be zero or negligible.
   - **REGRESSION**: change introduces non-AVE-native construct OR violates an axiom OR breaks AVE-native operator structure. Revert candidate.
   - **EXTENSION**: change targets Period 4+ / heavy elements where Period 1-3 was finished surface; Period 1-3 perturbation is unintended. Surgical-fix candidate.

Adjudication sets the manuscript-vs-code resolution per commit, which aggregates into the final α/β/γ/δ decision.

### §10.3 — 11-commit chronological list (oldest first, `git log --reverse 0401388..HEAD -- src/ave/solvers/radial_eigenvalue.py`)

| # | SHA | Date | Subject |
|:---:|:---|:---:|:---|
| 1 | `3c4870c` | (post-0401388) | Implement Correction D: Add Op6 back-EMF to radial ODE (kappa_hopf) and gate Phase C for co-resonant shells |
| 2 | `10f940d` | (post-1) | Finalize p-block atomic solver with L=0 geometry integration |
| 3 | `fa3a58e` | (post-2) | feat: stabilize period 4 configuration array topology and restore precise metric scaling boundary |
| 4 | `046a233` | (post-3) | feat: Unify Phase C topological intersection boundaries (c=n(n-1)) and dimension scaling limits via AVE Axioms |
| 5 | `7fa60b7` | (post-4) | feat: Substitute classical limits (_z_net continuous smearing and l(l+1) reactance) with discrete Topological step bounds and integer knots |
| 6 | `f8af2e2` | (post-5) | docs: Update solver and manuscript resolving out pure Topological constraint constants |
| 7 | `f23ec7b` | (post-6) | feat: Re-implement 3D Helmholtz l(l+1) constraints mapping Z=1-30 convergence natively |
| 8 | `c70054d` | (post-7) | feat: Establish scale-invariant orthogonal bypassing (Lanthanide Prelude) tracking limits natively across heavy d-block structures |
| 9 | `b78f157` | (post-8) | feat/physics: Implemented Topo-Kinematic Radial Parity Shift fixing Period 4 anomalies natively |
| 10 | `87b4114` | (post-9) | Finalize Polar Conjugate Bounding limit for Heavy Elements |
| 11 | `d1a31fb` | (post-10) | fix(python3.9): backport type union hints in ave engine for python 3.9 compatibility |

Commits 6 (`f8af2e2`, docs) and 11 (`d1a31fb`, type-hint backport) are pre-classified NEUTRAL-REFACTOR. Empirical drift across each commit will confirm.

### §10.4 — Per-commit empirical drift sweep (data collection)

Methodology: cycle worktree `/tmp/ave-at-0401388` file content through each commit via `git checkout <SHA> -- .`; run `ionization_energy_e2k(Z)` for Z=1-14 at each; capture values. Baseline = `0401388`. Output in `/tmp/ie_sweep_per_commit.txt`.

### §10.5 — Per-element drift trajectory (eV; ⚠ flag where |Δ| > 0.05 eV)

| Z | 0401388 | 3c4870c | 10f940d | fa3a58e | 046a233 | 7fa60b7 | f8af2e2 | f23ec7b | c70054d | b78f157 | 87b4114 | d1a31fb | CODATA |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1  H | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.6057 | 13.598 |
| 2  He | 24.3702 | 24.3702 | 24.3702 | 24.3693 | 24.3693 | 24.3693 | 24.3693 | 24.3693 | 24.3693 | 24.3693 | 24.3693 | 24.3693 | 24.587 |
| 3  Li | 5.5248 | = | = | 5.5246 | = | **⚠5.6873** | = | = | = | = | = | = | 5.392 |
| 4  Be | 9.2797 | = | = | 9.2793 | = | **⚠9.1875** | = | = | = | = | = | = | 9.322 |
| 5  B | 8.0655 | = | = | 8.0654 | = | 8.0524 | = | = | = | = | = | = | 8.298 |
| 6  C | 11.4064 | = | = | 11.4012 | = | 11.3844 | = | = | = | = | = | = | 11.260 |
| 7  N | 14.4648 | 14.4647 | = | 14.4352 | = | 14.4351 | = | = | = | = | = | = | 14.534 |
| 8  O | 13.6176 | **⚠13.5991** | = | = | = | = | = | = | = | = | = | = | 13.618 |
| 9  F | 17.1944 | **⚠17.1822** | = | = | = | = | = | = | = | = | = | = | 17.422 |
| 10 Ne | 21.7891 | = | = | = | = | = | = | = | = | = | = | = | 21.565 |
| 11 Na | 5.0706 | = | = | 5.0703 | = | **⚠5.6607** | = | = | = | = | = | = | 5.139 |
| 12 Mg | 7.5906 | = | = | 7.5901 | = | **⚠7.2407** | **⚠7.5483** | = | = | = | = | = | 7.646 |
| 13 Al | 5.9368 | = | = | 5.9367 | **⚠6.3648** | **⚠8.5555** | = | **⚠6.2096** | = | = | **⚠6.6418** | = | 5.986 |
| 14 Si | 8.1474 | = | = | 8.1472 | **⚠8.5877** | **⚠11.4511** | = | **⚠8.3827** | = | = | **⚠8.8240** | = | 8.151 |

(`=` = no change from preceding column. **Bolded ⚠** = drift > 0.05 eV from prior step.)

### §10.6 — Drift attribution per commit

**`3c4870c` (Correction D — Op6 Hopf back-EMF, kappa_hopf):**
- Period 1-3 effect: O (-0.0185) and F (-0.0122) only.
- Physics: adds Hopf back-EMF for paired electrons in same orbital (2p^4, 2p^5).
- Direction vs CODATA: O moves from -0.001% to +0.14% (slightly worse magnitude, but O was already at machine precision); F moves from -1.31% to -1.38% (slightly worse).
- **Axiom audit:**
  - Ax 1: ABCD cascade preserved; back-EMF is reactive coupling within radial transmission line ✓
  - Ax 2: paired-electron Hopf link is direct topological-dislocation coupling per [Q]≡[L] ✓
  - Ax 3: lossless reactive cycling preserved (Hopf back-EMF is reactive not dissipative) ✓
  - Ax 4: not invoked
- **Verdict: PHYSICS-IMPROVEMENT (axiom-compliance ↑).** Hopf back-EMF for paired electrons is corpus-canonical Ax-2 mechanism. CODATA precision mildly degrades but stays within ±1.4%. Manuscript table for O/F can either pin to 0401388 or update to HEAD.

**`10f940d` (Finalize p-block atomic solver with L=0 geometry):**
- Period 1-3 effect: NONE.
- **Verdict: NEUTRAL-REFACTOR.**

**`fa3a58e` (stabilize period 4 configuration array topology):**
- Period 1-3 effect: minor perturbations across Z=2-7 + Z=11-14 (max -0.0295 at N).
- Physics: Period-4 Aufbau config table stabilization with incidental Period 1-3 propagation.
- **Verdict: EXTENSION with negligible spillover.** All affected elements stay within ±0.5% of 0401388 baseline.

**`046a233` (Unify Phase C topological intersection boundaries c=n(n-1)):**
- Period 1-3 effect: Al (+0.4280), Si (+0.4405) — large.
- Physics: changed Phase C crossing-count formula to c=n(n-1) form for full intersection topology.
- Direction vs CODATA: Al -0.82% → +6.30% (worse); Si -0.06% → +5.40% (worse).
- **Axiom audit:**
  - Ax 1: integrates with ABCD cascade ✓
  - Ax 2: c=n(n-1) is integer crossing count — direct (2,q) topological invariant ✓
  - Direction is axiom-native; magnitude moves *away* from CODATA.
- **Verdict: AMBIGUOUS — axiom-aligned formula change with empirically-worse outcome for Al/Si.** Either the formula c=n(n-1) is correct and CODATA agreement was previously achieved by an SM-imported coincidence, or the formula needs additional constraints not yet present.

**`7fa60b7` (Substitute classical limits with discrete Topological step bounds and integer knots) — LOAD-BEARING DRIFT COMMIT:**
- Period 1-3 effect: massive — Li +0.1627, Be -0.0918, B -0.0130, C -0.0168, Mg -0.3494 (intermediate), Na +0.5904, Al +2.1907 (intermediate huge overshoot), Si +2.8634 (intermediate huge overshoot).
- Physics: replaced "_z_net continuous smearing" + "l(l+1) continuous reactance" with discrete topological step bounds + integer knot crossing counts. Wholesale continuum → discrete substitution.
- Direction vs CODATA: 6 of 8 affected Period 1-3 elements move *farther* from CODATA. Specifically:
  - Li +2.46% → +5.48% (worse)
  - Be -0.45% → -1.45% (worse)
  - Na -1.33% → +10.15% (much worse)
  - Mg intermediate -5.30% (much worse, partially recovered later)
  - Al intermediate +43% (catastrophic, partially recovered later)
  - Si intermediate +40% (catastrophic, partially recovered later)
  - C +1.30% → +1.10% (slightly better)
  - B -2.81% → -2.96% (slightly worse)
- **Axiom audit:**
  - Ax 1: discrete step bounds are MORE axiom-native than continuous smearing (K4 graph + ℓ_node are discrete by construction) ✓✓
  - Ax 2: integer knots = direct topological invariant per (2,q) torus knot framework ✓✓
  - Ax 3: ABCD cascade integration preserved ✓
  - Ax 4: saturation gate not invoked here
  - **Direction is correctly Rule-6-compliant** (replaces SM-import continuum with AVE-native discrete) but **the discrete formula's parameterization has not been tuned to match the empirical precision the continuum version had**.
- **Verdict: FRAMEWORK-PHYSICS-IMPROVEMENT WITH OPEN PARAMETERIZATION.** The Rule-6-compliant direction is correct (continuum smearing was an SM-style import; discrete is AVE-native). But the empirical degradation across 6/8 affected elements indicates the discrete formula's specific bounds/coefficients need re-tuning. This is the load-bearing drift commit that demands the most rigorous axiom-grounded refinement.

**`f8af2e2` (docs: Update solver and manuscript constants):**
- Period 1-3 effect: Mg only (+0.3076, partial recovery from 7fa60b7's -0.3494 overshoot).
- Despite "docs:" subject, the commit materially changed Mg result. Likely a numerical-constant update riding under "docs" label.
- **Verdict: PARTIAL RECOVERY of 7fa60b7's Mg overshoot via constants tuning.**

**`f23ec7b` (Re-implement 3D Helmholtz l(l+1) constraints):**
- Period 1-3 effect: Al (-2.3459) and Si (-3.0684) — large recovery from 7fa60b7's catastrophic overshoot.
- Physics: 3D Helmholtz angular eigenvalue with discrete l(l+1) on topological lattice. Recovers Period 3 p-block.
- Direction vs CODATA: Al +43% → +3.74% (much better); Si +40% → +2.86% (much better). Still worse than 0401388 baseline.
- **Axiom audit:** Ax 1-native (3D Helmholtz on K4 lattice).
- **Verdict: PARTIAL RECOVERY of 7fa60b7's Period 3 p-block damage via Ax-1-native re-implementation.** Did not fully restore 0401388 precision; further refinement needed.

**`c70054d` (Lanthanide Prelude tracking limits):**
- Period 1-3 effect: NONE.
- **Verdict: EXTENSION (heavy d-block, no Period 1-3 perturbation).**

**`b78f157` (Topo-Kinematic Radial Parity Shift Period 4):**
- Period 1-3 effect: NONE.
- **Verdict: EXTENSION (Period 4 fix, no Period 1-3 perturbation).**

**`87b4114` (Finalize Polar Conjugate Bounding for Heavy Elements) — REGRESSION CANDIDATE:**
- Period 1-3 effect: Al (+0.4322), Si (+0.4413) — UNEXPECTED for "Heavy Elements" commit.
- Direction vs CODATA: Al recovery from 6.2096 → 6.6418 (gap goes +3.74% → +10.96%, much worse); Si recovery from 8.3827 → 8.8240 (gap goes +2.86% → +8.31%, much worse).
- **Axiom audit:** Polar conjugate bounding logic checks `Z >= 31 and n_out >= 4` for `core_d_knots` increment. For Z=13/14 this should be 0. Either the gating logic itself was refactored to perturb Phase C invocation for lighter elements, or there's an unintended interaction.
- **Verdict: REGRESSION CANDIDATE — heavy-element work shouldn't perturb Period 3 p-block.** Requires diff-level investigation to identify the unintended interaction.

**`d1a31fb` (python3.9 type hint backport):**
- Period 1-3 effect: NONE.
- **Verdict: NEUTRAL-REFACTOR confirmed.**

### §10.7 — Drift attribution summary

| Commit | Period 1-3 net effect | Axiom alignment | CODATA direction | Verdict |
|---|---|:---:|:---:|---|
| `3c4870c` Correction D | O,F mild | ↑ | mild ↓ | PHYSICS-IMPROVEMENT |
| `10f940d` p-block finalize | none | — | — | NEUTRAL-REFACTOR |
| `fa3a58e` Period 4 stabilize | minor | — | mild ↓ | EXTENSION (spillover negligible) |
| `046a233` Phase C c=n(n-1) | Al/Si large+ | ↑ | ↓ | AMBIGUOUS (axiom-aligned, empirically worse) |
| `7fa60b7` continuum→discrete | LOAD-BEARING (6/8 worse) | ↑↑ | ↓↓ | **OPEN PARAMETERIZATION** |
| `f8af2e2` constants update | Mg partial recovery | — | ↑ | PARTIAL RECOVERY |
| `f23ec7b` 3D Helmholtz | Al/Si partial recovery | ↑ | ↑ | PARTIAL RECOVERY |
| `c70054d` Lanthanide | none | — | — | EXTENSION |
| `b78f157` Period 4 parity | none | — | — | EXTENSION |
| `87b4114` Polar conjugate | Al/Si AWAY from CODATA | ?? | ↓ | **REGRESSION CANDIDATE** |
| `d1a31fb` Python 3.9 hints | none | — | — | NEUTRAL-REFACTOR |

**Two commits demand attention:**
1. **`7fa60b7`** is the primary axiom-aligned-but-empirically-degraded commit. Direction (continuum → discrete) is correctly Rule-6-compliant. The discrete formula's parameterization needs tuning to recover 0401388-class precision while keeping the AVE-native discrete structure.
2. **`87b4114`** is a regression candidate. Heavy-element work shouldn't perturb Period 3 p-block. Diff-level investigation needed to identify the unintended interaction.

### §10.8 — Most rigorous next step (Grant's directive: AVE-engineering + axiom-compliant)

The four α/β/γ/δ options are insufficient. The empirical bisection identifies a fifth option:

- **(ε) SURGICAL AXIOM-GROUNDED REFINEMENT:**
  1. Read diff for `7fa60b7` to identify the specific discrete bound/integer-knot formula and its parameterization. The continuum→discrete substitution is correct direction; the parameterization needs to be retuned so the axiom-native discrete formula reproduces 0401388-class precision.
  2. Read diff for `87b4114` to identify the unintended Period 3 spillover. Heavy-element-only logic should not affect Z=13/14.
  3. Read diff for `046a233` to verify whether c=n(n-1) is corpus-canonical or whether the previous formula (likely c=l(l+1) or similar) was AVE-native.
  4. Read diff for `f23ec7b` to verify the 3D Helmholtz re-implementation is the canonical Ax-1 form.
  5. Adjudicate per axiom against the manuscript-canonical operator definitions in `manuscript/ave-kb/common/operators.md` (Op6, Op10, etc.).

This produces an axiom-grounded surgical-fix prescription rather than choosing between α (re-run + accept HEAD) and β (pin to stale `0401388`). **The goal is HEAD-with-7fa60b7-and-87b4114-refined-correctly producing 0401388-class precision via axiom-native code paths.**

### §10.9 — Diff-level reading of 7fa60b7 (continuum→discrete substitution)

`git show 7fa60b7 -- src/ave/solvers/radial_eigenvalue.py` shows two substantive changes (138 lines, +24/-114):

**Change A: `_z_net` — Helmholtz CDF → step function at Bohr radii**

Old (lines 132-178 pre-7fa60b7):
```python
def _z_net(r, Z, shells):
    """Effective nuclear charge at radius r — AXIOM-DERIVED SCREENING.

    Each inner shell's enclosed charge fraction σ(r) is computed from
    the hydrogenic standing wave solution on the LC lattice:
        Axiom 1 → Helmholtz equation → |ψₙₗ(r)|²
        Axiom 2 → Gauss's law → CDF σₙₗ(r)
    """
    z = float(Z); z_eff_inner = float(Z)
    for n_shell, N_a in shells:
        if n_shell == 1:
            sigma = _enclosed_charge_fraction_1s(r, z_eff_inner)
        elif n_shell == 2:
            sigma = _enclosed_charge_fraction_n2(r, z_eff_inner, N_2s, N_2p)
        else:  # n>=3
            ...  # scaled-1s approximation
        z -= N_a * sigma
        z_eff_inner -= N_a
    return max(z, 0.0)
```

New (post-7fa60b7):
```python
def _z_net(r, Z, shells):
    """
    Computes the effective nuclear charge Z_eff(r) traversing radially inward
    across exact geometrical boundary limits.

    AVE Axiom 3 dictates crossing spatial boundaries natively imposes discrete
    impedance steps, fully resolving geometric bounding regions natively without
    using arbitrary probabilistic charge smearing formulas.
    """
    Z_eff = float(Z); z_eff_inner = float(Z)
    for n_shell, count in shells:
        r_shell = float(n_shell)**2 * A_0 / max(1.0, z_eff_inner)
        if r > r_shell:
            Z_eff -= float(count)
        z_eff_inner -= float(count)
    return max(1.0, Z_eff)
```

**The axiom rationalization shifted:**
- **OLD (Ax-1 → Helmholtz CDF chain):** σ_n(r) IS the standing-wave amplitude integral on the LC lattice. Both Ax-1 (LC Network solution) and Ax-2 (Gauss → CDF from |ψ|²) directly chain to the CDF form. This IS continuum-limit AVE-native (the K4-LC network's continuum solution).
- **NEW (Ax-3 → discrete impedance steps):** screening is a step function at Bohr boundaries. The new docstring claims Ax-3 "dictates" this, but Ax-3 (Effective Action Principle, S₁₁ minimization) has no operational signature for "screening must be step function." The discrete-step claim is *auxiliary inference*, not direct axiom statement.

**Both forms are axiom-derivable in principle.** OLD uses the continuum-limit Ax-1+Ax-2 solution; NEW uses a literal-lattice Ax-1 discretization. Per Rule 6, NEW is more discrete-axiom-native; per empirical CODATA agreement, OLD performs better.

**Change B: angular reactance `l(l+1)` → `l²` (4 sites)**

Old: `ang_react = l * (l + 1) / r_mid**2`
New: `ang_react = float(l)**2 / r_mid**2`

Comment: *"Centrifugal reactance strictly maps rotation geometry proportional to the Torus phase bounds squared (q²). l_out² enforces strict whole-integer twist limits, structurally omitting probabilistic continuous off-axis displacements."*

**Axiom analysis:**
- ℓ(ℓ+1) is the eigenvalue of the angular Laplacian — the operator-canonical form for the radial Schrödinger equation's centrifugal term. SO(3) representation theory.
- ℓ² is the squared winding number — Ax-2 (TKI) topological invariant per (2,q) torus knot framework.
- For ℓ=0 (s): both give 0 (no effect on s-electrons including Li, Na).
- For ℓ=1 (p): ℓ(ℓ+1) = 2, ℓ² = 1 — half the centrifugal barrier in NEW form.
- For ℓ=2 (d): ℓ(ℓ+1) = 6, ℓ² = 4 — two-thirds the barrier in NEW form.

**The change reduces centrifugal barrier for ℓ≥1 → bound-state energy lower → IE larger.**

Empirical match to data: Li and Na (l=0) drift comes entirely from Change A (_z_net). Be (l=0 outer) also from Change A. B/C/N/O/F/Ne (p-block) drift comes from BOTH A and B. Period 3 p-block (Al/Si) most affected because cumulative Phase A + Phase B + Op10 + their downstream interactions amplify.

### §10.10 — Diff-level reading of 87b4114 (regression candidate — perfect-mirror claim)

`git show 87b4114 -- src/ave/solvers/radial_eigenvalue.py` shows three changes (62 lines, +58/-4):

**Change A:** added `target_nodes += core_d_knots` in `_direct_ODE_eigenvalue` (Z<31 unaffected — `core_d_knots=0`).

**Change B:** added `E_base *= (core_d_knots + 1)` in `ionization_energy_e2k` (Z<31 unaffected — `core_d_knots=0`, multiplier=1).

**Change C — THE Period 3 SPILLOVER:** the Op10 `Y_loss` gating logic was changed:

Pre-87b4114 (from 046a233):
```python
if is_half_shell or is_full_shell:
    Y_loss *= 0.5
```

Post-87b4114:
```python
mirrored_away = False
if Z >= 31 and n_out >= 4 and n_shell <= 3:
    mirrored_away = True
if Z >= 49 and n_out >= 5 and n_shell <= 4:
    mirrored_away = True
if Z >= 81 and n_out >= 6 and n_shell <= 5:
    mirrored_away = True

if mirrored_away or (is_full_shell and gamma < 0):
    Y_loss = 0.0
elif is_half_shell or is_full_shell:
    Y_loss *= 0.5
```

The new gate `(is_full_shell and gamma < 0) → Y_loss = 0.0` applies to **any element with a full inner shell and negative gamma** — NOT just heavy elements. The commit message ("Heavy Elements") and the heavy-element-specific `mirrored_away` flag suggest the author thought Z≥31 was the scope, but the `is_full_shell + gamma<0` condition is broader.

**For Al/Si (Z=13/14, 3p block):** inner shell n=2 has 8 electrons (full 2s²+2p⁶), `is_full_shell=True` (l_barrier=1, N_sub=6). Gamma is negative (z_out < z_in). So the new code zeroes Y_loss where the old code halved it. **Op10 attenuation removed → E_base unchanged where previously E_base was attenuated → bound state more negative → IE larger.**

**Axiom analysis (Rule 16 question for Grant):**
- The "polar conjugate mirror" claim says: full inner Torus closure + impedance step inward = perfect TIR (no transmission, no scattering loss).
- Per Ax 4 (Saturation): saturated boundaries can act as TIR mirrors at Regime IV (yield boundary).
- Per Ax 1 (LC Network): impedance steps cause partial reflection per Op3 (`Γ = (Z_out−Z_in)/(Z_out+Z_in)`); only at Z_out=0 or Z_in=∞ is reflection perfect.
- For a full inner shell at Period 3 p-block, gamma is finite (≈0.85 for Si: z_in=14-2=12, z_out=12-8=4, gamma=-(8/16)=-0.5; |Γ|²=0.25). NOT perfect reflection per Op3.

**The perfect-mirror claim contradicts Op3 reflection physics for Period 3.** Either there's a missing axiom-anchored mechanism that promotes partial reflection to perfect at full-shell closures, or the perfect-mirror gating is too broad and should be restricted to literal Z>=31 heavy-element cases.

### §10.11 — Diff-level reading of 046a233 (Phase C unification c=n(n-1))

`git show 046a233 -- src/ave/solvers/radial_eigenvalue.py`: relocated Op10 logic from inside `_sir_mode_weighted_base` to global scope inside `ionization_energy_e2k`.

Pre-046a233: Op10 was inside SIR with `c_intersections = 2` (Malus's law fixed: 2 crossings per radial oscillation). Only triggered for specific co-resonant boundary cases per the deleted docstring "*This shell is co-resonant with the valence soliton (adjacent n)*."

Post-046a233: Op10 in main pipeline with `c_intersections = n_shell*(n_shell-1)`. Applied to all elements with l_out>0.

The relocation broadened Op10's applicability from "co-resonant adjacent-n" to "all inner shells with l_A ≤ l_out." For Al (Z=13): pre-046a233 used c=2 fixed → small Y_loss; post-046a233 uses c=n(n-1)=2 (n_shell=2 inner) → same numerical c but applied at different gating, yielding +0.43 IE shift.

87b4114 then changed `c_intersections` formula from `n_shell*(n_shell-1)` to `l_barrier*(l_barrier+1)`. For Al/Si with l_barrier=1, l_barrier*(l_barrier+1) = 2 — same numerical value as n_shell*(n_shell-1) for n=2. So the c-formula change in 87b4114 doesn't affect Al/Si numerically; the spillover is from the Y_loss=0 perfect-mirror gate (Change C above).

### §10.12 — Surgical-fix prescription (Rule 16 — questions for Grant)

Per Rule 16 (ask Grant fundamental physics questions when corpus + engine conflict), three plumber-physics questions emerge from the diff reads:

**Q1 (7fa60b7 Change A — `_z_net` form):** Which form of effective nuclear charge is corpus-canonical AVE physics?
- Form (i): σ_n(r) from Helmholtz CDF, derived as the standing-wave-amplitude integral on the K4-LC network in continuum limit. Old code, OLD docstring chains explicitly through Ax 1 + Ax 2.
- Form (ii): step function at Bohr radii, literal-lattice discretization. New code, NEW docstring claims Ax 3 dictates this without showing operational chain.
- Empirical: form (i) reproduces 0401388 manuscript precision (±0.008%); form (ii) drifts 6/8 affected Period 1-3 elements away from CODATA.

**Q2 (7fa60b7 Change B — angular reactance form):** ℓ(ℓ+1)/r² (Laplacian eigenvalue) or ℓ²/r² (Ax-2 winding-number squared)? Both are corpus-anchorable; current code uses ℓ². For ℓ=0 it doesn't matter; for ℓ≥1 it halves/two-thirds the centrifugal barrier.

**Q3 (87b4114 Change C — perfect-mirror at full-shell + gamma<0):** Is the polar-conjugate-mirror claim (Y_loss = 0 at `is_full_shell and gamma<0`) physically correct, or should it be restricted to literal Z≥31 heavy-element cases? Per Op3, gamma=-0.5 at Si is partial (|Γ|²=0.25), not perfect. The perfect-reflection gate may be too broad.

### §10.13 — Forward direction with Grant adjudication

Once Q1/Q2/Q3 adjudicated, surgical fix shape:

- **If Q1 = (i):** revert `_z_net` change in 7fa60b7; keep angular-reactance change conditional on Q2.
- **If Q1 = (ii):** the discrete-step formula needs additional sophistication (e.g., transition-zone width, per-shell Bohr-radius scaling factor, or different impedance-step formula). Tuning work.
- **If Q2 = ℓ(ℓ+1):** revert that change in 7fa60b7. Also implies Op10 c_intersections returns to ℓ(ℓ+1) form (where 87b4114 currently has it for the wrong reason).
- **If Q2 = ℓ²:** keep, but ensure all centrifugal-barrier instances are consistent (currently mixed across the file post-7fa60b7).
- **If Q3 = perfect-mirror correct:** keep 87b4114 broadly, accept Period 3 drift as physics; manuscript table needs update.
- **If Q3 = restrict to Z≥31:** narrow the gate to `mirrored_away` only (drop the `or (is_full_shell and gamma<0)` clause); Period 3 returns to pre-87b4114 values.

**Most rigorous AVE-engineering-axiom-compliant path forward:** Grant adjudicates Q1/Q2/Q3 in plumber-physics terms (one paragraph each); surgical commits land per adjudication; full Z=1-14 sweep re-verifies; manuscript table either pins to refined HEAD or stays at `0401388` per outcome.

The empirical bisection has narrowed the question from "manuscript-vs-code drift" (vague, large surface) to "three specific axiom-form questions about ABCD-cascade screening, centrifugal-barrier eigenvalue form, and full-shell TIR boundary condition" (sharp, code-anchored, plumber-physics-tractable).

[note: orphaned duplicate §9.6/§9.7 sections previously appeared here from an earlier draft state; superseded content is at §9.6 (line 238 "drift is purely post-2026-04-09") and §9.7 (line 253 "Provenance now-fully-resolved"). Removed as part of doc cleanup.]

### §10.14 — Q2 empirical sweep (per Grant 2026-04-30 directive — pre-adjudication test)

Auditor and Grant requested empirical Q2 test before commitment. **The sweep surfaced unexpected codebase state: HEAD already has MIXED ℓ-eigenvalue forms.**

**Pre-test grep at HEAD (`grep -n "l_out \* (l_out + 1)\|float(l_out)\*\*2\|float(l)\*\*2\|l \* (l + 1)" radial_eigenvalue.py`):**

| Line | Function | Form | Source |
|---:|---|---|---|
| 316 | `_radial_envelope` (V_centrifugal) | ℓ(ℓ+1) | (pre-7fa60b7, intact) |
| 427 | wavenumber from E_J | ℓ(ℓ+1) | (pre-7fa60b7, intact) |
| 546 | `_sir_mode_weighted_base` | ℓ(ℓ+1) | f23ec7b reverted from 7fa60b7's ℓ² |
| 637 | `_radial_ode` (RK45 integrand) | ℓ² | 7fa60b7, NOT reverted by f23ec7b |
| 715 | `_abcd_section` | ℓ² | 7fa60b7, NOT reverted by f23ec7b |
| 1486 | `_direct_ODE_eigenvalue` | ℓ(ℓ+1) | f23ec7b reverted from 7fa60b7's ℓ² |

f23ec7b ("Re-implement 3D Helmholtz l(l+1) constraints mapping Z=1-30 convergence natively") **partially reverted 7fa60b7** — restored the eigenvalue-determining sites (546, 1486) to ℓ(ℓ+1) but left the integration-only sites (637, 715) at ℓ². The current HEAD reflects this partial revert. **§10.6's verdict on 7fa60b7 needs amendment: 7fa60b7 was partially reverted by f23ec7b for the IE-determining path; the residual ℓ² remnants at 637+715 are not load-bearing for IE.**

**f23ec7b commit comment (verbatim from line 543-545 at HEAD):**
> *"Centrifugal reactance strictly maps the 3D Spherical Helmholtz Harmonic Eigenvalue mapping l(l+1) bounds geometrically, fully accounting for acoustic LC resonance volumes mapped natively across the vacuum grid without utilizing probabilistic QM assumptions."*

Per this comment, ℓ(ℓ+1) is claimed by f23ec7b as **AVE-native** (acoustic LC resonance volumes on the vacuum grid), explicitly *not* a QM-imported SO(3) Casimir. This contradicts 7fa60b7's framing that ℓ² is winding-native and ℓ(ℓ+1) is QM-imported. **Both commits are by Grant; the codebase contains both axiom positions iterated in Apr 2026.**

**Test 1 — flip the remaining ℓ² sites (637, 715) to ℓ(ℓ+1):**

| Z | Q2-test1 (637+715 flipped) | vs HEAD |
|:---:|:---:|:---:|
| 1-14 | identical to HEAD within 0.001% | ≈0 |

**Conclusion:** sites 637 + 715 are NOT load-bearing for `ionization_energy_e2k(Z)` outputs. The IE Newton search uses `_eigenvalue_condition` which calls `_direct_ODE_eigenvalue` (line 1486, already ℓ(ℓ+1)) and `_sir_mode_weighted_base` (line 546, already ℓ(ℓ+1)). The ℓ² remnants at 637+715 live in helper functions exercised by other callers (or by integration paths not gated to IE).

**Test 2 — flip the eigenvalue-path sites (546, 1486) FROM ℓ(ℓ+1) TO ℓ²:**

| Z | Q2-test2 (546+1486 flipped to ℓ²) | vs HEAD |
|:---:|:---:|:---:|
| 1-12 | identical to HEAD within 0.001% | ≈0 |
| **13 Al** | **9.1510 eV** | **+37.8%** ⚠ catastrophic |
| **14 Si** | **12.0540 eV** | **+36.6%** ⚠ catastrophic |

**The eigenvalue-path ℓ(ℓ+1) at HEAD is what prevents Al/Si from blowing up to +50% errors vs CODATA.** Switching to ℓ² catastrophically breaks Period 3 p-block (Al/Si). All other elements (Z=1-12) unaffected.

### §10.15 — Q2 closure: ℓ(ℓ+1) is empirically + axiomatically correct at the eigenvalue path

**Three reads of the result:**

1. **f23ec7b's framing is corpus-canonical (current HEAD comment):** ℓ(ℓ+1) is the AVE-native acoustic LC resonance volume eigenvalue, NOT a QM-imported quantity. The shape happens to match the SO(3) Casimir but the physics is substrate-derived. Per this read, Q2=ℓ(ℓ+1) at all sites; flipping 637+715 for code consistency is a low-priority hygiene fix.

2. **Both forms are partial:** ℓ² is winding-squared (topological invariant per Ax-2), ℓ(ℓ+1) is the operator eigenvalue at the radial Schrödinger boundary. Different physics. The empirical agreement of ℓ(ℓ+1) at the eigenvalue path means that's the load-bearing centrifugal-barrier form for atomic IE; ℓ² may be load-bearing elsewhere (e.g., higher-l excitations, free electrons, plasma).

3. **Mixed state is intentional:** the radial_ode/abcd_section may target different physics (e.g., dispersive propagation, plasma-soliton extension) than the IE Newton search. Different physics, different operator forms. The mix is a feature, not a bug.

**Most defensible position (per Rule 16 + auditor's "substrate-native erosion" pattern):** the f23ec7b commit comment's claim that ℓ(ℓ+1) is corpus-canonical-substrate-native is the canonical AVE position for the IE-determining path. **Q2 effectively closes: keep ℓ(ℓ+1) at the eigenvalue path** (already at HEAD via f23ec7b revert).

The remaining ℓ² sites at 637 + 715 don't affect IE values; whether to flip for code consistency is a low-priority hygiene question, separate from manuscript-table reproducibility.

### §10.16 — Adjudication state post-Q2-sweep

| Question | Status | Decision basis |
|---|---|---|
| **Q1** (Helmholtz CDF vs step at Bohr) | **Adjudicated by Grant 2026-04-30**: revert to Helmholtz CDF. | Both axiom-chain (old form has explicit Ax-1+2 derivation; new form claims Ax-3 without operational chain) AND empirical (old reproduces 0401388 precision; new drifts 6/8 elements). |
| **Q2** (ℓ(ℓ+1) vs ℓ²) | **Empirically closed by §10.14-§10.15**: ℓ(ℓ+1) at eigenvalue path. | f23ec7b commit comment claims ℓ(ℓ+1) IS AVE-native (acoustic LC resonance, not QM-imported); empirical sweep confirms ℓ(ℓ+1) is necessary at sites 546+1486 (flipping breaks Al/Si by +37%). Q2 sites 637+715 not load-bearing for IE. |
| **Q3** (perfect-mirror at full-shell+gamma<0) | **Adjudicated by Grant 2026-04-30**: narrow gate to Z≥31 (or reformulate with explicit mechanism). | Op3 reflection physics gives partial reflection (|Γ|²=0.25 for Si); no axiom-stated mechanism promotes partial→perfect at full-shell closure. |

### §10.17 — Surgical-fix prescription (final, post-adjudication)

Two surgical commits land per Grant's Q1/Q3 adjudication + Q2 empirical closure:

**Surgical Commit A — revert Q1 (`_z_net` to Helmholtz CDF):**
- File: `src/ave/solvers/radial_eigenvalue.py`
- Action: restore the pre-7fa60b7 `_z_net` function with `_enclosed_charge_fraction_1s` / `_enclosed_charge_fraction_n2` CDF-based screening; restore the auxiliary functions `_enclosed_charge_fraction_1s` and `_enclosed_charge_fraction_n2` if 7fa60b7 also removed them (need to verify diff).
- Axiom basis: Ax-1 → Helmholtz solution of K4-LC network → |ψ|² standing-wave amplitude integral → Ax-2 Gauss-derived CDF σ_n(r). Direct chain.
- Empirical effect: Li/Be/Na shift back toward 0401388 values (manuscript precision restored for s-block).

**Surgical Commit B — narrow Q3 perfect-mirror gate to Z≥31:**
- File: `src/ave/solvers/radial_eigenvalue.py`, Op10 loop in `ionization_energy_e2k`
- Action: change `if mirrored_away or (is_full_shell and gamma < 0): Y_loss = 0.0` to `if mirrored_away: Y_loss = 0.0`
- Axiom basis: Op3 reflection at impedance step is partial unless |Γ|²=1. For Si at gamma=-0.5, |Γ|²=0.25; no axiom-anchored mechanism promotes this to perfect mirror absent further saturation. The Z≥31 narrowing matches `mirrored_away`'s long-distance amplification framing.
- Empirical effect: Al/Si recover from HEAD's +11% to closer to f23ec7b's +3-4% (partial; full restoration depends on whether 046a233's Op10 promotion interacts).

**Optional Hygiene Commit C — flip Q2 remaining sites for code consistency:**
- File: `src/ave/solvers/radial_eigenvalue.py`, lines 637 + 715
- Action: change `float(l)**2` → `float(l * (l + 1))` to match f23ec7b's eigenvalue-path forms
- Empirical effect: zero change to IE values (per §10.14 Test 1)
- Justification: code consistency only; eigenvalue path already correct.

**Post-surgical-commits verification:** full Z=1-14 sweep against (a) 0401388 manuscript table and (b) CODATA. Expected: Li/Be/Na within 0401388-class precision; Al/Si improved (likely not fully restored if 046a233's Op10 promotion has independent effect, which would be residual scope for further investigation).

### §10.18 — Substrate-native erosion methodology pattern (auditor 2026-04-30)

Auditor's pattern observation across the three Q's:

> *"Q1 lost a substrate-derived form for a hydrogenic heuristic. Q2 lost a winding-native form for a spherical-Laplacian fact. Q3 lost an empirical Z-threshold for an unstated mechanism. The post-0401388 refinement direction was toward QM-textbook forms and away from substrate-anchored ones — three independent commits, same drift signature."*

(Note: Q2 is more nuanced per §10.15 — the f23ec7b code comment claims ℓ(ℓ+1) IS substrate-native (acoustic LC resonance volumes), not QM-imported. The auditor's pattern still holds for Q1 and Q3, and for the 7fa60b7 → ℓ² direction within Q2.)

**A47 v11d candidate — substrate-native erosion review at PR time (auditor-lane, COLLABORATION_NOTES):** when a refactor commit replaces an axiom-chain-anchored form (with explicit derivation chain in docstring) with a different form, require explicit Ax-1...4 + Op-N derivation chain in the new docstring. If no chain provided, the refactor is "claim-without-receipt" and should be flagged for review before merge.

The three commits in this case (7fa60b7, 046a233 Op10 promotion aspect, 87b4114 Y_loss=0 broadening) all replaced anchored forms with new forms whose docstrings claim axiom-compliance without showing the operational derivation chain. The 7fa60b7 `_z_net` docstring claim ("Ax 3 dictates discrete impedance steps") had no operational chain; the original `_z_net` docstring had explicit Ax-1 → Helmholtz → Ax-2 → Gauss chain.

**Discipline rule for Grant adjudication:** A47 v11c (commit-SHA anchoring at manuscript table-generation) + A47 v11d (axiom-chain-required-in-docstring at PR time) are paired manuscript-vs-code provenance disciplines. v11c is the post-hoc detection rule; v11d is the prevention rule. Both should land in COLLABORATION_NOTES per auditor-lane handoff.

### §10.19 — Authorization needed before surgical commits

Per memory rule "flag don't fix" + "executing actions with care," surgical commits A + B modify canonical engine code (`radial_eigenvalue.py`), which has downstream physics implications beyond IE. Before proceeding:

- **Surgical Commit A (Q1 revert)**: requires explicit Grant authorization. The revert restores Helmholtz CDF screening which Grant already adjudicated as correct, but the implementation requires reading the pre-7fa60b7 function bodies and restoring them; this is non-trivial code restoration, not a single-line revert. Approach: extract pre-7fa60b7 `_z_net` + `_enclosed_charge_fraction_*` from commit `8acadcd` (or earliest commit having them) and surgically restore.
- **Surgical Commit B (Q3 narrowing)**: simpler — single-line change. Still requires authorization since it modifies canonical code.
- **Optional Hygiene Commit C**: lowest priority; can defer or skip.

**Status:** standing by for Grant's go-ahead on Surgical Commits A + B. Worktree at `/tmp/ave-at-0401388` retained for implementation work. Doc 100 §10.17 prescription is the implementation specification.

### §10.20 — Surgical Commits A + B applied per Grant directive 2026-04-30 "proceed"

**Surgical Commit A (Q1 revert):** restored pre-7fa60b7 `_z_net` Helmholtz CDF body + restored deleted helper functions `_enclosed_charge_fraction_1s`, `_enclosed_charge_fraction_n2`, `_enclosed_charge_fraction` (these were called from `_sir_mode_weighted_base:379+383` as dead references at HEAD; restoring `_z_net` requires the helpers).

**Surgical Commit B (Q3 narrow):** dropped `or (is_full_shell and gamma < 0)` clause from Op10 perfect-mirror gate. `mirrored_away` (Z≥31 long-distance amplification) preserved.

**Post-A+B sweep:**

| Z | HEAD-orig | Q1+Q3 | manuscript | gap vs ms | recovery |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 13.6057 | 13.6057 | 13.606 | -0.002% | unchanged ✓ |
| 2 | 24.3693 | 24.3693 | 24.370 | -0.003% | unchanged ✓ |
| 3 | 5.6873 | **5.7860** | 5.525 | **+4.72%** | ⚠ regressed |
| 4 | 9.1875 | 9.2793 | 9.280 | **-0.007%** | ✓ matches |
| 5 | 8.0524 | 8.0654 | 8.065 | **+0.005%** | ✓ matches |
| 6 | 11.3844 | 11.4012 | 11.406 | **-0.042%** | ✓ matches |
| 7 | 14.4351 | 14.4352 | 14.465 | -0.206% | close |
| 8 | 13.5991 | 13.5991 | 13.618 | -0.139% | unchanged (3c4870c Hopf back-EMF) |
| 9 | 17.1822 | 17.1822 | 17.194 | -0.069% | unchanged |
| 10 | 21.7891 | 21.7891 | 21.789 | +0.000% | ✓ matches |
| 11 | 5.6607 | **5.8848** | 5.071 | **+16.05%** | ⚠ regressed |
| 12 | 7.5483 | **7.9126** | 7.591 | **+4.24%** | ⚠ regressed |
| 13 | 6.6418 | 6.3648 | 5.937 | +7.21% | partial recovery (was +11.9%) |
| 14 | 8.8240 | 8.5877 | 8.147 | +5.41% | partial recovery (was +8.31%) |

**Period 2 (Z=4-10): fully recovered to manuscript precision.** All elements within ±0.21% of manuscript table. Q1 revert is the load-bearing fix for Period 2.

**Period 3 p-block (Z=13, 14): partial recovery via Q3 narrow.** Al/Si improved from +11.9%/+8.3% to +7.2%/+5.4%. Q3 was correct direction but partial — residual drift from 046a233's Op10 promotion to global scope (potential Q6).

**Period 3 s-block (Z=11, 12) + Li (Z=3): REGRESSED.** Q1+Q3 made these worse vs both HEAD and manuscript. Root cause identified as f8af2e2's additional substrate-native deletions.

### §10.21 — Root cause for Li/Na/Mg regression: f8af2e2 ALSO deleted Phase A½ + Correction B

Diff read of `git show f8af2e2 -- src/ave/solvers/radial_eigenvalue.py` reveals the "docs:" labeled commit (f8af2e2) was NOT pure docs — it deleted **two substantive substrate-native code paths**:

**Q4 candidate — `_sblock_chain_correction` (Phase A½):** complete function deletion (60+ lines). Original docstring chained:
> *Axiom 1: r_n = n²a₀/Z → γ (Bohr radius geometric mismatch); Axiom 1: Y-matrix ABCD stub: y_mutual = -csch(γ)/Z_geo; Axiom 3: S₁₁=0 eigenvalue shift → ΔE = -E/(2 N_s_in cosh²γ); ν_vac: 2/7 compressional modes → only l=0 enters the stub.*

The function applied a downward shift to s-block IE via inner-shell ABCD stub coupling per ν_vac=2/7 compressional mode count. For Li (Z=3, n_out=2, n_in=1, N_s_in=2, γ = |4-1|/(2·1) = 1.5):
> ΔE = -E_base / (2 · 2 · cosh²(1.5)) ≈ -0.045 · E_base

For Li IE ~5.78 eV at Q1+Q3 (without Phase A½), Phase A½ would shift to ~5.52 eV — matching manuscript 5.525 within rounding.

**Q5 candidate — Correction B (SIR Boundary Reflection at saturated torus):** deleted from s-block path inside `ionization_energy_e2k` (the `n_adjacent != 1` branch). Original docstring chained:
> *Axiom 2 (Gauss): Z_in, Z_out at co-resonant boundary; Op3: |Γ|² = ((Z_out−Z_in)/(Z_out+Z_in))²; Axiom 3: P_C/2 = 4πα crossing scattering; ΔE = −|Γ|² × (P_C/2) × E_base.*

For Na (Z=11, 3s¹, n_adjacent=2 with 2s²+2p⁶ inner): Z_in=11, Z_out=3, γ ≈ -0.571, |Γ|² ≈ 0.327. ΔE ≈ -0.030 · E_base. Restoring would partially close Na.

**Both deletions used "organically incorporates" hand-wavy replacements without operational axiom chains** — same pattern as 7fa60b7 (Q1) and 87b4114 (Q3). f8af2e2 was labeled "docs:" but is the third substrate-native erosion commit in the Apr-9 to Apr-11 sequence.

### §10.22 — Q4/Q5 surfaced for Grant adjudication (Rule 16)

**Q4 — Phase A½ s-block compressional chain coupling:** does Li/Na/s-block IE include a corpus-canonical correction from inner s-resonators acting as ABCD stubs at the outer s-cavity inner port (per deleted `_sblock_chain_correction` + ν_vac=2/7 compressional mode derivation), or is Phase A "organically incorporating" this?
- f8af2e2 commit comment claims organic incorporation without chain.
- Empirical: deleting Phase A½ produces +5% drift on Li (Z=3); restoring closes Li to manuscript precision.

**Q5 — Correction B s-block Op3 reflection at saturated inner torus:** does outer-s IE include corpus-canonical |Γ|² × (P_C/2) correction at adjacent inner shell's p-subshell saturated torus boundary (per deleted Correction B + explicit Op3 + Axiom 3 chain), or is Phase A "organically incorporating" this?
- f8af2e2 deleted with same hand-wavy claim.
- Empirical: deleting Correction B contributes to +14% Na drift post-Q1; restoring partially closes Na.

**Pattern observation hardens (auditor's "substrate-native erosion"):** five deletions/promotions across Apr-9-11 commits, all with explicit Ax-N+Op-M chains in original docstrings replaced by "organically" claims without operational chains. The pattern is reproducible, quantitatively measurable, and corpus-detectable. **A47 v11d (axiom-chain-required-in-docstring at PR time) is now load-bearing-rule-with-empirical-evidence, not candidate.**

### §10.23 — Q4 + Q5 applied per Grant authorization 2026-04-30 "yes proceed with 4/5"

**Surgical Commit C (Q4 — Phase A½ restoration):**
- Restored `_sblock_chain_correction` function (Ax-1 + Ax-3 + ν_vac=2/7 chain) before `ionization_energy_e2k` definition.
- Restored Phase A½ call site in `ionization_energy_e2k`'s `if N_out <= 1:` early-return path.

**Surgical Commit D (Q5 — Correction B restoration):**
- Replaced the `pass` stub in `ionization_energy_e2k`'s s-block `else:` branch (`n_adjacent != 1` case) with the full Correction B Op3 reflection block.
- Op3 + Ax-2 + Ax-3 chain restored: `ΔE = -|Γ|² × (P_C/2) × E_base` where `|Γ|² = ((Z_out-Z_in)/(Z_out+Z_in))²` and `P_C/2 = 4πα`.

**Post-A+B+C+D sweep (12 of 14 elements within manuscript precision):**

| Z | manuscript | new | gap | status |
|:---:|:---:|:---:|:---:|:---:|
| 1 H | 13.606 | 13.6057 | -0.002% | ✓ |
| 2 He | 24.370 | 24.3693 | -0.003% | ✓ |
| 3 Li | 5.525 | **5.5246** | **-0.008%** | **✓ closed** |
| 4 Be | 9.280 | 9.2793 | -0.007% | ✓ |
| 5 B | 8.065 | 8.0654 | +0.005% | ✓ |
| 6 C | 11.406 | 11.4012 | -0.042% | ✓ |
| 7 N | 14.465 | 14.4352 | -0.206% | ✓ |
| 8 O | 13.618 | 13.5991 | -0.139% | ✓ |
| 9 F | 17.194 | 17.1822 | -0.069% | ✓ |
| 10 Ne | 21.789 | 21.7891 | +0.000% | ✓ |
| 11 Na | 5.071 | **5.0703** | **-0.014%** | **✓ closed** |
| 12 Mg | 7.591 | **7.5901** | **-0.011%** | **✓ closed** |
| 13 Al | 5.937 | 6.3648 | +7.21% | residual |
| 14 Si | 8.147 | 8.5877 | +5.41% | residual |

**Period 1 + Period 2 + Period 3 s-block: fully restored to manuscript precision.** Maximum gap across 12 elements: 0.21% (N).

**Residual Al/Si drift is isolated to Q6 (046a233's Op10 promotion):** the Period 3 p-block elements have residual drift attributable to 046a233's promotion of Op10 from inline-SIR-co-resonant-only-c=2 to global-pipeline-c=l(l+1). Q1/Q3/Q4/Q5 were not expected to close Period 3 p-block; only Q6 adjudication will.

### §10.24 — Q6 candidate (Period 3 p-block residual; pending Grant adjudication)

**Q6 — Op10 inline-co-resonant vs global-pipeline:** does Op10 junction projection apply only at the co-resonant inner-shell boundary (per pre-046a233 inline form with c=2 fixed crossings) or to all l>0 cases globally (per post-046a233 form with c=l(l+1) or n(n-1))?

- Pre-046a233: Op10 inside `_sir_mode_weighted_base`, gated to co-resonant boundary case only, c=2 (Malus's law fixed crossings per Op3→Op10 bridge in original docstring).
- Post-046a233 + 87b4114: Op10 in main `ionization_energy_e2k` pipeline, c=l(l+1), applied to all elements with l>0.
- Empirical: 046a233 caused +0.43 jump for Al/Si. Reverting to inline form would close Al to within 0.21% of manuscript and Si similarly.

**Pattern continuation:** 046a233's docstring claimed "E_base was already natively scattered by the Torus Knot boundary in the main pipeline" — same "organically incorporates" hand-wave pattern as 7fa60b7 / f8af2e2 / 87b4114. Same A47 v11d signature.

**Standing by on Q6.** If you adjudicate Q6 = revert to inline-co-resonant form, the surgical fix will close Period 3 p-block, completing 14/14 manuscript-precision recovery.

### §10.25 — Net result of restoration arc

The substrate-native erosion arc identified five Apr-2026 commits replacing axiom-chain-anchored forms with "organically incorporates" hand-waves:
1. ✅ 7fa60b7 `_z_net` Helmholtz CDF (Q1 — restored)
2. ⏸ 046a233 Op10 inline → global (Q6 — pending)
3. ✅ f8af2e2 Phase A½ deletion (Q4 — restored)
4. ✅ f8af2e2 Correction B deletion (Q5 — restored)
5. ✅ 87b4114 perfect-mirror broadening (Q3 — narrowed)

After 4 of 5 surgical fixes (A+B+C+D), 12/14 elements at manuscript precision (matching the `0401388` snapshot to ≤0.21%). Q6 (046a233 revert) would close the remaining 2/14.

This empirically validates the auditor's "substrate-native erosion" pattern and quantifies A47 v11d's load-bearing-rule status: restoring axiom-chain-anchored forms reproduces 0401388 manuscript precision to <0.21%; replacing with hand-waves degraded by 5-15%. The PR-time discipline rule (axiom chain required in docstring) would have prevented this drift.

