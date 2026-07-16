# The Hardware Ratings Map — the program reorganized as the vacuum's datasheet

**Date:** 2026-07-15 · **Status:** PROGRAM MAP / tracker (orchestration doc, not a claim). Supersedes the priority ordering of `_orchestration/2026-07-14_batch-outcomes-and-actions.md` §3 (that board's ledger content stands). · **Anchor-verification status:** ✅ **SWEEP LANDED 2026-07-15** (branch `docs/2026-07-15-hardware-ratings-anchor-sweep`) — full two-method pass over every §1–§5 receipt; FAIL/WEAK wording repaired in-place below; external tracker staleness (docket Entry 15; batch-board #689/#692/#693 OPEN rows) flipped in companion appends. Receipt table: §6.

## Charter framing (Grant, in-chat 2026-07-15, verbatim-faithful)

> *"Modern physics has wonderfully described the software of the universe, but software needs to understand the mechanical limitations of the machine running it. That's what AVE is searching for."*

**The operating rule this imposes:** every probe is IN-SPEC (returns the software's answers — consistency, echoes, peer-with-SM; the two-day arc confirmed the abstraction holds, ~11 independent ways) or AT-THE-RAILS (a hardware fingerprint). **The program no longer spends on in-spec consistency.** Every new lane drives a rating or writes a missing spec page. Engine drives test the *model's* hardware; only the bench touches the *actual* machine — engine rail-tests exist to sharpen bench predictions.

## §1 — The verified API (the software limits AVE derives; in-spec, closed, no further spend)

| Limit | AVE status | Session receipt |
|---|---|---|
| GR (continuum/adiabatic limit) | DERIVED projection: clock `√S` (Ruling 1), graded-index network, deflection doubling; Komar self-consistency = X44b (chartered, PR #688) | ✅ docket Rulings 1/11; `backreaction.py` `komar_weight` |
| ΛCDM (late-time limit) | The F6 drain converges onto Λ past τ₀; AVE-distinct content confined to the transition window w(z) | ✅ F6 tier-1 two-limits map (merged #674 arc) |
| QED tree level | Lattice-native diagrammatics (MSR/Wyld class): propagator = lattice Green's fn; vertices = kernel Taylor coefficients; Op4 dress = tree; transfer register = QED-faithful (`register_flip` demonstrated); anti-screening sign reproduced | ✅ #685 beta gate + #693 screening gate + the serialization framing (UNRATIFIED — pending Grant, queued) |
| QED loops | **NOT lattice-native as built**: loops need fluctuations; the reversible engine has none. QED = tree + ℏ-weighted loop calculus ⇒ the AVE question = *is ℏ the lattice's fluctuation-dissipation constant?* (derive-or-import; FORM/VALUE law, candidate 5th instance) | ✅ #693 (spectator medium) + #707 (no diffusion without sink) — one fact, two measurements |

## §2 — THE RATINGS TABLE (the hardware rows; the strategy = fill the status columns)

Status legend: **MEASURED-STATIC** · **DRIVEN** (dynamically exercised) · **IMPOSED-ONLY** (used as BC, never formed by drive) · **REFUSED** (the machine said no — itself a datasheet entry) · **UNRUN** · **BENCH-∅** (real machine untouched).

| # | Rating | Physical meaning | Model status | Real-machine status | Next drive |
|---|---|---|---|---|---|
| R1 | **Proportional limit (the knee)** — `A²=2α`, `ΔS=α` | onset of response departure; dress outer envelope | **MEASURED-STATIC** ✅ (`r_knee=(2α)^{-1/4}=2.877 ℓ_node` near-identity with `r99` outer envelope, ratio 1.06–1.27; PR #696 verdict **PARTIAL** vs primary `r90`) — never driven *through* | BENCH-∅ | dynamic knee-crossing drive (watch the response bend); rides the two-tone suite (R6) |
| R2 | **The rail (the wall)** — `S→0`, `\|Γ\|=1` | storage exhaustion; the mirror; carries M/Q/J | **IMPOSED-ONLY** ✅ (census amplitude-clamp BC; Wall-A anatomy, Ruling 6; `envelope-anatomy.md`) — never *formed by drive* | BENCH-∅ | drive a region to refusal and watch the wall form (feeds census S2 design) |
| R3 | **★ Absolute maximum (snap)** — `V_snap = m_ec²/e`; rectification past it | breakdown; pair production as vacuum avalanche (AC→DC winding; FPB walk + Miller row) | **UNRUN** — the most hardware-shaped test the program owns has never been run in-engine (only a static `V_SNAP` identity pin exists) | BENCH-∅ (Schwinger-scale; model-first) | **THE DESTRUCTIVE TEST** (new charter): drive one cell past snap; watch for rectification. Priority 2 |
| R4 | **Clock derating** — `ω = ω₀√S` under load | timing closure vs strain | point-confirmed ✅ (op14 `(1−2α)^{1/4}`, PR #690 hygiene land) — **curve never traced** | BENCH-∅ | sweep the derating curve (cheap; rides R1/R6 drives) |
| R5 | **Slew limit (FPB corner)** — `A_I = Ė/(E_cω₀)` | max drive rate; six markers span a ~half-decade ~MeV band (not a coincident point; PR #595 + #604 caveat) | **UNRUN** (framed only; PR #595 walk) | BENCH-∅ | FPB slew / crossover-band map — **REVIVED** (board task #34 is D-IV nucleation-capture only; do not cite phantom D-III) |
| R6 | **Clipping harmonics** — χ³ four-wave mixing | saturation nonlinearity products | derived ✅ (χ³ srs arc); two-tone protocol designed, **parked** (`superband-carrier-fork_result` FORK A) | BENCH-∅ | two-tone mixer + phase-slip capture — **REVIVED** (= the AC ratings section; not a task-#34 D-II/D-IV sublabel — those roman labels are `[RECEIPT-PENDING]` / unlocatable) |
| R7 | **Thermal / noise floor** — the entropy sink | fluctuation-dissipation; loops; thermometer | **REFUSED** as-built ✅ (#707) · **first-rung CHANNEL-BOUNDED** ✅ (parallel latent→bath on live lattice, 2026-07-15) — in-Hamiltonian ε depletion still UNRUN | BENCH-∅ | deeper F6 field-depletion rung; then thermometer re-fire |
| R8 | **Geometric floor** — ropelength `ℓ_node/2π` | smallest closed ring of refusal; ground-state incompressibility | **CONFIRMED** ✅ (census floor-pinned + lift-off rider; `envelope-anatomy.md`) | n/a (topological) | closed — no further spend |
| R9 | **Power-on transient** — the F6 window, w(z) | cosmological transition era; the only Λ-separable regime | chartered ✅ (F6 tier-1 ledger #674); needs the R7 *field* channel (tier-1 ODE ≠ the missing irreversibility) | real-machine = DESI/Euclid survey data | rides F6 field channel |
| R10 | **Overclocking (driven selection)** — census Stage-2 | does drive select (2,3)? the selection-principle gate | chartered ✅; cold leg proven incapable (scope theorem, #692); kernel-OFF control = **RECOMMENDED-cheap** (blob MODE-SORTING, #706); **F1 ordering fix first** | BENCH-∅ | census S2 driven — priority 4 (after F1 adjudication + R2 input) |
| R11 | **The real varactor curve** — `C_eff(V)` of the actual vacuum | the first true datasheet row of the machine itself | model-side spec'd ✅ (CVR requirements #667 + trade-study v2 #687) | **BENCH-∅ — nothing measured, ever** | **CVR selection session** (Grant + collaborator) — priority 5, elevated; the only real-machine probe; r_knee consumer + strain-fork empirical test ride the gap-design |
| R12 | **Gap-independence (Cleave-01)** — the femto-electrometer kill-test | chord = gap-INDEPENDENCE, not the slope echo | spec'd ✅ (cite-don't-duplicate) | BENCH-∅ | queued behind R11's session |

## §3 — Missing spec pages (build, don't probe)

1. **F6 ε→T2 irreversible *field* channel** — the thermal section. Unlocks R7, R9, the loop ledger (§1), and possibly the log. **Priority 1.** (Distinct from the already-merged F6 tier-1 two-reservoir ODE ledger #674 — that books reservoirs; this is the missing engine irreversibility / fluctuation sink.)
2. **The loop ledger** (QED-TRACE charter extension): which diagram classes the lattice implements (tree ✅, ladder ✅-spectator, loops = await F6+noise); the ℏ-as-FD-constant question stated as a gate. Charter-only; includes ratifying the serialization sentence (pending Grant nod).
3. **T_ij stress register** — instrumentation, not a rating: serves gate-(b) (F3/F5/§45 values + knee radius), X44b, census S2, electron T_rr. Build per the repaired #688 charter.
4. **F1 ordering fix** (defect-candidate, Grant adjudication) + the V-active consumer audit — engine hygiene prerequisite for R10.

## §4 — Demotions (explicit, so nothing drifts back)

Further echo-classification and consistency polishing (the API is verified); the Re/Im carve (software-language question — parked); standalone r_knee-consumer work (folded into R11's gap design); additional cold-linear census work (scope theorem closed it); walk-level unification prose without a rating attached.

## §5 — Standing Grant queue (unchanged, carried from the docket next-steps register)

F1 adjudication + consumer-audit call · Op4 scope ruling (pairwise-only label) · two vetoable adjudications (two-tank criterion; blob scoping) · serialization-sentence ratification · entropy-def stays PROPOSED (gated) · criterion/contour-tag sweep (ratified, queued).

**Board-clearing packages landed this sweep (await Grant word):**
- F1 package → [`_orchestration/2026-07-15_f1-adjudication-package.md`](2026-07-15_f1-adjudication-package.md)
- F6 field-channel charter (≠ tier-1 ledger) → [`../research/2026-07-15_f6-field-channel_CHARTER.md`](../research/2026-07-15_f6-field-channel_CHARTER.md)

## §6 — Anchor-verification receipt (2026-07-15 sweep)

Two-method pass (gh PR state + `rg`/`git grep` content). Full adversarial table in session trail; durable summary:

| Class | Items |
|---|---|
| **PASS** | §1 GR/ΛCDM/QED-tree/loops receipts; R3 UNRUN absence; R4 op14 point; R8 floor; R9/#674; R10 #692+#706+F1; R11 CVR; R12 Cleave-01; #688 T_ij; §5 Grant queue (blob "vetoable" inferred) |
| **FAIL → repaired** | R5/R6 phantom "task #34 D-II/D-III/D-IV" labels (`program-arc-map.md` OF9 `[RECEIPT-PENDING]`); R5 "converge ~MeV" → half-decade band per #595/#604 caveat |
| **WEAK → tightened** | R1 `= r99` → near-identity / PARTIAL vs `r90`; R2 Ruling-11 stretch → Ruling 6 + amplitude-clamp BC; R7 cite `ADDITIVE-ARTIFACT` as source verdict; §3 "5 motivations" → docket's 2 + map extension; §4 "biquaternion" struck |
| **External STALE → flipped** | Docket Entry 15 "blob IN FLIGHT" (vs #706 MERGED); batch board #689/#692/#693 "OPEN" (all MERGED 2026-07-15) — companion appends this PR |

---
*Rule-of-the-map: a row leaves this table only by MEASURED/DRIVEN/REFUSED status with a receipt, or by Grant striking it. The strategy is the empty cells.*
