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

One physical saturation boundary = **three channel-specific** $\Gamma$ values (three-impedance law; `research/2026-06-10_field-symbol-registry.md` §3.11):

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

Each channel is one substrate grade. The impedances and saturation $\Gamma$ values are reproduced verbatim from the three-impedance law ([`three-channel-impedances.md`](../ch4-dc-electrical-characteristics/three-channel-impedances.md):20-22); this leaf ADDS the two-"3"s grade tag without renaming any channel.

| Channel | Grade | Impedance | $\Gamma$ at saturation | Two-"3"s tag |
|---|---|---|---|---|
| $Z_{\mathrm{EM}}$ | T2 transverse field | $Z_{\mathrm{EM}}\equiv Z_0=\sqrt{\mu_0/\varepsilon_0}\approx376.73\,\Omega$ | $\Gamma_{\mathrm{EM}}=0$ — **MATCHED / radiative PORT** | — (matched port, not a hair-sector) |
| $Z_{\mathrm{shear}}$ | deviatoric $G$ | $Z_{\mathrm{shear}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ | $\Gamma_{\mathrm{shear}}\to-1$ — CONFINED | **CHARGE-"3"** (Cosserat micro-rotation winding) |
| $Z_{\mathrm{bulk}}$ | dilatation $K$ | $Z_{\mathrm{bulk}}=\sqrt2\,Z_0$ at $K=2G$ (i.e. $c_{\mathrm{bulk}}=\sqrt2\,c_0$) | $\Gamma_{\mathrm{bulk}}\to-1$ — CONFINED | **MASS-"3"** (A1 dilatation) |

**Naming discipline (do NOT rename the channels).** Keep $Z_{\mathrm{EM}}$ named $Z_{\mathrm{EM}}$ — do **not** rename it to $Z_{\mathrm{transverse}}$: BOTH EM and shear are transverse waves, so "transverse" is ambiguous; $Z_{\mathrm{EM}}\equiv Z_0$ is the native label because $Z_0=\sqrt{\mu_0/\varepsilon_0}$ is a vacuum constant. Keep this three-grade wave-channel set DISTINCT from the coarser **Electric / Magnetic / Either** per-element constitutive tags of the `AVE_VACUUM_CELL` (§1) — those are a different (per-element constitutive) classification, not the wave-channel set.

**Two-"3"s grade tag (the AMENDMENT this leaf adds).** Per the two-"3"s disambiguation ([`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20, Grant-ratified): the **bulk** channel carries the MASS-"3" (the A1 Heaviside-excised longitudinal dilatation scalar — $m_e c^2$ = trapped acoustic compression energy), and the **shear** channel carries the CHARGE-"3" (the orthogonal Cosserat $(2,3)$ micro-rotation winding — charge = Beltrami helicity). $A1\perp T2$: the two grades are orthogonal, never wired into one shared $(V_{\mathrm{inc}},V_{\mathrm{ref}})$ phasor (the genesis-24 / $w_{\mathrm{pol}}=0$ double-count guard). The EM channel is the matched radiative PORT, **not** a hair-sector — it is how the interior couples to the far field, not where an observable lives (see the M, J, Q honest map, §6.4).

#### 6.2 The confinement surface (Γ=−1 cage-wall, status OPEN)

The two CONFINED channels terminate at a **confinement surface** ([def-cf1srf](../../common/vocabulary-register.md)) — the $\Gamma=-1$ cage-wall $\partial\Omega$ where $Z_{\mathrm{core}}\to0$ ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):38,47-50). Its **shape is FORCED by topology** (the real-space body + the phase-space winding + the node-span) and is therefore **DERIVED, never posited-spherical** (Grant D4).

> **Status: OPEN.** The $\Gamma=-1$ TIR condition itself is canonical (clm-kezk9z; RUNG-1 T3.3 `sup-1ecv2m` — $\Gamma_{\mathrm{bulk}}$ crosses the OP2 gate by $A=0.95$, $\alpha$-FREE). What is **NOT** derived is the **shape-forcing chain**: no solved boundary-value problem produces the electron's surface from its $0_1$-unknot topology. The electron ($0_1$ unknot, single-node) and the proton ($6^3_2$ Borromean, multi-node — [`boundary-observables-m-q-j.md`](../../common/boundary-observables-m-q-j.md):43-44) get DIFFERENT derived shapes; the proton single-vs-multi-node confinement is **UNADJUDICATED**.

> **Two coincident $\Gamma=-1$ walls — do NOT re-collide.** The confinement surface is the **A1 MASS wall** ($Z_{\mathrm{bulk}}\to0$, the impedance-short $\Gamma=-1$ of the Pauli/TIR derivation). It is numerically coincident with — but a **DISTINCT object** from — the **$\Gamma_{\mathrm{spinor}}=-1$** topological $2\pi\to4\pi$ stability wall of the T2 micro-rotation sector ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):89-94; $A1\perp T2$ per [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20, Grant-ratified). The electron carries BOTH; the confinement surface terminating the **bulk** channel is the MASS one only. Reading the two $-1$'s as one wall would wire the cage into the charge-winding and break the two-"3"s orthogonality.

#### 6.3 The chiral circulator (inter-tank non-reciprocal coupling, STATED-pending-engine)

The two sublattice TANKS (the bipartite A/B sublattices of the $I4_1 32$ chiral srs net) are coupled through a **chiral circulator** ([def-ch1crc](../../common/vocabulary-register.md)) — a **NON-RECIPROCAL inter-tank coupling** carrying the lattice chirality. It is the inter-tank element of the network schematic (§6.6 Fig. i), drawn as a circulator.

> **Status: STATED — pending the chiral-crystal engine.** The cubic-FDTD engine averages chirality out, so the non-reciprocity MAGNITUDE is not yet computed (`cvr_model.py:243` AUDITOR_STATE note). This is a STATED frontier, NOT adjudicated and NOT available.

> **Do NOT call it "gyrator."** The reciprocal optical-activity **gyrator** ([def-0pt1ac](../../common/vocabulary-register.md) — the lossless reciprocal-Faraday polarization-plane rotator, $\pm75.46°$/unit) is a DIFFERENT element; "circulator" is reserved here for the non-reciprocal inter-tank coupling. The chiral circulator is also DISTINCT from the **per-particle** $S_{LR}\ne S_{RL}^*$ winding non-reciprocity (`cvr_model.py:242`), which is a single-instance scattering asymmetry of one bound resonator, not the inter-sublattice-tank coupling. (`open_ambiguity:true`, conflicting sites recorded in def-ch1crc.)

#### 6.4 The M, J, Q honest map (refuted bijection)

#### 6.5 Forks and open gates

#### 6.6 Figure slots (to be generated by the coupled-network derivation task)

---

### Verify-before-cite audit log (2026-06-12)

| Cited anchor | Verification |
|---|---|
| `orbital-friction-paradox.md`:35 | Grep: $m_e c^2 \cdot \alpha$ in reactive-shell row ✓ |
| `constants.py` | `Z_0`:98, `RHO_BULK`:646, `G_VAC`:654, `V_LONG`:658 ✓ |
| OP table numerics | `operating_point_coefficients.json` (driver run 2026-06-11) ✓ |
| Electron $\Gamma_{\mathrm{bulk}}$ not $\Gamma_{\mathrm{EM}}$ | [`electron-bh-isomorphism.md`](../../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):26 ✓ |

---
