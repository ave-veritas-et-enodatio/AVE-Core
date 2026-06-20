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
| Metric varactor | Electric | $C_{\mathrm{eff}}(V) = C_0/S(V)$, $S(V)=\sqrt{1-(V/V_{\mathrm{yield}})^2}$ | [`nonlinear-vacuum-capacitance.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) |
| Relativistic inductor | Magnetic | $L_{\mathrm{eff}}(I)$ rises as $\|I\|\to I_{\max}$; $dI/dt\to 0$ at cap | Same Axiom 4 kernel, magnetic projection |
| TVS / rupture | Either | $R_{\mathrm{eff}}=0$ at $\|V\|\ge V_{\mathrm{yield}}$ | Regime IV boundary |
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

#### Operating-point coefficients ($A^2 \approx 0.23$)

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

One physical saturation boundary = **three channel-specific** $\Gamma$ values (three-impedance law; canonical render at [`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):20-22 — the registry §3.11 source is `research/2026-06-10_field-symbol-registry.md`, a **NON-CANON DRAFT**, not the canonical anchor):

| Channel | Impedance | $\Gamma$ at saturation / horizon |
|---|---|---|
| EM-transverse | $Z_{\mathrm{EM}}\equiv Z_0$ | $\Gamma_{\mathrm{EM}}=0$ (SYM gravity) |
| Shear / GW | $Z_{\mathrm{shear}}=\rho\,c_{\mathrm{shear}}$ | $\Gamma_{\mathrm{shear}}\to -1$ |
| Bulk-longitudinal | $Z_{\mathrm{bulk}}=\rho\,c_{\mathrm{bulk}}$ | $\Gamma_{\mathrm{bulk}}\to -1$ |

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

**Mixed impedance DOMAINS (units discipline — do NOT collapse to one unit).** The three channel values are NOT a single homogeneous set: only $Z_{\mathrm{EM}}\equiv Z_0$ is an **electrical** impedance ($\Omega$, V/A). $Z_{\mathrm{shear}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ and $Z_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0$ (at $K=2G$) are **mechanical/acoustic** impedances ($\rho\times$speed, Pa·s/m) — they are **NOT in $Z_0$ units** and are off from $Z_0$ by ~12 orders of magnitude and a unit change. Writing "$Z_{\mathrm{bulk}}=\sqrt2\,Z_0$" is a **mis-scope** (the exact electrical-vs-mechanical conflation that [`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):14,38 warns against — $Z_{\mathrm{shear}}$, $Z_{\mathrm{bulk}}$ are $\rho\times$speed, not $Z_0$). The canonical bulk value is $Z_{\mathrm{bulk}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0$ at $K=2G$ ([`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):22). The three channels are **co-equal in ROLE** (one wired reactance branch per grade) but live in **different impedance DOMAINS**.

| Channel | Grade | Impedance | $\Gamma$ at saturation | Two-"3"s tag |
|---|---|---|---|---|
| $Z_{\mathrm{EM}}$ | T2 transverse field | $Z_{\mathrm{EM}}\equiv Z_0=\sqrt{\mu_0/\varepsilon_0}\approx376.73\,\Omega$ | $\Gamma_{\mathrm{EM}}=0$ — **MATCHED / radiative PORT** | — (matched port, not a hair-sector) |
| $Z_{\mathrm{shear}}$ | deviatoric $G$ | $Z_{\mathrm{shear}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ | $\Gamma_{\mathrm{shear}}\to-1$ — CONFINED | **CHARGE-"3"** (Cosserat micro-rotation winding) |
| $Z_{\mathrm{bulk}}$ | dilatation $K$ | $Z_{\mathrm{bulk}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0$ at $K=2G$ (i.e. $c_{\mathrm{bulk}}=\sqrt2\,c_0$) — a MECHANICAL/acoustic impedance ($\rho\times$speed), **NOT** in $Z_0$ units | $\Gamma_{\mathrm{bulk}}\to-1$ — CONFINED | **MASS-"3"** (A1 dilatation) |

**Naming discipline (do NOT rename the channels).** Keep $Z_{\mathrm{EM}}$ named $Z_{\mathrm{EM}}$ — do **not** rename it to $Z_{\mathrm{transverse}}$: BOTH EM and shear are transverse waves, so "transverse" is ambiguous; $Z_{\mathrm{EM}}\equiv Z_0$ is the native label because $Z_0=\sqrt{\mu_0/\varepsilon_0}$ is a vacuum constant. Keep this three-grade wave-channel set DISTINCT from the coarser **Electric / Magnetic / Either** per-element constitutive tags of the `AVE_VACUUM_CELL` (§1) — those are a different (per-element constitutive) classification, not the wave-channel set.

**Two-"3"s grade tag (the AMENDMENT this leaf adds).** Per the two-"3"s disambiguation ([`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20, Grant-ratified): the **bulk** channel carries the MASS-"3" (the A1 Heaviside-excised longitudinal dilatation scalar — $m_e c^2$ = trapped acoustic compression energy), and the **shear** channel carries the CHARGE-"3" (the orthogonal Cosserat $(2,3)$ micro-rotation winding — charge = Beltrami helicity). $A1\perp T2$: the two grades are orthogonal, never wired into one shared $(V_{\mathrm{inc}},V_{\mathrm{ref}})$ phasor (the genesis-24 / $w_{\mathrm{pol}}=0$ double-count guard). The EM channel is the matched radiative PORT, **not** a hair-sector — it is how the interior couples to the far field, not where an observable lives (see the M, J, Q honest map, §6.4).

#### 6.2 The confinement surface (Γ=−1 cage-wall, status OPEN)

The two CONFINED channels terminate at a **confinement surface** ([def-cf1srf](../../common/vocabulary-register.md)) — the $\Gamma=-1$ cage-wall $\partial\Omega$ where $Z_{\mathrm{core}}\to0$ ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):38,47-50). Its **shape is FORCED by topology** (the real-space body + the phase-space winding + the node-span) and is therefore **DERIVED, never posited-spherical** (Grant D4).

> **Status: OPEN.** The $\Gamma=-1$ TIR condition itself is canonical (clm-kezk9z; RUNG-1 T3.3 `sup-1ecv2m` — $\Gamma_{\mathrm{bulk}}$ crosses the OP2 gate by $A=0.95$, $\alpha$-FREE). What is **NOT** derived is the **shape-forcing chain**: no solved boundary-value problem produces the electron's surface from its $0_1$-unknot topology. The electron ($0_1$ unknot, single-node) and the proton ($6^3_2$ Borromean, multi-node — [`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):43-44) get DIFFERENT derived shapes; the proton single-vs-multi-node confinement is **UNADJUDICATED**.

> **Two coincident $\Gamma=-1$ walls — do NOT re-collide.** The confinement surface is the **A1 MASS wall** ($Z_{\mathrm{bulk}}\to0$, the impedance-short $\Gamma=-1$ of the Pauli/TIR derivation). It is numerically coincident with — but a **DISTINCT object** from — the **$\Gamma_{\mathrm{spinor}}=-1$** topological $2\pi\to4\pi$ stability wall of the T2 micro-rotation sector ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):89-94; $A1\perp T2$ per [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20, Grant-ratified). The electron carries BOTH; the confinement surface terminating the **bulk** channel is the MASS one only. Reading the two $-1$'s as one wall would wire the cage into the charge-winding and break the two-"3"s orthogonality.

#### 6.3 The chiral circulator (inter-tank non-reciprocal coupling, STATED-pending-engine)

The two sublattice TANKS (the bipartite A/B sublattices of the $I4_1 32$ chiral srs net) are coupled through a **chiral circulator** ([def-ch1crc](../../common/vocabulary-register.md)) — a **NON-RECIPROCAL inter-tank coupling** carrying the lattice chirality. It is the inter-tank element of the network schematic (§6.6 Fig. i), drawn as a circulator.

> **Status: STATED — pending the chiral-crystal engine.** The cubic-FDTD engine averages chirality out, so the non-reciprocity MAGNITUDE is not yet computed (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:243 AUDITOR_STATE note). This is a STATED frontier, NOT adjudicated and NOT available.

> **Do NOT call it "gyrator."** The reciprocal optical-activity **gyrator** ([def-0pt1ac](../../common/vocabulary-register.md) — the lossless reciprocal-Faraday polarization-plane rotator, $\pm75.46°$/unit) is a DIFFERENT element; "circulator" is reserved here for the non-reciprocal inter-tank coupling. The chiral circulator is also DISTINCT from the **per-particle** $S_{LR}\ne S_{RL}^*$ winding non-reciprocity (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:242), which is a single-instance scattering asymmetry of one bound resonator, not the inter-sublattice-tank coupling. (`open_ambiguity:true`, conflicting sites recorded in def-ch1crc.)

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

> **↗ Electrical-vs-mechanical projection-conflation map** (`research/2026-06-19_electrical-mechanical-projection-map.md`): the EM (Ω) ↔ mechanical (ρc) seams in this section are **NOT one artifact to dissolve** — 1 fixed units-conflation (`Z_bulk` mis-scope, #296) + 6 genuine distinctions the corpus holds. EM↔mechanical is a real impedance-DOMAIN boundary the ξ_topo transducer BRIDGES (units change), not a separation to resolve away; bulk↔shear is same-domain ($H_{\mathrm{couple}}$). The unified network buys HYGIENE, not a derivation; α stays echo. The 1.826-vs-2.582 ratio (seam 4) is OPEN pending Grant.

**The Q slot stays EMPTY (strict anti-substitution).** The TARGET of the network is to derive the electron $Q$ from channel impedances + couplings (the **channel-impedance-mismatch $Q$**). That target is **NOT achieved**: the $\alpha$-free cold-cage Q is $\approx30.8$, **NOT** 137 (`src/tests/engine_acceptance/test_l3_mass_cage.py`:702-703; RUNG-1 T3.4b `sup-wuy333`). This is the corpus **clean NEGATIVE** corroborating that the corpus $Q=1/\alpha$ is an instance-baked ECHO ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):19, value-scoped; `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:72 $Q_{\mathrm{TANK}}=1/\alpha$ baked at the instance). **Preserve it. Do NOT refill the slot, do NOT narrate it away.** (Plotting more instruments does not escape the echo: every display reads the same baked $Q$ — [`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):21.)

> **Build-A SECOND clean negative + the loaded-$Q$ test is CIRCULAR (2026-06-19; do NOT re-pose).** The Build-A native ISOLATION eigensolver adds a second reported negative: the **intrinsic** electron mode is **lossless** (EM-port-closed ⇒ Hermitian ⇒ $Q\to\infty$, GATE2), and the isolation eigen-$Q\gg45$ is lossless-confined — **NOT** $137$, NOT $30.8$ (eigenmode-$Q$ ≠ ringdown-$Q$; `research/2026-06-19_electron-Q-coupled-network_result.md`). The $137$ is therefore re-attributed to the **LOADED/radiative** $Q$ ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) §"Amendment (2026-06-19, Rule 12)"), **not** the intrinsic resonator $Q$. The tempting follow-up — "derive the loaded $Q=1/\alpha$ from the EM-port admittance" — is **ADJUDICATED CIRCULAR (do NOT pose it):** the engine's radiative leak is literally `1.0 - alpha` (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:161 `gamma_mag_sq_leak`) = the instrument-echo trap, and the α-free edge-radiation answer is already the cold-cage $30.8$ negative — **no α-free path to $137$.** Slot stays EMPTY; **no new Build-B slot.** Full registry verdict: [`electron-bound-resonator-coverage.md`](../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md) §registry gate B.1.

**Conserved $H_{\mathrm{couple}}$ (the only allowed inter-grade coupling).** Grades may couple ONLY through a conserved (energize-lock, no-pump) Hamiltonian pair — one $H_{\mathrm{couple}}$, source + back-reaction, NEVER a shared $(V_{\mathrm{inc}},V_{\mathrm{ref}})$ phasor (the $A1\perp T2$ fence, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20; the energize-lock rule, [`ch17 index`](../ch17-engine-requirements/index.md):19). The live candidate is the **graft-v3 shear$\leftrightarrow$bulk $\chi$-source** — but it is **DEMOTED B$\to$C / unimplemented**: present as live-but-not-adjudicated, **NOT available**.

**Two DIFFERENT coupling problems, because the channels live in different impedance DOMAINS (§6.1).** The mixed-domain distinction has a consequence for how channels couple:

- **bulk $\leftrightarrow$ shear** is a coupling **WITHIN the mechanical domain** (both $\rho\times$speed) — this is the inter-grade $H_{\mathrm{couple}}$ above (conserved, energize-lock; live candidate graft-v3, demoted/unimplemented).
- **EM (electrical, $\Omega$) $\leftrightarrow$ mechanical ($\rho c$)** crosses an impedance DOMAIN. Two ports in different units cannot be directly wired together; a domain-crossing coupling requires a **TRANSDUCER** (an electro-mechanical change-of-reference), not a direct wire.

> **Candidate-refinement (NOT asserted — the transducer node is itself PROPOSED-not-ratified).** The corpus's candidate electro-mechanical bridge is the **TKI-transformer** ([def-tk1xfm](../../common/vocabulary-register.md)) — Axiom 2 (the Topo-Kinematic Isomorphism, $\xi_{topo}$ dictionary $u/$strain$\leftrightarrow E$, $\omega/$curl$\leftrightarrow B$) read as the ideal, lossless, gain-1, pole-less, invertible electromechanical change-of-reference. In ROLE it is exactly an EM$\leftrightarrow$mechanical transducer, so it is the natural candidate to sit on the EM$\leftrightarrow$mechanical coupling. **FLAG (do NOT assert):** (1) def-tk1xfm is itself **`status:proposed`, awaiting auditor + Grant ratification — NOT yet canonical**; (2) it carries the strength ceiling *"identity-by-translation, NOT emerges-from / NOT a derivation"* (the `translation-circuit.md:660` piezo over-claim guard) — it transduces units losslessly, it does NOT supply a derived coupling MECHANISM or a pole; (3) the inter-grade DYNAMICS (poles, $Q$, the trap) live in the resonator $H(s)$, NOT in the transformer. So the TKI-transformer is offered here as the **candidate** electro-mechanical bridge, not an adjudicated wire — it is gated behind def-tk1xfm ratification, and the EM-port is in any case the matched radiative PORT ($\Gamma_{\mathrm{EM}}=0$), not a confined hair-sector (§6.4).

**Fork-A — isolation vs coupling (KEEP-BOTH discriminator).** Does the mass channel (bulk) couple to the charge channel (shear) via $H_{\mathrm{couple}}$, or is it galvanic isolation? **Both legs live:**

- *Isolation leg:* the measured $\omega\to V$ structural zero (the cold cage's $Q\approx30.8$ is a self-consistent isolated-tank number).
- *Coupling leg:* the graft-v3 $\chi$-source (demoted, unimplemented).

*Signatures:* mode-splitting / avoided-crossing (coupled) vs free-crossing (isolated). *Quantitative handle:* does engaging $H_{\mathrm{couple}}$ lift the cold-cage $Q\approx30.8$ toward the **OBSERVED** electron $Q$ — **NOT** the baked 137 (which is the echo, not an independent target)?

**Fork-B — the chiral circulator (STATED-pending-engine).** The inter-tank non-reciprocal coupling (§6.3) is STATED; its magnitude needs the chiral-crystal engine. Held open, not adjudicated.

**TENSION-1 discriminator (OPEN, defined test).** Does the EM far-field reduce to the **matched-port projection of the interior micropolar winding** ($\mathcal{Q}$=micropolar, EM=antenna), or is there a **residual EM-channel charge DOF**? A defined test, resolvable in the coupled-network derivation, currently OPEN.

**Q two-integrals reconciliation (OPEN, likely closer named).** Charge appears as a **1D linking number** ([`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):20) AND as a **3D Beltrami helicity** $H_{\mathrm{bel}}$ ([`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). These are almost certainly two projections of ONE charge via the **helicity=linking identity** (Moffatt 1969) — but that identity is **NOT written down for the AVE case**. Registered as a reconciliation gate (likely closer noted), OPEN.

> **Full open-gate registry.** The 12-item open-gate registry for this network is hosted in the BoundResonator coverage matrix ([`electron-bound-resonator-coverage.md`](../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md)) under its A/B/C FORM-chord / VALUE-echo buckets (INVARIANT-S11 extend-don't-reinvent — no parallel registry is minted here).

#### 6.6 Figure slots (to be generated by the coupled-network derivation task)

These are **provisional figure slots** — captions/specs only. The equations are the separate coupled-network derivation task; **do NOT fake plots**. Each is marked **to be generated by the coupled-network derivation task**.

| Slot | Figure | Caption spec |
|---|---|---|
| (i) | `fig:vol9_graded_network_schematic` | **Graded vacuum impedance network schematic** — three reactance branches ($Z_{\mathrm{EM}}$, $Z_{\mathrm{shear}}$, $Z_{\mathrm{bulk}}$) wired through the chiral circulator (inter-tank, §6.3) with confinement-surface terminations on the two CONFINED channels ($\Gamma=-1$) and the open matched port on $Z_{\mathrm{EM}}$ ($\Gamma=0$). *To be generated by the coupled-network derivation task.* |
| (ii) | `fig:vol9_graded_network_smith` | **Per-channel Smith / impedance** — $Z_{\mathrm{EM}}$ matched at $\Gamma=0$ (origin of the Smith chart); $Z_{\mathrm{shear}}$ and $Z_{\mathrm{bulk}}$ trajectories running toward $\Gamma=-1$ (the short-circuit point) as $S(A)\to0$. *To be generated by the coupled-network derivation task.* |
| (iii) | `fig:vol9_forkA_discriminator` | **Fork-A discriminator sweep** — $Q$ vs coupling strength: mode-splitting / avoided-crossing (coupled) vs free-crossing (isolated); cold-cage $Q\approx30.8$ (isolated, measured) vs coupled-$Q$ trajectory. Annotate that the target is the OBSERVED electron $Q$, NOT the baked 137. *To be generated by the coupled-network derivation task.* |
| (iv) | `fig:vol9_graded_network_op_sweep` | **Operating-point sweep** — channel impedances vs saturation $S$: $Z_{\mathrm{EM}}$ flat (matched), $Z_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}\,c_0\to0$ and $Z_{\mathrm{shear}}\to0$ as $A\to1$ (plot the two mechanical channels on their own $\rho\,c$ axis, NOT against $Z_0$). *To be generated by the coupled-network derivation task.* |
| (v) | `fig:vol9_confinement_surface_shapes` | **Confinement-surface shapes electron-vs-proton** — the topology-forced $\Gamma=-1$ surface for the electron ($0_1$ unknot, single-node) vs the proton ($6^3_2$ Borromean, multi-node); proton single-vs-multi-node UNADJUDICATED. *To be generated by the coupled-network derivation task.* |

---

### Verify-before-cite audit log (2026-06-12)

| Cited anchor | Verification |
|---|---|
| `orbital-friction-paradox.md`:35 | Grep: $m_e c^2 \cdot \alpha$ in reactive-shell row ✓ |
| `constants.py` | `Z_0`:98, `RHO_BULK`:646, `G_VAC`:654, `V_LONG`:658 ✓ |
| OP table numerics | `operating_point_coefficients.json` (driver run 2026-06-11) ✓ |
| Electron $\Gamma_{\mathrm{bulk}}$ not $\Gamma_{\mathrm{EM}}$ | [`electron-bh-isomorphism.md`](../../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):26 ✓ |

---
