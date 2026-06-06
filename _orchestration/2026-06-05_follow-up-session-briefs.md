# Follow-up Session Briefs — post Gravity-Sector Arc (2026-06-05)

Spawn-ready briefs for each follow-up from the gravity-sector session. Companion to `2026-06-05_gravity-sector-session-handoff.md` (status/decisions). Each section is promotable to its own epic doc on activation. Grouped: **LANDING** (gated on Grant review/picks) · **CHORD-HUNTS** (new physics) · **FUTURE/LARGER**.

---

## LANDING (gated on Grant review/picks; small)

### L1 — Merge the 3 gravity PRs (orchestrator runbook)
- **Goal:** land #91 → #92 → #90 to `main`.
- **Gating:** Grant/coworker approves each PR diff.
- **Steps (per AVE-Core audit-tag+merge discipline), in order #91, #92, #90:** review diff → tag `audit/2026-06-05_<topic>` at branch tip → `gh pr merge --no-ff` → push tag → delete branch (local+remote) after tag verifies on origin. **Order is load-bearing:** #91/#92 carry the result docs #90's walk-backs cite; merging #90 first → dangling citations (verify-md-links fail).
- **After:** update `_orchestration/index.md` to log the arc closure (tracked edit, fold into a trailing commit).
- **Skills:** verify-before-cite (confirm #90's basis-citations resolve once #91/#92 are on main), ave-evidence-framing.
- **Return:** 3 merges + 3 audit tags on origin + branches deleted + index.md updated.

### L2 — Foreword (b) surgical overclaim fixes (implementor)
- **Goal:** align the foreword's *bold lead* with its *own fine-print concessions* — surgical, no new claims.
- **Gating:** Grant picks the set from {b-i, b-ii, b-iii} (flagship headline claims = his call). EE-vs-ME fix is a confirmed **no-op** (already canonical).
- **Branch:** `analysis/foreword-b-surgical` off `origin/main`; PR; do NOT merge.
- **Scope (whichever Grant picks):** **b-i** the 3 "positive load-bearing empirical **confirmation** at scale" → "**consistency** at scale" (per INVARIANT-S9: public-catalog re-analyses aren't `exp-`). **b-ii** ρ_Λ "×1.5 vs 10¹²²" scoreboard → latent-heat conceptual reframe (drop input-consistency-vs-mode-sum mismatch). **b-iii** title/lede "Zero-Parameter" → carry the "target" caveat.
- **Skills:** ave-evidence-framing-discipline (core), verify-before-cite, Pure-AVE-corpus.
- **Return:** branch + PR; per-edit summary; confirm only register-alignment (no fine-print honesty removed, no new claims).

### L3 — Temporal-sector coherence cleanup (auditor/implementor)
- **Goal:** resolve the 3 W2-propagation items the walk-back passes surfaced (flag-don't-fix).
- **Items:** (a) `common/claim-quality.md` + `vol3/claim-quality.md:45` "temporal-only n → only the Newtonian half-deflection" sub-claim (tangles with W1's n_⊥=(2/7) finding); (b) `vol3/claim-quality.md:48` Pitfall #3 (same cluster); (c) `white-dwarf-gravitational-predictions.md:44` local-clock slope-2 vs `:51` resultbox slope-1 internal inconsistency.
- **These are DERIVATION-LEVEL, not relabels.** Apply the W2 ruling (local clock=√S slope-1; bulk index=slope-2; light deflection=(2/7) transverse, NOT n_spatial/n_temporal). The half-deflection sub-claim needs re-derivation against the (2/7):(1/7) Poisson result — `ave-audit-of-audit` before editing (don't mechanical-swap a derivation claim).
- **Gating:** after #90 merged (builds on W1/W2). **Branch:** `analysis/temporal-coherence-cleanup` off post-#90 main; PR.
- **Skills:** ave-walk-back, consistency-vs-emergence, ave-audit-of-audit, verify-before-cite.
- **Return:** 3 items resolved-or-surfaced (escalate any half-deflection reconciliation that needs Grant); PR.

---

## CHORD-HUNTS (new physics — north-star: discriminating test, not more polishing)

### C1 — Cosmic-rotation knee: alignment ∝ moment-of-inertia, Reynolds-style threshold *(my recommended next)*
- **Goal:** the one genuinely-novel prediction this session surfaced — cosmic-axis-alignment strength scales with object moment-of-inertia / knot-content (the soliton-lattice-coupling-operator's missing functional form, coupling ∝ I_s), with a Reynolds-style **knee** (critical coupling-number Q·δ ~ crit). **Testable against existing data.**
- **Phases:** (0) ave-prereg corpus-grep (soliton-lattice-coupling-operator.md, omega-freeze-cosmic-grain-cascade, SDSS DR17 spin result, `project_cosmic_rotation_soliton_coupling_thread` memory). (1) derive the coupling-number from the operator building-blocks (Op14 frame-drag asymmetry + J=Ω·I boundary observable + Q=α⁻¹) → the I_s / knot-content scaling. (2) the knee = critical dimensionless ratio (Q·δ, Reynolds-analog). (3) **data test:** SDSS DR17 / Shamir galaxy spin-axis alignment vs galaxy mass/I — does alignment-strength scale with I and show a knee? (4) `ave-discrimination-check` — is this AVE-distinct vs Bianchi-anisotropy / MOND / isotropic-ΛCDM? (the discriminating-test bar).
- **Skills:** ave-prereg, ave-canonical-leaf-pull (operator building-blocks), substrate-native-check, consistency-vs-emergence, **ave-discrimination-check (critical — the whole point is distinctness)**, verify-before-cite.
- **Gating:** none (independent research). **Return:** prereg + derivation + data-test + discrimination verdict (real-chord-or-echo).

### C2 — L3 dynamical self-lock: the α exact-value lift (research epic — SCOPING first)
- **Goal:** the deepest chord — does the full nonlinear + chiral-Cosserat bound-state engine **autonomously** reach R·r=1/4 / the K=2G magic angle that fixes α's *exact* value (not just the ~1/137 scale)? Only path to lift α from Class-B → first-principles.
- **Reality:** this is the UNSOLVED bound-state problem. Static routes CLOSED-NEGATIVE (2026-06-04 bijection result; L3 archive = 129 docs). HARD, open-ended, multi-week — NOT a clean session.
- **First deliverable = SCOPING ONLY:** what's been tried (L3 static-route negatives), what the dynamical path needs (Master Equation FDTD breathing-soliton at finer grid + chiral Cosserat back-coupling — the foreword's "finer-grid convergence study" open note + Q-G47 Sessions 19+), the PASS criterion (engine autonomously settles at R·r=1/4 / K=2G without injecting α), realistic effort.
- **Skills:** ave-prereg, substrate-native-check (Checkpoint 8: seed generative precursor, let dynamics build), ave-fundamental-ground-up-implementation, ave-canonical-leaf-pull, consistency-vs-emergence.
- **Gating:** research-capacity decision (big lift — scope before committing). **Return:** scoping doc (prereqs, convergence path, effort, go/no-go).

---

## FUTURE / LARGER

### F1 — Foreword register-inversion (a): full honesty pass (manuscript)
- **Goal:** the FULL register-inversion (bold-leads → honest-scope-leads) — the (a) option beyond (b)'s surgical subset. Draft exists: `research/2026-06-05_foreword-register-inversion-draft.md`.
- **IMPORTANT:** the draft predates this session's gravity findings — **update its gravity section first** (light-doubling = Poisson-derived not hand-set; perihelion-3 still hand-set; sign settled; (9/7) relabel) before applying.
- **Gating:** Grant's go (flagship, big editorial commitment); likely AFTER L1+L2. **Branch:** `analysis/foreword-register-inversion` off main; PR (heavy review).
- **Skills:** ave-evidence-framing-discipline (core), verify-before-cite, consistency-vs-emergence, Pure-AVE-corpus.
- **Return:** branch + PR; section-by-section inverted foreword.

### F2 — Vacuum-mirror E+B+AC complementary bench (CROSS-REPO: AVE-Bench-VacuumMirror)
- **Goal:** the symmetric-kernel / transmission test complementary to the E-only asymmetric reflection bench — drive BOTH E and B (symmetric loading) + AC on both → probe the *universal symmetric* kernel via transmitted-phase parametric modulation (the gravity-analog at bench scale; the E-only reflection bench is structurally blind to it).
- **Physics basis READY** (this session): static-E = asymmetric (Op14 Meissner, reflection); symmetric (both sectors) = Z-invariant (transmission, no reflection). The complementary bench probes the symmetric corner.
- **CROSS-REPO** — per cross-repo-session-scope, a SEPARATE AVE-Bench-VacuumMirror session; track via promotions-tracker, do NOT start in AVE-Core.
- **Scope (for the bench session):** E+B-bias + AC-on-both protocol; feasibility (per-node A₀ ~ 4e-5 at bench fields → probes leading kernel curvature in the symmetric/transmission channel); the QED discriminator.
- **Skills:** ave-ee-first-mapping, ave-prereg, ave-discrimination-check, substrate-native-check.
- **Return:** bench-design brief for the AVE-Bench session.

---

## Suggested activation order
LANDING (L1 → L2 → L3) clears the deck. Then ONE chord-hunt — **C1 (cosmic-rotation knee)** is the cheapest real discriminating test (existing data); **C2 (L3 self-lock)** is the deepest but a hard epic (scope only). F1/F2 are larger/cross-repo, later. Atomic Grant actions (not briefs): merge approvals, git reset.
