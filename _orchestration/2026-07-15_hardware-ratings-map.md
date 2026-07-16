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
| QED loops | **NOT lattice-native as built**: #707 — irreversible diffusion needs a sink the reversible engine lacks; #693 — spectator/pairwise medium gives WRONG-FORM for the loop-log. **Two separable results** (do not narrate as one fact). Peer QED = tree + ℏ-weighted loops; *whether ℏ is anything on the lattice* is **UNBANKED** (FORM of “ℏ = FD constant” was **not** derived; canonical AVE FDT is classical Nyquist / ℏ-free — `clm-eaiqj1`). Not a workstream. | ✅ #693 + #707 as separate receipts |

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
| R7 | **Thermal / noise floor** — the entropy sink | sink the thermometer/DE need; peer-label FD/Nyquist only after CHANNEL-BOUNDED | **REFUSED** as-built ✅ (#707) · rung-1 **CHANNEL-BOUNDED** ✅ · rung-2 **BIAS-MOVED** ✅ · Arm A **BIAS-MOVED** · Arm B G0 exterior-leave **BIAS-MOVED** (mode-count LIVE; sponge control OK) · frontier map chartered | BENCH-∅ | next hypothesis under mode-count discriminator (not Re(Z); not retune Arm A/B; not node mint); thermometer **GATED** |
| R8 | **Geometric floor** — ropelength `ℓ_node/2π` | smallest closed ring of refusal; ground-state incompressibility | **CONFIRMED** ✅ (census floor-pinned + lift-off rider; `envelope-anatomy.md`) | n/a (topological) | closed — no further spend |
| R9 | **Power-on transient** — the F6 window, w(z) | cosmological transition era; the only Λ-separable regime | chartered ✅ (F6 tier-1 ledger #674); needs a CHANNEL-BOUNDED in-Hamiltonian R7 door | real-machine = DESI/Euclid survey data | rides F6 field channel |
| R10 | **Overclocking (driven selection)** — census Stage-2 | does drive select (2,3)? the selection-principle gate | chartered ✅; cold leg incapable (#692); kernel-OFF = RECOMMENDED (#706); **F1 ★FIXED** (Grant DEFECT) | BENCH-∅ | census S2 driven — priority 4 (F1 hygiene cleared; R2 input still owed) |
| R11 | **The real varactor curve** — `C_eff(V)` of the actual vacuum | the first true datasheet row of the machine itself | model-side spec'd ✅ (CVR requirements #667 + trade-study v2 #687) | **BENCH-∅ — nothing measured, ever** | **CVR selection session** (Grant + collaborator) — priority 5, elevated; the only real-machine probe; r_knee consumer + strain-fork empirical test ride the gap-design |
| R12 | **Gap-independence (Cleave-01)** — the femto-electrometer kill-test | chord = gap-INDEPENDENCE, not the slope echo | spec'd ✅ (cite-don't-duplicate) | BENCH-∅ | queued behind R11's session |

## §3 — Missing spec pages (build, don't probe)

1. **F6 ε→T2 irreversible *field* channel** — Priority 1. Rung-1 ✅; rung-2 **BIAS-MOVED**; Arm A **BIAS-MOVED**; Arm B G0 exterior-leave **BIAS-MOVED** (`2026-07-16_f6-arm-b-exterior-leave_*` — exterior mode-count LIVE, bias knife kills, sponge control OK; do not retune). Map: [`../research/2026-07-16_f6-frontier-map_CHARTER.md`](../research/2026-07-16_f6-frontier-map_CHARTER.md). Next under [`../research/2026-07-15_f6-mode-count-door_CHARTER.md`](../research/2026-07-15_f6-mode-count-door_CHARTER.md): new hypothesis class ≠ face-port leave / ≠ interior snip; **forbid** Re(Z) absorb / Arm A·B retune / orthogonal bake-in / fake node mint.
2. **The loop ledger** (QED-TRACE charter extension) — charter-only; serialization sentence pending Grant; **not** driven by unbanked ℏ=FD.
3. **T_ij stress register** — build per repaired #688 charter.
4. **F1** — ★FIXED; consumer audit landed (`2026-07-15_f1-consumer-audit.md`); top-3 cheap re-runs queued.

## §4 — Demotions (explicit, so nothing drifts back)

Further echo-classification and consistency polishing (the API is verified); the Re/Im carve (software-language question — parked); standalone r_knee-consumer work (folded into R11's gap design); additional cold-linear census work (scope theorem closed it); walk-level unification prose without a rating attached; **in-Hamiltonian global V scale-down as F6 door** (rung-2 BIAS-MOVED); **event-gated local V + multi-mode credit as F6 door** (Arm A BIAS-MOVED — mode-count LIVE); **G0 face-port exterior leave as F6 door** (Arm B BIAS-MOVED — exterior mode-count LIVE); **ℏ = lattice FD constant as workstream** (FORM not derived; unbanked); **pre-naming matched-termination Re(Z) absorb as the next F6 door** (Ax3 retirement knife — Grant 2026-07-15); **assuming orthogonal / normal-to-surface latent release as derived** (conjecture — map charter G0–G3); **full N→N+1 frontier mint on current engines** (node_creation absent — map NO).

## §5 — Standing Grant queue (remaining)

Op4 scope ruling (pairwise-only label) · two vetoable adjudications (two-tank criterion; blob scoping) · serialization-sentence ratification · entropy-def stays PROPOSED (gated) · criterion/contour-tag sweep (ratified, queued) · F1 top-3 cheap re-runs (consumer audit).

**Board-clearing packages:**
- F1 ★FIXED + [`2026-07-15_f1-consumer-audit.md`](2026-07-15_f1-consumer-audit.md)
- F6 charter + rung-1/rung-2 + mode-count door charter + [`../research/2026-07-15_thermometer-refire_prereg_GATED.md`](../research/2026-07-15_thermometer-refire_prereg_GATED.md)

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
