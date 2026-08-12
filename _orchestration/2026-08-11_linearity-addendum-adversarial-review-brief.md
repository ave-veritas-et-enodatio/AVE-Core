# Review brief — adversarial pass on the §9 linearity addendum (2026-08-11)

**Target:** PR #955, `research/2026-08-11_gravity-linearity-audit_result.md` **§9 ONLY**
(+ driver legs **R10–R12** in `research/drivers/gravity_linearity_audit_number_check.py`).
**Out of scope:** §1–§8 (the license map) — reviewed as an ordinary records PR, not here.

**Why this brief exists.** §9 is **chat-walk algebra the lane ran on itself in conversation** with no
second reader. It now carries: a candidate resolution of the audit's central three-clock collision, a
mechanism for the `r_s`-vs-`r_sat` split, a proposed repair to the stated mechanism of **two Grant
rulings**, and a proposed third axis for the W2 carve. **That load is far past what conversational
algebra earns.** §9 is tagged UN-AUDITED at every site; this pass decides whether any of it survives.

**Posture: DEFAULT-TO-REFUTED.** A finding is REFUTED unless the reviewer can state, in the corpus's
own words at file:line, why it stands. Per-finding verdicts `CONFIRMED / DOWNGRADED / REFUTED`.
No aggregation, no overall grade.

**★ The single load-bearing claim.** Everything else in §9 hangs from **§9.2's ORTHOGONALITY CLAIM**:

> *"Co-scaling moves the LC product; bond-breaking moves the ratio. `Z` is blind to co-scaling and
> sensitive to bond-breaking, so `Γ` — not frequency — is the discriminator between the two clocks."*

**If it falls, §9.1's repair proposal, §9.2's two-radii mechanism, and §9.3's relational/absolute axis
all fall with it.** Attack it first, and if it dies, stop and report — do not rescue.

---

## Lenses

**L1 — SUBSTRATE-STENCIL (run first; the null here would be a disabled-flag artifact).**
The orthogonality claim is derived on an **idealized two-element lumped tank**. The substrate is a
graded K4 network with its own `ρ(A)` treatment. Does `Z` stay blind to co-scaling **on the substrate's
own stencil**, or is that blindness an artifact of the two-element idealization?
⚑ **Mandatory consume, do not re-litigate:** `saturating-modulus-and-backreaction.md`:194 —
the Grant-fenced **sign-relativity declaration** (wall-taxonomy §10, PR #869) rules any signed `Γ`
**computed-not-chosen from the branch-derived indicial wall row**, and records
`c = √(K/ρ) → 0` **with** `Z = √(Kρ) → ∞` via `ρ_eff = ρ₀/S³`. **§9's two-element tank gives
`Z → 0`.** Reconcile or refute — and if the graded-`ρ` treatment inverts §9's sign, say so plainly.
The cross-grade combine rule is **canon-OPEN** (`axiom-register.md`:190,:232); stay inside the fence.

**L2 — THE ORTHOGONALITY CLAIM, head-on.** Construct a counterexample: a substrate-legal perturbation
that moves `Z` **without** breaking a bond, or breaks a bond **without** moving `Z`. Either kills it.
Check specifically whether `ε₁₁`-grading and `A`-grading are genuinely independent knobs in canon or
are two names for one thing. Also test the ASYM row (`graded-network-response.md`:148, `S_ε<1, S_μ=1`,
`Z = Z₀(1−A²)^{−1/4}` → **∞**) against §9's bond-break (`Z → 0`): §9 asserts these are different
physics (static-E bias vs bond rupture). **Is that distinction real, or is §9 quietly inventing a
second ASYM branch with the opposite sign?**

**L3 — THE `m = 1/√g₀₀` IDENTIFICATION.** §9.1 finds `m = 1 + ε₁₁/7` reproduces the observed slope-1
redshift and `m² = n_temporal`. Is that **derived** or **back-fitted to the answer**? The lane
solved for the `m` that gives the known result — state whether anything **independently** fixes `m`,
or whether this is calibration wearing a mechanism's clothes. ⚑ Apply the coincidence-tell discipline:
`½`/`¼`-style over-determination and "it comes out exactly right" are tells, not receipts.

**L4 — THE RULING-REPAIR PROPOSAL.** §9.1 proposes substituting `m = 1/√g₀₀` for `√S` in the stated
mechanism of the **2026-06-29 SUBTRACT ruling** (`backreaction.md`:126–130) and the **2026-07-12 X44
Komar weight** (`backreaction.py`:14–17, operative code). Verify: (a) does the substitution actually
preserve each ruling's **verdict**, or does it change a number the rulings' downstream consumers rely
on? (b) X44's weight is **live in the engine** — what breaks if it changes? (c) is proposing a repair
to a Grant ruling inside a records-class lane a **scope violation**, even flagged as "proposed, not
applied"? Rule on the process question as well as the physics.

**L5 — GLOBAL/LOCAL AND THE `Γ_EM = 0` LEG.** §9.3's relational-vs-absolute axis leans on
`graded-network-response.md`:136–137 (*"gauge-relative; only spatial gradients of `A₀` are
observable"*). Does that INVARIANT-S2 statement bear the weight §9 puts on it, or is §9 promoting a
gauge remark into an equivalence-principle claim? Separately verify the three `Γ_EM = 0` cites
(`einstein-field-equation.md`:49, `lattice-extreme-bh-rationality.md`:37, `backreaction.md`:62)
actually say what §9 says, **and** that "EM bonds never break" is a legitimate reading of them rather
than a gloss.

**L6 — SECTOR OWNERSHIP OF `μ`.** §9 works under Grant's chat ontology **μ = fabric / ε = bonds**.
§9.4 flag 2 says this is *not* promoted to canon. Verify that no §9 statement smuggles it in as a
sector assignment, and check it against canon's declared roles for `μ` (circulation-keyed relativistic
inductor; **sign/spin selector**). If §9's conclusions require the fabric reading to be *true*, say so
— that converts flag 2 from a caveat into a dependency.

**L7 — QUOTE + NUMBER GATE.** Every verbatim span in §9 re-read at HEAD, byte-exact. Every numeral
re-derived independently of `R10–R12` (do **not** just re-run the lane's driver — that is one engine,
not two). Confirm `f(S)`'s exponent is genuinely **left open** and that §9 nowhere silently settles the
VACATED Op16 question (`operators.md` §8 FLAG-CEFF-CITE).

---

## Fences

- **Verify-not-derive.** Refute or confirm; do **not** repair §9, and do **not** build a better version
  of it. A dead claim is banked dead.
- **No edits** to any KB leaf, axiom file, register, ruling, or manuscript file. §9 is a records-class
  addendum; this pass adds a review record, nothing else.
- **Frozen criteria travel verbatim** or as file:line. The orthogonality claim is quoted above in full
  precisely so no paraphrase of it becomes the pivot.
- **Consensus-bias check before flagging §9 as weak:** ask whether standard practice does the same
  thing and gets a pass (a lumped-element idealization is ordinary; "it's idealized" alone is not a
  refutation — say what the idealization *breaks*).
- **Stop-and-ask applies.** Two-attempt cap; a clean STUCK-POINT report beats a spun-out verdict.
- **PR stays `[DO-NOT-MERGE]`.** Only Grant merges.

## Outcome grammar (frozen)

Per lens, per finding: **`CONFIRMED`** (survives; state why in corpus words) /
**`DOWNGRADED`**(name the surviving narrower claim) / **`REFUTED`**(state the killing fact).
Then one disposition for §9 as a whole, from exactly this set:

| verdict | meaning |
|---|---|
| `CANDIDATE-SURVIVES` | orthogonality CONFIRMED; §9 may be routed for canonical propagation as a **proposal** |
| `CANDIDATE-NARROWED` | orthogonality DOWNGRADED; **name the surviving scope** |
| `CANDIDATE-DEAD` | orthogonality REFUTED; §9 is banked as a **negative**, §7 reverts to STUCK-POINT |
| `BLOCKED-ON-FENCE` | L1's graded-`ρ` reconciliation cannot be done without ruling the open cross-grade fork → **back to Grant** |

**If `CANDIDATE-DEAD`: §7's stuck-point stands unchanged and that is a clean, useful outcome — the
license map (§1–§8) does not depend on §9 in any way.**

---

**How to launch.** Not auto-dispatched — Grant launches (his call on model + effort). The
`ave-adversarial-pr-review` skill fits this shape directly:
`args = {pr: 955, context: "§9 only; default-to-refuted; orthogonality is the load-bearing claim",
lenses: [L1…L7 above]}`. L1 and L2 are the ones worth the most compute; L7 is mechanical.
