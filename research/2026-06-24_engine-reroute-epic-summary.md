# The Engine-Reroute Epic — Reflective Summary

**Status:** CONSISTENCY-class throughout. No chord claimed. Auditor-lane synthesis; all load-bearing nodes grep-verified at `/tmp/pswind` HEAD `10407d8e` (branch `analysis/engine-phase-space-winding`) this turn.

**Grant-ratified conclusion:** the electron is **two-natured** — a DYNAMICAL energy-bound MASS (A1 longitudinal cavity, does work) + a STATIC topological CHARGE (the (2,3) Clifford winding = Link, reactive). Both internal *dynamical* loci tested NEGATIVE (real-space eigensolve #415 + phase-space coupling #59). `charge = Link(∂Ω,F)` STANDS. The AVE-distinct chord lives ONLY in forward predictions.

---

## 1. The Arc

The reroute ran a staged engine campaign to ask one question: *does the (2,3) charge winding re-emerge as a live, energetic, mass-pinning mechanism — or is it a static texture the seed carries?*

| Stage | Test | Verdict | Evidence (verified this turn) |
|---|---|---|---|
| S1 | winding DOF host on the native lattice | host exists | `research/2026-06-24_engine-s1-winding-dof_result.md` |
| S2 | conservative A1↔ω lock (H_couple), no leak | (precursor to S3) | `research/2026-06-24_engine-s2-hcouple_result.md` |
| Stage-2 | bulk A1 self-trap on native lattice | **DISPERSES** (mass alone does not confine) | `research/2026-06-24_engine-stage2-native-cage_result.md` |
| S3 | Γ=−1 cavity pins the dispersing A1 core | **DISPERSE-FALSIFIED** | `research/2026-06-24_engine-s3-cavity-pinning_result.md` |
| #415 | coupled eigensolve — both sectors present on ONE eigenstate | gate-(d) **FAIL**: winding bled out, `bw_on_torus=0.0001` | `research/2026-06-24_engine-coupled-eigensolve_result.md:69` |
| #59 | phase-space coupling-winding orbit | **BREAK**: orbit reads (−5,−5)=(1,1)-class carrier-lock, not (2,3) | `research/2026-06-24_engine-phase-space-winding_result.md:18-23` |

**Two terminal NEGATIVES, both clean, each with a single named mechanism:**
- #415 tested the WRONG locus three ways — real-space (vs phase-space), V_snap-mass-core (vs V_yield-charge-front), static-eigenstate (vs dynamic-orbit) — and the (2,3) bled off the bound mass mode.
- #59 corrected all three (phase-space + V_yield-front + dynamical-orbit) and STILL read NEGATIVE: the only surviving integer is the **oscillator carrier ratio**, not a topological charge.

The discipline caught its own scope-error and re-ran clean. This is the methodology working, not rationalizing a result.

---

## 2. The Two-Natured Electron + the No-Work Principle

**The two natures are the two substrate sectors, orthogonal, not two standard nouns riding a missing DOF:**
- **MASS = A1 longitudinal dilatation breather** (`master-equation.md:20`, PR#260) — DYNAMICAL: it seeds, evolves, slosh-exchanges; the time-orbit lives here. This is the work-doing C↔L breather recovering E = m_e c² (`resonant-lc-solitons.md:23`). **Untouched by the negatives, and the A1 mass cavity EXISTS** (fork-b ECHO, recovered as the eigensolve HALT gate `forkb_omega=2.839` on the cold-cage 2.87 anchor, `engine-coupled-eigensolve_result.md:65`).
- **CHARGE = transverse Cosserat (2,3) micro-rotation winding = Link(∂Ω,F) ∈ ℤ** (`charge_quantization.py:258`) — a real-space boundary linking integer, topologically protected (invariant under continuous deformation, jumps on unwind). **STANDS, independently grounded, touched by neither negative.** The ~18% helicity-integral caveat (measured 1.08 vs p·q=6 at R≈7) is honestly carried at `charge_quantization.py:341`, not papered over.

**Scope of the negatives:** they close the *JOINT* mass+charge dynamical locus — the (2,3) does not re-emerge as a conserved dynamical time-orbit OR survive on a coupled bound eigenstate. They do NOT touch either sector's independent existence.

**The no-work principle — handle with care (see §5).** Grant's framing is that the static charge "does no work." The corpus-native statement is **reactive / lossless** (Axiom 3: Γ→−1 confined mode, Im(ω)=0, intrinsic Q→∞, `resonant-lc-solitons.md:100`). The phrase "no work" does **not appear** in any result/conclusion doc or in VCA ch1 (grep-confirmed ZERO hits this turn). The substrate-native property of the charge sector is *reactance/losslessness*, and the no-work statement is a defensible CONSISTENCY-class *consequence* of that — but it must be pinned to the corpus phrasing or given a substrate definition (work = ∮ across a dissipative port = 0 because Im(ω)=0) before it propagates into the KB. Do not let an interpretive gloss become a canon claim.

---

## 3. What Was Learned

**(1) The 3-axis locus-lens is real and load-bearing.** A null is scoped by *which locus*: real-space vs phase-space; V_snap-mass-core vs V_yield-charge-front; static-eigenstate vs dynamic-orbit. The prereg names all three explicitly as the errors #415 made (`engine-phase-space-winding_prereg.md:7`). Re-testing on the corrected loci and STILL reading NEGATIVE is what makes this a clean negative rather than an artifact.

**(2) The carrier-vs-charge distinction is the genuine new finding.** The dynamical orbit's winding integer **tracks the carrier ratio under detuning** (1:1→0.93, 2:3→0.65, 3:2→1.54, 1:2→0.48; CI-gated at `test_phase_space_winding.py:147-161`, `|ratio − 0.667| < 0.15`). A topology-protected charge could NOT do this. Therefore the orbit winding is the **LC oscillator (A1/T2 carrier-frequency Lissajous) ratio**, NOT the topological charge. The (2,3) the seed carries is a static geometric Clifford-torus texture.

**(3) The no-work principle is vindicated by the data, not asserted onto it.** Charge = Link(∂Ω,F) is a static boundary linking integer; the dynamical homes are closed; the static home is untouched and independently grounded. "static" here = *deformation-invariant integer, no time-orbit* — a frame-independent invariant-vs-orbit distinction, NOT a Galilean frame artifact. The prompt's implicit worry that "static" is a frame statement is unfounded: it is `Link(∂Ω,F)` (invariant) vs `θ(t)=2φ+3ψ` (conserved time-orbit), frame-independent on both sides (`engine-phase-space-winding_prereg.md:7`).

---

## 4. Methodology Wins + Honest Standing

**Methodology wins (verified):**
- **F4 self-deception caught.** "Two independent reads agree" was agreement-by-construction — unwrap and circulation are the SAME wrapped-increment estimator. The post-audit downgrade (`10407d8e`) correctly re-anchored the verdict on the detuning discriminator. Verify-before-cite operating at the load-bearing level; a numerical claim de-rated when found non-independent (A47 v11c).
- **Stranded-merge #413 caught.** `25d28e07` merged into the dead S3 branch (`020875b0`), `git merge-base --is-ancestor 25d28e07 main` → **NOT an ancestor of main** (verified this turn). The immune system caught a git-topology error before it silently dropped the eigensolve content; re-landed via `7dee6859`.
- **Over-reach corrected.** The "engine-exhausted" over-reach and the Planck-anchor route were both recorded as Grant-corrected redirections (session-trace #3, #6), with the corrected conclusion carried forward consistently.
- **Reproducibility.** All 10 phase-space tests pass live at HEAD (10 passed, this turn). The BREAK verdict is reproducible.
- **α-clean verdict path.** Import-time guard triad blocks ALPHA/Q_TANK/V_SNAP/ELECTRON/KAPPA_CHIRAL_ELECTRON (`phase_space_winding.py:87-92`); reads are pure `arg()`; Q=137 stays EMPTY. Satisfies consistency-vs-emergence: a null that does not depend on `ave.core.constants` for its verdict.

**Honest standing (symmetric-standard, no rescue, no over-claim):**
- **CONSISTENCY-class throughout.** Both negatives are α-free on the verdict path; the channel-impedance-mismatch Q target stays EMPTY (cold-cage Q≈30.8 ≠ 137, `resonant-lc-solitons.md:124`); the negatives do NOT refill that slot.
- **charge = Link STANDS** (un-walked-back, Rule 12: retract-not-refill correctly applied — no successor hypothesis refilled the falsified mutual-pinning slot).
- **mass = A1 untouched**, and the A1 mass cavity EXISTS.
- **No physics over-reach.** Every BREAK/DISPERSE/FAIL verdict has a single named mechanism (carrier-lock; shared stiff-core stiffness; winding-bleed), energy-certification (conserved to 2.2e-10; pumped control trips the bleed gate), and a live negative control.
- **The AVE-distinct chord lives ONLY in forward predictions** — all carrying `experimental_solidity: null` across 299 clm- nodes (`forward-prediction-register.md:13-29`); internally peer-with-SM. Held to the SM bar: SM imports α/Yukawas/Λ/charge-quantization un-derived too — the object-level knife (smuggled fits, failed validate-on-known, SM's predictive lead) stays sharp, but the two-natured decomposition is not penalized as "comedown" for an echo SM also carries.

---

## 5. Terminology / Vocab + VCA Reconciliation Summary

**Vocab register (`manuscript/ave-kb/common/vocabulary-register.md`):** the phase-space-Clifford-torus-NOT-real-space half is ALREADY canon (`def-3638f2` winding `:228`; `CLAUDE.md:22` knot/trefoil disambiguation). The NEW epic attributes — STATIC / =Link(∂) / reactive-no-work — are ABSENT (grep: 0 hits). The carrier-vs-charge distinction is ABSENT from the `carrier` node (`def-a9eef5`, status: ambiguous, `:111-123`). "two-natured" / "dual-nature" return ZERO hits. The closest anchor (`def-5d2b8a` the-3, `:509`) says "two objects, not one" (A1⊥T2) but does NOT assign mass=DYNAMICAL / charge=STATIC. **No superseded text to retract in these two files** — they already hold the correct non-superseded forms (`def-cf1srf` is status OPEN; `CLAUDE.md:22` says (2,q)=phase-space-not-real-space).

**VCA canon (`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/`):** the grade-level decomposition is ALREADY canon and ALREADY matches the reframe — mass=Z_bulk/A1, charge=Z_shear/T2 (`resonant-lc-solitons.md:118-120`). The reframe re-expresses ~70%, adds ~30% (the explicit pure-reactance-no-work label on the charge boundary; the carrier(port)-vs-charge(boundary)-vs-mass(store) role labels). **One BLOCKING fork lands directly on the reframe** (§ below): the V_yield sector attribution. See `vca_reconciliation` for the file:line map.

---

## 6. Where Next

1. **Land this summary** as the epic doc home (recommend `research/2026-06-24_engine-reroute-epic-summary.md`) — implementer-lane write.
2. **Rule-12 the stale synthesis doc** (`research/2026-06-24_electron-vacuum-state-synthesis.md`, committed 11:10, PRE-DATES the S3 falsification 12:39 and the phase-space BREAK 15:30): add a 🔴 header demoting "mutual-pinning OPEN" (lines 6, 39, 79) to "tested NEGATIVE in both loci." Preserve body; do NOT refill the slot. This is the auditor-lane signature catch (stale-belief propagation).
3. **Grant physics call (BLOCKING, gates the VCA update):** the V_yield sector-attribution fork (KB-A1 vs engine-εeff vs reframe-T2). Flag-don't-fix.
4. **Vocab + VCA canon-propagation** gated on (3) and the integration scoping (`wwhfdbtcy`) + the #60 pass.

---

*Operating in auditor lane; recommendations require implementer execution.*
