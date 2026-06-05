# Experimental Protocol Revamp — Orchestration Epic (2026-06-03)

**Purpose:** survey + challenge/revamp experimental protocols across the AVE experimental
repos, prioritize the clearest/most-rigorous *discriminating* tests, spawn per-repo
implementors (challenge/harden, not greenfield), integrate results back into AVE-Core. Per
Grant 2026-06-03.

**Provenance:** 5 parallel read-only surveys (QED / benches+apparatus / domain / bio+topo /
Core-matrix-spine), 2026-06-03. Survey findings are **agent-reported** — every load-bearing
claim (magnitudes, file:line, discrimination) is verified-to-source during brief-building per
`verify-before-cite` BEFORE it drives an implementor.

**Discipline:** `ave-discrimination-check` (the lens), `ave-prereg` + `ave-canonical-leaf-pull`
(per revamp), `ave-walk-back` (KB-leaf propagation), `ave-evidence-framing-discipline`,
worktree-isolation + branch-check + wait-for-notification, adjudicate-don't-auto-merge cross-repo.

---

## §1 Consolidated ranked board

| Tier | Protocol | Repo | Discrimination | $ / horizon | State | Key gap / action |
|---|---|---|---|---|---|---|
| **A1** | HOPF chiral antenna (01/02) | AVE-HOPF | clean binary — pq/(p+q) slope **=α** + medium-independence (AIC/BIC-gated) | **$123 / weeks** | apparatus-built, pre-measurement | **Phase-0: verify slope=α is substrate-derived, not fitted** → potential experimental α-readout |
| **A2** | IVIM Bragg vacuum-mirror | AVE-Bench-VacuumMirror | clean binary, **12 OOM** (V⁴ scaling + Bragg-angle) | $45–55k / months | pre-reg, Phase-0 done | adversarial re-verify Γ=1.94e-11 + systematics; then build |
| **B1** | Sagnac-RLVE | AVE-PONDER | binary (2 rad vs ~1e-20) | $2–3k / months | designed + **OPEN PR #1** | FOG-non-detection killer-Q + C17/C18 walk-back reconcile (PR #1 fixes only the Ψ-framing) |
| **B2** | Cleave-01 PZT topological charge | AVE-Bench-FemtoElectrometer | slope 41.5 mV/μm (**zero free param**, e/ℓ_node) | $7.7k / weeks | pre-reg | weak SM counterfactual (null-corrob) → revamp to two-sided via dielectric-invariance leg |
| **B3** | Tesla D2 hysteresis + D10 IM3 | AVE-Tesla | binary (loop) + slope (V³ vs QED V⁶) | $107k / 12–18mo | pre-reg Phase 2 | keep D2/D10; **drop or fix** D1 (no closed form) / D4 (drift lifetime unpredicted) / D6 (±1e5 flux) |
| **C1** | Protein random-conf + basin-multiplicity | AVE-Protein | slope (basin landscape) | compute / days | pre-reg, not run | **CONFOUND: r=−0.64 anti-corr R_A'' vs RMSD** → lock Phase-0 substrate-derivation of thresholds; GATE |
| **C2** | Neurology Q-NEURO-004 VR PoV (7 F's) | AVE-Tangents/AVE-Neurology | binary (F1/F2/F3 EEG-γ) + slope (F5 MAC/DTI) | $15–55k / 3–6mo + IRB | pre-reg, pre-IRB | high bio-confound (γ-artifacts, individual var) → GATE on EM-layer result |
| **RETIRE** | Casimir (sub-nm + acoustic) | AVE-QED, AVE-Metamaterials | non-discriminating (both surveys agree) | — | designed | retire from roadmap — no new observable vs QED |
| **AVOID/SPLIT** | Cold-fusion Pd/D | AVE-Fusion | unfalsifiable 0.90–0.929 window | — | idea | split: keep only the clean falsifier leg "any measured Pd/D > 1.858 kills AVE" |
| **DEMOTE** | muon g-2 / Lamb / PVLAS static-B / RT-superconductivity / HTS-KI / PONDER-01 / acoustic-rect | QED/Metamat/Propulsion/PONDER | postdiction / null-corrob / next-gen-only / mfg-impossible / no-closed-form-magnitude | — | mixed | off the near-term track (PVLAS revisit at 1e-24; RT-SC flagged "huge if real" but mfg <0.001% defect implausible) |
| **PARK (facility)** | Schwinger-autoresonant / metric-fusion / baryon-ladder / e-parallax | QED/Fusion/Core | clean but facility-class | $1M–$100M / years | idea/derivation | park; revisit if a partner facility opens |

**Already-executed anchors (not to-build):** C13a SPARC galactic rotation (zero-param, 11.5%
mean residual, DONE — foreword anchor); C1 BH ringdown (LIGO, PASS at GR-class); C5 CMB axis
(driver ran, Outcome-D data-insufficient). These are analysis results, not bench protocols.

---

## §2 Cross-cutting findings

1. **Saturation-kernel / α dependence (load-bearing).** Most domain/propulsion magnitude
   predictions route through V_yield = √α·V_snap + the Ax-4 kernel S(V). Per the 2026-06-02
   honest-α relabel, α's *value* is closed-form-at-one-identification (Class B). So these
   experimental magnitudes inherit Class-B status — only as firm as the kernel. (NB: several
   surveys mis-flagged V_yield=43.65 kV as "asserted, not derived" — it is canonical in
   `constants.py`; the fair statement is "inherits the kernel," not "circular.")

2. **HOPF antenna slope = α — potential experimental α-readout.** HOPF-01/02 predicts the
   antenna Δf slope equals α ≈ 1/137. The 2026-06-02 work concluded the *substrate does not
   independently select* α. So the load-bearing Phase-0 question for HOPF is: **is the measured
   antenna slope a genuine substrate-derived α, or a fitted coefficient that lands near 1/137?**
   If genuine, this is a tabletop experimental α-determination — directly ties the experimental
   pivot to the α close. This elevates HOPF beyond "cheap antenna test."

3. **Casimir is non-discriminating** (QED + Metamaterials surveys independently agree) — same
   magnitude + d⁴ scaling as QED, only the *mechanism* relabels. Retire.

4. **Sagnac discriminator = magnitude, not Ψ-ratio** (GR scales with density too). **Already
   under fix in AVE-PONDER PR #1** (§3). The *deeper* gap — why existing fiber-optic gyros don't
   already see a 2-rad effect, and reconciliation with the retired C17/C18 Sagnac claims — is
   NOT addressed by that PR and is the real Phase-0 for B1.

---

## §3 AVE-PONDER open PR #1 (in-flight — coordinate, don't duplicate)

- PR #1 "PONDER Ch.6 Sagnac-RLVE: fix GR-discrimination framing (magnitude, not the Ψ=7.15
  ratio)" — branch `discipline/2026-06-01-sagnac-gr-discrimination-fix`, OPEN since 2026-06-02,
  1 commit `eb7a49b`. **AVE-PONDER working tree is checked out ON this branch.**
- It independently confirms the domain survey's Sagnac finding (magnitude-not-ratio).
- **Implications:** (a) review/adjudicate this PR FIRST — Grant's merge call; (b) the Sagnac
  implementor builds ON it under worktree-isolation to avoid contaminating the PR branch; (c)
  the FOG-non-detection killer-question + C17/C18 reconciliation are separate, deeper issues
  this PR does not touch.

---

## §4 Proposed per-repo spawn plan (PENDING Grant's adjudication)

**Spawn now (challenge/harden, worktree-isolated, background):**
1. **AVE-HOPF** — verify antenna slope=α provenance (substrate vs fitted; reconcile honest-α);
   lock systematic-error budget (control null-shift tolerance); confirm pq/(p+q) + medium-
   independence discrimination is clean vs classical antenna theory. → hardened pre-reg + Core row.
2. **AVE-Bench-VacuumMirror** — adversarial re-verify Γ + V⁴ to `constants.py` source; stress-
   test the Ch-23 pre-reg decision tree; audit the systematic list. → hardened protocol + Core row.
3. **AVE-PONDER** — review/adjudicate PR #1; then the real work: answer the FOG-non-detection
   killer-question + reconcile C17/C18. Survive-or-retire verdict. → verdict + Core row.
4. **AVE-Bench-FemtoElectrometer** — revamp Cleave-01 to a two-sided discriminator (dielectric-
   invariance leg) so a null falsifies, not just confirms SM. → revamped pre-reg + Core row.

**Light retire-adjudication (no full implementor):** AVE-QED + AVE-Metamaterials (retire
Casimir; demote non-discriminators); AVE-Fusion (split cold-fusion claim to the clean falsifier
leg). These are walk-back propagations, not new protocols.

**GATE (do NOT spawn yet — gate on EM-layer results):** AVE-Protein (confound r=−0.64 must be
resolved at Phase-0 first); AVE-Tangents/Neurology (bio-confound; gate on HOPF/IVIM).

**Optional / lower priority:** AVE-Tesla (keep D2/D10, drop the D1/D4/D6 cascade).

---

## §5 Integration-to-Core mechanism (incl. experimental KB-leaf discipline — Grant 2026-06-03)

Every implementor deliverable includes BOTH:
- **(a) Per-repo:** the hardened protocol doc + its **per-repo experimental KB leaf** updated.
- **(b) AVE-Core update package:** the `divergence-test-substrate-map.md` row (Predictions +
  Lifecycle + Execution-details) + `appendix-experiments.md` entry + `closure-roadmap.md` §0.5
  changelog — **per `ave-walk-back` propagation** (the experimental KB leaves and the matrix row
  move in lockstep; no stale-leaf stragglers).

**Experimental KB leaves are updated as part of every revamp — per-repo leaf + Core matrix row
together (Grant 2026-06-03).** Orchestrator adjudicates the Core updates (does NOT auto-merge
sibling→Core), lands with Grant's merge-go, tracks cross-repo promotions via the promotions-tracker.

---

## §6 Decision needed from Grant

1. **Confirm the spawn set** — 4 now (HOPF, VacuumMirror, PONDER, FemtoElectrometer)? Adjust?
2. **AVE-PONDER PR #1** — review + merge before the PONDER implementor builds on it, or leave open?
3. **Gates** — agree Protein + Neurology gate on EM-layer (HOPF/IVIM) results?
4. **Retires** — greenlight retiring Casimir + splitting the cold-fusion claim?

---

## §7 Implementor verdicts (2026-06-03) — all 4 home, deflationary sweep

| ID | Verdict | Survives as | Branch (pushed, not merged) |
|---|---|---|---|
| **HOPF A1** | α-readout **FALSE** (slope=α CODATA-injected `constants.py:133`; form-shared w/ classical coupled-line) | medium-independence + enantiomer-sign legs ($123, HOPF-02a) | `analysis/2026-06-03-hopf-antenna-harden` (AVE-HOPF, `871189b`) |
| **IVIM A2** | discrimination **SOUND** (8.38e12, V⁴ to source); headline magnitude + APD detection NOT defensible (corpus self-contradicts 15–30 OOM, half-walked-back) | HELD pending Grant R-A (interferometric walk-back) vs R-B (derive N²-Bragg) | `analysis/2026-06-03-ivim-harden` (VacMirror, `7745954`) |
| **Sagnac A2** | **RETIRE** → corroborative-null (Earth-rotor +7e-4 bias excluded by RLG geodesy 7e4×; Ch.6 eq.80 10⁶ arithmetic error) | W-vs-Al Ψ=7.15 self-consistency only | `analysis/2026-06-03-sagnac-fog-question` (PONDER, `d0cac77`) |
| **Cleave B2** | two-sided revamp **WORKED** (conditional on detection; P3 all-null irreducible); slope 41.490 mV/μm to source | clean 2-sided, $7.7k; pending gap-dielectric call | `analysis/2026-06-03-cleave-two-sided` (Femto, `47d58a3`) |

Meta: the survey + Phase-0 gates caught 1 injected-α (HOPF), 1 excluded-by-existing-data (Sagnac), 1 internally-contradictory (IVIM), 1 genuine-upgrade (Cleave). Every headline corrected — the deflation IS the deliverable.

## §8 Skill-candidates watch (Grant "keep tabs" 2026-06-03)

- ✅ **ave-ee-intuition-summary** — CREATED + committed (`~/.claude/skills`, `b94edc5`). 5-beat EE-mapped intuition summary; battle-tested on IVIM/HOPF/Sagnac. Self-audit (`ave-newly-created-skill-self-audit`): the 4 per-experiment summaries are owed → land them in the KB leaves.
- 📋 **ave-experimental-protocol-survey** — the 5-survey discrimination-ranked-board fan-out pattern (this epic §1). Candidate.
- 📋 **ave-discrimination-check amendment** — the three discriminator-failure modes (form-shared / already-constrained-by-existing-data / injected-magnitude); 2 of 3 fired today (Sagnac already-constrained, HOPF injected). Candidate.
- 📋 **ave-walk-back amendment** — "resurrection detection": a walk-back started then reverted elsewhere without re-adjudication (IVIM Camp-A-WKB-walked-back → Camp-B-Bragg-resurrected, 15–30 OOM). Candidate.

## §9 Cleanup state + pending

- **Landing now:** HOPF A1 + Sagnac A2 Core walk-backs (worktree-isolated implementer → branch `analysis/2026-06-03-hopf-sagnac-walkbacks`); orchestrator reviews + merges.
- **Pending Grant decisions:** (1) IVIM **R-A vs R-B**; ~~(2) Cleave **gap-dielectric-vs-ℓ_node**~~ → **RESOLVED 2026-06-03**: gap-dielectric **LOCKS** dielectric-invariant — the gap-protection is on the integer linking charge $\mathcal{Q}=\mathrm{Link}(\partial\Omega,\mathbf{F})\in\mathbb{Z}$ (no-hair-blind to Pauli-filled interior occupancy; node-occupation = Pauli = Axiom-4 ceiling, corpus-derived), and $\xi_{topo}=e/\ell_{node}=\sqrt{\alpha}$ is the frozen-metric unit-bridge, NOT a Chern number. C15 Type-D walk-back **merged to main `d2b37f53`** (audit tag `audit/2026-06-03_cleave-occupation-derivation`, implementor tip `ccb1f14e`); ~~(3) HOPF protocol-doc correction (approval-gated AGENTS.md §117)~~ → **RESOLVED 2026-06-04** (Grant-approved full §6 sweep applied to `hopf_01_TEST_PROCEDURE.md` §6.2/§6.3 + Decision Gate — slope=α reframed consistency-class, medium + enantiomer = AVE-distinct; AVE-HOPF branch `analysis/2026-06-03-hopf-antenna-harden` `e4989d2`, pushed not merged). IVIM Core walk-back finalizes after (1).
- **Sibling-repo merges (durable on origin, pending):** the 4 hardened-protocol branches merge to their repos with audit-tags — sequenced after the Core walk-backs + decisions.
- **flag-don't-fix queue:** stale `:205`→`:246` ξ_topo cites (4 sites); `vacuum-impedance-mirror.md:67-79` retired-Reading-M framing (IVIM); ~~`flyby-anomaly…:237`~~ **FIXED** (`7f7447cb`); HOPF stale crib-sheet.

---

## §10 — Kernel-discovery thread + current board (2026-06-03)

**The thread (how the experimental pivot unfolded, with Grant):** Sagnac-RLVE retired (achiral *density* coupling — GR-shared, RLG-excluded) → Grant: "spinning chiral impedance-matched antenna to couple to the lattice?" → **chirality, not density, is the AVE-distinct channel** (GR/EM have no parity-odd vacuum coupling) → that channel *is* HOPF → its (p,q)-chiral term is **nonlinear-saturation** (above V_yield), not linear → Grant: "autoresonance/PLL — measure the **AC response of the bulk lattice, not DC**" → characterize the vacuum as a **saturable reactor** (yield-knee map) → grep: the literal knee at V_yield is **bench-unreachable** (V_yield is per-node), but the reachable AVE-distinct observable is the **tree-level V²-coefficient SIGN** (AVE softens δε/ε₀=−A²/2; QED stiffens) → **converged onto Q-G42** (the prior Phase-0, decision-ready).

**Two preregs (committed):**
- `research/2026-06-03_spinning-chiral-coupling-prereg.md` — **CLOSED Outcome B/C** (mechanical spin conflates internal-Cosserat-ω with bulk-ω; category substitution caught by grep; superseded).
- `research/2026-06-03_yield-knee-map-prereg.md` — **reframed** to the tree-level V²-coefficient SIGN test; resume from Q-G42.

**The convergence (the session's experimental core):** the saturation kernel ε_eff(V)=ε₀√(1−(V/V_yield)²) is the coherent center — measured **three ways, same physics**: IVIM (reflectance Γ(V)), PONDER-05 (C–V, 27.4% ε-collapse at V_DC/V_yield=0.687), Q-G42 (V²-coefficient sign). HOPF is the *parity* channel; the kernel is the *saturation* channel. **All three pivots this session (HOPF, IVIM, Q-G42) converged onto existing corpus work** — the program is far more coherent than the survey's pile suggested.

> **⚑ FLAG (2026-06-03, post-R-A mapping audit — [`research/2026-06-03_ivim-RA-adjudication.md`](../research/2026-06-03_ivim-RA-adjudication.md) §4):** the "three transducers, same physics" claim is now PARTIALLY UNDERCUT by the **per-node-V_yield / apparatus-voltage conflation**. IVIM's photon-counting magnitude is R-A-walked-back (unreachable as framed — leaf `vacuum-impedance-mirror.md` plugs gap-V into the per-node kernel; A~10⁻⁹ at 43 kV/100 µm, not 0.99; now interferometric). PONDER-05 (DC-biased **quartz**) raises a **vacuum-vs-material** consistency-vs-emergence question (is the 27.4% ε-collapse the vacuum kernel, or quartz's ordinary voltage-coefficient-of-capacitance relabeled?). If both resolve adversely, **Q-G42 (V²-sign) is the one clean forward discriminator of the kernel** — a material deflation needing Grant adjudication before corpus surgery. (Line 167's Q-G42 dispatch already tasked the G_geom reconcile + vacuum-vs-material separation; this finding sharpens why.) **Mechanical "fourth transducer" scoped (Grant's grain/piezo-coupling instinct, `ave-prereg` → [`research/2026-06-03_piezo-mechanical-fourth-transducer-prereg.md`](../research/2026-06-03_piezo-mechanical-fourth-transducer-prereg.md)):** GREEN-FIELD but BLOCKED — the mechanical channel exists only in the LOCKED (finite-strain) substrate reading = Grant's unresolved doc-109 trampoline question (canonical engine is SLIDING → mechanical strain collapses to the dead field channel); even locked, A_mech ~ 10⁻⁶ (δε/ε ~ 10⁻⁸ at fracture), grain-discriminator's materials-map open, κ_entrain real-power-excluded. **Not a rescue. ~~gated on the foundational locked-vs-sliding fork~~ → CORRECTED 2026-06-03 (full doc-109 read): RULED OUT, not gated — doc-109 was reframed (§13 boundary-envelope, impedance-only, Grant-confirmed) AND closed at v14 Mode I (doc 113: the Master Equation FDTD engine `src/ave/core/master_equation_fdtd.py` hosts a breathing-soliton bound state; K4-TLM cannot). The geometric-locked channel was reframed-against + empirically unneeded. Q-G42 stays the one clean discriminator.** T2 (κ_entrain real-power exclusion fences off the locked coefficient) stands; ~~T1~~ **DISSOLVED** — the neutron-lifetime "phonons shake 𝓜_A" is impedance-shaking (doc 109 §3.3/§13.8), consistent with impedance-only, not a tension.

**Meta-result:** the `ave-prereg` + corpus-grep discipline caught **two** dead-ends (spinning category-error; literal-knee unreachability) BEFORE any bench was built — the whole point of the discipline, demonstrated twice in one thread.

**Resumption (DISPATCHED 2026-06-03):** Q-G42 — derive the green-field **autoresonant Δf₀/f₀** small-signal number (Ch 15 lacks it) + design the **vacuum-vs-material separation** (universal −A²/2 vs material-specific electrostriction) + recommend the **detection architecture** (Q-G42 §4 Q1–Q3: precision-bridge ΔC/C~10⁻⁹ / cryo-lock-in 10⁻¹² / resonant-Q autoresonant 10⁻¹⁵) + reconcile the β/G_geom catalog ({30,10³,10⁵}).

**Current board (tiered, post-hardening):** LIVE = HOPF (chiral legs) · **Cleave (two-sided — occupation-gap CLOSED, walk-back merged `d2b37f53`)** · **IVIM (R-A adjudicated 2026-06-03: WKB-suppressed → interferometric re-scope; per-node-V_yield conflation = root of Camp-A/B; see [`research/2026-06-03_ivim-RA-adjudication.md`](../research/2026-06-03_ivim-RA-adjudication.md))** · **Q-G42 V²-sign kernel test (decision-ready)**. RETIRED = Sagnac/ROENTGEN-03 (landed) · Casimir (queued). GATED = Protein · Neurology. DONE anchors = SPARC · BH-ringdown. PARK = Schwinger · metric-fusion · baryon-ladder. DEMOTED = muon-g2 · Lamb · PVLAS-static-B · RT-SC · HTS-KI · PONDER-01 · acoustic-rect.

**Pending Grant decisions (parked behind the kernel thread):** ~~IVIM **R-A/R-B**~~ → **R-A adjudicated 2026-06-03** (interferometric re-scope; IVIM-local walk-back queued — see adjudication doc §6). ~~HOPF **§6.2** doc-correction~~ → **RESOLVED + applied 2026-06-04** (AVE-HOPF `e4989d2`, pushed not merged). ~~Cleave gap-dielectric~~ → **RESOLVED + merged `d2b37f53`**. **NEW (⚑ surfaced by the R-A mapping audit, BLOCKS corpus surgery):** per-node-V_yield/apparatus conflation is corpus-wide (conflated camp = `vacuum-impedance-mirror.md` + `measurement-hierarchy-snr.md:66` + `universal-saturation-kernel-catalog.md:72`; honest camp = Q-G42 + `trampoline-framework.md:439` + `claim-quality.md:393`) **+ the PONDER-05 vacuum-vs-material** consistency-vs-emergence question → both need Grant's call before the kernel-convergence narrative (§10 ¶3 flag) re-scopes. ~~Casimir retire + cold-fusion split~~ → **AVE-Core §0.5 changelog LANDED** (on origin/main; cross-repo leaf edits remain queued as chips: QED + Metamaterials Casimir, Fusion Pd/D).

---

## §11 — Round-1 merges LANDED + round-2 hardening DISPATCHED (2026-06-04)

**The 4 hardened round-1 protocol branches MERGED to their sibling-repo mains** (Grant merge-go
2026-06-04; worktree-isolated, `--no-ff`, audit-tagged, sibling mains ruff-clean):

| Protocol | Repo main | Audit tag | Verdict banked |
|---|---|---|---|
| Cleave two-sided | AVE-Bench-FemtoElectrometer `7cd73d1` | `audit/2026-06-04_cleave-two-sided` | **UPGRADE** — two-sided dielectric-invariance discriminator (slope 41.490 mV/μm = e/ℓ_node) |
| HOPF antenna-harden | AVE-HOPF `6a74498` | `audit/2026-06-04_hopf-antenna-harden` | **DEFLATION** — α-readout FALSE (CODATA-injected, form-shared); survives medium-indep + enantiomer-sign |
| IVIM re-verification | AVE-Bench-VacuumMirror `0e9070d` | `audit/2026-06-04_ivim-harden` | **DEFLATION** — V⁴ discrimination sound; headline photon-counting magnitude not defensible |
| Sagnac retire | AVE-PONDER `a097edd` | `audit/2026-06-04_sagnac-fog-retire` | **RETIRE** — corroborative-null (RLG-excluded 7e4×) + Ch.6 eq.80 10⁶ fix |

Merge notes: (a) PONDER PR #1 (`eb7a49b` GR-discrimination-fix) was already on main via `9d2a788`; the
fog-question merge added only the retire `d0cac77`. (b) IVIM had a ruff-format(origin)-vs-content(harden)
conflict on `scripts/analytical_gamma_v_sweep.py` — resolved by keeping harden content + re-applying ruff
format. (c) All 4 sibling repos' `origin/main` had concurrently merged Grant's `ci/mirror-core-tooling`
PRs; local mains were stale — caught at first push (non-fast-forward), re-merged onto fresh origin/main.
(d) Newly-merged drivers ruff-cleaned (predated the repos' ruff baseline; I001 + F541, behavior-preserving).
**Round-1 branches NOT deleted — pending Grant's separate branch-cleanup go.**

**Round-2 hardening DISPATCHED — 4 worktree-isolated background implementors (2026-06-04):**

| Hardener | Repo | Branch (push-don't-merge) | Round-2 attack |
|---|---|---|---|
| Cleave R2 | AVE-Bench-FemtoElectrometer | `analysis/2026-06-04-cleave-round2-smcounterfactual` | SM-counterfactual: can electrostriction/flexoelectric/triboelectric mimic BOTH the slope AND dielectric-invariance? + positive control + go/no-go SNR |
| HOPF R2 | AVE-HOPF | `analysis/2026-06-04-hopf-round2-chiral-counterfactual` | classical-chiral (bianisotropy/optical-activity) counterfactual on the 2 survivors (medium-indep + enantiomer-sign) |
| IVIM R2 | AVE-Core | `analysis/2026-06-04-ivim-round2-rescope` | R-A interferometric re-scope: derive Δφ off CORRECT per-node V_yield; re-scope leaf `vacuum-impedance-mirror.md`; inventory the broader per-node conflation (flag-don't-fix, Grant-gated) |
| Q-G42 R2 | AVE-Core | `analysis/2026-06-04-qg42-vsign-harden` | Phase-1: derive small-signal Δf₀/f₀; vacuum-vs-material separation; detection-architecture pick; β/G_geom catalog reconcile |

Each runs prereg→derive→auditor→result, push-don't-merge. **Round-2 results merge as a SECOND merge-call
round** (Grant go per branch, same pattern). The attacks deliberately re-aim the round-1 failure mode
(*form-shared-with-classical-theory*) at the survivors — round-2 MAY further deflate, which is the point;
merging round-1 first banked the auditable checkpoint.

**Pending:** round-2 verdicts (4 implementors in flight); round-1 sibling-branch cleanup (Grant go); the
broader per-node-V_yield/apparatus-conflation corpus sweep (still Grant-gated per §10).

---

## §12 — Round-2 hardening verdicts: ALL 4 HOME (2026-06-04)

All 4 round-2 implementors complete; branches **PUSHED-NOT-MERGED**; verdicts verified by orchestrator to
load-bearing level (driver-honesty + key citations + corpus-correction sanity); **AUDITOR-GATE PENDING
before any merge.**

| Protocol | Branch (tip) | Round-2 VERDICT | Net |
|---|---|---|---|
| **Cleave** | `analysis/2026-06-04-cleave-round2-smcounterfactual` (`76f66b9`) | **SURVIVES (conditional on gap-sweep)** | Found + cured a real **CPD (moving-Kelvin)** form-sharing trap round-1 missed; upgraded to a 4-corner symmetry discriminator {linear ∧ polarity-odd ∧ material-indep ∧ **gap-indep**}. GO, $7.7k, SNR 41,490×. **The flagship survivor.** |
| **Q-G42** | `analysis/2026-06-04-qg42-vsign-harden` (`fdd88c3`) | **FORWARD-DISCRIMINATOR (conditional)** | Δf₀/f₀ = +¼A²η_eff, **+sign** forward-distinct (driver verified forward/canonical); magnitude +1.8e-12…-15, only autoresonant-PLL reaches it; gated on per-node reachability-fork + **FN-destruction** (2.3e5× FN ceiling). |
| **IVIM** | `analysis/2026-06-04-ivim-round2-rescope` (`c3fdb53`) | **STRUCTURE survives, magnitude undetectable** | V⁴ tree-vs-loop + isotropy-vs-birefringence parameter-free; Δφ~1.8e-12 rad → 7.6 yr to SNR=1, apparatus field-emits first. Leaf re-scoped (Rule-12, strengthens 1.0→0.5). |
| **HOPF** | `analysis/2026-06-04-hopf-round2-chiral-counterfactual` (`d240d70`) | **C3/C4 RETIRE (form-shared); chirality PARTIAL** | Medium-indep + enantiomer-sign are reciprocal-Pasteur (own metamaterials ch:164: "circular birefringence Γ_L≠Γ_R"); only non-reciprocity (Tellegen) escapes, corpus pins it above-yield. Survivor: cheap 2-port S₂₁-vs-S₁₂ reciprocity sweep on existing HOPF-02a (not-yet-run, decisive). |

**THE THROUGHLINE (hard-confirmed by round-2):** the protocols that survive are exactly the ones whose
discriminator is a **SYMMETRY or SIGN at zero-free-parameter, NOT a magnitude.** Cleave SURVIVES on a
4-corner symmetry; Q-G42 on a sign. IVIM + HOPF-legs leaned on magnitude → deflated. The discriminating
question is *"does the protocol have a symmetry corner NO classical mechanism can fake?"* — Cleave: yes
(gap-independence, which CPD cannot fake); HOPF: only above-yield (non-reciprocity). Same throughline as the
2026-06-04 status answer (sign-tests + zero-free-param geometry survive the α-undecided).

**Flag-don't-fix queue (round-2 — NOT landed; auditor + Grant):**
- **Cleave F-R2-3 (corpus correctness):** round-1's *"SM predicts exactly 0.0 in vacuum-gap-only"* is FALSE —
  CPD (moving-Kelvin) gives ~21%-of-floor, polarity-ODD, same parity as the floor. Corrected locally in Femto
  TEST_PROCEDURE; KB leaf + AVE-Core Phase-3 prereg §4 need the CPD caveat (auditor to locate exact sites —
  orchestrator quick-grep did NOT surface the "0.0" phrasing in `project-cleave-01.md`).
- **Cleave F-R2-2 (recurring stale pointer):** XI_TOPO verified at `constants.py:251`; cited as `:246`
  (round-1 + occupation-robustness doc) and `:205` (which is actually ALPHA_COLD). Drifted 205→246→251 across
  versions → argues for CONTENT-anchored cites. Lockstep fix owed.
- **IVIM:** 8 corpus-wide per-node-conflation sites BLOCKED on Grant (2 known + 6 new) + index-convention
  discrepancy (δn≈−A²/4 vs Δn≈+A²/2, factor-2 + sign).
- **Q-G42:** `ch15-autoresonant-breakdown/theory.md` ⛔ INVALIDATED banner (wrong 60 kV); per-node reachability
  fork now carries verbatim both-camp evidence + FN-destruction corollary (BLOCKING per §10).

**Convergence:** the per-node-V_yield/apparatus conflation (§10 BLOCKING) is now **OVER-DETERMINED** — IVIM +
Q-G42 independently rooted their feasibility-kills in it. Grant's adjudication of the corpus-wide sweep is the
gating decision.

**Pending (sequenced):** (1) **auditor-gate** over the 4 round-2 branches; (2) round-2 **merge-calls** (Grant
go per branch); (3) **adjudications** — HOPF sugar-water-vs-ferrite physics call + cheap reciprocity-sweep add;
the per-node-conflation corpus sweep; Cleave SM≠0.0 propagation; XI_TOPO content-anchor lockstep fix;
round-1 sibling-branch cleanup.

**Adjudication ledger (Layer 2 — the *why* behind each decision):** the 5 round-2 adjudications are
tracked EE-mapped + skill-disciplined in [`experimental/2026-06-04_round2-adjudications.md`](experimental/2026-06-04_round2-adjudications.md)
— #1 HOPF reciprocity **AGREED** (reciprocal-Pasteur at linear; add reciprocity sweep); #2 Cleave CPD/SM≠0.0
SURFACED; #3–#5 queued.
