# PREREG — Cavitation-core probe: does a self-circulating core reach ρ̄_cav = −1/φ, and is the event FLASH / LOCK / CLIP / NO-REACH?

**Date (frozen):** 2026-06-10
**Branch:** `analysis/2026-06-10-cavitation-core-probe` (worktree off `origin/main`; do not push/merge)
**Governing discipline:** `ave-apparatus-floor-attribution` (the whole question is FLASH-physics vs CLIP-apparatus)
**Skills fired at design time:** substrate-native-check (CP1/2/4/5/6/7/9/10 walked below), ave-prereg (corpus-grep below), ave-canonical-source, ave-conserved-vs-pumped, ave-regime-phase-state-check, phase-space-coordinate-check, ave-driver-script-honesty, verify-before-cite.

---

## 0. The target (one sentence)

Does a **circulating bulk-density flow**, rarefied by its **own** rotation (centrifugal pressure deficit), drive its core density `ρ̄_core` down to the candidate cavitation floor `ρ̄_cav = (1−√5)/2 = −1/φ ≈ −0.618` — and if it reaches there, is the event a **FLASH** (discontinuous phase-change: stiffness collapse `c_bulk²→0`, latent-release, pocket formation, hysteresis on de-energize), a **LOCK** (bounded oscillation about the floor — pocket-compliance), a **CLIP** (the value pins at a numerical floor parameter — apparatus), or **NO-REACH** (circulation cannot rarefy below ≈ −0.3 at any stable drive)?

## 0.1 CANDIDATE-CLAIM status of ρ̄_cav (HARD CONSTRAINT)

`ρ̄_cav = −1/φ` is a **CANDIDATE-CLAIM**, Propulsion-derived: it is the `c_eff² → 0` root of
`c_eff² = c₀²(1 + ρ̄/(1−ρ̄²))` (`AVE-Propulsion/.../04_superluminal_transit.tex:86,89`, "not a free parameter", Ax4), reproduced as the **bulk-mode** freeze-point in `AVE-Core/research/2026-06-09_substrate-temporal-values-definition.md:30,39,68,70`. Zero KB/`constants.py` hits → **NOT Core-canonical**. Cited as candidate throughout; never "canonical". The root:
```
1 + ρ̄/(1−ρ̄²) = 0  →  ρ̄² − ρ̄ − 1 = 0  →  ρ̄ = (1−√5)/2 = −1/φ ≈ −0.6180339887
```
(`PHI = (1+√5)/2` is canonical, `constants.py:199`; `−1/PHI` reproduces the root — this is the only canonical anchor.)

## 0.2 FIREWALL (HARD CONSTRAINT — the cavitated core is a FOURTH object)

Per `_orchestration/double-slit-ee-mapping.md` cavitation-distinctness line: the cavitated core is handled as a **substrate-bulk-density tensile-failure pocket** — explicitly **NOT** the Rayleigh-Plesset bubble (no saturated inertial gas bubble), **NOT** the photon bubble, **NOT** the Γ=−1 EE cavity (this is the bulk/volumetric **K** sector, not the shear A→1 saturation ceiling). It is the `c_bulk² ≤ 0` tensile-failure region of the volumetric modulus. This language is used in prereg + result.

---

## 1. Physical picture (substrate-native, before equations)

- **What circulates, where:** a column of substrate bulk-density medium carrying a conserved **circulation** Γ (a vortex line / solid-body-rotation column). The azimuthal velocity `v_θ(r)` demands a centripetal force; the only force available in the inviscid bulk is the **pressure gradient**. The medium responds by evacuating density from the core until `∂p/∂r = ρ v_θ²/r` — a **centrifugal pressure deficit**. The core is where `ρ̄` is most negative.
- **Which limit:** the bulk volumetric modulus **K** (NOT shear G, NOT EM). Stiffness `c_bulk²(ρ̄) = c₀²(1+ρ̄/(1−ρ̄²))` **softens** on the rarefaction side and crosses zero at `ρ̄_cav = −1/φ`. Below it `c_bulk² < 0` = tensile failure = the pocket.
- **The conserved invariant (ave-conserved-vs-pumped):** circulation Γ / vorticity ζ = ∂ₓv − ∂_yu is a **conserved** topological invariant (Kelvin's theorem for barotropic inviscid flow, `d|Γ|/dt = 0`). It is **ENERGIZED + LOCKED**, never pumped. The swept "drive amplitude" sets the **initial** circulation (the energizing); the dynamics then evolve freely. No secular drive term on ζ.
- **The feedback that could FLASH:** as `ρ̄_core → −0.618⁺`, `c_bulk² → 0⁺`, so the pressure-restoring acceleration `−[c_bulk²/(1+ρ̄)]∇ρ̄ → 0`. The core loses its ability to resist centrifugal evacuation → positive feedback (softer ⇒ deeper ⇒ softer). Whether this runs away discontinuously (FLASH) or is capped by mass-conservation / rim back-pressure (NO-REACH) or rings boundedly (LOCK) is the empirical question.
- **Discrete onset vs smooth curve:** below the floor the core deficit is a smooth `∝ M_edge²` curve (M_edge = v_θ,edge/c₀). The discrete-onset signature (if any) is the stiffness-collapse / pocket-nucleation event at `ρ̄_cav`.

## 1.1 substrate-native-check (walked at design time, recorded)

- **CP1 (dynamics):** wave propagation / dynamical time-integration of the compressible **bulk-density** flow — NOT minimization, NOT a root-find for the equilibrium. The lattice/flow IS the computation.
- **CP2 (sector + carrier capability):** BULK volumetric **K** sector; state = density `ρ̄` + velocity vector `u`. **The existing scalar `MasterEquationFDTD` is irrotational** (scalar potential ⇒ ∇×∇V≡0 ⇒ no circulation) and implements the *stiffening* saturation kernel `c²=c₀²/√(1−A²)`, NOT the *softening* rarefaction relation; **`lbm_3d.py` is incompressible** (constant density ⇒ no rarefaction). Neither can carry "circulating + rarefying", so a dedicated **vector-velocity compressible bulk-flow branch** is required (representation-capability finding, justified).
- **CP4 / phase-space-coordinate-check:** the corpus claim `ρ̄_cav` is a claim about the **density variable ρ̄** itself (a real-space volumetric-strain scalar) — NOT a phase-space φ²/Clifford-torus claim. So the matching measurement coordinate IS the real-space ρ̄ field. (This is explicitly NOT the (2,3)-topology phase-space case A46 warns about.) PASS.
- **CP5 (local clock):** track `c_bulk²(r)` and the local bulk clock `τ_bulk(r) = τ₀/√(1+ρ̄/(1−ρ̄²))` (temporal-values:39); the clock freezes (τ→∞) exactly at the floor — a stiffness-collapse co-signature.
- **CP6 (reactance pair):** the compressible LC pair = compression PE (C-state, `∫ pressure-energy(ρ̄)`) ↔ kinetic energy (L-state, `½∫ρ|u|²`). Track BOTH every recorded step + total energy + Γ conservation.
- **CP7 (sampling):** PML/sponge cells excluded before any extremum extraction; sample `ρ̄_core` as the **density minimum** (most-negative ρ̄) in the interior, not a centroid+offset (the core of a rotating column is a genuine extremum at the axis).
- **CP9 (heuristic-vs-dynamical):** LOAD-BEARING. `ρ̄_core` is **dynamically evolved** by the continuity equation integrating `−∇·[(1+ρ̄)u]` — it is NOT the algebraic centrifugal formula `ρ̄(r) = −½(Ω²r²)/c²` plugged in. Plugging the analytic profile would test nothing. We integrate the actual flow and let ρ̄ build.
- **CP10 (boundary-not-bulk):** cavitation is rendered as a **stiffness collapse in the EOS wave-speed** `c_bulk²(ρ̄)` inside the momentum equation (the natural constitutive location), NOT as an added confining bulk potential. No `dS/dA`-style bulk force.

---

## 2. Governing equations (the rarefaction-stiffness bulk-flow branch)

2-D compressible, barotropic, inviscid bulk-density flow (the substrate-native "1" longitudinal/volumetric sector). State `ρ̄(x,y)`, `u=(u,v)`; full density `ρ = ρ₀(1+ρ̄)`:

```
Continuity:  ∂ρ̄/∂t = −∇·[(1+ρ̄) u]
Momentum:    ∂u/∂t  = −(u·∇)u − [c_bulk²(ρ̄)/(1+ρ̄)] ∇ρ̄
EOS:         c_bulk²(ρ̄) = c₀²(1 + ρ̄/(1−ρ̄²))        (Propulsion 04_superluminal_transit.tex:86; Ax4, zero free params)
```
Conserved invariant: vorticity `ζ = ∂ₓv − ∂_yu`, circulation `Γ = ∮u·dl`, `d|Γ|/dt = 0` (barotropic Kelvin). Tracked as the energize+lock check.

### 2.1 Dimensional analysis / magnitude pre-freeze (ave-prereg Step 3.5)

Linear-regime radial balance `dp/dr = ρ v_θ²/r` with `p = c₀²ρ₀ρ̄` gives, for solid-body rotation `v_θ = Ω r` over core radius R:
```
ρ̄(R) − ρ̄(0) ≈ Ω²R²/(2c₀²) = M_edge²/2,     M_edge ≡ v_θ,edge/c₀ = ΩR/c₀
```
With approximate mass conservation (mean ρ̄ ≈ 0 over the column), the **core deficit scales as**
```
ρ̄_core ≈ −(¼ … ½)·M_edge²        (profile-dependent prefactor)
```
**Consequence pre-frozen:** reaching `ρ̄_core = −0.618` requires `M_edge ~ O(1)` — i.e. **transonic edge rotation** (`v_θ,edge ~ c₀`). This is the regime where the nonlinear softening feedback (§1) turns on. Sub-transonic drives (`M_edge ≲ 0.5`) should stall well above the floor (deficit `≲ −0.12`); the floor is only approachable near `M_edge ~ 1`. The drive sweep must therefore span `M_edge ≈ 0.3 → ~1.4`.

---

## 3. APPARATUS INVENTORY — the CLIP suspects (the rarefaction analog of S_min / A_cap)

> 🔴 **POST-RUN AMENDMENT (2026-06-10) — see [§3 AMENDMENT](#3-amendment--2026-06-10-post-run-rule-12) at the end of this file (Rule 12: appended, the §3 table below is preserved verbatim). It records (a) a post-freeze inventory addition (`rho_diff`), (b) two inventoried-but-UNSWEPT knobs (`eps_den`, `cfl`/`dt`), (c) the "all clips swept 4× each" coverage overstatement corrected to 5-of-7-swept, and (d) the single-commit ordering caveat.**

Every numerical floor/clip/epsilon on `ρ̄` and `c_bulk²` is enumerated here BEFORE any run. The verdict must clear these (STEP 3 gate sweeps them):

| # | knob | default | what it could secretly set | how it's a CLIP |
|---|---|---|---|---|
| K1 | `c2_floor` | `1e-3·c₀²` | floors `c_bulk²(ρ̄) = max(…, c2_floor)` to keep the scheme hyperbolic (CFL) | the apparent "stiffness-collapse depth" / `c_bulk²→0` reading could BE this floor, not physics |
| K2 | `rho_floor` | `−0.95` | clips `ρ̄ = max(ρ̄, rho_floor)` to keep `(1+ρ̄)>0` and `(1−ρ̄²)>0` | if `rho_floor > −0.618` it PINS ρ̄_core above the floor (false NO-REACH); if ρ̄_core sits AT rho_floor it is CLIP |
| K3 | `eps_den` | `1e-6` | `(1−ρ̄²)` → `(1−ρ̄²)` guarded; denominator epsilon | minor; sets behaviour right at ρ̄→±1 |
| K4 | `nu_art` | `2e-3` (lattice) | artificial viscosity `+nu_art ∇²u` for stability | dissipates the conserved Γ; could damp the deficit (false NO-REACH) OR smooth a real FLASH |
| K5 | `cfl` / `dt` | `0.25` | timestep safety | too-large dt → blow-up read as FLASH; too-small → no effect |
| K6 | `N` | 192 (2D) | grid resolution | under-resolved core → false floor |

**The verdict-clearing rule (ave-apparatus-floor-attribution):** a reported FLASH/LOCK depth that **tracks** K1–K6 under the sweep is APPARATUS (→ CLIP verdict). A depth that **plateaus independent** of K1–K6 is (provisionally) physics. The clip floor the verdict must clear is established in STEP 3 before any physics claim.

---

## 4. THE BINS (FROZEN — Rule 11, no post-hoc redefinition)

- **FLASH** — `ρ̄_core` crosses `−0.618` accompanied by a **discontinuous event**: (i) stiffness collapse `c_bulk²_core → 0` at the crossing, AND at least one of (ii) a latent-release signature (a step/spike in the energy partition — kinetic↔compression — at the crossing, not a smooth ramp), (iii) a defect/pocket of finite spatial extent with `c_bulk² ≤ 0`, (iv) **hysteresis**: on de-energize (kill the circulation), `ρ̄_core` does NOT recover to 0 — the pocket persists. AND knob-independent (clears §3).
- **LOCK** — `ρ̄_core` reaches near `−0.618` and executes **bounded oscillation about the floor** (pocket-compliance), and on de-energize it **recovers** to ≈ 0 (reversible). Knob-independent. No discontinuity.
- **CLIP** — `ρ̄_core` (or the `c_bulk²→0` reading) **pins at / tracks a §3 knob** (rho_floor or c2_floor) under the STEP-3 sweep. Apparatus, not physics. NOT a flash.
- **NO-REACH** — `ρ̄_core` cannot get below ≈ −0.3 at any **stable** drive (integrator stays valid, Γ conserved); the deficit caps well above the floor. Characterize the limiter (mass-conservation? rim back-pressure? Γ redistribution?). The prior-art beam floor is the anchor: `tr_min = −0.26`.

A "flash" sitting at a clip value is apparatus (HARD CONSTRAINT). Do NOT debug toward FLASH.

---

## 5. PREDICTIONS (discriminating outcomes)

- **Outcome A (expected, primary):** a **critical drive** `M_edge*`. Below it: LOCK — bounded centrifugal deficit, reversible, depth `∝ M_edge²`, never near floor. Above it: the softening feedback drives `ρ̄_core` through −0.618 → FLASH (stiffness collapse + persistent tensile-failure pocket + hysteresis), PROVIDED the depth clears §3.
- **Outcome B (alternative):** NO-REACH — mass conservation + rim back-pressure cap the deficit above −0.618 at all stable drives. Then the discriminator vs the matched control + prior art: does genuine circulation beat the beam floor `−0.26`, or stall at the same place (→ "the limiter is generic, not beam-vs-vortex")?
- **Outcome C (null / apparatus):** CLIP — the deep reading tracks rho_floor or c2_floor. The "flash" is the bench. Report the clip floor; no physics claim.

## 5.1 Matched control + prior art

- **Matched control (same energy, no circulation):** same total kinetic energy injected as a **curl-free radial (diverging) breather** (`ζ = 0`). Curl-free ⇒ no conserved sustained deficit ⇒ should dip-and-rebound. **Discriminator:** does the conserved-circulation vortex reach deeper / sustain, vs the curl-free same-energy drive?
- **Prior art anchor:** counter-propagating opposite-handed **beams** reached `tr_min = −0.26` ("sub-cavitation, the mundane suction side", `2026-06-08_rrad-l-rarefaction-phase5_result.md:24,119,131`). **Does circulation beat −0.26?**

## 5.2 Falsifiers

- FLASH framing falsified if the collapse depth tracks any §3 knob (→ CLIP), OR if Γ is not conserved across the "event" (→ the event is dissipation/numerics, not physics).
- The probe-vs-beam claim falsified if the vortex stalls at the same ≈ −0.26 as the beams (→ limiter is geometry-generic, circulation buys nothing).

---

## 6. Regime / phase-state declaration (ave-regime-phase-state-check)

- **MODE:** BULK (volumetric K, density sector) — NOT shear, NOT EM-transverse. Scalar effect (density rarefaction), regime-relevant.
- **REGIME:** near-floor rarefaction — pushing toward the `c_bulk²→0` tensile-failure boundary (the analog of near-yield, on the rarefaction side). The effect (deep rarefaction / cavitation) CAN exist in this regime by construction; this is NOT the wrong-regime-artifact trap that voided the sub-yield dark-wake nulls.
- **PHASE-STATE:** start compliant (ρ̄=0, linear), evolve toward the rarefaction floor; the FLASH bin is precisely the rupture/tensile-failure phase transition.
- **DYNAMICAL (CP9):** ρ̄ and u are time-integrated state variables, not algebraic observers.

## 6.1 ave-conserved-vs-pumped (recorded class)

Circulation/vorticity = **conserved** topological invariant (Kelvin, barotropic, `d|Γ|/dt=0`) → **energize + lock**, NOT pumped. The drive amplitude sets the initial Γ once; no secular drive term. Compression PE and kinetic energy are the pumpable/exchangeable extensive stores that slosh at fixed Γ. A run whose Γ drifts is dissipation-contaminated (flagged, not a physics event).

## 7. Zero new free parameters (beyond the swept engineering drive)

The ONLY free parameter is the **drive amplitude** `M_edge` (the energizing of the circulation), which is swept. `c₀`, the EOS, and `ρ̄_cav` are canonical/candidate-derived. K1–K6 are apparatus knobs (swept in STEP 3, not physics inputs). No tuned coefficient enters the verdict.

---

## 8. Corpus-grep (ave-prereg Step 2 — prior work)

- **Prior floor-proximity run (the anchor):** `2026-06-08_rrad-l-rarefaction-phase5_result.md` — counter-propagating opposite-handed chiral **beams**, `tr_min = −0.26` (sub-cavitation), ledger-closed, derived the floor `ρ̄_cav=−1/φ`. THIS probe replaces beams with genuine circulation.
- **The derivation:** `04_superluminal_transit.tex:86,89` (the `c_eff²` relation, Ax4, "not a free parameter").
- **The bulk-mode floor assignment:** `2026-06-09_substrate-temporal-values-definition.md:30,39,68,70` (bulk K mode freezes at `ρ̄_cav=−1/φ`; bulk desaturation = the rarefaction floor).
- **No existing compressible-flow / circulation-with-conserved-Γ / cavitation solver** in `src/ave/` (scalar `MasterEquationFDTD` irrotational; `lbm_3d.py` incompressible; gargantua "vortex" is a ray-march renderer). Green-field engine; treat results with extra skepticism + cross-check (the matched control + the linear-regime analytic known-positive serve as cross-validation).

**Corpus state:** OPEN (the floor is derived; the circulation-vs-beam reach + the FLASH/LOCK/CLIP/NO-REACH classification are unrun).

---

## §3 AMENDMENT — 2026-06-10 (post-run, Rule 12)

Appended after the run (commit `b8143b7c`) per the 2026-06-10 cavitation-core-probe panel review. The frozen §3 K1–K6 table above is **preserved verbatim and NOT rewritten**; these are the post-freeze record corrections.

**(a) `rho_diff` was added to the clip inventory POST-FREEZE.** Conservative (mass) diffusion `rho_diff` is **not** in the frozen §3 K1–K6 table (K1 `c2_floor`, K2 `rho_floor`, K3 `eps_den`, K4 `nu_art`, K5 `cfl`/`dt`, K6 `N`); it appears only in the result-doc gate sweep. It **was** swept (sub-floor M=0.5): `rho_diff` 1e-4 → 5e-3 shallows the deficit **−0.298 → −0.271** (run-JSON `B_gate.sub_floor.rho_diff`). Direction is **conservative** (more diffusion ⇒ shallower deficit ⇒ it can only suppress, never manufacture, the reach), so the post-freeze addition does not threaten the floor-crossing.

**(b) `eps_den` (K3) and `cfl`/`dt` (K5) were inventoried but NEVER SWEPT.** Non-binding rationale, recorded for honesty:
- `eps_den` guards `(1−ρ̄²)` only as `ρ̄ → ±1`; the deepest physical reach is `≈ −0.93` (`|ρ̄| ≤ 0.93`), far from the guard — so `eps_den` is irrelevant in the achieved regime.
- `cfl`/`dt` was left at default. An unswept (possibly too-large) `dt` biases toward **false-FLASH** (blow-up read as a flash event, per the §3 K5 note). Since the verdict landed on the LOCK/CLIP side, leaving `cfl`/`dt` unswept is **conservative** — it could only have manufactured a flash we did NOT claim.
- (Note on numbering: the review brief labeled `cfl`/`dt` as "K6"; the frozen §3 table numbers it **K5**, with `N` as K6. The frozen numbering governs this doc.)

**(c) Coverage correction — "all clips swept 4× each" is an OVERSTATEMENT.** The §3 closing line ("K1–K6 are apparatus knobs (swept in STEP 3)", §7) and the result-doc §1 ("every clip … swept 4× each way") imply full coverage of the inventory. Counting the post-freeze `rho_diff`, the inventory totals **seven** knobs; the run swept only **five 4× each** — `c2_floor`, `rho_floor`, `nu_art`, `N` (four of the six frozen) **+** `rho_diff` (the post-freeze addition). `eps_den` (K3) and `cfl`/`dt` (K5) were **not** swept. Corrected statement: *five knobs swept 4× each; two inventoried-but-unswept, both conservative-direction per (b).*

**(d) Process note — prereg-before-run ordering is doc-structural, not git-provable.** The prereg, the result doc, the engine (`cavitation_flow.py`), the driver, the run-JSON and all four figures landed in a **single commit** (`b8143b7c`, 10 files). Git history therefore cannot prove the prereg was frozen before the run; the ordering rests only on the doc's "frozen" dating. **Process fix for future probes: commit the frozen prereg in its OWN commit BEFORE running**, so prereg-before-run ordering is git-provable.
