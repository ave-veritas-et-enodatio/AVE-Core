# AUDIT RESULT — the AUTONOMOUS-HARMONIC-BALANCE lens (PR #1019): the existence criterion is DEAD as posed

**Date:** 2026-08-26 · **Branch:** `research/2026-08-26-hb-lens-audit-result` · **Base:** `origin/main` @ `a3f4fef7`
**Object under audit:** [`research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`](2026-08-25_autonomous-harmonic-balance-lens_RECORD.md) (PR #1019, MERGED)
**Charter:** §6 of that record, `:151-167` — seven items **A1–A7** plus two required checks
**Routing item:** [`_orchestration/open-items/2026-08-25-autonomous-hb-lens-audit.md`](../_orchestration/open-items/2026-08-25-autonomous-hb-lens-audit.md)

---

## §0 — VERDICT

> # `THE EXISTENCE CRITERION IS DEAD AS POSED`
>
> ### The lens is repairable **only as a SELECTION test, never as an EXISTENCE test.**
>
> "Does a nontrivial source-free solution exist" cannot return NO. Existence is
> generic: continuous one-parameter families at machine-zero residual
> (`r_auto ~ 5e-15`), in **every** winding sector, **delocalized** across 45–85 %
> of the lattice, running continuously down to `A→0` where they **are** the cold
> empty lattice's own linear eigenmodes.

### ⚠ FIRST — THE AUDIT'S OWN INSTRUMENT WAS BROKEN, and it broke in the dangerous direction

The verify phase's roll-up computed each finding's status as
**`refuters >= ceil(total/2)`**. With two adversarial lenses per finding that
makes **one refuter equal REFUTED**. It stamped **all six findings REFUTED**
when **five were 1-of-2 SPLITS**, and in **four** of those five the *reproduce*
lane — the lane that ran code against the branch tip — voted `refuted=false`
with `confidence: high`.

**Had the orchestrator acted on the status column, four findings that survived
read-and-run would have been discarded.** This is a defect in the audit
*instrument*, not in the lens, and it is recorded here first because it is the
most transferable lesson of the round. Full treatment in §1.

### ⚠ WHAT THIS IS, AND WHAT IT IS NOT — read before quoting anything below

**Class: AUDIT DISPOSITION.** This doc records what the A1–A7 audit measured and
which charter items it discharged. It is **not** a physics result, **not** a
ruling, and **not** a decision. It mints nothing: no `clm-`/`def-`/`exp-`/`sup-`,
no KB leaf edited, no solidity moved, no register touched.

- **It does NOT rule on R58.** Decision 1 and the (2,3) carrier fork stay
  **LIVE and un-ruled**, exactly as the lens record's §7 (`:171-174`) states.
  Only Grant can rule that the lens replaces them, and this audit's verdict is
  that it does not currently qualify to.
- **It does NOT retract the lens record.** Per Rule 12 the merged record's body
  is untouched; a single dated status note is appended pointing here.
- **The findings are lane products, not this lane's measurements.** Every number
  below carries its measuring lane. The two exceptions — F9/F10 in §4 — were
  re-run against this branch's base before being quoted.

**Sector declaration.** MODE numerical-lens-audit · REGIME driven-to-saturated
(`A_bond` swept `0 → 0.95`, `S(A)` down to `0.31`; the kernel's clip domain
`A_cap=0.99 / S_min=0.05` is reached and is where every solver failed) ·
PHASE-STATE cold-through-saturated, no yield · CHANNEL **scalar / A1-adjacent
longitudinal ONLY** — the T2/Cosserat channel is not wired in
(`src/ave/solvers/harmonic_balance_srs.py:146-149`, verbatim: *"The T2/Cosserat
channel is NOT wired in (A1 perpendicular to T2, master-equation.md:20); no
winding observable exists here."*) · CARRIER **srs-z3**, `L=2` (N=64, degree 3,
96 bonds, **ndof = 192**), with unitarity spot-checked at `L=3` (648) and `L=4`
(1536). **Cross-wiring check performed:** nothing measured here couples the
scalar channel to charge, spin or mass — and §2.4 records that the *lens* does
cross that line, which is finding F4.

### Provenance of the evidence

Two phases, both agentic, neither previously landed in the repo:

| phase | shape | what it produced |
|---|---|---|
| **REVIEW** | 6 lanes, one per charter cluster | **28 findings**; 3 of them independently checked and all 3 **DOWNGRADED to MINOR** |
| **VERIFY** | **6** of those 28 findings × 2 adversarial refuter lenses (12 votes) + 1 completeness-critic synthesis | the verdict table, the two orphan findings, F9/F10, the reframe assessment |

**Selection bias, stated up front:** the verify phase re-tested only **6 of the
28** review findings, and all six came from **3 of the 6** review lanes. The A2
lane, the A4 lane and the A5/logic lane contributed **zero** findings to the
verify phase. Everything those three lanes found is **review-grade and
un-refuted-tested**. §5 and §8 say where that matters.

## §1 — THE INSTRUMENT BUG — read this before the verdict table

**The roll-up was wrong, and it was wrong in the dangerous direction.** The
synthesizer led with it, and it leads here for the same reason.

Each of the six findings was handed to **two** adversarial refuter lenses:

- a **reproduce** lane (build the object, run the code at the branch tip, try to
  break the measurement), and
- a **does-it-measure** / construct-validity lane (grant the number, attack the
  inference).

The roll-up then computed a per-finding status as `refuters >= ceil(total/2)`.
With `total = 2`, `ceil(2/2) = 1`: **a single dissenting lens sets the status to
REFUTED.** The synthesis states the same thing in its own words —
*"It is computed as `≥1 refuter → REFUTED`."*

### The actual votes

| # | finding | reproduce lane | does-it-measure lane | roll-up said | what it is |
|---|---|---|---|---|---|
| **F1** | unitary-generic | `refuted=true` | `refuted=true` | REFUTED | the **only** unanimous one |
| **F2** | seed-is-fork | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F3** | winding-is-seed | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F4** | no-wound-sector | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F5** | amplitude-free | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F6** | priorart-precondition | `refuted=true` | **`refuted=false`** | REFUTED | **SPLIT, the other way** |

All twelve votes carry `confidence: high`. **Five splits reported as six
unanimous refutations.** In four of the five, the lane that dissented from
REFUTED was the one that had actually built the operator and run it.

### Why it is the dangerous direction and not a wash

A false REFUTED is silently expensive in a way a false CONFIRMED is not. A false
CONFIRMED gets attacked again at the next gate — the corpus is built to do that.
A false REFUTED **removes the finding from the board**, and nothing downstream
ever re-opens it. Four of the discarded findings here are the ones that
established that the lens's core criterion cannot fail.

The failure has a second edge worth naming: in three cases the refuting lane was
arguing against receipts **produced in the same round that it could not see**.
F2's does-it-measure lane wrote that the wound-vs-trivial discriminating run
*"does not exist anywhere"*; F2's reproduce lane had run it, in the same round,
with a template-free integer readout (§2.2). Cross-lane invisibility plus a
one-vote refutation threshold is how a panel converts *"we disagree"* into
*"it is dead."*

### Two receipt-level cautions on this section

1. **The `status` column is not in the journal.** The twelve result records
   carry only `refuted`, `confidence`, `reasoning`, `corrected_claim`,
   `receipts`, `symmetric_standard_note`. The status field lives in the workflow
   roll-up, outside the journal. The formula quoted above is therefore recorded
   **as the synthesizer reported it**, cross-checked against the vote pattern
   (which is directly readable and is what the table above is built from), not
   read out of the roll-up source.
2. **"Three" vs "four".** The dispatch brief for this doc says the reproduce
   lane voted the other way *"in three of those"*. The journal says **four**
   (F2, F3, F4, F5). The synthesis's own bottom line agrees with four
   (*"it will discard four findings that survived read-and-run"*). Flagged, not
   silently harmonised.

### The repair, stated so it is reusable

A 2-lens adversarial panel has **no majority**. It should not report a scalar
status at all. The honest roll-up for an even panel is the vote vector plus the
disagreement axis — and where one lane ran code and the other did not, that
asymmetry is itself part of the report. `refuters >= ceil(total/2)` is a
majority rule applied to a set that cannot have one.

## §2 — THE VERDICT TABLE, F1–F6

Severities are `in` = as filed by the review lane, `out` = after the two
adversarial lenses and the synthesis.

| # | finding | sev. in | sev. out | disposition | corrected claim, one line |
|---|---|---|---|---|---|
| **F1** | unitary-generic | CRITICAL | **MAJOR** | **CONCLUSION CONFIRMED / ARGUMENT REFUTED** | The frozen-S route is dead (0/192 cold eigenvectors solve the self-consistent problem at any `A>0`), but the conclusion is **re-established on F5+F6 receipts**: the self-consistent problem has continuous one-parameter families at `r_auto ~5e-15`, in every sector, running continuously to `A→0` where they **are** the cold linear eigenmodes. Bare existence carries near-zero discriminating content. |
| **F2** | seed-is-fork | CRITICAL | **CRITICAL** | **CONFIRMED** (refutation mooted) | The winding enters via the seed and is returned bit-exactly by the solve. |
| **F3** | winding-is-seed | CRITICAL | **MODERATE** | **DOWNGRADED + RE-SCOPED** | The `rigid_template` read is seed-determined for every nonzero `b_w`; it is not a PR-#1019 defect, and dynamical readers exist elsewhere. It **is** a hard constraint on charter item A3. |
| **F4** | no-wound-sector | CRITICAL | **CRITICAL — BLOCKED** | **CONFIRMED, premise swapped** | The barrier is **grade orthogonality**, not field data type. Blocked on an unreconciled three-way canon collision over where the (2,3) lives. |
| **F5** | amplitude-free | MAJOR | **MAJOR** (measurement) / **MODERATE** (attribution) | **CONFIRMED as measured, DOWNGRADED as a lens defect** | The unconstrained square system is rank-deficient by **exactly one**, null direction = amplitude rescale. Drop the α clause; drop the lens-attribution (the incumbent driven test has the same property). |
| **F6** | priorart-precondition | MAJOR | **MODERATE** | **SUBSTANTIVELY AGREED; the split is verbal** | Both lanes converge on the same repair — **one selection constraint from a conserved quantity, NOT loss** (loss would violate Ax3). |

### §2.1 — F1, the headline, handled precisely: ARGUMENT REFUTED, CONCLUSION RE-ESTABLISHED

This is the one that must not be compressed. It is the only unanimous REFUTED in
the round, and the conclusion it was refuting is nevertheless **true** — just on
different receipts.

**The filed argument.** M is Y-unitary for any S-field — measured
`||M^H diag(Y) M − diag(Y)||_max / ||diag(Y)||_max = 3.083e-16`, `ndof = 192` —
therefore every eigenvector is a source-free solution, therefore existence is
vacuous. Independently reproduced by both lenses (`8.018e-17` and `8.018e-17`,
same machine-precision order, norm-convention difference), and confirmed **not**
to be cold-specific: it survives a graded, deeply saturated field
(`A ∈ [0.1, 0.95]` → `2.510e-16`; `A` random in `[0,0.9]` → `2.960e-16`).

**REFUTED, and correctly.** `S` is a function of `|v|`, so the 192 cold
eigenvectors are **not** solutions of the nonlinear problem. Re-measured, with
`M` rebuilt from each eigenvector's **own** envelope:

| target mean `A_bond` | median defect | min | max | n < 1e-8 |
|---|---|---|---|---|
| `0.0000` | `3.467e-15` | `1.475e-15` | `5.997e-15` | **192** |
| `0.0010` | `1.274e-07` | `4.890e-08` | `1.002e-05` | 0 |
| **`0.0854`** (`=√α`) | **`9.414e-04`** | `3.594e-04` | `1.213e-01` | **0** |
| `0.3000` | `1.365e-02` | `4.866e-03` | `4.652e-01` | 0 |
| `0.6000` | `2.049e-01` | `2.889e-02` | `5.361e-01` | 0 |

**0 of 192 at `A = √α = 0.0854`**, median defect `9.4e-4`. The 192/192 pass at
`A = 0` is `v = 0`. Separately, the "192" is a **basis artifact**: the cold
spectrum has only **23 distinct θ** with multiplicities up to **34**
(convention-free restatement and correction in §4).

**⚠ AND THE CONSENSUS-BIAS HIT, which is a standing discipline and not a
courtesy.** Both F1 lenses flagged it and both withdrew the move. The inference
*"the frozen-field operator is Hermitian/unitary for ANY field, so every
eigenvector is a solution, so the criterion is vacuous"* would equally condemn:

- **Hartree–Fock / SCF** — the Fock operator is Hermitian for any density;
- **Dyson–Schwinger and gap equations**;
- **lattice-QCD transfer matrices** and γ₅-Hermiticity work;
- **the entire NLS / Gross–Pitaevskii / discrete-breather bound-state
  literature**;
- and **QM itself** — `U = e^{−iHt}` is unitary and a finite box has `dim(ℋ)`
  stationary states; nobody calls bound-state existence vacuous.

Standard practice does this freely and gets a pass. Flagging it in AVE and not
there is consensus bias, and the lanes caught it themselves.

**RE-ESTABLISHED, on F5/F6 receipts.** The refutation carried an implicit
promise — that self-consistency *re-discretizes* the solution set. F5 and F6
measured that promise and it is **false**:

- The unconstrained **square** autonomous system (phase pin only, no norm) is
  rank-deficient by **exactly one**, and the null direction is the amplitude
  rescale. Two independent lanes:
  - `σ_min/σ_max = 3.207e-11` vs `σ_[-2]/σ_max = 8.280e-04`, overlap with the
    rescale direction **0.997**, gauge overlap `0.00691`; the null vector's
    `dθ` component `+2.764519e-03` matches the sweep tangent
    `+2.774243e-03` to **0.35 %**;
  - independently, `σ_min = 1.680e-11` vs `σ_[-2] = 3.739e-04`, overlap
    **1.0000**.
- The branch runs **continuously down to `A→0`**, where it **becomes** the cold
  linear eigenmode. Measured from `amp = 0.020` (`A_max = 0.02512`,
  `resid 4.61e-15`) upward, all 30 sweep points converging at `~5e-15`.

So the self-consistent solutions are *continuous deformations of the very cold
eigenvectors the refutation excluded.* The refuters' distinction does not save
the criterion; **it relocates it by one continuous parameter.**

**Why the two halves are not a contradiction.** F1's lanes reported "0/192
self-consistent" while F5/F6 reported converged branches at `5e-15` over
continuous amplitude ranges. F1's lanes used a **one-shot frozen-S residual and
undamped Picard**; F5/F6 used **damped Picard with eigenvector-overlap branch
tracking and an imposed norm**. F1's reproduce lane said so itself and was
honest about it — verbatim: *"limit-cycle stall, not divergence … Reported as a
solver stall, NOT as non-existence."* F1's does-it-measure lane was not: its
*"self-consistency DOES re-discretize"* headline is a one-shot residual
presented as a fixed-point result, and its supporting claim that a uniform
S-field makes M amplitude-independent does not apply to the actual solutions,
whose envelopes are **not** uniform (`A_max 0.212 / A_min 0.125` on the same
branch, from the other lane's own receipt).

### §2.2 — F2, seed-is-fork: CONFIRMED, refutation mooted

The winding enters via the seed and comes back bit-exactly. The
wound-vs-trivial discriminating run that the refuting lane said *"does not exist
anywhere"* **was run in the same round**, by the other lane, with a
template-free integer readout on the module's own gate-3 ring fixture:

```
seed                       theta        2pi m/N     r_auto  conv  winding
ring_mode m=0+noise  +0.000000000        0.0000   3.04e-15  True   -0.000
ring_mode m=1+noise  +0.261799388        1.0000   2.74e-15  True    1.000
ring_mode m=2+noise  +0.523598776        2.0000   2.61e-15  True    2.000
ring_mode m=3+noise  +0.785398163        3.0000   1.64e-15  True    3.000
ring_mode m=5+noise  +1.308996939        5.0000   2.52e-15  True    5.000
ring_mode m=-2+noise -0.523598776       -2.0000   1.90e-15  True   -2.000
(winding = -sum of principal-branch phase steps of v[:,0] around the ring / 2pi; no template)
```

Seeds `m ∈ {0,1,2,3,5,−2}` in → `{0,1,2,3,5,−2}` out, `θ = 2πm/24`, `r_auto`
`1.6–3.0e-15`. And solver-independently: **all 24 sectors** `m = −11…12` are
exactly solvable with **no iteration at all**, `r_auto ≤ 3.6e-15`, saturation
engaged (`S_min = 0.9682 < 1`).

**The caveat the reproduce lane did not apply to itself**, supplied by another
lane: the "all 24 sectors, no iteration" receipt is on `build_ring_net`, where
`a_nodes` cancels and the nonlinearity is **structurally inert**
(`src/ave/solvers/harmonic_balance_srs.py:1062-1070`; the module's own guard 4
at `:677-680` says a per-node-uniform admittance cancels at the shunt junction).
On the load-bearing **srs** net the wound seeds are **2 of 4 converged**.

Two further corrections the round produced and the headline should carry:

- **`r_auto` is not uniformly at machine zero.** The first of the six quoted
  thetas is **UNCONVERGED**: `seed0: theta=2.499991678 r_auto=1.06e-06
  dA=4.4e-05, 300/300 outers`. *"All at or near machine zero"* is false for it.
- **A LINEAR control reproduces the whole phenomenon with the nonlinearity
  OFF.** Same six seeds, same selection rule, operator fixed and
  seed-independent: six different exact machine-zero autonomous solutions, all
  delocalized, `r_auto 3.4–4.2e-15`. The nonlinear run then dresses θ by only
  `~1e-2` off that pre-existing seed-independent spectrum. **"Different seeds →
  different solutions" is not evidence about the saturation kernel at all.**

### §2.3 — F3, winding-is-seed: DOWNGRADED to MODERATE, re-scoped onto A3

The `rigid_template` read `ω = |b_ω| · ê_w`
(`src/ave/solvers/srs_cage_winding.py:482`; mechanism in its own docstring at
`:480`) is seed-determined for **every** nonzero `b_w`. Reproduced exactly by
both lanes at the production config (`SrsCageWindingConfig()` defaults, `L=12`,
`frame_N=32`, `R=7.0`, `r=2.3`, 13824 nodes): baseline
`(w_tor, Q_link) = (2,3)`, `Q_link_raw = 2.9959`; substituting the **entire**
dynamical DOF `b_w` with complex Gaussian noise → `(2,3)`, `2.99488`; all-ones →
`(2,3)`; `U[0,1e3]` → `(2,3)`; lognormal noise spanning **four spatial decades**
→ `(2,3)`. Only `b_w ≡ 0` collapses it, to `(0,0)`. Conversely, scrambling `ê_w`
with a seeded `b_w` collapses `Q_link` to `0`.

**Why it downgrades.** It is not a PR-#1019 defect — the PR is three markdown
files, 211 insertions, and touches no winding module. A genuinely dynamical
reader **does** exist in the tree: `phase_space_winding.read_winding` counts
turns of `arg(Σ a_A1)` and `arg(Σ b_w)` off the solved trajectory and **moves**
under the same noise substitution (`q_int 0 → −1`). So *"THE production winding
observer"* is over-general.

**Why it still bites, and this is the part that routes.** A `rigid_template`
read **cannot discharge charter item A3** without tautology. Any future P2
prereg must name which reader it uses.

**Unrebutted aggravator.** `SrsCageWindingConfig` has **no `winding_mode` field
at all** (0 grep hits in that file). The `dispersive_vector` negative-control
arm the refutation leaned on
(`src/ave/solvers/coupled_cage_winding.py:163-167` — *"KEPT as a documented
negative control (the winding-NOT-conserved arm)"*) is **diamond-carrier only**.
**On the srs carrier the rigid template is the only representation available and
there is no control arm.**

### §2.4 — F4, no-wound-sector: CONFIRMED with the premise swapped — and BLOCKED

**DROP the filed premise.** *"Every (2,3) reader consumes a real 3-vector
Cosserat ω"* is measurably **false**: the production reader consumes two
`complex128` **scalar** fields, `a_A1` and `b_w`, and reads the toroidal "2" as
`arg(Σ a_A1)` off the A1/MASS sector; the real 3-vector `a_w` is the
non-production control arm. A second counterexample sits in
`src/ave/core/observable_battery.py:738` — a (2,3) reader that consumes K4
`V_inc`/`Φ_link`, explicitly *"NOT the Cosserat sector"*.

**The real barrier is GRADE ORTHOGONALITY.** Measured on the object the lens
actually solves:

- the HB unknown is `(64, 3) complex128` = **192 complex port phasors**, one per
  **directed** port, on the A1-adjacent scalar srs-z3 carrier
  (`harmonic_balance_srs.py:146-147`);
- `V_ref = w[:,None] − v` (`apply_M`, `:499-500`) is a **rank-192-of-192** image
  of `V_inc` — i.e. exactly the *"read-only projection of the same scalar `V`,
  not an independent DOF"* condition that
  `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`
  **forbids wiring a winding into**;
- the same leaf at `:33` states verbatim that A1 and T2 *"share no
  $(V_{inc}, V_{ref})$ phasor"*;
- the HB module carries **zero** winding/Link/Cosserat machinery: AST import
  scan returns only `chiral_lattice` + `vacuum_varactor_scatter`, and a
  docstring-stripped keyword count returns `cosserat 0 | Cosserat 0 |
  omega_field 0 | winding 0 | Link 0 | helicity 0 | curl 0 | T2 0`.

So §4 restricts the search space using the **(2,3)/T2** winding sector's
protection mechanism on a solve whose only variable lives on the **orthogonal
A1** grade. The refutation demonstrated a **generic ℤ phase winding** — a *name*
match to the (2,3), not a *grade* match — and its own corrected claim concedes
the (2,3) **pair** is not established on the degree-3 srs carrier.

**🚧 BLOCKER — three canon sites put the (2,3) in three different places, and no
lane reconciled them.** Cosserat ω / K4 `V_inc·Φ_link` / K4 `V_inc·V_ref`
Clifford torus, against `master-equation.md:33`'s *"share no
$(V_{inc},V_{ref})$ phasor"*. **The F4 verdict literally depends on which
reading is canonical.** F4 is reported BLOCKED, not adjudicated. This is charter
item A4, and §5 records that A4 got zero coverage.

**One methodological self-indictment, recorded because it is instructive.** The
refuting lane accused the finding of a vocab-cage error (using A1⊥T2 outside the
observable it was ratified about) and **then committed the same error itself**,
treating a phasor-space winding on a phasor state as sufficient — a name match,
not a grade match. The other lane had already anticipated and answered that
move; the refuting lane did not engage the distinction.

**A3's sub-question got one partial answer here.** *"What is the discrete
analogue of passing through zero?"* — the winding read is **ill-defined exactly
at `|v| = 0`**: `np.angle(0) = 0`, and a measured continuation returned winding
`−3` *at* the zero crossing (`|v[3]| = 0.000`), flipping to `−2` only past it. A
discrete amplitude-floor guard is required on any seeded-sector solve.

### §2.5 — F5, amplitude-free: CONFIRMED as measured, DOWNGRADED as a lens defect

**Cross-confirmed by two independent lanes** — the rank-1 deficiency receipts are
in §2.1 and are not repeated. What changes from the filing:

- **DROP the α clause.** *"which is the `A² = α` operating point re-entering as
  a solver input"* is not established. `√α = 0.085425`; the sweep **floor** is
  `0.211922 = 2.48 × √α` and the ceiling `≈ 0.91 = 10.65 × √α`. **The α point is
  never in range.** And what is imposed is `||v||`, not `A`. It also collides
  with the P2 prereg skeleton's own text
  (`research/2026-08-25_p2-existence-solve_prereg-SKELETON-DRAFT.md:290-291`):
  *"`A = \sqrt{\alpha}` appears only as a **report-against** canonical operating
  point … never as a pass/fail."*
- **DROP the lens-attribution.** The **incumbent driven test has the identical
  property**: over a 16× drive sweep (`s = 0.05 → 0.8`) with a real
  `Termination` on 8 crossing ports, `A_max/s` = `0.7375, 0.7374, 0.7371,
  0.7361, 0.7314` — flat to **0.8 %**. The operating point is set by the free
  drive amplitude in exactly the same way. This is a **G2-prereg requirement**,
  not a cost of adopting the lens.
- **TRIM the "one family" wording.** Warm-started continuation runs `||v||`
  `2.0 → 8.5` (`A_max → 0.950373`), then Picard stops converging where `A_max`
  crosses the kernel's `A_cap=0.99 / S_min=0.05` clip
  (`src/ave/core/crystal_engine.py:63-64`, `:192-195`), and `||v|| = 10.25 →
  10.5` is a **second, distinct continuum** at `θ ≈ 2.334`. At least two
  continua with a solver-breakdown gap. **This strengthens the conclusion** —
  more branches, less selection — and it is also where F8 lives (§3).
- **Reproduction-fidelity disclosure the lane made itself:** the low-end numbers
  did not reproduce exactly (`A_max 0.211922 / θ 2.410` vs `0.243168 / 2.412475`)
  because the cold `θ = 2.4119` band is **6-fold degenerate** and the branch
  tracker lands on a different member. The top end matches to 4 digits and the
  rank-1 result is configuration-independent by dimension count.

### §2.6 — F6, prior-art precondition: the split is verbal; both lanes agree on the repair

**Both lanes converge:** the missing ingredient is **one selection constraint
from a conserved quantity** — norm / charge / Derrick-type scale condition — and
**NOT dissipation.** Adding loss would violate Ax3. The finding never actually
prescribed loss (it said the mechanism is *"lost"*), so this is a clarification.

**The strongest consensus-bias check in the entire round is here, and it is
measured rather than asserted.** *"Lacks gain compression"* would condemn every
lossless soliton existence proof, so the lane **built the control**: a discrete
NLS / Gross–Pitaevskii stationary state on a ring of 8, posed as the identical
square system (16 real + `μ` = 17 unknowns, 16 eqs + phase pin = 17).

```
   norm^2    mu             ||G||      sigma_min(square)  sigma_2nd   sigma_min(+norm eq)
    0.50    0.67858532   5.8e-13    4.421e-22       3.403e-04   3.403e-04
    1.00    0.76977285   3.3e-13    8.236e-22       2.530e-03   2.530e-03
    2.00    0.94861976   7.0e-13    7.743e-22       1.748e-02   1.748e-02
    4.00    0.50000000   3.6e-13    4.985e-23       2.509e-01   2.509e-01
    8.00    1.00000000   4.1e-13    1.660e-24       2.509e-01   2.509e-01
```

**The textbook lossless problem carries the identical rank-1 deficiency**
(`σ_min ~1e-22` vs `σ_2nd 1e-4 … 0.25`) and **one norm equation restores full
column rank exactly** (`σ_min(+norm) == σ_2nd`). The same ring **with**
van-der-Pol gain/compression is full-rank and the amplitude *is* pinned — which
is precisely the ingredient Ax3 forbids, and precisely why the correct repair is
the norm condition and not a damping device.

**What survives against the record.** §3.1 sells the method by naming RF
free-running-oscillator prior art whose amplitude selector is a gain-vs-**loss**
balance — structurally absent here. The measured statement: on the shipped
operator, the RF amplitude-pinning equation `|loop gain| = 1` is **identically
`0 = 0`** — `max ||λ|−1| = 1.132e-14` over `A_uniform ∈ {0, 0.10, 0.25, 0.50,
0.70, 0.85, 0.95}` on a genuinely graded field. **It pins nothing.**

**Minor cite drift, both lanes independently:** the record quotes
`harmonic_balance_srs.py:23-26`; the actual span is **`:22-25`**, and the record's
truncation drops the `:24-25` qualifier (*"the only energy exit is a declared
matched TERMINATION (a boundary condition, never a bulk loss term)"*).

## §3 — THE ORPHAN FINDINGS — F7 and F8, filed by nobody

**These two were produced as by-products of refutations, by lanes that were
arguing about something else, and no lane filed either of them. They are more
damaging to the lens than anything in §2.** They get their own section for that
reason.

### F7 — DELOCALIZED (CRITICAL, CONFIRMED, was UNFILED)

**Every converged autonomous solution measured in the round is delocalized.**
Participation **86.6 – 164.0** of **192** dofs; inverse participation ratio
**0.0061 – 0.0116** against a uniform-state IPR of **0.005208** (`= 1/192`).
These are **extended lattice modes, not bound states.**

Measured independently by two lanes while refuting *other* findings:

```
seed0: theta=0.625959 IPR=0.00961 participation=104.1/192  A_max=0.7462
seed1: theta=2.499995 IPR=0.00610 participation=164.0/192  A_max=0.5223
seed2: theta=2.420522 IPR=0.00789 participation=126.8/192  A_max=0.7190
seed3: theta=2.393286 IPR=0.00628 participation=159.1/192  A_max=0.6145
  -> every seed: DELOCALIZED (54-85% of the lattice). Same verdict six times.
```

**Receipt-precision correction, made here and not in the synthesis.** The
extremes of the quoted range do not come from the same run family. The
nonlinear converged solutions span participation `104.1 – 164.0` (IPR
`0.00610 – 0.00961`). The **`86.6` / `0.01155` endpoints come from the LINEAR
control** — the same seeds and the same selection rule with the **saturation
switched off** and the operator fixed and seed-independent (participation
`105.8, 123.9, 118.3, 97.4, 105.3, 86.6`). Quoting `86.6 – 164.0` as a range over
nonlinear solutions is imprecise. **It also strengthens F7 rather than weakening
it:** delocalization is not caused by the nonlinearity, it is a property of the
carrier, and turning the kernel on does not localize anything.

**A potential counterexample, checked and dead.** A third lane's srs run
returned one low-participation state — `random seed 1: theta=+0.000000000
partic=0.147` — which would be a localized solution. It has
`r_auto = 2.449e-02`: **not converged.** Every one of that lane's *converged*
states sits at participation fraction `0.542 – 0.851`, and its wound seeds at
`0.851`. **The counterexample does not survive the convergence gate.**

**Why it is the most damaging item in the round.** F1's own reproduce lane, in
its refutation, wrote that the entire discriminating load falls on
*"the non-triviality gate, the wound-sector restriction, and **a
localization/structure criterion**."* **That criterion had already been measured,
twice, in the same round — and it fails.** The last remaining discriminator was
gone before the refutation naming it was written.

### F8 — NO FOLD (MAJOR, CONFIRMED, was UNFILED) — and this is the direct answer to A5

The record's §3.4 backup selector, verbatim at
`research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md:116-117`:

> *"Wind up slowly and watch for the branch to fold back; **the fold IS the
> existence boundary.**"*

**It is measurably absent.** Two lanes pushed the continuation up:

| lane | reached | `S(A_max)` | `dθ/dA` | turning point? |
|---|---|---|---|---|
| rail sweep | `A_max = 0.91819` | `0.39613` (**60 % kernel compression**) | monotone **positive** throughout (`+7.1e-05` at `amp=0.04` rising smoothly to `+2.3e-03` at `0.60`, continuing through `0.80`) | **none** |
| warm-started continuation | `A_max = 0.950373` at `||v||=8.5`, `r_auto 6.386e-15` | — | monotone positive | **none** |

Every point on the way up is an **exact source-free solution** at `~5e-15`.

**The top-end break is not a fold — it is the kernel's own declared clip
domain.** `A_cap = 0.99` / `S_min = 0.05`
(`src/ave/core/crystal_engine.py:63-64`, applied at `:192-195`:
*"S(A)=√(1-A²), A=|V|/V_yield, clipped to [S_min, 1] (the A-034 kernel)"*).
Convergence dies at `||v|| = 8.75`, `A_max = 0.986728`, `r_auto = 1.029e-01`
after 600 outers — i.e. **exactly where `A_max` crosses `A_cap`.**

**This is the direct answer to charter item A5**, whose own text warned that
*"A false positive here would be a serious error"* (`RECORD.md:159`). **The
answer is negative: the stall is a numerical failure at the clip, not a
result.**

**And A5 already had a second, independent negative answer from the review
phase that the verify phase never saw.** One review lane ran the record's own
quoted ladder — `research/drivers/data/p2_scoping/accel.py` §B — and reproduced
`it = 8/11/20/41` at `D = 0.3/0.5/0.7/0.8` and `{it:150, conv:false}` at
`D = 0.9`; then at the **same** endpoint `D=0.9`, `anderson(A0, term(0.9),
depth=6, maxit=150)` → `{it:66, conv:true}`. **A genuine fold is a property of
the solution branch and is not cured by swapping the outer accelerator.** The
solution demonstrably exists at `D=0.9`. Two independent routes, same verdict:
**numerical failure, not a result.** §5 records that this answer was already in
the record's own §5.1 (`:136-138`) eighteen lines below the question.

**One measurement that is not a null and is not the effect either.** The
saturating medium **stiffens** the branch — `θ` is not constant, and the spread
across the ladder is `3.493e-01` — so the nonlinearity is demonstrably **active,
not inert**. This is a null **in precisely the regime where the effect would
live**, not a null where the effect cannot exist. That distinction is what makes
F8 a result rather than an artifact.

## §4 — F9 / F10 — two new measurements, and a receipt-convention correction

Both were produced by the completeness-critic synthesizer, not by any review or
refuter lane. Both are INFO-severity against the lens itself and **fatal for the
reframe assessed in §7**.

**F9 — STATIC DEGENERACY.** The `θ=0` and `θ=±π` eigenspaces are each
**34-dimensional** on srs `L=2` (**68 of 192** dofs) and stay **exactly**
34-dimensional at `A=0`, at `A=√α`, and under a random graded field that lifts
everything else from 23 to 127 distinct θ. **Amplitude cannot lift the static
degeneracy.**

**F10 — M IS EXACTLY REAL.** `max|Im M| = 0.000e+00` for **every** S-field, and
the shipped `bloch_adjacency` satisfies `A(−k) = conj(A(k))` to **`0.000e+00`**
— i.e. **exact spinless time-reversal symmetry**. `S(A)=√(1−A²)` and `Y=Y₀/√S`
are real and `CONNECT` is a permutation, so no amplitude can introduce a complex
phase.

### The verbatim receipt block

Receipt script: `scratchpad/chk3.py` (session scratchpad, **not in-repo** — see
the reproducibility flag below), originally run against
`/Users/grantlindblom/AVE-staging/AVE-Core` at `766d5179`. Engine files are
identical to the branch tip; PR #1019 touches no solver code (`git diff --stat`
on the merge: 3 files, 211 insertions, all markdown).

```
net: N=64 degree=3 ndof=192 n_bonds=96
cold A=0              Y-unitarity 8.018e-17  max|Im(M)|=0.000e+00  M REAL? True
                      n_distinct_theta=23  mults=[4,6,9,17,34]
                      dim(theta=0)=34   dim(theta=+-pi)=34
A=sqrt(alpha)=0.0854  Y-unitarity 2.216e-16  max|Im(M)|=0.000e+00  M REAL? True
                      n_distinct_theta=23  mults=[4,6,9,17,34]
                      dim(theta=0)=34   dim(theta=+-pi)=34
graded rand[0,0.9]    Y-unitarity 1.706e-16  max|Im(M)|=0.000e+00  M REAL? True
                      n_distinct_theta=127 mults=[1,16,18,34]
                      dim(theta=0)=34   dim(theta=+-pi)=34
BLOCH: max_k ||A(-k) - conj(A(k))|| over 8 random k = 0.000e+00 -> spinless TRS HOLDS
```

### RE-RUN AT THIS BRANCH'S BASE — verify-before-cite, not copy-paste

This lane re-ran `chk3.py` unmodified against the worktree at **`a3f4fef7`**
(`origin/main`, the merge of PR #1019). **Every line reproduces bit-identically**
to the block above, including both `0.000e+00` entries.

### ⚠ RECEIPT-CONVENTION CORRECTION — the three "multiplicity" receipts do NOT disagree

Three receipts in the round report the srs `L=2` cold multiplicity structure
three different ways, and on the face of it they conflict:

| source | reported |
|---|---|
| `chk3.py` (above) | `n_distinct_theta=23`, `mults=[4,6,9,17,34]` |
| F6-reproduce's STUCK-POINT | *"no simple eigenvalue; minimum multiplicity 4; **17-fold at ±π**, 34-fold at 0"* |
| F1-reproduce's `diag.py` | `distinct thetas: 23`, `multiplicities: [4, 6, 9, **16, 18**, 34]` |

**They are the same spectrum.** `θ=+π` and `θ=−π` are the **same eigenvalue**,
`λ = −1`; `np.angle` splits that one eigenspace into two buckets by the sign of
a floating-point zero, and the split point moves with the field. Measured
convention-free (clustering on the complex eigenvalue itself, tolerance `1e-8`),
this lane's own run at `a3f4fef7`:

```
cold A=0         n_distinct_EIGENVALUES=22  mult multiset={4, 6, 9, 34}
                 mult(lam=+1)=34  mult(lam=-1)=34
                 np.angle bucketing: n_distinct_theta=23  theta=+pi:17 theta=-pi:17
A=sqrt(alpha)    n_distinct_EIGENVALUES=22  mult multiset={4, 6, 9, 34}
                 mult(lam=+1)=34  mult(lam=-1)=34
                 np.angle bucketing: n_distinct_theta=23  theta=+pi:17 theta=-pi:17
graded rand      n_distinct_EIGENVALUES=126 mult multiset={1, 34}
                 mult(lam=+1)=34  mult(lam=-1)=34
                 np.angle bucketing: n_distinct_theta=127 theta=+pi:16 theta=-pi:18
```

**The convention-free statement, which is the one that should be quoted
downstream:**

> On srs `L=2` the cold operator has **22 distinct eigenvalues**, not 23. `λ=+1`
> and `λ=−1` are **each exactly 34-fold**. A random graded field lifts every
> other eigenvalue to **multiplicity 1** (126 distinct) and leaves the two
> 34-fold blocks **completely intact**.

**This is sharper than F9 as filed and it cuts the same way, harder.** F9 said
amplitude cannot lift the static degeneracy. The convention-free measurement
says a graded field lifts *everything else* to simple — and the two 34-fold
blocks, 68 of 192 dofs, **35 % of the spectrum**, survive untouched. Whatever
protects them is not something amplitude can reach.

Cross-check that the 34 is not an artifact of this lane: the number is already
banked independently in the corpus. `research/2026-08-25_solver-crosscheck-phase1_result.md`
§1's reproduction gate carries the row *"srs $L=2$ cycle-space block | **34** at
$\theta=0$ and $\theta=\pi$"*, verified against a cycle space of `B−N+1 = 33`.

### ⚑ Reproducibility flag (NOT fixed by this lane)

`chk3.py` is a session-scratchpad file outside the repo. The F9/F10 receipt is
therefore **re-runnable only because this lane re-ran it and reproduced it
here**, and the block above is now the durable record. If F9/F10 are ever to
gate anything, the script belongs in `research/drivers/` under the
unreferenced-drivers policy. Routed, not done.

## §5 — CHARTER DISPOSITION — A1 through A7

*(section landed in a later commit)*

## §6 — THE BOTTOM LINE

*(section landed in a later commit)*

## §7 — THE OVER-BRACED CHIRAL CRYSTAL REFRAME — does it dodge these defects?

*(section landed in a later commit)*

## §8 — FLAGS SURFACED, NOT FIXED BY THIS LANE

*(section landed in a later commit)*

## §9 — WHAT THE AUDIT DID NOT COVER

*(section landed in a later commit)*

## §10 — Skill-selection retro-pass

*(section landed in a later commit)*
