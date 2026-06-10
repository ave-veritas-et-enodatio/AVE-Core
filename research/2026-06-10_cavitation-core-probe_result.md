# RESULT — Cavitation-core probe: a self-circulating core REACHES + CROSSES ρ̄_cav=−1/φ, but the event is LOCK (reversible compliance), not FLASH

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-cavitation-core-probe` (worktree off `origin/main`; not pushed/merged)
**Prereg (frozen):** [`2026-06-10_cavitation-core-probe_prereg.md`](2026-06-10_cavitation-core-probe_prereg.md)
**Engine (new branch):** [`src/ave/core/cavitation_flow.py`](../src/ave/core/cavitation_flow.py) — `CavitationFlow2D`, the rarefaction-stiffness bulk-flow branch
**Driver:** [`src/scripts/vol_4_engineering/cavitation_core_probe.py`](../src/scripts/vol_4_engineering/cavitation_core_probe.py) · figures [`…_figures.py`](../src/scripts/vol_4_engineering/cavitation_core_probe_figures.py)
**Data:** `src/scripts/vol_4_engineering/_output/cavitation_core_probe_results.json`
**Governing discipline:** `ave-apparatus-floor-attribution` (FLASH-physics vs CLIP-apparatus). Skills: substrate-native-check, ave-prereg, ave-canonical-source, ave-conserved-vs-pumped, ave-regime-phase-state-check, phase-space-coordinate-check, ave-driver-script-honesty, verify-before-cite.

---

## 0. VERDICT — **LOCK** (with a clip-cleared floor-crossing)

> 🔴 **SUPERSEDED — 2026-06-10 PANEL REVIEW (Rule 12 / A47 v11b: header added, body below preserved verbatim — NOT rewritten). The standing verdict is now CLIP, not LOCK; this LOCK is DEMOTED. Read §0-bis (PANEL VERDICT ADDENDUM, immediately below this section) for the final verdict and its driver. Do not cite the §0 LOCK body as the standing result.**

> **A genuinely circulating bulk-density core, rarefied by its OWN rotation (centrifugal pressure deficit), REACHES and CROSSES the candidate cavitation floor `ρ̄_cav = −1/φ ≈ −0.618` at a critical drive `M_edge* ≈ 0.75–0.8` — decisively beating the prior-art counter-propagating-beam floor of −0.26. The bulk stiffness collapses through zero into the tensile-failure region (`c_bulk²_core` goes from +0.25 at M=0.7 to −0.86, −2.78, −5.53 at M=0.8, 0.9, 1.0). BUT the three discriminating FLASH signatures are all NEGATIVE: (ii) the energy partition is SMOOTH across the crossing (no latent-release discontinuity); (iii) `pocket_cells_final = 0` (no persistent tensile-failure defect); (iv) on de-energize the core REFILLS (−0.93 → −0.07; reversible). The core RINGS and REBOUNDS — bounded oscillation, not runaway. That is the prereg's LOCK bin: pocket-COMPLIANCE, not a discontinuous phase-change. At over-drive (`M_edge ≥ 1.1`) the deepest reading pins at the apparatus clip `rho_floor = −0.95` (CLIP regime — flagged as apparatus, not physics).**

**One-line FLASH/LOCK/CLIP/NO-REACH tally:** reach = YES (not NO-REACH); discontinuity = NO; persistence/hysteresis = NO (reversible); over-drive depth = CLIP. → **LOCK** for the physical drive band `M_edge ∈ [0.8, 1.0]`; CLIP for `M_edge ≥ 1.1`.

This is reported as the discipline at full strength (Rule 11): **the data were NOT debugged toward FLASH.** The floor-crossing is real and clip-cleared; the irreversibility/latent-heat signatures a FLASH requires are simply absent in the canonical rarefaction-stiffness EOS.

---

## 0-bis. PANEL VERDICT ADDENDUM — 2026-06-10 (cavitation-core-probe adversarial review)

**Final verdict: CLIP.** The §0 LOCK verdict is **DEMOTED** (preserved verbatim above per Rule 12 / A47 v11b; this addendum supersedes it, it is not rewritten). Panel two-lens disposition **converges on a single root defect**: **Lens-1 (LOCK-as-a-physics-event) is REFUTED** (= true; the LOCK verdict does not survive); **Lens-2 returns WARN, with finding F5 converging on the same defect** named in (a) below.

### (a) The demotion driver — the dynamics never integrated `c²<0`

The momentum RHS ran on the **FLOORED** wave speed `c_eff² = max(c_bulk²_raw, +1e-3·c₀²)` (`src/ave/core/cavitation_flow.py:159–163`, `c_bulk2()` with default `c2_floor=1e-3`; consumed in the RHS at `:180`, `c2 = self.c_bulk2(rho)`). The floor is strictly **positive**. The negative readings headlined in §0 as load-bearing — `c_bulk²_core = −0.86 / −2.78 / −5.53` at M = 0.8/0.9/1.0 — are `c_bulk2_raw` **DIAGNOSTIC** values only (`:155–157`; the run-JSON `c2_core_raw` series). They were **never integrated.** The floor fired hard, in exactly the LOCK band: `clip_c2_hits = 42,788 / 267,236 / 676,336` interior cell-steps at M = 0.8/0.9/1.0 (run-JSON `C_probe.rows`).

A strictly-positive `c²` can produce **only reversible compliance** — a stiff/soft acoustic medium that rings and rebounds — and is mathematically incapable of a tensile runaway. **FLASH was therefore excluded BY CONSTRUCTION, not by evidence.** The de-spin "recovery" (`rc_deepest −0.927 → rc_final −0.068` at M=1.0; `E_hysteresis`) and `pocket_cells_final = 0` are **scheme-pre-determined consequences of the positive floor**, not discriminating measurements. Decisively: **reversibility was never swept over `c2_floor`** — `E_hysteresis` ran at the default floor only — so the one knob that could expose the defect was held fixed in the only test that mattered.

### (b) WHAT SURVIVES (load-bearing positive — the reach/crossing)

The CLIP demotion does **not** touch the reach result, which is clip-invariant and stands:

- A genuinely circulating core (solid-body column, vorticity `ζ = 2Ω`; the density deficit **emerges dynamically via continuity**, CP9, not the algebraic centrifugal formula; angular momentum **energized + locked**, free-drift floor **0.044%**) **crosses** the candidate floor `ρ̄_cav = −1/φ ≈ −0.618` at `M_edge* ≈ 0.75–0.8` and **reaches ≈ −0.93** (M=1.0).
- The reach is **clip-invariant**: `c2_floor` 1e-4→5e-2 (−0.927→−0.908), `rho_floor` −0.99→−0.95 (−0.927, both), `N` 128→224 (−0.924→−0.912) — run-JSON `B_gate.super_floor`. The depth is physics, not apparatus.
- It **decisively beats the prior-art beam floor −0.26** (which stalled there because it was sub-yield, `A²_focal = 0.05`).
- The `∝ M_edge²` **exponent is confirmed** (known-positive `deepest/M² = −1.35 / −1.32 / −1.28`).
- Over-drive `M ≥ 1.1` pins at **exactly −0.950 = `rho_floor`** (`C_probe` rows; `clip_rho_hits = 552 / 57,532 / 232,340`) — correctly self-attributed CLIP in §2 already.

What this probe legitimately advances, and the **only** load-bearing claim it carries forward: **the EOS `c²=0` root `ρ̄_cav=−1/φ` is dynamically reachable by circulation.** Nothing about the *kind* of event.

### (c) Relabel the FLASH signatures: STRUCTURALLY UNAVAILABLE, not NEGATIVE

§0, §2.2, §2.3 and §7 read the three discriminating FLASH signatures as **negative findings**. Per defect (a) they must be relabeled **"structurally unavailable in this engine"** (not "negative"):

- **(ii) latent-release** — structurally unavailable: a positive-floored `c²` has no below-floor branch to release from.
- **(iii) persistent `c²≤0` pocket** — structurally unavailable: `c_eff²` is floored ≥ +1e-3·c₀² everywhere, so `pocket_cells = 0` is *enforced by the scheme*, not measured.
- **(iv) hysteresis** — structurally unavailable: reversible compliance is the only behavior a strictly-positive-stiffness medium can exhibit; recovery on de-spin is guaranteed, not discovered.

These are not evidence against FLASH; the experiment could not have produced them.

### (d) Known-positive prefactor miss (carried over, sharpened)

The known-positive confirms the **M² exponent** but the **magnitude is under-predicted**: observed prefactor `deepest/M² ≈ −1.3` vs the pre-frozen `−(¼ … ½)` (prereg §2.1) — under-predicted **2.6–5.4×**. This is *why* the crossing lands at `M* ≈ 0.8` rather than the pre-frozen `M ~ O(1)`: the deeper-than-predicted prefactor pulls the −0.618 crossing down from M≈1.1 to M≈0.7–0.8. Exponent confirmed; magnitude (and hence the critical drive) was mis-pre-registered.

### (e) FLASH-vs-LOCK is UNDECIDED — gated, not refilled

Because the dynamics never integrated a genuine `c²<0`, **whether the event is FLASH or LOCK is UNDECIDED** by this probe. §6 (the "needs a named below-floor closure" paragraph) is hereby **promoted to load-bearing**: a real FLASH/LOCK discrimination requires a **NAMED below-floor closure** (a latent-heat term, metastable-void nucleation, or a hardened `Γ=−1` wall) integrated into the dynamics, **with `c2_floor` swept inside the reversibility test.** The plumber-physical question — **what does the medium physically do at genuine `c²<0`** (does it rupture/cavitate, or is `c²<0` unreachable because something else yields first?) — is **surfaced to Grant as a gate.** This slot is **NOT** refilled with a new hypothesis (Rule 12 / A47 v11b: substitution-not-retraction).

### (f) ρ̄_cav status unchanged — still CANDIDATE-CLAIM

`ρ̄_cav = −1/φ` remains a **CANDIDATE-CLAIM** (`AVE-Propulsion/.../04_superluminal_transit.tex:86,89`; zero KB / `constants.py` hits). This probe does **not** promote it. It advances only that the EOS stiffness-collapse root is dynamically reachable by circulation; the physical interpretation (cavitation / vapor-lock) still needs the §6 mechanism + Grant adjudication.

---

## 1. The apparatus gate FIRST (STEP 3) — what the verdict had to clear

Per `ave-apparatus-floor-attribution`: every clip on `ρ̄`/`c_bulk²` was inventoried (prereg §3) and swept 4× each way at a fixed sub-floor (`M=0.5`) AND super-floor (`M=1.0`) drive BEFORE any physics claim. Clip floor the verdict must clear:

**Sub-floor drive (M=0.5, deepest ≈ −0.295) — the instrument is CLEAN above/at the approach to the floor:**

| knob swept (4 values) | deepest ρ̄_core | tracks knob? |
|---|---|---|
| `c2_floor` 1e-4 → 5e-2 | −0.295, −0.295, −0.295, −0.295 | **NO (invariant)** |
| `rho_floor` −0.99 → −0.75 | −0.295, −0.295, −0.295, −0.295 | **NO (invariant)** |
| `N` 128 → 224 | −0.295, −0.295, −0.295, −0.295 | **NO (resolution-robust)** |
| `nu_art` 0 → 5e-3 | −0.301, −0.295, −0.281, −0.257 | weak (conservative: ↑visc ⇒ shallower) |
| `rho_diff` 1e-4 → 5e-3 | −0.298, −0.295, −0.285, −0.271 | weak (conservative) |

**Super-floor drive (M=1.0, physical deepest ≈ −0.927):**

| knob | deepest ρ̄_core | reading |
|---|---|---|
| `c2_floor` 1e-4 → 5e-2 | −0.927, −0.927, −0.923, −0.908 | depth NOT set by c2_floor |
| `rho_floor` −0.99, −0.95, −0.85, −0.75 | −0.927, −0.927, **−0.850, −0.750** | **CLIP iff rho_floor > physical depth** |
| `N` 128 → 224 | −0.924, −0.927, −0.928, −0.912 | resolution-robust |

**Gate conclusion:** the depths up to ≈ −0.93 (M≤1.0) are **clip-INVARIANT** (independent of `c2_floor` 1e-4..1e-2, of `rho_floor` for −0.95..−0.99, and of `N`). The reach and crossing of `−0.618` are **physics, not apparatus.** The ONLY clip that bites is `rho_floor`, and only when it is set *shallower* than the physical depth (then ρ̄_core pins at `rho_floor` — the CLIP signature) — which is exactly the over-drive `M_edge ≥ 1.1` regime where the physical depth would exceed −0.95. Both stabilizers (`nu_art`, `rho_diff`) make the deficit *shallower* (conservative — they suppress, never manufacture, a deficit), so the true inviscid reach is at least as deep as reported.

---

## 2. The probe (STEP 4) — drive sweep, the reach curve

Solid-body rotation column (R_core=0.18, N=160, nu_art=5e-4, rho_diff=5e-4), drive = edge Mach `M_edge=v_θ,edge/c₀` (the one swept engineering knob; sets the INITIAL conserved circulation — energize+lock, never pumped).

| M_edge | deepest ρ̄_core | crossed −0.618? | min c_bulk²_core (raw) | rho_clip hits | L drift | verdict band |
|---|---|---|---|---|---|---|
| 0.3 | −0.115 | no | + | 0 | −0.00% | sub-floor LOCK |
| 0.5 | −0.295 | no | + | 0 | −0.22% | sub-floor LOCK |
| 0.7 | −0.535 | no | **+0.250** | 0 | −0.86% | sub-floor LOCK |
| **0.8** | **−0.767** | **YES** | **−0.862** | 0 | −1.31% | **floor-cross, LOCK** |
| 0.9 | −0.876 | YES | −2.777 | 0 | −1.62% | floor-cross, LOCK |
| 1.0 | −0.927 | YES | −5.526 | 0 | −2.14% | floor-cross, LOCK |
| 1.1 | −0.950 | YES | — | 552 | −2.57% | **CLIP (rho_floor)** |
| 1.2 | −0.950 | YES | — | 57 532 | −3.10% | **CLIP** |
| 1.3 | −0.950 | YES | — | 232 340 | −3.52% | **CLIP** |

- **Critical drive `M_edge* ≈ 0.75–0.8`** (deepest jumps −0.535 → −0.767 over ΔM=0.1 — the softening-feedback steepening the prereg §1 predicted: as ρ̄→floor, c_bulk² drops, less pressure support, deeper).
- **Stiffness collapse (FLASH signature i) PRESENT and robust:** c_bulk²_core crosses zero at M*≈0.8 and goes deeply negative (tensile failure) above it — the substrate-bulk-density tensile-failure pocket (the FOURTH object, prereg §0.2) forms *transiently*.
- **L (angular momentum) is the clean energize+lock invariant:** free-evolution drift = **0.044%** over 3000 steps (the ledger noise floor). Probe drift is 0.0–0.9% for M≤0.7 (clean) and 1.3–3.5% for M≥0.8 (real dissipation in the violent transient — flagged; conservative since viscosity biases shallower).

## 2.1 Time-series shape — bounded oscillation, NOT runaway (Fig 1, Fig 4-left)

Every drive deepens to a transient minimum then **REBOUNDS** (rebound +0.25 to +0.55; 5–15 oscillation sign-changes): the core rings. It does **not** monotonically run away to the clip and does **not** pin at the floor for M≤1.0. This is the prereg's LOCK "bounded oscillation about the floor / pocket-compliance" signature.

## 2.2 The crossing is CONTINUOUS — no latent release (FLASH signature ii NEGATIVE, Fig 4-right)

At the M=0.9 crossing of −0.618 (recorded t=0.24→0.28): KE 0.0483 → 0.0470 (smooth ↓), PE 0.0150 → 0.0165 (smooth ↑), KE+PE 0.0633 → 0.0631 (smooth, slow dissipation). **No step, no spike, no kink at the crossing.** The reactance pair (CP6: KE=L-state ↔ PE=C-state) exchanges smoothly. There is no latent-heat-like discontinuous release.

## 2.3 Hysteresis — REVERSIBLE (FLASH signatures iii, iv NEGATIVE)

| M_edge | deepest ρ̄_core | after de-spin (kill circulation) | pocket_cells_final | recovered? |
|---|---|---|---|---|
| 0.8 | −0.768 | **−0.128** | 0 | YES |
| 1.0 | −0.927 | **−0.068** | 0 | YES |

On de-energize, the rim over-pressure (the mass evacuated from the core piled into a `ρ̄>0` rim) pushes mass back into the core; ρ̄ rises above −0.618, `c_bulk²` becomes positive again, and normal acoustic restoration completes the refill. **The tensile-failure state is NOT a stable frozen defect in the canonical EOS — it heals once the centrifugal demand is removed.** `pocket_cells_final = 0` confirms no persistent `c_bulk²≤0` region remains. This is the decisive LOCK-vs-FLASH discriminator: reversible, no hysteresis, no locked/flashed pocket.

---

## 3. Matched control + prior art (STEP 4) — flag-don't-fix on "does circulation beat the beam"

| drive | deepest ρ̄_core | status |
|---|---|---|
| vortex M=0.6 (KE=0.0293) | −0.406 | physics (clip-robust) |
| vortex M=0.8 (KE=0.0521) | −0.768 | physics |
| vortex M=1.0 (KE=0.0815) | −0.927 | physics |
| curl-free breather, SAME KE (each) | **−0.950** (all three) | **CLIP** (pins at rho_floor) |
| prior-art counter-propagating beams | −0.26 | (sub-yield, A²=0.05) |

**Honest, non-overclaimed reading (the discriminator was confounded, so I report it straight):**
1. **vs the prior-art beams (−0.26):** the vortex (−0.41 to −0.93) goes far deeper — **but** the prior-art beams stalled at −0.26 because they were *sub-yield amplitude* (A²_focal=0.05, deep linear regime), NOT because beams-can't-cavitate. The deeper reach here is a *drive-amplitude/regime* effect (these drives are transonic), not proof that circulation-per-se beats compression.
2. **vs a SAME-ENERGY curl-free focused breather (this engine):** the breather reaches the clip (−0.95) at *equal energy* — i.e. a focused radial implosion is a *more efficient* core-evacuator than distributed circulation (it concentrates all KE on the core in one shot). **Circulation does NOT beat a same-energy focused compressional drive on DEPTH.** Its breather depth is clip-pinned (apparatus), so only its floor-CROSSING is meaningful.
3. **What circulation uniquely buys:** a *sustained* deficit at fixed conserved L (energize+lock) vs the breather's one-shot transient. Floor-crossing itself is NOT unique to circulation; sustaining it is the rotational signature.

---

## 4. Instrument floor (skill A — calibrated on knowns at the run's scale)

- **Known-null** (no rotation): ρ̄_core = 0.0 exactly (false-positive floor = 0).
- **Known-positive** (small M solid-body): deepest/M² = −1.35, −1.32, −1.28 for M=0.15/0.25/0.35 — the predicted `∝ M_edge²` centrifugal scaling (prereg §2.1) confirmed, L drift < 0.1%.
- **Free-evolution drift:** L conserved to 0.044% over 3000 steps = the energize+lock ledger noise floor.
- **EOS zero-crossing** numerically at ρ̄ = −0.61800 vs candidate −0.61803 (`−1/φ`); known-null/positive/drift all pass.

---

## 5. consistency-vs-emergence + regime/phase-state classification

- **Class:** this is a **manifestation/consistency** result, not an emergence claim. It tests whether a CANDIDATE-derived floor (`ρ̄_cav=−1/φ`, Propulsion `04_superluminal_transit.tex:86,89`) is dynamically reachable + what kind of event it is. The floor value is an *input bin boundary*, not a fitted/emergent output.
- **MODE/REGIME/PHASE-STATE (ave-regime-phase-state-check):** BULK volumetric-K density sector; near-floor rarefaction regime (the effect CAN exist here — not a wrong-regime artifact); phase-state traverses compliant → tensile-failure → (reversibly) back. DYNAMICAL (CP9): ρ̄ integrated by continuity, never the algebraic centrifugal formula.
- **phase-space-coordinate-check:** ρ̄_cav is a claim about the density variable ρ̄ itself (real-space volumetric strain) — measured in the matching coordinate. PASS (NOT the (2,3) phase-space case).
- **ave-conserved-vs-pumped:** circulation/L is conserved (energize+lock, free-drift 0.044%); never pumped. The drive set the initial L once. The pumpable stores (KE↔PE) sloshed at fixed L.

---

## 6. Implication for the vapor-lock picture (one paragraph, hypothesis-class language)

**Hypothesis-class statement (NOT a canonical claim):** *if* the "vapor-lock" picture requires the cavitated core to be a **persistent, irreversible** locked/flashed pocket (a frozen tensile-failure defect that survives removal of the drive — a true phase-change with latent release and hysteresis), then **the canonical rarefaction-stiffness EOS alone does NOT supply it.** Within `c_bulk²(ρ̄)=c₀²(1+ρ̄/(1−ρ̄²))` rendered as a stiffness-collapse (CP10 boundary-not-bulk), a self-circulating core genuinely *reaches and crosses* `ρ̄_cav=−1/φ` and the stiffness genuinely *collapses into tension* — but the crossing is **smooth and reversible** (LOCK / pocket-compliance): kill the circulation and the core heals. A genuine vapor-LOCK (irreversible, latent, hysteretic) would need an **additional below-floor rupture/nucleation mechanism** (a latent-heat term, a metastable-void nucleation, or a hardened `Γ=−1`-type wall that freezes the pocket) that the `c_eff²(ρ̄)` relation by itself does not encode. So this probe **localizes** the vapor-lock question: the floor is reachable (good), the stiffness-collapse is real (good), but the *irreversibility* — the part that makes it a "lock" rather than a "dip" — is **NOT** in the candidate EOS and must come from a separate, named, dynamical mechanism (a new hypothesis with its own verification chain, Rule 12 — not a refill of this slot).

---

## 7. DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED / canonical-anchored:**
- The candidate floor `ρ̄_cav=(1−√5)/2=−1/φ≈−0.618` as the `c_bulk²→0` root (Propulsion `04_superluminal_transit.tex:86,89`; bulk-mode freeze-point `temporal-values:30,39`). PHI canonical (`constants.py:199`); the floor is CANDIDATE, not Core-canonical.
- The `∝ M_edge²` linear-regime centrifugal scaling (prereg §2.1), confirmed by the known-positive.

**NUMERICALLY VERIFIED (this probe — native units, signs/depths/reversibility):**
- Reach + crossing of −0.618 by genuine circulation at M*≈0.8 (clip-cleared; gate §1).
- Stiffness collapse c_bulk²_core: +0.25 (M=0.7) → −0.86, −2.78, −5.53 (M=0.8/0.9/1.0).
- Continuous (no-latent) crossing — smooth KE↔PE; reversible de-spin recovery (−0.93→−0.07), pocket_cells_final=0 → **LOCK**.
- CLIP regime at M≥1.1 (pins at rho_floor −0.95) — apparatus, flagged.
- L (energize+lock) conserved to 0.044% free / ≤3.5% at high drive.

**BLOCKED / out of scope:**
- Absolute units (the EOS + drive are in natural c₀ units; depths/reversibility are dimensionless and unit-free, so the verdict is robust, but no Newtons/Joules).
- A TRUE-FLASH test: this engine has no below-floor rupture/latent/nucleation mechanism (by construction — it is the bare `c_eff²(ρ̄)` EOS). Whether a corpus mechanism makes the pocket irreversible is a separate hypothesis (§6).
- 3D vortex-ring geometry: deferred — 2D solid-body column was chosen (justified: clean centrifugal-deficit core, cheap enough for the 4×-each clip sweep + hysteresis the apparatus gate requires; the 3D ring's curved self-advecting core is the wrong tool for a floor-attribution study).

---

## 8. Corpus-state deltas to QUEUE (auditor lands; implementer surfaces only)

1. **NEW capability:** `CavitationFlow2D` — the rarefaction-stiffness bulk-flow branch (vector velocity + compressible density + the canonical softening EOS), the first AVE engine that can host *circulation + rarefaction* together (the scalar Master-Equation FDTD is irrotational; LBM is incompressible). Reusable for any bulk-density cavitation / vortex-core question.
2. **NEW result (manifestation-class):** the candidate floor `ρ̄_cav=−1/φ` is **dynamically reachable** by genuine centrifugal circulation (M*≈0.8), decisively below the prior-art beam −0.26 — but the floor-crossing is **LOCK (reversible compliance)**, not FLASH, under the bare canonical EOS. Forward-useful constraint on the vapor-lock picture (§6): irreversibility needs a mechanism beyond `c_eff²(ρ̄)`.
3. **FLAG (flag-don't-fix) for Grant — the matched-control confound:** "does circulation beat the beam −0.26" is **regime-confounded** — the prior-art beams stalled at −0.26 because they were *sub-yield amplitude*, and a *same-energy curl-free focused breather* reaches *deeper* than the vortex here (clipped). So circulation's distinct virtue is *sustaining* a deficit at conserved L, NOT reaching deeper per unit energy. Surfaced verbatim, not reframed.
4. **FLAG — `ρ̄_cav` remains CANDIDATE-CLAIM** (zero KB/constants hits); this probe does not promote it. It confirms the value is the EOS stiffness-collapse root and that the root is dynamically reachable; the *physical interpretation* (cavitation/vapor-lock) is the part needing the §6 mechanism + Grant adjudication.
