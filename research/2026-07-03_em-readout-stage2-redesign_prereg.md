# FROZEN PREREG — EM-readout Stage-2 REDESIGN (the un-riggable emergence instruments)

**Epic:** EM-readout derivation — Axiom-2's last underived leg. **Stage-2 (redesign).**
**Charter:** `_orchestration/2026-07-03_em-readout-derivation-charter.md` (canonized, PR #473 MERGED).
**This redesign chartered:** Grant, 2026-07-03 (verbatim: *"ii) yes"*), after the Stage-1b static-linear tautology finding.
**Branch:** `analysis/em-readout-stage2-redesign` (off `origin/main` @ `6b696c80`). NO self-merge — push + open PR.
**Prereg status:** FROZEN at this commit. The observable, the positive control, the structural-degeneracy check, the bins, and Grant's expectation do NOT move post-freeze. Only a Grant framing-ruling on §4 (the A-composition fork) may re-freeze §4 specifically.

**Disciplines applied (skill-selection plan, written before scaffolding):** `substrate-native-check` (§0 walk — done BEFORE any solver code) · `pre-test-physics-check` trigger 8 (the A-composition fork §4.3 → surfaced to Grant BEFORE design, Rule 16) · `phase-space-coordinate-check` (§5 — real-space enclosing-sphere radii, the (2,3) is phase-space and does NOT enter the metric) · `consistency-vs-emergence` (§3) · `verify-before-cite` (every file:line re-verified at HEAD `6b696c80` this session) · `flag-don't-fix` (the A-composition fork surfaced, not silently resolved) · `ave-driver-script-honesty`.

---

## 0. SUBSTRATE-NATIVE WALK (done before the first line of solver code)

Per operating-principle 1, the K4 / Cosserat / Op14 / phase-space-vs-real-space checkpoints, walked BEFORE scaffolding:

- **K4 / carrier:** the scalar EM-ε Poisson solve is ILL-POSED on the bipartite diamond-K4 TETRA_OFFSETS cage (nullspace ≥ 12, checkerboard) — the Stage-1 carrier finding (committed, `em_readout_vsector_transducer.py:62-90`, re-verified this session). The well-posed carrier for a **static scalar** channel is the chiral **srs (z=3)** net (`build_srs_net`, nullspace = constant mode only). Stage-2 builds on srs. **The srs graph Laplacian `L = D − A` is the substrate-native discrete Laplace–Beltrami on the edge-regular degree-3 net — NOT a Cartesian 7-point stencil.**
- **Cosserat:** the winding ω is the **microrotational** Cosserat field (Axiom-1, `axiom-definitions.md:16` verbatim: *"three microrotational (inductive coupling μ₀, identified with the magnetic field)"*). It enters the node's operating point through the **μ / inductive / magnetic-amplitude** channel of the shared LC node — NEVER as a right-hand-side charge. This is the un-riggability anchor: ω is a FIELD in the constitutive state, never a source.
- **Op14 / saturation:** the Ax4 kernel is `S(A) = √(1 − A²)` (INVARIANT-S2; `universal-saturation-kernel-catalog.md:11,20`; `dual-reactance-storage-taxonomy.md:31`). `A = V/V_yield` (translational) or `A = B/B_snap` (magnetic) — a **per-node, per-channel** ratio (`constants.py:520` comment: *"r = V/V_yield (or B/B_yield)"*). Effective reactances modulate: `ε_eff = ε₀·S`, `μ_eff = μ₀·S`, `c_eff = c₀/√S` (`vocabulary-register.md:423`). **Op14 local-clock modulation** (`op14-local-clock-modulation.md`): `ω_local(r) = ω_global·√(S(r))`.
- **Phase-space vs real-space:** the (2,3) winding lives in phase-space (θ = pφ + qψ). The **exterior-field observable is measured in REAL SPACE** (enclosing-sphere radii, minimum-image node distance). The winding's phase-space texture enters the constitutive state (a real-space A(r) field); the observable metric is the real-space enclosed-flux profile. These coordinates are matched: a real-space field sourced by a phase-space-textured medium, measured in real space. No φ²-vs-Cartesian mismatch (A46 clean).

---

## 1. WHY THE STATIC-LINEAR CELL IS CLOSED (the anchoring finding, recorded verbatim-faithful)

The Stage-1b result (`2026-07-03_em-readout-vsector-stage1b_result.md`, PR #479 in flight, §3 verbatim): *"for a KNOWN imposed source, ∇·E = +(source − mean) by construction of the solve — this confirms the discrete Gauss theorem of L."* A **LINEAR static solve `L φ = b` with a hand-assembled `b` is INFORMATIONALLY TRANSPARENT**: the enclosed-charge observable `Q_enc = Σ_Ω(∇·E) = Σ_Ω(b − mean)` returns the source you built. It is a MIRROR, not an instrument — the solve gives back its own RHS.

**Grant's ratification (2026-07-03):** the `{static, linear, cold, local, {∇×ω, ω}}` cell is CLOSED. The epic continues with TWO instruments where **the DC state is FOUND BY THE SYSTEM, never assembled by hand**, and where **there is NO right-hand-side source term, EVER** (§2).

The old cell's theorem-grade closure (a DEC-consistent div/curl adjoint pair on srs) is being derived by a **sibling DEC-operator arc** (charter collision-guard (b)); this redesign does NOT need it (there is no source term to make DEC-consistent) but cites it as the pending formal closure of the old cell.

---

## 2. THE UN-RIGGABILITY CORE (both instruments — non-negotiable)

**There is NO right-hand-side source term, EVER.** The winding ω enters ONLY through the constitutive state:

- Per **Axiom 1** each node is an LC tank whose translational (ε₀/E) and rotational (μ₀/B) reactances SHARE the node (`axiom-definitions.md:16`).
- Per **Axiom 4** the local operating point `A` modulates those reactances via `S(A) = √(1 − A²)`, with `A` the local amplitude ratio from canon (`constants.py`).
- The winding's ω texture contributes to the local amplitude `A` through the μ/magnetic channel of the shared node (§4).

**The question both instruments ask:** does the winding's texture, acting PURELY through the medium's constitutive state (the spatially-varying `S(A(r))` that modulates the node/bond reactances), FORCE a nonzero static exterior E — and does its flux count Link?

**The zero floor (the un-riggability guarantee):** with `b ≡ 0` (no RHS source anywhere) and a COLD LINEAR medium (`S ≡ 1` uniform), the ONLY solution of the homogeneous problem is `φ ≡ 0`. Anything nonzero is generated by **nonlinearity (spatially-varying S) + texture (the winding's A(r))**, not by us. There is no `b = 𝒬·δ³`, no `∮E·dA = 𝒬/ε₀` enforced, no `𝒬 → e` dictionary. Gauss (`∇·E`, `∮E·dA`) is a DIAGNOSTIC only.

**The mechanism (how a source-free nonlinear medium polarizes):** a spatially-varying `ε_eff(r) = ε₀·S(A(r))` makes the Laplace operator **inhomogeneous**: `∇·(ε_eff(r) ∇φ) = 0`. A homogeneous-medium harmonic (`φ ≡ const`) is NO LONGER a solution when the boundary/geometry breaks the symmetry, because the variable-coefficient operator has a different null structure. The winding's texture enters as the spatial profile of `ε_eff` (via `A(r)`), NOT as a charge. Whether a nonzero exterior E emerges is exactly what the substrate decides. **This is a variable-coefficient homogeneous PDE, not a sourced Poisson equation** — the categorical difference from the closed cell.

---

## 3. CONSISTENCY-VS-EMERGENCE CLASS (declared up front)

- The **instrument build** (the nonlinear .OP solver + the dynamical settler) is MEDIUM-scaffold — infrastructure, not a claim.
- **Validate-on-known** (§6 v1/v2/v4) is CONSISTENCY-class (reproduce the linear solver's known behaviour in the S→1 limit; the cold-floor).
- **The liveness positive control** (§6 v3) is a CONSISTENCY-class instrument-validity check (a KNOWN constitutive texture that must polarize → the instrument reads it). It does NOT test the winding; it proves the instrument is ABLE to produce nonzero output.
- **The winding readout** (the decisive runs, HELD until the hold-point review) is the **EMERGENCE** test: does the winding's constitutive texture FORCE a nonzero exterior E that counts Link. Per Grant's mission framing: emergence is the goal; a non-emergence is the honest stakes-table result.
- **Dictionary-translated comparison:** standard EM would source 1/r from a counted integer via Gauss+multipole. A nonzero emergent exterior flux HERE — sourced purely by a nonlinear medium's constitutive texture with NO charge term — is NOT a standard-EM mechanism; if it counts Link it is an AVE-distinct emergence. Pre-registered so it is not mis-headlined as mere Coulomb-recovery.

---

## 4. THE KEY PHYSICS INPUT — THE A-COMPOSITION RULE (⚠ FRAMING FORK SURFACED, §4.3)

**This is the load-bearing physics input and the one place canon may be silent.** The whole instrument turns on: **how does the winding's ω texture set the local operating point A(r) that modulates S?**

### 4.1 What canon fixes (verified at HEAD `6b696c80`)

- **The kernel:** `S(A) = √(1 − A²)`, A dimensionless ∈ [0,1) (`universal-saturation-kernel-catalog.md:20`).
- **The per-channel ratios:** translational `A_ε = V/V_yield`; magnetic `A_μ = B/B_snap`. `V_yield = √α·V_snap` (`constants.py:464`); `B_snap = √(2μ₀ m_e c²/ℓ³)` (`constants.py:481`). Both are PER-NODE, PER-CHANNEL (`dual-reactance-storage-taxonomy.md:31`; `constants.py:520`).
- **The winding is microrotational (μ-channel):** `axiom-definitions.md:16` — ω is the inductive/μ₀/magnetic DOF. So the winding's amplitude enters `A_μ` (the magnetic-amplitude ratio), via the field strength `|∇×ω|` or `|ω|` (a magnetic-analog field the μ reactance responds to).
- **The regime anchor:** the electron's A1 core operates at `A = √α ≈ 0.085` (sub-saturated, `S ≈ 0.996`); the T2 wall sits AT `A = 1` (`V_yield`) (`vocabulary-register.md:670`). **The interesting regime is near-yield.**

### 4.2 What canon is SILENT on (grep-confirmed absent this session)

**There is NO A-composition rule in the corpus** — no `A² = f(A_ε, A_μ)` combining the translational and rotational amplitudes into the single shared node's operating point. Grep across `manuscript/ave-kb/` for `A² = …V…B…`, `quadrature amplitude`, `combined operating point`, `A_local =`, `total saturation` returns NO composition formula. Canon gives A **per channel**; the shared-node LC structure (Axiom 1) says both reactances share the node, but the RULE by which the two channel-amplitudes compose into the one A that both channels' S see is **UNDERIVED**.

### 4.3 THE FORK (flag-don't-fix — surfaced, not silently resolved; Grant's door open)

> **How do the translational (ε) and rotational (μ) amplitudes compose into the shared node's single operating point A?** The winding enters `A_μ` (magnetic). But `S` modulates BOTH ε_eff and μ_eff at the shared node. Three physically-motivated candidate rules, none canon-forced:
>
> - **(Q) Energy-additive quadrature** — `A² = A_ε² + A_μ²` (the total stored reactive energy sets the operating point; the LC tank's total energy is the sum of capacitive + inductive; the physically-natural default since S is a Born–Infeld energy-density limit). **My recommended default.**
> - **(M) μ-channel-only** — `A = A_μ` (each channel saturates on its own amplitude; the ε reactance sees only the ε amplitude, the μ reactance only the μ; the winding modulates only μ_eff, leaving ε_eff cold unless the winding also drives a translational amplitude). The most conservative — it means the winding modulates only the magnetic reactance directly, and any ε polarization must propagate through the LC shared-node coupling.
> - **(X) Max / dominant-channel** — `A = max(A_ε, A_μ)` (the node saturates when EITHER channel hits yield; the sharp-corner rule).

**This is a trigger-8 STOP-and-surface, but it does NOT block the build** (charter §Stage-2a authorizes: *"where canon is silent, tag ENGINEERING-CHOICE and sweep the choice as a robustness knob rather than picking silently"*). Therefore: **the build proceeds with (Q) as the tagged ENGINEERING-CHOICE default, and (M)/(X) are swept as a robustness knob.** The verdict is reported per-rule. **If the emergence outcome DIFFERS across the three rules, that difference is itself surfaced to Grant as a framing decision the axioms cannot settle** (a [STUCK-FRAMING] sub-outcome on the composition rule). If the outcome is ROBUST across all three, the fork is moot for the verdict. The hold-point report headlines this fork regardless.

### 4.4 The winding→A_μ magnitude map (the field the μ channel responds to)

The μ reactance responds to a magnetic-analog field strength. The winding carries `ω` (microrotation) and its substrate flux `F = ∇×ω`. Candidate magnetic-amplitude fields, tagged ENGINEERING-CHOICE, swept:
- **(f1)** `A_μ(r) = amplitude · |ω(r)| / ω_ref` — the microrotation magnitude directly (ω IS the magnetic DOF per Axiom-1).
- **(f2)** `A_μ(r) = amplitude · |∇×ω(r)| / F_ref` — the substrate flux magnitude (the B-analog; `F = ∇×ω` is the Link-carrying flux).

Default **(f1)** (ω is the μ₀ DOF directly per `axiom-definitions.md:16`); **(f2)** swept. `ω_ref`/`F_ref` set so that the peak `A_μ = amplitude` (the seed-amplitude knob is the regime control, §7). **NO Link integer, NO helicity, NO 𝒬 enters this map — only the ω FIELD** (audited §8).

---

## 5. THE FROZEN OBSERVABLE (per instrument — identical, phase-space-clean)

**The adjoint-consistent enclosed-flux profile on enclosing-sphere radii, jellium-corrected** (the #479 review's torus-hole hazard pre-registered away):

```
Q_enc(r) = Σ_{u : |pos_u − r_core| < r} (∇·E)[u]  −  Q_jellium(r)
```
where `∇·E = +Lφ` (the discrete divergence of the SOLVER's own L, operator-consistent — the #479 adjoint-consistent form, copied with provenance) and the **jellium correction** removes the growing neutralizing-background:
```
Q_jellium(r) = Q_total · [1 − (4π/3)(r/box)³]   evaluated on the enclosing-sphere volume fraction
```
The **jellium form** `1 − (4π/3)(r/box)³` is the pre-registered correction (charter-specified). **Radii `r ≥ 8`** (real-space, minimum-image node distance) — the near-core `r < 8` is excluded (the torus-hole hazard: the (2,3) torus has an empty central hole; sampling inside it reads the hole, not the field — density-peak discipline, Rule 10 corollary). The profile is read on the enclosing SHELL, not at a centroid.

**Phase-space-coordinate-check (A46):** `r` is REAL-SPACE minimum-image node distance. The (2,3) winding's phase-space coordinates (φ, ψ) do NOT enter the metric. The medium's constitutive texture is a real-space field; the observable is a real-space flux. Coordinates matched. ✓

**Density-peak vs centroid (Rule 10):** the core `r_core` is the winding's real-space geometric center (torus center); the profile samples enclosing shells at `r ≥ 8` OUTSIDE the torus tube — the exterior field, where an emergent monopole would live. NOT the empty torus hole.

---

## 6. VALIDATE-ON-KNOWN (Stage-2a — ALL before any winding run)

- **(v1) COLD / ZERO-TEXTURE FLOOR:** `S ≡ 1` uniform (cold linear medium), `b ≡ 0` → `φ ≡ 0` EXACT. The un-riggability floor: a source-free linear medium invents nothing. **Gate: `max|φ| < 1e-12`.**
- **(v2) LINEAR LIMIT (S→1):** with a KNOWN small imposed constitutive modulation and `A → 0` (so `S → 1`), the nonlinear .OP must reproduce the linear solver's response on that known modulation to tolerance. **Gate: `‖φ_nonlin − φ_lin‖/‖φ_lin‖ < 1e-6` at `A_max = 1e-3`.** (Certifies the nonlinear solver reduces to the certified linear core in the cold limit.)
- **(v3) LIVENESS POSITIVE CONTROL (mandatory — the #479 lesson):** construct a constitutive texture that PROVABLY must polarize the network — a **maximally asymmetric S-depression dipole layer** (one hemisphere of nodes driven to `A → 1` / `S → 0`, the opposite hemisphere cold `S = 1`), with NO source term. The instrument MUST read a nonzero enclosed-flux profile (the variable-coefficient operator polarizes across the S-gradient). **Gate: `max|Q_enc(r)| > 100 × floor` AND the profile is structured (not noise).** The instrument must be shown ABLE to produce nonzero output BEFORE any winding null counts. If v3 fails, the instrument is blind and NO winding null is meaningful — [NO-CONVERGENCE]/instrument-blocker, not physics.
- **(v4) CONVERGENCE-VS-RESOLUTION STABILITY:** on the v3 control, sweep `srs_L ∈ {8, 10, 12}` and the Picard/Newton damping; the Q_enc plateau must be stable (not drift with resolution/solver params). **Gate: plateau varies < 20% across resolutions.** Plus: **the fixed-point convergence diagnostics** (residual history, iteration count, `cg_info`) EXPORTED and ASSERTED converged (the #479 lesson: no unchecked solver info).

**The gate:** v1–v4 ALL pass before any winding run. The decisive winding runs are HELD at the §8 hold-point regardless.

---

## 7. REGIME HONESTY (Grant's regime discipline — declared per run)

The interesting regime is **near-yield**: the electron's T2 wall sits AT `V_yield` (`A = 1`); its A1 core at `A = √α ≈ 0.085`. **A cold-regime null alone does NOT close the question.** The seed amplitude (the winding's peak `A_μ`) is swept:
- **deep-cold:** `A_max ∈ {0.01, 0.05}` (near the A1-core √α regime; `S ≈ 0.996`).
- **intermediate:** `A_max ∈ {0.2, 0.5}`.
- **near-yield:** `A_max ∈ {0.8, 0.95, 0.99}` (approaching the T2 wall; `S → 0`; the nonlinearity is strongest).

**Every run declares its MODE (static .OP / dynamical settle) + REGIME (cold/intermediate/near-yield) + PHASE-STATE (S value at peak).** A null in the cold regime is booked as cold-regime-only; the near-yield sweep is where the nonlinearity can force emergence. **The decisive winding runs (this sweep, with the winding texture) are the HELD runs — fired only after the §8 hold-point review.**

---

## 8. THE HARDENED EQUATION-AUDIT + THE HOLD-POINT (the Stage-1 sequence violation does NOT repeat)

**Sequence: build → validate (v1–v4) → audit → STOP → orchestrator+panel review → THEN the decisive winding runs.** The Stage-1 violation (emergence run fired before the audit) does not repeat.

The hardened audit (the #479 reconcile-grade pattern):
- **Live import-closure module list:** scan EVERY ave-module in the solve+constitutive-assembly import path (not self-scoped) for forbidden patterns.
- **Anchored allowlists:** every constitutive-assembly input is a labeled `A_field` (the ω-derived amplitude) or a KNOWN control texture — NO `Q_link`, `helicity`, `w_tor`, `𝒬`, or `rho` may reach the constitutive assembly.
- **Consumed alpha-guard:** the `_FORBIDDEN_ALPHA` carrier list is CONSUMED (asserted absent from the constitutive path), not dead code.
- **Runtime independence check:** the constitutive assembly is shown at RUNTIME to depend only on the ω FIELD, never on any integer topological invariant. `A(r)` is computed from `ω(r)` pointwise; the Link integer is computed SEPARATELY for the audit-comparison only, never fed back.
- **NO RHS source anywhere:** grep + runtime assert that `solve` / `settle` is called with `b ≡ 0` for every winding run (the un-riggability core: there is no source term). The winding enters ONLY the constitutive `A(r)` field.

**⚠ HOLD-POINT:** Stage-2a ENDS at build + v1–v4 validation + liveness-control reading + regime-sweep plan + hardened-audit output + this frozen prereg, and STOPS. **The decisive winding runs fire ONLY after the orchestrator + panel review the audit.** The final report carries: validation numbers, the liveness-control reading, the regime-sweep plan, the audit output, the A-composition fork (§4.3), PR number, blockers.

---

## 9. FROZEN BINS (both instruments — identical; robustness ladder: existence primary, counting the prize)

- **[FLUX-EMERGES-COUNTING]** — nonzero exterior flux; the `Q_enc` plateau (at `r ≥ 8`) TRACKS `Q_link` across seeds `Q = 1, 2, 3`; the sign FLIPS with the enantiomorph (right ↔ left srs). The robustness ladder: **existence primary** (nonzero flux at all), **counting the prize** (plateau ∝ Q_link, sign-tracks-enantiomorph). This is the emergence chord.
- **[FLUX-EMERGES-NON-COUNTING]** — nonzero exterior flux but it does NOT track Link (no `Q = 1,2,3` scaling, or no enantiomorph sign-flip). **Booked honestly — no rescue.** The winding polarizes the medium but the flux is not the charge.
- **[NO-FLUX]** — `E ≡ 0` at the fixed point (`Q_enc` at/below the v1 floor across all regimes including near-yield). The honest stakes-table negative: the winding's constitutive texture does NOT force a static exterior E. Charter §2 SCREENED/ABSENT branch.
- **[NO-CONVERGENCE]** — the fixed point fails to exist / the Picard/Newton iteration does not converge (or v3 liveness fails ⇒ blind instrument). A NAMED INSTRUMENT BLOCKER, not physics. Booked as such; not a null.
- **[STUCK-FRAMING]** — a further framing fork the axioms cannot settle (the A-composition rule §4.3 producing rule-DEPENDENT verdicts is the likely one) ⇒ STOP, surface to Grant.

**Both Grant's expectation and the measured verdict are recorded regardless of agreement** (standing instruction).

**Grant's pre-registered expectation (recorded):** per the Stage-1 fork-ruling, the electron is an electric monopole via the winding's linking flux read through the massless EM/V-sector; the emergence goal is that `∮E·dA` counts Link. Grant's regime intuition: the interesting physics is near-yield (the T2 wall). Whether it emerges is the falsifiable target; a near-yield null is the honest negative.

---

## 10. ANCHORING-CLEANLINESS (Step 3.8 liveness discipline — MANDATORY, stated explicitly)

**NO nonlinear-instrument data exists anywhere.** This prereg is anchoring-CLEAN: no `S(A)`-modulated nonlinear .OP or dynamical-settler has ever been run on this problem. The Stage-1 / Stage-1b runs were a DIFFERENT instrument — a LINEAR static solve with a hand-assembled `b` (the tautology). Their unblinded profiles (the `Q_enc` numbers in `..._results.json`) are recorded as EXISTING but do NOT contaminate this prereg: they belong to the closed linear cell (§1); the nonlinear instrument's `Q_enc` is computed by a categorically different operator (variable-coefficient homogeneous PDE vs sourced Poisson). **No bin threshold in §9 was tuned to any nonlinear result — there is none to tune to.** The liveness positive control (§6 v3) is the instrument-validity anchor, established on a KNOWN control texture, before any winding run.

---

## 11. STAGE-2b — THE DYNAMICAL SETTLING TEST (chartered here; built only after 2a's hold-point clears)

The dynamical instrument, complementary to the static .OP:
- Complete the **translational-sector EVOLUTION** (the unified engine's dormant `u`-slot) with the axiom-native LC coupling as DYNAMICS (the ε↔μ shared-node LC exchange, Axiom-1).
- **Seed the winding** (ω its own DOF); evolve with the **Ax4 nonlinearity live** (`S(A(r,t))` modulating the reactances each step).
- **Time-average / settle** to the DC fixed point THE DYNAMICS CHOOSES (not assembled by hand); read the SAME frozen observable (§5) at settlement.
- **Same bins** (§9).
- **ENERGY-CONSERVATION GATE (lossless Ax3):** the settled evolution must conserve total reactive energy to tolerance (`|ΔH/H| < 1e-3`) — a VALIDITY PRECONDITION. A settler that leaks energy is not the lossless substrate; its fixed point is an artifact.
- **Reactance-pair tracking (Rule 10):** record BOTH the C-state (V_inc / the ε amplitude) AND the L-state (Φ_link / the μ amplitude) at every step over the recording window — a snapshot at one phase cannot distinguish a static fixed point from an oscillator caught at peak.

Stage-2b is chartered but NOT built in this dispatch — it is built only after 2a's hold-point review clears.

---

## 12. DELIVERABLES

- **This frozen prereg** (deliverable #1).
- The Stage-2a solver (new module — NOT `em_readout_vsector_transducer.py`, owned by PR #479) + validation suite (v1–v4) + hardened audit.
- **STOP at the hold-point** with: validation numbers, the liveness-control reading, the regime-sweep plan, the audit output, the A-composition fork, PR number, blockers.
- **Do NOT run the decisive winding configurations before the hold-point review.**
- If a framing fork the axioms can't settle appears (the A-composition rule §4.3 is the likely one, if verdicts are rule-dependent), STOP and surface it.

Corpus updates (any manual/register entries) remain SURFACED for the auditor to land (implementer surfaces, auditor lands).
