# EM keying ROUND 3 — the ε-side DC-mechanism: CHARGE-KEYED vs EXCURSION-KEYED — PRE-REGISTRATION [FROZEN]

**Date:** 2026-07-06 · **Lane:** implementer · **Branch:** `analysis/em-keying-round3-eps-dc-mechanism`
**Class:** DERIVATION of the ε-grade keying MEMBER within the amplitude class (derive-or-kill / prove-or-disprove).
No claim minted until the derivation + the four mandatory sub-answers + the constraint evaluations complete.

**The open-goal question (verbatim from the fire order):** determine FROM THE CANONICAL VACUUM NETWORK
STRUCTURE ALONE whether the ε-grade (transverse-T2 permittivity channel) nonlinearity keys on

- **(H1) the PARKED displacement** — charge/stretch, DC-included, **mean-square** `⟨A_V²⟩`, OR
- **(H2) the EXCURSION about an adapted quiescent point** — AC-only, **variance** `Var_t(A_V)`.

Round 2 (`research/2026-07-05_em-keying-round2-worked-cell_RESULT.md`, [SELECTED-NOT-DERIVED]) DERIVED the
amplitude CLASS over the rate (`𝒲_beat` killed) but showed the LC ledger cannot pick variance vs
mean-square within the class; the variance member is currently **[SELECTED-NOT-DERIVED]**. Round 3
derives the member or proves it underivable.

## HARD BLINDNESS RULE (binding on the entire derivation chain §1–§8)

The derivation may NOT reference the muonic-H result, CREMA, #539, Table I, PVLAS, or any experimental
survival. Those enter ONLY in the clearly-firewalled §9 COMPARISON. If any step chooses structure
because it survives an experiment, that is the round-1/round-2 defect — stop and bin honestly. No tuning
to reproduce `0.046` or any known number (½/¼ over-determination = coincidence tell).

---

## 0. REGIME HEADER (mandatory; declared UP FRONT per the fire order (v))

- **MODE:** bias-then-small-signal (the standard EE nonlinear-reactive workflow: set DC bias → linearize
  → read AC), applied to a single vacuum LC cell and its probe.
- **SECTOR:** the **ε-grade = transverse-T2 permittivity channel** of the EM `Z_EM=√(μ_eff/ε_eff)` (the
  varactor `C_eff=C₀/S(A_V)`, `ε_eff=ε₀S(A_V)`; `node-up-small-large-signal.md`:49,:104-106,:117-118).
  Per the round-2 review's adjudication (node-up:117-118 pins the statement to the ε-grade / transverse-T2
  permittivity channel), THIS is the channel in question.
- **OUT OF SCOPE (stated so no reviewer cross-wires):**
  - the **A1 dilatation-MASS varactor** (`C_eff=C₀/S`, keyed on `A≡V/V_snap`, the longitudinal-A1 bond
    compliance; `CLAUDE.md`:73, device-circuit-models:60) — a DIFFERENT reactance (A1⊥T2).
  - the **mechanical Q-point sector** (bond-strain / ρ_eff / transverse-tangent-stiffness).
  - **an E-GRADIENT's mechanical FORCE on cells** — that is the A1/mechanical momentum ledger
    (pressure on the cage), a DIFFERENT ledger; explicitly out of scope here.
- **PHASE-STATE:** deep-cold vacuum, small operating point `A_V≪1`; probe about it. R2 static-E route
  (`S_ε<1, S_μ=1`) for the held case vs a propagating pump for the worked case.
- **Homonym guard.** "A²" is overloaded: (i) Ax4 kernel argument (phase-space reactance coord, A46),
  (ii) the Letter's `(E/E_c)²`, (iii) mechanical bond strain, (iv) round-1 transport `𝒯`, (v) round-2
  worked content `𝒲`. This round's object is the ε-grade kernel argument `A_V=V/V_yield=|E|/E_yield`; the
  two candidate MEMBERS within the amplitude class are the **mean-square** `⟨A_V²⟩` (H1) and the
  **variance** `Var_t(A_V)=⟨A_V²⟩−⟨A_V⟩²` (H2). Named distinctly throughout.

## 0.1 GATES ON (verify-before-cite; grepped live at worktree HEAD `d70446ae`)

- **Round-2 RESULT + prereg** `research/2026-07-05_em-keying-round2-worked-cell_{RESULT,prereg_FROZEN}.md`:
  amplitude CLASS DERIVED (`𝒲_beat` killed by frequency-independence of the reactive-energy swing); within
  `{𝒲_var, 𝒲_ms}` the LC ledger cannot discriminate; the held-DC discriminating input picks the
  MEAN-SQUARE (`1−S(0.3)=0.046 ≠ 0`); variance member [SELECTED]. B-side [WORKED-DERIVED] (Lenz).
  The frozen round-2 STEP-1 enumeration (prereg:149-153) names exactly H1/H2/H3.
- **The keyed-argument duality (microfoundation)** `node-up-small-large-signal.md`:§1 (LC tank
  `L_cell=μ₀ℓ`, `C_cell=ε₀ℓ`, `ω_C=1/√(LC)=c/ℓ`), :104-106 (ε-varactor `C_eff=C₀/S(A_V)`, `A_V=V/V_yield`),
  :117-118 (ε keys on the **field amplitude V~E**, a *potential* variable; "A DC bias is a real operating
  point"), :119-123 + :364 (µ keys on **circulation** induced by `∂_tB`, Lenz; static B → no dI/dt →
  `A_I=0` → `S_μ=1` **analytically exact** — the CANON-EXACT B-side template), :125-129 (A46: `A_V`,`A_I`
  are PHASE-SPACE reactance coords), :217-221 (R2: "a static E is a real operating-point bias for the
  V-keyed varactor — it loads ε and shifts n").
- **The LC TOPOLOGY (load-bearing for M1)** `device-circuit-models.md`:52 (`L_cell=μ₀ℓ`, `C_cell=ε₀ℓ`);
  `per-dof-vacuum-node-circuit.md`:30-34 (`C_i=ε₀ℓ` is the **node capacitance to baseline** = SHUNT;
  `L_i=μ₀ℓ` the bond inductor); `relativistic-inductor.md`:15,§("Why SPICE Cannot Exceed c") (the SERIES
  inductor limits `dI/dt`). The small-signal-vs-large-signal varactor split `C_eff=C₀/S` vs `C_ss=C₀/S³`
  (device-circuit-models:60).
- **The AXIOM-LEVEL kernel-argument definition (load-bearing for M0)** `common/axiom-register.md`
  Axiom-4 :186 (`A` = "local strain, normalized to A_yield"; kernel `S(A)=√(1−(A/A_yield)²)`) + :188
  (the FORCED L2 invariant is pinned to the **dynamical phase-plane vector** `(V/V_max, Φ/Φ_max)` — the
  lossless bond-LC tank conserves `E=½CV²+½Φ²/L` so the *dynamical* `(V_inc, Φ_link)` pair traces a
  machine-precision circle; the L2 invariant is FORCED for that dynamical pair).
- **The GAUGE-RELATIVITY of the A-state (load-bearing for M3/M0 + the observability rider)**
  `CLAUDE.md` INVARIANT-S2 :75 (VERBATIM: *"This state is **gauge-relative**: only spatial gradients of A
  across the substrate are physically observable, not absolute per-node values."*);
  `common/claim-quality.md`:1318 (*"All measurement is AC — a uniform DC bias is gauge-relative and
  self-cancels (= relativity)... Every AVE-distinct observable is an AC reading of a DC gradient or
  topology — differential BY PRINCIPLE"*); `form-deriving-value-importing.md`:187 (the DC offset
  "self-cancels, because rulers and clocks are wave-made and ride the same offset").
- **The relaxation timescale (load-bearing for the slow-ramp settle-out (i))**
  `tau-relax-derivation.md`:11,58 (`τ_relax=ℓ_node/c≈1.288e-21 s`; `dS/dt=(S_eq(r)−S)/τ_relax`; the
  hysteresis-loop area `∮S dr` = **dissipated** energy per cycle — a LOSSY channel, so a lossless
  "forget" via τ_relax is Ax3-forbidden).
- **The quiescent-point Q-point re-expression (H2's canon hook — Grant's Reading-A)**
  `node-up-small-large-signal.md`:§4b (:300-354); `resonant-lc-solitons.md`:137 (VCA = small-signal
  around the quiescent point). **Reading-A** (quiescent deformation relative to rest) — Grant leans DC-only
  (resonant-lc-solitons:157).
- Constants live from `ave.core.constants` (`OMEGA_C, L_NODE, Z_0, E_YIELD, V_YIELD, ALPHA, C_CELL, L_CELL`).
  No hardcoding.

## 0.2 THE ASYMMETRY PROBLEM (recorded from the fire order — confront head-on, do NOT analogy-dual)

The naive dual FAILS and the derivation must confront it. For the vacuum INDUCTOR the keying variable
(circulation `I_vac`) has a ZERO static limit because circulation is the lattice's DYNAMIC response to
`∂_tB` (Lenz). For the CAPACITOR, polarization/displacement responds to E DIRECTLY — its static limit is
NONZERO (that IS what ε means). Under the naive energy-store dual (µ-loading = kinetic/current store;
ε-loading = potential/charge store), the E-side comes out CHARGE-KEYED and canon node-up:217 stands.
**H2 therefore requires REAL ADDITIONAL STRUCTURE, not analogy.** Derive it or kill it. Grant's Reading-A
(operating point relative to the rest/quiescent point) is the canon hook for H2: IF the quiescent point
ADAPTS under held bias — LOSSLESSLY — then only excursions register and the keying is exactly `Var_t`. The
question is whether the canonical lattice equations FORCE that adaptation.

---

## 1. CANDIDATE MECHANISMS (enumerated; each derive-or-kill with a shipped artifact)

- **M0 NULL (H1 default).** Does the canonical chain already FORCE H1? Check the Ax4 kernel argument `A`
  at axiom level: is it defined on a static-capable variable (stored-energy ratio / amplitude of WHAT)?
  If `A` is axiom-defined on a static-capable variable, H2 needs an axiom-level REINTERPRETATION — flag
  as [NOT-DERIVABLE without axiom change]; do NOT quietly reinterpret an axiom.
- **M1 TOPOLOGY DC-BLOCK.** In the srs/K4 bond-LC network, does the saturating ε-element sit behind an
  effective SERIES capacitance in the E-signal path (a series-C charges once, then passes zero current →
  DC-blindness topology-forced)? Or is it a SHUNT element that sees the held V directly?
- **M2 MODE DECOMPOSITION.** Does the static response ride a LINEAR (non-saturating) mode while the AC
  response engages the saturating tank? If `½ε₀E²` for held fields is parked in a harmonic mode that
  never touches the elliptic kernel, static transparency follows. Must show WHERE the energy lives and
  that the ledger closes (energy-momentum crank-check).
- **M3 QUIESCENT SLIDE.** Does the node equilibrium move under held bias along a soft/zero-restoring
  direction such that the TANGENT stiffness a probe sees is unchanged? Must be ELASTIC/LOSSLESS — plastic/
  STZ relaxation is RETIRED (Ax3 violation). If the only mechanism found is dissipative, that KILLS H2.
- **(M2 and M3 may be the same mechanism in different coordinates — reconcile if so.)**

## 2. FROZEN BINS (verbatim; routed with no post-hoc criterion drops, Rule 11; ALL outcomes reportable)

- **[DERIVED: EXCURSION-KEYED]** — the canonical network FORCES the ε-grade to key on the excursion
  `Var_t(A_V)` about an adapted quiescent point (blind to a held DC bias); a real lossless adaptation
  mechanism is named + derived; the H2 energy ledger closes with `½ε₀E²` held OUTSIDE the kernel.
- **[DERIVED: CHARGE-KEYED]** — the canonical network FORCES the ε-grade to key on the mean-square
  `⟨A_V²⟩` (DC-included); no lossless DC-block mechanism exists (M1/M2/M3 all fail structurally); a held
  DC E genuinely loads the local ε. The E-side rescue via a Lenz-dual is dead.
- **[NOT-DERIVABLE]** — the network cannot force the member either way; [SELECTED-NOT-DERIVED] stands;
  enumerate exactly what missing physics would decide it.
- **[CONDITIONAL]** — the member is forced GIVEN a named open dependency (e.g. a gauge-observability
  reading, or an axiom-level reinterpretation); name the dependency precisely.

No outcome is "bad." A clean CHARGE-KEYED derivation is as valuable as EXCURSION-KEYED.

## 3. MANDATORY SUB-ANSWERS (each with a shipped artifact)

- **(i) SLOW-RAMP SETTLE-OUT** (Grant's falsifier). Under the derived keying, a field ramped up over
  seconds engages during the ramp (`J_D=ε₀dE/dt≠0`), then settles. Derive the POST-SETTLE behavior
  explicitly: does the ε-shift PERSIST (→H1) or DECAY (→H2)? If it decays, name the LOSSLESS mechanism
  and derive its timescale from network constants (`ℓ_node, ω_C, Z₀` — from `ave.core.constants`, no fit,
  no hardcoding). A cell that "forgets a stress it is still under" must have an explicit ELASTIC
  bookkeeping — where did the stress go? (Note: `τ_relax`-driven relaxation dissipates `∮S dr` per cycle,
  tau-relax:24 — a LOSSY forget is Ax3-forbidden; a lossless forget needs a soft mode.)
- **(ii) ENERGY LEDGER.** Under H2, `½ε₀E²` for a held field is real and parked — show exactly WHICH
  network element holds it and WHY that element is OUTSIDE the saturating kernel. Ledger must close.
- **(iii) EXACTNESS.** The derived keying comes out EXACTLY `Var_t(E)/E_c²` (excursion about the adapted
  quiescent) or EXACTLY something else — state what. An approximately-variance result is a DIFFERENT
  object; bin it as such.
- **(iv) FREQUENCY-INDEPENDENCE preserved.** Whatever is derived must NOT smuggle back rate-keying
  (`𝒲_beat ∝ (ω/ω_C)²` is dead by round 2). Check the derived member is amplitude-class (freq-indep).

## 4. THE PLUMBER QUESTION SURFACED TO GRANT (pre-test-physics-check; recorded, non-blocking)

Fired `pre-test-physics-check` (trigger 1 pre-reg freeze; trigger 8 dispatch-ontology; trigger 9
fork-to-computable; trigger 10 null-verdict liveness). The top-level ontology (H1 charge / H2 excursion)
is Grant-framed. The residual is converted to a COMPUTABLE DISCRIMINATOR, not pressed for fiat:

> **Plumber question (surfaced, recorded).** Gauge-relativity of the A-state (`CLAUDE.md`
> INVARIANT-S2:75, VERBATIM "only spatial gradients of A are physically observable") makes a spatially-
> **UNIFORM** held DC bias self-cancel on readout (= the PHASE-ONLY north-star). But the LOCAL cell
> kernel deficit under that uniform bias is REAL (the kernel is a local function of the instantaneous
> `A_V`, mean-square, DC-included) — it is just UNREADABLE without a gradient (a co-located wave-made
> ruler rides the same offset). Two honest readings collide: **(a)** the LOCAL ledger is CHARGE-KEYED
> (mean-square, H1 — the cell does not FORGET a held stress, it is parked in the charged shunt-C); **(b)**
> the OBSERVABLE is gradient/differential (a UNIFORM offset is gauge-hidden). A held field with a SPATIAL
> GRADIENT (a real bench field's fringe, an atomic Coulomb field) is NOT gauge-hidden — its `∇A` is
> observable. So gauge-relativity rescues UNIFORM held-DC transparency WITHOUT making the local ledger
> excursion-keyed; it does NOT give the round-2 time-variance member (which is blind to a NON-uniform
> held DC too). **Question for the bin:** does "the ε-grade keys on the time-EXCURSION (variance, blind
> to a held NON-uniform DC)" survive the network structure — or does the network force CHARGE-KEYING at
> the local ledger with only a UNIFORM-bias gauge rider? The derivation adjudicates; NOT resolved by fiat.

The freeze protects the derivation regardless of Grant's answer. If Grant collapses the fork in one
sentence it is recorded as an errata banner and the matching bin is routed.

## 5. FALSIFIERS / KNIFE (armed on ALL; NO parameter chosen to satisfy them)

- **½/¼ derived-only:** any new `½`/`¼` in a derived coefficient must be sympy-traced (the Letter's
  `−½`/`−¼` are its DERIVED kernel coefficients; `Var(cos)=½` is the cosine variance identity, declared).
- **ω_C/9-class thresholds:** the `9·ℓ_node` muonic defeat-scale (a §9-COMPARISON object) must NOT be
  reproduced coincidentally in the blind derivation.
- **2/7, 9.7734, √8:** mechanical-Q-point sector numbers — must NOT appear in the ε-coefficient
  (cross-wire flag if they do). Sector-guard test.
- **Gates must PROVE they can fire.** Feed each gate a COUNTERFACTUAL that FAILS it (no `Var(cos)=½`
  tautologies; the round-2 lesson). ReconcileGate can-fire proven on real paths, derived tolerances.
- **Null-verdict liveness (trigger 10).** Any suspiciously-exact zero (e.g. a "blind" verdict) is CHECKED
  with a positive control that goes nonzero through the identical pipeline.

## 6. THE M1/M2/M3/M0 VERDICT TABLE (frozen SHAPE; filled by the derivation)

| Mechanism | Question | Derived verdict (filled in §RESULT) | Artifact |
|---|---|---|---|
| **M0** | Is `A` axiom-defined on a static-capable variable ⟹ H1 forced? | — | §derivation |
| **M1** | Series-C DC-block on the ε path? | — | topology driver |
| **M2** | Static energy on a linear spectator mode outside the kernel? | — | mode/ledger driver |
| **M3** | Lossless quiescent slide preserving tangent stiffness? | — | tangent driver |

## 7. THE DUAL S_B (Route C, MERGED — the CANON-EXACT template, consumed not re-derived)

The B-side is `[WORKED-DERIVED]` (node-up:364, analytically exact): µ keys on `A_I=|∮H·dℓ|_norm/I_max`,
induced only by `∂_tB` (Lenz); static B → `I_vac=0` → `S_µ=1`. The E-side derivation must state WHY the
E-side does or does NOT admit the same DC-block (the asymmetry problem §0.2): is there a series element
on the ε path whose keying variable has a zero static limit? Report the duality's success or FAILURE.

## 8. DISCIPLINE STACK

Prereg FROZEN before results (this doc; the fire order + Grant's asymmetry-problem framing §0.2 verbatim);
skeleton-first then one section per commit; sympy on every analytical step; independent code paths for
numerics (derive-then-confirm, ReconcileGate with can-fire proven on REAL paths, derived tolerances); NO
self-verifying controls; import constants from `ave.core.constants` (no hardcoding); the ReconcileGate
helper at `src/ave/validation/reconcile_gate.py` where applicable; magnitudes as bands; quote-audit;
homonym guard (§0); regime/sector header (§0); phase-space coordinate discipline (state which coordinate
each leg measures); consistency-vs-emergence tag (a derived DC-block would be a CONSISTENCY identity of the
network topology; finding none is likewise consistency-class); pure-corpus; `make verify` green; tests
split (fast core + ≥1 standing falsifier that catches regression of whatever is derived); prereg-vs-code
fidelity — any FORCED deviation gets its erratum banner AT the moment it is forced; PR titled with the
routed bin, `[REVIEW: pending-orchestrator]`, DO-NOT-MERGE, NO SELF-MERGE.

## 9. POST-DERIVATION COMPARISON (firewalled — written ONLY after the blind §1–§8 derivation routes)

- If **[DERIVED: EXCURSION-KEYED]:** the round-2 muonic conditional-PASS becomes derived; STAGE (do NOT
  land) the node-up:217 supersession as a PROPOSAL BLOCK in the RESULT for Grant. Do NOT edit
  `manuscript/ave-kb/**` in this arc.
- If **[DERIVED: CHARGE-KEYED]:** the E-side rescue is dead; `#539 [C-EXCLUDED]` + the Letter's
  protective-cutoff reading stand as the complete story; say so plainly.
- If **[NOT-DERIVABLE]:** `[SELECTED-NOT-DERIVED]` stands; enumerate exactly what missing physics decides it.
- If **[CONDITIONAL]:** name the open dependency; state which of the above it collapses to once resolved.

The §9 muonic/CREMA/#539/Table-I/PVLAS evaluations are computed here ONLY, downstream of the routed bin.

---
**FROZEN.** Any change below this line after the first result commit is an ERRATA BANNER ONLY (the body is
a record). The freeze act is this commit; the derivation fires on it.
