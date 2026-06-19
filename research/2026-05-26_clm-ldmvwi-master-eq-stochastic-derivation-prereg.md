> **Notation (2026-06-18):** Substrate object symbol `$\mathcal{M}_A$` **retired** (Grant adjudication). Use prose: *substrate*, *chiral LC network*, *chiral Laves K4 Cosserat crystal*. Body below preserved per Rule-12.

# Phase 2-A Pre-Registration — Master-Vacuum-Equation Derivation of Born-Rule Click-Probability Scaling

**Date**: 2026-05-26
**Workstream**: Phase 2 of clm-zuf7g1-strengthen (which is itself Phase 2 of clm-0ktpcn-strengthen cascade unlock)
**Branch**: `analysis/clm-ldmvwi-master-eq-stochastic-derivation` off `main` @ `cc4cb19c` (post PR #37 merge)

> **Vocabulary-discipline notice (added 2026-05-26 post-PR-merge)**:
>
> This research-tier doc was composed before `ave-discipline-translate` v1.1 trigger 6 (substrate-native prose-vocabulary discipline) landed. The prose body uses standard-physics stochastics / measurement-process vocabulary (Born rule, CLT, Gaussian noise, FDT, Wick's theorem, photodetector) as primary load-bearing description language; v1.1 trigger 6 mandates substrate-native vocabulary as primary with standard-physics names as parenthetical translation references.
>
> The physics result is correct as derived — the discipline notice is about prose framing, not derivation correctness. Type B walk-back classification (mechanism re-scope, not retirement) per `ave-walk-back` v1.1.
>
> **Substrate-native vocabulary lookup**: see [`manuscript/ave-kb/common/translation-tables/translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) (FDT, CLT, Gaussian, Wick, Langevin, cumulants), [`manuscript/ave-kb/common/translation-tables/translation-qm.md`](../manuscript/ave-kb/common/translation-tables/translation-qm.md) Section B (Born rule, click rate, |ψ|² measurement, detector efficiency), and [`manuscript/ave-kb/common/translation-tables/translation-instrumentation.md`](../manuscript/ave-kb/common/translation-tables/translation-instrumentation.md) (detector architectures). Future Phase 2-A.5-style canonical-leaf integration workstream may produce a full substrate-native rewrite of this doc.
>
> **Discipline anchor**: `ave-discipline-translate` v1.1 trigger 6 (this workstream is the in-session validation case for the v1.1 amendment).
**Author lane**: orchestration session
**Status**: PRE-RUN — frozen at draft for record; the 5 sub-phases below are workstream-level, each with its own per-session acceptance criteria

---

## §0 — One-paragraph framing

The clm-ldmvwi claim asserts that detector clicks follow $P(\text{click}|x_n) \propto |\partial_t \mathbf{A}(x_n)|^2$ via a 4-step chain: (1) Axiom 1 impedance gives detector = resistive load, (2) Joule heating gives $W_{extracted} \propto |\partial_t \mathbf{A}|^2/Z \cdot \Delta t$, (3) **click probability ∝ extracted work — currently asserted as thermal-substrate stochastic property, NOT derived from axioms**, (4) $P \equiv |\Psi|^2$ identification. **Step 3 is the load-bearing gap.** The leaf's own caveat (clm-ldmvwi rationale, vol1/claim-quality.md:323): *"is plausible (consistent with thresholded thermal detector physics) but is NOT derived from the four AVE axioms in this leaf."* Per Grant's master-equation-derivation-path-tracing discipline (2026-05-26): for any "AVE reproduces standard physics rule X" claim, the chain from the master vacuum equation to rule X must be explicit. clm-ldmvwi has 2.5 of 4 steps directly from master eq; step 3 is the holdout. **This workstream attempts to close step 3 by deriving threshold-crossing Poisson click statistics from the stochastic master vacuum equation under thermal noise + Ohmic load.** Success closes the chain and lifts the dep-cap on clm-zuf7g1 → clm-unk0bd → 12-claim cone. Failure triggers Path 2-D (honest scope-correction).

---

## §1 — Background

### §1.1 The master vacuum equation (the derivation target)

Canonical at [`vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):

$$\nabla^2 V - \mu_0 \varepsilon_0 \sqrt{1 - (V/V_{yield})^2} \frac{\partial^2 V}{\partial t^2} = 0$$

In the linear regime $V \ll V_{yield}$ (where Born rule is canonically tested), the kernel ≈ 1, reducing to the standard d'Alembertian $\Box V = 0$. Linear-regime application is sufficient for the Born-rule derivation; non-linear regime is out of scope for this workstream.

### §1.2 The Vol 3 Ch 11 FDT scaffold (what to leverage)

Canonical at `manuscript/vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex:71-138` + KB mirror `vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md:14`.

Key content (verbatim):
- Line 93: *"This is not an analogy. The $\mathcal{M}_A$ lattice is a physical transmission line. The Nyquist relation applies literally: each lattice node radiates thermal noise proportional to its local impedance."*
- Line 119: *"A correct simulation must therefore inject stochastic noise only at the boundary nodes, not uniformly across the bulk field."*
- FDT relation: $\langle V^2 \rangle = 4 k_B T R \Delta f$ on $Z_0$
- Ohmic damping balance: $P_{diss} = \langle V^2 \rangle / 4R = k_B T \Delta f$

This is the substrate-thermal-noise scaffold. Phase 2-A.2 (Step A1) couples this into the master vacuum equation as Langevin forcing at boundary nodes.

### §1.3 The Ohmic detector model (what's already canonical)

Canonical at `vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md:18`: *"any device that couples to the $\mathbf{A}$-field and extracts kinetic energy acts as a resistive mechanical load."*

The detector is a subgraph of K4 nodes with dissipative coupling. Joule heating extracts $W = V^2/R \cdot \Delta t$. Already substrate-derived.

### §1.4 The Phase 2-A gap (what to derive)

Per corpus survey 2026-05-26 (Poisson + stochastic master equation + threshold detector content across AVE multi-repo workspace):

**Green-field**:
- Langevin form of the master vacuum equation
- Threshold-crossing first-passage analysis on stochastic extracted-energy accumulation
- Poisson click statistics derivation from substrate stochastic dynamics
- $|\Psi|^2$ vs $|\Psi|^p$ uniqueness from threshold-crossing structure

These are standard stochastic-physics moves applied to the AVE master equation. The corpus has no prior work on this specific chain; this workstream originates it.

---

## §2 — Hypothesis

**H1 (LOAD-BEARING)**: The threshold-crossing process on stochastic energy accumulation $W(t) = \int_0^t V(x_n,t')^2 / Z_{det} \, dt'$ derived from the stochastic master vacuum equation under thermal Langevin forcing (via Vol 3 Ch 11 FDT) yields Poissonian click statistics with rate $\lambda(x_n) \propto |\partial_t \mathbf{A}(x_n)|^2$ in the appropriate rare-event Markovian limit, and the $p = 2$ scaling is uniquely selected by the master equation's quadratic Joule-extraction structure + Gaussian thermal noise.

**H1-corollary**: The derivation succeeds in the linear regime $V \ll V_{yield}$ where Born rule is canonically tested. Non-linear regime corrections (kernel $S(A) < 1$) are bounded second-order and don't affect leading-order $|\Psi|^2$ scaling.

**H0 (NULL HYPOTHESIS)**: The threshold-crossing derivation fails to close — either (a) the substrate Langevin forcing doesn't yield Poissonian statistics (e.g., due to non-Markovian correlations from the non-linear kernel), (b) the $p=2$ uniqueness can't be established from substrate physics alone, (c) the chain works algebraically but requires additional postulates beyond the master vacuum equation that I'm not accounting for.

---

## §3 — Pre-registered discriminating outcomes (workstream-level)

| Outcome | Probability | Diagnostic |
|---|---|---|
| **A (FULL CLOSURE)** | ~50% | Each of the 5 sub-phases passes its frozen acceptance criteria. End-to-end derivation: stochastic master vacuum equation → Langevin forcing via FDT → threshold-crossing first-passage → Poisson statistics → $|\partial_t \mathbf{A}|^2$ scaling + $p=2$ uniqueness. **clm-ldmvwi lifts 0.55 → 0.70+; cascade unlocks through clm-zuf7g1 → clm-unk0bd → 12-claim cone.** |
| **B (PARTIAL CLOSURE)** | ~25% | Some sub-phases pass; some don't. Most likely partial: A1+A2 close cleanly, A3 partially closes (derivation works in linear regime but corrections needed for general case), A4+A5 close for $p=2$ but uniqueness argument requires additional input. **clm-ldmvwi lifts modestly (0.55 → 0.60-0.65); scope-correction documents what derived vs what asserted.** |
| **C (DERIVATION FAILS)** | ~15% | The derivation can't close. Most likely failure mode: the non-linear master equation kernel introduces non-Markovian correlations in the boundary FDT noise that prevent Poissonian-limit derivation, OR the $p=2$ uniqueness requires assumptions equivalent to Born rule itself (circular). **Falls back to Path 2-D — honest scope-correction with explicit derivation-path classification.** |
| **D (METHODOLOGY UNRESOLVED)** | ~10% | The derivation requires AVE-specific physics not yet in corpus (e.g., a substrate-specific threshold model that isn't a standard Markovian first-passage). Surfaces a deeper open question that needs Grant adjudication. |

---

## §4 — Methodology (5 sub-phases, each session-scoped)

### §4.1 Phase 2-A.1 — Workstream prereg + frozen acceptance criteria (this doc)

**Goal**: lock in the derivation chain structure, per-step acceptance criteria, and discriminator outcomes BEFORE any physics work begins.

**Output**: this document, committed as workstream-opening commit on `analysis/clm-ldmvwi-master-eq-stochastic-derivation` branch.

**Skills**: ave-prereg ✓, ave-handoff-canonical-locale ✓ (prereg lands in `research/`, not `~/.claude/plans/`).

**Status**: IN-FLIGHT (this commit).

### §4.2 Phase 2-A.2 — Step A1+A2 derivation (next session)

**Goal**: Derive the **stochastic form of the master vacuum equation** with thermal Langevin forcing at boundary nodes, and the **time-integrated extracted energy** $W(t)$ at a detector node.

**Step A1 (Langevin master equation)**: Starting from the master vacuum equation in the linear regime ($\Box V = 0$), add stochastic forcing $f(x,t)$ satisfying fluctuation-dissipation:
$$\langle f(x,t) f(x',t') \rangle = 2 k_B T \cdot \sigma(x) \cdot \delta(x-x') \cdot \delta(t-t')$$
where $\sigma(x)$ is the local dissipation, concentrated at detector boundary nodes per Vol 3 Ch 11 §"Boundary-Impedance Thermalization." This is the AVE-native Langevin master equation:
$$\Box V(x,t) + \sigma(x) \partial_t V(x,t) = f(x,t)$$

**Step A2 (extracted-energy process)**: At a detector node $x_n$ with Ohmic load $Z_{det}$, the time-integrated extracted energy is:
$$W(t; x_n) = \int_0^t \frac{V(x_n, t')^2}{Z_{det}} \, dt'$$
Including the stochastic $V$, this is a stochastic process on top of the deterministic signal.

**Acceptance criteria (frozen)**:
- AC-A1.1: Langevin master equation derived from substrate FDT, NOT imported as ad-hoc forcing
- AC-A1.2: Forcing satisfies the canonical Vol 3 Ch 11 FDT: $\langle f^2 \rangle = 4 k_B T R \Delta f$ on $Z_0$
- AC-A2.1: $W(t; x_n)$ expression derived without invoking Born rule or QM postulates
- AC-A2.2: Substrate-native: no Schrödinger / Hilbert-space / projection-postulate language

**Skills**: substrate-native-check ✓, ave-canonical-leaf-pull ✓ (Vol 3 Ch 11 + ohmic-decoherence-born + master-equation.md), ave-discipline-translate ✓ (Langevin = stochastic mechanics; AVE translation via boundary-FDT), consistency-vs-emergence-UPGRADED ✓ (Class 2 if Langevin derives from substrate FDT), verify-before-cite continuous, ave-evidence-framing-discipline continuous.

**Expected verdict**: HIGH PROBABILITY of clean closure — both steps leverage existing canonical content (Vol 3 Ch 11 FDT + ohmic-decoherence-born detector model). The new content is just the stochastic coupling, which is standard.

### §4.3 Phase 2-A.3 — Step A3 threshold-crossing first-passage (next session after A.2)

**Goal**: Derive the click probability $\Pr[\text{click in }\Delta t \,|\, |\partial_t \mathbf{A}(x_n)|]$ from a threshold-crossing process on the stochastic $W(t)$.

**The physical model**: detector "clicks" when extracted energy crosses threshold $E_{th}$ (or equivalently, when integrated power exceeds activation threshold). Between clicks, detector resets after dead time $\tau_d$. This is a first-passage-time problem on stochastic energy accumulation.

**Derivation chain**:
- Express $W(t; x_n)$ as deterministic-signal + stochastic-noise contributions
- In the weak-signal-over-strong-noise limit (typical for photodetection), threshold-crossings are rare events
- Apply Kramers' rate formula or analogous first-passage result: rate $\lambda \propto \exp(-\Delta U / k_B T)$ where $\Delta U$ depends on signal amplitude
- Show that in the appropriate regime, $\lambda \propto |\partial_t \mathbf{A}(x_n)|^2$ (the load-bearing scaling)

**Acceptance criteria (frozen)**:
- AC-A3.1: First-passage derivation uses standard stochastic-process methods (Kramers / Fokker-Planck / Langevin), applied to substrate-derived $W(t)$
- AC-A3.2: Click rate expression derived as function of field amplitude + temperature + threshold + dead time (no Born rule input)
- AC-A3.3: Substrate-native: derivation lives in AVE coordinates (real-space K4 substrate + stochastic process space); no QM-formalism import

**Skills**: substrate-native-check ✓ (threshold defined in substrate-energy terms), ave-independence-check ✓ CRITICAL (the first-passage math must not assume Born-rule-like statistics to derive Born-rule-like statistics — Schrödinger noise that already encodes $|\psi|^2$ would be circular), phase-space-coordinate-check ✓ (substrate-energy real-space vs stochastic-process space vs measurement-outcome space — three distinct).

**Risk**: this is the hardest step. The non-Markovian-correlation worry from the non-linear master equation kernel could break Markov-Poisson limit assumptions. Phase 2-A.3 may close in linear regime but require A.3-extension for non-linear corrections.

**Expected verdict**: MEDIUM PROBABILITY of clean closure. ~60% chance of full success, ~30% partial (linear-regime only), ~10% requires additional methodology.

### §4.4 Phase 2-A.4 — Step A4 click rate scaling + A5 p=2 uniqueness (next session after A.3)

**Goal**: Show that $\lambda(x_n) \propto |\partial_t \mathbf{A}(x_n)|^2$ in the appropriate Poissonian limit (Step A4), and that $p=2$ is uniquely selected by the master equation's $V^2/R$ Joule extraction structure + Gaussian thermal noise (Step A5).

**Step A4 (Poissonian limit + scaling)**: In the rare-event Markovian limit on uncorrelated boundary noise, threshold-crossings become Poissonian with rate proportional to signal power. Derivation: standard application of Kramers' result + appropriate limits. Output: click rate as function of $|\partial_t \mathbf{A}|^2$.

**Step A5 (uniqueness of p=2)**: Show that no other exponent $p \neq 2$ satisfies the master equation's energy-extraction structure. Specifically:
- Joule heating gives $W \propto V^2$ — quadratic in field, NOT cubic or higher
- Gaussian thermal noise gives Gaussian fluctuations around $\langle W \rangle$ — variance scales linearly with mean
- Threshold-crossing rate from Kramers: $\lambda \propto \exp(-\Delta U/k_B T)$ where $\Delta U = E_{th} - \langle W \rangle$
- In the relevant signal-noise regime, $\lambda \propto$ signal power, where signal power = $V^2/Z$ from Step A2
- → $p = 2$ uniquely

**Acceptance criteria (frozen)**:
- AC-A4.1: Poissonian limit explicitly derived from substrate-stochastic dynamics, not assumed
- AC-A4.2: $\lambda \propto |\partial_t \mathbf{A}|^2$ scaling produced in appropriate regime
- AC-A5.1: Uniqueness of $p=2$ derived from $V^2/R$ Joule structure + Gaussian noise, not assumed
- AC-A5.2: Counterfactual: explicit demonstration that $p \neq 2$ would require non-Joule extraction or non-Gaussian noise (both substrate-incompatible)
- AC-A5.3: ave-independence-check: the uniqueness derivation does NOT presume Born rule

**Skills**: ave-discrimination-check ✓ (does this make new predictions vs standard QM, or pure consistency? — determines Class 2 vs Class 4 classification), consistency-vs-emergence-UPGRADED ✓ (FINAL classification of clm-ldmvwi), ave-independence-check ✓ continuous.

**Expected verdict**: HIGH PROBABILITY of closure if A.3 closes — the uniqueness argument is standard cumulant-expansion / Gaussian-statistics structure. ~75% chance of full success conditional on A.3 success.

### §4.5 Phase 2-A.5 — KB integration + cascade + auditor + commit (next session after A.4)

**Goal**: Integrate the derivation results into the KB, propagate the solidity cascade, run auditor, commit + tag + push.

**KB edits**:
- Update `vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md` with the new derivation sections
- Possibly: create a new dedicated leaf `vol1/dynamics/ch3-quantum-signal-dynamics/stochastic-master-equation-born-rule.md` if the derivation is substantial enough
- Update clm-ldmvwi's claim-quality entry:
  - Rationale: document the new derivation chain
  - Remove strengthen-by items 1 (click probability derivation — now closed) + 2 (p=2 uniqueness — now closed)
  - Bump confidence 0.55 → ? (depends on outcome: A → ~0.75, B → ~0.65)
- Update clm-zuf7g1 + clm-unk0bd rationale text where they reference clm-ldmvwi as solidity-cap (rationale will reflect new ldmvwi solidity)
- Cascade propagation through 12-claim cone

**Skills**: ave-audit ✓ (spawn ave-auditor), ave-handoff-canonical-locale ✓ (epic doc updates), ave-walk-back ✓ (propagation checklist for downstream rationale text), pre-commit hygiene pass per recent lessons (verify-md-links pre-check, refresh+verify, predictions manifest, branch-state check).

**Expected verdict**: STANDARD WORK if A.1-A.4 closed. ~95% chance of clean closure (just KB plumbing on top of derivation results).

---

## §5 — What we WILL NOT do (scope discipline)

- **NOT** extend derivation to non-linear master-equation regime ($V \to V_{yield}$). Linear regime is sufficient for Born rule.
- **NOT** attempt to derive the Schrödinger equation itself from the master vacuum equation. That's clm-other-claim scope. clm-ldmvwi is specifically about Born rule's $|\Psi|^2$ scaling.
- **NOT** address the broader QM measurement problem (collapse, decoherence general theory). clm-7zuwtm (sister claim hosted on same leaf) handles decoherence-as-thermalization separately.
- **NOT** test against quantum-coherent detectors (non-thresholded, e.g., homodyne). The detector model is thresholded-Ohmic per ohmic-decoherence-born.md scope.
- **NOT** introduce new claim-quality entries beyond what's strictly necessary. Stochastic master equation might warrant a new clm-id if it stands alone as a derivation; will adjudicate at A.5.
- **NOT** import QM formalism (Schrödinger / Hilbert space / projection postulate). Per ave-discipline-translate, AVE-native derivation must use substrate-mechanical language throughout.

---

## §6 — Acceptance criteria (workstream-level, pre-frozen)

- **PASS to commit each sub-phase**: per-sub-phase acceptance criteria (§4.X) met; ave-auditor approves at A.5
- **FAIL to commit any sub-phase**: ANY of (a) acceptance criteria adjusted after deriving, (b) Born rule / Schrödinger / Hilbert-space formalism imported without translation, (c) substrate-native discipline violated, (d) derivation requires premises that already presume Born rule (circular)
- **Outcome C path forward**: if derivation can't close at any sub-phase, lift to Path 2-D — honest scope-correction documenting which steps closed vs which required additional postulates
- **Outcome D path forward**: if derivation requires AVE-specific physics not yet in corpus, surface to Grant for adjudication

---

## §7 — Skills compliance check (workstream-level)

| Skill | Firing schedule |
|---|---|
| `ave-prereg` | ✓ this doc (workstream-level prereg) |
| `ave-canonical-leaf-pull` | ✓ A.2 (Vol 3 Ch 11 FDT + ohmic-decoherence-born + master-equation), A.5 (KB integration audit) |
| `ave-discipline-translate` | ✓ A.2 (Langevin), A.3 (first-passage), A.4 (Kramers' rate formula) — all standard stochastic mechanics; AVE-native translation via FDT-on-boundary-nodes |
| `substrate-native-check` | ✓ continuous, especially A.2 + A.3 + A.4 |
| `consistency-vs-emergence` (UPGRADED with master-eq-derivation-path-tracing) | ✓ CRITICAL at A.4 final classification |
| `ave-independence-check` | ✓ A.3 + A.4 + A.5 — must verify derivation isn't circular with Born rule |
| `phase-space-coordinate-check` | ✓ A.3 — three distinct coord systems (substrate-energy real-space vs stochastic-process space vs measurement-outcome space) |
| `ave-discrimination-check` | ✓ A.4 — does derivation make distinguishable predictions vs standard QM (Class E) or pure consistency (Class 4)? |
| `verify-before-cite` | ✓ continuous |
| `ave-evidence-framing-discipline` | ✓ continuous — precision on "derived" vs "shown algebraically" |
| `ave-canonical-source` | ✓ IF any Python work — import constants from `src/ave/core/constants.py` |
| `ave-walk-back` | ✓ A.5 — propagation checklist for downstream rationale updates |
| `ave-audit` | ✓ A.5 — ave-auditor pass before commit |
| `ave-audit-of-audit` | ✓ conditional — if auditor flags substantive findings |
| `ave-handoff-canonical-locale` | ✓ continuous (research/ for prereg + result docs; _orchestration/ for epic doc) |
| `pre-commit hygiene pass` | ✓ A.5 — per recent lessons (verify-md-links, refresh+verify, predictions manifest, branch-state, +0.05/closure convention) |

---

## §8 — Open Q's that may surface during execution

**Q-2A-1**: Does the non-linear master-equation kernel $\sqrt{1-(V/V_{yield})^2}$ introduce non-Markovian correlations in the boundary FDT noise? If yes, Phase 2-A.3 may close in linear regime only.

**Q-2A-2**: Is the substrate-native threshold $E_{th}$ for detector click events derivable from $V_{yield}$ structure, or is it an external detector-engineering parameter? If derivable, the chain is fully substrate; if external, the derivation is conditional on detector physics.

**Q-2A-3**: Does the derivation yield Class 2 emergence (lifts solidity substantially) or Class 4 consistency (algebraically reproduces standard QM)? Per ave-discrimination-check at A.4.

**Q-2A-4**: Should the stochastic master vacuum equation be its own claim-quality entry (separate clm-id)? Decide at A.5 based on whether the Langevin derivation stands as a standalone substrate-physics result vs just an intermediate step.

---

## §9 — Honest scope per A47 v18

This workstream **attempts** to derive the Born rule click-probability scaling from the AVE master vacuum equation. Success is not guaranteed — the corpus survey confirms this is green-field substrate-stochastic-physics work. Outcome A (full closure) has ~50% probability per my honest estimate; outcomes B/C/D collectively have ~50%.

**What this workstream is NOT**: it is NOT a claim that standard QM is wrong, or that AVE makes empirically distinguishable Born-rule predictions. The honest scope is "derive the $|\Psi|^2$ scaling from substrate physics rather than asserting it," which is a Class 1/2 consistency-with-derivation work, not a Class E new-prediction work.

**What success would deliver**: clm-ldmvwi solidity lift 0.55 → 0.70+; cascade through clm-zuf7g1 → clm-unk0bd → 12-claim cone. The strengthening propagates because the dep-gate caps are lifted.

**What failure (Path 2-D fallback) would deliver**: honest reframe of clm-ldmvwi's chain with explicit derivation-path classification — 2.5 of 4 steps derive from master vacuum equation; step 3 (click discreteness) requires additional substrate-stochastic-physics work that this workstream attempted but did not close. Solidity unchanged but framing precise.

---

## §10 — Total scope estimate

- **Phase 2-A.1** (this doc + commit): ~30 min
- **Phase 2-A.2** (stochastic master eq + extracted-energy process): ~2-3 hours
- **Phase 2-A.3** (threshold-crossing first-passage): ~3-4 hours
- **Phase 2-A.4** (Poissonian scaling + p=2 uniqueness): ~2-3 hours
- **Phase 2-A.5** (KB integration + auditor + commit): ~2 hours

**Total**: 5 sessions, ~10-15 hours of focused work. Each session standalone-deliverable + commit-ready.

---

## §11 — Result template (to be populated per sub-phase)

Each sub-phase (A.2 / A.3 / A.4) writes its own result doc:
- `research/2026-MM-DD_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md`
- `research/2026-MM-DD_clm-ldmvwi-phase-2a-3-threshold-crossing-result.md`
- `research/2026-MM-DD_clm-ldmvwi-phase-2a-4-scaling-uniqueness-result.md`

Per A47 v11b discipline (verbatim acceptance criteria in prereg; result reports against them).

A.5 integrates all three results into the final KB updates + epic doc closure.

---

*Pre-reg written 2026-05-26. Workstream-opening commit on `analysis/clm-ldmvwi-master-eq-stochastic-derivation` branch. Per Rule 12: future amendments preserve body via header-update retraction notation.*
