# FROZEN PREREG — Axiom-4 Reduction EPIC: is the Universal Saturation Kernel a Theorem or a genuine Axiom?

**Date:** 2026-07-02
**Lane:** orchestration epic (foundational / axiom-reduction). Analysis + derivation + adversarial verification. NO engine simulation (see §6 — the corpus already showed static observables are shape-blind).
**Branch:** `analysis/axiom4-reduction-epic` (off `origin/main` @ `f556dcdc`)
**Disciplines fired:** `ave-prereg`, `substrate-native-check`, `pre-test-physics-check`, `consistency-vs-emergence`
**Prior single-agent pass:** `analysis/axiom4-saturation-forced` @ `7170f40e` (`research/2026-07-02_axiom4-forced_result.md`, verdict CONDITIONALLY-FORCED) — READ in full.
**Register seed:** `analysis/axiom-register` @ `e066d1e0` (Axiom 4 seeded `SHAPE-DERIVED (conditional)`).

> **SHA-PIN (Rule-16).** The discriminator (§2), the PASS/FAIL criterion, the lens set (§4), and
> the classification axis (§5) are LOCKED at freeze, BEFORE the verdict is written. Any post-verdict
> change to these is a new prereg with its own version, not an edit here.

---

## 0. The object under test

Axiom 4 (Scheme A canonical, `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:48-58`; `common_equations/eq_axiom_4.tex`):

$$ S(A) = \sqrt{1 - (A/A_{yield})^2}, \qquad A \in [0, A_{yield}] $$

posited as an axiom (NO claim ID). The single most cross-cited operator in the corpus (A-034 catalog, 26 instances / 21 orders of magnitude).

**Grant's incisive frame:** *"What defines forced? If it is forced, should it actually be an axiom?"*

## 1. Corpus state (ave-prereg grep — this is NOT green field; most sub-questions are already CLOSED)

A cross-repo prior-art grep (12 repos + archive) plus direct reads establish that the prior
single-agent pass (`analysis/axiom4-saturation-forced` @ `7170f40e`) **already closed four of the
five original sub-questions**. The epic's remaining open work is a SINGLE load-bearing question.

| Sub-question | Corpus verdict | Evidence |
|---|---|---|
| **(i)** Does substrate structure force **L2** vs L∞/Nyquist-peak? | **PARTIAL** — L2 is a genuine choice; the map kernel↔norm is **1-to-1** (an `L^p` invariant forces `S=(1−A^p)^{1/p}`, a *different* curve per `p≠2`). Endpoints + Maxwell limit + vertical tangent do NOT force `p=½` (whole `(1−A²)^p`, `0<p<1` family fits). | `2026-07-02_axiom4-forced_result.md §2`; register provenance |
| **(iii)** Fixed-radius ceiling `A_yield`? | Named **GAP-2** — a HARD fixed radius (vertical tangent), currently a **posit**. | result §3 |
| **(iv)** Born-Infeld / S11-min variational route independent? | **NEGATIVE** — "adds no independent forcing"; re-expresses the L2/quadratic posit in a Lagrangian dialect. | result §2.3; register |
| **(v)** ν=2/7 / K=2G elasticity route forces the shape? | **NEGATIVE** — the elasticity route selects the *operating point* in the **cold linear S=1 regime** (`2026-06-25_alpha-variational-strain-projection_prereg.md:43`; `2026-05-31_FT-b-saliency-derivability_result.md:101` — script has *zero* occurrences of "kernel/saturat/winding"). K=2G is itself **GR-imported** (`2026-06-20_node-2domain-nport.md:223`; PR#261) — cannot be a forcing residual. |
| **(ii)** Is the STATIC 7-mode RMS `A` the same L2 object as the DYNAMIC `(V_inc,Φ_link)` energy-phase? | **OPEN — THIS IS THE EPIC.** The dynamical energy-circle L2 is FORCED (lossless bond-LC, Ax1+Ax3, `x²+y²=1` to machine precision); the static RMS L2 is only **IDENTIFIED** with it (GAP-1). | result §3; register OPEN note |

**A new, load-bearing methodological constraint the grep surfaced (Fork-B live-fire, 2026-06-20):**
`research/2026-06-20_fork-b-saturation-tank-confinement_result.md` verdict **ECHO** — the quarter-arc
`√(1−A²)` gives **IDENTICAL** bound-mode localization to the `(1−A²)^p` comparator (`p≠½`), gap ≪ 10%;
"**the quarter-arc shape is not load-bearing**" for confinement. Corroborated by
`2026-06-20_mass-sector-characterization_synthesis.md:203` ("RMS radius is insensitive to the exponent
once norm+depth are matched"). **CONSEQUENCE (locks §6):** the L2-vs-L∞ discriminator CANNOT be produced
by ANY static localization / confinement observable — those are shape-blind. The discriminator must be
**analytical**, resting on the energy-conservation structure of the *dynamical* reactive DOFs.

**Orthogonal prior epic (not a competitor):** the earlier `ax4-saturation` epic
(`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`, 2026-05-26) takes the kernel as
INPUT and derives the observable amplitude-shape signature (κ₃/κ₄) at narrow apertures. ORTHOGONAL to
forcing; useful only as corroboration that the varactor `C_eff=C₀/S` / vertical-tangent picture is canonical.

## 2. The discriminator (LOCKED)

The epic's verdict turns on ONE question: **is the Axiom-4 static argument `A` the time-average (RMS ≡ L2) of the forced dynamical bond-LC energy-phase — i.e. the *same* L2 object — or an independent identification?**

- **FULL reduction (→ `DERIVED-TO-THEOREM`, count 4→3):** requires proving BOTH
  - **(F-a)** the static 7-mode RMS `A² = ε² + κ² + V²` IS the time-average of the dynamical reactive
    oscillation (RMS² = ⟨amplitude²⟩ = ½·peak² ∝ the conserved reactive energy = the forced-L2 invariant),
    for EACH of the three orthogonal reactance tanks (A1-V, Cosserat-ε, Cosserat-κ), so GAP-1 is a THEOREM
    of the lossless-LC L2 (Ax1+Ax3), not an identification; **AND**
  - **(F-b)** the saturation ceiling keys on the **SUM** of the three orthogonal tank energies (L2 total),
    excluding the L∞ (max / "which-sector-saturates-first") alternative; **AND**
  - **(F-c)** `A_yield` (the hard fixed radius + vertical tangent, GAP-2) is inherited from an
    already-present Axiom-1 primitive (the Nyquist/bandwidth cell-energy ceiling `V_SNAP²`), not an
    independent posit.
  Only if ALL THREE close from Axioms 1+3 + a bare, already-present identification does the axiom's
  *entire* content become a theorem (count drops).

- **PARTIAL / confirmed (→ stays `SHAPE-DERIVED (conditional)` or reverts toward `POSTULATED`):** if any
  of (F-a)/(F-b)/(F-c) requires an independent posit — in particular if an L∞/peak measure survives the
  adversary, or the static↔dynamic identity needs a definitional redefinition of `A` (Decision Point 1)
  — then the L2 norm is a **genuine independent axiomatic content** and "postulated" is the honest,
  final answer. Count stays 4.

**A primitive FORCES iff it UNIQUELY selects, not merely permits.** Per Fork-B, "permits" is cheap for the
static observable; the burden is a UNIQUE analytical selection of L2 from the *reactive-energy structure*.

## 3. What I expect (pre-registered)

**Prediction:** the outcome is **CONFIRMED-PARTIAL, sharpened** — i.e. the L2 norm is a genuine (but
minimal, EE-native) residual axiom, and the honest status stays **SHAPE-DERIVED (conditional)**, NOT a
full 4→3. Reasoning:
- **(F-a) likely CLOSES.** For a lossless reactive DOF, energy IS quadratic in amplitude (½CV², ½LI²) —
  there is no L∞ conserved quantity for a 2-state LC tank. So "static RMS = time-average of the dynamical
  energy = L2" should be a theorem *per tank*. This is Grant's thesis and it is physically natural.
- **(F-b) is the knife.** Whether the ceiling is the SUM (L2) across the three A1⊥T2 orthogonal tanks
  (`trampoline-framework.md:246` "acts on the total") or the MAX (L∞, `master-equation.md:101`
  "which constitutive parameter saturates first") is a genuine in-corpus tension. My lean: the shared
  cell-energy budget `V_SNAP²` makes the TOTAL-energy ceiling (L2 sum) natural, and "which-first" is a
  loading-asymmetry (SYM vs ASYM) statement about the *direction* of approach, NOT the norm defining the
  wall — but this must be DERIVED, and the L∞ alternative genuinely tested, not assumed.
- **(F-c) likely leaves a residual.** `A_yield` as a HARD fixed radius (vertical tangent) plausibly ties
  to the Nyquist cell-energy ceiling, but the "hard vs soft/asymptotic" character is a posit unless
  Ax-1 forces the hardness.

**Falsifier of my own expectation:** if the adversarial L∞ pass finds a substrate-native peak/max measure
that reproduces a valid saturation curve AND is consistent with the dynamical energy structure, then even
the "sharpened PARTIAL" softens toward "genuinely postulated with a natural-but-non-unique motivation."
Conversely, if (F-a)+(F-b)+(F-c) ALL close cleanly from Ax1+Ax3, the reduction is FULL (4→3) — a stronger
result than I expect; I must NOT force it (the seductive-positive is the named failure mode).

## 4. The lenses (LOCKED — refocused per §1 onto the OPEN question; settled parts are VERIFY not DERIVE)

**Phase 1 — DERIVE / VERIFY (one agent each, structured output):**
- **L-A (Static↔dynamic bridge — THE CORE, F-a).** Derive whether `A²=ε²+κ²+V²` (static RMS) equals the
  time-average of the dynamical reactive oscillation per tank, so RMS ≡ L2 energy. Surface the
  RMS-vs-instantaneous fork (is the corpus `A²_local=Σ V_inc²` the instantaneous snapshot or the
  envelope/time-average?). Substrate-native: phase-space `(V_inc,Φ_link)` + Cosserat `(u,u̇)`,`(θ,ω)`.
- **L-B (L∞ adversary + 3-sector ceiling, F-b).** Does the ceiling key on the SUM (L2) or MAX (L∞) of the
  three orthogonal A1⊥T2 tank energies? Resolve `trampoline-framework.md:246` (total) vs
  `master-equation.md:101` (which-first). Adversarially test whether an L∞/peak ceiling is EXCLUDED by the
  shared cell-energy budget, or survives.
- **L-C (A_yield ceiling, GAP-2 / F-c).** Is `A_yield` the Axiom-1 Nyquist/bandwidth cell-energy limit
  (`V_SNAP²`) — ceiling inherited, not new? Does Ax-1 force the HARD fixed radius + vertical tangent, or
  is "hard vs soft" a residual posit?
- **L-D (Independent VERIFY of the prior result — read AND run).** Reproduce the 2026-07-02 numerical
  claims: (1) the `L^p`↔kernel 1-to-1 map (a different curve per `p≠2`); (2) the lossless-LC energy-circle
  `x²+y²=1` to machine precision; (3) Born-Infeld = same posit (no independent forcing). Confirm or refute.
- **L-E (Prior-art reconciliation).** State PRECISELY what each prior result closed vs left open, so the
  epic EXTENDS not restates: Q-G47 (operating-point only, not shape); Fork-B (shape-blind observable);
  the "postulated" self-statements; the ν=2/7/K=2G NEGATIVE; Born-Infeld NEGATIVE; AVE-VirtualMedia
  sigmoid (`σ²+r²=1` unit-circle = the same L2 posit in LLM-activation dialect, cross-domain instance
  NOT independent forcing).

**Phase 2 — ADVERSARIAL VERIFY (perspective-diverse, refute-by-default):**
- Per-lens: independent skeptics tasked to REFUTE each lens's derivation (correctness lens +
  substrate-native-leak lens). Refute-by-default; survive only if the attack fails.
- **L∞ SUPER-ADVERSARY (the sharpest attack):** a dedicated agent whose sole job is to BREAK "both faces
  are one L2 object" and to find ANY non-L2 (L∞/peak/L1) measure consistent with BOTH the dynamical
  energy structure AND the static ceiling. If it succeeds, PARTIAL is confirmed and FULL is refuted.
- **Completeness critic:** what's missing — a claim unverified, a sector unchecked, an SM/Cartesian leak?

**Phase 3 — SYNTHESIZE + CLASSIFY (orchestrator, main loop):** verdict FULL vs PARTIAL with the
L∞-adversary outcome; consistency-vs-emergence classification; recommended (HELD) axiom-register status +
canonical restatement.

## 5. Classification commitment (consistency-vs-emergence — META-classification of an axiom's status)

The outcome is tagged on the axiom-register four-value axis:
**{POSTULATED / SHAPE-DERIVED (conditional) / CHALLENGED / DERIVED-TO-THEOREM}**, where **only
DERIVED-TO-THEOREM moves the independent-axiom count 4→3.** Per `consistency-vs-emergence`: I MUST name
explicitly what NEW substrate primitive (if any) does the forcing, and NOT inflate a norm-choice into an
emergence. A norm-choice that is itself a posit is NOT a reduction. The forced part (dynamical LC L2) is a
Class-B axiom-manifestation of Ax1+Ax3; the question is whether the static-argument bridge is
derived-from-master (theorem) or requires-additional-postulate (residual axiom).

## 6. Lane / method discipline

- **Analysis + adversarial verification ONLY. No engine simulation.** LOCKED by the Fork-B finding (§1):
  static localization observables are shape-blind, so a solver run CANNOT discriminate L2 from L∞. The
  small numerical checks (L^p 1-1 map; energy-circle `x²+y²=1`) are numpy-only discriminators, reproduced
  in agent scratch, NOT engine runs.
- **substrate-native-check (prose-derivation, Checkpoints 2/4/6/10):** the L2 norm is the reactance-pair
  energy conservation (CP6); the circle is the K4-TLM unitary eigenvalue (CP2); the ceiling is a Γ=−1
  boundary `Z_core=Z_0√S→0` (CP10, NOT a bulk force); coordinates are phase-space (CP4). Any lens that
  reaches for a Cartesian gradient-descent or continuum-Helmholtz posit is leaking SM.
- **Grant's pre-vetted ontology (kickoff 2026-07-02, recorded per pre-test-physics-check Step 5):**
  *"saturation is both static and dynamic, like all strain we observe today — the static A is the
  time-average of the dynamic oscillation."* This IS the thesis the epic TESTS (not assumes). The one
  refinement the substrate-walk added: `A²=ε²+κ²+V²` spans THREE orthogonal sectors (A1-V, Cosserat-ε,
  Cosserat-κ; A1⊥T2 per `master-equation.md:20`), while the forced-L2 was shown only for the single K4
  `(V_inc,Φ_link)` pair — so the static↔dynamic bridge must hold PER TANK and the ceiling must be shown to
  key on the SUM.
- **Flag-don't-fix; retract-don't-refill:** if a lens's derivation breaks, report the negative; never
  substitute a new derivation to preserve a hoped-for reduction.
- **HOLD canonization:** derive + recommend only. Do NOT edit `axiom-definitions.md` / `eq_axiom_4.tex` or
  restate Axiom 4 as a theorem. Grant rules the canonical change + the axiom-register status flip.

## 7. Decision points → back to Grant (do NOT self-resolve)

1. **Redefine `A` as the dynamical energy-phase?** If FULL reduction requires *redefining* the Axiom-4
   argument `A` from "static 7-mode strain RMS" to "dynamical LC energy-phase," that is a corpus-wide
   canonical redefinition — Grant's call.
2. **Final canonical restatement** of Axiom 4 (theorem vs axiom) + the axiom-register status flip —
   recommend, Grant rules.

## 8. Outputs

- This prereg (frozen) + `2026-07-02_axiom4-reduction-epic_result.md` (per-lens derivations, verdict with
  the L∞-adversary outcome, Q-G47/prior-art reconciliation, recommended HELD axiom-register status +
  canonical restatement).
- Branch + PR of the research doc (NOT a canon change). Report to Grant with verdict + the two decision points.
