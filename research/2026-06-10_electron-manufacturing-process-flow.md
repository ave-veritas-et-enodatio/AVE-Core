# Electron-manufacturing process flow — a fab traveler for building one electron from a photon

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-electron-manufacturing-flow` (worktree off `origin/main`; not pushed/merged)
**Grant directive (verbatim, the header question this doc answers):**

> **"do we need energy accounting? Enhance free body diagram? walk through a manufacturing an electron engineering process flow/steps?"**

**Status:** ENGINEERING-PROCESS-FLOW synthesis (fab-traveler format) over CANONICAL + CANDIDATE-CLAIM pieces. It assembles the existing genesis-arc results, the in-flight cavitation/vapor-lock/BEMF probes, and the Vol 9 cell datasheet into one traveler with explicit QC gates and a forward FBD. **It introduces no new derived number.** The one live derivation it attempts — the forward `R/r` radial balance (§4) — returns **UNDERDETERMINED**, reported as such (the discipline at full strength, not debugged toward `φ²`).

**Disciplines applied:** `ave-fundamental-ground-up-implementation` (§4 is its case — the forward balance is attempted from canonical constants, not deferred), `ave-live-fire-derivation-provenance` (§4 ran the code: dead-input + forward-vs-fit residual tests), `ave-apparatus-floor-attribution` (every QC gate carries its instrument floor), `consistency-vs-emergence` (every step + the §4 outcome class-tagged), `ave-canonical-source` (the numeric check imports `ave.core.constants` only), `verify-before-cite` (every `file:line` grep-confirmed this session; unpushed content cited by branch+commit, or by branch+working-tree where untracked), `ave-evidence-framing-discipline`, `ave-representation-capability-check` (the real-space `O₁` unknot vs the `(2,3)` phase winding kept distinct throughout), `ave-driver-script-honesty`, `flag-don't-fix`.

**Representation-capability lock (held throughout, per the hard constraint):** the manufactured object is a **real-space `O₁` UNKNOT vortex ring carrying a `(2,3)` PHASE-space winding**. The two are never conflated. `R/r` (§3–§4), the pocket geometry, the radii — all are **real-space `O₁` ring** quantities. The `(2,3)` charge/spin winding lives in the `(V_inc, V_ref)` Clifford-torus **phase space** and is read by the Park projection (OP-6), never by the radial FBD. The cavitated core is a **FOURTH distinct object** (a bulk-K tensile-failure pocket), firewalled from the `Γ=−1` impedance cavity, the photon bubble, and the Rayleigh-Plesset inertial bubble — per `double-slit-ee-mapping.md:101` (the three-object non-merge) extended by the vapor-lock framing doc's §4.

---

## §0 — TL;DR (the traveler at a glance)

Building one electron = running a photon through 7 operations on the vacuum cell (Vol 9 datasheet). The chain is **mechanically localized but NOT closed**: two operations have no corpus mechanism (OP-2 close-the-loop; OP-4 flash-irreversibility), one has a falsified-and-walked-back drive (OP-3, the v3/v4 graft failures), and the geometry lock (§4 `R/r`) is underdetermined. The arc's actual failures map cleanly onto specific steps — each failure is a step's QC gate firing, which is the traveler working as designed.

| OP | name | event | QC verdict to date |
|---|---|---|---|
| 0 | RAW MATERIAL | vacuum at operating point + photon(s) | open: pair/partner question |
| 1 | FOCUS | self-lensing (achromatic gradient) | reproduces (genesis precursor) |
| 2 | CLOSE-THE-LOOP | open path → closed `O₁` ring | **NAMED UNKNOWN #1** (no mechanism) |
| 3 | RAREFY | circulation drops core to `ρ̄_cav` | floor REACHED (cavprobe), drive-conversion FALSIFIED (v3/v4) |
| 4 | FLASH | strain-snap phase change + latent heat | **LOCK not FLASH** (cavprobe): irreversibility absent in bare EOS |
| 5 | LOCK | pocket compliance + BEMF payment + C3 latch | wrong-shaft lock (v4); pump-detonation (genesis-24) |
| 6 | SETTLE/QC | phase-space read of `(2,3)`, charge, mass, α | `(2,3)` does not self-assemble; α leak dispersion-contaminated |

---

## §1 — THE PROCESS STEPS (the fab traveler)

Each step: **inputs | operation | regime/conditions | QC gate (measurable + instrument floor) | failure modes (arc failures mapped) | running ledger deltas**.

### OP-0 — RAW MATERIAL: the vacuum cell at operating point + the input photon(s)

- **Inputs:** (i) the natural vacuum substrate `𝓜_A` at a defined operating point `A₀` — the chiral Laves K4 Cosserat crystal documented in the **Vol 9 cell datasheet** (`manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex:18,38`: *"the same epistemic stance as a manufacturer's component datasheet for a natural material … the substrate documented here is the natural vacuum"*). (ii) the input transverse photon(s), energy `E_γ`.
- **Operation:** none yet — this is incoming-material inspection. The cell's operating point is `(A₀, T, boundary class SYM/ASYM, regime I–IV)` (`ch01:54`). The relevant absolute-maximum ratings (the datasheet's "do-not-exceed" box, `ch02_absolute_maximum_ratings.tex`): `V_snap = m_e c²/e ≈ 511 kV` (`:33,79`, per-node topological node-destruction), `E_S = m_e²c³/(eℏ)` Schwinger (`:35,85`), `B_snap²/(2μ₀) = m_e c²/ℓ_node³` per-cell (`:37,59`), and — load-bearing for this traveler — the row `ρ̄_cav` at `ch02:61`: *"per-cell (bulk) DERIVED (c_bulk=0 root) — **CANDIDATE-CLAIM**"*.
- **Regime/conditions:** Regime I (small-signal) on arrival; the operation drives toward the Regime III/IV boundary `r = A/A_c = 1.0` where saturation reorganizes topology (`ch02:18`).
- **QC gate:** photon energy/momentum manifest vs the threshold. **Measurable:** `E_γ` and `p_γ = E_γ/c`. **Instrument floor:** the Vol 9 ratings are derived from `{m_e, c, ℓ_node}` with `α` the only calibration input (`ch02:64`); the per-cell field resolution floor is `E_yield = V_yield/ℓ_node ≈ 1.13×10¹⁷ V/m` below which Axiom-4 corrections are sub-coupling and unresolvable (`CLAUDE.md` operating-point note).
- **OPEN — the pair/partner question (surfaced explicitly, NOT resolved here):** a single transverse photon cannot become a single electron — charge, lepton number, and momentum conservation forbid it (the corpus pair-production canon, Vol 9 `ch02:85` / `clm-ezai5b`, makes electrons in **e⁺e⁻ pairs**, parity forcing one LH + one RH). So OP-0's true raw material is either **(a)** a photon **plus a partner/seed region** that absorbs the conjugate charge + recoil, or **(b)** a two-photon / photon-in-field event. This doc carries the single-electron traveler with the partner accounting flagged at every charge/momentum row (it is **NAMED UNKNOWN #2**, §2 + §5). Do not read the traveler as "one photon in, one electron out, nothing else."
- **Ledger delta:** `+E_γ` energy, `+p_γ` momentum, `0` charge, `0` net helicity (a linearly-polarized photon) or `±h` (a circularly-polarized photon — the handedness seed).

### OP-1 — FOCUS: self-lensing (achromatic gradient regime)

- **Inputs:** the photon from OP-0; the cell's `c_eff(A)` gradient response.
- **Operation:** the photon self-focuses via the Axiom-4 varactor-bias mechanism — a local amplitude gradient modulates `c_eff`, bending the ray toward higher amplitude (self-lensing). This is the **gradient regime**: smooth, **achromatic** (the lensing is a refractive-index gradient, frequency-independent), **reversible**, and **`∮ = 0`** by construction (the 2026-06-09 wrong-regime lesson — a sub-yield gradient effect cannot rectify or commit).
- **Regime/conditions:** sub-yield, linear-to-large-signal; MODE = the propagation sector; PHASE-STATE = compliant. Per `ave-regime-phase-state-check`: nothing irreversible can happen here — this step only concentrates the field.
- **QC gate:** focal amplitude `A²_focal` rising above the linear background. **Measurable:** peak `|field|²` at the focus (PML-excluded, density-peak sampled — not centroid, per Rule 10). **Instrument floor:** the prior-art rarefaction runs reached `A²_focal = 0.05` (deep linear, sub-yield) — the floor below which the focus has not left Regime I (cavprobe result §3, citing the counter-propagating-beam prior art).
- **Failure modes:** none unique to this step in the arc — self-lensing reproduces as the genesis precursor. The risk is **stalling sub-yield** (the prior-art beams stalled at `tr_min = −0.26` because the focus never left the linear regime, not because focusing failed — cavprobe §3, flag-don't-fix).
- **Ledger delta:** energy redistributed (concentrated), conserved; no partition yet.

### OP-2 — CLOSE-THE-LOOP: open path → closed `O₁` ring (**NAMED UNKNOWN #1**)

- **Inputs:** the focused, propagating photon (an OPEN path); the self-generated amplitude structure from OP-1.
- **Operation:** the open propagating path must become a **closed `O₁` (unknot) vortex ring** — the topological event that turns a travelling wave into a bound circulating loop. This is the step with **no mechanism in the corpus.** Candidates, listed honestly and NOT resolved (parameterized, per the hard constraint):
  1. **Reflection-closure off the self-generated wall** — the photon saturates the cell ahead of it, forms a moving `Γ=−1` wall, and reflects back onto its own tail (the "reflected into existence" picture, arc doc `:104`). *Status: the moving-`Γ=−1`-boundary self-trap reproduces the "2" carrier in one engine (`historical-precedents.md:28` verdict II) but the loop-closure as a topological event is not demonstrated.*
  2. **Capture by the partner/seed region** (pair-production canon): the loop closes because the e⁺e⁻ pair is co-created at a saturated node and the two rings are born already-closed and counter-rotating (`clm-ezai5b`, Vol 9 `ch02:85`).
  3. **Helicity re-orientation under confinement** — the photon's spin angular momentum re-projects into a poloidal circulation when the propagation direction is bent past 90°.
- **Regime/conditions:** the transition Regime I → III; this is where "open" becomes "bounded" — i.e. where a **container** first exists (the vapor-lock framing doc's container principle: *"pressure needs to be bounded by a container"* — without a closed loop / wall there is no container, and the longitudinal pressure cannot stand).
- **QC gate:** loop topology — is the path closed? **Measurable:** the winding/linking of the field streamlines (a closed `O₁` has a defined enclosed circulation `Γ_circ = ∮ v·dl ≠ 0`); the longitudinal `V_inc` becoming non-zero (a container now bounds it). **Instrument floor:** `max|V_inc|` vs the float64 machine-precision floor — genesis-23 measured this at exactly `0` (below ~1e-16), the decisive null.
- **Failure modes — genesis-23 (no container):** mapped HERE. Branch `analysis/2026-06-09-reflection-genesis-23` @ `ca991999` (arc doc `:117-119`): the `(2,3)` does **not** self-assemble from a transverse photon — **`max|V_inc| = 0` to machine precision across every config** (soft/hard wall, explicit/implicit, EMF reciprocal ON/OFF). The longitudinal `(V_inc, V_ref)` phase-space is **unpopulated** — *"the '3' never enters phase-space, so there is nothing to wind."* The container-principle reading (vapor-lock doc §2): **no closed loop formed → no container → no standing longitudinal pressure → `V ≡ 0`**. This is the OP-2 QC gate firing: the loop did not close, so the run had nothing to wind. **This is a retro-explanation, not a prediction (tagged hypothesis-class).**
- **Ledger delta:** if the loop closes, `Γ_circ` becomes a conserved invariant (energize-and-lock, `ch17_engine_requirements.tex:71`); no energy partition yet, but the conserved topological charge slot opens.

### OP-3 — RAREFY: circulation drops core density toward `ρ̄_cav` (the DRIVE step)

- **Inputs:** the closed `O₁` ring with conserved circulation `Γ_circ`; the cell's bulk EOS.
- **Operation:** the ring's own circulation produces a centrifugal pressure deficit that **rarefies the core** — the bulk density `ρ̄` at the ring axis drops toward the **cavitation floor `ρ̄_cav = −1/φ ≈ −0.618`**, the `c_bulk² = 0` root of the candidate EOS `c_eff²(ρ̄) = c₀²(1 + ρ̄/(1−ρ̄²))` (AVE-Propulsion `vol_propulsion/chapters/04_superluminal_transit.tex:86,89` — **CANDIDATE-CLAIM, NOT Core-canonical**). This is the **drive step** in the locked-motor picture: the conserved circulation is energized (driven up) until the core stiffness collapses. The winding `(2,3)` is driven into the Cosserat-ω phase-space sector here, on its own independent carrier (never the A1 phasor — the genesis-24/crystal/graft-v2 double-count, arc doc `:143`).
- **Regime/conditions:** BULK volumetric-K sector; near-floor **rarefaction** regime; PHASE-STATE traverses compliant → tensile-failure. DYNAMICAL (`ρ̄` integrated by continuity, never an algebraic centrifugal formula — CP9).
- **QC gate (in-flight — the cavitation-core probe):** does a genuinely circulating core REACH `ρ̄_cav`? **Measurable:** deepest `ρ̄_core` vs `−0.618`, in **bulk-sector volumetric-strain coordinates** (phase-space-coordinate-check: the claim is a bulk-K tensile event, measure in `ρ̄`, not shear-Cartesian). **Instrument floor:** the apparatus clips — `rho_floor = −0.95` and `c2_floor` — swept 4× each way; depths to `≈ −0.93` are **clip-invariant** (physics), and the EOS zero-crossing reads `−0.61800` vs candidate `−0.61803` numerically. **Result (branch `analysis/2026-06-10-cavitation-core-probe` @ `b8143b7c`, `research/2026-06-10_cavitation-core-probe_result.md`):** a self-circulating core **REACHES and CROSSES `ρ̄_cav` at `M_edge* ≈ 0.75–0.8`**, decisively below the prior-art beam floor `−0.26`; the bulk stiffness collapses through zero into tension (`c_bulk²_core: +0.25 → −0.86, −2.78, −5.53` at `M=0.8/0.9/1.0`). The floor is **dynamically reachable** — this gate PASSES for the reach.
- **Failure modes — v3 fixed-phase slip, v4 no-payment runaway:** mapped HERE (the drive's winding-conversion sub-mechanism).
  - **graft-v3 (fixed-phase / fixed-axis slip):** the centrosymmetric **fixed-axis** chiral buckle `f_ω = −κ̃·∇×(g·V·h·x̂)` deposits a coherent x-axis circulation at high contour reliability but **no knot geometry-selects** (`w_tor=w_pol=0`, both chiral arms); `H_bel` is quadratic in ω, so a scalar handedness `h` carries net helicity `RH=LH≈−1.4×10⁻¹⁵` (arc doc `:147`). The drive points at a **fixed phase/axis** rather than tracking the ring — the knot never forms.
  - **graft-v4 (no-payment runaway):** branch `analysis/2026-06-10-graft-v4-photon-helicity` @ `f9447421`, `research/2026-06-10_graft-v4-photon-helicity_result.md` (PANEL VERDICT **C → LOCK-FAIL**). The full trilinear coupling `H = κ̃∫gV[w·(∇×ω)]` that would **conserve-and-transfer** the photon helicity 1:1 into the winding is **linear in each of V, w, ω ⇒ INDEFINITE (unbounded below) ⇒ the discrete dynamics PUMP and DETONATE** (the `deplete_RH` arm); the only stable rendering drops the back-reaction `f_w` — and then the photon is a **non-depleting chiral director that transfers ~none of its `−291` helicity** (result §6). *"The coupling that would CONSERVE-AND-TRANSFER the helicity is a pump; the coupling that is a stable lock does not transfer it."* The drive cannot pay into the winding without running away — **no payment**.
- **Ledger delta:** `−ΔKE_circ` from the source into circulation kinetic energy; bulk PE rises (the rim over-pressure); the partition fractions `{f_KE, f_trap}` open but are UNQUANTIFIED (named parameters, §2).

### OP-4 — FLASH: the strain-snap phase change + latent-heat release (the energy-budget anchor)

- **Inputs:** the core at/below `ρ̄_cav` with collapsed stiffness (`c_bulk² ≤ 0`, tensile failure).
- **Operation:** the cavitation **phase change** — the bulk crosses from compliant-rarefied into a persistent tensile-failure void (liquid→vapor analog), releasing **latent heat** as the topology reorganizes. This is the **energy-budget anchor**: if (and only if) the latent heat of this transition equals `m_e c²` in the genesis direction, the YM mass gap would be **derived** rather than assumed (vapor-lock doc N6 — *payoff-if-true, unverified*).
- **Regime/conditions:** Regime IV (breakdown / "saturation phase transition", `ave-compactness-limit.md:28`); the irreversible commit (`τ_eq < τ_pump`).
- **QC gate:** is the crossing a discontinuous, irreversible, latent-releasing FLASH, or a smooth reversible LOCK? **Measurable (three FLASH signatures):** (i) stiffness collapse `c_bulk² → 0⁻`; (ii) an energy-partition **discontinuity** at the crossing (latent release); (iii) a **persistent** tensile-failure defect after de-energize (`pocket_cells_final > 0`, hysteresis). **Instrument floor:** the smooth-vs-step discrimination needs the energy ledger resolved below the dissipation noise floor (cavprobe: `L`-drift `0.044%` free / `≤3.5%` at high drive).
- **Failure mode — the FLASH does NOT occur (LOCK instead):** mapped HERE. The cavprobe found signature (i) PRESENT and robust, but **(ii) NEGATIVE** (the crossing is **continuous** — smooth KE↔PE exchange, no latent-release discontinuity at the `−0.618` crossing) and **(iii)/(iv) NEGATIVE** (**reversible**: de-spin recovers `−0.93 → −0.07`, `pocket_cells_final = 0`). Verdict: **LOCK (reversible pocket-compliance), NOT FLASH.** Decisive consequence (cavprobe §6, hypothesis-class): **the irreversibility a true vapor-LOCK requires is NOT in the bare `c_eff²(ρ̄)` EOS** — it needs *"an additional below-floor rupture / nucleation mechanism (a latent-heat term, a metastable-void nucleation, or a hardened `Γ=−1` wall that freezes the pocket) that the relation by itself does not encode."* **This step's mechanism is a NAMED UNKNOWN (the FLASH/latent-heat mechanism, §5).** Without it, OP-4 is a reversible dip, not a phase change — and the energy-budget anchor (latent-heat = `m_e c²`) has no carrier.
- **Ledger delta:** IF FLASH: `−L_cav` latent heat released (partition fraction `f_latent`); a persistent void forms. AS MEASURED (LOCK): the core rings and rebounds, energy sloshes KE↔PE reversibly, **no latent partition** — the budget's `f_latent` row is currently **0 in the canonical EOS** (the open mechanism would make it nonzero).

### OP-5 — LOCK: pocket compliance + BEMF payment + C3 latch (the ratified one-circuit)

- **Inputs:** the rarefied/committed core; the conserved circulation; the drive (photon energy still feeding).
- **Operation:** the **GRANT-RATIFIED (2026-06-10) locked-motor unification** — three components of **ONE circuit**, not three competitors. Verbatim (branch `analysis/2026-06-10-bemf-feedback-smoke`, `research/2026-06-10_bemf-feedback-smoke_prereg.md:10`, **uncommitted working-tree file** — cited by branch + working tree per verify-before-cite):
  > *"The locked-motor unification — **BEMF = the payment** (drive balanced by back-EMF at steady state), **cavitation pocket = the compliance**, the **C3 commit = the latch** — components of ONE circuit, not competitors."*
  The **BEMF is conservative/reactive (does NO net work)** — `P_V^BEMF + P_ω^BEMF = 0` exactly in the continuum: it **transfers reactively** between source (V, the capacitive buckle) and circulation (ω, the inductive BEMF) = the full reactive LC tank (`:49`). The pocket (OP-4) supplies the **compliance** (the C); the C3 commit (`2026-06-07_entrainment-vortex-trapping-deep-dive.md:309-310`) supplies the **latch** (the irreversible commit, `τ_eq < τ_pump`). The static FBD of §3 is **this step's hold condition**: at the lock, the radial force balance closes.
- **Regime/conditions:** steady-state; drive torque balanced by BEMF torque (the torque balance, §3); `|L_ω|` flat (`d|L|²/dt ≈ 0`, `ch17:67`).
- **QC gate:** does the lock HOLD a conserved invariant (energize-and-lock) rather than PUMP it? **Measurable:** the payment ledger `|work_V + work_ω| / |work_ω|` (the reactive pair must cancel), and the `|L_ω|` saturation ratio across doublings vs a frozen tolerance. **Instrument floor:** the sign-probe measured payment-ledger closure at `≈ 2.7×10⁻⁸` (machine precision, well above any `±6.5%`-class floor, bemf prereg `:68`); the saturation STOP gate tolerance is `1.3` (graft-v4 `smoke_saturation`).
- **Failure modes — genesis-24 pump-detonation (the payment), the wrong-shaft lock (v4):** mapped HERE.
  - **genesis-24 (pump-detonation at the payment):** branch `analysis/2026-06-09-genesis-24-saturated-seed` @ `df1c3f78` (arc doc `:125-127`). The EMF channel is **non-conservative and AMPLIFIES** (`k4_cosserat_coupling.py:703`, its own docstring: *"this AMPLIFIES the runaway"*); the ledger fails (`H_drift = −6.3%`, `|L|` unbounded `2.7 → 43.4`) and the emit window **detonates** (`E_V → 6.8×10⁸`). This is the payment paid with a **pump**: you cannot pump a conserved quantity (`ave-conserved-vs-pumped`). The BEMF-as-payment ratification (above) is the FIX — a reactive transfer, not an amplifying pump.
  - **the wrong-shaft lock (v4 LOCK-FAIL at the latch):** the graft-v4 saturation lock **clamps the wrong DOF** — the runaway is a **GLOBAL rigid-body rotation (SEPARABLE)**, so the lock *"removes only the rigid-body"* rotation, not the internal winding (`result:137`); the STOP gate FAILS on every active lock-ON arm (doubling ratios `5.03/3.97/5.19` vs tol `1.3`, η-invariant — the *"linear-damper-against-a-growing-source"* signature). Locking the rigid shaft does not lock the knot.
- **Ledger delta:** at a successful lock: `+E_trap` (the trapped reactive standing energy = mass, `f_trap`); the drive/BEMF pair nets zero work; the latch makes `Γ_circ` + the topological charge permanent.

### OP-6 — SETTLE / QC: the phase-space read (final inspection)

- **Inputs:** the locked ring (if OP-5 held).
- **Operation:** read out the four product specs in their **correct coordinates** (representation-capability-check):
  1. **`(2,3)` winding** — Park-projected along the field contours in `(V_inc, V_ref)` **phase space** (resolution-gated; the real-space `O₁` ring is NOT where the `(2,3)` lives).
  2. **charge = helicity sign** — `H_bel = ∫ω·(∇×ω)` sign (the Beltrami helicity).
  3. **mass = trapped energy** vs `m_e c²` (the `f_trap` standing energy).
  4. **α = the slip** — the mirror's residual transparency (`Q = α⁻¹`).
- **QC gate:** all four specs in tolerance. **Measurable + instrument floor:**
  - `(2,3)`: contour reliability `rel > 0.5` and `alias_clean = True` — graft-v4 found the de-novo RH/LH contours **`alias_clean = False`** (the `w_tor=4` read NOT internally validated); only the poloidal sub-read was clean, and **it does not geometry-select from a director source** (`result:185`).
  - mass: `E_trap` finite vs `m_e c² ≈ 511 keV` — the crystal-engine closed the latent-heat=mass ledger leg (`E_V = 149.3`, finite, manifestation-class, arc doc `:139`).
  - **α (the slip) — QC gate is HONEST about contamination:** the leak observable is **currently dispersion-contaminated** per the apparatus-floors verdict (branch `analysis/2026-06-10-apparatus-floors` @ `a0d7dbb8`); `Q_dyn` scatters `[41, 1181]` across `(N, steps)` and the joint-ledger guard **REFUSES** the single-run `Q_dyn=113` fluke (arc doc `:139`). **This gate cannot currently pass — the α leak is not cleanly separable from numerical dispersion.**
- **Failure mode — the `(2,3)` does not self-assemble:** across genesis-23/24, crystal, graft-v2/v3/v4 the de-novo `(2,3)` never closes; the residual is **mode-selection** (the winder primitive). This is the final-inspection reject that has held throughout the arc.
- **Ledger delta:** if all gates pass: the product is one electron — `m_e c²` trapped, `−e` charge (helicity sign), `ℏ/2` spin (conserved, energized-and-locked), `α` slip. **No genesis claim currently stands** at this gate.

---

## §2 — THE ENERGY / CHARGE / MOMENTUM BUDGET

**Answer to "do we need energy accounting?": YES — and the accounting is the discriminator.** Below, every partition fraction the corpus does not pin is named as a **parameter** (not a number), so the budget is a constraint, not a claim.

### §2.1 — Energy partition

Input photon energy `E_γ` partitions across four bins; the fractions sum to 1 but are individually **UNQUANTIFIED**:

```
E_γ  =  f_latent · E_γ     (pocket latent heat, OP-4)      ← currently 0 in the bare EOS (LOCK not FLASH)
     +  f_KE · E_γ          (circulation KE, OP-3)          ← the conserved-circulation store
     +  f_trap · E_γ        (trapped reactive standing E)   ← = mass; crystal-engine: E_V finite (manifestation)
     +  f_rad · E_γ          (radiated remainder / recoil)   ← carried off + to the partner (NAMED UNKNOWN #2)
```

| bin | parameter | what it is | current corpus status |
|---|---|---|---|
| pocket latent heat | `f_latent` | latent heat of the cavitation phase change | **0** in the canonical EOS (cavprobe: LOCK, no latent release); nonzero only if the OP-4 mechanism exists |
| circulation KE | `f_KE` | kinetic energy of the conserved `Γ_circ` | conserved (energize-and-lock); set once by the drive |
| trapped reactive | `f_trap` | standing reactive energy = rest mass | finite + manifestation-class (crystal `E_V=149.3`); fraction of `E_γ` UNQUANTIFIED |
| radiated/recoil | `f_rad` | remainder radiated + recoil to partner/seed | UNQUANTIFIED; couples to the partner question |

### §2.2 — The threshold question (why exactly `m_e c²`?) — the circularity, defused honestly

Two canonical statements bear on "why `m_e c²`":

1. **The YM per-cell energy ceiling** (Vol 9 `ch02:37,59`): `B_snap²/(2μ₀) = m_e c² / ℓ_node³` — *"energy density = rest energy per cell."* The substrate's saturation ceiling per cell IS one electron rest energy. This is the cleanest "why `m_e c²`": it is the energy at which one cell's compliance is exhausted.
2. **The `ℓ_node = ℏ/(m_e c)` circularity** (`constants.py:238`; CLAUDE.md calibration note): `ℓ_node` is **defined from `m_e`**, and `m_e` is one of the **calibration inputs** `{m_e, α, G}` (`constants.py:114,128-131`; CLAUDE.md:60). So statement 1, `m_e c²/ℓ_node³`, is **`m_e c²` expressed in units built from `m_e`** — it is **not an independent derivation of the threshold from below.** The YM mass gap is, in the corpus's own words, *"the rest energy of the **assumed** lightest topological defect, NOT a derived consequence"* (`yang-mills-steps1-2.md:10`, via vapor-lock doc §6).
   - **Defused honestly:** the traveler does **not** claim `m_e c²` is derived. It is the **calibration anchor**. The genesis-direction payoff — IF the OP-4 latent heat equals `m_e c²` (vapor-lock N6) — would convert the assumed gap into a derived one, but that is **untested** and is itself an open mechanism (OP-4). Until OP-4 has a mechanism, "why `m_e c²`" reduces to "because `m_e` is the calibration input that defines the cell."

### §2.3 — The charge ledger (where the opposite handedness goes — **NAMED UNKNOWN #2**)

`charge = helicity sign` (the `(2,3)` winding sense). A single electron carries `−e`; charge conservation from a neutral photon requires the conjugate `+e` to go **somewhere**. The **pair-production canon** is the binding constraint (Vol 9 `ch02:85`, `clm-ezai5b`):

> at `E = E_S`, `A² → 1` at adjacent A/B K4 nodes, `Γ → −1` TIR walls form, `c_local → 0`, and *"the blocked longitudinal kinetic energy shatters sideways into two contra-rotating Beltrami vortices — the electron-positron pair, each of mass `m_e`, with parity forcing one LH + one RH outcome."*

So the opposite handedness is the **positron partner**, co-created. The open question for the single-electron traveler: in OP-2/OP-5, **is the partner ring co-manufactured (the canon), or is the conjugate charge absorbed by a seed region / the apparatus?** The traveler cannot make a lone electron without resolving this — the charge ledger does not balance otherwise. (This is the same partner question flagged at OP-0.) `H_bel` flips sign cleanly with seed helicity in every engine (genesis-24 `−78/+78`, crystal `+8.22/−9.47`) — but that is the **carried** helicity provenance, not emergent knot-charge; the de-novo charge has never closed.

### §2.4 — Momentum / recoil row

Photon momentum `p_γ = E_γ/c` must balance: `p_γ = p_ring + p_partner + p_rad`. A closed `O₁` ring at rest carries zero net linear momentum, so either the partner carries the recoil (pair-production canon: two contra-propagating rings), or a third body (seed/apparatus) absorbs it. **Unquantified; couples to NAMED UNKNOWN #2.** The conserved angular momentum is separate: `ℏ/2` spin is the energized-and-locked topological helicity (`Γ_circ`), never pumped.

---

## §3 — THE FREE-BODY DIAGRAM (the locked-annulus wedge)

**Answer to "Enhance free body diagram?": YES — here is the static hold condition of OP-5, as both an ASCII diagram and a generated figure.** The FBD is the radial (+ axial + torque) balance on a wedge of the **locked annulus** — the wall of the real-space `O₁` ring between inner radius `r` (the cavitated pocket boundary at `ρ̄_cav`) and outer radius `R` (the saturation wall).

### §3.1 — Labeled ASCII diagram

```
                      P_wall  (Γ=−1 saturation wall reaction, INWARD at r=R)
                        ↓↓↓
              ┌───────────────────────┐   ← outer radius R  (ρ̄ → ρ̄_wall, S→0)
            ╱   →→ T_hoop ←←  (circ.)   ╲
          ╱   ┌───────────────────────┐  ╲
        ╱    │   annulus wall (locked) │   ╲   →  ρ̄ v_θ²/r   (centrifugal load, OUTWARD)
       │     │                         │    │
       │     └───────────────────────┘     │  ← inner radius r
        ╲   ↑↑↑  P_pocket  (rarefied      ╱
          ╲      core, ρ̄ = ρ̄_cav = −1/φ ╱   ← the FOURTH object: bulk-K tensile pocket
            ╲    pushes OUTWARD, weak)  ╱       (NOT the Γ=−1 cavity, NOT R-P bubble)
              ╲___________________ ___╱
                     (ring axis)

RADIAL :  P_pocket·r  +  (ρ̄ v_θ²/r)·dV   =   P_wall·R  +  T_hoop      (net inward = net outward at lock)
AXIAL  :  ring self-tension balances toroidal curvature (the O₁ ring closes on itself)
TORQUE :  τ_drive  =  τ_BEMF        (locked-motor: drive paid by back-EMF, OP-5; net zero work)
```

- **`P_pocket`** at `r_inner`: the pocket is **rarefied** (`ρ̄ = ρ̄_cav = −1/φ`), so its absolute pressure is a **deficit** below ambient: `P(ρ̄_cav) − P₀ = ρ₀c₀²·[ρ̄ − ½ln(1−ρ̄²)] = −0.377 ρ₀c₀²` (computed in the §4 figure script). The pocket pushes outward only weakly — the deficit is what the wall + hoop must hold against the centrifugal load.
- **`P_wall`** at `r_outer = R`: the `Γ=−1` saturation-wall reaction (`S(ρ̄) = √(1−ρ̄²) → 0`). A boundary condition (Op17-bounded), **never a bulk force** (`ch17:40`, the CP10 boundary-not-bulk requirement — the genesis-24 detonation was exactly the bulk-force leak).
- **`T_hoop`**: circumferential hoop tension from the conserved circulation — net inward.
- **centrifugal load** `ρ̄ v_θ²/r`: outward, from the ring's rotation.
- **torque balance**: `τ_drive = τ_BEMF` — the locked-motor's reactive payment (OP-5).

### §3.2 — Generated figure (data-derived labels)

`research/figures/electron_mfg_fbd.png` (generated by `src/scripts/vol_1_foundations/electron_mfg_fbd_figure.py`, canonical constants only). **Left panel:** the wedge with the four labeled contributions and the data-derived `ρ̄_cav = −0.6180` + pocket deficit `0.377 ρ₀c₀²`. **Right panel (the §4 result, made visual):** `R/r` as a **continuous curve** vs the outer-wall density `ρ̄_wall` (the missing 2nd boundary condition); the Golden-Torus `φ² = 2.618` is a single horizontal line, crossed only at the **non-canonical** `ρ̄_wall ≈ 0.440` — the canonical landmark walls (`+1/φ`, `+1/φ²`, `+0.5`) land at `3.21`, `2.46`, `2.79`, **none on `φ²`**.

---

## §4 — THE FORWARD `R/r` DERIVATION (the φ-link closure candidate)

**This is the `ave-fundamental-ground-up-implementation` case** (§4 IS its instance): rather than defer the `R/r` value as engineering-choice, the forward radial balance is attempted from canonical constants. **The discipline gate (`ave-live-fire-derivation-provenance`) was run live** — the numeric check `src/scripts/vol_1_foundations/electron_mfg_rr_balance.py` does the dead-input and forward-vs-fit residual tests. **The result is reported in its frozen bin without debugging toward `φ²`.**

### §4.1 — The forward setup (no target in the loop)

From the §3 radial balance, with the barotropic EOS `c_eff² = dP/dρ` and `ρ = ρ₀(1+ρ̄)`, the radial momentum balance `dP/dr = ρ v_θ(r)²/r` becomes a 1st-order ODE in `ρ̄(r)`. Two ingredients are **canonical / candidate-canonical**:

- **Inner boundary (DERIVED, parameter-free):** `ρ̄(r) = ρ̄_cav`, the `c_eff² = 0` root of the candidate EOS. The script solves `ρ̄² − ρ̄ − 1 = 0` from the EOS (not asserting `−1/φ`) and confirms the negative root `= −0.6180339887498948 = −1/φ` to machine precision (`|diff| = 0`), with the clean identity `1 − ρ̄_cav² = 1/φ`. **This part MATCHES — but it is an IDENTITY** (the root of the candidate EOS), not the `R/r` claim.
- **The balance integral:** for the `v_θ = c₀` closure (rigid lock at the trapped-photon speed — the only scale-free closure), `c₀²` cancels and `ln(R/r) = G(ρ̄_wall) − G(ρ̄_cav)` with `G(ρ̄) = −¼ln(1−ρ̄) + (5/4)ln(1+ρ̄) + ½/(1+ρ̄)` (partial-fraction antiderivative, verified in-script).

**Target in the loop?** No — `R/r` is computed forward from `(ρ̄_cav, ρ̄_wall, profile)`; `φ²` is imported **comparison-only** (`= R_GOLDEN_TORUS / R_GOLDEN_TORUS_MINOR`, `constants.py:200-201`) and never enters the balance.

### §4.2 — Live-fire result (dead-input + forward-vs-fit)

| outer-wall density `ρ̄_wall` | forward `R/r` (v=c₀ closure) | = `φ²`? |
|---|---|---|
| `+1/φ` (= `+0.618`, symmetric mirror of the floor) | **3.207** | no |
| `+1/φ²` (= `+0.382`) | **2.462** | no |
| `+0.5` | **2.795** | no |
| **back-solved to force `φ²`** | 2.618 | **only at `ρ̄_wall ≈ 0.440` — NON-canonical** |

**Forward-vs-fit residual test (the live-fire tell):** to land `R/r = φ²` the balance needs `ρ̄_wall ≈ 0.440`, which is **not** any canonical density (not `1/φ`, not `1/φ²`, not a saturation root `±1`, not the symmetric mirror). The forward calculation at canonical walls **misses `φ²`** (by `+22%`, `−6%`, `+7%`); hitting it **requires choosing the wall to make it appear** — the signature of a **FIT**, not a derivation. And the second closure (solid-body `v_θ = Ωr`, the cavprobe's actual config) does not even produce a scale-free ratio: it pins `(Ω²/2c₀²)(R²−r²)`, leaving `R/r` a free function of the edge Mach.

### §4.3 — VERDICT (frozen bin)

> ## **`R/r` = UNDERDETERMINED**
>
> The forward radial balance with the canonical inner boundary (`ρ̄_cav = −1/φ`) is **one constraint short of a pure ratio**. A unique `R/r` needs a **second independent canonical boundary condition** — the **outer saturation-wall density `ρ̄_wall`** — **AND** the **circulation/velocity-profile law `v_θ(r)`**. Neither is fixed by canonical constants. **No canonical pair tested lands on `φ²`**; forcing it needs `ρ̄_wall ≈ 0.440` (non-canonical) ⇒ fitted. **The φ-link between the cavitation floor and the Golden-Torus `φ²` is NOT closed by this FBD.** This is consistent with the vapor-lock doc's standing flag (§5.3): the `ρ̄²−ρ̄−1=0` floor and the `2R²−R−½=0` torus are the same golden quadratic in **physically unrelated constructions** (a bulk-stiffness zero vs a phasor-area embedding), and the link must not be cited as physics *"until one Axiom-4 derivation produces both roots in a single step."* That single-step derivation has not been done.

- **`rr_value`:** not a number — `R/r` is a function of `(ρ̄_wall, profile)`; `φ²(comparison) = 2.6180339887`.
- **Consistency-vs-emergence class:** the §4 outcome **cannot be graded emergence** — the inputs do not close the ratio. (The inner-BC `ρ̄_cav = −1/φ` IS a clean parameter-free **identity**, but it is the root of a **candidate-claim** EOS, and it is not the `R/r` claim.) Tagging the unclosed balance "emergence" would be the failure mode `ave-live-fire-derivation-provenance` exists to catch.
- **Coordinate check (`ave-representation-capability-check` + `phase-space-coordinate-check`) — UNADJUDICATED, flagged not asserted:** the coordinate-match between `R/r` and `φ²` is itself **not settled** (corrected from the prior over-claim of "coordinate-matched"). `constants.py:200-201` labels the Golden-Torus radii **real-space major/minor**, which — taken at face value — would make `R/r` (a real-space `O₁` ring major/minor ratio) coordinate-matched to `φ²`. **BUT** the cited vapor-lock doc §5.3 (commit `24cf3aa4`, `research/2026-06-10_matter-as-vapor-locked-pump_framing.md:118`) states the two roots are *"physically unrelated constructions (a phasor-area embedding vs a bulk-stiffness zero); the torus form only appears under a post-hoc `x = 2R` substitution"* — i.e. `φ²` may be a **phase-space (phasor-area) ratio**, in which case comparing it to a real-space hydrodynamic `R/r` is a coordinate **MISMATCH** (the never-conflate hard constraint: the real-space `O₁` ring vs the `(V_inc, V_ref)` phase winding). The `constants.py` "major/minor" wording may itself be a downstream re-labeling of the phasor-area construction. **This does NOT change the UNDERDETERMINED bin** — it strengthens "do not cite the φ-link." The real-space-vs-phasor-area provenance of `R_GOLDEN_TORUS` / `R_GOLDEN_TORUS_MINOR` is **surfaced to Grant for adjudication** (it sits in the same coincidence-magnet slot as U6). The `(2,3)` phase winding does **not** enter the radial balance regardless of how that adjudication lands.
- **The named input that closes it (the next derivation target):** the **outer saturation-wall boundary condition** — what density / impedance pins `r_outer` relative to `r_inner`. Equivalently: the circulation-profile law `v_θ(r)` that the locked ring obeys. Deriving *that* from Axiom 4 (the single-step both-roots derivation the vapor-lock doc names) is the gate that would move this from UNDERDETERMINED to a verdict.

---

## §5 — THE UNKNOWNS TABLE (what is still not physically clear)

Ranked by how hard each blocks the next electron-genesis build (**v5**). Owner ∈ {Grant adjudication, implementer derivation, in-flight workflow}.

| # | Named unknown (step) | What would resolve it | Blocks v5? | Owner |
|---|---|---|---|---|
| **U1** | **Close-the-loop mechanism** (OP-2, NAMED UNKNOWN #1) — open path → closed `O₁` ring; no corpus mechanism | A derivation/run picking among the 3 candidates (reflection-closure / partner-capture / helicity-reorientation); genesis-23 showed the loop did NOT close (`V≡0`) | **HARD** — no ring, no electron | implementer derivation + Grant (candidate selection) |
| **U2** | **FLASH / latent-heat irreversibility** (OP-4) — the bare EOS gives LOCK not FLASH; no below-floor rupture/nucleation/hardened-`Γ=−1` term | A new dynamical mechanism (latent-heat term OR metastable-void nucleation OR pocket-freezing wall) with its own verification chain (Rule 12 — new slot, not a refill) | **HARD** — without irreversibility the commit is a reversible dip; parametric runaway (the detonation arm) | implementer derivation (cavprobe localized it; in-flight = none yet) |
| **U3** | **Charge ledger / opposite-handedness partner** (§2.3, NAMED UNKNOWN #2) | Adjudicate: is the e⁺ partner co-manufactured (pair-production canon) or absorbed by a seed/apparatus? | **HARD** — charge + momentum do not balance for a lone electron | Grant adjudication + pair-production canon (`clm-ezai5b`) |
| **U4** | **Drive→winding conversion** (OP-3) — a bounded, depleting, helicity-conserving photon→winding coupling | The graft arc: a coupling that is neither indefinite (v4 pump/detonate) nor non-depleting (v4 director); the missing **winder primitive** + mode-selection | **HARD** — this is the localized residual the whole arc points to | in-flight workflow (graft arc) |
| **U5** | **`R/r` closure / 2nd boundary condition** (§4) — UNDERDETERMINED | Derive the outer saturation-wall BC (or `v_θ(r)`) from Axiom 4 — the single-step both-roots derivation | SOFT for v5 (geometry lock, not assembly); HARD for the φ-link claim | implementer derivation |
| **U6** | **The φ-link coincidence-magnet** (§4 / vapor-lock §5.3) — `ρ̄_cav` floor ↔ Golden-Torus `φ²` are the same quadratic in unrelated constructions | One Axiom-4 derivation that produces BOTH roots in a single step (until then: state the algebra, do not cite the link) | not a blocker — a coherence flag | implementer derivation + Grant |
| **U7** | **Wrong-shaft lock / which DOF the lock clamps** (OP-5) — v4 locked the rigid-body rotation, not the winding | A lock that targets the internal winding (non-separable from the `(2,3)`), not the global rigid rotation | MEDIUM — the lock must hold the right invariant | in-flight workflow (bemf-feedback / graft) |
| **U8** | **`ρ̄_cav` promotion** — CANDIDATE-CLAIM, Propulsion-tex-derived, **zero** KB/`constants.py` hits | Auditor promotion via the Vol-9 worklist (the cavprobe confirms it is the EOS root + dynamically reachable, but does not promote) | not a blocker — provenance hygiene | auditor lane (Vol-9 worklist) |
| **U9** | **Equilibration-slot adjudication** — 3 claimants (C3-gate, dark-wake [wobbly post wrong-regime walk-back], cavitation pocket) | Grant's call on which (or "both") occupies the irreversible-commit slot; the pocket is a competitor, NOT a default filler | MEDIUM — feeds U2/U4 | Grant adjudication |

**Ranking note:** U1, U2, U3, U4 are the four HARD blockers; any one of them open means v5 cannot manufacture a stable charged electron. U2 and U4 are the two that the in-flight probes have most sharply localized (cavprobe → U2; graft v3/v4 → U4). U1 and U3 are the two that need **Grant adjudication first** (mechanism selection / partner accounting) before an implementer run is well-posed — consistent with Rule 16 (ask before design).

---

## §6 — CROSS-REFERENCES (all verified this session; unpushed cited by branch+commit)

- **The candidate cavitation EOS + floor:** AVE-Propulsion `manuscript/vol_propulsion/chapters/04_superluminal_transit.tex:86` (`c_eff² = c₀²(1 + ρ̄/(1−ρ̄²))`), `:89` (`ρ̄` definition + "not a free parameter; derives from Axiom 4"). **CANDIDATE-CLAIM, Propulsion-derived, NOT Core-canonical.**
- **The cell datasheet (Vol 9):** `manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex:18,38,54` (datasheet stance + operating point); `02_absolute_maximum_ratings.tex:33,35,37,59,61,79,85` (`V_snap`, `E_S`, `B_snap`, the `ρ̄_cav` CANDIDATE row, pair-production mechanism); `07_saturation_characteristics.tex:24` (Axiom-4 kernel `S(A)`); `17_engine_requirements.tex:38,40,41,67,71` (the `c_eff(V)` / boundary-not-bulk / conserved-pair / energize-and-lock requirements).
- **The vapor-lock framing doc (in flight):** branch `analysis/2026-06-10-vaporlock-framing-and-tracker`, `research/2026-06-10_matter-as-vapor-locked-pump_framing.md` (committed @ `24cf3aa4`) — the container principle (§2), the FOURTH-object firewall (§4), the φ-link coincidence-magnet flag (§5.3), the three equilibration claimants (§5.2), the falsifiable surface (§9).
- **The cavitation-core probe (in flight):** branch `analysis/2026-06-10-cavitation-core-probe` @ `b8143b7c`, `research/2026-06-10_cavitation-core-probe_result.md` — floor REACHED at `M*≈0.8`, verdict **LOCK not FLASH**, irreversibility NOT in the bare EOS (§6).
- **The locked-motor ratification (in flight):** branch `analysis/2026-06-10-bemf-feedback-smoke`, `research/2026-06-10_bemf-feedback-smoke_prereg.md:10` (**uncommitted working-tree file** — cited by branch + working tree per verify-before-cite) — BEMF = payment, pocket = compliance, C3 = latch, ONE circuit; reactive `P_V+P_ω=0` (`:49`).
- **The genesis arc (failure-mode map):** `_orchestration/2026-06-09_ion-compression-rectifier-arc.md:104,117-127,139,143,147` — genesis-23 (`ca991999`, `V≡0`), genesis-24 (`df1c3f78`, EMF pump-detonation), crystal/graft-v2 (double-count fix), graft-v3 (fixed-axis no-knot); graft-v4 (`analysis/2026-06-10-graft-v4-photon-helicity` @ `f9447421`, LOCK-FAIL / wrong-shaft lock / no-payment runaway).
- **Canonical constants:** `src/ave/core/constants.py:199` (`PHI`), `:200-201` (Golden-Torus radii; `R/r = φ²`, `R·r = 1/4`), `:238` (`ℓ_node ≡ ℏ/(m_e c)`), `:114,128-131` (`m_e` calibration input); `manuscript/ave-kb/CLAUDE.md` (calibration inputs `{m_e, α, G}`).
- **The two-"3"s conflation flag (for the auditor lane):** `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md` (the Maxwell-Heaviside "longitudinal re-engages at saturation = the electron" note conflates the A1-dilatation MASS scalar with the Cosserat `(2,3)` WINDING — flagged, not edited here; KB-queue item per the vapor-lock doc).
- **The numeric check + figure (this doc):** `src/scripts/vol_1_foundations/electron_mfg_rr_balance.py` (the §4 forward balance + live-fire tests; JSON at `_output/electron_mfg_rr_balance_results.json`); `src/scripts/vol_1_foundations/electron_mfg_fbd_figure.py` → `research/figures/electron_mfg_fbd.png` (the §3/§4 figure).

---

*Disciplines fired, retroactive pass: `ave-fundamental-ground-up-implementation` (§4 attempted from canon, not deferred — verdict UNDERDETERMINED with the closing input named); `ave-live-fire-derivation-provenance` (§4 ran the code: dead-input + forward-vs-fit residual; the `ρ̄_wall≈0.440` fit-tell is the live-fire catch); `consistency-vs-emergence` (§4 outcome = cannot-grade-emergence; OP steps class-tagged); `ave-canonical-source` (numeric check imports `ave.core.constants` only); `ave-apparatus-floor-attribution` (every QC gate carries its instrument floor; OP-6 α gate honest about dispersion contamination); `ave-representation-capability-check` (real-space `O₁` ring vs `(2,3)` phase winding kept distinct; the FOURTH-object firewall held); `verify-before-cite` (every file:line grep-confirmed; unpushed cited by branch+commit, untracked by branch+working-tree); `ave-evidence-framing-discipline` + `flag-don't-fix` (the φ-link flagged not claimed; the two-"3"s conflation surfaced for the auditor, not edited).*

