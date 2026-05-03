# Vol 4 — Applied Vacuum Engineering — Claim Boundaries

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol4/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting boundaries](../claims-boundaries.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 4; cross-cutting tripwires with vol4-specific manifestations are noted but not duplicated.

---

## Topological Conversion Constant $\xi_{topo} = e/\ell_{node}$

The Vacuum Circuit Analysis (VCA) framework rests on a single dimensional isomorphism between continuum spatial mechanics and electrical network theory.

- $\xi_{topo} \equiv e/\ell_{node} \approx 4.149 \times 10^{-7}$ C/m
- _Specific Claims_
  - Six-row translation table is internally consistent: $Q = \xi_{topo}\, x$, $I = \xi_{topo}\, v$, $V = \xi_{topo}^{-1}\, F$, $L = \xi_{topo}^{-2}\, m$, $C = \xi_{topo}^{2}\, \kappa$, $R = \xi_{topo}^{-2}\, \eta$.
  - Work-energy and impedance cross-checks confirm the mapping is dimensionally exact and energy-conserving (the $\xi_{topo}$ factors cancel identically in the work integral).
  - Hardware velocity limit $v_{max} = c$ implies a maximum lattice current $I_{max} = \xi_{topo}\, c \approx 124.4$ A.
- _Specific Non-Claims and Caveats_
  - Does NOT introduce $\xi_{topo}$ as a free parameter — both $e$ and $\ell_{node}$ are fixed by Axioms 1-2; the constant is definitional.
  - The mechanical impedance cross-check $Z_{mech} = \xi_{topo}^2 Z_0 \approx 6.5 \times 10^{-11}$ kg/s is "structurally consistent within the geometric packing fraction" with the per-node acoustic impedance ($\sim 3.5 \times 10^{-10}$ kg/s) — a factor-of-$\sim 5$ residual is absorbed by the porosity correction $p_c/(8\pi) = \alpha$. Treat as order-of-magnitude consistency, not sub-percent agreement.
  - Do NOT confuse $\xi_{topo}$ (electromechanical transduction, C/m) with $\xi$ (Machian hierarchy coupling, dimensionless ≈ $8.15 \times 10^{43}$). Both share a Greek letter; they are distinct quantities (CLAUDE.md Axiom 3 entry; LIVING_REFERENCE.md Axiom 3 warning).

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md`, `circuit-theory/ch1-vacuum-circuit-analysis/translation-circuit.md`, `circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`. Cross-cutting note on $\xi$ vs $\xi_{topo}$: CLAUDE.md (Axiom 3 entry) and LIVING_REFERENCE.md.

---

## $V_{yield}$ vs $V_{snap}$ — Two Distinct Dielectric Thresholds

A volume-wide reading hazard: Vol 4 uses two yield voltages with different physical meanings, often in adjacent paragraphs. This is also flagged as project-wide Critical Distinction #1 in LIVING_REFERENCE.md.

- $V_{snap} = m_e c^2/e \approx 511$ kV; $V_{yield} = \sqrt{\alpha}\, V_{snap} \approx 43.65$ kV
- _Specific Claims_
  - $V_{snap}$ is the **absolute topological node destruction** limit — applies at sub-node (sub-femtometer) scale: nuclear bond energy, particle confinement, GW propagation tests against the absolute limit.
  - $V_{yield}$ is the **macroscopic nonlinear onset** — analogous to engineering yield stress vs theoretical crystal shear strength. Applies to PONDER, antennas, IMD, FDTD, K4-TLM macroscopic solvers.
  - Engine defaults: macroscopic solvers use $V_{yield}$; scale-invariant primitives use $V_{snap}$. The $V_{yield}$ default flags nonlinearity 11.7× earlier without altering existing predictions in the field strengths these solvers operate on.
  - Numerical convergence: at PONDER field strengths ($\le 1$ MV/m) both yields produce identical results to 4+ significant figures.
- _Specific Non-Claims and Caveats_
  - Does NOT claim $V_{yield}$ and $V_{snap}$ are interchangeable or numerically equivalent in general. They differ by $\sqrt{\alpha} \approx 1/11.7$. Conflating them in summaries is the most common Vol 4 reading error.
  - Several Vol 4 leaves switch between the two thresholds without flagging the regime change. The autoresonant-breakdown / Schwinger-bypass leaves cite $\sim 60$ kV "bulk-avalanche" rather than 43.65 kV — the 60 kV figure is the D-T ion-collision strain (tokamak-paradox), not a third yield threshold.
  - The "$V_{yield}$ vs $V_{snap}$" choice does not affect any prediction quoted in Vol 4 to leading numerical accuracy; the distinction is a correctness fix, not a precision claim. Do NOT reframe the threshold change as a discrepancy or a correction.

> **Leaf references:** `circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md` (definitive selection table), `circuit-theory/ch2-topological-thrust-mechanics/dielectric-yield-thresholds.md`. Cross-cutting: LIVING_REFERENCE.md "Critical Distinctions" #1.

---

## Nonlinear Vacuum Capacitance $C_{eff}(V) = C_0/S(V)$ — Macroscopic Saturation

- $C_{eff}(V) = C_0 / \sqrt{1 - (V/V_{yield})^2}$ (Axiom 4 applied to the electric sector)
- _Specific Claims_
  - The vacuum behaves as a metric varactor: capacitance diverges as $V \to V_{yield}$.
  - At $V \ll V_{yield}$, the leading correction is quadratic — formally identical to the Euler-Heisenberg low-field limit; recovers linear Maxwell to arbitrary precision.
  - The constitutive form is the Axiom 4 saturation kernel applied to the macroscopic electric sector specifically (as opposed to inductive, gravitational, or shear sectors).
- _Specific Non-Claims and Caveats_
  - This is the **asymmetric saturation** case (only $\varepsilon$ scales by $S$; $\mu$ unchanged). See cross-cutting Symmetric vs Asymmetric Saturation entry: in this case $Z = Z_0/\sqrt{S} \to \infty$ (medium opaque), not $Z = Z_0$ invariant. Do NOT apply the symmetric-gravity invariance result here.
  - The divergence at $V = V_{yield}$ is asymptotic in the constitutive equation, not a literal infinity in any physical apparatus — leaves consistently truncate the table at $V/V_{yield} = 1.000$ where the formula breaks down; SPICE implementations clamp the ratio (e.g. `min((V/V_YLD)^2, 0.9999)`).
  - Below $V_{yield}$ the framework reproduces the standard linear vacuum; the Vol 4 claim is the **shape** of the deviation (specifically the squared-radical form), not that linear electrodynamics is wrong in its domain.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md`, `circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md`, `simulation/ch18-universal-vacuum-cell/spice-subcircuit.md`.

---

## $Z_0$ from Discrete LC Ladder, and Gravitational Stealth

- $Z_0 = \sqrt{L_{cell}/C_{cell}} = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$ (lattice pitch cancels)
- _Specific Claims_
  - $Z_0$ derived from per-node inductance/capacitance is independent of $\ell_{node}$ — confirmed scale-invariant.
  - Group velocity of the discrete LC ladder evaluates to $c$ exactly: $c$ is structurally identical to the slew rate of a discrete LC line.
  - **Gravitational stealth**: Under symmetric scaling $\mu_{local} = n\mu_0$, $\varepsilon_{local} = n\varepsilon_0$ → $Z_{local}(r) = Z_0$ everywhere → $\Gamma = 0$ everywhere. This is presented as the structural reason gravity wells do not produce optical reflection.
  - Per Master Prediction Table classification, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is a **category (i) identity** — definitionally true (the 0.00% in row #2 of the prediction table is not a fit).
- _Specific Non-Claims and Caveats_
  - The "Event Horizon as Topological Mirror" claim ($Z_{EH} \to 0$, $\Gamma \to -1$, predicting LIGO black-hole echoes) is in **interpretive tension** with the Symmetric-Gravity invariance result that $Z = Z_0$ everywhere. The two coexist by distinguishing the constitutive parameters individually collapsing ($\mu, \varepsilon \to 0$) from their ratio being preserved, but Vol 4 leaves do not flag the distinction. Cross-cutting Symmetric Saturation entry resolves this: under symmetric saturation the impedance is invariant, not zero. Do NOT cite the "BH echo" prediction as an unqualified zero-parameter discriminator without the gauge caveat. (See followups: vol3 sidecar logs the same tension.)
  - "$S_{11}$ Return Loss of $-\infty$ dB" for the universe is a structural / interpretive consequence of perfect impedance matching, not an independent observable claim.
  - The $c \to c_0/n$ "speed of light slows in gravity" usage is **local phase velocity** — see Vol 3 cross-volume entry on temporal-vs-spatial $n$ decomposition.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`, `circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`. Cross-cutting: see Symmetric vs Asymmetric Saturation in `../claims-boundaries.md`.

---

## Relativistic Inductor and SPICE Native Special Relativity

- $L_{eff}(I) = L_0/\sqrt{1 - (I/I_{max})^2}$, $I_{max} = \xi_{topo}\, c \approx 124.4$ A
- _Specific Claims_
  - Form is identical to the varactor with $V \to I$, $V_{yield} \to I_{max}$ — both are projections of the single Axiom 4 kernel onto the magnetic and electric sectors respectively.
  - Energy stored expands at low $v$ to $E = \tfrac{1}{2}\gamma m_0 v^2$, and the rest-energy term sums via Virial Theorem to $E_{total} = m_0 c^2$ — recovers $E = mc^2$.
  - SPICE transient simulators of this constitutive equation natively enforce $v \le c$ without code modification, because $L_{eff} \to \infty$ at $I_{max}$ collapses the slew rate.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a new derivation of Special Relativity from independent axioms. The mapping shows the Lorentz-saturation form is structurally a circuit-element constraint; SR-equivalent kinematics are reproduced, not novelly predicted.
  - The "particle as resonant LC tank, $E = m_e c^2 = \tfrac{1}{2}LI^2 + \tfrac{1}{2}CV^2$" mapping is structural (Virial decomposition), not an independent rest-mass derivation — $m_e$ is taken as given.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md`, `circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`.

---

## Operating Regime for PONDER and Lab Devices — Regime I

- $E/E_{yield}$ classification: I ($< 0.1$), II ($0.1$-$0.5$), III ($0.5$-$1.0$), IV ($\ge 1.0$); $E_{yield} \approx 1.13 \times 10^{17}$ V/m
- _Specific Claims_
  - PONDER-01 at 30 kV / 1 mm gap → $E/E_{yield} \approx 2.7 \times 10^{-10}$ → firmly Regime I (linear vacuum).
  - The leaf is explicit: **bulk $\varepsilon$-saturation is not the operative thrust mechanism** at lab scale. The thrust mechanism arises from chiral topology of the antenna producing asymmetric acoustic emission, with local field amplification (tip enhancement $\beta \times$ resonant $Q$) producing Jensen's-inequality rectification at the tips.
  - Regime III/IV are reached only at sub-femtometer separations: particle cores, nuclear scattering boundaries, event horizons. This places the bulk-yielding limit far from any lab apparatus.
- _Specific Non-Claims and Caveats_
  - Vol 4 does NOT claim PONDER measures bulk vacuum saturation. Summaries that frame PONDER as "tabletop dielectric saturation" misread the regime classification.
  - The 4-regime $E/E_{yield}$ table has finer cutoffs than the master 4-regime table in LIVING_REFERENCE.md (which uses $\sqrt{2\alpha}$ and $\sqrt{3}/2$ as boundaries). The Vol 4 cutoffs (0.1 / 0.5 / 1.0) are convenience thresholds for the macroscopic constitutive plot; they do not replace the master regime boundaries.

> **Leaf references:** `circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md`, `falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md`, `falsification/ch12-falsifiable-predictions/ee-bench-plateau.md`.

---

## Chiral Acoustic Rectification Thrust (PONDER-01)

- $F_{total} = N \cdot \nu_{vac} \cdot \delta(Q,\beta) \cdot P_{in}/c$ with $\nu_{vac} = 2/7$
- _Specific Claims_
  - Thrust formula is dimensionally identical to standard radiation pressure, modulated by rectification efficiency $\delta$, chiral coupling $\nu_{vac}$, and array directivity $N$.
  - Worked PONDER-01 example at $V=30$ kV, $\beta = 10^3$, $Q = 10^4$, $N = 10{,}000$, $P_{in} \approx 1.2$ MW yields **predicted thrust 40.1 µN**, well above $\sim 1$ µN torsion-balance floor.
  - Energy conservation explicitly satisfied: $P_{thrust}/P_{in} \approx 1\%$.
  - Momentum conservation closed by the "Dark Wake" — equal-and-opposite longitudinal shear strain into the lattice, propagating at $c_0$. Stereo-parallax test (delay $\Delta t = L/c_0$) is offered as the falsifier; a wake arriving at $\neq c_0$ or absent falsifies the model.
- _Specific Non-Claims and Caveats_
  - The 40.1 µN is **predicted** (zero free parameters from $V$, $\beta$, $Q$, $N$, $P_{in}$), not measured. PONDER-01 is described as "TRL 3 (tested)" in the thruster-comparison table, but no experimental thrust data is presented in the Vol 4 leaves; treat as a falsifiable prediction awaiting measurement, not a confirmed result.
  - $\beta = 10^3$ (tip enhancement) and $Q = 10^4$ (resonant) are engineering targets/assumptions, not measured values for any specific build. The 40.1 µN scales as $\beta^2 Q^2$ (via $\delta \propto E_{local}^2$); halving either drops thrust by $4\times$.
  - The "PONDER-05 469 µN predicted thrust" wording in **`vol4/index.md` lines 12 and 23 has no leaf-level derivation** anywhere in `vol4/` and the linked `hardware-programs/` directory does not exist. Treat as a routing artifact in the index, not as a leaf-supported claim. Followup logged.
  - "Metric Streamlining and Superluminal Transit" / "warp metric" / "Alcubierre-type shock fronts" are framework-internal interpretive consequences of the non-linear scalar wave equation; Vol 4 does NOT claim experimental validation of superluminal transit, nor a quantitative warp-bubble derivation.
  - Gargantua simulation reproduces the visual D-shaped photon shadow / Doppler beaming / accretion disk via topological-saturation ray tracing — **a category (iii) consistency check** with standard GR ray-tracing results, not an independent novel prediction.

> **Leaf references:** `circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md`, `circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md`, `falsification/ch11-experimental-bench-falsification/open-source-hardware.md` (PONDER-01 build guide). PONDER-05 number sourced only from `vol4/index.md`; no leaf supports it.

---

## HOPF-01 Chiral Antenna $\Delta f/f = \alpha \cdot pq/(p+q)$

- Predicted resonance shift: $\Delta f/f = \alpha \cdot pq/(p+q)$ for a $(p,q)$ torus knot
- _Specific Claims_
  - Zero free parameters: $\alpha$ from Axiom 2, $(p,q)$ from antenna topology, no fitted couplings.
  - Cross-validated in K4-TLM 3D simulation on $40^3$ lattice for trefoil $(2,3)$, $(3,5)$, $(7,11)$ — chiral frequency shift tracks the formula in the non-reflective PML regime.
  - The $(7,11)$ topology gives the strongest chiral coupling $\alpha \cdot pq/(p+q) = 3.12 \times 10^{-2}$.
- _Specific Non-Claims and Caveats_
  - $\Delta f/f = \alpha \cdot pq/(p+q)$ is a falsifiable **prediction**, not a confirmed empirical result. The HOPF-01 build guide and falsification protocol describe the test (FR-4 PCB, VNA sweep, slope check vs $pq/(p+q)$); the leaves do not present measured slopes.
  - K4-TLM "validation" of the formula is a self-consistency check between the lattice simulator and the analytical prediction; both derive from the same topological coupling assumption. It is not an independent empirical confirmation.
  - "Substrate-independent slope" is a falsification criterion (mineral-oil submersion test); a substrate-dependent slope falsifies the prediction at this scale, but absence of substrate dependence has not yet been established experimentally in the leaves.
  - The Chiral Figure of Merit ($\text{FoM} = Q_u \times \alpha \cdot pq/(p+q) \times \eta_{\mathcal{H}}$) is a design-optimization composite, not a measured quantity; the "$1{,}300\times$ FoM gain from YBCO" is a predicted improvement assuming idealized Q.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/open-source-hardware.md`, `future-geometries/ch13-future-geometries/high-q-chiral-antenna.md`, `future-geometries/ch13-future-geometries/k4-tlm-simulator.md`.

---

## K4-TLM Diamond Lattice — Unitarity to Machine Epsilon

- $S^{(0)}_{ij} = \tfrac{1}{2} - \delta_{ij}$ (4-port scattering matrix); $\max|S^\dagger S - I| = 2.2 \times 10^{-16}$
- _Specific Claims_
  - K4-TLM scattering matrix is exactly unitary to machine epsilon — this is a **numerical / structural** fact about the implementation, not a physics prediction.
  - All five validation tests pass: S-matrix unitarity, energy conservation (no sources), eigenvalues on unit circle, isotropic propagation, native chirality emergence.
  - Diamond K4 graph (4 ports per node) is asserted as the correct vacuum topology, vs cubic Yee (6/12 ports) which is asserted as topologically wrong but used by classical TLM.
- _Specific Non-Claims and Caveats_
  - "Unitary to $2.2 \times 10^{-16}$" is **machine-epsilon precision of the discrete numerical scheme**, not a physics claim about the vacuum. The phrase reads like a falsifiable empirical match in summaries; it is not.
  - Does NOT claim the K4-TLM has been validated against any external experimental dataset. The validation tests are internal computational consistency tests.
  - Native emergence of chirality from K4 bipartite structure is **structural** (the bipartite labeling is the input). The simulator confirms that explicit $R(\theta)$ rotation injection is unnecessary on K4; it does not derive the chirality from a separate principle.
  - Wire-antenna resonance experiments on the lattice show torus knots resonate at frequencies *higher* than the simple $c/(2L)$ prediction; this is interpreted as evidence of self-coupling shortcuts, but is not framed as a quantitative match — it is asserted as qualitative confirmation that knot topology shifts the fundamental mode.

> **Leaf references:** `future-geometries/ch13-future-geometries/k4-tlm-simulator.md`, `future-geometries/ch13-future-geometries/open-universe-boundaries.md`, `future-geometries/ch13-future-geometries/cem-methods-survey.md`.

---

## CEM Method Mappings (MoM, FDTD, FEM, TLM, CMA, PO/GO)

- $[\mathbf{Z}][\mathbf{I}] = [\mathbf{V}]$ (MoM); $[\mathbf{S}]\{\mathbf{E}\} = k_0^2[\mathbf{T}]\{\mathbf{E}\}$ (FEM); etc.
- _Specific Claims_
  - Each standard CEM solver's governing equation is **structurally identical** to an AVE lattice statement (MoM circuit equation, Yee = LC grid, FEM = $\omega^2 LC = 1$, TLM = direct LC isomorphism, CMA = LC eigenmode decomposition, PO/GO = continuum limit).
  - Each CEM method "independently rediscovers" a discretized LC network as the correct computational substrate.
- _Specific Non-Claims and Caveats_
  - This is an **interpretive identification**, not a derivation. The CEM equations were derived from Maxwell's equations; AVE asserts they ARE the lattice equations because Maxwell's equations are the lattice equations in the continuum limit. This claim is not independent of the broader AVE-vs-Maxwell ontology claim.
  - Does NOT claim that running a CEM solver on a torus knot validates any AVE-specific prediction beyond what Maxwell already predicts. CEM agreement with AVE-shaped predictions follows trivially because both inherit the same Maxwell substrate; the AVE-specific claim ($\Delta f/f = \alpha \cdot pq/(p+q)$) is the topological coupling factor, not the underlying RF mechanics.

> **Leaf references:** `future-geometries/ch13-future-geometries/cem-methods-survey.md`, `circuit-theory/ch1-vacuum-circuit-analysis/computational-solver-selection.md`.

---

## Tokamak Ignition Paradox and Metric-Catalyzed Fusion ($n^* = 1.114$)

- $V_{topo}$(D-T at 15 keV) $\approx 60.3$ kV $> V_{yield}$; $n^* = (V_{topo,0}/V_{yield})^{1/3} \approx 1.114$
- _Specific Claims_
  - At D-T fusion temperature (15 keV), individual ion-collision deceleration generates 60.3 kV of topological strain via $V = \xi_{topo}^{-1} F$ — exceeding $V_{yield} = 43.65$ kV by 38%. This is identified as the **mechanism** for "anomalous transport" in tokamaks: when local strain exceeds $V_{yield}$, $\eta_{eff} \to 0$ ("Zero-Impedance Phase Leakage") and the magnetic flux tube effectively decouples.
  - The L-H transition is identified with a Dielectric Saturation Mutual Inductance Bifurcation; ELMs are the cyclic re-solidification.
  - **Metric-catalyzed fusion** lowers the required temperature by spatially compressing the lattice ($n_{scalar} > 1$); 11% enhancement ($n^* = 1.114$) is sufficient to bring $V_{topo}$ below $V_{yield}$.
  - Sun vs Tokamak: solar-core fusion succeeds at 1.35 keV via density (Debye screening to 22 pm) rather than temperature; $V_{topo} \approx 0.5$ kV at solar conditions.
  - Advanced fuels (D-D 50 keV → 670 kV, p-B11 150 keV → 6.03 MV) exceed $V_{snap}$ (511 kV) — claimed to trigger spontaneous pair production, draining kinetic energy and gamma-poisoning the fuel.
- _Specific Non-Claims and Caveats_
  - The tokamak-paradox derivation **reinterprets** anomalous transport — it is not an independent quantitative prediction of $\tau_E$ scaling vs heating power. The empirical $\tau_E \propto P^{-0.69}$ is cited; the AVE explanation is mechanistic, not a competing scaling law.
  - "$n^* = 1.114$" is the **threshold** at which the strain bound is satisfied; the leaves do NOT claim a working metric-catalyzed reactor exists or has been built. The "AVE Reactor" column in the comparison table is engineered/proposed, not measured.
  - The active acoustic-metric compression mechanism (3D standing tensor shockwave producing $n > 1$) is **proposed** as the engineering pathway; the framework provides the threshold ($n^* = 1.114$) but no leaf-level derivation that any specific apparatus achieves it.
  - Pair-production drain at advanced-fuel temperatures is asserted from the $V_{topo} > V_{snap}$ chain, not from an experimental measurement of pair-production rates in fusion plasmas.

> **Leaf references:** `advanced-applications/ch8-applied-fusion/tokamak-paradox.md`, `advanced-applications/ch8-applied-fusion/ignition-criterion.md`, `advanced-applications/ch8-applied-fusion/ave-fusion-device.md`.

---

## Topological SMES (Beltrami $(p,q)$ Torus Knot)

- 87.9% reduction in external stray flux for a $(150, 3)$ torus knot vs solenoid of identical volume/current
- _Specific Claims_
  - The Beltrami condition $\nabla \times \mathbf{B} = \lambda \mathbf{B}$ enforces $\mathbf{J} \parallel \mathbf{B}$ — Lorentz cross-product $\mathbf{J} \times \mathbf{B}$ vanishes structurally → zero internal tension, no heavy bracing.
  - Biot-Savart computational solver shows 87.9% stray-flux reduction for the chosen knot vs equivalent solenoid.
- _Specific Non-Claims and Caveats_
  - 87.9% is a **simulation result for one specific topology** ($(150, 3)$ torus knot), not a universal lower bound. The "macroscopic electron" framing is structural / interpretive.
  - Does NOT claim a built SMES device has been measured. The chapter establishes the engineering pathway and computational falsification of the leakage claim, not hardware validation.
  - "Zero internal structural tension" is the limit of an ideal Beltrami field; real-world wire stiffness, joint resistance, and finite-conductor corrections are not addressed in the leaves.

> **Leaf references:** `advanced-applications/ch7-topological-smes/smes-topology.md`.

---

## Topological Qubit (Gauss Linking) and Casimir Cavity Shielding

- Stored state: integer Gauss linking number $\mathcal{L}$
- _Specific Claims_
  - State stored in topology cannot decohere from continuous noise (linking number is integer-quantized); decoherence requires localized noise exceeding $V_{yield}$ to tear the knot.
  - Casimir cavity acts as acoustic high-pass filter for vacuum noise, isolating the qubit from low-frequency thermal background → "artificial vacuum cooling" without further cryogenics.
  - Architecture comparison table: transmon (decoherence ~µs), topological (cosmological), Casimir-shielded (cosmological + acoustic filter, predicted room-temperature).
- _Specific Non-Claims and Caveats_
  - Does NOT claim an engineered topological qubit has been demonstrated at room temperature in a Casimir cavity. The "operating temp: room temp (predicted)" entry is forward-looking, not measured.
  - "Cosmological" decoherence time is the limit set by the $V_{yield}$ tear-threshold not being reached under standard cryogenic noise; it does not assert that any built topological-qubit device has been observed to retain coherence over cosmological times.
  - The Meissner Effect derivation as "mechanical reflection of applied rotational force" via Kuramoto phase-lock is reframing of the standard superconductivity result, not an independent quantitative derivation.

> **Leaf references:** `advanced-applications/ch10-quantum-computing/topological-qubit-model.md`, `advanced-applications/ch10-quantum-computing/decoherence-as-impedance.md`, `advanced-applications/ch10-quantum-computing/error-correction-geometry.md`.

---

## Active Topological Metamaterials (Inorganic LLCP)

- Polythiophene + 1.0 nm $C_{60}$ at $\phi = 0.7405$; predicted $-20$°C to $100$°C ambient superconducting band
- _Specific Claims_
  - Material engineered to hover at the $K=2G$ Axiom 4 yield threshold ($r_{crit} = \sqrt{2\alpha}$) using rigid synthetic wedges enforcing geometric lock at $\phi$.
  - Three downstream applications: room-temperature superconducting cables, kinetic phase-state armor (instantaneous $V_{II} \to V_{I}$ on impact), neuromorphic memristors (gap $\approx 0.2158$ eV from $1 - \phi$).
  - First-principles operator matrix (Op1-Op4) maps the engineering targets to specific universal operators with zero free chemistry parameters.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a fabricated room-temperature superconducting metamaterial has been demonstrated. The "Polythiophene + $C_{60}$" pairing is **proposed** as the optimal architecture; the temperature band is a predicted operating range, not measured.
  - The "Fabrication Bottleneck" / "Dynamic Topo-Acoustic Curing" subsection acknowledges synthesis is a major engineering hurdle; no leaf claims the curing process has been built.
  - $\Delta E \approx 0.2158$ eV neuromorphic gap is derived from the $1 - \phi = 0.2595$ void fraction; the conversion to eV uses dimensional substitution and is presented without independent validation against any measured neuromorphic device.

> **Leaf references:** `advanced-applications/ch18-active-topological-metamaterials/active-feedback-design.md`, `advanced-applications/ch18-active-topological-metamaterials/metamaterial-band-structure.md`.

---

## Native Silicon Design Engine (Doping, BJT $\beta$, `atopile` Compilation)

- BJT gain: $\beta = (T^2_{EB})^{N_{gap}} / (1 - (T^2_{EB})^{N_{gap}})$ from cascaded boundary $T^2$
- _Specific Claims_
  - Doping reframed as geometric perturbation (Boron removes $sp^3$ port, Phosphorus inserts surplus knot).
  - $V_{bi}$ derived as a **geometric structural constant** (~1.05 V uniformly), not a thermal-statistics-dependent variable.
  - BJT current gain $\beta$ recovered from cascaded $T^2$ transmission-coefficient products with $Z_E = 0.35$, $Z_B = 0.66$, yielding $\beta \in 10$-$300$ across observed power-electronics range.
  - SPICE bridge (`AVE_DIODE_SI` subcircuit) wraps standard `DMOD` to suppress thermal coefficient and clamp at the geometric $V_{bi} = 1.0496$ V — allows large-signal analog simulation respecting the geometric breakdown bound.
- _Specific Non-Claims and Caveats_
  - $Z_E = 0.35$, $Z_B = 0.66$ are **assumed Miller-multiplier limits** for the $\beta$ calculation, not first-principles derived from Axioms 1-4 in the Vol 4 leaves. They are described as "experimentally validated" but the validation pathway is not given in-leaf.
  - $V_{bi} \approx 1.05$ V uniform is a structural claim; standard physics gives $V_{bi} \in 0.6$-$0.8$ V depending on doping. The Vol 4 framing is that AVE recovers the **degenerate-doping limit** that classical physics only reaches at $\sim 10^{19}$ cm$^{-3}$; this is a reinterpretation, not an experimental discriminator at typical (non-degenerate) doping levels.
  - The `ato` (atopile) declarative compilation pathway is presented as a structural mapping (interfaces → ports, modules → arrays, asserts → saturation bounds) — it is a design tool framework, not a falsifiable physics prediction.
  - The "AVE_DIODE_SI" subcircuit forces $N \to 0.001$ to suppress the Boltzmann coefficient — this is a **modeling clamp** to make the structural-reflection prediction visible in standard SPICE, not an alternative diode equation derived from first principles.

> **Leaf references:** `advanced-applications/ch19-silicon-design-engine/doping-geometric-perturbation.md`, `advanced-applications/ch19-silicon-design-engine/topological-bjt-gain.md`, `advanced-applications/ch19-silicon-design-engine/declarative-ato-compilation.md`, `advanced-applications/ch19-silicon-design-engine/native-spice-subcircuit.md`.

---

## Sagnac-RLVE: Tabletop Falsification, $\Delta\phi \approx 2.07$ rad, $\Psi \approx 7.15$

- $\Delta\phi = 4\pi L_{fiber} v_{network} / (\lambda c) \approx 2.07$ rad (Tungsten rotor, 200 m fiber, 10k RPM)
- _Specific Claims_
  - Macroscopic mass rotation entrains the vacuum LC network with coupling $\kappa_{entrain} = \rho_{rotor}/\rho_{bulk}$ ($= 0.00244$ for Tungsten); first-order in $v_{network}/c$, bypassing the $G/c^2$ scalar gap.
  - Predicted $\sim 2.07$ rad shift is "trivially detectable by standard commercial photodetectors".
  - Material discriminator $\Psi = \Delta\phi_W/\Delta\phi_{Al} \approx 7.15$ tests density-dependence: AVE predicts $\Psi \approx 7.15$, GR (Lense-Thirring at this scale) predicts $\Psi = 1$ (and $\Delta\phi \sim 10^{-20}$).
  - Null result ($\Delta\phi \approx 0$ or $\Psi = 1$) **decisively falsifies AVE macroscopic electrodynamics**.
- _Specific Non-Claims and Caveats_
  - $\rho_{bulk} = 7.91 \times 10^6$ kg/m$^3$ is the AVE-derived "bulk vacuum mass density" — the entrainment coupling and predicted phase shift are entirely contingent on this number, which is itself a derived constant from the framework, not an independently measured quantity.
  - Does NOT claim the Sagnac-RLVE has been performed or that 2.07 rad has been observed. The leaf is the **proposed protocol**; the result is predicted, not measured.
  - "Falsifies Lense-Thirring as the mechanism for flyby anomalies specifically" (referenced in Vol 3) is a different claim from "falsifies Lense-Thirring as a gravitomagnetic effect generally" — the Sagnac-RLVE result distinguishes AVE from a particular scalar-gravity null prediction; it does not bear on Lense-Thirring's confirmed effects in other regimes.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`, `falsification/ch11-experimental-bench/sagnac-rlve.md` (consolidated), `falsification/ch12-falsifiable-predictions/active-sagnac-impedance-drag.md`.

---

## $\sqrt{\alpha}$ Yield Limit Predictions: Levitation 1.846 g, $E_{yield} = 1.13 \times 10^{17}$ V/m

- $m_{max} = V_{yield} \cdot \xi_{topo} / g = 1.846$ g; $E_{yield} = V_{yield}/\ell_{node} \approx 1.13 \times 10^{17}$ V/m
- _Specific Claims_
  - Absolute single-node static lift bounded at 1.846 g: Penny (2.50 g), Dime (2.27 g), Ping-pong ball (2.70 g) all exceed; paper clip (1.0 g) and wooden match (0.5 g) hover safely. Universal scaling consequence of $V_{yield} \times \xi_{topo}$.
  - Macroscopic field limit $E_{yield} \approx 1.13 \times 10^{17}$ V/m is below the QED Schwinger limit by factor $\sqrt{\alpha}$.
  - YBCO phased array (per-node static lift summed across $10^6$ Hopf-knot inductors per m$^2$) predicted to give $\sim 24{,}480$ N (2.5 metric tons) of lift per square meter — the framework's pathway around the single-node 1.846 g cap.
- _Specific Non-Claims and Caveats_
  - "1.846 g" is a **single-actuator** static-grip ceiling. Phased arrays sum many actuators and bypass the limit by extensivity; this is asserted, not demonstrated.
  - "Dielectric Death Spiral" caveat (insulating a single wire to survive 43.65 kV transients exceeds 1.846 g for any standard magnet wire) is the framework's own admission that **classical copper wire cannot achieve 1G levitation** — single-actuator levitation is mathematically forbidden under the same axioms that predict it.
  - YBCO array prediction (2.5 metric tons / m$^2$) assumes drive at 59 kV per node "safely below the 60 kV saturation limit" — the 60 kV figure itself is the bulk-avalanche limit (vs the 43.65 kV point-yield); the per-node grip per actuator (2.49 g) is contingent on the chosen 59 kV operating point, not derived from a separately validated YBCO process.
  - Has NOT been experimentally demonstrated. Treat as a parameter-free prediction with a falsifiable threshold (no levitation above 1.846 g per single actuator), not a confirmed result.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/zero-parameter-derivations.md`, `falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md`, `falsification/ch11-experimental-bench-falsification/ybco-phased-array.md`, `falsification/ch11-experimental-bench-falsification/metric-refraction-capacitor.md`.

---

## Vacuum Impedance Mirror $\Gamma(V) = (Z_{local}/Z_0 - 1)/(Z_{local}/Z_0 + 1)$

- $Z_{local}(V) = Z_0 (1 - (V/V_{yield})^2)^{-1/4}$ → $\Gamma \to 1$ as $V \to V_{yield}$
- _Specific Claims_
  - Asymmetric saturation (only $\varepsilon$ scales by $S$) drives local impedance to infinity at $V_{yield}$ → photons reflect off pure DC-electrostatic gradient.
  - Falsification protocol: 100 µm tungsten micro-electrode gap, UHV (sub-$10^{-4}$ Torr to avoid Paschen arcing), $0.5$ mW probe laser, APD trap. Sweep $35$-$43$ kV DC; expected: non-linear exponential rise in back-scattered photons.
  - Detection of optical reflection from a static DC field falsifies linear QED.
- _Specific Non-Claims and Caveats_
  - Strict prerequisite: this is the **asymmetric** saturation case only — the symmetric-gravity invariance result ($Z = Z_0$) does not apply. Cross-cutting Symmetric vs Asymmetric Saturation entry is the canonical bound.
  - Does NOT claim the experiment has been performed or a positive result observed; the leaf provides the theoretical formula and protocol.
  - Several inbound references in the leaf (`\ref{sec:topological_defects_lc}`, `\ref{sec:point_yield}`, `\ref{eq:dielectric_saturation}`) are dangling — the in-leaf comment flags these as "presumed Vol 3 targets" and they are not resolved.
  - Hard distinction between "vacuum mirror" ($V_{yield}$ asymptotic strain, no rupture) vs "Zener avalanche" (impulse past $V_{yield}$, complete dielectric breakdown) is explicit in-leaf — summaries that conflate them describe two physically distinct boundary regimes.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md`.

---

## Vacuum Birefringence Discriminator: $E^4$ vs $E^2$

- AVE: $\Delta n \propto E^4$ (Taylor of $1 - \sqrt{1 - (E/E_{yield})^2}$); QED: $\Delta n \propto E^2$ (Euler-Heisenberg)
- _Specific Claims_
  - High-finesse cavity sweep through extreme DC field — the **scaling exponent** ($E^4$ vs $E^2$) cleanly separates AVE from QED.
  - IMD spectroscopy variant: dual-tone drive, IM3 amplitude scales as $V^3$ (AVE cubic) vs QED $V^6$; measurable above $\sim 30\%$ of $V_{yield}$ ($\sim 13$ kV).
- _Specific Non-Claims and Caveats_
  - The IMD predicted IM3 power table evaluated at lab-attainable drive levels gives strongly negative dBc values ($-160$ dBc at $1\%$ of $V_{yield}$); detection threshold is "Strong" only at $\sim 90\%$ of $V_{yield}$ ($\sim 39$ kV) per the leaf's own table. Any "easily measurable IM3 in standard labs" framing reads the high-drive end of the table as if it were attainable everywhere.
  - QED's predicted IM3 cross-section ($\sim 10^{-65}$ cm$^2$ at optical) is "$\sim 10^{40}$ times smaller than the AVE prediction at the same frequency" — the AVE prediction depends on the apparatus reaching $\sim 30\%$ of $V_{yield}/\ell_{node} \sim 3 \times 10^{16}$ V/m macroscopic field, which is far beyond current laboratory capability without resonant local enhancement.
  - Distinguishing $E^2$ from $E^4$ to within $\pm 0.5$ in the exponent is the falsification target; sub-decade dynamic range or systematic field-uncertainty would allow both fits.

> **Leaf references:** `falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`, `circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md`, `falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md`.

---

## Torus Knot Baryon Forward Predictions $(2,17), (2,19), (2,21)$

- $(2,17)$: $\sim 2742$ MeV, $(2,19)$: $\sim 2983$ MeV, $(2,21)$: $\sim 3199$ MeV; $\sim 170$ MeV per crossing
- _Specific Claims_
  - Six retrospective matches established (proton 0.00%, $\Delta(1232)$ 2.35%, $\Delta(1600)$ 1.11%, $\Delta(1900)$ 0.27%, $N(2190)$ 0.21%, $\Delta(2420)$ 2.40%) with **zero parameters adjusted between states**.
  - Three forward predictions for unobserved $(2, q)$ resonances, accessible to CLAS12 / PANDA.
  - Linear $\sim 170$ MeV/crossing spacing consistent with empirical Regge slope.
- _Specific Non-Claims and Caveats_
  - Falsification: no resonance within $\pm 100$ MeV of each prediction falsifies the ladder; departure from linear spacing at higher $c$ also falsifies. These are the framework's own falsification bounds, not unilateral confirmation criteria.
  - Per-row Δ% in the retrospective matches mixes "0.00%" (proton) with $\sim 2.4\%$ (top of error bar) — these are category (iv) derived predictions per the Master Prediction Table classification, but the proton 0.00% and the 2.40% are not the same kind of claim. The forward predictions inherit at least the 0.27%-2.40% scatter of the established matches.
  - Does NOT claim the forward predictions have been confirmed. They are open experimental targets.

> **Leaf references:** `falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md`. Cross-cutting: see Master Prediction Table reading conventions in `../claims-boundaries.md`.

---

## SPICE Particle Decay (Leaky Cavity) — Qualitative Muon Model

- LC tank ($L = 1$ mH, $C = 1$ nF, IC = 150 kV) discharging through voltage-controlled switch at $V > V_{yield}$
- _Specific Claims_
  - Heavy-fermion decay (e.g. muon) reproduced as RC-discharge time constant: standing wave exceeds $V_{yield}$ → $R_{eff}$ collapses from $1\,\text{G}\Omega$ to $50\,\Omega$ → exponential decay.
  - The 43.65 kV breakdown is **invariant under bulk dielectric environment**: a muon at the bottom of the Mariana Trench decays at the same RC-discharge rate as in vacuum, because the muon's sub-femtometer topology sits in the void space between molecular electron clouds.
- _Specific Non-Claims and Caveats_
  - **The SPICE RC muon model is qualitative.** This is project-wide Critical Distinction #5 (LIVING_REFERENCE.md): the SPICE netlist demonstrates the *mechanism* (voltage-triggered avalanche → RC discharge), not the *quantitative lifetime*. The quantitative muon lifetime comes from the standard Fermi formula with AVE-derived $G_F$ (3.9% accurate per Master Prediction Table #13).
  - Does NOT claim the SPICE netlist's specific $L$ and $C$ values reproduce the empirical muon lifetime. The 1 mH / 1 nF values give a particular $\tau$; the leaves do not derive the actual muon $\tau \approx 2.2$ µs from these.
  - Bulk-dielectric invariance is a structural / geometric argument; it is not a measurement of muon decay rates in dense media.

> **Leaf references:** `simulation/ch14-leaky-cavity-particle-decay/theory.md`, `simulation/ch14-leaky-cavity-particle-decay/spice-netlist.md`. Cross-cutting: LIVING_REFERENCE.md "Critical Distinctions" #5.

---

## Autoresonant PLL — Schwinger Limit Bypass Mechanism

- $C_{eff}(V) = C_0 \sqrt{1 - (V/V_{60k})^2}$ detunes a fixed-frequency drive; PLL tracks the dropping resonant frequency
- _Specific Claims_
  - The vacuum acts as a Duffing oscillator: its non-linear capacitance shifts the local resonance as drive amplitude rises, detuning fixed-frequency lasers and reflecting power back at the source.
  - A phase-locked loop tracking the instantaneous $f = 1/(2\pi\sqrt{LC_{eff}})$ allows a continuous-wave drive at far lower power to ring up the lattice past the Schwinger limit and trigger pair production.
- _Specific Non-Claims and Caveats_
  - This is an **engineering proposal / SPICE proof-of-concept**, not a demonstrated experiment. No leaf claims pair production has been induced via PLL drive at sub-petawatt levels.
  - The 60 kV "bulk-avalanche limit" used in this chain is distinct from $V_{yield}$ (43.65 kV) — see the $V_{yield}$ vs $V_{snap}$ entry above. The SPICE model uses 60 kV as the rupture threshold; the leaves do not reconcile this with the 43.65 kV figure quoted elsewhere.
  - Reflected-power detuning is a standard non-linear-resonator behavior; the framework's specific contribution is identifying the vacuum's $C(V)$ form and the PLL bypass — neither of which is independently measured at vacuum-rupture amplitudes.

> **Leaf references:** `simulation/ch15-autoresonant-breakdown/theory.md`, `falsification/ch12-falsifiable-predictions/autoresonant-dielectric-rupture.md`, `falsification/ch12-falsifiable-predictions/autoresonant-helicity.md`.

---

## Sapphire Phonon Centrifuge — Predicted 6.35 G Artificial Gravity

- $a_{LT} = v_{vac}^2 / r$ with $v_{vac} = v_{sound} \times (\rho_{Al_2O_3}/\rho_{bulk})$
- _Specific Claims_
  - 1 m sapphire sphere with phased ultrasonic transducers at 11{,}100 m/s sound speed → $v_{vac} \approx 5.58$ m/s → centripetal Lense-Thirring $\approx 62.3$ m/s$^2$ (6.35 G) at the center.
- _Specific Non-Claims and Caveats_
  - Treats $\rho_{bulk} = 7.91 \times 10^6$ kg/m$^3$ as a derived AVE constant; the prediction is downstream of that derivation — see the Sagnac-RLVE entry caveat about $\rho_{bulk}$ being framework-derived rather than independently measured.
  - Has NOT been experimentally tested. Predicted as an **industrial-scale artificial-gravity device**; engineering feasibility of trapping a stable acoustic vortex at 11.1 km/s in a 1 m sapphire sphere is asserted, not demonstrated.
  - "Inductive shield" framing (Beltrami coil + acoustic vortex → impenetrable boundary) is a structural / interpretive consequence, not an independent prediction.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/sapphire-phonon-centrifuge.md`.

---

## Optical Caustic Singularity Resolution

- $E_{\max}$ at focus bounded by $E_{YIELD} \approx 43.65$ kV/m (note: kV/m, not kV/m converted from $E_{yield}$)
- _Specific Claims_
  - Self-consistent 1D transmission-line solver caps focal intensity at the saturation boundary: as area shrinks, strain rises, $Z_{eff} = Z_0/\sqrt{S}$ stiffens, $\Gamma \to 1$ reflects converging rays back, finite focal waist replaces the classical caustic catastrophe.
  - Same saturation mechanism (asymmetric, electric-sector) used for the vacuum impedance mirror and the EE-bench plateau — operator-level consistency across applications.
- _Specific Non-Claims and Caveats_
  - Leaf states $E_{\max} = E_{YIELD} = \sqrt{\alpha} \cdot m_e c^2/e \approx 43.65$ **kV/m** — this is a leaf-level units inconsistency: the value 43.65 kV is the integrated $V_{yield}$, while 43.65 kV/m would be a specific field strength orders of magnitude below the macroscopic $E_{yield} \approx 1.13 \times 10^{17}$ V/m derived elsewhere. Treat the units in this leaf as suspect; the substantive claim (focal intensity bounded by the same asymmetric saturation kernel) is the load-bearing bound.
  - Does NOT claim the focal saturation has been experimentally observed; the leaf is a self-consistent solver result (Brent root-finding), not a measurement.
  - "Resolves the caustic catastrophe" is a structural / theoretical resolution within the AVE framework; classical optics already handles the singularity via diffraction corrections — AVE asserts a different resolution mechanism, not a numerical discrepancy with classical optics in any tested regime.

> **Leaf references:** `advanced-applications/ch20-optical-caustic-resolution/index.md`.

---

## Annihilation and Pair Production as Topological Mechanics

- $E_{knot} = \tfrac{1}{2}I\omega^2 \to E_{photon} = h\nu$; thresholds $2m_e c^2 = 1.022$ MeV ($\gamma\gamma$), $2m_p c^2 \approx 1876.5$ MeV ($p\bar p$)
- _Specific Claims_
  - $e^- e^+$ annihilation reframed as flywheel collision of opposite-handed Beltrami unknot vortices; rotational energy releases as photon.
  - Pair production reframed as transverse acoustic wave shear past $V_{yield}$, shedding one left- and one right-handed vortex (net topological charge zero).
  - All three processes (annihilation, pair production, $p\bar p$ → mesons) conserve topological charge, angular momentum, and energy.
- _Specific Non-Claims and Caveats_
  - This is an **interpretive reframing** of standard particle physics — the energy thresholds and kinematics are the standard results; AVE supplies a mechanical / topological mechanism rather than a probabilistic field-theoretic one.
  - Does NOT claim a quantitative rate prediction (cross-section, branching ratio) for any of these processes that differs from the Standard Model. The conservation laws and thresholds match.
  - $E = mc^2 = \tfrac{1}{2}LI^2 + \tfrac{1}{2}CV^2$ Virial decomposition is structural; not an independent rest-mass derivation.

> **Leaf references:** `advanced-applications/ch9-antimatter/annihilation-mechanism.md`.

---

## Definitive Binary Kill-Switches (Neutrino Parity, GRB Dispersion)

- _Specific Claims_
  - Detection of a stable, freely propagating right-handed neutrino permanently falsifies the $\tfrac{1}{3}G_{vac}$ microrotational boundary condition of the chiral LC bandgap → destroys the AVE Weak Force derivation.
  - Energy-dependent arrival-time delay (lattice dispersion) in trans-Planckian gamma-ray bursts falsifies the framework's photon-as-massless-link-variable claim.
- _Specific Non-Claims and Caveats_
  - These are **falsification criteria**, not predictions of detection. AVE asserts both should produce null results under current observation; positive detection of either falsifies the framework.
  - The leaf abbreviates a longer original list (the heading promises three but only two are present in this leaf; treat as the published subset).

> **Leaf references:** `falsification/ch12-falsifiable-predictions/binary-kill-switches.md`.

---

## Orbital Friction Paradox — Reactive vs Real Power

- $P_{real} = F_g \cdot v_{orb} \cos(90°) \equiv 0$ W for a stable circular orbit
- _Specific Claims_
  - Stable planetary orbit has radial gravity orthogonal to tangential velocity → $\theta = 90°$ → real power dissipation is identically zero → orbit is structurally a lossless LC tank operating in pure reactive power.
  - Eliminates the "vacuum drag" objection to AVE: inductive drag is suppressed by the dielectric phase transition ($\eta \to 0$), and the remaining gravitational coupling is purely orthogonal.
- _Specific Non-Claims and Caveats_
  - "$\theta = 90°$ → zero loss" is a **classical AC-power-analysis result** (real vs reactive power); AVE's contribution is identifying the orbital geometry as the physical realization of this circuit. Not an independent quantitative prediction.
  - Does NOT account for measurable orbital decay where $\theta \neq 90°$ (gravitational-wave inspiral, atmospheric drag, tidal dissipation) — these are framed as "$\theta \neq 90°$" perturbations consistent with the same framework. No quantitative match to observed inspiral rates is claimed in-leaf.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md`.

---
