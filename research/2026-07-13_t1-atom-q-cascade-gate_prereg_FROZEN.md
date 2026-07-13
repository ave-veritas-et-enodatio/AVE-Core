# T1 — the atom-Q cascade gate — FROZEN PRE-REGISTRATION

**Date:** 2026-07-13 · **Lane:** satellite derivation + numerical consistency driver (self-contained).
**Brief (binding):** `_orchestration/2026-07-13_t1-atom-q-cascade-gate-handoff.md` (Grant GO 2026-07-13).
**Branch:** `derivation/t1-atom-q-cascade-gate` · **PR:** opens `[DO-NOT-MERGE]` (only Grant merges).

**FREEZE-BY-PUSH (Step 3.11).** This prereg lands as its OWN commit, PUSHED to origin, BEFORE any
driver / derivation / result code exists in the tree. The freeze margin is the gap between this
push and the first code push — auditable from the GitHub API push timestamps. No bin, tolerance,
observable, control, or verdict in this document is edited after the first computation runs
(Rule 11).

---

## SECTOR HEADER (declared before any substrate claim)

- **MODE:** derivation-from-canon + numerical consistency driver. **NOT engine-fire.** No new
  primitive; the instrument evaluates a loss channel on x42's *existing* de Broglie dispersion
  (`local_wavenumber_sq`), which x42 rendered but never used to compute a loss-Q.
- **REGIME:** cold lattice, **deep sub-yield** (hydrogen `V_Coulomb(a₀)/(m_e c²) = α² ≈ 5.3×10⁻⁵`;
  `V/V_yield ~ Zα² ≈ 10⁻⁴`, x42 `RESULT.md:24-25`). Axiom-3 sub-yield **losslessness holds** — the
  vacuum is linear and lossless below rupture (`vol4/claim-quality.md:1168`, "linear below rupture,
  dissipative at and above rupture"). No saturation dynamics.
- **PHASE-STATE:** a **bound standing matter-wave** (bulk-modulus longitudinal acoustic mode, the
  **Z_bulk** channel — `de-broglie-standing-wave.md:50`) trapped between its own turning-point
  reflections in the **off-line, source-slaved Coulomb dress** (bin-3 of the impedance-register
  walk: `|Γ|=1` at ω→0, radiates nothing, **no `Re(Z)`** — x42 `RESULT.md:57-58`).
- **SECTOR:** A1 ⊥ T2 respected. The trapping walls are the **longitudinal Z_bulk** channel; the
  radiative loss (spontaneous emission) is the **transverse Z_EM** channel — a *different* sector
  under the three-impedance law (`de-broglie-standing-wave.md:50`: photon→Z_EM, gravity→Z_shear,
  matter-wave→Z_bulk). Charge = Cosserat (2,3) winding, untouched.

---

## Step 1 — derivation target (one sentence)

Derive the **atom's loss-Q** — the `~10⁷` "excited atom" rung of the ring-down Q-ladder
(`keying-register-walk_framing.md:117`, FRAMING walk-estimate, "order-of-magnitude only") — **from
first principles as the insertion loss of the graded Coulomb-dress walls of the atomic
eigencavity**, using x42's existing dispersion machinery, and adjudicate whether the substrate
yields a value **distinct** from the ladder endpoints (electron intrinsic `Q→∞`, loaded
`α⁻¹≈137`, BH QNM `Q~few`) or **collapses onto an endpoint** (the cascade-filter framing is a
vocabulary echo on this rung).

## Step 1.5 — physical picture (mechanical, before equations)

1. **What is trapped, where:** a bound bulk-modulus matter-wave (the electron's de Broglie
   dispersion mode, Z_bulk) confined in the proton's `1/r` Coulomb dispersion well. The "walls"
   are the classical turning points where the local wavenumber `k²(r) → 0` and beyond which
   `k²<0` (evanescent) — `de-broglie-standing-wave.md:42,54`.
2. **Which Γ=−1 boundary, which scale:** the atomic turning-point wall, at the atomic (`a₀`)
   scale, **deep sub-yield**. Per the ring-down framing (`keying-register-walk_framing.md:111`) a
   loss-Q is "how lossily the boundary reflects the confined mode."
3. **Soliton population/topology:** one `0₁`-unknot electron; the mode-count integers `{n,l,m}`
   (embedding/cavity register) are what "quantize" here — NOT the winding `{Q,(2,3)}` (graph
   register). Ionization kills the mode, not the knot (x42 D4).
4. **Scaling:** the dress `V(r) ∝ 1/r`; beyond the outer turning point `V−E → |E_n| > 0` as
   `r→∞` (the well tail vanishes, the state sits *below* threshold), so the forbidden region
   extends to infinity.
5. **Discrete onset vs smooth curve:** the observable is a **ring-down / linewidth** (an AC
   dispersion quantity), not a discrete onset. The BH endpoint gets a finite Q **only** because it
   sits AT/ABOVE rupture where the boundary turns dissipative (`|Γ|<1`); the atom is nowhere near
   rupture.

## WHICH-Q DECLARATION (binding — the Q-glyph guards ≥4 non-interchangeable electron objects)

The Q-glyph ownership row (`theorem-3-1-q-factor.md:158-170`) guards ≥4 electron-scale Q's:
loaded/radiative `137.036` (`:164`), intrinsic `∞` (`:165`), cold-cage ring-down `30.8` (`:166`),
structural radiative floor `29.98` (`:167`), per-mode `Q=ℓ` (`:168`). **The Q derived here is NONE
of these.** It is:

> **`Q_wall(atom)` — the loss-Q of the bound atomic standing mode against its own graded
> Coulomb-dress turning-point walls**, i.e. the cavity's **insertion loss / round-trip
> leakage** of the trapped bulk-modulus (Z_bulk) matter-wave. It is a *cavity insertion-loss*
> object, at the *atomic* scale, on the *longitudinal* channel.

No downstream cite may conflate `Q_wall(atom)` with the electron tank's loaded/intrinsic/cold-cage
Q's, nor with the transverse-EM radiative-decay Q (see the RADIATIVE-CHANNEL note below).

## Corpus state (prior-art inventory — Step 2)

*(cross-repo `ave-corpus-grep` dispatched + integrated 2026-07-13, before this freeze commit.
Verdict: PARTIAL — the x42 machinery exists and is MERGED; the loss-Q is a NOT-YET-DONE follow-on;
no stale cross-repo duplicate of x42/theorem-3-1 exists (both single-homed in AVE-Core). The corpus
PRE-ADJUDICATES my suspected outcome as an α-echo / vocabulary-rhyme — this gate DISCHARGES that
framing-flag with a live driver.)*

**Cross-repo hits that move the prereg:**
- **R2 rhyme pre-adjudicates this exact target** (`AVE-Core-collapse-wt/research/2026-07-10_collapse-target-registry.md:783-788`;
  candidate-gen, `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` — corroborative, NOT authority):
  verbatim "Q-namesake radiative linewidth Δω/ω=α … the tank is reactive (P_real=0, 'rings
  forever') — τ=Q/ω₀ and Δω/ω=1/Q are **dissipative-Q relations and do not transfer to a reactive
  tank; only the tiny R_rad port gives a real linewidth** … Vocabulary-not-mechanism trap"
  (against a "0-for-7 hopeful-interior-mechanism ledger"). **T1's job = upgrade this framing-flag to
  a COMPUTED verdict** (a driver that runs x42's dispersion and demonstrates it), not to re-assert it.
- **★ X41 open-fork CAVEAT — do NOT assert unconditional `|Γ|=1` losslessness.**
  `research/2026-07-10_x41-radiative-scoping-why_RESULT.md:37` routes the held-static-Coulomb
  kernel-transparency to `[UNDERDETERMINED — K1 ∧ K2]`; standing canon `manuscript/ave-kb/CLAUDE.md:75`
  has "a static-E-only drive is ASYMMETRIC … loads the ε/capacitive sector only (S_ε<1, S_μ=1)."
  **Robustness note (load-bearing):** that fork is whether the held dress *reactively LOADS* the ε
  kernel (an `S_ε<1` amplitude/dispersion shift, `~10⁻⁴` in deep-linear H) — it is **NOT** a
  dissipation question. Axiom-3 makes the sub-yield substrate lossless (`Re(Z)=0`); saturation
  `S<1` is a reactive softening, not a resistive loss (`Re(Z)` appears only at/above rupture). So a
  loaded reactive wall is **still lossless** → `Q_wall→∞` regardless of how X41 resolves. Leg A
  computes the transmission directly from x42's dispersion; an `~10⁻⁴` well-depth rescale does not
  make the infinite outer barrier finite. **The kill is robust to the X41 fork; I state the fork,
  and I do not lean on unconditional losslessness — I lean on `Re(Z)=0` sub-yield.**
- **α⁻³ is a KNOWN echo family** (not atomic-linewidth, but the same value-level echo my `Q_rad∝α⁻³`
  joins): `research/2026-06-24_e4-im3-vacuum-distortion.md:104,179` ("the MAGNITUDE rides α⁻³ and AVE
  does not derive α → α-echo at the value level", magnitude `~1.9×10⁷`, coincident with the target),
  `research/2026-07-03_birefringence-flagA-ratio-comparison_note.md:30`. **Symmetric-standard note:**
  QED's coefficient is *equally* α-rooted — the α-echo disqualifies the value as a *cascade-distinct
  filter cutoff*, it is not a double standard against AVE (SM does not make the cascade claim).

**Locally verified anchors** (grepped at base `046d883c` / brief-base `d0037d8f`):

Locally verified anchors (grepped at base `046d883c` / brief-base `d0037d8f`):
- `de-broglie-standing-wave.md:42,50,54` — turning-point reflections are **total** (`|Γ|=1`,
  imaginary impedance); the orbital is a **lossless** resonant impedance match; Z_bulk ≠ Z_EM.
- x42 `RESULT.md:47,57-58,78-86` — eigencavity is **consistency-class, NO new primitive**; dress
  is **bin-3, no `Re(Z)`, radiates nothing**; the frozen-prereg `Z(r)` is the **defect's
  dispersion/index `n(r,ξ)`, NOT a medium impedance** (lattice `Z₀=377Ω` everywhere, Regime I) —
  *the brief's cite of "impedance/mismatch profile Z(r)" at `RESULT.md:84` is the **superseded
  pre-repair** rendering, KEEP-BOTH-logged; the live register is dispersion/index.*
- `keying-register-walk_framing.md:111-118,125` — the Q-ladder; atom `~10⁷` is a FRAMING
  walk-estimate; "linear below rupture, dissipative at/above rupture"; BH finite Q is an
  at/above-rupture object.
- `theorem-3-1-q-factor.md:145-170` — `α⁻¹=137` is the **loaded/radiative** Q (α-baked ECHO), NOT
  intrinsic; **intrinsic `Q→∞` when the EM port is CLOSED (Hermitian)**; loaded-Q derivability
  adjudicated **CIRCULAR/OPEN**.
- `research/2026-06-19_electron-Q-coupled-network_result.md:180-181,205` — precedent, verbatim:
  "a confined reactive mode on a lossless substrate (Axiom 3) has no loss channel ⇒ intrinsic
  `Q→∞` (GATE2 closed-port Q=1.4e16)"; the re-posed loaded-Q test is "ADJUDICATED CIRCULAR."
- `qnm-quality-factor.md:15-20` — BH `Q=ℓ` from Op21 mode-counting at the `Γ=−1` **saturation/TIR**
  boundary (a genuinely distinct *structural* derivation — the DISTINCT-endpoint contrast).

**Corpus state (post cross-repo grep): PARTIAL.** x42 built the dispersion/spectrum but never
evaluated a loss channel; no prior computed atom-`Q_wall` derivation exists (the R2 rhyme is a
framing-flag, not a driver). The over-determined prior from five canonical leaves + the R2
framing-flag is that the sub-yield wall is reactive (`Re(Z)=0`) → `Q_wall→∞`. This gate turns that
prior into a **computed, fireable** verdict.

---

## THE INSTRUMENT (what the driver computes — Step 3 / substrate-native)

Loss rendered as a **BOUNDARY property (Γ, transmission), never a bulk loss term** (substrate-check
Ckpt-10). Three legs, on x42's *own* dispersion `local_wavenumber_sq`:

- **Leg A — wall insertion-loss (Gamow / WKB round-trip leakage), α-free.** For a bound level
  `(Z,n,l)` at energy `E_n<0`, find the outer turning point `r_turn` (`k²(r_turn)=0`) and integrate
  the evanescent decay across the forbidden region:
  `I(R) = ∫_{r_turn}^{R} √(−k²(r)) dr`, `T_outer = exp(−2 I(R))`, `Q_wall = 2π / T_outer`.
  This is the round-trip leakage of the trapped mode through its outer wall — the literal
  "insertion loss of the graded walls." **Uses no α as a Q-seed; the well scale (`a₀`,`Ry`) is
  canonical geometry (x42-identical), and the *result* is α-independent.**
- **Leg B — positive control (Step 3.8a) through the IDENTICAL pipeline.** The SAME
  turning-point-finder + Gamow integrator + `Q=2π/T` run on a **planted finite barrier** (a
  rectangular/finite-width forbidden region with a propagating channel beyond it, a quasi-bound
  resonance) tuned to land `Q ∈ [10⁵,10⁹]`. This proves Leg A **can report a finite intermediate
  Q** — so an atom `Q_wall→∞` is a *physics verdict*, not an instrument that cannot fire (Step 3.10
  fireability).
- **Leg C — quarantined RADIATIVE-CHANNEL diagnostic (NOT a bin-(i) candidate).** The classical
  Lorentz radiative Q of the atomic transition dipole, `Q_rad = (3/2) m_e c² / (α ℏω)`, evaluated
  for Lyman-α — reported ONLY to classify the observed `~10⁷` rung as the transverse-EM
  loaded/radiative port (a **different sector** x42's longitudinal Hermitian eigencavity does not
  express) and to expose it as **α-sourced** (`∝ α⁻³`). This leg USES α — solely to *demonstrate
  the number is the α-echo*, the opposite of seeding a distinct value. It is walled off from Legs
  A/B and never feeds `Q_wall`.

## ANALYTIC EXPECTATIONS (Step 3.9 — the walked picture's predicted numbers, frozen)

- **Leg A (atom):** beyond `r_turn`, `√(−k²) → √(2m|E_n|)/ℏ = 1/(n a₀)` (the known asymptotic
  decay of the hydrogen bound state), so `I(R) ≈ (R−r_turn)/(n a₀) → ∞` **linearly and
  without bound** as `R→∞`. Therefore `T_outer → 0` and **`Q_wall → ∞`**, α-, Z-, and
  n-independent. Predicted: `I(R)` grows linearly (no plateau); at `R=50 a₀`, `n=1`, `I≈48`,
  `T≈e⁻⁹⁶≈2×10⁻⁴²`, `Q_wall≈10⁴²` and *still climbing with R* → the intrinsic endpoint
  (`Q→∞`), NOT a finite plateau.
- **Leg B (positive control):** a rectangular barrier height `Vb`, width `w`, quasi-level at `E`:
  `κ=√(2m(Vb−E))/ℏ`, `T=e^{−2κw}`, `Q=2π/T` — **finite** (parameters frozen in the driver to give
  `Q≈10⁶`, in-window). Confirms fireability.
- **Leg C (radiative diagnostic):** with `ℏω_Lyα = (3/4)Ry = (3/8)α² m_e c²`, the classical
  Lorentz Q is **`Q_rad = 4 α⁻³`** exactly ⇒ `4 × (137.036)³ ≈ 1.03×10⁷`. The QM value (oscillator
  strength `f_Lyα≈0.416`) is `Q_rad/f ≈ 2.5×10⁷ ≈ 9.6 α⁻³` — the measured rung. **`Q_rad ∝ α⁻³`:
  two powers of α from the Rydberg transition scale (`∝α²`), one from the radiative coupling.**
  This is the electron's loaded-Q echo (`α⁻¹`) at a higher power — the same coupling constant, not
  a distinct filter cutoff.

---

## FROZEN BINS (verbatim from the brief) + FROZEN NUMERIC TOLERANCE

- **(i) DISTINCT-Q-DERIVED.** The machinery returns a first-principles value within a pre-named
  tolerance of the observed atomic linewidth-class Q (the `~10⁷` rung). **Kills the relabel-echo.**
  - **FROZEN tolerance (pre-run, no post-hoc widening):** bin (i) fires iff **Leg A returns a
    FINITE `Q_wall ∈ [10⁵, 10⁹]`** (±1 dex around the order-of-magnitude walk-estimate `10⁷`),
    computed **α-free** (no α seed, no normalization to `α⁻¹`). Leg C (`Q_rad`) is **explicitly
    NOT** a bin-(i) candidate — it is α-sourced and is disqualified by the no-α rail regardless of
    its magnitude.
- **(ii) NO-DISTINCT-VALUE.** The machinery runs but returns only endpoint-class or degenerate
  values. **The kill-shape FIRES** — the cascade is a vocabulary echo on this rung.
  - **FROZEN threshold:** bin (ii) fires iff Leg A returns `Q_wall ≥ 10¹²` (collapse toward the
    intrinsic endpoint `Q→∞`) **OR** `Q_wall ≤ 10³` (collapse toward the loaded/cold-cage/radiation
    endpoint cluster `~{30,137}`) **OR** a degenerate value (0, ∞, or a grid artifact with no
    distinct intermediate structure).
- **(iii) MACHINERY-INSUFFICIENT.** An honest instrument gap: x42's eigencavity cannot express the
  loss channel that carries the observed number. **Artifact-class, NOT a physics verdict.** If
  (iii), the deliverable is a named instrument gap.
  - **FROZEN scope:** applies specifically to the **radiative channel** — the transverse-EM
    (`Z_EM`) port that sets the observed `~10⁷` is NOT expressible by x42's longitudinal, bin-3
    (no `Re(Z)`), Hermitian (real-`E`) eigencavity. Any `~10⁷` obtained via Leg C is a *different
    sector*, booked as a bin-(iii) instrument gap on the wall picture (and α-sourced), NOT as a
    bin-(i) pass.

## FIREABLE vs ENTAILED (Step 3.10)

| Bin | FIREABLE / ENTAILED | note |
|---|---|---|
| (i) DISTINCT | **FIREABLE** | Leg A *can* return a finite in-window Q — Leg B proves it on a finite barrier. If the atom's wall had finite insertion loss (finite barrier, or a `Re(Z)` leak in the rendering), bin (i) fires. It does not — a physics fact, not an instrument limit. |
| (ii) NO-DISTINCT (`Q→∞`) | **ENTAILED by the physics the gate names** | A sub-threshold bound state has no open channel ⇒ infinite outer barrier ⇒ `T=0` ⇒ `Q→∞`. When this fires the honest verb is **DEMONSTRATED, not adjudicated**: the run *demonstrates* the sub-yield wall is lossless (the endpoint), which is exactly the kill — the atom rung is structurally forced to be the endpoint, hence not a distinct filter section. |
| (iii) MACHINERY-INSUFFICIENT | **FIREABLE** (for the radiative channel) | x42 either can or cannot express a `Re(Z)` radiative port; it cannot — a checkable structural fact. |

## STRUCTURAL-DEGENERACY SELF-CHECK (Step 3.8b)

Is `Q_wall→∞` forced by a bookkeeping artifact rather than physics? **No** — it is forced by
*physics* (no open channel below threshold), which is the very thing under test, and Leg B (finite
barrier, same pipeline) returns a finite Q, proving the readout is not rigged to ∞. The one genuine
degeneracy risk — a decaying-BC bound-state solver that *cannot* represent leakage — is avoided:
Leg A computes the transmission integral directly (a leakage-capable observable), and Leg B
exercises it on a leaky case.

---

## RAILS (binding)

1. **NEVER seed or normalize from `α⁻¹=137.036`.** That is the electron tank's LOADED/radiative Q
   (Class-B echo, citable as identity only; `theorem-3-1-q-factor.md:164`,`:145-147`). Leg A's
   result is α-independent by construction; Leg C uses α ONLY to *classify the observed rung as the
   α-echo*, never to manufacture a distinct value.
2. **Middle rungs are FRAMING, not canon.** Only the endpoints are canon (electron `Q→∞`
   `keying-walk:115`; BH `Q~few` `:118`). The job is to **upgrade-or-kill** the atom rung, not to
   reproduce the `~10⁷` walk-estimate.
3. **Declare WHICH Q** — done above (`Q_wall(atom)`, the cavity insertion-loss object).
4. **Freeze-by-push** — this prereg is its own pushed commit before any code.
5. **Adversarial review wrapper** — the PR gets `ave-adversarial-pr-review` via a `scriptPath`
   wrapper that inlines ARGS (the named-workflow args path silently drops args).
6. **DO-NOT-MERGE** — PR opens `[DO-NOT-MERGE]`; only Grant merges.

## Discriminating outcomes + AC/DC sector classification (Step 3, v1.5)

- **Outcome A (most likely, my disclosed leaning): bin (ii) fires on Leg A** — `Q_wall→∞`, the
  intrinsic endpoint, α-free, DEMONSTRATED. **+ bin (iii) rider on Leg C** — the `~10⁷`-carrying
  radiative port is a different sector x42 can't express, and is α-sourced (`α⁻³` echo). Verdict:
  the cascade-filter framing has **no distinct content at the atom rung** — on the wall channel
  it's the lossless homogeneous line relabeled; on the radiative channel it's the α-echo at a
  higher power. **The kill-shape fires; I do NOT rescue it.**
- **Outcome B (would be a genuine surprise): bin (i) fires** — Leg A returns a finite α-free
  `Q_wall ∈ [10⁵,10⁹]`. Then the cascade has real content at the atom rung and this is a chord. I
  am open to this; the driver adjudicates.
- **Outcome C (null of the instrument): Leg B fails to return a finite Q** — the instrument can't
  fire bin (i) at all ⇒ the whole gate is unfireable ⇒ rework before verdict (would invalidate the
  run, not the framing).

**AC/DC sector (`clm-acdc07`):** the loss-Q / ring-down is a **pure-AC dispersion quantity** →
per the carve it **cannot be a framework-level empirical discriminator**, and a null here is *not*
an axiom falsification. This gate is an **internal FRAMING-coherence test** (does the cascade
relabel carry distinct content?), and its kill is a **framing demotion**, explicitly NOT a
falsification of any AVE axiom.

## Falsifier (what would show MY framing wrong)

If Leg A returns a finite, α-free `Q_wall` near `10⁷` (bin (i)), my "lossless sub-yield wall →
endpoint" framing is wrong and the cascade has content — I report the chord. If an adversarial lens
surfaces a legitimate α-free finite-Q leakage channel through the *walls* (not the transverse
radiative port) that I missed, the kill is a false-kill and must be withdrawn.

## Skill-selection plan (60-sec, pre-workstream)

APPLIED: **ave-prereg** (this doc), **ave-canonical-leaf-pull** (Q-factor class — 6 leaves pulled),
**substrate-native-check** (loss as boundary Γ/transmission, not bulk term; Ckpt-10),
**phase-space-coordinate-check** (impedance/transmission register — matched, not real-space),
**consistency-vs-emergence** (consistency/instrument-gap class, no emergence, negative result),
**ave-canonical-source** (constants from `ave.core.constants`), **ave-driver-script-honesty**
(driver reports `Q→∞`/endpoint honestly, no "AVE predicts 10⁷" print), **ave-discrimination-check**
(SM-counterfactual + false-kill guard at adjudication), **ave-adversarial-pr-review** (PR gate),
**ave-worktree-paths** (worktree-absolute paths throughout). NOT-fired: engine/loop-gap skills
(no engine-fire), pre-test-physics-check dispatch trigger (ontology fixed by Grant in the brief;
the one load-bearing reframe — walls are lossless bin-3, the number lives in a different transverse
sector — is surfaced in this prereg and the RESULT).
