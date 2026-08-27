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
> (`r_auto ~ 5e-15`), in **every** winding sector, **delocalized** across 54–85 %
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

The charter is `research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md:151-167`
— seven items plus two required checks.

| # | charter item | class | disposition | what established it |
|---|---|---|---|---|
| **A1** | the shipped `harmonic_balance_srs` can be run autonomously — same fixed point, source dropped, one phase pinned | MACHINERY | **DISCHARGED — NEGATIVE** | Read-and-run: it is **not a flag flip**. `solve_tone` takes `theta: float` as an **INPUT** (`:534`, `:537`), never an unknown, and forms the *linear* system `(e^{iθ}I − M_FF)x = M_FT ŝ`. With `term=None`, `ŝ=0`, so `b=0`. On the shipped ring fixture (N=12, m=2, `θ=1.0471975511965976`) the true ring mode **is** a source-free fixed point (`r_auto = 5.73e-16`), yet `solve_tone(..., term=None)` returns **`‖v‖ = 0.000e+00` with `converged=True`** — in **three** configurations, including warm-started at the **exact** true mode. Separately, damped Picard + branch tracking + an imposed norm **does** converge; plain Picard stalls (48/48 branches failed). |
| **A2a** | autonomous/oscillator HB is standard external prior art | EXTERNAL | **DISCHARGED — CONFIRMED, with the precondition dropped** | **The retrieval WAS run** (see the correction box below), against three named sources. The technique, the extra-unknown/extra-equation structure and the phase-pinning convention are **as described**. What the transfer omits: the counting yields an **ISOLATED** solution only because dissipation + active gain balance and pin the amplitude — the one ingredient Ax3 forbids. |
| **A2b** | its phase-normalization is the same move as clause Q | ASSEMBLY | **DISCHARGED — NEGATIVE** | **RESEMBLANCE, NOT THE SAME OBJECT. "NOT FIT to travel to a prereg as written."** Detail below. |
| **A3** | topology is preserved by seeding the sector | NUMERICAL + CANON | **PARTIALLY DISCHARGED — negatively** | F2 + F3: the winding comes back **= the seed**, and the production reader is template-circular, so a `rigid_template` read **cannot discharge A3 without tautology**. The sub-question *"what is the discrete analogue of passing through zero"* got one partial answer (§2.4: the read is ill-defined at `\|v\|=0`; `np.angle(0)=0` returned `−3` **at** the zero crossing). **Not closed.** |
| **A4** | the phase-space (2,3) is a PER-TANK object, so uniform imposition conflates per-tank trajectory with collective charge | CANON READING | **DISCHARGED — UNDERDETERMINED** (verdict is "canon does not decide") | A dedicated lane swept it by **two** methods (pattern + full read) against the whole canon set the charter names. Verdict: **canon never carves the scope, and where it speaks it EQUATES the per-bond chart with the collective boundary integer.** The record therefore **proposes a carve, it does not catch a conflation.** An independent checker confirmed every cite verbatim and **downgraded the finding MAJOR→MINOR** on the grounds that the record self-flags the reading and A4 exists to adjudicate exactly this. |
| **A5** | the continuation stall may be a RESULT rather than a numerical failure | INTERPRETIVE | **DISCHARGED — NEGATIVE, twice, independently** | (1) **F8** (§3): no fold to `A_max 0.918`/`0.950`, `dθ/dA` monotone positive, break at the kernel's declared clip. (2) The review phase re-ran the record's own quoted ladder: `anderson(depth=6)` converges at the **same** `D=0.9` endpoint in **66 outers** where plain Picard fails at 150. **A fold is a property of the branch and is not cured by swapping the outer accelerator.** Charter warned *"A false positive here would be a serious error."* Answer: **numerical failure.** |
| **A6** | dropping the scaffold dissolves decision 1 and the carrier fork rather than hiding them | LOGIC | **DISCHARGED — the claim is OVERSTATED-TO-FALSE** | That is **F2**. The fork **re-enters at the seed**, fully and intact, relocated to the initial condition. The tone set re-enters as an input constraint. |
| **A7** | a source-free solution "cannot belong to the scaffold" | LOGIC | **DISCHARGED — VACUOUS, and stronger than A7's own hedge** | That is **F1** (§2.1), re-established on the F5/F6 receipts. The record hedged it *"true but possibly vacuous"*; the measurement says the sentence at `RECORD.md:98` is **false**, not merely vacuous. |
| — | **consensus-bias symmetric standard** | required check | **DISCHARGED — thoroughly** | Twelve notes across six findings, run in **both** directions; in five instances a lane **withdrew its own or the finding's argument** on symmetric-standard grounds. §5.2 below. |
| — | **discrimination check** (*"organizing power, a number, or neither"*) | required check | **DISCHARGED — and the answer is worse than the record predicted** | Two lanes ran it. §5.3 below. |

### ⚠ §5.1 — CORRECTION TO THE SYNTHESIS'S OWN CHARTER-COVERAGE SECTION

**This is the most important correction in this document, and it runs against the
brief that commissioned it.** The verify-phase synthesis reports A2 as a *"total
coverage hole"*, **"UNDISCHARGED, BOTH HALVES"**, A4 as **"ZERO COVERAGE"**, A5
as *"filed by nobody"*, the discrimination check as **"NOT PERFORMED BY ANY
LANE"**, and the routing item as *"quoted by no lane"*.

**All five are false as statements about the audit. All five are true as
statements about the *verify phase*.** They have a single common cause: **the
synthesizer saw only the six selected findings and the twelve verify votes. It
never saw the review journal's 28 findings or its six clean reports.** The
scoping error is the same instrument-level failure as §1 — a roll-up reasoning
about a subset as though it were the whole.

What is verifiably true, each checked directly against both journals:

| synthesis claim | verify phase | review phase | net |
|---|---|---|---|
| *"A2's external retrieval was never run by anyone"* | **TRUE** — one lane states verbatim *"I did NOT do external literature retrieval (audit item A2's own charge); I relied on discipline knowledge"* | **FALSE** — a lane scoped *"Charter item A2 only"* states *"The record flags this claim as asserted-from-discipline-knowledge and NOT retrieved (:156). **I retrieved it.**"* and names three sources: Wiley-IEEE *Analysis and Design of Autonomous Microwave Circuits*; Elsevier *A robust and efficient oscillator analysis technique using harmonic balance*; **arXiv 1006.4931** | **A2a DISCHARGED** |
| *"the string 'clause Q' appears nowhere in any of the twelve votes"* | **TRUE** — grep over all twelve votes returns **0** | irrelevant — the review journal has **23** hits, and one lane's headline finding **is** the clause-Q verdict | **A2b DISCHARGED** |
| *"A4 — ZERO COVERAGE … no lane checked it against the two-threes carve, INVARIANT-N1, or the electron-plumbing primer"* | **TRUE** | **FALSE** — a dedicated A4 lane checked **all three by name** and enumerated its sweep method | **A4 DISCHARGED (underdetermined)** |
| *"A5 — ANSWERED BY MEASUREMENT, FILED BY NOBODY"* | **TRUE** (F8 was an orphan) | **FALSE** — A5 was **filed as a MAJOR review finding** with its own read-and-run receipt | **A5 DISCHARGED twice** |
| *"discrimination check — NOT PERFORMED BY ANY LANE"* | **TRUE** | **FALSE** — performed by **two** lanes, with opposite-verdict conditions stated | **DISCHARGED** |
| *"the routing item … is quoted by no lane"* | **TRUE** | **FALSE** — quoted at `:31-33` by a lane that used it to check fork-status discipline | — |

**Consequence for this doc's deliverables:** the A2 coverage hole the dispatch
asked me to open a new item for **does not exist in the form described**. What
*does* exist is thinner and is what §8 routes instead: **A2's two findings never
received the adversarial verify pass** — like everything else from the three
lanes the verify phase skipped, they are **single-lane and review-grade**.
Flag-don't-fix: I have not reframed the synthesis to match, and I have not
reframed this doc to match the synthesis.

### §5.2 — A2b in full, because it is the plank that makes the lens look canon-endorsed

The record, `RECORD.md:85-90`:

> *"**The arbitrary phase that the normalization condition fixes IS ϖ.** … That
> is canon's own clause Q — Grant's ratifying words on 2026-08-10 were **"makes
> perfect sense, we need a ground reference."** **The EE method and the source
> law agree on the treatment.**"*

Three canon facts, all re-verified on this branch by this lane:

1. **R43 is BINDING and the record breaches it.** `manuscript/ave-kb/common/vocabulary-register.md:500`, verbatim:
   *"★ VOCABULARY RULING (R43, 2026-08-10 — **BINDING on every consumer**…): the **canonical term is "DC operating point / quiescent point (Q-point)"**. **"Ground (reference)" is the EE-ANALOGY GLOSS, NEVER the canonical noun** — it may appear only as an explicitly-labelled analogy."*
   The record's use is **not** labelled as an analogy; it is the **warrant for
   the identification**. The same register entry at `:501` pre-flags exactly
   this: *"**"ground"** is a live mis-use hazard created by the ruling itself,
   since the EE analogy is the natural thing to reach for — it is the gloss, not
   the noun."*
2. **Clause Q is a DC / zero-frequency condition.**
   `manuscript/common_equations/eq_axiom_5.tex:82`, verbatim: *"**Q (quiescence
   --- the DC operating point).** The sourceless substrate sits at the cold
   operating point: `∇·π = 0, θ = 0, ε₁₁ = 0` … away from defects."* Its job is
   to supply the missing boundary condition at spatial infinity so **clause G's
   elliptic solve** is well-posed.
3. **R55 licenses the GENUS, not the object.**
   `_orchestration/docket-entries/2026-08-24-ruling-r55-axiom5-source-law.md:58`,
   verbatim: *"A ground reference is a gauge choice, not a material primitive."*
   That establishes *"both moves fix an arbitrary reference"* and **nothing
   narrower**.

**Stated in circuit terms before adjudicating, per the vocab-cage discipline:**

| | clause Q | autonomous-HB phase normalization |
|---|---|---|
| removes | an **additive constant** of a static scalar potential | a **multiplicative global phase** of a complex phasor |
| symmetry group | **ℝ** (potential translation) | **U(1)** (time-origin of a periodic orbit) |
| frequency | **ω = 0** | **ω ≠ 0** |
| sector | A1 / bound, on `ε₁₁, π, θ` | the HB unknown, which is `V_inc` on directed bonds |
| purpose | boundary condition at infinity for an elliptic solve | squareness against an added frequency unknown |

**Different group, different frequency, different sector, different origin of the
degeneracy.** Measured supports: `grep -rn "clause Q" manuscript _orchestration
| grep -icE "phase|phasor|oscillat"` → **0**; `grep -n
"eps_11\|epsilon_11\|varepsilon" src/ave/solvers/harmonic_balance_srs.py` → **0
hits**. **Clause Q does not govern the variable the normalization acts on.**

**What survives, and it matters:** the **ϖ half is correct** and R58-supported —
R58 §2.1 measured ϖ as a global drive phase that multiplies the whole solution
because M is real (`1.6e-12`, replicated twice), which is exactly the U(1) orbit
an autonomous solve must quotient. **Same genus, different species.** The only
evidence offered for the species-level identity is a shared English word that
canon has explicitly demoted to a gloss and pre-flagged as a trap.

**Symmetric-standard check, run by the lane itself:** an identification argued
from shared vocabulary rather than shared structure *"would be flagged in an
SM/QED paper too — this is the same class as reading QED's gauge fixing and GR's
gauge fixing as one object because both are called 'gauge'."* **Not a
consensus-bias artifact.**

**Mitigation, recorded because it is fair:** the record did not mint the
mislabel. R55 does the same thing at `:56-58`, and the quote itself is verbatim
in canon at three places. The defect is the **"ratifying words"** label — the
actual R43 ratification quote is the one that **strips "ground" of canonical
status**: *"we can map it to ground but call it DC operating point? approved."*

**Second-order point that belongs in the discrimination check:** even taken at
its strongest, consequence 1 buys the lens **nothing new** — R58 §2.1 already
records that *"the ϖ objection to source-termination evaporates"* on current
main, in the **driven** setting.

### §5.3 — the discrimination check, run twice, answer worse than predicted

The charter predicted the honest answer would be *"organizing power and zero
numbers"* (`RECORD.md:165-167`).

- **Lane 1's answer:** *"this lens buys organizing power and zero numbers"* —
  which is a **legitimate and expected outcome for a lens and is NOT a
  failure**. But nothing in the record is testable yet, and **nothing may be
  promoted, ruled or frozen into a prereg on the strength of the lens alone.**
  Genuine organizing gain: the scaffold-FORM axis of decision 1, the
  matched-vs-mismatched generator question and the `term=None` structural-zero
  branch **do** lose their subject. Over-credited: decision 1's projection axis
  was **already dead on main** before this lens, and the carrier fork
  **relocates rather than dissolves**.
- **Lane 2's answer is harsher and is measured:** *"zero numbers AND **negative
  organizing power**"* — because the four scaffold-shaped choices the lens
  removes (drive spec, projection, generator match, `term=None` branch) are
  replaced by four choices that are **harder to audit** — the seed sector, the
  imposed norm, the tone constraint set, and the `(n−1)` unpinned tone phases —
  **none of which currently has a computed receipt**, where the driven
  formulation's choices at least had `source_amp` / `exchange_amp` / `P_net`
  receipts (`harmonic_balance_srs.py:787-855`).

**Combined with F7 and F8 the answer is: organizing power, zero numbers, and one
fewer discriminator than the driven test had.**

### §5.4 — the symmetric-standard ledger, in both directions

**Six instances where AVE was held to a HARSHER standard than SM/QED/lattice/
soliton practice — all six caught and named by the lanes themselves:**

1. **F1, both lanes** — the vacuity move would condemn Hartree-Fock/SCF,
   Dyson-Schwinger, lattice-QCD transfer matrices, the NLS/GP/discrete-breather
   literature, and QM itself. **Named and withdrawn.**
2. **F4-reproduce, on the finding's own premise** — *"every (2,3) reader must
   consume a real 3-vector Cosserat ω"* imports a Yang-Mills prior that
   topological charge lives on a gauge/vector field. Standard physics puts
   winding integers on complex **scalar** order parameters freely
   (Ginzburg-Landau vortices, superfluid circulation, Berry phase, `π₁(S¹)=ℤ`).
   **Named, withdrawn, and independently killed by measurement.**
3. **F4-does-it-measure** — seeding a winding into a complex field's phase and
   preserving it by *"cannot unwind unless the amplitude passes through zero"*
   is textbook GL/superfluid/Abrikosov. **Correctly flagged as harsh** — though
   contested, because the finding is about the (2,3)/T2 sector specifically.
4. **F5, both lanes** — *"the operating point is a solver input"* condemns
   Petviashvili iteration, Newton-conjugate-gradient, fixed-norm imaginary-time
   relaxation, shooting at fixed ω, Q-balls, boson stars, Skyrmions at fixed B,
   lattice scale-setting, and QED taking α and `m_e` as inputs. **Both lanes
   narrowed to the symmetric requirement — *state the family and state the
   selector*.**
5. **F6-reproduce — measured, not asserted.** *"Lacks gain compression"* would
   condemn every lossless soliton existence proof; the lane **built the
   discrete-NLS/GP control** and measured the identical rank-1 deficiency (§2.6).
   **The strongest consensus-bias check in the set.**
6. **F3-does-it-measure** — *"the observer is a pure function of the seed"*
   would condemn the Skyrme hedgehog (`U = exp(iτ·n f(r))` carries `B=1` by
   construction; only `f(r)` is solved) and fixed-topology lattice QCD.
   **Named**; contested on the read-the-verdict-off-the-frozen-part distinction.

**Four instances where standard practice is STRICTER than the lens — these are
the ones that survive:**

1. **F2** — in every standard sector-restricted problem the sector still
   contains a **live** existence question; you extremize an energy or action and
   the sector **can be empty**. Derrick's theorem exists precisely because
   sectors can be empty. Here M is exactly lossless, so every sector has a
   machine-zero-residual solution at every amplitude: **the answer can never be
   NO.** Mirror test: a lattice-QCD paper reporting *"initialized in Q=1,
   measured Q=1, residual 1e-15, therefore the instanton exists"* would be
   rejected. **Same standard, same verdict, either framework.**
2. **F3** — LGT computes topological charge **from the solved gauge links**
   (clover/field-theoretic Q after gradient flow, or the overlap index) and it is
   gauge-invariant; gauge-fixing does not supply the integer. The real analogue
   of `ω=|b_w|·ê_w` is **topology freezing**, which the discipline treats as a
   known systematic **pathology** requiring fixed-topology finite-volume
   corrections. And on the srs carrier AVE has **no negative-control arm at
   all**.
3. **F5** — the soliton and lattice literatures **always state the family and
   the selector explicitly**. The lens does neither, and §3.1 *sells* the method
   by naming prior art whose selector is a gain-vs-**loss** balance. Same error
   class as citing asymptotic freedom for a theory with no running coupling.
4. **F6** — the soliton literature also demands a demonstration that the
   physical member is **not continuously connected to vacuum**. The lens has
   neither the selector nor that demonstration, and the branch was measured
   running continuously to `A→0`. **This is the item that defeats the R58 §4
   non-triviality gate**: *"nonzero"* is satisfied at every point on a curve
   that reaches zero.

**One asymmetry running the other way, worth stating.** Two lanes note that AVE
holds itself to a **stricter** standard than SM has an equivalent for.
`master-equation.md:20`'s forbidden-wiring guard — *"**never wire the winding
into the breather's own phasor `(V_inc, V_ref)`** — `V_ref` is a read-only
projection of the same scalar `V`, not an independent DOF"* — is a named,
ratified, load-bearing rule policing a conflation SM has **no explicit
prohibition against**. One lane then **measured** the forbidden condition:
`V_ref` is a **rank-192-of-192** image of `V_inc`. **F4 is an application of
AVE's own rule, not an imported one.**

**Net answer to the required check: yes, in six named places, and the lanes
caught all six themselves. No unflagged instance of AVE being held to a harsher
standard remains in this verdict set.**

## §6 — THE BOTTOM LINE

**(a) The existence criterion as posed is DEAD, and (b) the lens is repairable
only as a *selection* test, never as an *existence* test.**

Three sentences:

1. **"Does a nontrivial source-free solution exist" is dead as a criterion.**
   Existence is generic: continuous one-parameter families at machine-zero
   residual (`r_auto ~5e-15`), in **every** winding sector, **delocalized**
   across 54–85 % of the lattice, running continuously down to `A→0` where they
   **are** the cold empty lattice's own linear eigenmodes.
2. **The lens is repairable, but only if it stops being an existence test.** It
   needs all four of:
   - **(i)** one added **scalar constraint from a conserved quantity or the Link
     integral** — measured on the standard control to be exactly what restores
     full column rank, and lossless, so Ax3 survives;
   - **(ii)** a **non-triviality gate that the `A→0` end of the *same branch*
     demonstrably fails** — R58 §4's *"nonzero"* is satisfied at every point on
     a curve that reaches zero, so it is not that gate;
   - **(iii)** a **localization / structure criterion** — which has already been
     measured once, and **it failed** (F7);
   - **(iv)** a **winding read from the converged solution by a non-template
     reader**, which **does not exist on the srs carrier** — the rigid template
     is the only representation available there and there is no control arm.
3. **The review lanes were not wrong; the roll-up was** — five of six findings
   are split votes reported as REFUTED, and the two most damaging measurements
   of the entire round (universal delocalization, absence of the fold) were
   produced as by-products of refutations and filed by nobody.

### The one sentence that is now falsified rather than hedged

`research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md:97-98`, §3.1
consequence 3, verbatim:

> *"**A source-free nontrivial solution cannot be: there is nothing else it
> could belong to.**"*

**It can be, and it does belong to something else. It belongs to the cold
lattice, continuously.** The charter hedged this as *"true but possibly
vacuous"* (`:161`). The measurement is stronger than the hedge: the sentence is
**false**, because the branch that carries the "nontrivial" solution runs
continuously into the cold empty lattice's own linear eigenmode, and unitarity
supplies the source-free solution for free at every point along the way. The
correct reading is *"there is nothing it **needs** to belong to."*

Rule 12 governs what happens to that sentence: **its body is preserved
byte-identical** and a dated status note is appended to the record pointing
here. It is not edited, and it is not deleted.

### What survives and is worth building

A lens that **finds** candidate states, plus a separate and honest set of gates
that **select** among them. That is what soliton physics and lattice QCD both
do, out loud. It is not what §3.1 consequence 3 claims.

Two parts of the record survive this audit intact and should not be swept away
with §3.1 — one lane made the point explicitly and it is correct:

- **§3.2** (winding as a Lagrange constraint, with the multiplier as the idle
  measure) is *"precisely the standard fix for the genericity problem — it is
  the Q-ball/fixed-charge move — and is the strongest formulation in the
  record."*
- **§3.3** (pole search) and **§3.4** (fold/turning point) both supply the
  discreteness §3.1 lacks — though §3.4's specific mechanism is the one F8
  measured absent, so it is a *shape* that survives, not a *result*.

**A VACUOUS verdict on A7 is not a verdict against the record's §3 as a whole.**

### What this does NOT do to R58

Nothing. **Decision 1 and the (2,3) carrier fork stay LIVE and un-ruled**,
exactly as `RECORD.md:171-174` and the routing item both state. This audit's
finding is that the lens **does not currently qualify** to moot them — not that
they are settled. **Only Grant rules that the lens replaces them.**

### Ordered next work, by kill-power per unit compute

1. **Adjudicate A4 and the (2,3) canon collision.** One reading lane, no code.
   Until *"where does the (2,3) live"* is settled, **F4 cannot be closed**.
   Highest leverage, cheapest. Note that the A4 lane's own verdict is that
   **canon does not currently decide it** — so this is a Grant-level carve, not
   a sweep.
2. **File F7 and F8 as first-class measurements** — a localization gate on the
   converged family, and a fold search with **proper arclength continuation**
   rather than Picard, to separate the kernel clip from a genuine turning point.
3. **Build the symmetry-adapted / Bloch-reduced / deflated solve.** It unblocks
   the constrained-system nullity measurement, the accidental-vs-symmetry-
   enforced degeneracy question, and everything in §7.
4. **Run the two-tone (2:3) case — or declare S2 fatal and say so.**
5. **Re-run A2's retrieval through the external-retrieval pipeline** so its
   three named sources carry gate-specified standing rather than single-lane
   standing (§8).

## §7 — THE OVER-BRACED CHIRAL CRYSTAL REFRAME — does it dodge these defects?

**Scope: assessed ONLY for evasion vs inheritance of the confirmed defects. NOT
assessed for truth.** The reframe is a separate proposal (a Maxwell–Calladine
self-stress count on an over-braced chiral Cosserat lattice, with a Berry/Chern
integer transported around a closed loop as the charge). It is live on its own
PR and this lane rules nothing about it.

| defect confirmed above | verdict | why |
|---|---|---|
| **D1** — existence generic; one-parameter continuum; no selection; connected to `A→0` (F1/F5/F6/F8) | **RELOCATED, NOT EVADED** | The instinct is right: for a Y-unitary family `\|λ\|=1` is identically satisfied and imposes nothing, whereas an eigenvalue **collision** `λ_i=λ_j` is a genuine condition on the parameter. Replacing a vacuous condition with a codimension-≥1 one is the correct structural move. **But on this carrier the degeneracy is already generic and amplitude-rigid** — FLAG 1. |
| **D2** — the seed supplies the sector and the solve returns it (F2) | **EVADED IN PRINCIPLE, PARTIALLY RE-IMPORTED** | A parallel-transported Berry/Chern integer is **computed**, not seeded — the correct LGT-analogue answer. But transport must track eigenvectors around the loop, and **every** branch tracker in this round used max-overlap-with-the-current-iterate, i.e. *"an experiment whose selection rule is literally 'stay nearest the seed'."* With multiplicity up to 34 the abelian transport is ill-defined; you need Wilczek–Zee over the degenerate block, and **the choice of starting subspace inside a 34-dimensional block is a seed.** |
| **D3** — template winding reader (F3) | **CLEANLY EVADED** | The invariant never touches `srs_cage_winding` or `ê_w`. This is the defect the reframe dodges outright and it should be credited plainly. |
| **D4** — wrong sector; no Cosserat channel; no (2,3) reader (F4) | **INHERITED IN FULL** | The proposal says over-braced chiral **Cosserat** lattice. The audited object has **no Cosserat channel** (`harmonic_balance_srs.py:147-149`; zero winding/Cosserat symbols in the code body). A Maxwell–Calladine count on a Cosserat lattice **requires the micro-rotation DOF** — the exact channel that is absent — and `V_ref` is a rank-192-of-192 projection of `V_inc`, so there is no independent second DOF to brace against. Either build T2 first (**R58 blocker S1**, a much larger job) or the computed integer is **not** the charge. |
| **D5** — amplitude selection absent; loss forbidden by Ax3 (F5/F6) | **CORRECTLY EVADED IN KIND** | Structural (degeneracy) selection is lossless and needs no gain compression — the right answer to F6's confirmed diagnosis. Note it is a *different* cure from the one F6 measured (one added norm equation restores full rank); degeneracy selection adds no equation, it picks isolated points on the existing family. Both are legitimate. The degeneracy route must show the collisions are **finitely many, not symmetry-enforced, and at physical amplitudes.** None of the three is measured and the one relevant measurement is adverse. |
| **D6** — universal delocalization (F7) | **INHERITED, ARGUABLY WORSENED** | Nothing about self-stress or a Chern integer makes a state localized. The self-stress space of a **periodic** hyperstatic frame is spanned by Bloch states at every `k`, and Chern integers are bulk-**band** properties. By bulk-boundary correspondence the physical localized object would then sit at a **boundary or defect**, not in the bulk — which the periodic srs torus with `term=None` **does not have**. Consistent with the corpus's own bulk-cage falsification, but it means the object must be re-posed on a lattice **with** a defect or boundary. Different build. |
| **D7** — no fold (F8) | **NEUTRAL / EVADED** | The reframe replaces the fold with the collision as the distinguished point. Legitimate. Weak counter-evidence only: the measured branch is structurally featureless to `A_max 0.95`. |

### Seven flags — places the reframe re-imports a confirmed defect

**FLAG 1 — the degeneracy selector fires everywhere on this carrier. This is D1
re-imported verbatim, in a new coordinate.** Measured (F9, §4, re-run by this
lane at `a3f4fef7`): `λ=+1` and `λ=−1` are **each exactly 34-fold** — 68 of 192
dofs — at `A=0`, at `A=√α`, and under a random graded field that lifts
**everything else to multiplicity 1**. One lane hit the same wall independently
as a declared STUCK-POINT (*"no simple cold eigenvalue; minimum multiplicity
4"*). A criterion reading *"the selected amplitude is where the spectrum becomes
degenerate"* fires on **35 % of the spectrum at every amplitude, including
`A=0`** — the one place a selector must not fire. **The reframe is viable only
after a symmetry-adapted (irrep-block / Bloch-reduced) decomposition that
quotients out symmetry-enforced degeneracies and looks for *accidental*
collisions within a single irrep block. That machinery does not exist and nobody
has built it.**

**FLAG 2 — the Chern integer is identically ZERO on this operator, by exact
symmetry, at every amplitude.** Measured (F10, §4, re-run at `a3f4fef7`): **M is
exactly real**, `max|Im M| = 0.000e+00` for cold, `√α` and a random graded
field, because `S(A)=√(1−A²)` and `Y=Y₀/√S` are real and `CONNECT` is a
permutation. And the shipped `bloch_adjacency` satisfies `A(−k) = conj(A(k))` to
**`0.000e+00`** — exact spinless time-reversal symmetry. **A real Bloch matrix
has odd Berry curvature and every band's Chern number vanishes identically.** No
amplitude can break it, because the saturation kernel is real. The srs lattice's
*geometric* chirality is **not** broken time-reversal in the sense a Chern
number requires. Escapes exist — ℤ₂ rather than ℤ; non-abelian Wilczek–Zee over
degenerate blocks; a synthetic loop with **twisted boundary conditions**, which
would introduce the complex phases that rescue this — but each requires
machinery the periodic torus with `term=None` does not provide.

**FLAG 3 — where is the loop?** A Chern number needs a closed loop in a
parameter space of dimension ≥2. The only parameter this audit established is
the **amplitude**: a 1-D open interval from `A→0` (cold linear) to the
saturation rail. **An open interval has no closed loops.** Either add a second
parameter (twist/flux/chirality angle — FLAG 2) or take the loop in `k`-space,
which leads to FLAG 4.

**FLAG 4 — a `k`-space loop makes the invariant a property of the SCAFFOLD. This
is the exact thing `RECORD.md:98` was trying to escape.** A Chern number over
the BZ of the S-dressed lattice is **piecewise constant in amplitude**, jumping
only at gap closings. At the `A→0` end of the branch that is the **cold empty
lattice's** band invariant. Unless the branch crosses a collision on the way up,
the integer is **inherited from the empty lattice** — and *"there is nothing
else it could belong to"* becomes false again, in the same way and for the same
reason F1 already made it false.
**One-line kill test, cheap, run it first: is `Chern(A→0, cold empty lattice) ≠
Chern(A at the solution)`? If equal, the invariant belongs to the scaffold and
D1 is re-imported in full.**

**FLAG 5 — amplitude-dependent bracing cannot change the hyperstaticity, only
where the eigenvalues sit.** Maxwell–Calladine is a **connectivity** count.
`S(A)` changes bond **admittances** (`Y=Y₀/√S`), not connectivity, so `s−m` is
amplitude-**invariant**. Measured confirmation: the `λ=+1` block stays exactly
34-dimensional from `A=0` through a random graded field. The **only** place
bracing could change the effective count is the rail, where `S→0` and `Y→∞` (a
compliance becoming a rigid constraint) — and that is **exactly** the kernel's
declared clip domain (`A_cap=0.99 / S_min=0.05`) and **exactly** where every
solver in this review failed (F8). **So the reframe's selection point, if it
exists at all, sits precisely at the numerically-unreachable boundary that F8
showed to be a kernel-clip artifact rather than established physics.**
Determining whether `A→1` is physics or the clip is a **prerequisite** for the
reframe, not an aside.

**FLAG 6 — the category translation has not been made, and this is a vocab-cage
hazard.** Maxwell–Calladine operates on a **rigidity/equilibrium matrix** of a
frame; a state of self-stress is `ker(Rᵀ)`, a **static** (zero-frequency)
object. The HB formulation has no equilibrium matrix — it has a unitary
scattering map `M = C ∘ blockdiag(S_u)`, and its eigenproblem is at **nonzero
θ**. In circuit terms the self-stress analogue is a **circulating loop current
with zero terminal excitation**, i.e. a null space of the reduced
admittance/incidence structure. **That is a genuinely different object from an
eigenvector of M at `|λ|=1` — which is good news: the reframe is not F1
relabelled.** But the bridge from the rigidity matrix to the scattering map does
not exist, nobody has written it, and importing Maxwell–Calladine's *name*
imports its framework's theorems with it. **State the observable in circuit
terms before adjudicating.** Obvious first measurement, and cheap: **if
"load-free equilibrium" maps to the `λ=+1` eigenspace, the self-stress space on
srs `L=2` is 34-dimensional and scales with N — an extensive, amplitude-rigid,
over-braced-by-34 object, and correspondingly non-selective.** That is a
testable prediction of the reframe on its own terms and the existing data
already leans against it. *(Corroborating, independently banked: the
solver-crosscheck phase-1 reproduction gate carries "srs L=2 cycle-space block |
34 at θ=0 and θ=π" against a cycle space of `B−N+1 = 33`.)*

**FLAG 7 — one integer versus a pair.** A Chern number is a single integer. The
(2,3) is a **pair**. The mapping from one to the other is undone, and it sits
directly on top of the unresolved **A4 / canon-collision blocker** in F4. Until
that is adjudicated the reframe cannot say *which* integer it is computing or
that it equals the charge.

### Net assessment of the reframe

**It cleanly evades D3, correctly evades D5's Ax3 problem in kind, and evades D2
in principle. It inherits D4 and D6 in full. Its two load-bearing mechanisms —
degeneracy-as-selector and Chern-as-invariant — are both measurably vacuous on
the shipped carrier as it stands:** 34-fold amplitude-rigid degeneracy at `λ=±1`,
and Chern ≡ 0 from exact realness of M. So on the object this audit examined it
does **not** currently dodge D1 — **it relocates D1 into the spectrum's
degeneracy structure, where the same "the condition is identically satisfied"
failure recurs.**

**That is not a kill.** It is a statement that the reframe requires **three
builds before it can be tested at all**: (i) a symmetry-adapted / Bloch-reduced
solve separating accidental from symmetry-enforced degeneracies; (ii) a
mechanism that breaks the exact realness of M (twisted boundary conditions, or a
genuinely complex sector), or a switch to a ℤ₂/non-abelian invariant that
survives spinless TRS; and (iii) the **Cosserat/T2 channel**, without which the
Maxwell–Calladine count has no micro-rotation DOF to count and the computed
integer is not the charge. **None of the three exists. The third is R58's
standing blocker S1.**

## §8 — FLAGS SURFACED, NOT FIXED BY THIS LANE

Flag-don't-fix. None of these was resolved here; each names who must resolve it.

| # | flag | who resolves |
|---|---|---|
| **FL-1** | **The audit instrument's roll-up rule.** `refuters >= ceil(total/2)` is a majority rule applied to an even panel that cannot have a majority. It converted five splits into six unanimous refutations. | orchestrator lane — workflow config, not physics |
| **FL-2** | **The synthesis's charter-coverage section is wrong on five counts** (§5.1), because the synthesizer reasoned about the verify subset as though it were the whole audit. **The synthesis is otherwise the strongest document of the round and its physics is sound** — this is a scoping defect, not a physics defect. | orchestrator lane; do not re-quote the coverage bullets |
| **FL-3** | **The (2,3) canon collision (A4).** Three canon sites place it in three different places — Cosserat ω / K4 `V_inc·Φ_link` / K4 `V_inc·V_ref` Clifford torus — against `master-equation.md:33`'s *"share no `(V_inc,V_ref)` phasor"*. The A4 lane's verdict is that **canon does not currently decide it**. F4 cannot be closed until it is decided. | **Grant** — this is a carve, not a sweep |
| **FL-4** | **`solve_tone` fails SILENTLY into the trivial state**: `term=None` ⇒ homogeneous ⇒ `‖v‖ = 0.000e+00` with **`converged=True`**, three configurations, including warm-started at the exact true mode. This is R58 §4's *"'converged' is not 'non-zero'"* trap, live in shipped code. | engine lane — a non-triviality guard in the solver, not just in a prereg |
| **FL-5** | **`SrsCageWindingConfig` has no `winding_mode` field.** The `dispersive_vector` negative-control arm is **diamond-carrier only**; on the srs carrier the rigid template is the only representation and **there is no control arm at all**. | engine lane |
| **FL-6** | **A2's retrieval carries single-lane standing.** Three sources are named (Wiley-IEEE *Analysis and Design of Autonomous Microwave Circuits*; Elsevier *A robust and efficient oscillator analysis technique using harmonic balance*; **arXiv 1006.4931**) but the retrieval was not run through the external-retrieval pipeline and never received an adversarial pass. **Tentative-standing, not discharged-with-authority.** | orchestrator lane — this is what the new open item tracks |
| **FL-7** | **R43 breach in the merged record.** `RECORD.md:87-89` uses *"ground reference"* as the **warrant** for the clause-Q identification, unlabelled as an analogy, against the BINDING ruling at `vocabulary-register.md:500`. The record did not mint the mislabel — **R55 `:56-58` does the same thing** — so the sweep is wider than one file. | auditor lane — a wording repair plus a register sweep, not a physics change |
| **FL-8** | **A quotation in the merged record whose string exists nowhere in the corpus.** `RECORD.md:118-119` presents an italic attributed quotation, *"converges 8/11/20/41 outers up the rungs but does not fix the top rung alone."* `git grep "8/11/20/41"` on main returns nothing. **The CONTENT is exactly right and reproduces** (`research/drivers/data/p2_scoping/accel.py` §B gives `it = 8, 11, 20, 41` at `D=0.3/0.5/0.7/0.8` and `{it:150, conv:false}` at `D=0.9`) — the referent is an uncommitted terminal session. Quote-hygiene, not fabrication. | auditor lane |
| **FL-9** | **The termination probe is unreplicated and the two runs disagree.** One lane: **50 of 176** free-slot eigenvalues remain unimodular. Another: **72 of 184**. Different plane/termination configs, both reported as the same probe. Neither leaned on it; nobody reconciled it. | whoever next uses a terminated autonomous operator |
| **FL-10** | **`chk3.py` is scratchpad-only.** The F9/F10 receipt lives outside the repo; this doc's §4 block is now the durable record, but if F9/F10 are to gate anything the script belongs in `research/drivers/`. | this arc's next lane |
| **FL-11** | **Uniqueness / basin structure uncharacterised.** Six trivial seeds gave six distinct θ. Combined with the rank-1 continuum, the solution set within a **single** sector is at least 1-parameter **and** multi-branch. Nobody characterised it. | next lane |

### One flag that is about this lane's own evidence base

**FL-12 — the review phase's own findings were themselves only partly checked.**
Of 28 review findings, **3** went to an independent checker and **all 3 were
DOWNGRADED to MINOR** (two `EVIDENCE-VOID`, one `CONCLUSION-WRONG`). A fourth
checker was dispatched and **never returned**. Six of the 28 went to the verify
phase. **The remaining 19 have had no second pass of any kind.** Anything quoted
from them — including several items in §5's table — carries **single-lane
standing**. This doc marks lane provenance throughout for that reason.

## §9 — WHAT THE AUDIT DID NOT COVER

Modalities not run, in the order they matter:

1. **The two-tone (2:3) case. Every single receipt in this audit is
   SINGLE-TONE.** The entire lens is about the electron's (2,3), and `RECORD`
   §5.4 concedes *"whether a 2:3 tone structure is even representable as an
   autonomous solution on this machinery is open."* **It is still open. This is
   the largest modality gap in the round.** A review lane separately measured
   that the relative tone phase is **exactly inert** (`2.2e-16`) and that no
   exact 2:3 pair exists in the spectrum (nearest `1.500766779`) — which sharpens
   the gap rather than filling it.
2. **The augmented system with an actual selection constraint, on the AVE
   lattice.** The GP/DNLS control showed one norm equation restores full column
   rank exactly. **Nobody ran the AVE analogue.** The attempt hit a declared
   STUCK-POINT: srs `L=2` has **no simple eigenvalue** (minimum multiplicity 4),
   so the amplitude null direction is confounded with symmetry null directions.
3. **A symmetry-adapted / Bloch-reduced / deflated solve.** Routed by one lane
   as its own item. **Nobody built it.** Prerequisite for both #2 and for §7.
4. **A localization gate.** Measured twice as a by-product; **never gated, never
   pre-registered, never applied as a criterion.**
5. **Larger carriers.** Unitarity was checked at `L=3` (ndof 648) and `L=4`
   (1536). The **self-consistent family** was only ever solved at `L=2` and on
   the 24-ring. **Finite-size and continuum-limit behaviour of the branch:
   unknown.**
6. **The A2 sources were never adversarially read** (FL-6), and **19 of 28
   review findings never got a second pass** (FL-12).

## §10 — Skill-selection retro-pass

| skill | fired | where |
|---|---|---|
| `verify-before-cite` | ✅ | every load-bearing cite re-verified in this worktree at `a3f4fef7`: `vocabulary-register.md:500`, `eq_axiom_5.tex:82`, R55 `:58`, `master-equation.md:20`/`:33`, `harmonic_balance_srs.py:146-149` and `:534/:537/:802-804`, `crystal_engine.py:63-64`/`:192-195`, R58 `:98`. The two-cite drifts the lanes found (`:23-26`→`:22-25`; `:480`→`:482`) are recorded rather than propagated |
| Rule-10 empirical-driver discipline | ✅ | `chk3.py` **re-run**, not copied: bit-identical at `a3f4fef7` (§4). A second convention-free run was written and executed to reconcile three apparently-conflicting multiplicity receipts |
| `flag-don't-fix` | ✅ | §5.1 and §8. **The most consequential application ran against the dispatch brief itself** — the A2 "total coverage hole" it asked me to record does not exist in the form described, and I recorded the discrepancy rather than either complying or silently correcting |
| `consensus-bias-symmetric-standard` | ✅ | §2.1's F1 box and §5.4's full ledger in **both** directions, including the one asymmetry running the other way (AVE's forbidden-wiring guard is stricter than anything SM has) |
| Rule-12 additive-only | ✅ | the merged lens record receives **one appended dated status note**; body verified byte-identical by `git diff` before commit |
| `regime/phase-state discipline` | ✅ | §0 sector declaration; §3's F8 explicitly argues the null is **in** the regime where the effect would live (60 % kernel compression), not where it cannot exist |
| `phase-space-coordinate-check` | ✅ | §2.4 — the audit's own barrier is a **grade** mismatch (A1-adjacent scalar solve vs T2 winding sector), and the *name*-match-vs-*grade*-match distinction is carried through F4 and §7 FLAG 7 |
| `mechanism-claims-discipline` | ✅ | every headline carries its solidity and its measuring lane; F4 is reported **BLOCKED** rather than adjudicated because its verdict depends on an unresolved canon collision |
| stop-and-ask | ✅ (0 stuck-points) | nothing stalled; the one place a two-attempt cap would have fired — reconciling the three multiplicity receipts — resolved on the first convention-free measurement |
| `substrate-native-check` | ➖ **not fired, and correctly** | no solver, observer, eigsolver or operator was scaffolded by this lane. Every number here was measured by a prior lane or re-run unmodified |
| `ave-prereg` | ➖ not applicable | this is an audit disposition, not a test |

**Drift from the plan:** one unplanned skill fired — the convention-free
eigenvalue re-measurement in §4 was not scoped, and it changed a number the
round had reported three different ways. **Cheap, and it is the only place this
doc adds evidence rather than landing it.**

**Discipline boundary observed:** no physics was re-run beyond `chk3.py` and its
convention-free companion, no shipped number was moved, no KB leaf was edited,
no register was touched, and no ruling was made. R58 decision 1 and the (2,3)
carrier fork remain **LIVE and un-ruled.**
