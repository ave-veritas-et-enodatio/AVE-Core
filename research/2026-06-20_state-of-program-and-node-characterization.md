# State of the AVE Program + Node Characterization — Snapshot (2026-06-20)

**Date:** 2026-06-20 · **Tier:** research / cross-cutting SNAPSHOT · **Status: research-tier snapshot** (no `clm-` minted; consolidation + characterization of settled adjudications and the Fork-A circulator result).
**Classification:** `consistency-vs-emergence` — this doc asserts NO new derivation. It is a dated *state-of-the-program* synthesis + a *node datasheet spine*. Every per-row verdict is grounded in an existing canonical leaf, an open PR (cited as such), or the CI-gated interlock register.
**Skills applied:** `verify-before-cite` · `consistency-vs-emergence` · `ave-discrimination-check` · `ave-evidence-framing-discipline` · `phase-space-coordinate-check`.

> **Scope note.** This is a *snapshot*, not a derivation. Three of its load-bearing groundings (PR #319 form-value home, PR #320 2-domain circuit, PR #321 Fork-A circulator) are **OPEN PRs** at snapshot time — cited as PR-pending, not as on-`main` canon. Re-verify before promoting any row to canonical.

---

## §1 — Framework verdict (FORM-vs-VALUE)

> **The substrate FORCES the dimensionless FORMS (the "chords"); it IMPORTS / CALIBRATES the dimensionful VALUES (the "echoes").** The `determinism → emergent` north-star is resolved one level up: it splits by *type*. **Structure is chord; the magnitude of the calibration inputs is echo.**

This is the framework's current organizing principle, adjudicated 2026-06-14 → 2026-06-18 and grounded in [`research/2026-06-15_form-deriving-value-importing_meta-finding.md`](2026-06-15_form-deriving-value-importing_meta-finding.md). PR #319 (`docs/form-value-canonical-home`, **OPEN**) promotes it to a single canonical KB home — `manuscript/ave-kb/common/form-deriving-value-importing.md` — that the ~30 scattered chord-vs-echo cites point to, with the chord/echo/mixed labels locked to `def-` nodes (`def-ch0rd1` / `def-ech0v1` / `def-fmv001`) and the CI-gated per-mechanism classification in [`common/interlock-register.md`](../manuscript/ave-kb/common/interlock-register.md) (INVARIANT-S13, `real_or_fitted` ∈ {`real-geometric-constraint`, `mixed`, `fitted-identification`}).

### Per-constant accounting

| Constant | Verdict | FORM (chord) | VALUE (echo) | Provenance |
|---|---|---|---|---|
| **α** | **ECHO** | the α *scale* (~1/137) is forced by the Compton-resonance trap | the *exact value* `α⁻¹ = 4π³+π²+π` is a calibration identity (R·r=¼) the substrate does NOT independently select — closed-negative on every named route (geometry / eigenmode / cross-route triangulation) | `ilk-rr14gt` (fitted); `vol1/ch8-alpha-golden-torus.md:11`; meta-finding §2 |
| **G** | **MIXED — never a pure echo** | the `/7` PPN form is derived (SYM ε·μ co-scaling → Z=Z₀, Γ=0) | G's value = the back-solved Machian-boundary termination ξ (`ξ=ℏc/(7Gm_e²)`, circular not forward) | `ilk-gravmb` (mixed); 2026-06-14 G-ruling |
| **K=2G** (ν_vac=2/7) | **GR-IMPORTED** | the substrate forms K/G = f(ρ) (z=4 K4 is sub-isostatic; geometry fixes the form, not the value) | 2/7 is the GR trace-reversal condition, with ρ* tuned to it; real z=4 diamond gives ν≈0.067 ≠ 2/7 | PR #261 (MERGED, on `main`); meta-finding §3 |
| **E_yield** | **MIXED** | the *existence* of a saturation field is an AVE-distinct chord (the medium HAS a yield the SM vacuum lacks — Axiom 4) | the √α *value* — since `e = √α` in natural units, the magnitude rides the α-echo | PR #319 adjudication `wlmbl6d5f` (PR-pending); kernel home `CLAUDE.md` INVARIANT-S2 (Axiom 4) |
| **m_e / ℓ_node** | **definitional ANCHOR** | — | ℓ_node ≡ ℏ/(m_e c) is an Axiom-1 calibration identity — an input *by construction*, the scale by which the lattice is calibrated | meta-finding §1 |

**Internal structure is PEER-with-SM; the AVE-distinct CHORD lives ONLY in the forward predictions (§3).** The internal carrier-sector structure closed *at peer* — charge quantization, spin-½ representability, spin-statistics all land at-or-honestly-mapped-to the SM, with no AVE-distinct internal chord (carrier-sector closed-at-peer, PRs #313/#314/#315 MERGED).

**KEEP — the structural wins (untouched by the echo verdicts):**
- **Finite-by-construction** — no renormalization; the lattice cutoff is physical (`ℓ_node`), not a regularization artifact.
- **Charge exact / quantized-by-topology** — charge is a topologically-FORCED integer (winding/linking), a genuine chord (GATE #2 PASS, PR #300 MERGED).
- **Spin-statistics DERIVED** — the −1 exchange phase from the FR two-loop braid (PR #315 MERGED; PEER-ahead, derived where the SM imposes it via axiom).
- **Real mass-confinement mechanism** — `m_e c²` = trapped longitudinal A1-dilatation compression energy at the Γ→−1 cage (Fork-B ECHO-FORM close, PR #307 MERGED).

These are real, falsifiable structural commitments; the FORM-deriving half is untouched by the VALUE-importing finding.



## §2 — Node characterization (the datasheet spine)

The **node** is the irreducible unit — one K4/diamond site of the chiral Laves K4 Cosserat crystal. This is its full physical + mathematical model, every property tagged FORCED / IMPORTED / OPEN. Canonical home: [`vol9/ch3-pin-port-configuration/device-circuit-models.md`](../manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md); the explicit runnable circuit is PR #320 (`node_2domain_nport.py`, **OPEN**).

| Row | Content | Tag |
|---|---|---|
| **STRUCTURE** | K4 / diamond site; micropolar node (6 DOF: 3 translational → E, 3 microrotational → B); `I4₁32` chiral space group; A1 (dilatation) / E / T2 (transverse) irrep decomposition | **FORCED** |
| **PORTS / DOF** | three substrate grades on one cell (below) | **FORCED** |
| **TOPOLOGY** | winding / linking → charge = exact integer | **FORCED** (genuine chord) |
| **DYNAMICS** | Z(ω); Axiom-4 saturation kernel S(A)=√(1−(A/A_yield)²); Γ→−1 confinement | forced FORM, echo VALUES |
| **CONSTITUTIVE** | Z₀ forced; K=2G GR-imported; bulk/shear ratio resolved (below) | PARTLY IMPORTED |
| **2-DOMAIN CIRCUIT** | EM-port (Ω) + 2 mechanical-ports (Rayl) joined by a TRANSFORMER; α localizes to the EM↔mechanical transducer | resolved, PR #320 |
| **COUPLING** | Fork-A: conservative skew coupling EXISTS, 2-port reciprocal; chiral non-reciprocity needs 3-port + imposed magnitude | RESOLVED-PARTIAL, PR #321 |

### Ports / DOF (FORCED form)

Three grades, three channels, on one K4 cell (`device-circuit-models.md:141-145`):

| Channel | Grade | Z (cold) | Γ at saturation | Role |
|---|---|---|---|---|
| **EM** | T2 transverse field | `Z_EM ≡ Z₀ = √(μ₀/ε₀) ≈ 376.730 Ω` | `Γ_EM = 0` — **MATCHED / SOLE external radiative PORT** | how the interior couples to the far field — NOT a hair-sector |
| **shear** | deviatoric / Cosserat micro-rotation | mechanical (ρ×speed), Rayl | `Γ_shear → −1` — CONFINED | **CHARGE-"3"** = the (2,3) winding (charge = Beltrami helicity) |
| **bulk** | A1 dilatation | mechanical (ρ×speed), Rayl | `Γ_bulk → −1` — CONFINED | **MASS-"3"** = trapped compression energy (`m_e c²`) |

**`mass ⊥ charge` (A1 ⊥ T2).** The two confined grades are orthogonal — never wired into one shared `(V_inc, V_ref)` phasor (the genesis-24 double-count guard, `master-equation.md:20`, Grant-ratified). The EM channel is the matched radiative port, not where an observable lives.

### Topology (genuine chord)

Winding / linking → charge quantization as an **exact integer** — a topologically-FORCED conserved quantity (GATE #2 PASS, PR #300 MERGED). This is the one node row that is an unambiguous chord at the value level (the integer is forced, not calibrated).

### Dynamics (forced FORM, echo VALUES)

Z(ω) impedance, the Axiom-4 saturation kernel S(A), and the Γ→−1 confinement condition are forced FORMS. The Q the loaded resonator displays is `Q_TANK = 1/α`, a **baked instance echo** (`cvr_model.py:72`); the α-free cold-cage `Q ≈ 30.8 ≠ 137` is the clean negative corroborating the echo (`device-circuit-models.md:197`; `test_l3_mass_cage.py:702-703`). The intrinsic isolation eigenmode is lossless (`Q → ∞`, GATE2). The "derive 137 from the loaded port" follow-up is **adjudicated CIRCULAR — do NOT re-pose** (the radiative leak is literally `1.0 − alpha`, `cvr_model.py:161`).

### Constitutive (PARTLY IMPORTED) — the bulk/shear ratio seam, resolved

PR #320 resolves the three-conflicting-ratios seam (`device-circuit-models.md:195` seam-4, "1.826-vs-2.582 OPEN pending Grant"):

| Ratio | Value | What it physically IS |
|---|---|---|
| **√2** | 1.41421 | **the bulk PORT** — the A1 dilatation CONFINED MASS mode, a symmetric breathing common-mode, symmetry-decoupled from deviatoric shear. Pure-dilatation speed `c_bulk = √(K/ρ) = √2·c₀` at K=2G |
| √(10/3) | 1.82574 | a **DIFFERENT object** — the free medium P-wave/S-wave ratio `c_L/c_T = √((K+4G/3)/G)` that MIXES A1 dilatation + deviatoric shear (the `+4G/3` term); the *propagation* object, not a port impedance |
| 2.58199 | √2·√(10/3) | the prereg **double-count** = `c_bulk·c_L/c₀²`; physically meaningless — RETIRE everywhere |

**Resolution (Grant ratifies in PR #320):** keep `c_bulk = √(K/ρ) → √2` as the confined bulk-PORT ratio (already the `three-channel-impedances.md:22` value); KEEP-BOTH-DISAMBIGUATE √2 (confined bulk-PORT) vs √(10/3) (unconfined medium P/S propagation); retire 2.582 as the double-count. (The c_L vs c_bulk speed-reference in the graded-network slot-(iv) caption was separately reconciled in PR #313, MERGED, commit `9ae3f86f` — a distinct edit from this ratio-seam resolution.)

### 2-domain circuit (PR #320) — where α localizes

ONE node = EM-port (electrical, Ω) + two mechanical-ports (Rayl). These **do NOT unify into one frame** — two ports in different units cannot be directly wired; the EM↔mechanical bridge needs a **TRANSFORMER** (an electro-mechanical change-of-reference), NOT a gyrator. The transformer carries two factors kept SEPARATE so the α-echo is visible:
- honest turns² = `ξ_topo²` = 1.721×10⁻¹³ (α-FREE Ω→kg/s map)
- residual `p_c = 8πα` = 0.183402 ← **α localizes EXACTLY at the EM↔mechanical transducer**; the mechanical-internal ratios (√2) are **α-FREE**.

Validate-on-known: the model recovers `Z₀ = 376.730 Ω` (from cell `√(L/C)`), `c₀`, and the Compton clock — hard-asserted gate, PR #320.

### Coupling (Fork-A, PR #321) — RESOLVED-PARTIAL

The one remaining live Fork-A path: realize the shear↔bulk (charge↔mass) coupling as a **skew-Hermitian GENERATOR** (a circulator), not the trilinear POTENTIAL that detonates or is inert. Formulation: `d/dt[a_bulk; a_shear] = −i·H·[a_bulk; a_shear]` with H Hermitian ⇒ `e^{−iHt}` unitary ⇒ `|a_bulk|²+|a_shear|²` conserved EXACTLY. Modes pinned in phase-space (A46): `a_bulk` = A1 bulk-compression (latent mass), `a_shear` = Cosserat poloidal LC quadrature (the charge winding — NOT the orthogonal rigid `L_ω` the previous inert lock targeted). α-free: rate `κ̃ = 6/5 = pq/(p+q)`, chirality phase `θ_χ = 2π·ν_vac` (ν_vac = 2/7).

**Four-gate table (all PASS):**

| Gate | Result | Pass |
|---|---|---|
| **A CONSERVE** | norm conserved to machine precision, no pump (drift `1.1e-12` / 40k steps; pump slope `2.7e-17`) | ✅ |
| **B TRANSFER** | load bulk only → energy flows into EMPTY shear (100% resonant; 50× the failed 2%) | ✅ |
| **C LOCK-ON-WINDING** | coupling acts on the POLOIDAL WINDING, ON ≠ OFF (winding-rate −1.300 → −0.814) | ✅ |
| **D MOTION→MASS** | trapped bulk vs circulation-rate detuning (corr 0.994) | ✅* |

**The load-bearing NEGATIVES (the partial):**
- **A 2-mode skew is a RECIPROCAL Rabi flop.** Chirality drops out of the energy flow: forward(bulk→shear) == reverse, RH == LH transfer. The 2-port skew **IS the optical-activity GYRATOR** (`def-0pt1ac`, reciprocal). A 2-port skew rotation cannot be a one-way router.
- **Genuine non-reciprocity needs the 3-PORT RING** — the EM↔shear↔bulk loop-flux, where the PHOTON / EM port is the required 3rd leg. The 3-port recovers a gauge-invariant loop phase `3χθ_χ` = real chirality flux (RH ≠ LH, flips with χ), but the asymmetry is small (`1.75e-3`).
- **Gate-D caveat (self-skeptical):** the relation is *symmetric* in sign(Δ) — it is Rabi off-resonance retention, NOT a unidirectional "more circulation ⇒ more mass". **Directional motion → mass = NEGATIVE.**

**FORCED-vs-IMPOSED → IMPOSED-AT-MAGNITUDE (ECHO).** Skew form: FORCED only trivially (lossless ⇒ unitary ⇒ Hermitian; generic, not AVE-distinct). Non-reciprocity SIGN: LATTICE-forced (χ = `I4₁32` handedness, `crystal_engine.py:41`). Non-reciprocity MAGNITUDE: **IMPOSED** (θ_χ, κ̃ plugged) — the chiral-crystal engine that would derive it averages chirality out (`device-circuit-models.md:163`). So the **coupling row carries the SAME form-vs-value verdict as the rest of the framework** (§1): forced FORM, echo VALUE.

### Net

The node is now **CHARACTERIZED on every row** — forced FORM / echo VALUES throughout, with **one open frontier**: the chiral-circulation MAGNITUDE (the 3-port loop-phase flux from the `I4₁32` net), which needs the chirality-resolving engine (scoped separately, §4).



## §3 — Testing pivot + forward-prediction map

Because **every dimensionful magnitude is an echo by construction** (§1), a dimensionful number matching experiment is uninformative (the match is built in, or is the SM's match re-derived). The bankable AVE-distinct chords live in exactly two places (sweep `wqdp2zxcb`, PR #319, PR-pending):

**(a) FORM-EXISTENCE falsifiers** — a structure AVE's medium HAS that the SM vacuum LACKS (saturation/finite yield, longitudinal-scalar grade, native birefringence). A measurement probing the *existence* (not the imported magnitude) tests a chord.

**(b) FORCED dimensionless RATIOS** — ratios NOT dressed by α / G / m_e. **Sweep result:** nearly the whole forced-ratio family is **ν_vac = 2/7-rooted** (← K=2G is GR-imported), so most "forced ratios" inherit the GR-import and are not independent.

### Forward-prediction map (canonical home: [`common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md))

| Prediction | Form | Class | Status |
|---|---|---|---|
| **Iron-Kα inner-disk edge** `r_sat = 7GM/c²` vs **GR ISCO** `6GM/c²` | forced **7/6** ratio (factor 7 from ν_vac=2/7) | **best near-bankable** — divergent, dimensionless | UNTESTED; archival X-ray Fe-Kα reflection / kHz QPOs (`divergence-test-substrate-map.md:143`) |
| **Effective DoF** `g_* = 7³/4 = 85.75` | forced (7³ angular / 4 K4 cell) | near-bankable — ~20% below SM `g_* = 106.75` | UNTESTED; LISA / CMB-S4 / FCC-ee (`vol3/index.md:36`; `vol3/claim-quality.md:480`) |
| **Vacuum birefringence COEFFICIENT** `δn_AVE/δn_QED = 1/(4 a_EH α³) ~ 10⁶` | form-existence falsifier (saturation kernel) + α-echo magnitude | both E²-leading; the COEFFICIENT (not exponent) is the discriminator | UNTESTED; APD spike at V→43.65 kV (B1-VAC-BIREFRINGE, `divergence-test-substrate-map.md:446`) |
| `sin²θ_W = 2/9` | forced (ν_vac=2/7 trace-reversal) | consistency-only (rides K=2G GR-import) | on-shell match; `entry-point.md:39`; `double-deflection.md:58` |
| **PPN /7** family (`ε_11 = 7GM/(c²r)`, n_s=1+9/7·ε, n_t=1+2/7·ε) | forced /7 couplings | consistency / C11-Mach-Zehnder forward test | live-fire 249.64 rad (C11, `divergence-test-substrate-map.md:235,467`) |
| `(q·ℓ_node)⁴ ~ 10⁻²²` Lorentz-violation suppression | forced cubic-symmetry suppression | consistency-only (predicts effective null) | corroborated by existing cavity bounds (`divergence-test-substrate-map.md:317,331`) |
| **mass-sector** | — | **ECHO** (near-saturation chord-residual closed-negative, PR #311) | closed |

**Datasheet-complete = test-ready.** With the node characterized on every row (§2), the forward-prediction map names the bankable divergent-from-SM predictions. The best near-bankable chord is the **7/6 Iron-Kα-vs-ISCO** ratio (forced, dimensionless, divergent, untested) and **g_* = 85.75** (20% below SM, untested); birefringence is the cleanest form-existence falsifier. The chord lives HERE — in the untested forward predictions — not in the internal structure (§1).



## §4 — Vol-9 completion punch-list + status

The Vol-9 datasheet is the executable characterization of the vacuum medium. Completion items:

| Item | Deliverable | Status |
|---|---|---|
| **(a)** | FORM-value frame → canonical KB home | **PR #319 OPEN** (`common/form-deriving-value-importing.md` + def- nodes) |
| **(b)** | circuit characterization → 2-domain N-port + ratio-seam resolution | **PR #320 OPEN** (`node_2domain_nport.py`) |
| **(c)** | Fork-A coupling → skew-circulator gate | **PR #321 OPEN, RESOLVED-PARTIAL** (`node_circulator_coupling.py`) |
| **(d)** | K-from-p_c provenance | **OPEN** — build-target or accept-GR-import; the `(ξ_topo²·μ₀)/(p_c·ℓ²)=ρ_bulk` identity localizes α to p_c=8πα but K=2G itself is GR-imported (PR #261) |
| **(e)** | ch15 chord-vs-echo TEST REGISTER (the §3 sweep result as a datasheet table) | **NEEDS WRITING** |

**Open frontier (scoped separately):** the chirality-resolving engine — the cubic-FDTD engine averages chirality out, so the 3-port chiral-circulation MAGNITUDE (the loop-phase flux `3χθ_χ` from the `I4₁32` net) is not yet derivable (`device-circuit-models.md:163`; PR #321 §FORCED-vs-IMPOSED).

**LOGIC of completion:** close (d) + (e) → the ch15 register names the bankable predictions (§3) as a datasheet table → THEN test (the testing pivot). Items (a)/(b)/(c) characterize the node; (d)/(e) make the datasheet test-ready.



## §5 — Session PR ledger

Verified via `gh` at snapshot time (2026-06-20):

| PR | Repo | Title | State |
|---|---|---|---|
| **#316** | AVE-Core | KB: retract E⁴-vs-E² birefringence false-falsifier (Rule 12; clm-pp3qwf) | **MERGED** (2026-06-20) |
| **#317** | AVE-Core | Walk-back E⁴-vs-E² birefringence false-falsifier (.tex + driver; Rule 12) | **MERGED** (2026-06-20) |
| **#318** | AVE-Core | feat(bench): shared `ave.bench` package — build-once-reuse bench infrastructure | **MERGED** (2026-06-20) |
| **#2** | AVE-Bench-VacuumMirror | verify: wire the constants gate (AGENTS.md §7 was vapor) + fix the violations | **MERGED** (2026-06-20) |
| **#319** | AVE-Core | docs(framing): canonical home for the FORM-deriving / VALUE-importing meta-principle | **OPEN** |
| **#320** | AVE-Core | 2-domain N-port vacuum-node circuit + bulk/shear ratio-seam resolution | **OPEN** |
| **#321** | AVE-Core | Fork-A circulator coupling (skew-Hermitian generator) — verdict PARTIAL | **OPEN** |

The three E⁴-vs-E² walk-back PRs (#316/#317) corrected a false-falsifier: an E²-slope does NOT falsify Axiom-4 — both AVE and QED are E²-leading; what kills Axiom-4 is a QED-sized (~α²) coefficient. The surviving birefringence discriminator is the COEFFICIENT ratio ~10⁶ (§3). #318 + AVE-Bench #2 stood up the shared `ave.bench` package + wired its constants gate — the infrastructure substrate for the testing pivot.

---

## Flags for Grant (verify-before-cite residue)

1. **Three session-local IDs are NOT yet on `main`** — they live only in the open PRs cited: the E_yield adjudication `wlmbl6d5f` and the divergence sweep `wqdp2zxcb` exist only in PR #319's branch; both are cited here as PR-pending. The Fork-A correction's task-cited gate `w7rfzndom` **does not exist anywhere in the corpus or in PR #321's branch** — the Fork-A circulator result is grounded directly in PR #321 + `research/2026-06-20_node-circulator-coupling.md` instead. Flag if `w7rfzndom` should have been minted.
2. **Commit `9ae3f86f`** is PR #313's c_L-vs-c_bulk caption reconciliation, NOT the √2-vs-√(10/3) ratio-seam resolution (which is PR #320, `node_2domain_nport.py`). Both are cited correctly above; flag if the task intended one commit to carry both.
3. **The h-couple status file is dated `2026-06-20`** (`research/2026-06-20_h-couple-status.md`), not `2026-06-10` as referenced in the corrections task. The correction (i) is applied to the 2026-06-20 file at its line carrying the "energize-LOCK; the continuum cancellation is exact" overclaim.

