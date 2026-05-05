# Vol 4 — Applied Vacuum Engineering — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol4/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 4; cross-cutting tripwires with vol4-specific manifestations are noted but not duplicated.

---

## Topological Conversion Constant $\xi_{topo} = e/\ell_{node}$
<!-- id: i9l284 -->

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

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## $V_{yield}$ vs $V_{snap}$ — Two Distinct Dielectric Thresholds
<!-- id: 0vxzfu -->

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

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Nonlinear Vacuum Capacitance $C_{eff}(V) = C_0/S(V)$ — Macroscopic Saturation
<!-- id: vjv4zf -->

- $C_{eff}(V) = C_0 / \sqrt{1 - (V/V_{yield})^2}$ (Axiom 4 applied to the electric sector)
- _Specific Claims_
  - The vacuum behaves as a metric varactor: capacitance diverges as $V \to V_{yield}$.
  - At $V \ll V_{yield}$, the leading correction is quadratic — formally identical to the Euler-Heisenberg low-field limit; recovers linear Maxwell to arbitrary precision.
  - The constitutive form is the Axiom 4 saturation kernel applied to the macroscopic electric sector specifically (as opposed to inductive, gravitational, or shear sectors).
- _Specific Non-Claims and Caveats_
  - This is the **asymmetric saturation** case (only $\varepsilon$ scales by $S$; $\mu$ unchanged). See cross-cutting Symmetric vs Asymmetric Saturation entry: in this case $Z = Z_0/\sqrt{S} \to \infty$ (medium opaque), not $Z = Z_0$ invariant. Do NOT apply the symmetric-gravity invariance result here.
  - The divergence at $V = V_{yield}$ is asymptotic in the constitutive equation, not a literal infinity in any physical apparatus — leaves consistently truncate the table at $V/V_{yield} = 1.000$ where the formula breaks down; SPICE implementations clamp the ratio (e.g. `min((V/V_YLD)^2, 0.9999)`).
  - Below $V_{yield}$ the framework reproduces the standard linear vacuum; the Vol 4 claim is the **shape** of the deviation (specifically the squared-radical form), not that linear electrodynamics is wrong in its domain.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md`, `circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md`, `simulation/ch18-universal-vacuum-cell/spice-subcircuit.md`, `simulation/ch17-hardware-netlists/ee-bench-netlist.md` (`ee_bench.cir` SPICE realization sweeping the $C_{eff}(V)=C_0\sqrt{1-(V/V_{yield})^2}$ plateau with the $>10\%$-deviation Anomaly Window above $\sim 37$ kV).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## $Z_0$ from Discrete LC Ladder, and Gravitational Stealth
<!-- id: kezk9z -->

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

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`, `circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`. Cross-cutting: see Symmetric vs Asymmetric Saturation in `../claim-quality.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Relativistic Inductor and SPICE Native Special Relativity
<!-- id: p5cf3t -->

- $L_{eff}(I) = L_0/\sqrt{1 - (I/I_{max})^2}$, $I_{max} = \xi_{topo}\, c \approx 124.4$ A
- _Specific Claims_
  - Form is identical to the varactor with $V \to I$, $V_{yield} \to I_{max}$ — both are projections of the single Axiom 4 kernel onto the magnetic and electric sectors respectively.
  - Energy stored expands at low $v$ to $E = \tfrac{1}{2}\gamma m_0 v^2$, and the rest-energy term sums via Virial Theorem to $E_{total} = m_0 c^2$ — recovers $E = mc^2$.
  - SPICE transient simulators of this constitutive equation natively enforce $v \le c$ without code modification, because $L_{eff} \to \infty$ at $I_{max}$ collapses the slew rate.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a new derivation of Special Relativity from independent axioms. The mapping shows the Lorentz-saturation form is structurally a circuit-element constraint; SR-equivalent kinematics are reproduced, not novelly predicted.
  - The "particle as resonant LC tank, $E = m_e c^2 = \tfrac{1}{2}LI^2 + \tfrac{1}{2}CV^2$" mapping is structural (Virial decomposition), not an independent rest-mass derivation — $m_e$ is taken as given.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md`, `circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Operating Regime for PONDER and Lab Devices — Regime I
<!-- id: trgqtf -->

- $E/E_{yield}$ classification: I ($< 0.1$), II ($0.1$-$0.5$), III ($0.5$-$1.0$), IV ($\ge 1.0$); $E_{yield} \approx 1.13 \times 10^{17}$ V/m
- _Specific Claims_
  - PONDER-01 at 30 kV / 1 mm gap → $E/E_{yield} \approx 2.7 \times 10^{-10}$ → firmly Regime I (linear vacuum).
  - The leaf is explicit: **bulk $\varepsilon$-saturation is not the operative thrust mechanism** at lab scale. The thrust mechanism arises from chiral topology of the antenna producing asymmetric acoustic emission, with local field amplification (tip enhancement $\beta \times$ resonant $Q$) producing Jensen's-inequality rectification at the tips.
  - Regime III/IV are reached only at sub-femtometer separations: particle cores, nuclear scattering boundaries, event horizons. This places the bulk-yielding limit far from any lab apparatus.
- _Specific Non-Claims and Caveats_
  - Vol 4 does NOT claim PONDER measures bulk vacuum saturation. Summaries that frame PONDER as "tabletop dielectric saturation" misread the regime classification.
  - The 4-regime $E/E_{yield}$ table has finer cutoffs than the master 4-regime table in LIVING_REFERENCE.md (which uses $\sqrt{2\alpha}$ and $\sqrt{3}/2$ as boundaries). The Vol 4 cutoffs (0.1 / 0.5 / 1.0) are convenience thresholds for the macroscopic constitutive plot; they do not replace the master regime boundaries.

> **Leaf references:** `circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md`, `falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md`, `falsification/ch12-falsifiable-predictions/ee-bench-plateau.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Chiral Acoustic Rectification Thrust (PONDER-01)
<!-- id: 7tynm2 -->

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

> **Leaf references:** `circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md`, `circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md`, `falsification/ch11-experimental-bench-falsification/open-source-hardware.md` (PONDER-01 build guide), `falsification/ch11-experimental-bench/pcba-bench-protocols.md` (consolidated PCBA bench protocol summary), `simulation/ch17-hardware-netlists/ponder-01-stack-netlist.md` (cascaded LC stack SPICE realization). PONDER-05 number sourced only from `vol4/index.md`; no leaf supports it.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## HOPF-01 Chiral Antenna $\Delta f/f = \alpha \cdot pq/(p+q)$
<!-- id: wzezvt -->

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

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/open-source-hardware.md`, `falsification/ch11-experimental-bench-falsification/project-hopf-02.md` (HOPF-02 VNA $S_{11}$ chiral-impedance-match falsifier), `falsification/ch11-experimental-bench/pcba-bench-protocols.md` (consolidated PCBA summary including HOPF-02), `future-geometries/ch13-future-geometries/high-q-chiral-antenna.md`, `future-geometries/ch13-future-geometries/k4-tlm-simulator.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## K4-TLM Diamond Lattice — Unitarity to Machine Epsilon
<!-- id: hd9bee -->

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

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## CEM Method Mappings (MoM, FDTD, FEM, TLM, CMA, PO/GO)
<!-- id: u462e4 -->

- $[\mathbf{Z}][\mathbf{I}] = [\mathbf{V}]$ (MoM); $[\mathbf{S}]\{\mathbf{E}\} = k_0^2[\mathbf{T}]\{\mathbf{E}\}$ (FEM); etc.
- _Specific Claims_
  - Each standard CEM solver's governing equation is **structurally identical** to an AVE lattice statement (MoM circuit equation, Yee = LC grid, FEM = $\omega^2 LC = 1$, TLM = direct LC isomorphism, CMA = LC eigenmode decomposition, PO/GO = continuum limit).
  - Each CEM method "independently rediscovers" a discretized LC network as the correct computational substrate.
- _Specific Non-Claims and Caveats_
  - This is an **interpretive identification**, not a derivation. The CEM equations were derived from Maxwell's equations; AVE asserts they ARE the lattice equations because Maxwell's equations are the lattice equations in the continuum limit. This claim is not independent of the broader AVE-vs-Maxwell ontology claim.
  - Does NOT claim that running a CEM solver on a torus knot validates any AVE-specific prediction beyond what Maxwell already predicts. CEM agreement with AVE-shaped predictions follows trivially because both inherit the same Maxwell substrate; the AVE-specific claim ($\Delta f/f = \alpha \cdot pq/(p+q)$) is the topological coupling factor, not the underlying RF mechanics.

> **Leaf references:** `future-geometries/ch13-future-geometries/cem-methods-survey.md`, `circuit-theory/ch1-vacuum-circuit-analysis/computational-solver-selection.md`, `circuit-theory/ch1-vacuum-circuit-analysis/solver-selection.md` (concise FDTD-vs-K4-TLM decision matrix variant of the same mapping).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Tokamak Ignition Paradox and Metric-Catalyzed Fusion ($n^* = 1.114$)
<!-- id: qagkgy -->

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

> **Leaf references:** `advanced-applications/ch8-applied-fusion/tokamak-paradox.md`, `advanced-applications/ch8-applied-fusion/ignition-criterion.md`, `advanced-applications/ch8-applied-fusion/ave-fusion-device.md`, `advanced-applications/ch8-applied-fusion/radius-scaling.md` (Bohr-radius compression $r(n)=a_0/n$ and $V_{topo}(n)=V_{topo,0}/n^3$ derivation), `advanced-applications/ch8-applied-fusion/temperature-scaling.md` (WKB derivation of $T_{ign}(n)=T_0/n^2$), `advanced-applications/ch8-applied-fusion/gamow-compressed.md` (compressed Gamow exponent $\eta(n)=\eta_0/n$), `advanced-applications/ch8-applied-fusion/vtopo-scaling.md` (topological-velocity $V_{topo}(n)=V_{topo,0}/n^3$ scaling and three operating-regime rules), `falsification/ch11-experimental-bench/zero-parameter-derivations.md` (consolidated $\sqrt{\alpha}$ alignment with the 60.3 kV fusion strain).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Topological SMES (Beltrami $(p,q)$ Torus Knot)
<!-- id: 6btlq3 -->

- 87.9% reduction in external stray flux for a $(150, 3)$ torus knot vs solenoid of identical volume/current
- _Specific Claims_
  - The Beltrami condition $\nabla \times \mathbf{B} = \lambda \mathbf{B}$ enforces $\mathbf{J} \parallel \mathbf{B}$ — Lorentz cross-product $\mathbf{J} \times \mathbf{B}$ vanishes structurally → zero internal tension, no heavy bracing.
  - Biot-Savart computational solver shows 87.9% stray-flux reduction for the chosen knot vs equivalent solenoid.
- _Specific Non-Claims and Caveats_
  - 87.9% is a **simulation result for one specific topology** ($(150, 3)$ torus knot), not a universal lower bound. The "macroscopic electron" framing is structural / interpretive.
  - Does NOT claim a built SMES device has been measured. The chapter establishes the engineering pathway and computational falsification of the leakage claim, not hardware validation.
  - "Zero internal structural tension" is the limit of an ideal Beltrami field; real-world wire stiffness, joint resistance, and finite-conductor corrections are not addressed in the leaves.

> **Leaf references:** `advanced-applications/ch7-topological-smes/smes-topology.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Topological Qubit (Gauss Linking) and Casimir Cavity Shielding
<!-- id: 07wvul -->

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

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Active Topological Metamaterials (Inorganic LLCP)
<!-- id: ffa5sq -->

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

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Native Silicon Design Engine (Doping, BJT $\beta$, `atopile` Compilation)
<!-- id: 0hwopi -->

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

> **Leaf references:** `advanced-applications/ch19-silicon-design-engine/doping-geometric-perturbation.md`, `advanced-applications/ch19-silicon-design-engine/topological-bjt-gain.md`, `advanced-applications/ch19-silicon-design-engine/declarative-ato-compilation.md`, `advanced-applications/ch19-silicon-design-engine/native-spice-subcircuit.md`, `advanced-applications/ch19-silicon-design-engine/pn-junction-s-parameter.md` (P-N junction as $S_{11}$ impedance-step boundary; silicon at $V_R/V_{BR}=0.050$).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Sagnac-RLVE: Tabletop Falsification, $\Delta\phi \approx 2.07$ rad, $\Psi \approx 7.15$
<!-- id: wqmb19 -->

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

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`, `falsification/ch11-experimental-bench/sagnac-rlve.md` (consolidated), `falsification/ch11-experimental-bench-falsification/sagnac-parallax.md` (24-hour static-loop variant against the 370 km/s CMB-dipole metric wind), `falsification/ch12-falsifiable-predictions/active-sagnac-impedance-drag.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## $\sqrt{\alpha}$ Yield Limit Predictions: Levitation 1.846 g, $E_{yield} = 1.13 \times 10^{17}$ V/m
<!-- id: ui3m8a -->

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

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/zero-parameter-derivations.md`, `falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md`, `falsification/ch11-experimental-bench-falsification/ybco-phased-array.md`, `falsification/ch11-experimental-bench-falsification/metric-refraction-capacitor.md`, `falsification/ch11-experimental-bench/industrial-scaleup.md` (consolidated levitation limit + dielectric death spiral + YBCO array + metric-refraction capacitor + sapphire centrifuge), `falsification/ch11-experimental-bench/zero-parameter-derivations.md` (consolidated $\sqrt{\alpha}$-yield alignment with levitation and fusion limits).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Vacuum Impedance Mirror $\Gamma(V) = (Z_{local}/Z_0 - 1)/(Z_{local}/Z_0 + 1)$
<!-- id: 5s5b0d -->

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

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md`, `falsification/ch11-experimental-bench/advanced-protocols.md` (Protocol 11 condensed restatement of the $\Gamma(V)\to 1$ derivation and APD-back-scatter falsification protocol).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Vacuum Birefringence Discriminator: $E^4$ vs $E^2$
<!-- id: pp3qwf -->

- AVE: $\Delta n \propto E^4$ (Taylor of $1 - \sqrt{1 - (E/E_{yield})^2}$); QED: $\Delta n \propto E^2$ (Euler-Heisenberg)
- _Specific Claims_
  - High-finesse cavity sweep through extreme DC field — the **scaling exponent** ($E^4$ vs $E^2$) cleanly separates AVE from QED.
  - IMD spectroscopy variant: dual-tone drive, IM3 amplitude scales as $V^3$ (AVE cubic) vs QED $V^6$; measurable above $\sim 30\%$ of $V_{yield}$ ($\sim 13$ kV).
- _Specific Non-Claims and Caveats_
  - The IMD predicted IM3 power table evaluated at lab-attainable drive levels gives strongly negative dBc values ($-160$ dBc at $1\%$ of $V_{yield}$); detection threshold is "Strong" only at $\sim 90\%$ of $V_{yield}$ ($\sim 39$ kV) per the leaf's own table. Any "easily measurable IM3 in standard labs" framing reads the high-drive end of the table as if it were attainable everywhere.
  - QED's predicted IM3 cross-section ($\sim 10^{-65}$ cm$^2$ at optical) is "$\sim 10^{40}$ times smaller than the AVE prediction at the same frequency" — the AVE prediction depends on the apparatus reaching $\sim 30\%$ of $V_{yield}/\ell_{node} \sim 3 \times 10^{16}$ V/m macroscopic field, which is far beyond current laboratory capability without resonant local enhancement.
  - Distinguishing $E^2$ from $E^4$ to within $\pm 0.5$ in the exponent is the falsification target; sub-decade dynamic range or systematic field-uncertainty would allow both fits.

> **Leaf references:** `falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`, `circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md`, `falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md`, `falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md` (Birefringence Kill-Switch as the third binary discriminator, evaluated from the Axiom-4 Taylor expansion), `falsification/ch11-experimental-bench/epistemology-kill-switches.md` (consolidated $E^2$-vs-$E^4$ slope statement).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Torus Knot Baryon Forward Predictions $(2,17), (2,19), (2,21)$
<!-- id: to41c7 -->

- $(2,17)$: $\sim 2742$ MeV, $(2,19)$: $\sim 2983$ MeV, $(2,21)$: $\sim 3199$ MeV; $\sim 170$ MeV per crossing
- _Specific Claims_
  - Six retrospective matches established (proton 0.00%, $\Delta(1232)$ 2.35%, $\Delta(1600)$ 1.11%, $\Delta(1900)$ 0.27%, $N(2190)$ 0.21%, $\Delta(2420)$ 2.40%) with **zero parameters adjusted between states**.
  - Three forward predictions for unobserved $(2, q)$ resonances, accessible to CLAS12 / PANDA.
  - Linear $\sim 170$ MeV/crossing spacing consistent with empirical Regge slope.
- _Specific Non-Claims and Caveats_
  - Falsification: no resonance within $\pm 100$ MeV of each prediction falsifies the ladder; departure from linear spacing at higher $c$ also falsifies. These are the framework's own falsification bounds, not unilateral confirmation criteria.
  - Per-row Δ% in the retrospective matches mixes "0.00%" (proton) with $\sim 2.4\%$ (top of error bar) — these are category (iv) derived predictions per the Master Prediction Table classification, but the proton 0.00% and the 2.40% are not the same kind of claim. The forward predictions inherit at least the 0.27%-2.40% scatter of the established matches.
  - Does NOT claim the forward predictions have been confirmed. They are open experimental targets.

> **Leaf references:** `falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md`, `falsification/ch12-falsifiable-predictions/baryon-mass-predictions.md` (consolidated $(2,q)$ ladder retrospective + forward predictions table). Cross-cutting: see Master Prediction Table reading conventions in `../claim-quality.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## SPICE Particle Decay (Leaky Cavity) — Qualitative Muon Model
<!-- id: c54kdd -->

- LC tank ($L = 1$ mH, $C = 1$ nF, IC = 150 kV) discharging through voltage-controlled switch at $V > V_{yield}$
- _Specific Claims_
  - Heavy-fermion decay (e.g. muon) reproduced as RC-discharge time constant: standing wave exceeds $V_{yield}$ → $R_{eff}$ collapses from $1\,\text{G}\Omega$ to $50\,\Omega$ → exponential decay.
  - The 43.65 kV breakdown is **invariant under bulk dielectric environment**: a muon at the bottom of the Mariana Trench decays at the same RC-discharge rate as in vacuum, because the muon's sub-femtometer topology sits in the void space between molecular electron clouds.
- _Specific Non-Claims and Caveats_
  - **The SPICE RC muon model is qualitative.** This is project-wide Critical Distinction #5 (LIVING_REFERENCE.md): the SPICE netlist demonstrates the *mechanism* (voltage-triggered avalanche → RC discharge), not the *quantitative lifetime*. The quantitative muon lifetime comes from the standard Fermi formula with AVE-derived $G_F$ (3.9% accurate per Master Prediction Table #13).
  - Does NOT claim the SPICE netlist's specific $L$ and $C$ values reproduce the empirical muon lifetime. The 1 mH / 1 nF values give a particular $\tau$; the leaves do not derive the actual muon $\tau \approx 2.2$ µs from these.
  - Bulk-dielectric invariance is a structural / geometric argument; it is not a measurement of muon decay rates in dense media.

> **Leaf references:** `simulation/ch14-leaky-cavity-particle-decay/theory.md`, `simulation/ch14-leaky-cavity-particle-decay/spice-netlist.md`. Cross-cutting: LIVING_REFERENCE.md "Critical Distinctions" #5.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Autoresonant PLL — Schwinger Limit Bypass Mechanism
<!-- id: 9sujp8 -->

- $C_{eff}(V) = C_0 \sqrt{1 - (V/V_{60k})^2}$ detunes a fixed-frequency drive; PLL tracks the dropping resonant frequency
- _Specific Claims_
  - The vacuum acts as a Duffing oscillator: its non-linear capacitance shifts the local resonance as drive amplitude rises, detuning fixed-frequency lasers and reflecting power back at the source.
  - A phase-locked loop tracking the instantaneous $f = 1/(2\pi\sqrt{LC_{eff}})$ allows a continuous-wave drive at far lower power to ring up the lattice past the Schwinger limit and trigger pair production.
- _Specific Non-Claims and Caveats_
  - This is an **engineering proposal / SPICE proof-of-concept**, not a demonstrated experiment. No leaf claims pair production has been induced via PLL drive at sub-petawatt levels.
  - The 60 kV "bulk-avalanche limit" used in this chain is distinct from $V_{yield}$ (43.65 kV) — see the $V_{yield}$ vs $V_{snap}$ entry above. The SPICE model uses 60 kV as the rupture threshold; the leaves do not reconcile this with the 43.65 kV figure quoted elsewhere.
  - Reflected-power detuning is a standard non-linear-resonator behavior; the framework's specific contribution is identifying the vacuum's $C(V)$ form and the PLL bypass — neither of which is independently measured at vacuum-rupture amplitudes.

> **Leaf references:** `simulation/ch15-autoresonant-breakdown/theory.md`, `simulation/ch15-autoresonant-breakdown/spice-netlist.md` (`pll_breakdown.cir` realization with behavioral $C_{eff}(V)$ and PLL phase integrator), `falsification/ch12-falsifiable-predictions/autoresonant-dielectric-rupture.md`, `falsification/ch12-falsifiable-predictions/autoresonant-helicity.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Sapphire Phonon Centrifuge — Predicted 6.35 G Artificial Gravity
<!-- id: iz3svl -->

- $a_{LT} = v_{vac}^2 / r$ with $v_{vac} = v_{sound} \times (\rho_{Al_2O_3}/\rho_{bulk})$
- _Specific Claims_
  - 1 m sapphire sphere with phased ultrasonic transducers at 11{,}100 m/s sound speed → $v_{vac} \approx 5.58$ m/s → centripetal Lense-Thirring $\approx 62.3$ m/s$^2$ (6.35 G) at the center.
- _Specific Non-Claims and Caveats_
  - Treats $\rho_{bulk} = 7.91 \times 10^6$ kg/m$^3$ as a derived AVE constant; the prediction is downstream of that derivation — see the Sagnac-RLVE entry caveat about $\rho_{bulk}$ being framework-derived rather than independently measured.
  - Has NOT been experimentally tested. Predicted as an **industrial-scale artificial-gravity device**; engineering feasibility of trapping a stable acoustic vortex at 11.1 km/s in a 1 m sapphire sphere is asserted, not demonstrated.
  - "Inductive shield" framing (Beltrami coil + acoustic vortex → impenetrable boundary) is a structural / interpretive consequence, not an independent prediction.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/sapphire-phonon-centrifuge.md`, `falsification/ch11-experimental-bench/industrial-scaleup.md` (consolidated industrial-scale write-up of the sapphire centrifuge alongside the YBCO array and metric-refraction capacitor).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Optical Caustic Singularity Resolution
<!-- id: uosu8w -->

- $E_{\max}$ at focus bounded by $E_{YIELD} \approx 43.65$ kV/m (note: kV/m, not kV/m converted from $E_{yield}$)
- _Specific Claims_
  - Self-consistent 1D transmission-line solver caps focal intensity at the saturation boundary: as area shrinks, strain rises, $Z_{eff} = Z_0/\sqrt{S}$ stiffens, $\Gamma \to 1$ reflects converging rays back, finite focal waist replaces the classical caustic catastrophe.
  - Same saturation mechanism (asymmetric, electric-sector) used for the vacuum impedance mirror and the EE-bench plateau — operator-level consistency across applications.
- _Specific Non-Claims and Caveats_
  - Leaf states $E_{\max} = E_{YIELD} = \sqrt{\alpha} \cdot m_e c^2/e \approx 43.65$ **kV/m** — this is a leaf-level units inconsistency: the value 43.65 kV is the integrated $V_{yield}$, while 43.65 kV/m would be a specific field strength orders of magnitude below the macroscopic $E_{yield} \approx 1.13 \times 10^{17}$ V/m derived elsewhere. Treat the units in this leaf as suspect; the substantive claim (focal intensity bounded by the same asymmetric saturation kernel) is the load-bearing bound.
  - Does NOT claim the focal saturation has been experimentally observed; the leaf is a self-consistent solver result (Brent root-finding), not a measurement.
  - "Resolves the caustic catastrophe" is a structural / theoretical resolution within the AVE framework; classical optics already handles the singularity via diffraction corrections — AVE asserts a different resolution mechanism, not a numerical discrepancy with classical optics in any tested regime.

> **Leaf references:** `advanced-applications/ch20-optical-caustic-resolution/index.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Annihilation and Pair Production as Topological Mechanics
<!-- id: 5rigtn -->

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

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Definitive Binary Kill-Switches (Neutrino Parity, GRB Dispersion)
<!-- id: gw2wgc -->

- _Specific Claims_
  - Detection of a stable, freely propagating right-handed neutrino permanently falsifies the $\tfrac{1}{3}G_{vac}$ microrotational boundary condition of the chiral LC bandgap → destroys the AVE Weak Force derivation.
  - Energy-dependent arrival-time delay (lattice dispersion) in trans-Planckian gamma-ray bursts falsifies the framework's photon-as-massless-link-variable claim.
- _Specific Non-Claims and Caveats_
  - These are **falsification criteria**, not predictions of detection. AVE asserts both should produce null results under current observation; positive detection of either falsifies the framework.
  - The leaf abbreviates a longer original list (the heading promises three but only two are present in this leaf; treat as the published subset).

> **Leaf references:** `falsification/ch12-falsifiable-predictions/binary-kill-switches.md`, `falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md` (Neutrino Parity, GRB Dispersion, and the $E^2$-vs-$E^4$ Birefringence Kill-Switch enumerated together), `falsification/ch11-experimental-bench/epistemology-kill-switches.md` (consolidated three-binary-kill-switches restatement).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Orbital Friction Paradox — Reactive vs Real Power
<!-- id: v6ti0v -->

- $P_{real} = F_g \cdot v_{orb} \cos(90°) \equiv 0$ W for a stable circular orbit
- _Specific Claims_
  - Stable planetary orbit has radial gravity orthogonal to tangential velocity → $\theta = 90°$ → real power dissipation is identically zero → orbit is structurally a lossless LC tank operating in pure reactive power.
  - Eliminates the "vacuum drag" objection to AVE: inductive drag is suppressed by the dielectric phase transition ($\eta \to 0$), and the remaining gravitational coupling is purely orthogonal.
- _Specific Non-Claims and Caveats_
  - "$\theta = 90°$ → zero loss" is a **classical AC-power-analysis result** (real vs reactive power); AVE's contribution is identifying the orbital geometry as the physical realization of this circuit. Not an independent quantitative prediction.
  - Does NOT account for measurable orbital decay where $\theta \neq 90°$ (gravitational-wave inspiral, atmospheric drag, tidal dissipation) — these are framed as "$\theta \neq 90°$" perturbations consistent with the same framework. No quantitative match to observed inspiral rates is claimed in-leaf.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## CLEAVE-01 Femto-Coulomb Electrometer ($Q = \xi_{topo}\, x = 0.415$ pC/$\mu$m)
<!-- id: ydksh6 -->

- A PZT-driven 1 µm gap step generates $Q = \xi_{topo}\, x = 4.149 \times 10^{-7}\,\text{C/m} \times 10^{-6}\,\text{m} = 0.415$ pC; into a 10 pF parasitic this reads $V = Q/C = 41.5$ mV per micron.
- _Specific Claims_
  - Direct hardware test of the topo-kinematic identity $Q \equiv \xi_{topo}\, x$ (Vol 4 Ch.1) at the macroscopic-mechanical scale.
  - Zero free parameters: the predicted 41.5 mV step depends only on $\xi_{topo}$, the 1 µm displacement, and the (controlled) 10 pF parasitic input capacitance. No fitted couplings.
  - Hardware spec is COTS: ADA4530-1 ultra-low-bias electrometer ($\sim 20$ fA bias), guard rings, Teflon standoffs, PZT linear actuator stepping in $<100$ ms.
  - Falsification: a step of $0.0$ mV permanently falsifies $\xi_{topo}$ as a hardware constant; a step of exactly $41.5$ mV per micron validates the topological conversion constant on a tabletop.
- _Specific Non-Claims and Caveats_
  - Has NOT been performed; the leaf gives the protocol and the predicted readout. Treat as a falsifiable protocol, not a confirmed result.
  - The 41.5 mV magnitude is contingent on the assumed 10 pF parasitic input capacitance; deviations in the actual board parasitics rescale the readout linearly via $V = Q/C$ — a different parasitic does not falsify the framework, it rescales the predicted step. Builders must measure $C$ in-circuit to interpret the result.
  - The 1 µm step in $<100$ ms is an engineering choice for SNR; the prediction is on the per-micron step, not the timing.
  - The leaf carries an in-source comment flagging an authoring error: the $Q \equiv \xi_{topo} x$ identity is defined in Ch.01 (topological-kinematics), not Ch.13 as the protocol text states. The physics binding is to Ch.01.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/project-cleave-01.md`, `falsification/ch11-experimental-bench/pcba-bench-protocols.md` (consolidated PCBA bench protocols, CLEAVE-01 entry).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## ROENTGEN-03 Solid-State Sagnac Induction ($B \approx 4.2$ pT)
<!-- id: qsgl7d -->

- Spinning a non-metallic dense ceramic disk at 10k RPM creates $v_{vac} \approx 0.038$ m/s at $r=5$ cm; an interdigitated capacitor driven at 10 kV / 1 kHz overhead synthesizes a $B \approx 4.2$ pT alternating field via $\mathbf{B} = (1/c^2)\,\mathbf{v} \times \mathbf{E}$ acting on the induced vacuum drift.
- _Specific Claims_
  - Roentgen's 1888 moving-dielectric induction extended to the bulk vacuum metric: spinning a neutral mass macroscopically phase-shifts $\mathcal{M}_A$ via mutual inductance, allowing a B-field to be synthesized from the vacuum's own induced drift rather than from any embedded current.
  - The 4.2 pT prediction induces $\sim 0.26\,\mu$V in a differential planar pickup coil. Standard hardware Lock-In amplifier extracts the signal from noise floor.
  - Falsification: amplitude must scale strictly linearly with RPM and flip phase $180°$ on motor reversal. Substrate signature: failure of either scaling falsifies the inductive density $\rho_{bulk} \approx 7.9 \times 10^6$ kg/m$^3$ at this scale.
- _Specific Non-Claims and Caveats_
  - Has NOT been performed; this is the proposed protocol with predicted readout.
  - The 0.038 m/s drift velocity uses the Sagnac-RLVE entrainment chain: it is contingent on the same framework-derived $\rho_{bulk}$ as the Sagnac-RLVE signal — see the Sagnac-RLVE entry's caveat about $\rho_{bulk}$ being framework-derived.
  - Lock-In SNR is asserted; no leaf-level noise budget proves the $\sim 0.26\,\mu$V signal is recoverable in the presence of motor EMI, mains hum, and ground-loop noise typical of high-RPM rigs.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/project-roentgen-03.md`, `falsification/ch11-experimental-bench/pcba-bench-protocols.md` (consolidated PCBA bench protocols, ROENTGEN-03 entry).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## ZENER-04 Impedance Avalanche Detector — Anomalous Knee at 43.65 kV
<!-- id: cltls0 -->

- 80 kV transient (sub-µs rise) into an encapsulated spherical electrode in vacuum; AVE predicts an anomalous "Avalanche Knee" — a sudden non-linear spike in displacement current $I_D = C\,dV/dt$ at the moment the localized field crosses $V_{yield} = 43.65$ kV.
- _Specific Claims_
  - The vacuum LC network behaves identically to a Transient Voltage Suppression (TVS) Zener diode: rigid $Z_0 \approx 377\,\Omega$ until $V > V_{yield}$, then absolute impedance rupture ($\Gamma = -1$) drops the effective impedance to zero.
  - Standard linear electrostatics predicts $I_D = C\,dV/dt$ remains perfectly linear during charging of an isolated spherical capacitor; AVE predicts a distinct, anomalous discontinuity exactly at the topological yield voltage.
  - Falsification: a perfectly linear $I_D(V)$ across the 43.65 kV crossing falsifies the impedance-rupture mechanism that underlies the SPICE leaky-cavity model, the autoresonant PLL bypass, and the Zener-avalanche side of the vacuum impedance mirror.
- _Specific Non-Claims and Caveats_
  - Has NOT been performed; this is the proposed Marx-generator protocol.
  - The 43.65 kV figure is the same $V_{yield} = \sqrt{\alpha} \cdot m_e c^2/e$ used elsewhere in Vol 4. Note that several adjacent leaves (autoresonant-breakdown, levitation-array) instead use 60 kV as the avalanche threshold — see the $V_{yield}$ vs $V_{snap}$ entry for the regime distinction; ZENER-04 specifically targets the 43.65 kV onset.
  - "Encapsulated spherical electrode in vacuum" is a hardware mitigation for atmospheric Paschen arcing; classical surface-arc artefacts inside an imperfect chamber would mimic an avalanche knee and must be excluded by the vacuum quality. The leaf does not specify a vacuum-quality threshold.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/project-zener-04.md`, `falsification/ch11-experimental-bench/pcba-bench-protocols.md` (consolidated PCBA bench protocols, ZENER-04 entry).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## TORSION-05 Horizontal Metric Rectification — $\sim 100\,\mu$N DC Thrust
<!-- id: kl1ern -->

- A heavily-potted TAMD PCBA on a Cavendish torsion pendulum in $10^{-6}$ Torr vacuum, driven by an asymmetric SiC-MOSFET / ferrite-flyback waveform: slow-edge $+500$ V grip generates $+0.207$ mN forward thrust ($V \ll V_{yield}$); fast-edge $-75$ kV kickback ($> V_{yield}$) ruptures the metric and produces $0$ mN backward reaction. Time-averaged net DC thrust $\sim 100\,\mu$N.
- _Specific Claims_
  - Bypasses the 1.846 g vertical levitation cap by working on a horizontal torsion balance: lateral resistance is effectively $0$G, allowing continuous micro-Newton thrust measurement.
  - The asymmetric flyback exploits the $V_{yield}$ threshold as a one-way impedance valve: the slow charge edge (below $V_{yield}$) couples to a matched $377\,\Omega$ vacuum line; the fast snap-off (above $V_{yield}$) finds a ruptured ($\Gamma=-1$) vacuum that returns no reaction force. Net: a continuous DC thrust per cycle.
  - Falsification: the pendulum remaining perfectly stationary inside the chamber falsifies the asymmetric-impedance / one-way-valve mechanism on which the LC non-linear geometry rests.
- _Specific Non-Claims and Caveats_
  - Has NOT been performed; this is the proposed protocol.
  - The $+0.207$ mN forward grip and $0$ mN backward reaction are the framework's idealized step-function — the calculated time-averaged $\sim 100\,\mu$N assumes perfect rectification at the $V_{yield}$ crossing. Real-world rise-time finite-bandwidth effects of the 75 kV flyback (even at $<10$ ns) will leak some backward reaction into the average; the leaf does not quantify this floor.
  - The 75 kV figure is the inductive kickback magnitude; this is the same $|V| > V_{yield}$ rupture regime claimed in the ZENER-04 protocol and the autoresonant PLL — see also the $V_{yield}$ vs $V_{snap}$ entry. TORSION-05 specifically rests on the 43.65 kV crossing being a reaction-free wall.
  - Cavendish pendulums are sensitive to electrostatic patch potentials, residual gas drift, and seismic micro-tremor at the 100 µN level; the leaf identifies the chamber and suspension but does not enumerate these systematic backgrounds.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/project-torsion-05.md`, `falsification/ch11-experimental-bench/pcba-bench-protocols.md` (consolidated PCBA bench protocols, TORSION-05 entry).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Achromatic Impedance Lens (Protocol 9) — $\Gamma = 0$ Across All Angles
<!-- id: k9up5c -->

- Gravity scales $\mu(r)$ and $\varepsilon(r)$ proportionally → $Z_{gravity} = \sqrt{\mu_0\, n(r)/(\varepsilon_0\, n(r))} = Z_0$, identically. A laboratory metamaterial dielectric with $\mu_r$ and $\varepsilon_r$ co-doped at the same radial gradient should mimic a gravitational well and exhibit $\Gamma = 0$ at all incidence angles, bypassing classical Fresnel reflection.
- _Specific Claims_
  - Identifies gravity as an *achromatic* impedance lens: the physical reason photons bend in a gravitational well without producing any Fresnel reflection (no $S_{11}$ return) is that $\mu$ and $\varepsilon$ scale together, preserving the characteristic impedance.
  - Provides a benchtop falsifier: a co-doped $\mu_r$/$\varepsilon_r$ metamaterial under VNA or optical-laser sweep should display physically zero reflection across all angles — a signature standard non-engineered metamaterials cannot reproduce.
  - Sharp discriminator vs. standard impedance-mismatched lenses (whose $\Gamma$ rises with angle off normal).
- _Specific Non-Claims and Caveats_
  - This is the asymmetric-vs-symmetric saturation distinction that anchors the cross-cutting Symmetric-vs-Asymmetric Saturation entry. The Achromatic Lens prediction is the *symmetric* invariance result; the Vacuum Impedance Mirror entry is the *asymmetric* divergence result. Do NOT mix the two: the same axiom set produces opposite reflection behavior depending on which constitutive parameter is strained.
  - Has NOT been demonstrated. Co-doping $\mu_r$ and $\varepsilon_r$ at exactly proportional radial gradients is itself a non-trivial fabrication problem; achievable proportionality is asserted, not built.
  - "Mimics a gravitational well" is structural — the metamaterial reproduces the impedance signature, not the curvature of spacetime; the experiment falsifies the impedance-pair hypothesis, not General Relativity directly.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/achromatic-lens-test.md`, `falsification/ch11-experimental-bench/advanced-protocols.md` (consolidated Protocol 9 statement).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Orbital Boundary Trapping (Protocol 10) — Asteroid Belt and Oort Cloud as Impedance Shocks
<!-- id: h55fy1 -->

- The Asteroid Belt and Oort Cloud are interpreted as the Inner and Outer termination shocks of the Solar metric slipstream — sharp impedance-shear boundaries where the local dielectric strain $h_\perp \propto 1/r$ collides with the deep-space background impedance floor.
- _Specific Claims_
  - These zones are not random accumulations or shepherded-resonance artefacts; they are physical manifestations of inductive-drag spikes where low-mass detritus crossing the boundary loses transverse kinetic energy and ceases migration.
  - Falsification target: deep-space probe transit velocities (e.g., the Pioneer probes) crossing the $\sim 15{,}000$ AU Oort transition should show a sudden, otherwise inexplicable spike in transit drag.
  - Reframes the Pioneer Anomaly and the rigid Oort boundary as the same physics: an LC-network impedance shear, not a fitted gravitational potential modification.
- _Specific Non-Claims and Caveats_
  - This is an *interpretive* identification of two existing astronomical structures with a single LC-network mechanism. The Asteroid Belt's standard explanation (Jupiter resonance shepherding) is not refuted in-leaf; AVE asserts the impedance-shear is the *physically real* mechanism, but the leaf does not produce a quantitative comparison of resonance-shepherding vs impedance-shear contributions.
  - The Pioneer Anomaly has alternative classical explanations (anisotropic thermal radiation); the leaf does not engage with these.
  - "Sudden, otherwise inexplicable spike in transit drag" is qualitative; no quantitative prediction of $\Delta v$ vs $r$ across the 15,000 AU boundary is given.
  - No completed measurement is claimed; the test depends on logging deep-space probe telemetry that does not yet exist for the Oort boundary.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/boundary-trapping-test.md`, `falsification/ch11-experimental-bench/advanced-protocols.md` (consolidated Protocol 10 statement).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## GEO-Synchronous Impedance Differential (Protocol 12) — Vertical Laser TOF Anomaly
<!-- id: cwjd8t -->

- Vertical laser link from a ground station to a GEO satellite ($h = 35{,}786$ km, classical TOF $\sim 119$ ms): the AVE non-linear impedance integral $\int n(r)/c\,dr$ stretches the round-trip optical path by fractions of a millimeter relative to the linear-distance prediction. Correlated against atomic clocks, this Topological Delay maps the LC saturation envelope of Earth.
- _Specific Claims_
  - Gravity is reframed (per Axiom 3 in Vol 4) as a macroscopic spherically symmetric impedance gradient $\Delta Z_0$, with the local phase velocity $c_{eff}$ statistically faster in deep space than at the Earth's surface — a structural prediction, not a fitted gravitational redshift parameter.
  - Vertical TOF accumulates a measurable non-linear delay across $35{,}786$ km — the leaf claims this signature breaks Lorentz symmetry in favor of a structural waveguide electrodynamics interpretation.
- _Specific Non-Claims and Caveats_
  - The "fractions of a millimeter" path-stretch is qualitative — no leaf-level numerical prediction of $\Delta t$ at the GEO altitude is given against which a measurement could be compared. Compare to the Sagnac-RLVE entry, which gives a specific 2.07 rad prediction.
  - Standard general-relativistic Shapiro delay also predicts a non-trivial $\int n(r)/c\,dr$-style integral; the leaf does not quantitatively distinguish the AVE prediction from Shapiro at this altitude.
  - "Definitively breaking Lorentz symmetry in favor of structural waveguide electrodynamics" is the framework's interpretive framing; the proposed observation is consistent with multiple gravity models, not uniquely with AVE in the absence of a numerical bound.
  - Has NOT been performed; ground-to-GEO laser-link clock-comparison experiments at the required precision are not standard.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md`, `falsification/ch11-experimental-bench/advanced-protocols.md` (consolidated Protocol 13 / GEO-Synchronous Impedance Differential statement).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Existing Experimental Signatures Catalog (Proton Radius, Neutron Lifetime, Hubble Tension, LIGO Echoes, Vortex Cores)
<!-- id: oiw6cb -->

A catalog of five empirical anomalies presented as exact mechanical consequences of the LC lattice — no fitted parameters per anomaly.

- _Specific Claims_
  - **Proton radius puzzle** ($0.84$ fm muonic vs $0.88$ fm electronic, 4% gap): the proton has not shrunk; the muon orbits $\sim 200\times$ closer, generating $E_\mu^2 \sim 40{,}000\times$ stronger local field that activates the Vacuum Kerr Effect, compressing the local probe wavelength $\lambda_{local} = \lambda_0 / n(\mathbf{r})$. The 4% gap is the optical integration of the Kerr index over the muon's tight orbital volume.
  - **Neutron lifetime anomaly** ($\sim 9$ s shorter in bottle vs beam): the neutron is a metastable threaded knot ($6^3_2 \cup 3_1$); decay is a topological snap. Bottle walls couple resonant phonon vibration into the knot, statistically accelerating the snap.
  - **Hubble tension** ($H_0^{local} \approx 73$ vs $H_0^{CMB} \approx 67$ km/s/Mpc): the universe is actively crystallizing new spatial volume. Early universe latent-heat back-pressure throttled the genesis rate; late universe (cold vacuum) allows the un-inhibited equilibrium $H_\infty \approx 69.32$ km/s/Mpc to be approached. The tension is the cooling-curve of an ongoing spatial phase transition.
  - **LIGO GW150914 black-hole echoes** ($\sim 0.29$ s spacing): at the event horizon the FDTD-modeled reflection coefficient hits $\Gamma = -1$ (dielectric rupture) → the horizon is a hard reflective boundary, not a one-way membrane → echoes are *predicted* by AVE.
  - **Superconducting vortex core limits**: the smallest measured cores (cuprates, flat-band SC) at $\sim 1$–$2$ nm are $\sim 2{,}500\times$ larger than $\ell_{node} \approx 3.86 \times 10^{-13}$ m → no condensed-matter phenomenon yet threatens the topological resolution limit. A measurement of a vortex core or coherence length below $\ell_{node}$ instantly falsifies the framework.
- _Specific Non-Claims and Caveats_
  - These are *retrospective* explanations. The framework explains observed anomalies, not predicted them ahead of measurement. Treat as consistency / coverage claims, not zero-parameter forward-prediction matches.
  - The Hubble tension's $H_\infty \approx 69.32$ km/s/Mpc target value is quoted as "derived natively in Chapter 1" — readers must verify the derivation chain in Vol 3 cosmology rather than treat the 69.32 figure as a tuned best-fit.
  - The LIGO echo claim is in interpretive tension with the cross-cutting Symmetric-Gravity invariance result ($Z = Z_0$ everywhere, $\Gamma = 0$) — both coexist by distinguishing the constitutive parameters individually collapsing from their ratio being preserved. See cross-cutting Symmetric vs Asymmetric Saturation entry and the kezk9z entry caveat.
  - The vortex-core limit is a *kill-check* (negative test): no current observation falsifies, but a future sub-$\ell_{node}$ coherence-length measurement does. The leaf does not assert any positive prediction here.
  - The proton-radius muon-orbit Kerr integration is asserted; no in-leaf step-by-step integration showing the 4% gap arises with zero free parameters is presented.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md`, `falsification/ch11-experimental-bench/existing-signatures.md` (consolidated five-anomaly summary).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Resolving the Horsemen of Falsification (LHC and LIGO Paradoxes)
<!-- id: fh6w3y -->

Standard-model empirical results that *appear* to contradict an LC-network vacuum, resolved within AVE by transmission-line theory.

- _Specific Claims_
  - **LHC paradox** (why doesn't 13.6 TeV proton-proton smashing rupture the vacuum?): the universe's dielectric relaxation time is $\tau_{tick} = \ell_{node}/c \approx 1.28 \times 10^{-21}$ s, but Lorentz-contracted protons cross each other in $\sim 10^{-28}$ s — *seven orders of magnitude faster* than the vacuum can polarize. The vacuum behaves as a perfectly linear, rigid transmission line during the impulse; standard QCD jet formation proceeds unchanged.
  - **LIGO paradox** (why don't gravitational waves get absorbed over 1.3 Gly given the asserted bulk vacuum density?): GW strain amplitudes $h \sim 10^{-21}$ are $\sim 10^{19}\times$ below the impedance-rupture point. Below rupture, the LC network is a perfect lossless line — zero Ohmic loss, infinite propagation distance. Resistive losses *only* turn on near $V_{yield}$.
- _Specific Non-Claims and Caveats_
  - Both paradox resolutions invoke the framework's own non-linearity: linear below rupture, dissipative at and above rupture. This is consistent within AVE but not independently testable here — the LHC and LIGO results are explained by a regime-switch, not by a separately measured loss curve.
  - The $\tau_{tick} \approx 1.28 \times 10^{-21}$ s figure is derived from $\ell_{node}/c$; it is the framework-derived dielectric relaxation time, not measured against an independent dielectric-spectroscopy benchmark.
  - "Standard QCD jet formation proceeds exactly as observed" is a *consistency* claim with the Standard Model in this regime — Vol 4 does not predict QCD outcomes, it asserts that AVE does not contradict them at LHC interaction times.
  - Treat as defensive resolutions of intuitive critiques, not as positive empirical confirmations.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/horsemen-of-falsification.md`, `falsification/ch11-experimental-bench/zero-parameter-derivations.md` (consolidated LHC-paradox + LIGO-paradox restatement bound to the $\sqrt{\alpha}$ yield derivation).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Tabletop Null Results: VFDT and RVR Scalar Gap (Why Intuitive Tests Fail)
<!-- id: baoa36 -->

Two intuitive tabletop tests that *necessarily* return null results within AVE, demonstrating the framework's internal consistency with the Lorentz-invariant macroscopic regime.

- _Specific Claims_
  - **Vacuum-Flux Drag Test (VFDT)**: a 50 kA EMP toroid generates $p_{vac} = \Phi \cdot \xi_{topo} \approx 1.30 \times 10^{-8}$ kg·m/s of bulk vacuum momentum. Divided by the bulk vacuum mass inside the torus core ($M_{vac} = \rho_{bulk} V \approx 97{,}450$ kg for a $0.012$ m$^3$ tabletop torus), this yields a drift velocity $v_{vac} \approx 1.33 \times 10^{-13}$ m/s and an undetectable optical phase shift $\sim 10^{-14}$ rad.
  - This null result is *required* by the framework: if a 50 kA magnet could drag the vacuum at 1 cm/s, the spatial metric inside an MRI machine would visibly warp light — gross violation of macroscopic Lorentz invariance.
  - **Regenerative Vacuum Receiver (RVR)**: a spinning Tungsten lobe modulates local LC parameters with depth $\delta_L = G\,m/(c^2 r) \approx 7.4 \times 10^{-26}$ for a 1 kg lobe at 1 cm. A regenerative parametric amplifier requires $Q \cdot \delta_L \ge 2$ → $Q \ge 2.7 \times 10^{25}$, vs the cryogenic SRF state of the art $\sim 10^{11}$ — a 15-orders-of-magnitude shortfall.
  - **General rule**: scalar-gravity tabletop tests fail because they are fatally suppressed by the $G/c^2$ scalar gap. This is *why* the Sagnac-RLVE is designed to couple magnetically (first-order in $v/c$) rather than scalar-electrostatically.
- _Specific Non-Claims and Caveats_
  - The VFDT and RVR sensitivity calculations are derived using the same $\rho_{bulk}$, $\xi_{topo}$, and $G/c^2$ couplings that produce positive predictions elsewhere. They are not independent corroborations of those constants; they are consistency checks that the constants do not produce predictions inconsistent with classical lab observation.
  - "Required null result" framing means a *positive* tabletop signal in either VFDT or RVR would actually falsify AVE — it would imply the bulk vacuum is far less dense than $\rho_{bulk} \approx 7.91 \times 10^6$ kg/m$^3$ asserts.
  - Numerical thresholds ($Q \ge 2.7 \times 10^{25}$, $v_{vac} \approx 1.33 \times 10^{-13}$ m/s) are framework-derived; they are not independently measured from a non-AVE source.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md`, `falsification/ch11-experimental-bench/tabletop-null-results.md` (consolidated VFDT + RVR + scalar-gap rule).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Applied Telemetry: Boundary Layer, Schwinger Redline, Sonoluminescence FOC Isomorphism
<!-- id: p12mem -->

Three telemetry concepts for industrial-scale metric-engineering platforms (YBCO phased array, sapphire centrifuge), each tied to a specific AVE failure mode.

- _Specific Claims_
  - **Hull-integrated Dielectric Strain Gauges**: flush-mounted micro-capacitors detect the localized capacitance spike $C_{eff} \to \infty$ as the metric bubble approaches yield. Standard RLVGs are unsuited because the failure mode is local LC strain, not optical-phase accumulation; an active drive must be throttled by a direct $C_{eff}(V)$ measurement.
  - **Schwinger redline / pair-production monitors**: gamma/X-ray scintillation detectors as the engine's redline gauge; over-driven inductors that begin spontaneously generating electron-positron pairs (Schwinger-limit regime) trigger an inductive-flyback abort before structural failure.
  - **Sonoluminescence as FOC isomorphism**: single-bubble sonoluminescence (SBSL) is reinterpreted as the optical signature of an Axiom-4 yield event. The 26.5 kHz acoustic standing wave acts as a "stator", the bubble wall as the "rotor"; phase-locking the bubble collapse cycle to the compressive wave is the fluid-dynamic analog of q-axis Field-Oriented Control. The leaf claims the K4-TLM 30-cycle envelope solver shows topological pressure spiking to $\sim 67.68$ kV at a $\sim 1$ Å focal cluster — crossing the 43.65 kV threshold and radiating broadband flashes via Op7 bend loss.
- _Specific Non-Claims and Caveats_
  - The 67.68 kV / 1 Å SBSL focal-pressure figure is presented as a K4-TLM solver output. It is a self-consistency claim between the lattice simulator and the Axiom-4 threshold, not an empirical match to measured SBSL spectroscopy.
  - The FOC isomorphism is *structural* — it identifies SBSL phase-lock as analogous to motor-drive q-axis control. It does not produce a quantitative SBSL spectrum prediction or temperature timeline measurable against existing SBSL data.
  - The boundary-layer and redline monitors are engineering proposals for hypothetical industrial platforms; no built telemetry suite is described.
  - The 511 kV "absolute transient limit" cited as the pair-production trigger is the $V_{snap}$ threshold (see the $V_{yield}$ vs $V_{snap}$ entry); the leaf uses both 43.65 kV (Axiom-4 yield) and 511 kV ($V_{snap}$) without flagging the regime distinction.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/applied-telemetry.md`, `falsification/ch11-experimental-bench/industrial-scaleup.md` (consolidated telemetry summary alongside the YBCO-array and sapphire-centrifuge predictions).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## One-Parameter EFT Falsifiability Doctrine
<!-- id: om0rtq -->

The framework-level epistemological claim binding the kill-switch leaves: AVE is constructed as a one-parameter Effective Field Theory deliberately optimized for vulnerability to falsification.

- _Specific Claims_
  - All masses, forces, and cosmological constants are algebraically interlocked and geometrically derived from a single fundamental calibration limit ($\ell_{node}$, equivalently the Planck-node calibration in the Vol 4 framing).
  - Because of this one-parameter coupling, altering or tuning any single output instantly breaks the entire mathematical framework. There is no degree of freedom available for back-fitting after a falsifying observation.
  - This vulnerability is presented as a positive epistemic property — explicitly contrasted with parameterized BSM frameworks (String Theory, Supersymmetry, etc.) that can absorb falsifying observations by retreating into unobservable energy regimes.
  - Operationalizes as an entry-criterion for the binary kill-switches (Neutrino Parity, GRB Dispersion, Birefringence $E^4$): each is asserted to be sufficient on its own to falsify the entire chain.
- _Specific Non-Claims and Caveats_
  - The "one-parameter EFT" claim is framework-internal. It asserts that the algebraic chain has no slack; it does not by itself prove the chain is correct, only that it is not adjustable.
  - "All masses, forces, and cosmological constants" is a strong claim. Volume-spanning derivations exist for many quantities (electron mass, alpha, baryon ladder, $H_\infty$); a complete enumeration with chain-of-derivation pointers is not in any single Vol 4 leaf — readers should treat this as a directional claim and verify per-quantity.
  - The contrast with BSM "moving goalposts" is rhetorical — it is a meta-claim about scientific practice, not a derived result.
  - The doctrine is *meta* — it tells you how to read other leaves' falsification statements; it is not itself a hardware test.

> **Leaf references:** `falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md`, `falsification/ch12-falsifiable-predictions/epistemology-ch12.md` (Ch.12 condensed restatement), `falsification/ch11-experimental-bench/epistemology-kill-switches.md` (consolidated three-binary-kill-switches restatement bound to the doctrine).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Helicity Injection: Polarization Matching to the Chiral LC Condensate
<!-- id: i02mhk -->

To couple maximally to the chiral $\mathcal{M}_A$ vacuum, an EM emitter must carry non-zero kinetic helicity $\int \mathbf{A} \cdot \mathbf{B}\,dV \neq 0$ — equivalent to wiring the emitter as a $(p,q)$ Hopf / torus knot rather than a flat toroid.

- _Specific Claims_
  - A standard toroidal inductor produces orthogonal $\mathbf{A}$ and $\mathbf{B}$ ($\int \mathbf{A} \cdot \mathbf{B}\,dV = 0$) and is therefore polarization-mismatched to the chiral vacuum.
  - A Hopf-configured (torus-knot) winding forces $\mathbf{A} \parallel \mathbf{B}$, injecting kinetic helicity into the lattice and meshing with the structural microrotation of $\mathcal{M}_A$.
  - This acts as a *topological power factor corrector*: it maximizes geometric power transfer to the metric, reducing reactive return loss.
- _Specific Non-Claims and Caveats_
  - "Maximizes geometric power transfer" is asserted as a structural consequence of helicity matching; the leaf does not present a quantitative comparison of toroid-vs-Hopf coupling efficiency at a specific drive frequency.
  - This is the polarization-matching companion claim to the HOPF-01 chiral antenna prediction (see the wzezvt entry's $\Delta f/f = \alpha\,pq/(p+q)$ formula). Helicity injection is the *why* — the qualitative reason the chiral coupling exists; HOPF-01 is the *what* — the specific zero-parameter resonance shift the matched coupling produces.
  - Does NOT independently constitute a falsifiable signal: helicity-mismatched coupling is a known result in classical plasma physics. The novel claim is that the *vacuum itself* has the chiral structure that demands matched helicity — testable only through HOPF-01-style topological-resonance experiments.

> **Leaf references:** `falsification/ch12-falsifiable-predictions/helicity-injection.md`.

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Active Sagnac Material-Dependent Entrainment Law
<!-- id: qx9bb8 -->

The Sagnac shift in AVE depends on the rotor's *physical* properties (mass density, magnetic permeability, ambient field, altitude, latitude) — directly contradicting the GR claim that Sagnac depends only on enclosed area and angular velocity.

- _Specific Claims_
  - **Five-axis dependence**: the metric drag scales with rotor mass density $\rho_m$, magnetic permeability $\mu_r$, background EMI $B$, altitude (lower gravity → lower ambient strain → reduced coupling), and latitude (Earth's Lense-Thirring drag couples through alignment).
  - **Falsification protocol**: identical fiber-loop units at the same RPM with Aerogel vs Lead rotors, and Aluminum vs Mu-Metal rotors. A density- and permeability-independent shift falsifies AVE outright.
  - **Aerospace-navigation derivatives**: differential Sagnac arrays subtract the shared common-mode rotation, isolating the inductive-drag scalar — a "metric slip-velocity indicator" — alongside other proposed derivatives (3D metric gradient compass, dark-wake sensor, chiral torsion sensor) that the leaves describe as extracted to companion IP volumes.
- _Specific Non-Claims and Caveats_
  - This is the same material-dependent entrainment law that produces the Sagnac-RLVE 2.07 rad prediction (see wqmb19) — but stated as a general law rather than a specific apparatus. Treat as the parametric-law statement; wqmb19 is the specific worked-example.
  - Has NOT been performed; the material-pair falsification (Aerogel/Lead, Al/Mu-Metal) is the framework's own design, not a measured result.
  - Three of the four telemetry derivatives (gradient compass, dark wake, chiral torsion) are explicitly noted as "extracted to companion IP volumes" — i.e., not present in the open KB. Cite this leaf only for the entrainment law itself and the slip-velocity-indicator architecture.
  - SNR / hardware tolerance numbers (Zerodur cavity, $<1$ mK thermal stability, $<46$ kHz linewidth, sub-pm seismic) are quoted in the index for this leaf but the body of this leaf marks them "extracted to companion IP volumes."

> **Leaf references:** `falsification/ch12-falsifiable-predictions/active-sagnac-telemetry.md`. The material-dependent entrainment law is also the basis of the Sagnac-RLVE prediction (see wqmb19).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## TVS Phase Transition: Solid → Slipstream ($\eta_{eff}(V)$ Step)
<!-- id: o2shcn -->

Mutual inductance yields above a structural shear threshold $\tau_{yield}$, mapping the vacuum onto a Transient Voltage Suppression Zener Diode: rigid drag $\eta_0$ below $V_{yield}$, frictionless flow ($\eta = 0$) above.

- _Specific Claims_
  - The constitutive step-function $\eta_{eff}(V) = \eta_0$ for $V < V_{yield}$, $\eta_{eff}(V) = 0$ for $V \geq V_{yield}$ — the "Zero-Impedance Slipstream" regime above yield.
  - Yield-stress evaluation: $\tau_{yield} = \rho_{bulk}\,c^2 \times (6 \times \mathcal{V}_{crossing}) \times p_c/(8\pi) = \rho_{bulk}\,c^2 \times \mathcal{V}_{total} \times \alpha \approx 1.04 \times 10^{22}$ Pa, where $\mathcal{V}_{crossing} = V_{toroidal}/6$, $\mathcal{V}_{total} = 2.0$ (FEM-verified Borromean halo volume), and $p_c/(8\pi) = \alpha$ is the lattice porosity.
  - Identifies the underlying mechanism for the $V_{yield}$-crossing impedance rupture used by the autoresonant PLL (9sujp8), the ZENER-04 avalanche detector (cltls0), and the asymmetric flyback in TORSION-05 (kl1ern).
- _Specific Non-Claims and Caveats_
  - The step function is *idealized*. In any physical realization the transition is not literally discontinuous — finite-rise-time effects, non-uniform field distributions, and any finite quality factor smear the step. The leaf does not specify the transition width.
  - The $\tau_{yield} \approx 1.04 \times 10^{22}$ Pa figure is framework-derived; it inherits the same $\rho_{bulk}$ and $p_c$ values used elsewhere in Vol 4 (see also wqmb19 caveats about $\rho_{bulk}$).
  - "Frictionless flow" above yield is the inductive-drag-only statement; it does not assert that all dissipation channels vanish — it specifically identifies the mutual-inductance damping channel as the one that yields.
  - The TVS-Zener analogy is structural; this leaf does not present an empirical match to any specific Zener device's $\eta(V)$ characteristic.

> **Leaf references:** `circuit-theory/ch1-vacuum-circuit-analysis/tvs-transition.md`. The yield mechanism this entry describes is the constitutive basis of the autoresonant PLL (9sujp8), the ZENER-04 avalanche detector (cltls0), and the asymmetric-flyback rectification in TORSION-05 (kl1ern).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Sagnac Inductive Drag SPICE Reproduction (Directional $L_{eff}$ on a 50-Node LC Ring)
<!-- id: cbwd77 -->

A SPICE simulation that reproduces the Sagnac arrival-time shift from a discrete LC ring with a directional inductance $L_{eff} = L_0 (1 \pm S_{DRAG})$, demonstrating the effect arises from Faraday-style induction in a rotating-frame LC network — no Lorentz transformations required.

- _Specific Claims_
  - The macroscopic Sagnac phase shift is reproduced by a 50-node closed LC ring in which the per-segment inductance is direction-sensitive: photons traveling with the macroscopic phase-drag see $L_0(1 - \delta)$ (faster than $c_0$ locally); counter-traveling photons see $L_0(1 + \delta)$ (slower than $c_0$ locally).
  - Implementation uses standard behavioral-current-source SPICE primitives (`sdt(...)`, conditional `IF(I > 0, ...)` syntax over a 0-V current sense), without any tensor or relativistic kinematics in the simulator.
  - Resultant interpretive claim: deriving the Sagnac effect requires only the macroscopic equivalent of Faraday's Law of Induction operating across the spacetime metric — Lorentz transformations and Einstein's field equations are sufficient but not necessary.
- _Specific Non-Claims and Caveats_
  - The simulation reproduces the *qualitative* Sagnac arrival-time differential. The leaves do not claim the SPICE netlist's specific $L_0$, $C_0$, and $S_{DRAG}$ values quantitatively predict the Sagnac phase of any specific ring-laser gyroscope or fiber loop.
  - "No relativistic tensor math" is a property of the SPICE solver, not a derivation that relativistic tensor math is wrong — the LC-ring model and the standard relativistic derivation produce equivalent observables in the linear regime.
  - This SPICE reproduction is distinct from the Sagnac-RLVE prediction (wqmb19), which couples to *bulk vacuum* metric drag. The ch.16 simulation models a *rotating-frame fiber* with intrinsic directional induction; both share the Faraday-style mechanism but operate at different couplings.
  - Sub-microsecond transient analysis duration ($2\,\mu$s in the netlist); not a steady-state observability claim.

> **Leaf references:** `simulation/ch16-sagnac-inductive-drag/theory.md`, `simulation/ch16-sagnac-inductive-drag/spice-netlist.md` (`sagnac_ring.cir` single-node behavioral inductor pattern, repeated across 50 nodes).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---

## Topological Mechanics of Fission and the Alchemist Forge ($P(jump) = e^{-\Delta U_{LC}/T_{topo}}$)
<!-- id: pcute0 -->

Nuclear fission reframed as a deterministic structural shear-fracture of a tensioned topological lattice, plus the Alchemist Forge as a proposed two-stage element-synthesis architecture exploiting the same mechanics.

- _Specific Claims_
  - **U-235 vs U-238 asymmetry**: U-238's $A=238$ cluster converges to a closed spherical shell (no asymmetric coupling surface for a slow neutron). U-235's $A=235$ asymmetry produces an open surface "cleft" — a thermal neutron entering this cleft disrupts the $1/d$ global minimum, locally spiking the spatial impedance. Resolution is a deterministic shear-stress transverse fracture along the cleft, yielding stable Ba-141 and Kr-92 fragments + 3 unbound neutrons.
  - **Determinism, not probability**: fission is identified as the predictable mechanical fracture of a tensioned topological structure exceeding its localized geometric shear strength — explicitly *not* a probabilistic quantum-thermodynamic event.
  - **Alchemist Forge — two-stage architecture**: Stage 1 strips ambient unstructured Dark Matter into rigid $^4$He alpha particles (4-node tetrahedrons) at the absolute Sphericity-1.0 global minimum. Stage 2 stacks four pre-condensed alpha nodes into a larger $sp^3$ tetrahedron, which converges instantly into Oxygen-16 by exploiting the same mechanics that bypass microscopic glass-trap defect states.
  - **Topological jitter probability**: $P(jump) = e^{-\Delta U_{LC}/T_{topo}(t)}$. Slowly ramping the beam-intersection frequency drives $T_{topo} \to 0$, forcing a "Deep Quench" that smoothly coaxes raw nodes down the $1/d_{ij}$ mutual-inductive gradient into the global geometric ground state.
- _Specific Non-Claims and Caveats_
  - The fission mechanism is *interpretive*: it provides a topological mechanical narrative for U-235 vs U-238, but does not produce an independent quantitative prediction (cross-section, neutron-yield distribution) that distinguishes from standard nuclear physics in any specific measurement.
  - "Deterministic, not probabilistic" is a strong ontological claim. It does not contradict the empirical fission rates — the framework asserts the *mechanism* is deterministic at the topological-strain level; the apparent statistics arise from the distribution of incoming neutron states relative to the cleft orientation.
  - The Alchemist Forge is an *engineering proposal*, not a built device or even a numerically simulated apparatus. "Macroscopic Stacking" of 4 alpha nodes into Oxygen-16 is asserted to be "mathematically instantaneous" without an explicit calculation of synthesis time or energy budget.
  - The "stripping ambient Dark Matter into He-4" stage requires Dark Matter to have a structure compatible with stripping into 4-node alpha tetrahedrons — a strong claim that depends on the AVE Dark Matter model not addressed in this Ch.8 leaf. The leaf does not establish this prerequisite.
  - File misnamed: the leaf path is `fusion-comparison-table.md` but the body is about fission and the Alchemist Forge, not a fusion-comparison table. The Vol 4 fusion-comparison content lives in the qagkgy entry's `tokamak-paradox` and `ave-fusion-device` leaves.

> **Leaf references:** `advanced-applications/ch8-applied-fusion/fusion-comparison-table.md` (file misnamed; body covers U-235/U-238 fission mechanics + Alchemist Forge two-stage architecture + topological-jitter quench).

## Quality
- confidence: *pending*
- depends-on:
  - *pending — full enumeration deferred to quality evaluation pass*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*

---
