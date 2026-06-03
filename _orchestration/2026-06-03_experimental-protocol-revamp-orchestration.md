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
