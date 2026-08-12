[↑ Ch.3 Pin/Port Configuration](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Class B/C synthesis leaf — device equivalent-circuit schematics and port semantics. Consolidates canonical Vol 4 Ch 18 + three-impedance law + electron confinement; no new substrate primitive."
-->

## Device Circuit Models (canonical leaf)

Engineering datasheets for nonlinear components include an **equivalent circuit** — the smallest diagram capturing port behavior. For the substrate, that diagram is the K4-LC bond topology in EE symbols, not an imposed engineering fiction.

**Discipline:** Class B/C synthesis per `consistency-vs-emergence` v1.3. Every load-bearing statement cites a canonical leaf in Vols 1–6; this leaf is the **source of truth** for Vol 9 §Device Circuit Models. The LaTeX chapter (`manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex`) is the **manuscript render** (figures + `\kbleaf{}` pointers).

**Skills applied (2026-06-12 pass):** `verify-before-cite` v1.4 · `consistency-vs-emergence` v1.3 Step 8 · `ave-discrimination-check` (Q row) · `ave-canonical-source` (OP table) · `ave-ee-first-mapping` (EE-primary vocabulary).

> ↗ See also: [`bulk-impedance-at-saturation-boundary.md`](../../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md) — astrophysical $Z_{bulk}$ assignment; [`substrate-hysteresis-index.md`](../../common/substrate-hysteresis-index.md) §5b — LOOP GAP vs $\Omega_{\text{freeze}}$.

---

### 1. Universal vacuum cell (`AVE_VACUUM_CELL`)

**Classification:** Class B — consolidates Vol 4 Ch 18 SPICE subcircuit + Axiom 4 varactor/inductor projections into datasheet equivalent-circuit form.

Between any two substrate nodes **A** and **B**, the canonical nonlinear constitutive model is the `AVE_VACUUM_CELL` subcircuit.

| Element | Sector | Constitutive law | Canonical source |
|---|---|---|---|
| Metric varactor | Longitudinal-A1 | $C_{\mathrm{eff}}(V) = C_0/S(V)$, $S(V)=\sqrt{1-(V/V_{\mathrm{snap}})^2}$ (divergent $C_0/S$ = A1 bond compliance, knee at $V_{\mathrm{snap}}$; sector-keying fix 2026-07-03, `def-vyvsn1`) | [`nonlinear-vacuum-capacitance.md`:18](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) |
| Relativistic inductor | Magnetic | $L_{\mathrm{eff}}(I)$ rises as $\|I\|\to I_{\max}$; $dI/dt\to 0$ at cap | Same Axiom 4 kernel, magnetic projection |
| TVS / rupture | Transverse-T2 | $R_{\mathrm{eff}}=0$ at $\|V\|\ge V_{\mathrm{yield}}$ (the T2 yield wall — stays keyed on $V_{\mathrm{yield}}$) | Regime IV boundary |
| Memristor | Level 2 | $\tau_{\mathrm{relax}}=\ell_{\mathrm{node}}/c$ — `AVE_MEMRISTOR_S_STATE` / `AVE_VACUUM_CELL_L1` (**scaled** $\tau$ in ngspice; canonical SI in harness) | [`tau-relax-derivation.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md); [`substrate-hysteresis-index.md`](../../common/substrate-hysteresis-index.md) §5b |

**SPICE subcircuit:** [`spice-subcircuit.md`](../../vol4/simulation/ch18-universal-vacuum-cell/spice-subcircuit.md). Implementation: `src/ave/solvers/spice_models/ave_vacuum_cell.lib`.

**Linear comparison:** `AVE_VACUUM_CELL_LINEAR` (fixed $L_0$, $C_0$). Bench protocol: difference $S_{11}$ traces at identical excitation to isolate Axiom 4 effects.

**Figure (render):** `manuscript/vol_9_vacuum_datasheet/figures/circuit_vacuum_cell.tex` → Fig. `fig:vol9_circuit_vacuum_cell` in PDF.

---

### 2. Electron device — $\Gamma_{\mathrm{bulk}}=-1$ TIR-confined LC tank

**Classification:** Class B — EE device mapping of electron confinement; Class C for OP numeric scout rows (forward evaluation from canon + imposed $A^2$).

The electron is the substrate's smallest stable **device** in the EE register.

| Property | Assignment | Canonical source |
|---|---|---|
| Device class | Chiral Vacuum Reactor (CVR) / reactive port | `research/2026-06-11_chiral-vacuum-reactor-framing.md` (framing, not canon) |
| Confinement | $\Gamma_{\mathrm{bulk}}=-1$ at saturated knot core ($Z_{\mathrm{bulk}}\to 0$) | [`bulk-impedance-at-saturation-boundary.md`](../../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md) |
| **Not** EM short at $Z_0$ | Surrounding vacuum: $Z_{\mathrm{EM}}=Z_0$, $\Gamma_{\mathrm{EM}}=0$ (matched) | Three-impedance law; registry §3.11 |
| Tank elements | $L_{\mathrm{cell}}=\mu_0\ell_{\mathrm{node}}$, $C_{\mathrm{cell}}=\varepsilon_0\ell_{\mathrm{node}}$ | `constants.py`; Ch.4 DC primitives |
| Clock | $\omega_C = c_0/\ell_{\mathrm{node}}$ | Theorem 3.1 / Compton relation |
| Reactive store | $Q_{\mathrm{react}} = m_e c^2 \cdot \alpha$ | [`orbital-friction-paradox.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md):35 |
| Loss calibration | $Q_{\mathrm{tank}}\approx\alpha^{-1}$ when dark-wake loss engaged | **Consistency-class**; swept-gamma characterization |
| Topology overlay | $(2,3)$ phase-space winding; real-space $0_1$ unknot | Ch.11 topological characteristics |

**Figure (render):** `manuscript/vol_9_vacuum_datasheet/figures/circuit_electron_barrier.tex` → Fig. `fig:vol9_circuit_electron_barrier`.

**Figure (render) — the self-biased multi-port Q-point:** `manuscript/vol_9_vacuum_datasheet/figures/electron_selfbiased_multiport.tex` → Fig. `fig:vol9_electron_selfbiased_multiport`. Draws the [`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):133-147 Q-point resultbox as a real schematic: one external EM carrier port ($Z_{\mathrm{EM}}=Z_0$, matched) + the CHARGE port self-trapped at $V_{\mathrm{yield}}$ as a $\Gamma=-1$ shorted stub ($Z_{\mathrm{shear}}\to0$) + the MASS port sub-saturated at $A=\sqrt\alpha\approx0.085$ ($S\approx0.996$, energy scale $V_{\mathrm{snap}}$) + the $\mu_{\mathrm{eff}}\to0$ Meissner state (transduced, ~~`def-tk1xfm` provisional~~ **`def-tk1xfm` SOLID — ★Grant-ratified 2026-07-21**; *status-sync 2026-08-02, Rule 12 KEEP-BOTH — the prior status is struck, preserved, not deleted. The node's strength ceiling **STANDS**: "identity-by-translation, NOT emerges-from / NOT a derivation" — SOLID means the node is ratified/canonical, **not** that it derives a mechanism* — [`vocabulary-register.md`](../../common/vocabulary-register.md):441); self-biased (Axiom-4 self-saturation), self-stable ($R\!\cdot\!r=\tfrac14$). The per-port $V_{\mathrm{yield}}/V_{\mathrm{snap}}$ bias ladder is at [`cvr-dc-operating-point.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md):43-45. Consistency-class. **Small-signal per regime** (this A1 varactor keys on $V_{\mathrm{snap}}$, so $A\equiv V/V_{\mathrm{snap}}$; $A=1$ is $V_{\mathrm{snap}}\approx511$ kV, NOT $V_{\mathrm{yield}}$)**:** the large-signal chord/secant varactor $C_{\mathrm{eff}}=C_0/S$ vs the small-signal differential $C_{\mathrm{ss}}=\mathrm{d}Q/\mathrm{d}V=C_0/S^3$ (cold $A\to0$ $\to C_0$; sub-snap electron bias at $A=\sqrt\alpha$ i.e. $V=V_{\mathrm{yield}}$: $C_{\mathrm{ss}}\approx1.011\,C_0$; near-snap $A\to1$ i.e. $V\to V_{\mathrm{snap}}$: $C_{\mathrm{ss}}\to\infty$, the A1 completion, not the T2 yield wall) — the $S^3$ split rung-5-tested in the Ch.13 worked SPICE ladder.

#### Operating-point coefficients at the swept-$\gamma$ characterization point ($A^2 \approx 0.23$)

> **Which operating point (KEEP-BOTH — two distinct quantities, not a contradiction).** The $A^2 \approx 0.23$ table below is the **swept-$\gamma$ loss-characterization** operating point: an $m_ec^2$-calibrated *impose* from swept-$\gamma$ device characterization (driver docstring; $A \equiv V/V_{yield}$, so $V_{op}=\sqrt{0.23}\,V_{yield}=48\%\,V_{yield}$), used to forward-compute the datasheet nonlinearity slopes ($\mathrm{d}C_{eff}/\mathrm{d}A$, $\mathrm{d}\varepsilon/\mathrm{d}E$). It is a DIFFERENT quantity from the electron's **A1-mass-core static confinement bias** $A = V_{yield}/V_{snap} = \sqrt{\alpha} \approx 0.085$ ($A^2=\alpha\approx0.0073$; $S(\sqrt\alpha)=\sqrt{1-\alpha}\approx0.996$, deeply sub-saturated), which is the strain at which the standing electron's longitudinal-A1 mass channel sits inside the transverse-$T_2$ confinement cage ([`nonlinear-vacuum-capacitance.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):16; `def-vyvsn1`, Grant 2026-06-30). The two differ by ~31× in $A^2$ because they answer different questions: $A^2=0.23$ is a **device-characterization scout** (the amplitude at which the slopes are tabulated), $A=\sqrt\alpha$ is the **derived $\alpha$-echo static bias** (why the mass channel binds and does not run away). Both are consistency-class; kept distinct so neither is read as "the" electron operating point. (Provenance verified 2026-07-04: the driver's `A2_ELECTRON_OP=0.23` docstring states "from swept-gamma characterization"; the fork leaf derives $A=\sqrt\alpha$ from the $V_{yield}/V_{snap}$ ladder — genuinely two objects, the homonym pattern.)

Forward scout (`src/scripts/vol_1_foundations/operating_point_coefficients.py`; consistency-class; regenerate from driver; JSON `assets/sim_outputs/operating_point_coefficients.json`):

| Quantity | Value | Note |
|---|---|---|
| $A^2$ | $0.23$ | Regime II |
| $S(A)$ | $0.877$ | Sub-yield |
| $C_{\mathrm{eff}}/C_0$ | $1.140$ | Varactor active |
| $\mathrm{d}(C_{\mathrm{eff}}/C_0)/\mathrm{d}A$ | $0.710$ | Datasheet nonlinearity column |
| $Q$ (at $\gamma=\alpha\,\omega_C$) | $\approx 137$ | Loss carries $\alpha$ |
| $V_{\mathrm{op}}$ | $\approx 20.9$ kV | $48\%$ of $V_{\mathrm{yield}}$ |

**`ave-discrimination-check` — $Q \approx 1/\alpha$ row**

| Element | SM-counterfactual | AVE-distinct? |
|---|---|---|
| Finite $Q$ from loss $\gamma$ | Any RLC tank with $Q = \omega L/R$ | Generic |
| Choosing $\gamma = \alpha\,\omega_C$ to land $Q \approx 137$ | Parameter fit to CODATA $\alpha^{-1}$ | **Consistency-class calibration**, not emergence |
| Dark-wake $\tau_{zx}$ loss feed | Not computed in scout driver | **Open emergence gate** |

**Verdict:** Do **not** promote $Q=1/\alpha$ as AVE-distinct confirmation. Report as definitional calibration pending real dark-wake loss path.

**PONDER-05 pointer (Ch.7 saturation bench):** per INVARIANT-S2 (`CLAUDE.md`), PONDER-05 at $V_{DC}/V_{yield}=0.687$ is a **quartz material VCC shape analog** (Class-II ceramic consistency), **not** a per-node vacuum-kernel falsifier at bench geometry. Vol 9 cites it as the canonical **kernel-shape** bench target; discrimination lives in Vol 4 falsification programme.

---

### 3. Three-channel boundary port

**Classification:** Class C — definitional channel assignments from registry §3.11; no new physics.

One physical saturation boundary = **three channel-specific** $\Gamma$ values (three-impedance law; canonical render at [`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):20-22 — the registry §3.11 source is `research/2026-06-10_field-symbol-registry.md`, a **NON-CANON DRAFT**, not the canonical anchor) — **⚑ COUNT SCOPE, 2026-08-05 (upgrade wave): the subject of this sentence is a *saturation boundary*, and as a count of THAT the "three" is incomplete by one.** The three rows below are the **three-impedance law**'s channels and that law is not re-counted here; the canonical $r_{\text{sat}}$ boundary carries **FOUR** channel views since 2026-08-05, the fourth being the Cosserat micro-rotation / wryness channel — see the COUNT SCOPE note directly below this table, which is the fuller statement and carries the certification status and the cross-grade fence:

| Channel | Impedance | $\Gamma$ at saturation / horizon |
|---|---|---|
| EM-transverse | $Z_{\mathrm{EM}}\equiv Z_0$ | $\Gamma_{\mathrm{EM}}=0$ (SYM gravity) |
| Shear / GW | $Z_{\mathrm{shear}}=\rho\,c_{\mathrm{shear}}$ | $\Gamma_{\mathrm{shear}}\to -1$ |
| Bulk-longitudinal | $Z_{\mathrm{bulk}}=\rho\,c_{\mathrm{bulk}}$ | $\Gamma_{\mathrm{bulk}}\to -1$ |

> **⚑ COUNT SCOPE, 2026-08-05 (upgrade wave) — this port renders THREE channels, and the boundary has FOUR.** The three rows above are the **three-impedance law**'s channels, and that law is **not re-counted here**: no record in this pass touches [`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md). What changed is the **saturation boundary**: the canonical $r_{\text{sat}}$ channel table now carries a **fourth row** — the **Cosserat micro-rotation / wryness** channel, [`port-register.md`](../../common/port-register.md) channel 4 — and at that boundary the fourth channel is **UNWALLED** — **not wall-free: its own wall is a $\kappa$-*amplitude* surface, which this DC *strain* bias does not reach.** Transport survives at full cold value: $S_\kappa$(wall) measured `1` **to every digit double precision carries** at physical gradients, with the ceiling reached only at the unphysical one-node gradient `qℓ_node = 1` — `0.999979916516139` at `ρ_bond = 1` and `0.998449148919932` at `ρ* = 9.7734`, the latter a `77×` larger deficit and the honest ceiling to quote ([`research/2026-08-05_srs-twist-coefficient_result.md`](../../../../research/2026-08-05_srs-twist-coefficient_result.md):318,:319,:320–323,:325; PR #890, Tier-2-verified). The $u\!\leftrightarrow\!\phi$ door rides the strain kernel and **closes**. **⚑ CERTIFICATION STATUS OF THE ROW THAT CLAUSE RIDES (standing print-certification rule, adopted 2026-08-05) — the door-closes clause is `ROW-NOT-CERTIFIED`.** The three load-bearing theorems of the strain-kernel wall row are **measured exact** — last-bond stiffness, residual $\lvert\Gamma_{LB}+1\rvert$ over `1680` swept harmonic points, spread over the whole beyond-wall grid, and the RHO-A$-$RHO-B separation all `0.0`, *not a tolerance* — while the discrete **row** is **`ROW-NOT-CERTIFIED`**, pending the named `G-RHO2` repair (`G-RHO2` gates the *off-limit* sensitivity only; the exact independence *at* the limit is `G-RHO` and passes at exactly zero) ([`research/2026-08-05_last-bond-kernel-collapse_result.md`](../../../../research/2026-08-05_last-bond-kernel-collapse_result.md):24,:27,:78). **Device-design consequence of the count, not of the law:** a boundary characterization that tags only EM / shear / bulk is **incomplete by one channel**, and the missing one is the channel that does *not* reflect. Sources: [`bulk-impedance-at-saturation-boundary.md`](../../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md) (row 4) and [`common/wall-taxonomy.md`](../../common/wall-taxonomy.md) §10.2. **⚑ CROSS-GRADE FENCE, NOT in the ruled text ([`2026-08-05-ruling-kernel-collapse-rescope.md`](../../../../_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md)`:10`–`:21`, PR #897, landed — checkable now; added by the doc lane 2026-08-05, and the omission at the ruling is routed to Grant):** *"the fourth channel is UNWALLED"* rides the **separate-kernel (L∞-across-grades)** member of an **open** fork — canon records the **cross-grade combine rule as underdetermined at $O(\alpha)$** ([`common/axiom-register.md`](../../common/axiom-register.md):190,:232); under **normalized-L2-across-grades** every grade rides ONE kernel and the fourth channel is **not** unwalled, and the primary receipt *"does not choose the member"* ([`research/2026-08-05_last-bond-kernel-collapse_result.md`](../../../../research/2026-08-05_last-bond-kernel-collapse_result.md):30). **A device-characterization plan that budgets for an un-reflecting fourth channel is therefore budgeting on one member of an open fork.** **The section heading, its `\label`, and the figure filename are identifiers, not claims, and are deliberately left unchanged.** **⚑ CURRENCY 2026-08-06 — WHICH RUN THIS QUOTES (doc-lane refresh pass).** The `ROW-NOT-CERTIFIED` state above is the **v1 run's** verdict and stands as that run's true measurement — `research/2026-08-05_last-bond-kernel-collapse_result.md`:24, *"`G-RHO2` FAILS on an injection point this lane sized wrong at freeze"*. **It is superseded as the CURRENT state:** the repair that v1's own §1.3 named — inject `k_0 = ε·ω·Z_1`, not `ε·k_cold` — has run, and TASK 2 is **`ROW-CERTIFIED`**. Read from the landed result document itself, not from a PR title: `research/2026-08-05_last-bond-g-rho2-rerun_result.md`:30, *"`G-RHO2` PASSES. TASK 2 of the last-bond lane is `ROW-CERTIFIED`."* — fitted exponent inside the **unchanged** v1 acceptance interval (PR `#902`, merge commit `b06cbeb1`). **What this does NOT do:** a certified **row** does not certify the **premise scan**, which stays `SCAN-NOT-CERTIFIED` with no bin adjudicated; and it licenses no compressed *"confirmed"* wording here — that stays docket-only. **⚑ FENCE RE-POINT, 2026-08-06 — this routing note now points at the v2 record.** The citable ruled text is the versioned re-issue [`2026-08-06-ruling-kernel-collapse-rescope-v2.md`](../../../../_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2.md):13–29, which **carries the cross-grade combine-member fence inside the ruled text itself**; the 2026-08-05 v1 record is preserved and gains a dated pointer to it. **The earlier *"the omission is at the RULING … routed to Grant for a possible re-issue"* language is RESOLVED — the re-issue happened**, so the fence is now carried AT THE RULING and no print site has to supply it. **Nothing about the physics moves:** the carve-out is still conditional on the per-grade (L∞-across-grades) member, and the cross-grade combine rule is still canon-OPEN. Delta declaration (three deltas from v1, all declared) and the CORRECTED engine-residence map: [`2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md`](../../../../_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md) C1/C2 — the engine codes the saturation amplitude **three** ways across two live functionals plus a separate objective, so *"the member the engine actually codes"* is over-broad; the carve-out's receipt is STRUCTURAL, not numerical.

**Device-design consequence:** $S_{11}$ at $Z_0$ measures EM channel only. Horizons and electron walls require channel tagging or multi-channel characterization.

**Figure (render):** `manuscript/vol_9_vacuum_datasheet/figures/circuit_three_channel_boundary.tex` → Fig. `fig:vol9_circuit_three_channel`.

---

### 4. Cascaded vacuum-cell string

**Classification:** Class B — wiring-topology synthesis; constitutive law unchanged per cell.

Macroscopic devices = wiring topologies of `AVE_VACUUM_CELL` instances, not alternate constitutive laws. Minimal string: **IN** — [cell]—[cell]—[cell] — **OUT** with $L_0=\mu_0\ell_{\mathrm{node}}$, $C_0=\varepsilon_0\ell_{\mathrm{node}}$, $Z_0=\sqrt{L_0/C_0}$ per cell.

Particle cores, coaxial rupture cavities, and PONDER stacks differ by **boundary conditions** and drive topology.

**Figure (render):** inline in `03a_device_circuit_models.tex` → Fig. `fig:vol9_cascaded_vacuum_line`.

---

### 5. LOOP GAP — manufacture closure pointer (2026-06-12)

**Classification:** Class B — routing synthesis; ties §3 three-channel table to genesis closure order.

Electron manufacture requires **bulk** $\Gamma_{\mathrm{bulk}}\to -1$ confinement (not EM $S_{11}$ at $Z_0$ alone), Compton-scale ring-up, conservative energize-lock, and Level-2 remanence ($\tau_{\mathrm{relax}}$ / zero-drive persistence). v10 discrete srs achieves partial CVR-SET under drive but **not** remanence; v11 targets P11 quiescence gate.

↗ [`loop-gap-electron-resonator-closure-doctrine.md`](../../common/loop-gap-electron-resonator-closure-doctrine.md); `research/2026-06-12_loop-gap-electron-resonator-synthesis.md` §3 audit matrix.

---

### 6. Graded Vacuum Impedance Network (FOUNDATION REPAIR — carries open gates)

**Classification:** Class C — CONSISTENCY re-expression of the three-impedance law (registry §3.11; `three-channel-impedances.md`) as a wired equivalent-circuit MODEL. Originates NO new substrate primitive. Documented as foundation repair carrying OPEN gates, not a solved framework.

The **graded vacuum impedance network** ([def-gv1net](../../common/vocabulary-register.md)) is the equivalent-circuit MODEL of the vacuum drawn as three WIRED reactance channels — one per substrate grade — coupled through a chiral circulator and terminated at confinement surfaces. It is a **CONSISTENCY re-expression** of the already-canonical three-impedance law ([`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md), registry §3.11), NOT a new substrate primitive. Per INVARIANT-N1 the network is the circuit MODEL of the medium, not a new substrate-object noun (the substrate-noun slot stays prose-only). This section is **foundation repair carrying open gates** (§6.5), not a solved framework.

#### 6.1 The three wired reactance channels

Each channel is one substrate grade. The impedances and saturation $\Gamma$ values are taken from the three-impedance law ([`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):20-22); this leaf ADDS the two-"3"s grade tag without renaming any channel.

> **↗ Node-constitutive layer (2026-06-19).** Beneath the EM channel's scalar cell pair sits the **per-DOF node-constitutive tensor** ([`per-dof-vacuum-node-circuit.md`](per-dof-vacuum-node-circuit.md)) — the reactive pair $(L_i,C_i)$ made diagonal in the three TRANSLATION DOF ($\mathbf u\to\mathbf E$, EM-translation sector). It is the node-level structure that lets the EM channel carry directional anisotropy (isotropic-achromatic vs deviatoric-birefringent vs high-$k$ cubic). It is a SEPARATE axis from this grade triple (per-DOF-translation ⊥ wave-channel-grade — do NOT collapse, seam-7) and touches neither the MASS-"3" nor the CHARGE-"3".

**Mixed impedance DOMAINS (units discipline — do NOT collapse to one unit).** The three channel values are NOT a single homogeneous set: only $Z_{\mathrm{EM}}\equiv Z_0$ is an **electrical** impedance ($\Omega$, V/A). $Z_{\mathrm{shear}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ and $Z_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0$ (at $K=2G$) are **mechanical/acoustic** impedances ($\rho\times$speed, Pa·s/m) — they are **NOT in $Z_0$ units** and are off from $Z_0$ by ~12 orders of magnitude and a unit change. Writing "$Z_{\mathrm{bulk}}=\sqrt2\,Z_0$" is a **mis-scope** (the exact electrical-vs-mechanical conflation that [`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):14,38 warns against — $Z_{\mathrm{shear}}$, $Z_{\mathrm{bulk}}$ are $\rho\times$speed, not $Z_0$). The canonical bulk value is $Z_{\mathrm{bulk}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0$ at $K=2G$ ([`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):22). The three channels are **co-equal in ROLE** (one wired reactance branch per grade) but live in **different impedance DOMAINS**.

| Channel | Grade | Impedance | $\Gamma$ at saturation | Two-"3"s tag |
|---|---|---|---|---|
| $Z_{\mathrm{EM}}$ | T2 transverse field | $Z_{\mathrm{EM}}\equiv Z_0=\sqrt{\mu_0/\varepsilon_0}\approx376.73\,\Omega$ | $\Gamma_{\mathrm{EM}}=0$ — **MATCHED / radiative PORT** | — (matched port, not a hair-sector) |
| $Z_{\mathrm{shear}}$ | deviatoric $G$ | $Z_{\mathrm{shear}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ | $\Gamma_{\mathrm{shear}}\to-1$ — CONFINED | **CHARGE-"3"** (Cosserat micro-rotation winding) ⚑ **CHANNEL-TAG CONFLICT (2026-08-07) — PENDING-GRANT; see the dated flag at the end of this leaf before citing this tag** |
| $Z_{\mathrm{bulk}}$ | dilatation $K$ | $Z_{\mathrm{bulk}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0$ at $K=2G$ (i.e. $c_{\mathrm{bulk}}=\sqrt2\,c_0$) — a MECHANICAL/acoustic impedance ($\rho\times$speed), **NOT** in $Z_0$ units | $\Gamma_{\mathrm{bulk}}\to-1$ — CONFINED | **MASS-"3"** (A1 dilatation) 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |

**Naming discipline (do NOT rename the channels).** Keep $Z_{\mathrm{EM}}$ named $Z_{\mathrm{EM}}$ — do **not** rename it to $Z_{\mathrm{transverse}}$: BOTH EM and shear are transverse waves, so "transverse" is ambiguous; $Z_{\mathrm{EM}}\equiv Z_0$ is the native label because $Z_0=\sqrt{\mu_0/\varepsilon_0}$ is a vacuum constant. Keep this three-grade wave-channel set DISTINCT from the coarser **Electric / Magnetic / Either** per-element constitutive tags of the `AVE_VACUUM_CELL` (§1) — those are a different (per-element constitutive) classification, not the wave-channel set.

**Two-"3"s grade tag (the AMENDMENT this leaf adds).** Per the two-"3"s disambiguation ([`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20, Grant-ratified): the **bulk** channel carries the MASS-"3" (the A1 Heaviside-excised longitudinal dilatation scalar — $m_e c^2$ = trapped acoustic compression energy), and the **shear** channel carries the CHARGE-"3" (the orthogonal Cosserat $(2,3)$ micro-rotation winding — charge = Beltrami helicity). $A1\perp T2$: the two grades are orthogonal, never wired into one shared $(V_{\mathrm{inc}},V_{\mathrm{ref}})$ phasor (the genesis-24 / $w_{\mathrm{pol}}=0$ double-count guard). The EM channel is the matched radiative PORT, **not** a hair-sector — it is how the interior couples to the far field, not where an observable lives (see the M, J, Q honest map, §6.4). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

#### 6.2 The confinement surface (Γ=−1 cage-wall, status OPEN)

The two CONFINED channels terminate at a **confinement surface** ([def-cf1srf](../../common/vocabulary-register.md)) — the $\Gamma=-1$ cage-wall $\partial\Omega$ where $Z_{\mathrm{core}}\to0$ ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):38,47-50). Its **shape is FORCED by topology** (the real-space body + the phase-space winding + the node-span) and is therefore **DERIVED, never posited-spherical** (Grant D4).

> **Status: OPEN.** The $\Gamma=-1$ TIR condition itself is canonical (clm-kezk9z; RUNG-1 T3.3 `sup-1ecv2m` — $\Gamma_{\mathrm{bulk}}$ crosses the OP2 gate by $A=0.95$, $\alpha$-FREE). What is **NOT** derived is the **shape-forcing chain**: no solved boundary-value problem produces the electron's surface from its $0_1$-unknot topology. The electron ($0_1$ unknot, single-node) and the proton ($6^3_2$ Borromean, multi-node — [`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):43-44) get DIFFERENT derived shapes; the proton single-vs-multi-node confinement is **UNADJUDICATED**.

> **Two coincident $\Gamma=-1$ walls — do NOT re-collide.** The confinement surface is the **A1 MASS wall** ($Z_{\mathrm{bulk}}\to0$, the impedance-short $\Gamma=-1$ of the Pauli/TIR derivation). It is numerically coincident with — but a **DISTINCT object** from — the **$\Gamma_{\mathrm{spinor}}=-1$** topological $2\pi\to4\pi$ stability wall of the T2 micro-rotation sector ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):89-94; $A1\perp T2$ per [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20, Grant-ratified). The electron carries BOTH; the confinement surface terminating the **bulk** channel is the MASS one only. Reading the two $-1$'s as one wall would wire the cage into the charge-winding and break the two-"3"s orthogonality.

#### 6.3 The chiral circulator (inter-tank non-reciprocal coupling, STATED-pending-engine)

The two sublattice TANKS (the bipartite A/B sublattices of the $I4_1 32$ chiral srs net) are coupled through a **chiral circulator** ([def-ch1crc](../../common/vocabulary-register.md)) — a **NON-RECIPROCAL inter-tank coupling** carrying the lattice chirality. It is the inter-tank element of the network schematic (§6.6 Fig. i), drawn as a circulator.

> **Status: STATED — pending the chiral-crystal engine.** The cubic-FDTD engine averages chirality out, so the non-reciprocity MAGNITUDE is not yet computed (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:243 AUDITOR_STATE note). This is a STATED frontier, NOT adjudicated and NOT available.

> **Do NOT call it "gyrator."** The reciprocal optical-activity **gyrator** ([def-0pt1ac](../../common/vocabulary-register.md) — the lossless reciprocal-Faraday polarization-plane rotator; the $\pm75.46°$/unit magnitude is an `ETA_ROT_PER_WRITHE` engineering decree, not a bankable transport) is a DIFFERENT element; "circulator" is reserved here for the non-reciprocal inter-tank coupling. The chiral circulator is also DISTINCT from the **per-particle** $S_{LR}\ne S_{RL}^*$ winding non-reciprocity (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:242), which is a single-instance scattering asymmetry of one bound resonator, not the inter-sublattice-tank coupling. (`open_ambiguity:true`, conflicting sites recorded in def-ch1crc.)

#### 6.4 The $\mathcal{M}$, $\mathcal{J}$, $\mathcal{Q}$ honest map (refuted bijection)

A seductive reading says the three boundary observables $\mathcal{M},\mathcal{J},\mathcal{Q}$ map one-to-one onto the three wave channels ("3 hairs = 3 channels"). **That clean bijection is REFUTED.** The honest structure is:

**HONEST map (what the corpus supports):**

| Observable | Where it lives | Channel | Note |
|---|---|---|---|
| $\mathcal{M}$ (mass) | bulk / A1 dilatation | $Z_{\mathrm{bulk}}$ | **FORCED** — three leaves converge ($m_e$=ground-state cutoff energy; the MASS-"3") |
| $\mathcal{J}$ (spin) | micropolar / Cosserat | (shear sector) | $\mathcal{J}$=FM-kink spin-½ |
| $\mathcal{Q}$ (charge) | micropolar / Cosserat | (shear sector) | $\mathcal{Q}$=Beltrami helicity |
| EM | matched radiative PORT | $Z_{\mathrm{EM}}$ | $\Gamma_{\mathrm{EM}}=0$ — **not a hair-sector** |

$\mathcal{J}$ and $\mathcal{Q}$ **CO-LOCATE in ONE sector** (the micropolar/Cosserat $(2,3)$ micro-rotation — the CHARGE-"3" of §6.1) — they are not two separate channels. EM is the matched radiative port (how the interior couples to the far field), not a fourth observable's home.

**REFUTED — the clean "3 hairs = 3 channels" bijection.** The evidence is that **two independent triples** exist and **NO leaf cross-identifies them**:

1. The **Stokes-dimension triple** (3D volume / 2D surface / 1D line $=\mathcal{M}/\mathcal{J}/\mathcal{Q}$) at [`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):19-23.
2. The **wave-channel triple** (EM / shear / bulk) at [`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):20-22.

These are **TWO INDEPENDENT AXES**. The Stokes axis counts integration dimensionalities of boundary integrals; the wave-channel axis counts substrate grades' wave impedances. No canonical leaf identifies "the 2D-surface observable" WITH "the shear channel," etc. **Hold the Stokes-dimension axis EXPLICITLY ORTHOGONAL to the wave-channel axis.**

> **Double-duty tell (register, do not resolve).** The SAME unproven Stokes-dimension triple ALSO props the $\alpha^{-1}=4\pi^3+\pi^2+\pi$ decomposition ($\Lambda_{\mathrm{vol}}\leftrightarrow\mathcal{M}$, $\Lambda_{\mathrm{surf}}\leftrightarrow\mathcal{J}$, $\Lambda_{\mathrm{line}}\leftrightarrow\mathcal{Q}$ — [`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):59-68; [`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):105). With $\alpha$ adjudicated **echo at the value level** ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):19), this Stokes triple is doing **double duty** — propping both the M/J/Q catalog and the $\alpha$-decomposition. That is a coincidence-magnet tell, not a confirmation. Registered, not resolved.

**$\Omega_{\mathrm{freeze}}$ is NOT a 4th hair — it is the global operating-point BIAS** (it sets $u_0^*$). Tagged **NOT-CLOSED**: the chain is a **back-fit** ($\alpha, G \to u_0^*$, the B2 re-scope), NOT a forward $\Omega_{\mathrm{freeze}}\to Q$ derivation; and the $\Omega_{\mathrm{freeze}}\leftrightarrow$electron-spin link is **research-only**. $\Omega_{\mathrm{freeze}}$ ties to $\mathcal{J}$ only at COSMIC scale ($\Omega_{\mathrm{freeze}}=\mathcal{J}_{\mathrm{cosmic}}/I_{\mathrm{cosmic}}$, [`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):97), not at electron scale.

#### 6.5 Forks and open gates

> **↗ Electrical-vs-mechanical projection-conflation map** (`research/2026-06-19_electrical-mechanical-projection-map.md`): the EM (Ω) ↔ mechanical (ρc) seams in this section are **NOT one artifact to dissolve** — 1 fixed units-conflation (`Z_bulk` mis-scope, #296) + 6 genuine distinctions the corpus holds. EM↔mechanical is a real impedance-DOMAIN boundary the ξ_topo transducer BRIDGES (units change), not a separation to resolve away; bulk↔shear is same-domain ($H_{\mathrm{couple}}$). The unified network buys HYGIENE, not a derivation; α stays echo. The 1.826-vs-2.582 ratio (seam 4) is OPEN pending Grant. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

**The Q slot stays EMPTY (strict anti-substitution).** The TARGET of the network is to derive the electron $Q$ from channel impedances + couplings (the **channel-impedance-mismatch $Q$**). That target is **NOT achieved**: the $\alpha$-free cold-cage Q is $\approx30.8$, **NOT** 137 (`src/tests/engine_acceptance/test_l3_mass_cage.py`:702-703; RUNG-1 T3.4b `sup-wuy333`). This is the corpus **clean NEGATIVE** corroborating that the corpus $Q=1/\alpha$ is an instance-baked ECHO ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):19, value-scoped; `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:72 $Q_{\mathrm{TANK}}=1/\alpha$ baked at the instance). **Preserve it. Do NOT refill the slot, do NOT narrate it away.** (Plotting more instruments does not escape the echo: every display reads the same baked $Q$ — [`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):21.)

> **Build-A SECOND clean negative + the loaded-$Q$ test is CIRCULAR (2026-06-19; do NOT re-pose).** The Build-A native ISOLATION eigensolver adds a second reported negative: the **intrinsic** electron mode is **lossless** (EM-port-closed ⇒ Hermitian ⇒ $Q\to\infty$, GATE2), and the isolation eigen-$Q\gg45$ is lossless-confined — **NOT** $137$, NOT $30.8$ (eigenmode-$Q$ ≠ ringdown-$Q$; `research/2026-06-19_electron-Q-coupled-network_result.md`). The $137$ is therefore re-attributed to the **LOADED/radiative** $Q$ ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) §"Amendment (2026-06-19, Rule 12)"), **not** the intrinsic resonator $Q$. The tempting follow-up — "derive the loaded $Q=1/\alpha$ from the EM-port admittance" — is **ADJUDICATED CIRCULAR (do NOT pose it):** the engine's radiative leak is literally `1.0 - alpha` (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:161 `gamma_mag_sq_leak`) = the instrument-echo trap, and the α-free edge-radiation answer is already the cold-cage $30.8$ negative — **no α-free path to $137$.** Slot stays EMPTY; **no new Build-B slot.** Full registry verdict: [`electron-bound-resonator-coverage.md`](../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md) §registry gate B.1.

**Conserved $H_{\mathrm{couple}}$ (the only allowed inter-grade coupling).** Grades may couple ONLY through a conserved (energize-lock, no-pump) Hamiltonian pair — one $H_{\mathrm{couple}}$, source + back-reaction, NEVER a shared $(V_{\mathrm{inc}},V_{\mathrm{ref}})$ phasor (the $A1\perp T2$ fence, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20; the energize-lock rule, [`ch17 index`](../ch17-engine-requirements/index.md):19). The live candidate is the **graft-v3 shear$\leftrightarrow$bulk $\chi$-source** — but it is **DEMOTED B$\to$C / unimplemented**: present as live-but-not-adjudicated, **NOT available**.

> 🔴 **UPDATE (2026-06-20, Rule 12 — the original status line above is preserved; this REVISES it to the PARTIAL).** The graft-v3 trilinear $\chi$-source is **no longer the only live Fork-A candidate**, and "NOT available" is now too strong: a **conservative skew-Hermitian circulator coupling EXISTS** (`research/2026-06-20_node-circulator-coupling.md`, **PR #321, verdict PARTIAL** — merged to `main`). It **escapes** the trilinear dead-end on all three failure modes — it does **NOT pump** (norm conserved to $1.1\times10^{-12}$/40k steps, no indefinite arm), is **NOT isolation** (Gate B: bulk-only load transfers 100 % into the empty shear winding — 50× the failed graft-v3 ~2 %), and is **NOT inert** (Gate C: acts on the poloidal winding, ON $\ne$ OFF). What it does **NOT** yet close: the **2-port skew is RECIPROCAL** (forward(bulk$\to$shear) $==$ reverse, RH $==$ LH — it *is* the optical-activity **gyrator** [def-0pt1ac], not a one-way router); **genuine chiral non-reciprocity needs the 3-PORT loop** (EM$\leftrightarrow$shear$\leftrightarrow$bulk, the EM/photon port as the 3rd leg — gauge-invariant loop phase $3\chi\theta_\chi$ flips with $\chi$ but the asymmetry is small, $1.75\times10^{-3}$); and the **non-reciprocity MAGNITUDE is IMPOSED** ($\theta_\chi,\tilde\kappa$ plugged) because the chiral-crystal engine averages chirality out (§6.3, [`cvr_model.py`](../../../../src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py):243). So the Fork-A coupling row reads **PARTIAL**: a bounded, lossless, winding-acting, helicity-transferring shear$\leftrightarrow$bulk coupling exists (form FORCED trivially), but it is an **ECHO at the non-reciprocity magnitude** — the same FORM-deriving / VALUE-importing verdict as the rest of the node (`common/form-deriving-value-importing.md`, PR #319 — merged to `main`). The skew generator's frequency-domain shadow is the §6.6 chiral-circulator $S\ne S^\top$ S-matrix; its 2-domain home is the explicit N-port (`src/scripts/vol_9_device/node_2domain_nport.py`, PR #320). $\alpha$-free throughout ($\tilde\kappa=6/5$, $\theta_\chi=2\pi\nu_{\mathrm{vac}}$, $\nu_{\mathrm{vac}}=2/7$).

**Two DIFFERENT coupling problems, because the channels live in different impedance DOMAINS (§6.1).** The mixed-domain distinction has a consequence for how channels couple:

- **bulk $\leftrightarrow$ shear** is a coupling **WITHIN the mechanical domain** (both $\rho\times$speed) — this is the inter-grade $H_{\mathrm{couple}}$ above (conserved, energize-lock; graft-v3 demoted, **but the skew-circulator PARTIAL now realizes it** — see the 🔴 2026-06-20 UPDATE above + PR #321).
- **EM (electrical, $\Omega$) $\leftrightarrow$ mechanical ($\rho c$)** crosses an impedance DOMAIN. Two ports in different units cannot be directly wired together; a domain-crossing coupling requires a **TRANSDUCER** (an electro-mechanical change-of-reference), not a direct wire.

> **Candidate-refinement (NOT asserted — ~~the transducer node is itself PROPOSED-not-ratified~~ the transducer NODE is now ratified SOLID, but the WIRE is still not asserted; status-sync 2026-08-02, see the banner below).** The corpus's candidate electro-mechanical bridge is the **TKI-transformer** ([def-tk1xfm](../../common/vocabulary-register.md)) — Axiom 2 (the Topo-Kinematic Isomorphism, $\xi_{topo}$ dictionary $u/$strain$\leftrightarrow E$, $\omega/$curl$\leftrightarrow B$) read as the ideal, lossless, gain-1, pole-less, invertible electromechanical change-of-reference. In ROLE it is exactly an EM$\leftrightarrow$mechanical transducer, so it is the natural candidate to sit on the EM$\leftrightarrow$mechanical coupling. **FLAG (do NOT assert):** (1) ~~def-tk1xfm is itself **`status:proposed`, awaiting auditor + Grant ratification — NOT yet canonical**~~ **def-tk1xfm is SOLID — ★Grant-ratified 2026-07-21** (`vocabulary-register.md`:441), and the co-equality it asserts is **REGIME-SCOPED** to below the band edge ($\omega\tau \ll 1$ / long-wave); *this sub-flag is DISCHARGED, and the ratification gate below with it — flags (2) and (3) are untouched and are what still withholds the assertion*; (2) it carries the strength ceiling *"identity-by-translation, NOT emerges-from / NOT a derivation"* (the `translation-circuit.md:660` piezo over-claim guard) — it transduces units losslessly, it does NOT supply a derived coupling MECHANISM or a pole; (3) the inter-grade DYNAMICS (poles, $Q$, the trap) live in the resonator $H(s)$, NOT in the transformer. So the TKI-transformer is offered here as the **candidate** electro-mechanical bridge, not an adjudicated wire — ~~it is gated behind def-tk1xfm ratification, and~~ *(that gate is DISCHARGED as of the 2026-07-21 ratification; struck 2026-08-02 per Rule 12, preserved not deleted — the candidate status is now withheld by flags (2) and (3), the strength ceiling and the resonator-$H(s)$ separation, NOT by the node's status)* the EM-port is in any case the matched radiative PORT ($\Gamma_{\mathrm{EM}}=0$), not a confined hair-sector (§6.4).

> **[Status-sync 2026-08-02 — `def-tk1xfm` proposed → SOLID. Rule 12 KEEP-BOTH: every prior status line above is struck in place and preserved, none deleted.]**
>
> **Status of this note.** Discharged-decision propagation of an already-ruled state — it adjudicates **nothing new** and asserts **no new wire**. [`vocabulary-register.md`](../../common/vocabulary-register.md):441 records `def-tk1xfm` as **SOLID — ★GRANT-RATIFIED 2026-07-21** (verbatim `[sic]`: *"ratify def-tk1xfm"*), with the prior *"proposed since PR #265 — GATED on auditor + Grant, NOT canon"* itself preserved there under Rule 12. Both sites in this leaf (the figure-render paragraph above and this candidate-refinement block) still read the pre-ratification status; they now match the register.
>
> **What ratification does and does not buy — quoted from the register so this leaf cannot inflate it.** The ratified package scopes the isomorphism as an *"EXACT, lossless, gain-1, pole-less, invertible **co-equality of the mechanical and electrical descriptions BELOW the band edge** ($\omega\tau\ll1$ / long-wave regime)"*, **regime-scoped**: at band-edge scales the distributed-in-bond (arccos TL) and lumped mass-spring descriptions book the delay differently and are no longer co-equal (`def-b0nd01` / `clm-bnd5rq`). And the register states the ceiling in its own words: *"The strength ceiling STANDS: 'identity-by-translation, NOT emerges-from / NOT a derivation' ... **SOLID means the node is ratified/canonical, NOT that it derives a mechanism.**"*
>
> **So the block's verdict is unchanged.** The TKI-transformer remains the **candidate** EM$\leftrightarrow$mechanical bridge, **not an adjudicated wire**. What changed is only *why* it is withheld: no longer the node's ratification status (discharged), but flags (2) and (3) — the strength ceiling and the fact that the inter-grade dynamics live in the resonator $H(s)$, not in the transformer. **Nothing is promoted from candidate to asserted here.**
>
> **⚑ FLAGGED, NOT FIXED (sibling stale-status sites, outside this lane's 8-item scope — flag-don't-fix).** The same pre-ratification status is still asserted at four vol4 sites, verified at HEAD by content: [`node-up-small-large-signal.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):84 and :300–301 (*"def-tk1xfm is `status:proposed`-not-ratified"*), and [`measurement-coupling-probe.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/measurement-coupling-probe.md):60 (*"which is **`status:proposed`-not-ratified**"*, citing `vocabulary-register.md:324` — itself a stale line cite; the node is at :435). Surfaced for routing as a vol4 status-sync follow-on, deliberately not edited here.

**Fork-A — isolation vs coupling (KEEP-BOTH discriminator).** Does the mass channel (bulk) couple to the charge channel (shear) via $H_{\mathrm{couple}}$, or is it galvanic isolation? **Both legs live:**

- *Isolation leg:* the measured $\omega\to V$ structural zero (the cold cage's $Q\approx30.8$ is a self-consistent isolated-tank number).
- *Coupling leg:* the graft-v3 $\chi$-source was demoted/unimplemented, **but the skew-Hermitian circulator now realizes a conservative, transferring coupling leg (PARTIAL)** — it escapes the trilinear pump/inert dead-end (4 gates PASS), with the 2-port reciprocal + chiral non-reciprocity needing the 3-port + magnitude imposed (🔴 2026-06-20 UPDATE above; PR #321).

*Signatures:* mode-splitting / avoided-crossing (coupled) vs free-crossing (isolated). *Quantitative handle:* does engaging $H_{\mathrm{couple}}$ lift the cold-cage $Q\approx30.8$ toward the **OBSERVED** electron $Q$ — **NOT** the baked 137 (which is the echo, not an independent target)?

**Fork-B — the chiral circulator (STATED-pending-engine).** The inter-tank non-reciprocal coupling (§6.3) is STATED; its magnitude needs the chiral-crystal engine. Held open, not adjudicated.

**TENSION-1 discriminator (OPEN, defined test).** Does the EM far-field reduce to the **matched-port projection of the interior micropolar winding** ($\mathcal{Q}$=micropolar, EM=antenna), or is there a **residual EM-channel charge DOF**? A defined test, resolvable in the coupled-network derivation, currently OPEN.

**Q two-integrals reconciliation (OPEN, likely closer named).** Charge appears as a **1D linking number** ([`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):20) AND as a **3D Beltrami helicity** $H_{\mathrm{bel}}$ ([`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). These are almost certainly two projections of ONE charge via the **helicity=linking identity** (Moffatt 1969) — but that identity is **NOT written down for the AVE case**. Registered as a reconciliation gate (likely closer noted), OPEN.

> **Full open-gate registry.** The 12-item open-gate registry for this network is hosted in the BoundResonator coverage matrix ([`electron-bound-resonator-coverage.md`](../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md)) under its A/B/C FORM-chord / VALUE-echo buckets (INVARIANT-S11 extend-don't-reinvent — no parallel registry is minted here).

#### 6.6 Figure slots — (i)-(iv) GENERATED (#309); (v) provisional

Slots (i)-(iv) are **GENERATED FROM THE LIVE ENGINE** (PR #309) — NOT hand-drawn,
NOT faked. The PNGs land in `manuscript/vol_9_vacuum_datasheet/figures/graded_network/`;
the driver is [`src/scripts/vol_9_device/graded_vacuum_network_figures.py`](../../../../src/scripts/vol_9_device/graded_vacuum_network_figures.py)
(kernels/constants/ratios IMPORTED from the engine, never hardcoded; deterministic,
byte-stable; `ALPHA` never imported into any figure path). Slot (v)
(confinement-surfaces) remains **provisional** pending Fork-B. **Do NOT fake the
provisional slot.**

| Slot | Figure | Status | Caption spec |
|---|---|---|---|
| (i) | `fig:vol9_graded_network_schematic` | **GENERATED (#309)** — `figures/graded_network/vol9_graded_network_schematic.png` | **Graded vacuum impedance network schematic** — three reactance branches ($Z_{\mathrm{EM}}$, $Z_{\mathrm{shear}}$, $Z_{\mathrm{bulk}}$) wired through the chiral circulator (inter-tank, §6.3) with confinement-surface terminations on the two CONFINED channels ($\Gamma=-1$) and the open matched port on $Z_{\mathrm{EM}}$ ($\Gamma=0$). Line-art, labelled with the LIVE channel numbers pulled from the engine ($c_L/c_T$ ratio, radiative floor, the $\Gamma$ map). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |
| (ii) | `fig:vol9_graded_network_smith` | **GENERATED (#309)** — `figures/graded_network/vol9_graded_network_smith.png` | **Per-channel Smith / impedance** — $Z_{\mathrm{EM}}$ matched at $\Gamma=0$ (origin of the Smith chart); $Z_{\mathrm{shear}}$ and $Z_{\mathrm{bulk}}$ trajectories running toward $\Gamma=-1$ (the short-circuit point) as $S(A)\to0$. Generated from the live varactor operator (`vacuum_varactor_scatter.py`, $Z_{\mathrm{bond}}=Z_0\sqrt{S(A)}$). |
| (iii) | `fig:vol9_forkA_discriminator` | **GENERATED (#309), isolated arm only** — `figures/graded_network/vol9_forkA_discriminator.png` | **Fork-A discriminator sweep** — $Q$ vs coupling strength. The **ISOLATED arm is real** (live engines): the graded-vacuum-network isolation eigensolver (intrinsic $Q\to\infty$) AND the $\alpha$-FREE cold-cage FDTD ringdown ($Q_{\mathrm{ringdown}}\approx30.8$, the canonical $N{=}72/6000$ anchor — annotated NOT 137, the baked echo). The **COUPLED-arm mode-splitting / avoided-crossing is honestly DEFERRED-pending-$H_{\mathrm{couple}}$** — it is the coupled-eigensolve (Build-B, not yet built per PR #308), drawn only as a dashed SCHEMATIC placeholder, NOT computed, NOT faked. |
| (iv) | `fig:vol9_graded_network_op_sweep` | **GENERATED (#309)** — `figures/graded_network/vol9_graded_network_op_sweep.png` | **Operating-point sweep** — channel impedances vs saturation $S$: $Z_{\mathrm{EM}}$ flat (matched), $Z_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0\to0$ and $Z_{\mathrm{shear}}\to0$ as $A\to1$ (plotted on the mechanical $\rho\,c$ axis, NOT against $Z_0$). From the live varactor map ($Z=Z_0\sqrt{S}$). |
| (v) | `fig:vol9_confinement_surface_shapes` | **PROVISIONAL** (pending Fork-B) | **Confinement-surface shapes electron-vs-proton** — the topology-forced $\Gamma=-1$ surface for the electron ($0_1$ unknot, single-node) vs the proton ($6^3_2$ Borromean, multi-node); proton single-vs-multi-node UNADJUDICATED. *Caption/spec only; to be generated by the Fork-B confinement-surface derivation.* |

---

### Verify-before-cite audit log (2026-06-12)

| Cited anchor | Verification |
|---|---|
| `orbital-friction-paradox.md`:35 | Grep: $m_e c^2 \cdot \alpha$ in reactive-shell row ✓ |
| `constants.py` | symbols `Z_0`, `RHO_BULK`, `G_VAC`, `V_LONG` ✓ |
| OP table numerics | `operating_point_coefficients.json` (driver run 2026-06-11) ✓ |
| Electron $\Gamma_{\mathrm{bulk}}$ not $\Gamma_{\mathrm{EM}}$ | [`electron-bh-isomorphism.md`](../../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):26 ✓ |

---

## ⚑ CHANNEL-TAG FLAG — shear vs Cosserat (dated 2026-08-07; SURFACED, NOT RESOLVED; PENDING-GRANT sector-ownership call)

**Placement note.** This block is an **EOF append** and the only edit above it is a one-token ⚑ marker inside the `:150` table cell — both deliberately **line-pin-neutral**, so none of the ~60 inbound `device-circuit-models.md:NN` cites (three of them inside `_prereg_FROZEN` docs) are rotted by this flag. The flag belongs beside the `:150` row; the marker carries the adjacency, this block carries the argument.

**The conflict.** The §6.1 channel table's shear row (`:150`) tags the deviatoric-$G$ channel ($Z_{\mathrm{shear}}=\rho\,c_{\mathrm{shear}}$) with the **CHARGE-"3" (Cosserat micro-rotation winding)**. The canonical port register carries those as **two DISTINCT channels with different physics**, not one:

- [`port-register.md`](../../common/port-register.md):48 — **channel 2**, *"Mechanical shear / GW"* ($T_2$ shear-$G$), $Z_{shear}=\rho\,c_{shear}$, $c_{shear}=c$, **GAPLESS** (*"gapless acoustic; edge"* $2c/\ell_{node}$); it is the carrier of the **observed GW** to the far field.
- [`port-register.md`](../../common/port-register.md):50 — **channel 4**, *"Cosserat micro-rotation / wryness"* (couple-stress $\gamma$-grade, the $(2,3)$ winding), $c_\kappa=\sqrt2\,c$, **GAPPED** (*"(gapped — see gap)"*; $m_\omega=\sqrt{4G_c/I_\omega}$, Yukawa reach $\sim\ell_{node}$).

**This row assigns channel 4's tag to channel 2's impedance.** The difference is physical, not clerical: **ch-2 is gapless and radiates at $c$; ch-4 is gapped and Yukawa-screened at $\sim\ell_{node}$.** Under the ch-4 reading the $(2,3)$ winding is confined **by the gap**. Under the ch-2 reading it rides the same gapless line the GW uses, and confinement must come from $\Gamma_{\mathrm{shear}}\to-1$ alone. Those are **different confinement stories for charge**, and this leaf asserts the second while the register asserts the first.

**Adjacent datum — surfaced because it is the likely ROOT, not because it settles anything.** The authority this leaf cites for the grade tag, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20 (the Grant-ratified 🔴 TWO-"3"s banner), itself calls the Cosserat winding *"T2 couple-stress"* — carrying **both** labels on one object ($T_2$ is the shear irrep; couple-stress is the ch-4 grade). So the conflation may be **inherited from the ratified line** rather than introduced here. Both readings are quoted verbatim; **neither is reframed to match the other.**

**NOT FIXED HERE.** No channel renamed, no tag moved, no row's physics edited. The sector-ownership question — *does the CHARGE-"3" own ch-2, ch-4, or a projection across both?* — is Grant's call. A twin flag is carried at `research/2026-06-20_node-2domain-nport.md` (the `shear-Cosserat` compound). **Until it is ruled, do not cite the `:150` grade tag as settling which channel the $(2,3)$ winding rides.**

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is byte-exact and is never reworded.

**Rows carried in this file.**

- **`:151`** — stamped at `:151`. *(family: Z_bulk=ρc_bulk formula)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  Z_bulk=ρ_bulk c_bulk=√2 ρ_bulk c_0 at K=2G (i.e. c_bulk=√2 c_0) — a MECHANICAL/acoustic impedance (ρ×speed), NOT in Z_0 units
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Canonical N-port formula site (also :101, :145); Γ_bulk→-1 CONFINED half survives; ρ×speed form consumes the phantom speed.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:155`** — stamped at `:155`. *(family: electron-sector label (past-wall))*  ⚑ **PAST-WALL**
  Quoted claim, byte-exact at HEAD:
  ```text
  the A1 Heaviside-excised longitudinal dilatation scalar — m_e c² = trapped acoustic compression energy
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Prereg-named electron-sector label class: 'trapped acoustic compression energy' → re-label at label level with past-wall scope declared; the anti-Heaviside physical-scalar content and the mass accounting survive re-homed on the bound field.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ PAST-WALL:** the content reaches past the saturation wall, a phase Axiom 5 explicitly does **not** write (its phase-structure paragraph puts the $D(A)\to\infty$ wall behaviour past-wall-adjacent and *not written here*, with the de-bonded and pre-freeze phase forms named-open). The demotion is therefore **scoped**: clause G resolves the cold, sub-yield side; the past-wall reading is neither discharged nor adjudicated here.

- **`:201`** — stamped at `:201`. *(family: two-speed seam ledger)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  The 1.826-vs-2.582 ratio (seam 4) is OPEN pending Grant.
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Ledger row recording the √(10/3)-vs-√2 speed incoherence as an open seam; under the carve neither is a propagation speed and the seam is explained/dissolved, not open — register re-read owed (prereg register-row class).
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:255`** — stamped at `:255`. *(family: figure spec consuming c_L/c_T; banked `uncertain`)*  ⚑ **BIAS-DEBT**
  Quoted claim, byte-exact at HEAD:
  ```text
  labelled with the LIVE channel numbers pulled from the engine (c_L/c_T ratio, radiative floor, the Γ map)
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Figure specification imports the P-wave ratio c_L/c_T (and a radiative floor whose channel is unstated) as live labels; re-route under the carve. Uncertain on which channel the radiative floor belongs to.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

