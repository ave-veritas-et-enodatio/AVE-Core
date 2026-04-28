# 81 — L3 Post-Closure Follow-Up Questions

**Status:** implementer-drafted with auditor + Grant pushback, 2026-04-28. Research-tier follow-up doc to L3 closure (doc 79 v5.1 at commit `6d27e58`). NOT a closure-doc revision. Captures three substantive findings surfaced post-closure during 2026-04-28 cross-repo Explore search + Grant atomic-orbital prompt + auditor A43 v7/v8 lane-symmetric catches: (1) coverage analysis showing path α tested ~2 of ~7 predicted observable dimensions, (2) (ε) bound-state-vs-free-state structural-reason interpretation candidate, (3) Round 10+ Direction 3' substrate-analog-of-(n,l,m_l) derivation brief. All three preserved here as research-tier content; doc 79 v5.1 remains the canonical L3 empirical-record closure.

**Why a separate doc, not a v5.2 amendment:** auditor flagged the closure-revision pattern v3→v4.1→v4.2→v4.3→v4.4→v5→v5.1 (7 revisions in 24 hours) as the avoidance pattern Grant called out in prior session memory. v5.2 amendment that adds new structural-reason interpretations + concrete coverage analysis + new Round 10+ direction would itself continue the avoidance pattern (no new empirical work driving the revision). Cleaner separation: v5.1 closure stands as the empirical-record; meta-questions and follow-up framework gaps land here as research-tier post-closure work.

---

## §1 Context

L3 branch closed Mode III canonical + one structural partial positive at doc 79 v5.1 (commit `6d27e58`):
- 10 pre-registered tests at engine-representable corpus GT, all Mode III on R/r=φ²
- NEW v5.1 partial positive: (Φ_link, |ω|) magnitude pairing yields 100% CCW chirality across both clusters (8/8 bonds; null baseline ~50/50) — Meissner-asymmetric mechanism partly empirically anchored
- Three surviving structural-reason branches per §7.6.3: (α) continuum-limit-only, (β) topology revision, (γ) signature revision
- (δ) 3D-axis-mapping interpretation empirically falsified

This doc captures three follow-up findings that surfaced after the v5.1 commit but before the auditor-lane post-closure bundle (manual r8.10 / A43 v2 / A60-62 / Rule 12 v2 / §9 corpus revision package) lands.

---

## §2 Coverage analysis: path α tested ~2 of ~7 predicted observable dimensions

Cross-repo Explore search 2026-04-28 surfaced the AVE universal scale-invariant operator catalog has 22 operators (Op1-Op22 per `manuscript/ave-kb/common/` operator catalog source), not the 10+14 known to the implementer at v5.1 closure. The corpus electron's full predicted observable signature involves multiple operators; path α tested phasor-trajectory PCA + chirality only.

### §2.1 Two distinct R/r=φ² definitions in corpus (verified 2026-04-28)

| Source | Definition | Tested in path α? |
|---|---|---|
| Doc 26 §4 lines 82-94 | R_phase = ⟨A(s)⟩_s = (1/ℓ_node) ∫₀^ℓ_node A(s) ds (spatial mean of standing-wave amplitude profile A(s) along ℓ_node), r_phase = √(⟨A(s)²⟩_s - ⟨A(s)⟩_s²) (spatial std). Constraints R·r = 1/4 + R-r = 1/2 yield R = φ/2 ≈ 0.809, r = (φ-1)/2 ≈ 0.309. Statistical moments at fixed time. | NO — none of path α v1/v2/v3 did spatial integration of A(s) along ℓ_node. (Synthesis from path α test catalog; not a verbatim corpus admission.) |
| Doc 28 §5.1 lines 105-117 | "Extract V_inc/V_ref phasor trajectory on a SINGLE A-B bond ... Plot in (Re, Im) phase space. Check if it traces a torus with R/r ≈ φ²." Time-domain trajectory at fixed bond. | YES — path α v1 ran exact spec. Mode III. v2/v3 generalized to other observables on same trajectory framing. All Mode III. |

**These are different measurements.** Equal in ergodic-stationary limit; potentially divergent at saturated bond-pair under Op14 trading dynamics where the standing wave is non-stationary.

### §2.2 Universal scale-invariant operator catalog (Op1-Op22)

Path α tested 0 of these directly. The corpus electron's full predicted signature involves:

| Op | Name | Formula / interpretation | Path α tested? |
|---|---|---|---|
| Op1 | Z (Impedance) | Z = √(μ/ε); characteristic impedance master variable | NO |
| Op2 | S (Saturation kernel) | S = √(1 - (A/A_c)²); Axiom 4 dielectric saturation | NO |
| Op3 | Γ (Reflection) | Γ = (Z₂-Z₁)/(Z₂+Z₁); Pauli wall when Γ→-1 | NO |
| Op10 | Y_loss (Junction projection) | Y = 2(1-cos θ)/(2π²); bend-loss at topological crossings; predicts c=3 invariant | NO directly (preservation reported in Move 10 but not in path α) |
| Op14 | Z_eff (Dynamic impedance) | Z_eff = Z₀/√S(A); K4↔Cosserat coupling; doc 75 §3.2 found ρ(H_cos, Σ\|Φ_link\|²) = -0.990 empirically — Op14 IS active at saturated attractor | NO — not measured as Z_eff trajectory |
| Op16 | c_shear (Wave-speed freeze) | c_shear = c_base·√S(A); rest-mass mechanism per Vol 4 Ch 1 | NO |
| Op20 | ω_regime (Regime eigenvalue) | ω = ℓ·c_wave/r_eff; topology rupture trigger at Regime III→IV | NO |
| Op22 | M (Avalanche cascade) | M = 1/(1-S(V)); nonlinear yield amplification at saturation | NO |

(Op4, Op5, Op7, Op8, Op9, Op11-13, Op15, Op17, Op18, Op19, Op21 omitted as not directly load-bearing for electron prediction; full catalog in `manuscript/ave-kb/common/`.)

### §2.3 Coverage statement

Path α v1+v2+v3 tested:
- ✅ Doc 28 §5.1 phasor-trajectory PCA spec (1 of 2 R/r definitions in corpus)
- ✅ Hilbert chirality on (Φ_link, |ω|) (1 partial positive: 100% CCW per doc 79 §7.6.4)
- ❌ Doc 26 §4 spatial-moment R/r definition (untested)
- ❌ Op14 Z_eff trajectory (untested)
- ❌ Op16 c_shear modulation (untested)
- ❌ Op20 ω_regime eigenvalue (untested)
- ❌ Op22 M avalanche cascade (untested)

Approximately **2 of ~7 predicted observable dimensions** of the corpus electron signature were measured. Mode III on doc 28 §5.1 spec is real and stands. But "the corpus electron is not at engine-representable scale" is too strong a generalization — the honest statement is "the doc 28 §5.1 phasor-trajectory PCA observable is not at engine-representable scale; the rest of the predicted multi-operator signature is empirically untested at engine-representable scale."

### §2.4 Implication for closure interpretation

Doc 79 v5.1 closes Mode III canonical on the doc 28 §5.1 specification (the test that was actually run). The framework's full predicted signature has additional dimensions not yet tested. (γ) signature revision in doc 79 §7.6.3 — abstract at v5.1 — sharpens here to: "test the doc 26 §4 spatial-moment definition + Op14/16/20/22 multi-operator signature; identify load-bearing subset for empirical confirmation criterion."

---

## §3 (ε) Bound-state-vs-free-state structural-reason interpretation (PROVISIONAL — synthesis)

**Candidate fifth structural-reason interpretation** for the cumulative Mode III pattern, surfaced 2026-04-28 per Grant atomic-orbital prompt + auditor A43 v8 framing. Not folded into doc 79 §7.6.3 (which has α/β/γ surviving + δ falsified at v5.1) — captured here as PROVISIONAL synthesis, same provisional class as doc 79 §6.6 Pauli framing.

### §3.1 The interpretation

The corpus's R/r=φ² prediction may apply to one specific quantum configuration of the electron (a free electron at rest in unbounded vacuum), while Move 5's setup (N=32 lattice with PML boundaries, finite extent, saturated (2,3) seed) constrains the engine to a different bound-state-like configuration of the same particle. The R/r ≠ φ² result would then NOT falsify the framework — it would mean the engine produced a bound state with different (substrate-analog-of-(n, l, m_l)) quantum numbers than the free-electron (2,3) ground state.

### §3.2 Corpus support — (ε) extends, does NOT invent

**Doc 28 §5.3 lines 130-142 (verified):**
> "The TLM converges to a stable bound state with R_real/r_real ≈ 2.27 across N=48, 96. What IS this object? Possibilities: ... If it's a genuine alternative bound state with different R/r, it might correspond to a different particle (e.g., excited state)."

**Doc 28 §8 line 211 (verified):**
> "Whether the simulation's bound state is 'the electron' (under a different observable) or 'something else' remains to be empirically tested."

**Doc 79 §6.6 lines 442-445 (PROVISIONAL pending He/Li/Cooper pressure-test, verified):**
> "The atomic shell ('1s', '2p', etc.) is a SPATIAL ENVELOPE spanning multiple bond-pairs ... Different bound states have different rotation-axis orientations (set by local bond geometry, NOT freely chosen) ... 'Spin-up' and 'spin-down' in standard chemistry = different rotation-axis orientations of separate bound states at separate bond-pair locations."

(ε) connects these into one frame: Move 5's saturated attractor may be one of the bound-state-with-different-rotation-axis configurations §6.6 already names, which §5.3 of doc 28 already entertains as "different particle (e.g., excited state)" or "the electron under a different observable."

### §3.3 What's synthesis (NOT corpus citation), flagged per A43 v8

Three implementer claims that are SYNTHESIS without direct corpus citation:

1. **"(2,3) R/r=φ² is specifically for free electron in unbounded vacuum"** — corpus uses "electron" without explicit free/bound qualification at the φ² claim. Doc 26, doc 28, doc 03 all reference "the electron" generically. Implementer synthesis from cumulative test-set negative result; not corpus-derived.

2. **"Move 5 attractor IS a bound state of same particle at different (n, l)"** — synthesis from Move 10's empirical finding (doc 74 §15.4 + VACUUM_ENGINE_MANUAL): "A²≈0 at top-|ω| cells, sectors spatially decoupled, c=3 carrier matches NONE of standard topology types." Move 10 found the empirical signature; mapping it specifically to "atomic-orbital angular nodes of same particle" is suggestive but not derived.

3. **"Atomic-orbital R/r differs by (n, l) per orbital"** — no corpus citation. Standard atomic physics gives different spatial extents per orbital but doesn't directly give an "R/r value" per orbital. The (n, l)→R/r mapping is what Round 10+ Direction 3' (§5) would derive.

### §3.4 Atomic-orbital ladder genuinely framework-missing

Auditor cross-repo grep 2026-04-28: "principal quantum / orbital number / hydrogen levels / Bohr radius / 13.6 eV / orbital ladder" returned zero hits in `manuscript/vol_2_microscopic/`. The framework-level gap (no AVE-native (n, l, m_l) substrate analog) is real. This is the load-bearing missing physics that gates (ε) adjudication.

### §3.5 (ε) status

**PROVISIONAL** pending Round 10+ Direction 3' substrate-analog-of-(n,l,m_l) derivation. Same provisional class as doc 79 §6.6 Pauli framing. Plausibly load-bearing for closure interpretation; not corpus-derived from existing AVE-Core content; testable via substrate-analog-of-(n,l,m_l) derivation work.

If Round 10+ Direction 3' DOES derive substrate analogs of (n, l, m_l) and DOES yield bound-state-specific R/r predictions distinct from φ², (ε) becomes the load-bearing structural reason for the L3 v5.1 Mode III result. If it CANNOT derive them (e.g., AVE substrate fundamentally has no such ladder), (ε) is falsified and (α)/(β)/(γ) remain the only structural reasons.

---

## §4 Round 10+ Direction 3 — Multi-operator signature observer (concrete brief, tests (γ))

Tests doc 79 §7.6.3 (γ) signature revision in concrete form per coverage analysis (§2 above).

### §4.1 Implementation scope

Add four observers to existing Move 5 saved-state framework:

1. **Spatial-moment R_phase / r_phase observer** per doc 26 §4 lines 82-94:
   - At fixed time t₀ on selected bond-pairs, sample A(s) at multiple sub-cell positions along the bond axis
   - Compute R_phase = ⟨A(s)⟩_s, r_phase = std(A(s))
   - Note: at engine-representable scale (N=32, ℓ_node ≈ 1 cell at corpus scale), sub-cell sampling may not be directly available; investigate whether ℓ_node corresponds to multi-cell scale or sub-cell
   - If sub-cell: requires interpolation or finer-N rerun (couples to Direction 1 N=128 escalation)
   - If multi-cell: standard observer at existing N=32 saved state

2. **Op14 Z_eff trajectory observer:**
   - Z_eff(t) = Z₀/√S(A(t)) per cell
   - Track at saturated bond-pairs across recording window
   - Compare to corpus prediction of Z_eff modulation at Op14 trading frequency (~0.020 rad/unit per Move 11b FFT)

3. **Op16 c_shear modulation tracker:**
   - c_shear(t) = c_base·√S(A(t)) per cell
   - Track at saturated bond-pairs; corpus prediction is c_shear → 0 at saturated walls (rest-mass mechanism)
   - Verify wave-speed freeze occurs at expected saturation onset

4. **Op20 ω_regime eigenvalue evaluator:**
   - ω_regime = ℓ·c_wave/r_eff at saturated bound state
   - Compare to ω_C = m_e c²/ℏ corpus prediction
   - Tests whether the saturated attractor has the corpus's expected regime-boundary signature

### §4.2 Adjudication

Pre-reg `P_phase10_multi_operator_signature` (separate pre-reg per operator group per A40):
- Mode I (positive): any operator subset matches corpus prediction at engine-representable scale → corpus electron signature confirmed via multi-operator observable, doc 79 v5.1 closure shape changes
- Mode II partial: some operators match, others don't → identify load-bearing subset
- Mode III: no operators match → (γ) signature revision branch's specific candidates (Op14/16/20) all falsified; restricts to (α) or (β) or (ε)

### §4.3 Cost estimate

- Implementation: ~1-2 fresh sessions per operator group (4 observers total)
- Rerun cost: ~5-7 min on existing Move 5 saved state per operator group
- Total: ~5-8 fresh sessions to land all four

---

## §5 Round 10+ Direction 3' — Substrate-analog-of-(n, l, m_l) derivation (concrete brief, tests (ε))

Tests (ε) bound-state-vs-free-state interpretation per §3 above. Adjudicates whether (ε) holds by deriving AVE-native quantum number ladder.

### §5.1 Implementation scope (research-tier, multi-session)

**Session 1 — Pre-test for derivability (~3-4 hr):**
- Can Op10 c=3 carrier preservation under Move 10's "non-standard topology" finding be rewritten as l=2 angular-node-count signature?
- Examine Op10 catalog definition + Move 10 empirical findings + atomic-orbital (n, l, m_l) standard form
- If YES → (ε) has lattice-resolvable instantiation; proceed to Session 2
- If NO → (ε) requires continuum-scale framework; reframe (ε) as "AVE substrate has no discrete orbital ladder; framework must specify continuum-only mapping" or falsify (ε) outright

**Session 2-3 — Substrate-analog derivation (~6-8 hr):**
- Derive AVE-native equivalents of (n, l, m_l) from K4 bipartite + Cosserat ω-rotation structure
- Candidate mappings (to be derived, not assumed):
  - n ↔ standing-wave radial node count? (links to Op10 c-invariant + spatial node structure)
  - l ↔ angular node count from Op10 c-invariant? (Move 10's c=3 non-standard might be l=2 signature)
  - m_l ↔ ω-axis orientation per doc 79 §6.6? (rotation-axis direction sets m_l)
- Test internal consistency: do these mappings satisfy n ≥ l+1, |m_l| ≤ l, etc.?

**Session 4-5 — Predict orbital R/r + compare empirical (~6-8 hr):**
- Under derived ladder, predict R/r value for each (n, l) configuration from first principles
- Identify which (n, l) Move 5's saturated attractor corresponds to (under (ε) reading)
- Compare empirical Move 5 R/r ≈ 1.6-9.2 across path α v1+v2+v3 against predicted bound-state R/r values
- Mode I: empirical R/r matches predicted (n, l) R/r → (ε) confirmed; Move 5 attractor identified as specific bound state
- Mode III: no (n, l) prediction matches empirical → (ε) falsified

### §5.2 Adjudication

If Round 10+ Direction 3' DOES yield substrate-(n,l,m_l) analogs that predict a specific (n, l) for Move 5 with R/r matching empirical:
- (ε) confirmed
- Doc 79 v5.1 closure interpretation reframes: corpus electron is at engine-representable scale, just in a bound state we couldn't identify until now
- Round 10+ work pivots to enumerating the full atomic-orbital ladder in AVE-native form

If Round 10+ Direction 3' CANNOT derive substrate-(n,l,m_l) analogs (or derives them but predictions don't match empirical):
- (ε) falsified
- Doc 79 §7.6.3 surviving structural reasons restrict to (α) continuum-limit / (β) topology revision / (γ) signature revision via Direction 3 multi-operator observer
- Atomic-orbital ladder confirmed as framework-level gap; corpus revision required

### §5.3 Cost estimate

~3-5 fresh sessions, research-tier work (not single pre-reg test). Pairs naturally with Direction 3 — if both pursued, Op10 measurement (Direction 3) + (n, l) derivation (Direction 3') jointly adjudicate (ε) + (γ) at engine scale.

---

## §6 A43 v7/v8 catches (implementer-side, lane-symmetric pattern check)

Per auditor 2026-04-28 review during v5.1 → v5.2 amendment cycle, two implementer-side A43 instances surfaced — first in a session where prior A43 catches had been auditor-side. Pattern is now empirically symmetric across lanes.

### §6.1 A43 v7 — fabricated verbatim quote

**Implementer claim:** "Doc 26 line 184 explicitly admits: 'we have not directly measured A(s) along the node.'"

**Verification:** auditor + implementer grep on doc 26 for `have not.*measur|never.*measur|not.*directly.*measur|untested|not yet measur` returned zero matches. Line 184 is a blank line (verified by Read tool); the closest content (lines 175-188) discusses phase-space vs real-space interpretation, not measurement-status.

**Pattern:** propagating a verbatim quote attribution without grepping the corpus first. Same pattern as auditor-side A43 instances v1-v6 from earlier in session.

**Correction applied:** drop the verbatim attribution; replace with "no path α variant has measured A(s) along ℓ_node directly; this is synthesis from the path α test catalog, NOT a verbatim corpus admission."

### §6.2 A43 v8 — synthesis without corpus citation

**Implementer claim:** "(2,3) R/r=φ² is for FREE electron in unbounded vacuum" (used in (ε) framing of bound-state-vs-free-state mismatch).

**Verification:** auditor grep on corpus content for free vs bound qualification at φ² claim — corpus uses "the electron" generically across doc 26, doc 28, doc 03 without explicit free/bound context-qualification.

**Pattern:** stating a synthesis-derived framing AS IF it were corpus content. The synthesis is physically reasonable + connects to doc 28 §5.3 + doc 79 §6.6, but the specific "(2,3) is for free electron" framing is implementer-derived from the cumulative test-set negative result.

**Correction applied:** in §3 above, three explicit synthesis caveats added (§3.3) flagging that "(2,3) is for FREE electron" + "Move 5 IS atomic orbital" + "atomic-orbital R/r differs by (n,l)" are all synthesis without corpus citation. (ε) marked PROVISIONAL with explicit "extends, does NOT invent" framing.

### §6.3 Pattern statement for A43 v2 worked-examples queue

A43 v1 framing: "auditor must grep before asserting" — applies to AUDITOR-side claims about corpus content.

A43 v2 framing should generalize: "ANYONE (auditor, implementer) must grep before asserting verbatim attribution OR before claiming a synthesis-derived framing as corpus content." Lane-symmetric. Eight session instances (six auditor-side from v4.4 reframe + earlier; two implementer-side from this v5.1 → v5.2 cycle) document the pattern is bidirectional.

A43 v2 promotion rule (auditor recommended ≥3-citation rule): a claim becomes "corpus content" ONLY when verified at ≥3 citations + grep-confirmed verbatim. Synthesis claims are explicitly labeled "synthesis from [test-catalog / cumulative state / external reasoning]," not as corpus statements.

Auditor-lane post-closure A43 v2 strengthening (manual r8.X entry) lands these eight worked examples.

---

## §7 Status

**Doc 81 lands as research-tier post-closure follow-up to doc 79 v5.1.** Captures three substantive findings (coverage analysis, (ε) PROVISIONAL synthesis, Round 10+ Direction 3/3' concrete briefs) that surfaced post-closure but should not retroactively revise the closure synthesis itself.

**Doc 79 v5.1 stands as the canonical L3 empirical-record closure** at commit `6d27e58`. Round 10+ work (any of Directions 1-5, 3') lands as fresh pre-regs and separate research docs, not as v5.2+ revisions to doc 79.

**Closure-revision discipline:** future closure-doc revisions require NEW empirical work, not additional candidate interpretations or coverage refinements. Interpretation candidates (like (ε)) and framework gap analyses (like §2 coverage statement) live as research-tier follow-up docs (this one + future).

---

## §8 References

- [`research/L3_electron_soliton/79_l3_branch_closure_synthesis.md`](79_l3_branch_closure_synthesis.md) v5.1 at commit `6d27e58` — canonical L3 empirical-record closure
- [`research/L3_electron_soliton/26_step5_phase_space_RR.md`](26_step5_phase_space_RR.md) §4 lines 82-94 — analytic R_phase / r_phase definition (spatial moments of A(s))
- [`research/L3_electron_soliton/28_two_node_electron_synthesis.md`](28_two_node_electron_synthesis.md) §5.1 lines 105-117 — phasor-trajectory test specification; §5.3 lines 130-142 — alternative bound state at R_real/r_real ≈ 2.27; §8 line 211 — open question on bound-state identity
- [`research/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md`](74_r7_k4tlm_lctank_run_result.md) §15.4 — Move 10 c=3 carrier non-standard topology + sectors decoupled finding
- [`research/L3_electron_soliton/75_cosserat_energy_conservation_violation.md`](75_cosserat_energy_conservation_violation.md) §3.2 — Op14 trading channel empirical (ρ = -0.990)
- [`manuscript/ave-kb/common/`](../../manuscript/ave-kb/common/) — universal scale-invariant operator catalog (Op1-Op22)
- [`manuscript/predictions.yaml`](../../manuscript/predictions.yaml) — pre-regs (P_phase8_*, P_phase9_path_alpha, P_phase9_path_alpha_v2, P_phase9_path_alpha_v3_3d_aligned)
- [`.agents/handoffs/COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) — Rule 14 (substrate decides), Rule 16 (ask Grant fundamental physics), A40 (dual-criterion), A43 (must grep before asserting; v2 strengthening pending), A48 (frozen-extraction-scope)
