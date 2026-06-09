# Ion-compression-cycle → asymmetric-grip rectifier arc — orchestration + documentation-homing plan

**Date:** 2026-06-09 · **Status:** ACTIVE · **Owner:** orchestration session (Grant direct)
**Directive (Grant 2026-06-09):** *"make sure we are planning to document this work in the proper places as we go."* This doc is the tracker + the as-we-go documentation-homing map for the arc.

> Per the 2026-06-05 workflow rule, this `_orchestration/` doc is itself PR-gated (lands on `main` via the arc's reviewed PR, with a pointer added to `index.md` at merge). Cross-repo items (Propulsion leaf, AVE-Skills mirror) are **separate-session** per the cross-repo-session-scope rule.

---

## 1. The arc (one paragraph)

Grant's "ion closed-loop compression cycle" tangent → dark-wake reaction-thrust (Phases 1–5, all B) → **reframed as a wrong-regime artifact** (sub-yield-linear shear/chiral = achromatic+reversible = ∮=0 by construction; the `ave-regime-phase-state-check` skill) → the temporal-saturation mode taxonomy (**shear/bulk/EM**, K=2G, the temporal-values doc) → **thixotropy bulk-mode check = B in the *right* regime** (it measured the substrate's lossy loop `∮S dρ̄=+0.04` but found it directionless) → the **ground-up asymmetric-grip rectifier design** (the heat-pump: lossy working fluid + biased diode + ledger; the `ave-asymmetric-grip` skill, "no ideal"). Parallel: the **Vol-9 datasheet figure program** (survey done; ρ̄_cav gap-fill registered).

## 2. Artifact inventory (by branch — none merged)

| branch (worktree) | artifacts | commits |
|---|---|---|
| `analysis/2026-06-09-saturation-temporal-preregs` (sattemporal-wt) | thixotropy prereg, time-dilation prereg, **temporal-values definition**, **ground-up rectifier design**, THIS epic doc | 52dbb215, a2d9eeef, fe530a36, 76cd1b74, 151ec9be, e8a07e92 |
| `analysis/2026-06-09-thixotropy-bulk-derivation` (thixo-wt) | thixotropy **result (B, structural)** + driver | eac96a0e |
| `analysis/2026-06-09-vol9-datasheet-figures` (vol9fig-wt) | datasheet figure work-list + survey JSON + **ρ̄_cav** registration | 9786dbe5 |
| `~/.claude/skills/` (not in repo) | **ave-engineering-program-rigor, ave-regime-phase-state-check, ave-asymmetric-grip** | — |
| memory/ | feedback_regime_phase_state_discipline, feedback_vacuum_engineer_not_gr_priors, project_ave_propulsion updates | — |

## 3. DOCUMENTATION-HOMING PLAN (the as-we-go map)

| artifact | current | proper canonical home | gate / session |
|---|---|---|---|
| thixotropy + time-dilation **preregs** | research/ (sattemporal) | stay in `research/` (frozen preregs — that IS their home) | none (research-grade) |
| thixotropy **result** (B, structural) | research/ (thixo, eac96a0e) | `research/` + a KB annotation on the `#59:77` seam (*"amplitude-dependent τ_bulk(ρ̄) derived 2026-06-09; instantaneous-ρ̄ only, no rectification"*) + closure-roadmap row (the clm-7tynm2 structural upgrade) | **PR-gated** (Core main); thixo branch → PR |
| thixotropy **figures** | /tmp (rendered) | thixo branch `research/assets/` + add `savefig` to the driver (closes the `ave-engineering-program-rigor` gap) | **fold into thixo branch** (now un-blocked — its run is committed) |
| **temporal-values definition** (shear/bulk/EM, voxel=gear) | research/ (sattemporal) | **KB leaf** (common/ or vol1) + **reconcile the 3 contradicting clock-exponent leaves** (op14-local-clock-modulation bare-S, Sleep-Pod c_EM, INVARIANT-S2 c_shear) | **PR-gated walk-back** (Core main) — corpus-coherence fix |
| **ρ̄_cav** = −1/φ (bulk cavitation floor) | datasheet branch (registered) + thixotropy result | datasheet **ch.02** (abs-max ratings, rarefaction-side) + **ch.14** (the c_eff²(ρ̄) figure) + candidate `claim-quality` entry + `constants.py` | datasheet PR (Core); the Propulsion-leaf canonization = **separate session** |
| **ground-up rectifier design** | research/ (sattemporal) | stays `research/` now; → **Vol 4 VCA** chapter *when validated* | PR-gated when validated (not before) |
| datasheet **figure work-list + survey** | datasheet branch | the figure-build executes against it; figures → **Vol 9** (extends the 2026-05-28 datasheet epic) | datasheet PR (Core) |
| 3 new **skills** | ~/.claude/skills | **mirror to AVE-Skills** repo | **separate session** (cross-repo) |
| regime + vacuum-engineer **feedback memory** | memory/ | done ✓ | none |
| **clm-7tynm2 walk-back** | queued | closure-roadmap + ~8 KB leaves (retire exotic-thrust, keep inertia-as-mass + radiation-pressure) | **HELD** (Grant); now *structurally earned* by the right-regime B; PR-gated |

## 4. Open decisions (Grant's calls)
- **PRs #144 (dark-wake), #145 (hysteresis), #2 (Propulsion brief)** — HELD ("lets wait"). #144 title is stale (says Phase 1–2); needs the full-arc + wrong-regime-caveat rewrite when un-held.
- **clm-7tynm2 walk-back** — HELD; basis upgraded from empirical to structural (right-regime B). Retire scope: exotic thrust / "inertial drive" (reactionless); KEEP inertia-as-mass + mundane radiation pressure.
- **Rectifier Stage-1** — next test (biased leaky diode + AC pump + ledger), pending Grant's gut-check on the physical fork (directed momentum vs re-radiated heat).
- **ρ̄_cav → claim?** — promote to a canonical claim (Grant "lets raise p-cav") via the datasheet + the feedback-fixed-point derivation; cross-volume canonization separate-session.

## 5. The as-we-go discipline (standing, this arc)
1. Every new result/design/prereg doc carries a **"documentation home"** line at creation (where it ultimately lands + the gate). The ground-up design doc's §7 + this table satisfy it going forward.
2. **KB / manuscript / matrix / claim-quality / constants.py landings are PR-gated** (Core main protected) — never direct.
3. **Cross-repo** (Propulsion leaf, AVE-Skills mirror) = **separate session**; tracked here + in the promotions-tracker, not executed inline.
4. **Nulls carry their regime label** (`ave-regime-phase-state-check`) before they justify any walk-back.
5. On any arc PR merge: add a one-line pointer to this epic from `index.md`, and log the closure-roadmap row.

## 6. Progress log (2026-06-09)
- **Thixotropy rigor-gap CLOSED** — `savefig` + 4-panel Outcome-B figure folded into the thixo branch (`5969bda1`); the result doc embeds it. (Was the one stranded artifact; now homed.)
- **Rectifier Stage-1 prereg FROZEN** — [`2026-06-09_rectifier-stage1-biased-diode_prereg.md`](../research/2026-06-09_rectifier-stage1-biased-diode_prereg.md): single DC-biased leaky varactor diode + AC pump + (V,Q) loop + ledger + mandatory bias sweep. Binds ave-asymmetric-grip + ave-regime-phase-state-check + ave-engineering-program-rigor.
- **Rectifier Stage-1 RAN → OUTCOME C** (branch `analysis/2026-06-09-rectifier-stage1-biased-diode` @ b8e6b022, NOT pushed): the biased leaky diode **IS a real rectifier** (directed fraction 1.9%, **robust** across the near-yield bias band, not over-unity, lossless-guard passes) — **but the induced lens is CHROMATIC plasma** (n<1, deflection ∝λ²), **NOT** achromatic gravity. **Engineered-gravity chord FALSIFIED at Stage 1.** Load-bearing constraint: **rectify ⇔ Z≠Z₀ (asymmetric); achromatic-gravity ⇔ Z=Z₀ (symmetric); ONE element can't be both.**
- **CORRECTION (flag against own prior claims):** the "one device, four observables" unification (rectifier-design §7, prereg §6a) is **FALSIFIED** — thrust (asymmetric/plasma) and gravity/lens/time-dilation (symmetric/achromatic) are **different symmetry branches**. Corrected in design-doc §7 (caveat box) + emergence-note §2 (the electron rides the SYMMETRIC/gravity branch; the diode is the separate plasma branch).
- **Auditor flag (Stage-1 surfaced, neither doc edited):** the thixotropy result headlines closing the thrust space "by derivation" via a **bias-independent parity** argument; Stage-1 shows that with the asymmetric diode + bias the loop **does** acquire a direction → the thrust space stays closed but **by chromaticity** (it's mundane plasma, not AVE-distinct), **not by parity**. Auditor adjudicates the scope on the thixo branch.
- **Carry-forward:** (i) is the **symmetric** (achromatic, no-reaction-thrust) engineered-gravity device a *separate* design — the warp/Sleep-Pod metric-gradient regime — distinct from the plasma thruster? (ii) a cascade/taper would have to separate an asymmetric rectifier stage from a symmetric lensing stage (mutually exclusive per element). (iii) **Electron-emergence note landed** — [`2026-06-09_electron-emergence-self-focusing-tracereversal-picture.md`](../research/2026-06-09_electron-emergence-self-focusing-tracereversal-picture.md): self-focusing photon → generates its own saturated regime → trace-reversal → (2,3); prior-art check pins the L3 gap to the **K4↔Cosserat (Op14/trace-reversal) coupling weakness** (A²_μ=0.012, A28 bug, v14-deferred) — a re-attack on a known weak link, not untried. L3-thread, likely a dedicated session.
