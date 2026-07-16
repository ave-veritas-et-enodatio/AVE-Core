# The Hardware Ratings Map — the program reorganized as the vacuum's datasheet

**Date:** 2026-07-15 · **Status:** PROGRAM MAP / tracker (orchestration doc, not a claim). Supersedes the priority ordering of `_orchestration/2026-07-14_batch-outcomes-and-actions.md` §3 (that board's ledger content stands). · **Anchor-verification status:** rows marked ✅ were session-verified 2026-07-14/15 (the two-day arc, PRs #664–#707); the full two-method anchor sweep is the FIRST review gate on this doc (next session).

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
| R1 | **Proportional limit (the knee)** — `A²=2α`, `ΔS=α` | onset of response departure; dress outer envelope | **MEASURED-STATIC** ✅ (`r_knee=(2α)^{-1/4}=2.877 ℓ_node` = r99, PR #696; ratio 1.06–1.27) — never driven *through* | BENCH-∅ | dynamic knee-crossing drive (watch the response bend); rides the two-tone suite (R6) |
| R2 | **The rail (the wall)** — `S→0`, `\|Γ\|=1` | storage exhaustion; the mirror; carries M/Q/J | **IMPOSED-ONLY** ✅ (census clamps; Wall-A anatomy, Rulings 6/11; `envelope-anatomy.md`) — never *formed by drive* | BENCH-∅ | drive a region to refusal and watch the wall form (feeds census S2 design) |
| R3 | **★ Absolute maximum (snap)** — `V_snap = m_ec²/e`; rectification past it | breakdown; pair production as vacuum avalanche (AC→DC winding; FPB walk + Miller row) | **UNRUN** — the most hardware-shaped test the program owns has never been run in-engine | BENCH-∅ (Schwinger-scale; model-first) | **THE DESTRUCTIVE TEST** (new charter): drive one cell past snap; watch for rectification. Priority 2 |
| R4 | **Clock derating** — `ω = ω₀√S` under load | timing closure vs strain | point-confirmed ✅ (op14 `(1−2α)^{1/4}`, PR #690) — **curve never traced** | BENCH-∅ | sweep the derating curve (cheap; rides R1/R6 drives) |
| R5 | **Slew limit (FPB corner)** — `A_I = Ė/(E_cω₀)` | max drive rate; six markers converge ~MeV | **UNRUN** (framed only; PR #595 walk) | BENCH-∅ | task #34 D-III slew map — **REVIVED** |
| R6 | **Clipping harmonics** — χ³ four-wave mixing | saturation nonlinearity products | derived ✅ (χ³ srs arc); two-tone protocol designed, **parked** | BENCH-∅ | task #34 D-II mixer calibration + D-IV phase-slip capture — **REVIVED** (= the AC ratings section) |
| R7 | **Thermal / noise floor** — the entropy sink | fluctuation-dissipation; loops; thermometer | **REFUSED** ✅ (PR #707: athermal as-built; bounded reversible dephasing; Ax3 line *measured*) — the missing spec page is **F6 ε→T2** | BENCH-∅ | **F6 build** — priority 1 (5 motivations: DE, thermo, loops/ℏ, hygiene, this row) |
| R8 | **Geometric floor** — ropelength `ℓ_node/2π` | smallest closed ring of refusal; ground-state incompressibility | **CONFIRMED** ✅ (census floor test: settles-at-floor + lift-off rider) | n/a (topological) | closed — no further spend |
| R9 | **Power-on transient** — the F6 window, w(z) | cosmological transition era; the only Λ-separable regime | chartered ✅ (F6 tier-1); needs the R7 build | real-machine = DESI/Euclid survey data | rides F6 |
| R10 | **Overclocking (driven selection)** — census Stage-2 | does drive select (2,3)? the selection-principle gate | chartered ✅; cold leg proven incapable (scope theorem, #692); kernel-OFF control = recommended (blob verdict, #706); **F1 ordering fix first** | BENCH-∅ | census S2 driven — priority 4 (after F1 adjudication + R2 input) |
| R11 | **The real varactor curve** — `C_eff(V)` of the actual vacuum | the first true datasheet row of the machine itself | model-side spec'd ✅ (CVR requirements #667 + trade-study v2 #687) | **BENCH-∅ — nothing measured, ever** | **CVR selection session** (Grant + collaborator) — priority 5, elevated; the only real-machine probe; r_knee consumer + strain-fork empirical test ride the gap-design |
| R12 | **Gap-independence (Cleave-01)** — the femto-electrometer kill-test | chord = gap-INDEPENDENCE, not the slope echo | spec'd ✅ (cite-don't-duplicate) | BENCH-∅ | queued behind R11's session |

## §3 — Missing spec pages (build, don't probe)

1. **F6 ε→T2 irreversible channel** — the thermal section. Unlocks R7, R9, the loop ledger (§1), and possibly the log. **Priority 1.**
2. **The loop ledger** (QED-TRACE charter extension): which diagram classes the lattice implements (tree ✅, ladder ✅-spectator, loops = await F6+noise); the ℏ-as-FD-constant question stated as a gate. Charter-only next session; includes ratifying the serialization sentence (pending Grant nod).
3. **T_ij stress register** — instrumentation, not a rating: serves gate-(b) (F3/F5/§45 values + knee radius), X44b, census S2, electron T_rr. Build per the repaired #688 charter.
4. **F1 ordering fix** (defect-candidate, Grant adjudication) + the V-active consumer audit — engine hygiene prerequisite for R10.

## §4 — Demotions (explicit, so nothing drifts back)

Further echo-classification and consistency polishing (the API is verified); the Re/Im biquaternion carve (software-language question — parked); standalone r_knee-consumer work (folded into R11's gap design); additional cold-linear census work (scope theorem closed it); walk-level unification prose without a rating attached.

## §5 — Standing Grant queue (unchanged, carried from the docket next-steps register)

F1 adjudication + consumer-audit call · Op4 scope ruling (pairwise-only label) · two vetoable adjudications (two-tank criterion; blob scoping) · serialization-sentence ratification · entropy-def stays PROPOSED (gated) · criterion/contour-tag sweep (ratified, queued).

---
*Rule-of-the-map: a row leaves this table only by MEASURED/DRIVEN/REFUSED status with a receipt, or by Grant striking it. The strategy is the empty cells.*
