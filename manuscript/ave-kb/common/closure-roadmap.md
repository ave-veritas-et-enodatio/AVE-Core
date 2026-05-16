[↑ AVE Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: living planning artifact post-structural-closure 2026-05-15; referenced from .agents/HANDOFF.md, trampoline-framework.md §11, L5 trackers, and all chapter propagation work -->

# AVE Framework Closure Roadmap

**Created:** 2026-05-15 (post structural-closure declaration). **Status:** living planning artifact. Update after every significant session.

**Purpose.** The AVE framework reached **structural closure** on 2026-05-15 (per `trampoline-framework.md` §11.0). This doc plans the path from structural closure to **theoretical closure** (all numerical derivations completed) and **empirical closure** (bench + cosmological observations consistent with framework predictions).

**Discipline rule.** Every remaining action in the framework's path to publication is logged in this doc. If it's not here, it's not happening. Status transitions are real-time, not retroactive.

**Supersedes:** `research/L3_electron_soliton/114_next_steps_consolidation_plan.md` for forward-looking planning. Doc 114 remains historical record of the post-2026-05-14 session.

---

## §0 Status dashboard (update after every session)

| Tier | Action | Status | L5 ID | Last touch (SHA / date) |
|---|---|---|---|---|
| 0 | Structural closure declared | ✓ DONE | — | `fb2ac44` 2026-05-15 |
| 1 | E-094 AVE-Core substrate-vocab propagation (Vol 1-4) | **APPLIED** 2026-05-15 (all 7 targets: Vol 1 Ch 1/4, Vol 2 Ch 1, Vol 3 Ch 2, Vol 4 Ch 1, glossary, constants.py) | E-094 | `2eb2b1c` |
| 1 | E-101 Three substrate invariants observables module | **APPLIED** 2026-05-15 (13/13 tests PASS; rigorous M + first-pass Q,J) | E-101 | `d488a25` |
| 1 | E-102 Vol 3 Ch 4 cosmic-𝒥 identification | **APPLIED** 2026-05-15 | E-102 | `d96e8d7` |
| 1 | E-103 Vol 3 Ch 21 same-epistemic-horizon framing | **APPLIED** 2026-05-15 | E-103 | `42e3819` |
| 1 | AVE-QED App F cosmic-𝒥 row explicit | **APPLIED** 2026-05-15 | (cross-repo) | `c59a1cb` (AVE-QED) |
| 1 | README + LIVING_REFERENCE structural-closure declaration | **APPLIED** 2026-05-15 | new | `d96e8d7` |
| 1 | v14 Mode I regression test (`src/tests/test_master_equation_v14_mode_i.py`) | **APPLIED** 2026-05-15 (5/5 PASS) | new | `d96e8d7` |
| 1 | Figure 2 storage-modes layout fix | **APPLIED** 2026-05-15 (3D + 2D dual-panel layout) | n/a | `d96e8d7` |
| 2 | **Q-G47 Session 6+ keystone u_0* derivation** | **Sessions 6-8 LANDED 2026-05-15** (full day Tier 2 push): Session 6 magic-angle equation explicit; corpus-grep audit reduced scope ~60-70%; Session 7 T-irrep theory complete + target #10 closed (7-mode bubble = T⊕T⊕A); **Session 8 HONEST FALSIFICATION** of A-033 secondary α irrep-dim claim (α coefficients come from Golden Torus geometry NOT K4 irrep dims; A-033 main electron-in-E⊗T claim still stands; A-001 α-as-calibration stands). Cosserat μ_c framework set up with dimensional issues flagged. Sessions 9-10 remaining: dimensional resolution of Cosserat μ_c + γ_per-path + rigorous K4 bound-state mode occupancy. | Q-G47 / A-027 / A-029 / A-030 / A-032 / A-033 | `33d1e2f` (S6), `6a3ff73` (S7), `9b63887` (S8) (AVE-Core); `6626f43` (S6), `32379a9` (S7), `d5f6390` (S8) (AVE-QED) |
| 3 | T_EM(u_0*) explicit closed-form | pending (Tier 2 dep) | Q-G47 closure | — |
| 3 | ~~Vol 3 Ch 4~~ **Vol 3 Ch 1 explicit ξ(R_H, ℓ_node) derivation** | **✓ ALREADY CLOSED in corpus** at Vol 3 Ch 1 §"Fundamental Unity of Gravity and Expansion" (lines 95-155) — corpus-grep audit 2026-05-15 evening. Canonical: $\xi = 4\pi(R_H/\ell_{\text{node}})\alpha^{-2}$; derives $G = \hbar c/(7\xi m_e^2)$, $\alpha_G = 1/(7\xi)$, $R_H/\ell_{\text{node}} = \alpha^2/(28\pi\alpha_G) \approx 3.455 \times 10^{38}$, $R_H \approx 1.334 \times 10^{26}$ m = 14.1 Gly, $H_\infty \approx 69.32$ km/s/Mpc (between Hubble tension bounds). Was originally located at "Vol 3 Ch 4" in this dashboard — that was wrong; actual location is Vol 3 Ch 1. | A-030 / A-031 | (corpus pre-existing, verified `060f429`) |
| 3 | Three-route α/G/𝒥 consistency verification | pending (Tier 3 deps): needs $T_{EM}(u_0^*)$ from Q-G47 Session 8+ closure (currently pending dimensional resolution per Session 8 §4.3) | A-030 + A-031 | — |
| 4 | First-law T·dS = dE axiom-first closure | pending (independent) | A-002 | — |
| 4 | Cosserat coupling on Master Equation FDTD | pending (independent) | doc 113 §5.4 | — |
| 4 | Strict stationary soliton via imaginary-time | pending (independent) | doc 113 §5.1 | — |
| 4 | Multi-soliton dynamics for Coulomb-law validation | pending (independent) | doc 114 §4.3 | — |
| 4 | Q-G45 multi-soliton interference as gravity (derivation) | pending (depends on Tier 4 multi-soliton engine) | Q-G45 | — |
| 4 | Higher-energy soliton ((2,5) cinquefoil) | pending (independent) | doc 114 §4.4 | — |
| 5 | Cosmic 𝒥_cosmic literature review (CMB + LSS) | pending (independent) | A-031 | — |
| 5 | AVE prediction for 𝒥_cosmic from numerics | pending (Tier 3 dep) | A-031 + A-030 | — |
| 5 | IVIM bench Phase 2A build | pending (procurement parallel) | Q-G42 + Q-G46 | — |
| 5 | IVIM measurement campaign | pending (bench dep) | Q-G42 + Q-G46 | — |
| 6 | Q-G43 atom-scale local Γ=-1 derivation | pending (cleaner after Tier 3) | Q-G43 | — |
| 6 | Q-G44 helio-scale local Γ=-1 derivation | pending (cleaner after Tier 3) | Q-G44 | — |
| 6 | App F atom + helio rows derived | pending (Q-G43 + Q-G44 deps) | (new) | — |
| 7 | All queued E-NNN entries applied (currently 30+) | pending | varies | — |
| 7 | Picture-audit infrastructure | pending (independent) | (new) | — |
| 7 | L3 + L5 deletion with cross-reference migration | pending (Tier 7 dep) | (new) | — |
| 7 | Backmatter "Framework Status" section | pending (Tier 5 verification dep) | (new) | — |
| 7 | Publication-ready manuscript pass | pending (everything above) | (new) | — |

**Closure state summary:**
- Structural closure: ✓ DONE 2026-05-15 (`trampoline-framework.md` §11.0)
- Theoretical closure: 🟡 IN PROGRESS (Tier 2-4 critical-path)
- Empirical closure: 🟡 IN PROGRESS (Tier 5 critical-path)

---

## §1 Closure-state taxonomy

| Closure level | What it means | Criteria | When |
|---|---|---|---|
| **Structural closure** | Conceptual shape locked in; framework structure visible end-to-end | 5 criteria per `trampoline-framework.md` §11.0: (1) ground-up construction maps to math; (2) every macroscopic observable has derivation path; (3) epistemic horizon named; (4) free parameters minimized; (5) falsification test specified | ✓ 2026-05-15 |
| **Theoretical closure** | All numerical derivations end-to-end closed | (a) Q-G47 Session 6+ rigorous u_0*; (b) Vol 3 Ch 4 explicit ξ; (c) three-route α/G/𝒥 consistency verified or framework revised; (d) all queued analytical derivations completed | 🟡 IN PROGRESS |
| **Empirical closure** | Bench + cosmological measurements consistent with framework predictions | (a) IVIM bench measures predicted IM3 cubic V³ slope; (b) cosmic 𝒥 from observations matches AVE prediction; (c) three-route empirical consistency holds; (d) Q-G43/44 boundaries observable | 🟡 IN PROGRESS |

**These run in parallel.** Theoretical and empirical closure share Tier 5 timing. Final publication-ready state requires both.

---

## §2 Tier 0 — Structural closure (DONE 2026-05-15)

✓ Six-step ground-up build with explicit math at each step (trampoline-framework.md §1.1-§1.7)
✓ Shared-spring inter-cell coupling (A-029)
✓ Phase-transition-while-spinning mechanism for u_0
✓ Machian G + α + G + cosmic-𝒥 joint cosmological anchoring (A-030, A-031)
✓ Substrate-observability rule applied fractally (A-026 sharpened)
✓ "God's Hand" epistemic horizon explicitly named
✓ Three-route falsifiability test specified
✓ Canonical doc: `trampoline-framework.md` §0-§14 with 7 figures
✓ L5 canonicalized: A-026, A-027, A-028, A-029, A-030, A-031

No further action at Tier 0 unless something canonical needs revision.

---

## §3 Tier 1 — Structural-closure propagation (independent, parallelizable)

These items reflect structural closure through manuscript and engine. **No dependencies between items.** Any order, any pace.

### §3.1 E-094 — AVE-Core substrate-vocab propagation

**Scope:** Vol 1 Ch 1/4/6/7; Vol 2 Ch 1; Vol 3 Ch 2; Vol 4 Ch 1; glossary; src/ave/core/constants.py docstrings

**Effort:** 5-8 hours focused authoring (mostly additive cross-refs to `trampoline-framework.md` + App G)

**Documentation target:** Each chapter gets:
- Substrate-native vocabulary box near first physics statement
- 3-column Rosetta-stone where applicable (substrate-native / EE / ME)
- Cross-ref to `trampoline-framework.md` as canonical picture-first reference
- Cross-ref to AVE-QED App G + glossary §5m as upstream vocab source

**L5 ID:** E-094 in `manuscript_pending.md` (HIGH PRIORITY)

**Status transitions:** queued → in-review (when chapter PR opens) → applied (`<commit-sha>`)

### §3.2 E-101 — Three substrate invariants observables module

**Scope:** new `src/ave/core/boundary_invariants.py` + tests; computes 𝓜, 𝓠, 𝓙 at any boundary ∂Ω

**Effort:** 3-4 hours engine + tests

**Documentation target:**
- Module docstring referencing AVE-QED App G §4 (canonical definitions)
- `src/tests/test_boundary_invariants.py` with: (a) known-analytical-boundary tests; (b) v14 breathing-soliton integration test asserting 𝓜, 𝓠, 𝓙 conservation; (c) canonical-electron-value cross-check
- Cross-ref from `trampoline-framework.md` §4.3 to engine implementation

**L5 ID:** E-101

### §3.3 E-102 — Vol 3 Ch 4 cosmic-𝒥 identification

**Scope:** Vol 3 Ch 4 generative cosmology — explicit identification of $\mathcal{J}_{\text{cosmic}}$ as cosmological IC

**Effort:** 1 hour

**Documentation target:**
- New §sec:cosmic_J_as_IC (or similar) declaring $\Omega_{\text{freeze}} = \mathcal{J}_{\text{cosmic}}/I_{\text{cosmic}}$
- Universe-as-vortex MECHANIZED statement (E-019 closure)
- Three-route consistency framework (α + G + 𝒥)
- Cross-refs: `trampoline-framework.md` §1.3.7; A-031; AVE-QED App F multi-scale Machian network

**L5 ID:** E-102

### §3.4 E-103 — Vol 3 Ch 21 same-epistemic-horizon framing

**Scope:** Vol 3 Ch 21 BH Interior Regime IV — brief note that the substrate-observability rule's epistemic horizon applies at every scale

**Effort:** 30 minutes

**Documentation target:** Short paragraph cross-cutting from BH interior (Kerr-BH observers see M, Q, J from outside but not the matter-history inside) to cosmic interior (we see 𝓜, 𝓠, 𝓙 of our cosmic boundary but not "God's Hand" beyond)

**L5 ID:** E-103

### §3.5 AVE-QED App F cosmic-𝒥 row explicit

**Scope:** AVE-QED `manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex` — cosmic row gets explicit $\mathcal{J}_{\text{cosmic}}$ observable

**Effort:** 30 minutes

**Documentation target:** Update Figure F.1 caption + multi-scale table to include explicit 𝓙_cosmic per A-031

**L5 ID:** (new — sibling to E-102, this is AVE-QED side)

### §3.6 README + LIVING_REFERENCE structural-closure declaration

**Scope:** AVE-Core top-level docs declare framework reached structural closure 2026-05-15

**Effort:** 1 hour

**Documentation target:**
- `README.md` — add "Framework Status: Structural Closure 2026-05-15" section
- `LIVING_REFERENCE.md` — add canonical pointer to `trampoline-framework.md` as picture-first entry point + `closure-roadmap.md` as planning artifact
- `.agents/CURRENT_STATE.md` — update with structural-closure declaration + path forward

**L5 ID:** (new)

### §3.7 v14 Mode I regression test in `make verify`

**Scope:** prevent future engine regressions from breaking Mode I PASS

**Effort:** 1 hour

**Documentation target:**
- New `src/tests/test_master_equation_v14_mode_i.py` — runs the v14 breathing-soliton driver, asserts V_peak mean > 0.2, FWHM stable, n(r) gradient measurable
- Wire into `Makefile` `verify` target

**L5 ID:** (new)

### §3.8 Figure 2 storage-modes layout fix

**Scope:** regenerate `02_three_storage_modes.png` with cleaner layout (state vector arrow currently buried in sphere)

**Effort:** 30 minutes (script already exists with revised version queued)

**Documentation target:** updated PNG; trampoline-framework.md figure ref unchanged

**L5 ID:** n/a (cosmetic)

**Tier 1 total scope:** ~12-15 hours. No item blocks another. Can be split across 3-5 sessions.

---

## §4 Tier 2 — Theoretical closure keystone (Q-G47 Session 6+)

**The keystone of theoretical closure.** Nothing else in Tier 3 can finalize without this.

### §4.1 Q-G47 Session 6+ rigorous u_0* derivation

**Scope:** complete the Q-G47 closure that Sessions 1-5 framework-prepared.

**Plan doc:** see `AVE-QED/docs/analysis/2026-05-15_Q-G47_session_6_plus_plan.md` for the session-by-session breakdown.

**Effort:** 3-6 weeks analytical work, ~20-40 hours total

**Documentation target:**
- 5+ session docs at AVE-QED `docs/analysis/2026-XX-XX_Q-G47_sessionN_*.md` (one per session)
- Final closure doc: `2026-XX-XX_Q-G47_closure.md` with the rigorous u_0* value + connection to Q-factor identity
- Updates to A-027 (two-engine), A-001 (α-as-calibration), A-030 (α+G joint) closing the "rigorous closure pending sessions 6+" caveat
- Trampoline-framework.md §11 migration: K = 2G operating point moves from "framework complete; rigorous closure pending" to canonical

**L5 ID:** Q-G47 (existing); A-027 / A-029 / A-030 (status migration on closure)

**This is the most important pending derivation in the entire framework.** It unblocks Tier 3.

---

## §5 Tier 3 — Theoretical closure (Tier 2 dependencies)

### §5.1 T_EM(u_0*) explicit closed-form

**Scope:** explicit numerical expression for bulk substrate tension at the magic-angle operating point

**Effort:** 1-2 weeks (included in Q-G47 Session 6+ scope likely)

**Depends on:** Tier 2 (Q-G47 Session 6+ closure giving u_0*)

**Documentation target:** included in Q-G47 closure doc + cross-ref from trampoline-framework.md §5.5

### §5.2 Vol 3 Ch 4 explicit ξ(R_H, ℓ_node) derivation

**Scope:** Machian impedance integral computed end-to-end from cosmic horizon and lattice scale

**Effort:** 1-2 weeks

**Depends on:** independent of Q-G47 — can run parallel

**Documentation target:**
- Vol 3 Ch 4 new §sec:machian_integral
- Companion KB leaf `vol3/cosmology/ch04-generative-cosmology/machian-impedance-integral.md`
- Updates to A-030, A-031 status

**L5 ID:** new E-NNN (queue in `manuscript_pending.md`)

### §5.3 Three-route α/G/𝒥 consistency verification

**Scope:** verify the three observational routes (α + G + cosmic 𝒥) give the same u_0*. Falsification test for single-parameter cosmological-anchoring claim.

**Effort:** 1 week (numerical verification + writeup)

**Depends on:** Tier 3.1 + 3.2 (T_EM + ξ closed); Tier 5.2 (cosmic 𝒥 prediction)

**Documentation target:**
- New `docs/analysis/2026-XX-XX_three_route_consistency.md` (in AVE-Core or AVE-QED)
- Result documented EITHER WAY:
  - **PASS:** framework theoretically closed; trampoline-framework.md §11 migration; A-030/A-031 status closure
  - **FAIL:** framework requires revision; identify which route(s) broke; document the failure mode in `axiom_derivation_status.md`
- Verification script in `src/scripts/verify/three_route_consistency.py` for ongoing re-run

**L5 ID:** A-030 + A-031 (status closure on verification)

---

## §6 Tier 4 — Independent theoretical work (parallel to Tier 2/3)

No dependency on Q-G47 Session 6+. Can run anytime.

### §6.1 First-law T·dS = dE axiom-first closure (A-002)

**Scope:** close the open Flag 62-A — derive first law from Ax 1 + Ax 4 + rupture thermodynamics (or accept S_thermodynamic as Ax 5 candidate)

**Effort:** 2-3 weeks analytical

**Documentation target:**
- Vol 3 Ch 11 §sec:first_law expanded with axiom-first derivation
- Research doc at AVE-Core `research/L3_electron_soliton/` (or successor location)
- A-002 status closure

**L5 ID:** A-002

### §6.2 Cosserat coupling on Master Equation FDTD

**Scope:** add Cosserat (u, ω) microstructure as constitutive layer modulating ε_eff(V) and μ_eff(V) on Master Equation FDTD engine

**Effort:** 2-3 weeks engine work

**Documentation target:**
- New `src/ave/core/master_equation_cosserat_coupled.py` (or extension to existing engine)
- Driver scripts for 7-mode bubble validation (3 translational + 3 rotational + 1 volumetric)
- Research doc capturing v14-style empirical validation of full 7-mode hosting
- Regression test
- doc 113 §5.4 status closure

**L5 ID:** doc 113 §5.4 (informal); should be elevated to E-NNN

### §6.3 Strict stationary soliton via imaginary-time propagation

**Scope:** replace t → iτ in Master Equation; find true stationary attractor (vs current breathing solution)

**Effort:** 1-2 weeks engine work

**Documentation target:**
- Engine extension at `src/ave/core/master_equation_fdtd.py` (imaginary-time mode)
- Driver script + research doc
- doc 113 §5.1 status closure

**L5 ID:** doc 113 §5.1 (informal); should be elevated

### §6.4 Multi-soliton dynamics (Coulomb-law validation)

**Scope:** plant TWO breathing solitons on Master Equation FDTD lattice; study interaction; verify 1/r² Newtonian at large d

**Effort:** 2-3 weeks engine work

**Documentation target:**
- Multi-soliton driver script
- Force-distance measurement protocol + results
- Research doc + Vol 3 Ch 3 cross-ref (refractive-index-of-gravity validation)
- doc 114 §4.3 status closure

**L5 ID:** doc 114 §4.3 (informal); should be elevated

### §6.5 Q-G45 multi-soliton interference as gravity (derivation)

**Scope:** analytical derivation of macroscopic gravity from multi-soliton substrate interference

**Effort:** 2-3 weeks analytical (depends on §6.4 engine work landing)

**Documentation target:**
- AVE-QED App F §multi_soliton expanded with formal derivation
- Vol 3 Ch 1 (Gravity and Yield) updated
- Q-G45 status closure

**L5 ID:** Q-G45

### §6.6 Higher-energy soliton ((2,5) cinquefoil)

**Scope:** test if Master Equation FDTD hosts proton-like (2,5) cinquefoil bound state

**Effort:** 2-3 weeks engine work

**Documentation target:** engine + driver + research doc

**L5 ID:** doc 114 §4.4

---

## §7 Tier 5 — Empirical closure (independent of theoretical work, runs in parallel)

### §7.1 Cosmic 𝒥_cosmic literature review (CMB + LSS)

**Scope:** survey CMB low-multipole anomalies ("axis of evil"), LSS rotation correlations, Hubble flow anisotropy measurements

**Effort:** 2-3 weeks

**Documentation target:** new `docs/analysis/cosmic_J_observational_constraints.md` with literature summary + AVE prediction comparison framework

**L5 ID:** A-031

### §7.2 AVE prediction for 𝒥_cosmic from numerics

**Scope:** compute 𝒥_cosmic from $\Omega_{\text{freeze}} \cdot I_{\text{cosmic}}$ given Tier 3 numerical closures

**Effort:** 1 week

**Depends on:** Tier 3 (T_EM + ξ closed)

**Documentation target:** Vol 3 Ch 4 §sec:cosmic_J_prediction with explicit numerical value + uncertainty bounds

**L5 ID:** A-031

### §7.3 IVIM bench Phase 2A build

**Scope:** physical bench construction per Bench-VM procurement plan

**Effort:** 2-3 months physical work (Grant's parallel)

**Documentation target:** Bench-VM build docs; commit-tracked equipment list + assembly notes

**L5 ID:** Q-G46 procurement; closes Q-G42 + Q-G46 on measurement

### §7.4 IVIM measurement campaign

**Scope:** run measurements; verify D10 IM3 cubic V³ slope + autoresonant breakdown predictions

**Effort:** 3-6 months

**Depends on:** §7.3 bench built

**Documentation target:** Bench-VM measurement records; cross-ref to AVE-Core predictions docs; Q-G42 + Q-G46 status closure

**L5 ID:** Q-G42 + Q-G46

---

## §8 Tier 6 — Empirical-dependent derivations

Cleaner after Tier 3 closes (for confidence) but not strictly blocked.

### §8.1 Q-G43 atom-scale local Γ=-1 derivation

**Scope:** derive AVE prediction for atomic-shell boundary saturation per App F's ?-marked atom row

**Effort:** 2-4 weeks

**Documentation target:** new research doc + Vol 2 Ch 7 update + App F atom-row migration ?-marked → derived

**L5 ID:** Q-G43

### §8.2 Q-G44 helio-scale local Γ=-1 derivation

**Scope:** same as Q-G43 but for heliopause/Oort boundary

**Effort:** 2-4 weeks

**Documentation target:** new research doc + Vol 3 Ch 6 update + App F helio-row migration

**L5 ID:** Q-G44

### §8.3 App F atom + helio rows: ?-marked → derived

**Scope:** AVE-QED App F refresh after Q-G43 + Q-G44 close

**Effort:** 5-8 hours

**Depends on:** §8.1 + §8.2

**Documentation target:** App F multi-scale table updated; Figure F.1 caption updated

---

## §9 Tier 7 — Manuscript finalization

### §9.1 All queued E-NNN entries applied (currently 30+ in manuscript_pending.md)

**Effort:** 20-40 hours sustained sweeping

**Documentation target:** each E-NNN closes with commit SHA; `manuscript_pending.md` drains to near-empty

### §9.2 Picture-audit infrastructure

**Scope:** formalize picture-first discipline per ave-prereg Step 1.5 — `docs/picture-audit/` with template + sample audits

**Effort:** 4 hours one-time setup

**Documentation target:** new `docs/picture-audit/` directory; ave-prereg skill updated

### §9.3 L3 + L5 deletion with cross-reference migration

**Scope:** the original cleanup that triggered the structural-closure session

**Effort:** 2-3 hours

**Depends on:** §9.1 (manuscript_pending mostly empty); §8.3 (App F rows derived); all canonical content propagated to chapter-bound homes

**Documentation target:**
- Verify no orphan cross-references remain
- `git rm -r research/L3_electron_soliton/ research/L5/`
- Single commit referencing the L5-driven incorporation work history

### §9.4 Backmatter "Framework Status" section

**Scope:** publication-level declaration of framework state at time of pressing

**Effort:** 1 hour

**Depends on:** Tier 5 measurements verified; three-route consistency closed

**Documentation target:** new `manuscript/backmatter/framework_status.tex`

### §9.5 Publication-ready manuscript pass

**Scope:** full Vol 1-4 review for consistency, completeness, prose quality

**Effort:** open

**Documentation target:** publication-ready PDFs

---

## §10 Documentation discipline framework

**Six rules that prevent slippage:**

### Rule 1 — Every action has a tracker ID before it starts

Format: E-NNN in `manuscript_pending.md` or `engine_pending.md`; A-NNN in `axiom_derivation_status.md`. If an action isn't in a tracker, it isn't happening. Discoveries that don't fit any existing entry generate a new entry on the spot.

### Rule 2 — Every commit cites its tracker ID

Format: `feature/fix: short description (E-NNN / A-NNN)`. Makes git-log searchable by tracker entry. Example:

```
trampoline-framework.md §5.5: Machian G as bulk integral (A-030)
```

### Rule 3 — L5 status transitions are real-time

When status changes (queued → in-review → applied), commit the status update in the SAME commit as the implementation. No batched retroactive updates. The tracker is the live state.

### Rule 4 — Cross-references are bidirectional

If doc A cites doc B, doc B's cross-references include doc A. Periodic audit (every ~10 sessions or before Tier 7 finalization) verifies link reciprocity.

### Rule 5 — Picture-first discipline

Any new physics claim destined for a manuscript chapter must first be reflected in `trampoline-framework.md` (or its successor). Chapter edits cite the canonical picture, not the reverse.

### Rule 6 — No orphan work

Every action either (a) closes a tracker entry, (b) opens a new tracker entry with its dependencies, or (c) updates an existing entry's status. Discoveries that don't fit any of those generate a new entry on the spot.

### Status dashboard update protocol

After every significant work session:
1. Update the dashboard at §0 with new SHA + date in "Last touch" column
2. If status transitioned, note in the relevant tier section
3. If a tier milestone closed, update §1 closure-state taxonomy
4. If a critical-path item moved, note in §11 critical-path call-outs

---

## §11 Critical-path call-outs

### Things that COULD break the framework (watch for)

1. **Three-route inconsistency** — if Q-G47 Session 6+ gives a u_0* that doesn't match the G route's u_0* (Vol 3 Ch 4 ξ derivation) or the cosmic-𝒥 route, the single-parameter claim fails. **Falsification.**

2. **IVIM bench null result** — if D10 IM3 cubic V³ slope doesn't appear at the predicted value, framework's predictive power is questioned at the bench scale.

3. **Cosmic 𝒥_cosmic inconsistency** — if CMB anomalies + LSS rotation give a 𝒥_cosmic that doesn't match the α + G route's predicted value, framework fails.

4. **Cosserat coupling on Master Equation FDTD doesn't host bound state** — would force rethinking the two-engine architecture; not a hard fail but a major revision.

5. **Q-G47 Session 6+ shows no magic-angle operating point** — if there's no u_0* at which K = 2G with the specific geometric factors AVE assumes, the closure chain breaks at its foundation.

### Things that ADVANCE the framework (look for)

1. **Q-G47 Session 6+ closes with u_0* matching α route** — first major theoretical milestone
2. **Vol 3 Ch 4 ξ derivation gives G consistent with CODATA** — second major milestone
3. **IVIM Phase 2A shows IM3 V³ slope at predicted value** — first independent empirical verification
4. **Cosmic 𝒥 estimate from CMB + LSS consistent with α/G chain** — closes the three-route loop empirically
5. **Cosserat coupling on Master Equation FDTD demonstrates 7-mode bound state** — engine work completes

---

## §12 Cross-references

**Canonical framework reference:** `manuscript/ave-kb/common/trampoline-framework.md`

**Q-G47 closure plan:** `AVE-QED/docs/analysis/2026-05-15_Q-G47_session_6_plus_plan.md`

**L5 trackers:**
- `research/L5/manuscript_pending.md` (E-NNN manuscript queue)
- `research/L5/engine_pending.md` (E-NNN engine queue)
- `research/L5/axiom_derivation_status.md` (A-NNN framework-level claims)
- `research/L5/living_documentation_tracker.md` (L3 doc index + clash registry)
- `research/L5/terminology_canonical.md` (substrate-native vocab)
- `research/L5/cross_repo_references.md` (sibling-repo path catalog)

**Historical precursor:** `research/L3_electron_soliton/114_next_steps_consolidation_plan.md` (post-2026-05-14 session plan; superseded by this doc for forward-looking planning)

**Session HANDOFF:** `.agents/HANDOFF.md` should reference this doc's dashboard at top

---

## §13 Maintenance

This doc is **canonical living planning artifact**. Update when:
- A status transition occurs at any tier
- A critical-path item progresses or breaks
- A new action is identified that doesn't fit existing tiers
- A tier milestone closes (move to historical, declare closure-state migration)

Updates that should NOT be made here:
- New analytical derivations (those land in the source manuscript chapters / KB leaves; this doc references them)
- Speculative framings (those land in `research/L5/axiom_derivation_status.md` as A-NNN entries)
- Session-by-session execution details (those land in dated analysis docs per L5 schema)

**Cross-cutting invariants** (per `manuscript/ave-kb/CLAUDE.md`): this doc uses $\mathcal{M}_A$ for substrate (INVARIANT-N1), $\ell_{\text{node}}$ script ell (INVARIANT-N2), Scheme A axiom numbering (INVARIANT-S2). No conflicts.
