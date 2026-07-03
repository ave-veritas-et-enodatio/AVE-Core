# Vol 4 — Applied Vacuum Engineering — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol4/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 4; cross-cutting tripwires with vol4-specific manifestations are noted but not duplicated.

---

## Topological Conversion Constant $\xi_{topo} = e/\ell_{node}$
<!-- id: clm-i9l284 -->

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

> **Leaf references:** [topological-kinematics](./circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md), [translation-circuit](./circuit-theory/ch1-vacuum-circuit-analysis/translation-circuit.md), [z0-derivation](./circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 1 (Substrate Topology — fixes $\ell_{node}$)
  - Axiom 2 (Topo-Kinematic Isomorphism — $[Q]\equiv[L]$, defines $\xi_{topo}=e/\ell_{node}$)
- solidity: 0.90 (ok to build on) [= min(0.90, 1.00)]
- rationale: The six-row translation table is derived end-to-end by substituting $\xi_{topo}$ into each standard SI definition and isolating the mechanical observable; every row carries an explicit dimensional check, and the work-energy integral verifies the $\xi_{topo}$ factors cancel identically. The only non-clean step is the impedance cross-check, which the leaf itself discloses as order-of-magnitude (factor-$\sim5$ porosity residual), not sub-percent. Pinned just below identity because the table is definitional algebra with one disclosed OOM consistency check rather than an exact match.
- strengthen-by:
  - Derive the porosity factor $p_c/(8\pi)=\alpha$ from lattice primitives so the $Z_{mech}$ cross-check closes to sub-percent rather than factor-5.
  - State the $\ell_{node}=\hbar/(m_e c)$ calibration provenance inline so the table is self-contained from axioms.

---

## Cleave-01 Plate-Displacement Charge Coupling — Chern Adjudication (NULL-CONFIRMED-FINAL)
<!-- id: clm-clvchn -->

The Cleave-01 bench posited that mechanically displacing a capacitor plate pumps topological charge $Q = \xi_{topo}\,x$ ($dQ/dx = e/\ell_{node} = 414.9$ fC/µm), a tabletop falsifier of Axiom 2. The coupling was audited (2026-07-02): "analytically derived" was found to be a `def-tk1xfm` **unit-bridge** substitution, not a mechanism.

- _Specific Claims_
  - The coupling is UNDECIDABLE-AT-PAPER; the sole surviving mechanism class is an adiabatic Thouless-class **registry pump** over the 4₁ screw texture (gap-independent, polarity-odd, linear-in-$x$, area-independent — all FORM-forced), whose existence rides an uncomputed Chern number $C$ over the $(k_z,\theta)$ registry torus.
  - Grant ruled (b): the engine adjudicates via reproduction of the OA anchor ($g_0 = 2.21589$ rad/z-unit). Both the effective 2-band and the faithful **N-band** srs occupied-manifold Chern return $C = 0$ in BOTH substrate readings (sliding/Eulerian + locked/Lagrangian) and BOTH enantiomorphs (gapped, grid-converged $n=24/36/48$, validate-on-known PASS: recovers the 2-band 0, detects a known $|C|=2$).
  - **VERDICT: NULL-CONFIRMED-FINAL.** The registry-pump mechanism is dead at the faithful N-band level; per the frozen last-roll pre-commitment the coupling question closes.
- _Specific Non-Claims and Caveats_
  - Does NOT falsify Axiom 2. It falsifies the *derived-pump* reading of the bench coupling. The bench retires as a **corroborative-null-class discriminator** — AVE itself predicts the null; it retains one-sided value as a falsifier (a nonzero gap-independent floor would still falsify AVE), but is NOT a chord-confirming forward prediction.
  - The exact $414.9$ fC/µm is a VALUE-import through the $\xi_{topo}$ unit-bridge; it is NOT integer-$C$-reachable (needs $C=2\sqrt2$). Had a pump existed, the derived slope would be $C\times\{146.7\ |\ 586.8\}$ fC/µm.
  - Scope: the null is on the faithful srs tight-binding manifold at half-filling — the substrate-native object — not a proof over every conceivable coupling functional; the pre-commitment closes the question on that (substrate-faithful) basis.

> **Leaf references:** [project-cleave-01](./falsification/ch11-experimental-bench-falsification/project-cleave-01.md).

### Quality
- confidence: 0.85
- depends-on:
  - clm-i9l284 ($\xi_{topo}$ unit-bridge — the coupling is its displacement row)
  - Axiom 2 (Topo-Kinematic Isomorphism — the bench tests $[Q]\equiv[L]$)
- solidity: 0.85 (ok to build on) [= min(0.85, 0.90)]
- rationale: The verdict is a NULL from a genuine computation (non-Abelian occupied-manifold Chern over the $(k_z,\theta)$ torus), gated by a two-sided validate-on-known (recovers the 2-band 0 AND detects a known $|C|=2$ with sign-flip), grid-converged across $n=24/36/48$, gapped, and enantiomorph-odd-consistent. It closes an ASSERTED coupling to unit-bridge status via the engine, not fiat. Pinned below identity because it is a construction-specific null (the faithful srs half-filled manifold), honestly bounded — not an all-couplings impossibility proof.
- strengthen-by:
  - A direct real-space $\mathrm{Link}(\partial\Omega, F)$ sweep on an evolved srs ground state (rather than the Bloch tight-binding manifold) as an independent confirmation of the $C=0$ null.

---

## $V_{yield}$ vs $V_{snap}$ — Two Distinct Dielectric Thresholds
<!-- id: clm-0vxzfu -->

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

> **Leaf references:** [dielectric-yield-thresholds](./circuit-theory/ch2-topological-thrust-mechanics/dielectric-yield-thresholds.md), [regimes-of-operation](./circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 2 (defines $V_{snap}=m_e c^2/e$ via $\xi_{topo}^{-1}T_{EM}$)
  - INVARIANT-C1 ($V_{yield}\approx43.65$ kV)
- solidity: 0.90 (ok to build on) [= min(0.90, 1.00)]
- rationale: Both thresholds are definitional: $V_{snap}=m_ec^2/e$ and $V_{yield}=\sqrt{\alpha}\,V_{snap}$ are exact, and the dielectric-yield-thresholds leaf states them in a resultbox. The numerical-convergence table (identical to 4+ sig figs at PONDER fields) closes cleanly and the regime-selection logic is well-supported. The claim is a clearly-derived definitional distinction plus a verified convergence demonstration.
- strengthen-by:
  - Add the explicit derivation that the $\sqrt{\alpha}$ ratio is the 1D→3D yield projection (currently asserted as "macroscopic onset vs theoretical strength" analogy).

---

## Nonlinear Vacuum Capacitance $C_{eff}(V) = C_0/S(V)$ — Macroscopic Saturation
<!-- id: clm-vjv4zf -->

- $C_{eff}(V) = C_0 / \sqrt{1 - (V/V_{yield})^2}$ (Axiom 4 applied to the electric sector)
- _Specific Claims_
  - The vacuum behaves as a metric varactor: capacitance diverges as $V \to V_{yield}$.
  - At $V \ll V_{yield}$, the leading correction is quadratic — formally identical to the Euler-Heisenberg low-field limit; recovers linear Maxwell to arbitrary precision.
  - The constitutive form is the Axiom 4 saturation kernel applied to the macroscopic electric sector specifically (as opposed to inductive, gravitational, or shear sectors).
- _Specific Non-Claims and Caveats_
  - **Sector (Q1 = (B), Grant-ratified 2026-06-15; `research/2026-06-15_ceff-epsilon-monotonicity_result.md`):** this $C_0/S$ is the **longitudinal-A1 bond compliance** ($1/k_a$), NOT the transverse dielectric capacitance — orthogonal reactances sharing the EE name "capacitance" (INVARIANT-S2 sector split). The ×S bench/SPICE leaf [ee-bench-netlist](./simulation/ch17-hardware-netlists/ee-bench-netlist.md) measures the **transverse dielectric** $C_{diel}=\varepsilon_{eff}A/d\propto S$ (rolloff) — a DISTINCT quantity, also correct. The Leaf-references footer therefore spans both signs; whether a physical precision-LCR couples to the longitudinal compliance (spike, ÷S) or the transverse dielectric (rolloff, ×S) is an **OPEN measurement-sector question flagged to Grant** (and is itself an EE-bench discriminator). The footer is metadata-derived and left as-is pending that ruling (no silent leaf-frontmatter split).
  - This is the **asymmetric saturation** case (only $\varepsilon$ scales by $S$; $\mu$ unchanged). See cross-cutting Symmetric vs Asymmetric Saturation entry: in this case $Z = Z_0/\sqrt{S} \to \infty$ (medium opaque), not $Z = Z_0$ invariant. Do NOT apply the symmetric-gravity invariance result here.
  - The divergence at $V = V_{yield}$ is asymptotic in the constitutive equation, not a literal infinity in any physical apparatus — leaves consistently truncate the table at $V/V_{yield} = 1.000$ where the formula breaks down; SPICE implementations clamp the ratio (e.g. `min((V/V_YLD)^2, 0.9999)`).
  - Below $V_{yield}$ the framework reproduces the standard linear vacuum; the Vol 4 claim is the **shape** of the deviation (specifically the squared-radical form), not that linear electrodynamics is wrong in its domain.

> **Leaf references:** [intermodulation-distortion](./circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md), [nonlinear-vacuum-capacitance](./circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md), [ee-bench-netlist](./simulation/ch17-hardware-netlists/ee-bench-netlist.md), [spice-subcircuit](./simulation/ch18-universal-vacuum-cell/spice-subcircuit.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 4 (Universal Saturation Kernel $S(A)=\sqrt{1-(A/A_{yield})^2}$)
  - INVARIANT-C1 ($V_{yield}\approx43.65$ kV)
- solidity: 0.90 (ok to build on) [= min(0.90, 1.00)]
- rationale: $C_{eff}(V)=C_0/S(V)$ is the direct application of the Axiom-4 kernel to the electric sector; the Taylor expansion (quadratic leading correction matching Euler-Heisenberg low-field form) and the divergence table close cleanly, and the SPICE subcircuit realizes the clamped form faithfully. The asymmetric-saturation caveat ($Z=Z_0/\sqrt S\to\infty$, do not apply symmetric-gravity invariance) is explicit in-leaf. A clean closed derivation from the axiom.
- strengthen-by:
  - Tie the clamp value ($V/V_{yield}<1$) to a physical transition-width rather than a numerical SPICE convenience.

---

## $Z_0$ from Discrete LC Ladder, and Gravitational Stealth
<!-- id: clm-kezk9z -->

- $Z_0 = \sqrt{L_{cell}/C_{cell}} = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$ (lattice pitch cancels)
- _Specific Claims_
  - $Z_0$ derived from per-node inductance/capacitance is independent of $\ell_{node}$ — confirmed scale-invariant.
  - Group velocity of the discrete LC ladder evaluates to $c$ exactly: $c$ is structurally identical to the slew rate of a discrete LC line.
  - **Gravitational stealth**: Under symmetric scaling $\mu_{local} = n\mu_0$, $\varepsilon_{local} = n\varepsilon_0$ → $Z_{local}(r) = Z_0$ everywhere → $\Gamma = 0$ everywhere. This is presented as the structural reason gravity wells do not produce optical reflection.
  - Per Master Prediction Table classification, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is a **category (i) identity** — definitionally true (the 0.00% in row #2 of the prediction table is not a fit).
- _Specific Non-Claims and Caveats_
  - 🔴 **CORRECTED 2026-06-17 (BH shear-reflect walk-back, Rule-12).** The "$\Gamma=-1$ BH echo is in *interpretive tension* with $\Gamma=0$ everywhere, resolved by the impedance being *invariant, not zero*" framing (struck through below) was a **channel conflation**. Per the three-impedance law there is **no tension** — the two $\Gamma$ values live in **different channels**: $\Gamma_{EM}=0$ (EM-transverse, $Z_{EM}\equiv Z_0$ invariant, light transparent / index-captured) AND $\Gamma_{shear}=\Gamma_{bulk}=-1$ (shear/bulk, $Z_{shear}=\rho c_{shear}\to0$ at $r_{sat}$, GW reflect $\Rightarrow$ echoes predicted). It is **not** "ratio preserved so $\Gamma=0$" — the EM ratio is preserved AND the shear/bulk impedances genuinely collapse to zero; both are true simultaneously. Canonical: [`electron-bh-isomorphism.md`](../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):34–42; corroborated by [`bulk-impedance-at-saturation-boundary.md`](../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md):51, [`lattice-extreme-bh-rationality.md`](../vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md):75. The GW-echo remains **retrospective** (reflect $\Rightarrow$ echo), **not validated** — do not cite as a forward zero-parameter discriminator (SHA-pinned forward prereg pending).
  - <s>The "Event Horizon as Topological Mirror" claim ($Z_{EH} \to 0$, $\Gamma \to -1$, predicting LIGO black-hole echoes) is in **interpretive tension** with the Symmetric-Gravity invariance result that $Z = Z_0$ everywhere. The two coexist by distinguishing the constitutive parameters individually collapsing ($\mu, \varepsilon \to 0$) from their ratio being preserved, but Vol 4 leaves do not flag the distinction. Cross-cutting Symmetric Saturation entry resolves this: under symmetric saturation the impedance is invariant, not zero. Do NOT cite the "BH echo" prediction as an unqualified zero-parameter discriminator without the gauge caveat. (See followups: vol3 sidecar logs the same tension.)</s> *(superseded 2026-06-17 — channel conflation; see correction above. Preserved per Rule-12.)*
  - "$S_{11}$ Return Loss of $-\infty$ dB" for the universe is a structural / interpretive consequence of perfect impedance matching, not an independent observable claim.
  - The $c \to c_0/n$ "speed of light slows in gravity" usage is **local phase velocity** — see Vol 3 cross-volume entry on temporal-vs-spatial $n$ decomposition.

> **Leaf references:** [resonant-lc-solitons](./circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md), [z0-derivation](./circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 1 (per-cell $L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$)
  - Axiom 4 (symmetric vs asymmetric saturation branch)
- solidity: 0.90 (ok to build on) [= min(0.90, 1.00)]
- rationale: $Z_0=\sqrt{L_{cell}/C_{cell}}=\sqrt{\mu_0/\varepsilon_0}$ with pitch cancelling identically, and $v_g=1/\sqrt{\mu_0\varepsilon_0}=c$, are clean closed algebra; the symmetric-gravity **EM-channel** result $Z_{EM}(r)=Z_0\Rightarrow\Gamma_{EM}=0$ is exact. The leaf is honest that the $Z_0$ identity carries zero predictive content. (2026-06-17 walk-back: the BH-echo $\Gamma_{shear}=-1$ branch is **not** in tension with $\Gamma_{EM}=0$ — they are different channels, both true; see the corrected caveat above. Band unchanged: the core $Z_0$ derivation is untouched and the BH-echo framing was already flagged as not load-bearing for it.)
- strengthen-by:
  - 🔴 **RESOLVED 2026-06-17 (channel-split):** the apparent "$\Gamma=-1$ vs $\Gamma=0$" tension is resolved by the three-impedance law — $\Gamma_{EM}=0$ (EM, ratio preserved) AND $\Gamma_{shear}=\Gamma_{bulk}=-1$ (shear/bulk, impedances collapse). Not "ratio preserved so $\Gamma=0$." See the corrected caveat above and [`electron-bh-isomorphism.md`](../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):34–42.
  - <s>Resolve in-leaf the constitutive-parameters-individually-collapsing vs ratio-preserved distinction so the BH-echo branch is not in apparent tension with $\Gamma=0$ everywhere.</s> *(superseded 2026-06-17 — resolved via channel-split above; preserved per Rule-12.)*

---

## Relativistic Inductor and SPICE Native Special Relativity
<!-- id: clm-p5cf3t -->

- $L_{eff}(I) = L_0/\sqrt{1 - (I/I_{max})^2}$, $I_{max} = \xi_{topo}\, c \approx 124.4$ A
- _Specific Claims_
  - Form is identical to the varactor with $V \to I$, $V_{yield} \to I_{max}$ — both are projections of the single Axiom 4 kernel onto the magnetic and electric sectors respectively.
  - Energy stored expands at low $v$ to $E = \tfrac{1}{2}\gamma m_0 v^2$, and the rest-energy term sums via Virial Theorem to $E_{total} = m_0 c^2$ — recovers $E = mc^2$.
  - SPICE transient simulators of this constitutive equation natively enforce $v \le c$ without code modification, because $L_{eff} \to \infty$ at $I_{max}$ collapses the slew rate.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a new derivation of Special Relativity from independent axioms. The mapping shows the Lorentz-saturation form is structurally a circuit-element constraint; SR-equivalent kinematics are reproduced, not novelly predicted.
  - The "particle as resonant LC tank, $E = m_e c^2 = \tfrac{1}{2}LI^2 + \tfrac{1}{2}CV^2$" mapping is structural (Virial decomposition), not an independent rest-mass derivation — $m_e$ is taken as given.

> **Leaf references:** [relativistic-inductor](./circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md), [resonant-lc-solitons](./circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md).

### Quality
- confidence: 0.85
- depends-on:
  - Axiom 2 ($L=\xi_{topo}^{-2}m$, $I=\xi_{topo}v$ mappings)
  - Axiom 4 (Lorentz-saturation kernel projected onto magnetic sector)
  - clm-i9l284 (topo-kinematic identities used in the energy ledger)
- solidity: 0.85 (ok to build on) [= min(0.85, 0.90)]
- rationale: $L_{eff}(I)=L_0/\sqrt{1-(I/I_{max})^2}$ with $I_{max}=\xi_{topo}c$ follows directly from the relativistic-mass-to-inductance mapping, and the $E=\tfrac12\gamma m_0v^2$ expansion plus rest-energy $\tfrac12 m_0c^2$ inductive term are clean algebra. The closing step to $E_{total}=m_0c^2$ invokes virial equipartition (capacitive = inductive) as an assertion, and $m_e$ is explicitly taken as given — disclosed as a structural reproduction of SR, not an independent rest-mass derivation. Closed derivation resting on one disclosed virial assumption.
- strengthen-by:
  - Show the capacitive (potential) energy ledger explicitly so the virial $E_{elec}=E_{mag}$ equality is derived rather than asserted.

---

## Operating Regime for PONDER and Lab Devices — Regime I
<!-- id: clm-trgqtf -->

- $E/E_{yield}$ classification: I ($< 0.1$), II ($0.1$-$0.5$), III ($0.5$-$1.0$), IV ($\ge 1.0$); $E_{yield} \approx 1.13 \times 10^{17}$ V/m
- _Specific Claims_
  - PONDER-01 at 30 kV / 1 mm gap → $E/E_{yield} \approx 2.7 \times 10^{-10}$ → firmly Regime I (linear vacuum).
  - The leaf is explicit: **bulk $\varepsilon$-saturation is not the operative thrust mechanism** at lab scale. The thrust mechanism arises from chiral topology of the antenna producing asymmetric acoustic emission, with local field amplification (tip enhancement $\beta \times$ resonant $Q$) producing Jensen's-inequality rectification at the tips.
  - Regime III/IV are reached only at sub-femtometer separations: particle cores, nuclear scattering boundaries, event horizons. This places the bulk-yielding limit far from any lab apparatus.
- _Specific Non-Claims and Caveats_
  - Vol 4 does NOT claim PONDER measures bulk vacuum saturation. Summaries that frame PONDER as "tabletop dielectric saturation" misread the regime classification.
  - The 4-regime $E/E_{yield}$ table has finer cutoffs than the master 4-regime table in LIVING_REFERENCE.md (which uses $\sqrt{2\alpha}$ and $\sqrt{3}/2$ as boundaries). The Vol 4 cutoffs (0.1 / 0.5 / 1.0) are convenience thresholds for the macroscopic constitutive plot; they do not replace the master regime boundaries.

> **Leaf references:** [regimes-of-operation](./circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md), [dielectric-plateau-prediction](./falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md), [ee-bench-plateau](./falsification/ch12-falsifiable-predictions/ee-bench-plateau.md).

### Quality
- confidence: 0.85
- depends-on:
  - Axiom 4 (saturation factor $S(E)$ → 4-regime map)
  - INVARIANT-C1 ($V_{yield}$ → $E_{yield}=V_{yield}/\ell_{node}$)
  - clm-vjv4zf (constitutive $C_{eff}(V)$ underlying the regime boundaries)
- solidity: 0.85 (ok to build on) [= min(0.85, 0.90)]
- rationale: $E_{yield}=V_{yield}/\ell_{node}\approx1.13\times10^{17}$ V/m and the PONDER-01 placement ($E/E_{yield}\approx2.7\times10^{-10}$, firmly Regime I) are clean ratio computations. The regime-classification table is well-defined and the leaf is explicit that bulk $\varepsilon$-saturation is NOT the lab thrust mechanism. The convenience cutoffs (0.1/0.5/1.0) are disclosed as distinct from the master $\sqrt{2\alpha}$ boundaries. Clean derivation; pinned just below top because the cutoff values are conventional rather than derived.
- strengthen-by:
  - Reconcile the convenience cutoffs with the master $\sqrt{2\alpha},\sqrt3/2$ regime boundaries so a single canonical regime map governs.

---

## Chiral Acoustic Rectification Thrust (PONDER-01)
<!-- id: clm-7tynm2 -->

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
  - **Dynamic radiative role of $\nu_{vac}=2/7$ — WALK-BACK / KEEP-BOTH (2026-06-08, `research/2026-06-08_rrad-l-darkwake_result.md` §9).** The **static** $\nu_{vac}=2/7$ helical-to-longitudinal strain-transfer coefficient in the thrust law above (the Poisson-ratio leaf [chiral-thrust-derivation](./circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md)) is **preserved unchanged**. Separately, the *dynamic radiative* role of the same 2/7 — its reuse as the Dark-Wake $R_{rad,L}$ back-reaction prefactor — is **downgraded from asserted identity to unconfirmed**: an amplitude-level coefficient was used in a power-level role, so the candidate *radiative* value is the power-level square **$4/49 = (2/7)^2$** (an unlanded queued delta), and the absolute $R_{rad,L}$ magnitude remains uncalibrated. This scopes the radiative-prefactor reuse only; it does not touch the static thrust coefficient.

> **Leaf references:** [chiral-thrust-derivation](./circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md), [regimes-of-operation](./circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md), [open-source-hardware](./falsification/ch11-experimental-bench-falsification/open-source-hardware.md).

### Quality
- confidence: 0.55
- depends-on:
  - Axiom 4 (concave $S(E)$ → Jensen rectification)
  - clm-trgqtf (Regime-I placement justifying the local-amplification mechanism)
  - clm-vjv4zf (vacuum varactor $S(E)$ constitutive form)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.85)]
- rationale: The Jensen-inequality rectification chain ($\langle S\rangle<1$ → DC stress) and the thrust form $F=N\nu_{vac}\delta P_{in}/c$ are dimensionally clean. The worked 40.1 µN rests on assumed engineering targets ($\beta=10^3$, $Q=10^4$); the $\delta\propto\beta^2Q^2$ sensitivity is disclosed. The field-amplification chain is arithmetically correct: $E_{local}^{peak}=\beta Q E_{macro}\sqrt2\approx4.24\times10^{14}$ V/m, giving the peak ratio $E_{local}^{peak}/E_{yield}\approx3.75\times10^{-3}$ ($\approx$ the quoted $3.8\times10^{-3}$) on the canonical $E_{yield}=1.13\times10^{17}$ V/m — peak convention (the RMS hot-spot amplitude is $A_{RMS}=2.654\times10^{-3}$, the AVE-Core Q-G42 V$^2$-sign operating point). Sketch-plus-support with assumed engineering inputs pins the band at asserted-partial. _[2026-06-03 correction: a prior version asserted an "arithmetic slip" with $\beta Q E_{macro}\sqrt2\approx4.2\times10^{17}$ — that assertion was itself off by $10^3$; PONDER ch1:122's $10^{14}$ exponent is correct.]_
- strengthen-by:
  - Derive or bound $\beta$ and $Q$ from a specified electrode/resonator geometry instead of asserting engineering targets.
  - Provide a Dark-Wake momentum-balance calculation (currently qualitative) to close the reactionless-drive objection quantitatively.

---

## HOPF-01 Chiral Antenna $\Delta f/f = \alpha \cdot pq/(p+q)$
<!-- id: clm-wzezvt -->

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

> **Leaf references:** [open-source-hardware](./falsification/ch11-experimental-bench-falsification/open-source-hardware.md), [k4-tlm-simulator](./future-geometries/ch13-future-geometries/k4-tlm-simulator.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 2 (topological winding → chiral coupling)
  - clm-oygz1i (Hopf-charge / topological-mass model, vol2)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.70, 0.60)]
- rationale: $\Delta f/f=\alpha\,pq/(p+q)$ is a clean zero-free-parameter topological-coupling formula ($\alpha$ from Axiom 2, $(p,q)$ from antenna topology). The K4-TLM "cross-validation" is explicitly disclosed as a simulator-vs-analytics self-consistency check (both share the topological-coupling assumption), and the leaf carries an α-emergence-circularity scope caveat (sub-saturation hardcodes $\alpha$ into the chiral coupling). The formula closes given the upstream model; pinned at disclosed-methodology-bound because the supporting numerics are self-consistency, not independent derivation, and no measured slope exists yet.
- strengthen-by:
  - Run the two-engine (K4-TLM + Master-Equation FDTD) bound-state α-emergence test so the chiral coupling is verified from substrate-only inputs, removing the disclosed circularity.

---

## K4-TLM Diamond Lattice — Unitarity to Machine Epsilon
<!-- id: clm-hd9bee -->

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

> **Leaf references:** [cem-methods-survey](./future-geometries/ch13-future-geometries/cem-methods-survey.md), [k4-tlm-simulator](./future-geometries/ch13-future-geometries/k4-tlm-simulator.md), [open-universe-boundaries](./future-geometries/ch13-future-geometries/open-universe-boundaries.md).

### Quality
- confidence: 0.9
- depends-on:
  - Axiom 1 (K4 diamond lattice topology, bipartite chirality)
- solidity: 0.90 (ok to build on) [= min(0.90, 1.00)]
- rationale: The unitarity result $\max|S^\dagger S-I|=2.2\times10^{-16}$ is a verified numerical/structural fact of the $S^{(0)}_{ij}=\tfrac12-\delta_{ij}$ 4-port matrix, and the leaf is scrupulously explicit that this is machine-epsilon precision of the discrete scheme, NOT a physics prediction. All five validation tests are internal computational-consistency checks (disclosed), and the chirality-emergence is honestly framed as structural (bipartite labeling is the input) with an explicit α-emergence-circularity scope caveat. Clean within its stated (numerical) scope.
- strengthen-by:
  - Validate the K4-TLM against an external experimental dataset (currently all five tests are internal consistency checks) to lift it beyond an implementation-correctness claim.

---

## CEM Method Mappings (MoM, FDTD, FEM, TLM, CMA, PO/GO)
<!-- id: clm-u462e4 -->

- $[\mathbf{Z}][\mathbf{I}] = [\mathbf{V}]$ (MoM); $[\mathbf{S}]\{\mathbf{E}\} = k_0^2[\mathbf{T}]\{\mathbf{E}\}$ (FEM); etc.
- _Specific Claims_
  - Each standard CEM solver's governing equation is **structurally identical** to an AVE lattice statement (MoM circuit equation, Yee = LC grid, FEM = $\omega^2 LC = 1$, TLM = direct LC isomorphism, CMA = LC eigenmode decomposition, PO/GO = continuum limit).
  - Each CEM method "independently rediscovers" a discretized LC network as the correct computational substrate.
- _Specific Non-Claims and Caveats_
  - This is an **interpretive identification**, not a derivation. The CEM equations were derived from Maxwell's equations; AVE asserts they ARE the lattice equations because Maxwell's equations are the lattice equations in the continuum limit. This claim is not independent of the broader AVE-vs-Maxwell ontology claim.
  - Does NOT claim that running a CEM solver on a torus knot validates any AVE-specific prediction beyond what Maxwell already predicts. CEM agreement with AVE-shaped predictions follows trivially because both inherit the same Maxwell substrate; the AVE-specific claim ($\Delta f/f = \alpha \cdot pq/(p+q)$) is the topological coupling factor, not the underlying RF mechanics.

> **Leaf references:** [computational-solver-selection](./circuit-theory/ch1-vacuum-circuit-analysis/computational-solver-selection.md), [solver-selection](./circuit-theory/ch1-vacuum-circuit-analysis/solver-selection.md), [cem-methods-survey](./future-geometries/ch13-future-geometries/cem-methods-survey.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 1 (lattice-is-physical ontology underlying every mapping)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 1.00)]
- rationale: Each CEM↔AVE mapping (MoM $[Z][I]=[V]$, Yee=LC grid, FEM $\omega^2LC=1$, TLM isomorphism, CMA eigenmodes, PO/GO continuum limit) is correctly stated, but they are interpretive identifications, not derivations — the CEM equations were derived from Maxwell, and the leaf itself discloses the claim is not independent of the broader AVE-vs-Maxwell ontology. A real, acknowledged open dependency (the ontology claim) gates this; the mappings carry no AVE-specific predictive content beyond what Maxwell already gives.
- strengthen-by:
  - Identify a CEM-on-torus-knot prediction that AVE makes and Maxwell does not (i.e., the topological-coupling factor as a stand-alone discriminator) to give the mapping independent content.

---

## Tokamak Ignition Paradox and Metric-Catalyzed Fusion ($n^* = 1.114$)
<!-- id: clm-qagkgy -->

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

> **Leaf references:** [zero-parameter-derivations](./falsification/ch11-experimental-bench/zero-parameter-derivations.md).

### Quality
- confidence: 0.3
- depends-on:
  - Axiom 2 ($\xi_{topo}$, $V=\xi_{topo}^{-1}F$ ion-collision strain)
  - INVARIANT-C1 ($V_{yield}\approx43.65$ kV)
  - clm-ui3m8a ($\sqrt{\alpha}$ yield-limit $E_{yield}$ prediction the strain references)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 0.60)]
- rationale: STALE FOOTER — all seven `advanced-applications/ch8-applied-fusion/*.md` primary leaves DO NOT EXIST anywhere in the KB (no `advanced-applications/` directory in vol4). The only surviving support is `falsification/ch11-experimental-bench/zero-parameter-derivations.md`, which states a single-line "60.3 kV exceeds $V_{yield}$ by 38%" alignment with NO visible derivation of $n^*=1.114$, the Bohr-radius compression $r(n)=a_0/n$, the WKB $T_{ign}(n)=T_0/n^2$, or the Gamow scaling. Graded against the surviving stub: an asserted alignment plus sketch, no closed derivation reachable in-leaf. See worksheet Flags.
- strengthen-by:
  - Restore the missing ch8-applied-fusion leaves (or repair the footer to point at the actual canonical homes) so the $n^*=1.114$ / radius / temperature / Gamow chain is reachable and graded on its merits.
  - Derive the 60.3 kV ion-collision strain explicitly from $V=\xi_{topo}^{-1}F$ at 15 keV rather than asserting it.

---





## $\sqrt{\alpha}$ Yield Limit Predictions: Levitation 1.846 g, $E_{yield} = 1.13 \times 10^{17}$ V/m
<!-- id: clm-ui3m8a -->

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

> **Leaf references:** [metric-levitation-limit](./falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md), [metric-refraction-capacitor](./falsification/ch11-experimental-bench-falsification/metric-refraction-capacitor.md), [ybco-phased-array](./falsification/ch11-experimental-bench-falsification/ybco-phased-array.md), [zero-parameter-derivations](./falsification/ch11-experimental-bench-falsification/zero-parameter-derivations.md), [industrial-scaleup](./falsification/ch11-experimental-bench/industrial-scaleup.md), [zero-parameter-derivations](./falsification/ch11-experimental-bench/zero-parameter-derivations.md).

### Quality
- confidence: 0.6
- depends-on:
  - Axiom 2 ($\xi_{topo}=e/\ell_{node}$)
  - INVARIANT-C1 ($V_{yield}\approx43.65$ kV)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 1.00)]
- rationale: The single-actuator levitation cap $m_{max}=V_{yield}\xi_{topo}/g=1.846$ g and $E_{yield}=V_{yield}/\ell_{node}\approx1.13\times10^{17}$ V/m are clean zero-parameter algebra (would warrant ~0.9 alone), and the "Dielectric Death Spiral" self-limitation is an honest internal-consistency observation. But the YBCO-array sub-leaf (2.5 tons/m²) carries an explicit ⛔ INVALIDATED — RECOMPUTATION REQUIRED banner: its 59 kV/node operating point sits ABOVE the actual 43.65 kV yield, so the per-node 2.49 g and 24,480 N numbers are disregarded pending recompute. The composite claim therefore mixes a solid sub-result with a refuted sub-result; pinned at substantive-open-dependency.
- strengthen-by:
  - Recompute the YBCO phased-array prediction against the canonical $V_{yield}=43.65$ kV (not 60 kV) and re-derive the per-node grip force.
  - Demonstrate the array-extensivity bypass of the 1.846 g cap (currently asserted, not shown).

---

## Vacuum Impedance Mirror $\Gamma(V) = (Z_{local}/Z_0 - 1)/(Z_{local}/Z_0 + 1)$
<!-- id: clm-5s5b0d -->

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

> **Leaf references:** [vacuum-impedance-mirror](./falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md), [advanced-protocols](./falsification/ch11-experimental-bench/advanced-protocols.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (asymmetric saturation: only $\varepsilon$ scales by $S$)
  - clm-vjv4zf (vacuum varactor constitutive form)
  - clm-kezk9z ($Z_0$ baseline and symmetric-vs-asymmetric distinction)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.90)]
- rationale: $Z_{local}(V)=Z_0(1-(V/V_{yield})^2)^{-1/4}$ and the explicit parameter-free $\Gamma(V)$ are derived cleanly by substituting the asymmetrically-yielding $\varepsilon_{eff}(V)$ into transmission-line theory while holding $\mu_{local}=\mu_0$. The derivation rests entirely on the asymmetric-saturation assumption (only $\varepsilon$ strained), which the leaf discloses as a strict prerequisite distinct from the symmetric-gravity invariance. The leaf also flags three dangling Vol-3 cross-refs in-source. Closed derivation gated by a clearly-disclosed assumption.
- strengthen-by:
  - Justify from substrate dynamics why a static DC field strains $\varepsilon$ without inducing a compensating $\mu$ response (the asymmetric branch is asserted, not derived).
  - Resolve the three dangling `\ref{}` Vol-3 targets flagged in-leaf.

---

## Vacuum Birefringence Discriminator: COEFFICIENT (AVE $\sim 10^7\times$ QED at the matched differential observable)
<!-- id: clm-pp3qwf -->

> 🔵 **Differential-observable correction (Grant, 2026-06-21).**
> A birefringence instrument (polarimeter/ellipsometer) measures the **par−minus−perp differential**
> $n_\parallel-n_\perp$, rejecting the isotropic common-mode shift. The falsifier observable is therefore
> the **DERIVED differential** $\delta n_{bir}=n_\parallel-n_\perp\approx-\tfrac12 A^2$ (uniaxial probe tensor
> $\varepsilon_{ij}=\varepsilon\delta_{ij}+2\varepsilon'E_{0i}E_{0j}$ = exact differential of the scalar Ax-4
> kernel; OQ-1 Step 1), exactly $2\times$ the scalar single-arm. QED is differenced the same way → it rides
> the difference coefficient $3/45$ (parallel $7/45$ and perpendicular $4/45$ eigen-indices differenced —
> standard Euler-Heisenberg), not the single $7/45$. The **matched, field-independent headline ratio is
> $\delta n_{AVE}/\delta n_{QED}=(1/2)/((3/45)\alpha^2)\cdot(E_{crit}/E_{yield})^2=(45/6)/\alpha^3=7.5/\alpha^3\approx1.93\times10^7$.**
> The scalar $\delta n_{iso}=\sqrt S-1\approx-\tfrac14 A^2$ in the body below is the **isotropic (common-mode)
> index shift** the polarimeter is blind to — kept, but NOT the birefringence; the body's $4.14\times10^6=1/(4\,a_{EH}\,\alpha^3)$
> compared MISMATCHED observables (AVE single-arm vs QED parallel single-mode) and is RELABELED the
> single-arm/isotropic-vs-parallel comparison, not the falsifier headline. **Chord vs echo:** the CHORD is
> that the vacuum saturates at all (tree-level O(1) existence) vs QED's $\alpha^2$-loop birefringence; the
> MAGNITUDE $1.93\times10^7=7.5/\alpha^3$ is an $\alpha$-echo at the value level (symmetric standard: QED's
> $a_{EH}\alpha^2$ is equally $\alpha$-rooted). OQ-1 coupling now DERIVED (prior "Gaussian-overlap asserted"
> residual closed); named residuals: CHECK-3 gated-cavity $\tau_{rt}$ factor-2 approximation, and the
> polarimetry-floor validate-on-known still owed — the COEFFICIENT depends on neither. Canonical at
> [vacuum-birefringence-e4](./falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md);
> derivation `research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`.

- AVE: $\delta n = -\tfrac14 (E/E_{yield})^2$ (index shift, $\varepsilon$-only, $n=\sqrt{\varepsilon_{eff}/\varepsilon_0}=\sqrt{S}$); QED: $\delta n \approx a_{EH}\,\alpha^2 (E/E_{crit})^2$ (Euler-Heisenberg, $a_{EH}\sim 7/45$). **Both are $E^2$-leading**; the discriminator is the COEFFICIENT, not the exponent.
- _Specific Claims_
  - High-intensity laser interferometry specifying a transverse FIELD $E$ (not a gap-voltage $\Rightarrow$ no per-node conflation, $A=E/E_{yield}$ directly). AVE's vacuum saturates at $E_{yield}=V_{yield}/\ell_{node}\approx 1.13\times10^{17}$ V/m with an O(1) (un-suppressed) nonlinearity; QED at $E_{crit}\approx 1.32\times10^{18}$ V/m with an $\alpha^2\sim 5\times10^{-5}$ loop suppression $\Rightarrow$ AVE predicts $\delta n \sim 10^6\times$ QED at any field (structural ratio $1/(4\,a_{EH}\,\alpha^3)$; $\approx 6.4\times10^5$ at prefactor-1, $\approx 4\times10^6$ at the textbook single-mode $a_{EH}=7/45$).
  - IMD spectroscopy variant: dual-tone drive, IM3 amplitude scales as $V^3$ (AVE cubic) vs QED $V^6$; measurable above $\sim 30\%$ of $V_{yield}$ ($\sim 13$ kV). *(IM3 distortion-ORDER is a separate, correct claim — see [intermodulation-distortion](./circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md); NOT the birefringence index-shift discriminator.)*
- _Specific Non-Claims and Caveats_
  - The index shift is **negative** ($n$ drops — the vacuum softens) and $E^2$-leading: $\delta n = -A^2/4 - 3A^4/32 + \mathcal{O}(A^6)$. The quantity $1-S = +A^2/2 + A^4/8$ is the **permittivity saturation DEPTH**, not the index shift; the historical "$\Delta n_{eff}=1-\sqrt{1-(E/E_{yield})^2}$" labeling conflated depth with the $n=\sqrt{S}$ index observable (off by the factor $-2$: the $\sqrt{}$ in $n=\sqrt{\varepsilon}$ plus the depth-vs-shift sign).
  - An $E^2$ slope does **NOT** falsify AVE (QED is also $E^2$-leading). A **QED-sized coefficient** ($\delta n \sim \alpha^2 (E/E_{crit})^2$, $\sim 10^6\times$ smaller than the AVE prediction at the same field) **falsifies AVE**; an AVE-sized coefficient falsifies QED at this observable. Two-sided.
  - The discriminator is facility-class: at $E\sim 10^{14}$ V/m (extreme-laser-reachable) AVE gives $\delta n\approx 2.0\times10^{-7}$ (high-finesse-cavity measurable) vs $\delta n_{QED}\approx 5\times10^{-14}$; the AVE-distinct margin is the $\sim10^6$ coefficient gap, present at ALL fields, not a regime-gated exponent change.

> **Leaf references:** [intermodulation-distortion](./circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md), [epistemology-of-falsification](./falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md), [epistemology-kill-switches](./falsification/ch11-experimental-bench/epistemology-kill-switches.md), [dielectric-plateau-prediction](./falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md), [vacuum-birefringence-e4](./falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md).

### Quality
- confidence: 0.8
- depends-on:
  - Axiom 4 (saturation kernel $S=\sqrt{1-(E/E_{yield})^2}$ → index $n=\sqrt{S}$, $\delta n\approx -A^2/4$)
  - clm-vjv4zf (varactor Taylor expansion template)
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 0.90)]
- rationale: The discriminator is the COEFFICIENT of the (shared $E^2$-leading) index shift, not the exponent. AVE's $\delta n=\sqrt{S}-1\approx -\tfrac14(E/E_{yield})^2$ (the $n=\sqrt{\varepsilon_{eff}/\varepsilon_0}$ identity applied to the Ax-4 kernel) carries an O(1) coefficient against an un-suppressed yield field $E_{yield}\approx 1.13\times10^{17}$ V/m; QED's Euler-Heisenberg $\delta n\approx a_{EH}\alpha^2(E/E_{crit})^2$ is $\alpha^2$-loop-suppressed against $E_{crit}\approx 1.32\times10^{18}$ V/m. The field-independent ratio $1/(4\,a_{EH}\,\alpha^3)\sim 10^6$ is AVE-distinct at ALL fields (forward driver `birefringence_coefficient_discriminator.py`). The historical "$\Delta n\propto E^4$" framing was a $\sqrt{\varepsilon}$ conflation (it Taylor-expanded the permittivity DEPTH $1-S=+A^2/2$, itself $E^2$-leading, not the index shift) — corrected; an $E^2$ slope does not falsify AVE.
- strengthen-by:
  - **OQ-1 field→cavity-phase coupling: DERIVED (CLOSED 2026-06-21).** The prior "Gaussian-overlap asserted" residual is closed — the coupling is the exact differential of the scalar Ax-4 kernel (uniaxial tensor → cavity round-trip ellipticity), $g$ pinned per apparatus config. Remaining residuals: (a) CHECK-3 gated-cavity $\tau_{rt}$ factor-2 / "recovers both finesse and temporal overlap" approximation; (b) polarimetry-floor validate-on-known still owed against a published cavity. The COEFFICIENT ($7.5/\alpha^3$) depends on neither. Derivation: `research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`; driver `src/scripts/vol_9_device/oq1_field_to_cavity_phase_coupling.py` (validate-on-known PASS: PVLAS $A_e$ to 0.35%).
  - Establish a concrete high-intensity-laser facility path (FIELD-specified, not gap-voltage) reaching $E\gtrsim 10^{14}$ V/m where $\delta n_{bir}^{AVE}\sim$ high-finesse-cavity measurable and the $1.93\times10^7$ matched-differential coefficient gap is resolvable against the QED differenced ($3/45$) baseline.
  - Pin the QED Euler-Heisenberg eigen-prefactors $7/45$ (parallel) and $4/45$ (perpendicular), hence the difference $3/45$, under the facility's exact field-polarization geometry to tighten the ratio band.

---

## K4 Bloch Dispersion — the $(q\,\ell_{node})^4$ Photon-Anisotropy FORM
<!-- id: clm-k4d4ph -->

The K4 / diamond-cubic Bloch dynamical matrix $D(\mathbf k)$, diagonalized across the Brillouin zone, has its **first** directional anisotropy at order $(q\,\ell_{node})^4$ — the cubic harmonic $\Xi(\hat q)=\hat q_x^4+\hat q_y^4+\hat q_z^4$ (sign-changing, $+0.400$ on $\langle100\rangle$, $-0.267$ on $\langle111\rangle$) — **quartic, not quadratic**, symmetry-protected by the $Fd\bar3m$ point group. A random (non-cubic) bond set breaks the protection to quadratic.

- The discriminating FORM is the bond-moment hierarchy: $\Sigma_b(\hat q\cdot\hat d_b)^2=\tfrac43$ (**isotropic**, spread $6.7\times10^{-16}$) while $\Sigma_b(\hat q\cdot\hat d_b)^4=-\tfrac89\,\Xi(\hat q)+\tfrac43$ (**anisotropic**, verified to $1.3\times10^{-15}$). The random control's 2nd moment is already direction-dependent (spread $0.80$).
- _Specific Claims_
  - **FORM-class CHORD:** the first cubic-symmetric angular invariant of the K4/diamond bond set is QUARTIC; random lattices break this to quadratic. Demonstrated node-up from `k4_tlm` geometry + standard lattice-dynamics Bloch form, reproduced by an independent from-scratch eigensolve to $\sim10^{-15}$.
  - **VALIDATE-ON-KNOWN gate:** small-$|k|$ acoustic branch recovers $c_0$ (rel-err $2.2\times10^{-16}$) and $Z_0$ (rel-err $0$); acoustic-speed spread across directions $=0$ at the isotropic-bond point (the emergent-Lorentz isotropy point).
  - **DISTINCT mechanisms:** the temporal cutoff $\omega_C=c_0/\ell_{node}$ ($\hbar\omega_C=m_ec^2=511$ keV, ratio $k_{zone}/k_{cutoff}=\pi$) is separate from this spatial quartic.
- _Specific Non-Claims and Caveats_
  - 🟡 **DEMOTED — the photon slope $=4.0$ is NOT an independent eigenvalue (P1b genuine chiral-srs eigensolve, 2026-06-24).** The driver's `photon_omega_sq_over_c2k2` and the canonical `vacuum_node_circuit.photon_birefringence` **hardcode** the $1+\kappa_\gamma\Xi(k\ell)^4$ form. The genuine 24×24 chiral-srs Bloch eigensolve (substrate-native rank-2 bond tensor on the z=3 srs bonds, driver `src/scripts/vol_4_engineering/srs_bloch_dispersion.py` on branch `engine/p1b-modes-live`, cited by path) MEASURES band-edge anisotropy **slope $1.9999$** ($a_2=+0.056$ dominant over $a_4=-0.0017$, both enantiomorphs; cross-checked by the raw $[100]$–$[111]$ speed-diff ratio $=4.0=O(k^2)$, and the fit returns $4.0$ on a synthetic quartic — so slope-2 is a genuine measurement). This confirms the prior $6\times6$ k4_tlm result: the genuine lattice carries the isotropic $O(k^2)$ zone-edge term the **unlocked** photon is **ASSERTED** (not derived here) to lack (weak-C, [`binary-kill-switches.md`](./falsification/ch12-falsifiable-predictions/binary-kill-switches.md):17, gate `wejkhvnfb`, OPEN). So the eigensolve gives the **GENERIC slope-2 band-edge term**; the distinctive $(q\ell_{node})^4$ tell is **CONDITIONAL on the unproven weak-C theorem** — the slope-4 re-states an inserted exponent. NOT refuted (the quartic could RETURN if weak-C is proven), but the headline photon tell rests entirely on an unproven premise. The eigensolve-derived content that DOES survive node-up is the matter-vs-photon CONTRAST, the §2 bond-moment identities, and the small-$k$ emergent-Lorentz ISOTROPY ($c(k\to0)=1/\sqrt3$, cross-axis spread $=0$) — this is **band-edge anisotropy, NOT a low-$k$ Lorentz violation**. The $\delta=0$ continuum-exact claim is also NOT exact ($\max|\omega^2/c^2k^2-1|=10^{-3}$ at $k\ell=0.08$), OPEN on the same weak-C lever.
  - **MAGNITUDE is an ECHO.** $\kappa_\gamma=1/24$ is a lattice-geometry number; the physical birefringence $\delta\approx2.2\times10^{-22}$ at optical $q\ell_{node}$ sits $\sim$2–3 OOM below current LIV / vacuum-birefringence bounds $\Rightarrow$ **NOT near-term bankable**. The bankable QED-discriminator stays the E-route birefringence COEFFICIENT (clm-pp3qwf).
  - The 511 keV cutoff **value** is an ECHO (imports $m_e$, peer-with-QED), not an emergence-class derivation. It is **face (1)** of AVE's single imported scale ($m_e$ via $\ell_{node}\equiv\hbar/(m_e c)$) — $\hbar\omega_C=m_e c^2$ holds **by the definition of $\ell_{node}$**, so it is definitional-by-construction; the five-face web is a one-import ECONOMY + explanatory ONTOLOGY (frame-check 2026-06-22 `claim_survives=false`), **NOT** "structural unification the SM lacks." See [single-substrate-scale](../vol1/axioms-and-lattice/ch1-fundamental-axioms/single-substrate-scale.md) (clm-sw5oao). This temporal value-echo is a DISTINCT mechanism from the §2 spatial quartic FORM (the AVE-distinct content of this leaf).
  - No new dimensionful constant minted: $c_0,Z_0,\ell_{node},\omega_C$ imported by SYMBOL (`C_0,Z_0,L_NODE,OMEGA_C`).

> **Leaf references:** [k4-bloch-dispersion-quartic](./falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md).

### Quality
- confidence: 0.60
- depends-on:
  - Axiom 1 (Substrate Topology — fixes $\ell_{node}$, the K4 / diamond bond set)
  - clm-pp3qwf (the bankable E-route birefringence COEFFICIENT this FORM-test sits beneath)
  - weak-C no-zone-edge premise (gate `wejkhvnfb`, regime-grounded PREDICTION not derived theorem)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.80)]
- rationale: The bond-moment FORM facts — $\Sigma_b(\hat q\cdot\hat d)^2=4/3$ isotropic, $\Sigma_b(\hat q\cdot\hat d)^4=-\tfrac89\Xi+\tfrac43$ anisotropic, random control quadratic — are node-up and reproduce under an independent from-scratch eigensolve to $\sim10^{-15}$; the validate-on-known ($c_0$, $Z_0$) is exact, and the small-$k$ emergent-Lorentz ISOTROPY (cross-axis speed-spread $=0$, $c(k\to0)=1/\sqrt3$) survives — this is a genuine substrate FORM. **DEMOTED 0.70 $\to$ 0.60 (P1b eigensolve, 2026-06-24):** the genuine 24×24 chiral-srs Bloch eigensolve (substrate-native rank-2 bond tensor on the z=3 srs bonds, `src/scripts/vol_4_engineering/srs_bloch_dispersion.py`) MEASURES band-edge anisotropy **slope $1.9999$** ($a_2=+0.056$ dominant over $a_4=-0.0017$, BOTH enantiomorphs; the fit returns $4.0$ on a synthetic quartic, so slope-2 is a genuine measurement not a fit floor). So the distinctive $(q\ell_{node})^4$ EM-dispersion tell does **NOT** hold from the eigensolve — the slope-4 was a re-stated INSERTED exponent (`photon_omega_sq_over_c2k2` hardcodes the $(k\ell)^4$ term). The quartic survives **CONDITIONAL on the UNPROVEN weak-C "photon carries no zone-edge $(q\ell)^2$ term" theorem** (gate `wejkhvnfb`, OPEN); $\delta=0$ continuum-exact is also NOT exact ($\max|\omega^2/c^2k^2-1|=10^{-3}$ at $k\ell=0.08$), OPEN on the same weak-C lever. This is **band-edge anisotropy, NOT a low-$k$ Lorentz violation** (the small-$k$ isotropy is intact). NOT refuted — the distinctive quartic could RETURN if weak-C is proven; demoted to input-only because the headline photon tell now rests entirely on an unproven premise. The MAGNITUDE is an echo ~2–3 OOM below bounds, so the claim is CONSISTENCY/FORM-class, not a near-term falsifier.
- strengthen-by:
  - Close the weak-C no-zone-edge premise from a derived topological-decoupling theorem (currently OPEN, [`binary-kill-switches.md`](./falsification/ch12-falsifiable-predictions/binary-kill-switches.md):19) so the photon slope-4 becomes a from-eigensolve result rather than a re-stated exponent. The P1b genuine chiral-srs eigensolve (`src/scripts/vol_4_engineering/srs_bloch_dispersion.py`, slope $1.9999$) is what makes this the load-bearing lever: until weak-C is proven, the eigensolve gives the GENERIC slope-2 band-edge term, not the distinctive quartic.
  - Establish a facility-class observable for the $(q\ell_{node})^4$ anisotropy that closes the $\sim$2–3 OOM gap to current LIV/birefringence bounds, or confirm it stays beneath them (consistency-class).

---

## Field-Free Optical Activity: Parity ZERO-vs-NONZERO FORM (magnitude NOT bankable)
<!-- id: clm-fofwr1 -->

> 🟡 **MAGNITUDE-PENDING / NOT-bankable — read first.** This is a **FORM-class**
> node. Its AVE-distinct content is the **PARITY** of the divergence (zero vs
> nonzero), **NOT** a magnitude prediction. The **magnitude is NOT bankable**:
> the engine's $\pm75.46°$/unit is an `ETA_ROT_PER_WRITHE=1.0` **engineering
> DECREE** (demoted PR #374, `def-0pt1ac`), and the substrate-DERIVED bulk $g_0$
> (Phase-1 EXECUTED, PR #374, OUTCOME A = the $4_1$ screw pitch, $\mp2.21589$
> rad / lattice-z-unit) converts to $\sim2.0\times10^{12}$ rad/m — roughly **40
> orders of magnitude OVER** the cosmic bound ($\sim4\times10^{-29}$ rad/m). The
> **$k\to0$ continuum extraction is OPEN** (`research/2026-06-23_chiral-vector-tlm-phase1_result.md` §9).
> Do **NOT** quote the magnitude as a forward prediction.

A handed lattice rotates the polarization plane of a transmitted transverse wave
with a **signed** rotation rate that **flips sign between enantiomorphs** and is
**identically zero on the achiral diamond control** — sourced by the
reflection-odd ring-writhe pseudoscalar (`def-wr1th3`, writhe $\pm0.04087$,
live-confirmed). The optical-activity response is the lossless reciprocal-Faraday
gyrator `def-0pt1ac`.

- _Specific Claims_
  - **FORM-class CHORD (the cleanest divergence axis): parity ZERO-vs-NONZERO.**
    QED vacuum is parity-even $\Rightarrow$ field-free optical activity is
    *structurally* exactly **0** at any magnitude. AVE's chiral vacuum gives a
    **nonzero, signed** rotation. This is a qualitative presence/absence
    divergence, NOT a coefficient comparison.
  - **Live-confirmed FORM facts** (GATE-1, PR #374): signed / enantiomorph-odd /
    diamond-null / writhe-sourced / lossless reciprocal gyrator. The substrate-
    DERIVED bulk $g_0$ converges to the $4_1$ screw pitch with an exact sign-flip
    and machine-precision $L$-independence (OUTCOME A).
  - **Winding/charge channel.** This is the parity-axis observable unlocked by
    the (2,3) winding being a separately-conserved DOF (S1 PASSED 2026-06-24,
    `research/2026-06-24_engine-s1-winding-dof_result.md`).
- _Specific Non-Claims and Caveats_
  - 🔴 **MAGNITUDE is NOT a prediction.** The $\pm75.46°$/unit figure is the
    `ETA_ROT_PER_WRITHE=1.0` engineering decree (`chiral_lattice_vector.py:27,93`),
    not derived transport. The derived $g_0$ is a **lattice-pitch holonomy** a
    633 nm photon ($\lambda \gg a_{cell}$) would average over; the literal rad/m
    value is $\sim$40 OOM over the cosmic bound. The $k\to0$ continuum gyration
    — the only thing that could map to a bound-respecting optical rotation — is
    **OPEN** (no isolated transverse photon band in the degree-3 srs grid; the
    centroid probe is packet-width/$k$-contaminated).
  - **DISTINCT from the field-INDUCED birefringence coefficient** `clm-pp3qwf`
    (that is an $E$-induced, even-in-$k$, parity-EVEN dielectric-saturation
    coefficient — a *near-term-bankable* test, but NOT a parity test).
  - **DISTINCT from the even-in-$k$ quartic** `clm-yr6tu4` / `clm-k4d4ph` (that
    is parity-EVEN, achiral diamond point group — also NOT a parity test).
  - This node does **NOT** touch the AVE cosmic-birefringence observable
    ($E/B$ decoupling from $K/G \neq 2$); $g_0$ is a *different mechanism* and is
    deliberately NOT mapped onto the live $\beta \sim 0.3°$ anomaly (and could
    not be — the literal lattice-scale value is $\sim$40 OOM too large).

> **Leaf references:** [field-free-optical-activity](./falsification/ch12-falsifiable-predictions/field-free-optical-activity.md).

### Quality
- confidence: 0.55
- depends-on:
  - Axiom 1 (Substrate Topology — fixes the chiral srs $I4_1 32$ lattice + the ring-writhe pseudoscalar that sources the rotation)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 1.00)]
- rationale: The FORM-class CHORD — parity zero-vs-nonzero, with QED structurally pinned to exactly zero — is the cleanest possible divergence axis, and the qualitative facts (signed / enantiomorph-odd / diamond-null / writhe-sourced / lossless reciprocal gyrator) are live-confirmed node-up (GATE-1, PR #374). Solidity is pinned at 0.55 (input-only) because the *bankable* content is missing: the engine magnitude is an `ETA_ROT_PER_WRITHE` engineering decree (demoted PR #374), the substrate-derived $g_0$ = the $4_1$ screw pitch is a lattice-pitch holonomy $\sim$40 OOM over the cosmic bound, and the $k\to0$ continuum extraction — the only route to a bound-respecting optical-rotation magnitude — is OPEN. The node is FORM-class / CONSISTENCY-class on the parity axis, NOT a near-term magnitude falsifier. This is a DISTINCT channel from the field-induced birefringence coefficient (clm-pp3qwf) and the even-in-$k$ quartic (clm-yr6tu4 / clm-k4d4ph), both of which are parity-EVEN.
- strengthen-by:
  - Close the $k\to0$ continuum gyration extraction (a clean isolated transverse photon band, or a large/aperiodic-slab supercell with a PML-grade absorbing face for the cascade) so the bulk $g_0$ maps to a physical rad/m value — currently OPEN (`research/2026-06-23_chiral-vector-tlm-phase1_result.md` §9). Until then the magnitude is NOT bankable.
  - Build the co-vs-anti-handed pairwise $|F|$ ratio (Observable-C / "Stage-6", UNBUILT) — a *dimensionless* winding-parity forward prediction that dodges the $m_e/\alpha$-echo magnitude trap, now buildable since S1 PASSED.

---

## Torus Knot Baryon Forward Predictions $(2,17), (2,19), (2,21)$
<!-- id: clm-to41c7 -->

- $(2,17)$: $\sim 2742$ MeV, $(2,19)$: $\sim 2983$ MeV, $(2,21)$: $\sim 3199$ MeV; $\sim 170$ MeV per crossing
- _Specific Claims_
  - Six retrospective matches established (proton 0.00%, $\Delta(1232)$ 2.35%, $\Delta(1600)$ 1.11%, $\Delta(1900)$ 0.27%, $N(2190)$ 0.21%, $\Delta(2420)$ 2.40%) with **zero parameters adjusted between states**.
  - Three forward predictions for unobserved $(2, q)$ resonances, accessible to CLAS12 / PANDA.
  - Linear $\sim 170$ MeV/crossing spacing consistent with empirical Regge slope.
- _Specific Non-Claims and Caveats_
  - Falsification: no resonance within $\pm 100$ MeV of each prediction falsifies the ladder; departure from linear spacing at higher $c$ also falsifies. These are the framework's own falsification bounds, not unilateral confirmation criteria.
  - Per-row Δ% in the retrospective matches mixes "0.00%" (proton) with $\sim 2.4\%$ (top of error bar) — these are category (iv) derived predictions per the Master Prediction Table classification, but the proton 0.00% and the 2.40% are not the same kind of claim. The forward predictions inherit at least the 0.27%-2.40% scatter of the established matches.
  - Does NOT claim the forward predictions have been confirmed. They are open experimental targets.

> **Leaf references:** [baryon-mass-predictions](./falsification/ch12-falsifiable-predictions/baryon-mass-predictions.md), [torus-knot-baryon-predictions](./falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md).

### Quality
- confidence: 0.6
- depends-on:
  - Axiom 1 (topological-knot mass spectrum)
  - INVARIANT-C2 / CODATA $m_e$ (single physics input)
  - clm-k6olj8 (the generating ladder; this forward-predictions leaf inherits its band — cannot grade higher than its source)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.60)]
- 🔴 **Rule-12 SOLIDITY DEMOTION (2026-06-19, crossing-ladder-overclaim walk-back):** prior grade was **confidence 0.85 / solidity 0.85 ("ok to build on")**, justified by "2 of 3 forward predictions land on existing PDG $\ast\ast$ entries" + "6/6 $J^P$-consistent." Both supports were **retracted** in [`torus-knot-baryon-predictions.md`](./falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) on 2026-06-19: (a) the $c=17/c=19$ "forward predictions" are **postdictions** against pre-existing hardcoded PDG-2024 catalog entries (driver `PDG_2024_BARYONS` lines 119–136), not forward predictions; (b) the "6/6 $J^P$-consistent" is **null-dominated** — the driver's own `null_hypothesis_random_hits_3pct = 6.0` shows random nearest-mass matching is expected to hit all 6 within $3\%$, and the $J^P$ filter excludes nothing (any $J\le c/2$, either parity). This leaf can no longer be graded **above its generating claim clm-k6olj8 (solidity 0.60)**; demoted to match. The genuine surviving chord — integer-$c$, odd/even link-exclusion, $(2,3)$ = smallest knot, curved ladder FORM, single proton $+0.74\%$ bare-topology hit — is **preserved** and is what the 0.60 band now rests on. Original rationale preserved below.
- ~~rationale: The leaf is now PDG-2024-anchored with a verifiable driver (`baryon_ladder_pdg_2024_anchor.py`): 6/6 $J^P$-consistent retrospective matches (proton at $-0.002\%$), 2 of 3 forward predictions land on existing PDG $\ast\ast$ entries ($\Delta(2750)$ at $-0.30\%$, $\Delta(2950)$ at $+1.12\%$), from a zero-adjusted-parameter formula (1 CODATA input + 1 topological integer + 1 Borromean halo invariant). The claim-quality prose uses the older $(2,17)\to2742$ MeV labelling, which matches the leaf's $(2,17)$ row. These are category-(iv) derived predictions per the leaf. A closed, driver-reproducible derivation; the per-row $0.27\%$–$4.5\%$ scatter is honestly tabulated.~~ *(superseded 2026-06-19 — forward-confirmed + discriminator supports retracted; see demotion note above. Preserved per Rule-12.)*
- rationale: (revised 2026-06-19) The structural core survives and is genuine: a single closed-form $m(c)$ applied across the odd-$c$ ladder with zero parameters re-tuned between states, reproducing the $S=0$ $N/\Delta$ catalog to within $5\%$, with the proton at $+0.74\%$ bare-topology ($-0.002\%$ post one contained $\delta_{th}$). What does NOT survive is the ensemble-discriminator and forward-prediction framing (see Rule-12 demotion note above). Graded **input-only** to match its generating claim clm-k6olj8.
- strengthen-by:
  - Convert $c=21\to3199$ MeV into an SHA-pinned forward prereg (the one genuinely-open row; currently misses nearest cataloged $\Delta(2950)$ by $+8.4\%$) and resolve at CLAS12/PANDA.
  - Find a discriminator that the driver's own null model does NOT already pass (the current $J^P$ filter + $\pm3\%$ window is null-dominated).

---

## SPICE Particle Decay (Leaky Cavity) — Qualitative Muon Model
<!-- id: clm-c54kdd -->

- LC tank ($L = 1$ mH, $C = 1$ nF, IC = 150 kV) discharging through voltage-controlled switch at $V > V_{yield}$
- _Specific Claims_
  - Heavy-fermion decay (e.g. muon) reproduced as RC-discharge time constant: standing wave exceeds $V_{yield}$ → $R_{eff}$ collapses from $1\,\text{G}\Omega$ to $50\,\Omega$ → exponential decay.
  - The 43.65 kV breakdown is **invariant under bulk dielectric environment**: a muon at the bottom of the Mariana Trench decays at the same RC-discharge rate as in vacuum, because the muon's sub-femtometer topology sits in the void space between molecular electron clouds.
- _Specific Non-Claims and Caveats_
  - **The SPICE RC muon model is qualitative.** This is project-wide Critical Distinction #5 (LIVING_REFERENCE.md): the SPICE netlist demonstrates the *mechanism* (voltage-triggered avalanche → RC discharge), not the *quantitative lifetime*. The quantitative muon lifetime comes from the standard Fermi formula with AVE-derived $G_F$ (3.9% accurate per Master Prediction Table #13).
  - Does NOT claim the SPICE netlist's specific $L$ and $C$ values reproduce the empirical muon lifetime. The 1 mH / 1 nF values give a particular $\tau$; the leaves do not derive the actual muon $\tau \approx 2.2$ µs from these.
  - Bulk-dielectric invariance is a structural / geometric argument; it is not a measurement of muon decay rates in dense media.

> **Leaf references:** [spice-netlist](./simulation/ch14-leaky-cavity-particle-decay/spice-netlist.md), [theory](./simulation/ch14-leaky-cavity-particle-decay/theory.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 ($V_{yield}$ rupture → $\Gamma=-1$ leaky cavity)
  - INVARIANT-C1 ($V_{yield}\approx43.65$ kV)
  - clm-o2shcn (TVS solid→slipstream phase transition underlying the rupture cavity)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.70)]
- rationale: The mechanism — standing wave exceeding $V_{yield}$ collapses $R_{eff}$ ($1\,\text{G}\Omega\to50\,\Omega$) into an RC discharge — is cleanly modeled and the leaf is explicit (Critical Distinction #5) that this is QUALITATIVE: the SPICE netlist demonstrates the mechanism, not the quantitative lifetime (which comes from Fermi/$G_F$). The bulk-dielectric-invariance argument (muon topology in the void space between electron clouds) is a sound geometric argument. Disclosed-bound: closes as a mechanism demonstration, explicitly not a quantitative $\tau$ derivation.
- strengthen-by:
  - Derive the muon $L,C$ values from its topology so the RC time constant reproduces $\tau\approx2.2\,\mu$s rather than being a chosen $1$ mH / $1$ nF illustration.

---

## Autoresonant PLL — Schwinger Limit Bypass Mechanism
<!-- id: clm-9sujp8 -->

- $C_{eff}(V) = C_0 \sqrt{1 - (V/V_{60k})^2}$ detunes a fixed-frequency drive; PLL tracks the dropping resonant frequency
- _Specific Claims_
  - The vacuum acts as a Duffing oscillator: its non-linear capacitance shifts the local resonance as drive amplitude rises, detuning fixed-frequency lasers and reflecting power back at the source.
  - A phase-locked loop tracking the instantaneous $f = 1/(2\pi\sqrt{LC_{eff}})$ allows a continuous-wave drive at far lower power to ring up the lattice past the Schwinger limit and trigger pair production.
- _Specific Non-Claims and Caveats_
  - This is an **engineering proposal / SPICE proof-of-concept**, not a demonstrated experiment. No leaf claims pair production has been induced via PLL drive at sub-petawatt levels.
  - The 60 kV "bulk-avalanche limit" used in this chain is distinct from $V_{yield}$ (43.65 kV) — see the $V_{yield}$ vs $V_{snap}$ entry above. The SPICE model uses 60 kV as the rupture threshold; the leaves do not reconcile this with the 43.65 kV figure quoted elsewhere.
  - Reflected-power detuning is a standard non-linear-resonator behavior; the framework's specific contribution is identifying the vacuum's $C(V)$ form and the PLL bypass — neither of which is independently measured at vacuum-rupture amplitudes.

> **Leaf references:** [autoresonant-dielectric-rupture](./falsification/ch12-falsifiable-predictions/autoresonant-dielectric-rupture.md), [autoresonant-helicity](./falsification/ch12-falsifiable-predictions/autoresonant-helicity.md), [spice-netlist](./simulation/ch15-autoresonant-breakdown/spice-netlist.md), [theory](./simulation/ch15-autoresonant-breakdown/theory.md).

### Quality
- confidence: 0.3
- depends-on:
  - Axiom 4 (nonlinear $C_{eff}(V)$ Duffing detuning)
  - clm-o2shcn (TVS solid→slipstream transition setting the $\eta_{eff}(V)$ step)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 0.70)]
- rationale: The primary leaf `simulation/ch15-autoresonant-breakdown/theory.md` carries an explicit ⛔ INVALIDATED — RECOMPUTATION REQUIRED banner: the $C_{eff}(V)=C_0\sqrt{1-(V/60\text{k})^2}$ detuning curve, the PLL frequency-tracking demonstration, and the "pumps past the 60 kV yield" Schwinger-bypass conclusion all rest on the wrong 60 kV rupture threshold (the canonical yield is 43.65 kV). The leaf's own notice states "none of the numerical autoresonant predictions" are defensible. The Duffing-detuning qualitative picture survives, but every quantitative claim is flagged for recompute. Asserted-partial at best.
- strengthen-by:
  - Recompute the entire $C_{eff}(V)$ detuning and PLL-bypass chain against $V_{yield}=43.65$ kV per the leaf's banner.

---

## Sapphire Phonon Centrifuge — Predicted 6.35 G Artificial Gravity
<!-- id: clm-iz3svl -->

- $a_{LT} = v_{vac}^2 / r$ with $v_{vac} = v_{sound} \times (\rho_{Al_2O_3}/\rho_{bulk})$
- _Specific Claims_
  - 1 m sapphire sphere with phased ultrasonic transducers at 11{,}100 m/s sound speed → $v_{vac} \approx 5.58$ m/s → centripetal Lense-Thirring $\approx 62.3$ m/s$^2$ (6.35 G) at the center.
- _Specific Non-Claims and Caveats_
  - Treats $\rho_{bulk} = 7.91 \times 10^6$ kg/m$^3$ as a derived AVE constant; the prediction is downstream of that derivation — see the Sagnac-RLVE entry caveat about $\rho_{bulk}$ being framework-derived rather than independently measured.
  - Has NOT been experimentally tested. Predicted as an **industrial-scale artificial-gravity device**; engineering feasibility of trapping a stable acoustic vortex at 11.1 km/s in a 1 m sapphire sphere is asserted, not demonstrated.
  - "Inductive shield" framing (Beltrami coil + acoustic vortex → impenetrable boundary) is a structural / interpretive consequence, not an independent prediction.

> **Leaf references:** [sapphire-phonon-centrifuge](./falsification/ch11-experimental-bench-falsification/sapphire-phonon-centrifuge.md), [industrial-scaleup](./falsification/ch11-experimental-bench/industrial-scaleup.md).

### Quality
- confidence: 0.6
- depends-on:
  - Axiom 1 (Sagnac mass-density-coupled mutual inductance; framework-derived $\rho_{bulk}$)
  - clm-qx9bb8 (active Sagnac material-dependent entrainment law)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.60)]
- rationale: The chain $v_{vac}=v_s(\rho_{Al_2O_3}/\rho_{bulk})\approx5.58$ m/s → $a_{LT}=v_{vac}^2/r=6.35$ G is clean algebra. But the whole prediction is downstream of the framework-derived $\rho_{bulk}=7.91\times10^6$ kg/m³ (imported, not independently grounded — same caveat as the Sagnac-RLVE entry), and the engineering feasibility of trapping a stable 11.1 km/s acoustic vortex in a 1 m sapphire sphere is asserted, not demonstrated. The "inductive shield" framing is disclosed as interpretive. Substantive open dependency on $\rho_{bulk}$ pins the band.
- strengthen-by:
  - Ground $\rho_{bulk}$ independently (or carry its derivation provenance inline) so the $a_{LT}$ prediction is not contingent on an unverified bulk-density import.

---



## Definitive Binary Kill-Switches (Neutrino Parity, GRB Dispersion)
<!-- id: clm-gw2wgc -->

- _Specific Claims_
  - Detection of a stable, freely propagating right-handed neutrino permanently falsifies the $\tfrac{1}{3}G_{vac}$ microrotational boundary condition of the chiral LC bandgap → destroys the AVE Weak Force derivation.
  - Energy-dependent arrival-time delay (lattice dispersion) in trans-Planckian gamma-ray bursts falsifies the framework's photon-as-massless-link-variable claim.
- _Specific Non-Claims and Caveats_
  - These are **falsification criteria**, not predictions of detection. AVE asserts both should produce null results under current observation; positive detection of either falsifies the framework.
  - The leaf abbreviates a longer original list (the heading promises three but only two are present in this leaf; treat as the published subset).

> **Leaf references:** [epistemology-of-falsification](./falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md), [epistemology-kill-switches](./falsification/ch11-experimental-bench/epistemology-kill-switches.md), [binary-kill-switches](./falsification/ch12-falsifiable-predictions/binary-kill-switches.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 1 (chiral LC bandgap → weak-force chirality)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: Both kill-switches are cleanly stated falsification criteria, each anchored to a named framework structure: right-handed-neutrino detection falsifies the $\tfrac13 G_{vac}$ microrotational boundary of the chiral LC bandgap; energy-dependent GRB arrival-time dispersion falsifies the photon-as-massless-link-variable claim. These are disclosed-import predictions (null expected) tied to specific axioms, not in-leaf derivations of the bandgap/decoupling theorem. The leaf notes the heading promises three but only two are present here (the third is the $E^4$ birefringence switch, clm-pp3qwf). Cleanly-anchored falsification criteria resting on imported derivations. **🔴 WEAK-C HONEST-SCOPE UPGRADE (2026-06-15, Rule 12 — rationale above PRESERVED; gate `wejkhvnfb`, Grant-confirmed 2026-06-14; prereg at repo-root `research/2026-06-15_weak-c-photon-continuum_prereg.md`):** the GRB no-dispersion kill-switch is upgraded from "asserted / substrate MISSING" to a **regime-grounded + empirically-corroborated prediction** — under weak-C the free photon is the continuum EM field (LC-ladder long-wavelength regime, sub-saturation, $Z_0$-matched, unlocked), so no zone-edge $(q\ell_{node})^2$ dispersion **follows from the regime** AND is corroborated by GeV–TeV GRB nulls (GRB090510 31 GeV; LHAASO 221009A 13 TeV across ~Gpc). It is explicitly **NOT** a fully-derived "topological decoupling theorem": the rigorous proof that the continuum limit is *exact* ($\delta = 0$, $\omega = ck$) remains OPEN; asserting it as derived would be substitution-not-retraction (A47 v11b). Carry no-LIV as a flagged prediction, not a theorem. Confidence/solidity UNCHANGED at 0.70 (no Class-2 lift; the upgrade is the no-dispersion's epistemic basis moving from asserted → regime-grounded+corroborated, not a derivation closure). The distinct $(q\ell_{node})^4$ optical birefringence (clm-pp3qwf, $\delta \approx 2.2 \times 10^{-22}$) is the surviving forward prediction and is KEPT.
- strengthen-by:
  - Include or cross-link the in-leaf derivation of the $\tfrac13 G_{vac}$ microrotational boundary condition so the neutrino-parity switch is traceable to its source.
  - Deliver the rigorous continuum-limit / topological-decoupling proof so the GRB no-dispersion prediction can move from regime-grounded+corroborated (weak-C) to derived; until then it is carried as a flagged prediction, not a theorem.

---

## Orbital Friction Paradox — Reactive vs Real Power
<!-- id: clm-v6ti0v -->

- $P_{real} = F_g \cdot v_{orb} \cos(90°) \equiv 0$ W for a stable circular orbit
- _Specific Claims_
  - Stable planetary orbit has radial gravity orthogonal to tangential velocity → $\theta = 90°$ → real power dissipation is identically zero → orbit is structurally a lossless LC tank operating in pure reactive power.
  - Eliminates the "vacuum drag" objection to AVE: inductive drag is suppressed by the dielectric phase transition ($\eta \to 0$), and the remaining gravitational coupling is purely orthogonal.
- _Specific Non-Claims and Caveats_
  - "$\theta = 90°$ → zero loss" is a **classical AC-power-analysis result** (real vs reactive power); AVE's contribution is identifying the orbital geometry as the physical realization of this circuit. Not an independent quantitative prediction.
  - Does NOT account for measurable orbital decay where $\theta \neq 90°$ (gravitational-wave inspiral, atmospheric drag, tidal dissipation) — these are framed as "$\theta \neq 90°$" perturbations consistent with the same framework. No quantitative match to observed inspiral rates is claimed in-leaf.

> **Leaf references:** [orbital-friction-paradox](./circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 ($\eta\to0$ dielectric-phase-transition drag suppression)
  - clm-i9l284 (Topo-Kinematic identity mapping $F_g\to V$, $v_{orb}\to I$)
  - clm-o2shcn (TVS solid→slipstream transition giving the $\eta_{eff}(V)$ drag step)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.70)]
- rationale: $P_{real}=F_g\,v_{orb}\cos(90°)\equiv0$ is exact classical AC-power algebra, and the orthogonality of radial gravity to tangential velocity in a circular orbit is correct. The AVE-specific content — identifying orbital geometry as a lossless reactive LC tank — is a sound mapping but, as the leaf discloses, not an independent quantitative prediction (it imports the $\eta\to0$ drag-suppression result and recasts a standard power-analysis identity). The $\theta\neq90°$ inspiral case is acknowledged without a quantitative match. Closes cleanly given the imported drag-suppression.
- strengthen-by:
  - Derive a quantitative $\theta\neq90°$ orbital-decay rate and compare to an observed inspiral so the framework makes a prediction beyond the lossless-tank identity.

---

## CLEAVE-01 Femto-Coulomb Electrometer ($Q = \xi_{topo}\, x = 0.415$ pC/$\mu$m)
<!-- id: clm-ydksh6 -->

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
  - **Discriminator is two-sided (2026-06-03); node-occupation gap CLOSED.** The dielectric-invariance leg (P2: the $\xi_{topo}\cdot x$ floor is the dielectric-invariant residue under material swap at fixed $C_{in}$) rests on the solid-dielectric node-occupation case, now closed by substrate-native derivation ([`research/2026-06-03_topological-charge-occupation-robustness.md`](../../../research/2026-06-03_topological-charge-occupation-robustness.md)): the floor LOCKS. **F2 precision:** the falsification target / protected quantity is $\mathcal{Q} = \mathrm{Link}(\partial\Omega,\mathbf{F})\in\mathbb{Z}$ (the integer linking charge — the no-hair observable; Pauli-saturated atomic occupancy is no-hair-INVISIBLE to the swept loop), with $\xi_{topo} = e/\ell_{node}$ as the **frozen-metric unit-bridge** that converts it to volts ($\ell_{node}=\hbar/m_e c$, unchanged by a dielectric slab) — $\xi_{topo}$ is not itself a topological invariant. Caveat (a measurable prediction): the lock holds iff the dielectric preserves the substrate's topological gap; a gap-closing material would shift the floor. ($\xi_{topo}=\sqrt{\alpha}$ in native units, so an isolated-$\xi_{topo}$ slope deviation is also an $\alpha$-chain signal.)

> **Leaf references:** [project-cleave-01](./falsification/ch11-experimental-bench-falsification/project-cleave-01.md), [pcba-bench-protocols](./falsification/ch11-experimental-bench/pcba-bench-protocols.md).

### Quality
- confidence: 0.85
- depends-on:
  - Axiom 2 ($Q\equiv\xi_{topo}\,x$ topo-kinematic identity)
  - clm-i9l284 (the topological-kinematics identity tested)
- solidity: 0.85 (ok to build on) [= min(0.85, 0.90)]
- rationale: The prediction $Q=\xi_{topo}x=0.415$ pC for a $1\,\mu$m step and the $V=Q/C=41.5$ mV/µm readout into a controlled 10 pF parasitic are clean zero-free-parameter algebra directly off Axiom 2. The parasitic-C contingency is disclosed (a different $C$ rescales linearly, does not falsify), and the leaf flags an in-source authoring error (the identity is Ch.01, not Ch.13). A discriminator vs piezo/triboelectric (dielectric-independence) is given. Clean derived prediction; pinned just below 0.9 because the readout magnitude is contingent on the assumed parasitic.
- strengthen-by:
  - Specify the measured in-circuit parasitic $C$ (or a guard-ring design that fixes it) so the 41.5 mV/µm step is a fixed, not rescalable, target.

---

## CLEAVE-01 Requirements / Boundary Conditions (derived apparatus floors for the $\xi_{topo}$ bench)
<!-- id: clm-fuajdb -->

- The **derived, frozen boundary conditions** any CLEAVE-01 apparatus must satisfy to adjudicate its own falsifier, read top-down from the measurement physics. Every number is physics-set from $\{m_e, \ell_{node}, e\}$ + the held-DC/multi-hour-sweep noise model, or is written parametric in an open design knob ($\delta$, $C_{in}$).
- _Specific Claims_
  - The position→charge master coupling is $dV/dx = \xi_{topo}/C_{in} = 41.49$ nV/pm at $C_{in}=10$ pF — gap jitter rides the *same* transfer function as the signal and is non-averageable, so pm-class gap-hold + vibration isolation are the hardest mechanical specs (physics-set, zero free parameters).
  - The binding noise model for a held-DC step over a multi-hour $N\ge50$ sweep is 1/f + drift (~0.61 µV rms in-band), NOT white noise (~10 nV/hold) — so the binding readout spec is LEVEL STABILITY ($\sigma_Q \le \delta\times414.9$ fC), not single-shot resolution. This is a fundamental property of any DC-comparison measurement.
  - The CPD background is ~21.3% of floor scaling $1/g^2$; across a $1\times\!\to\!4\times$ sweep it swings 19.97% of floor — the level-stability bar the chord adjudication must beat.
  - The bias-current ramp (20.0 fC/s on 10 pF) rails a bare follower $\Rightarrow$ step-differencing / reset-integration is a topology boundary condition. $kTC$ = 0.20 fC sets no wall.
  - All design-dependent specs (charge resolution, ENOB, drift, repeatability, gap-knowledge, $C_{in}$-fixed, thermal, vibration, EMI) are stated as the requirement *as a function of* the open knob, with safety factor $k=3$.
- _Specific Non-Claims and Caveats_
  - **Selects NOTHING.** This claim is the derived requirement set; the make-vs-buy selections and design-knob choices live in the sibling **trade-study decision-register (STATUS:OPEN, a `no-claim` record)** and are NOT adjudicated here.
  - The slope magnitude (0.415 pC/µm) is a consistency-class echo ($\xi_{topo}=\sqrt{\alpha}$ native + $\ell_{node}$=Compton); the tight Level-2 specs that protect it are consistency-polishing and must NOT be read as gating the emergence-class chord. The chord (gap-independent integer floor) is $\delta$- and $C_{in}$-absolute-independent.
  - Cite-line drift surfaced (prereg cites `XI_TOPO:246`/`L_NODE:234`; verified `:291`/`:257`) and an internal corpus inconsistency (leaf/Femto carry the superseded single-1-µm-step framing) are flagged flag-don't-fix, NOT resolved here.
  - Not performed; this is the apparatus boundary-condition datasheet, not a measurement result.

> **Leaf references:** [cleave-01-requirements-boundary-conditions](./falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md).

### Quality
- confidence: 0.85
- depends-on:
  - clm-ydksh6 (the canonical CLEAVE-01 $Q=\xi_{topo}x$ prediction these floors spec the bench against)
- solidity: 0.85 (ok to build on) [= min(0.85, 0.85)]
- rationale: The boundary conditions are clean dimensional + noise-model algebra off the canonical $\xi_{topo}=e/\ell_{node}$ floor — the 41.49 nV/pm coupling, the 19.97% CPD swing, the 20.0 fC/s bias ramp, the 0.20 fC $kTC$, and the ENOB/level-stability math all reproduce from canonical primitives (verified against `constants.py:291/257/100`). The 1/f-not-white binding-noise argument is the load-bearing structural finding and is correct for a held-DC step over a multi-hour sweep. Pinned at the parent prediction's 0.85: the derivations are sound and parametric (no pinned number pre-empts an open knob), but the floors inherit the parent's contingency on $C_{in}$ and the still-OPEN $C_{in}$-fixed topology (Q-C15-04). Honestly scoped: it derives requirements, it selects nothing.
- strengthen-by:
  - Close Q-C15-04 (the $C_{in}$-FIXED-while-$g$-sweeps topology) so the H3 boundary condition transfers from "tension" to a met mechanical or metrological spec.
  - Freeze Q-C15-02 ($\delta_{chord}$, $\delta_{slope}$) so the parametric specs collapse to pinned numbers.

---

## ROENTGEN-03 Solid-State Sagnac Induction ($B \approx 4.2$ pT)
<!-- id: clm-qsgl7d -->

> **Scope correction (2026-06-03 audit, Grant-adjudicated): RETIRED forward → corroborative-null, alongside A2-SAGNAC.** Same $\kappa = \rho_{rotor}/\rho_{bulk}$ entrainment, different transducer (Röntgen $\mathbf{v}\times\mathbf{E}$ magnetic pickup vs optical Sagnac); the Earth-rotor ring-laser-gyro exclusion ($+7\times10^{-4}$ bias excluded by $7\times10^4\times$) applies identically. The 4.2 pT prediction inherits the excluded $\kappa$; surviving fragment = RPM-linearity + $180°$ phase-flip self-consistency, NOT a forward kill-switch. See A2-SAGNAC retirement in `divergence-test-substrate-map.md`.

- Spinning a non-metallic dense ceramic disk at 10k RPM creates $v_{vac} \approx 0.038$ m/s at $r=5$ cm; an interdigitated capacitor driven at 10 kV / 1 kHz overhead synthesizes a $B \approx 4.2$ pT alternating field via $\mathbf{B} = (1/c^2)\,\mathbf{v} \times \mathbf{E}$ acting on the induced vacuum drift.
- _Specific Claims_
  - Roentgen's 1888 moving-dielectric induction extended to the bulk vacuum metric: spinning a neutral mass macroscopically phase-shifts the substrate via mutual inductance, allowing a B-field to be synthesized from the vacuum's own induced drift rather than from any embedded current.
  - The 4.2 pT prediction induces $\sim 0.26\,\mu$V in a differential planar pickup coil. Standard hardware Lock-In amplifier extracts the signal from noise floor.
  - Falsification: amplitude must scale strictly linearly with RPM and flip phase $180°$ on motor reversal. Substrate signature: failure of either scaling falsifies the inductive density $\rho_{bulk} \approx 7.9 \times 10^6$ kg/m$^3$ at this scale.
- _Specific Non-Claims and Caveats_
  - Has NOT been performed; this is the proposed protocol with predicted readout.
  - The 0.038 m/s drift velocity uses the Sagnac-RLVE entrainment chain: it is contingent on the same framework-derived $\rho_{bulk}$ as the Sagnac-RLVE signal — see the Sagnac-RLVE entry's caveat about $\rho_{bulk}$ being framework-derived.
  - Lock-In SNR is asserted; no leaf-level noise budget proves the $\sim 0.26\,\mu$V signal is recoverable in the presence of motor EMI, mains hum, and ground-loop noise typical of high-RPM rigs.

> **Leaf references:** [project-roentgen-03](./falsification/ch11-experimental-bench-falsification/project-roentgen-03.md), [pcba-bench-protocols](./falsification/ch11-experimental-bench/pcba-bench-protocols.md).

### Quality
- confidence: 0.55
- depends-on:
  - Axiom 1 (Sagnac material-dependent entrainment; framework-derived $v_{vac}$, $\rho_{bulk}$)
  - clm-qx9bb8 (active Sagnac material-dependent entrainment law)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.60)]
- rationale: The Roentgen $\mathbf{B}=(1/c^2)\mathbf{v}\times\mathbf{E}$ synthesis and the $\sim4.2$ pT → $\sim0.26\,\mu$V pickup are dimensionally clean, but the load-bearing input — the $v_{vac}\approx0.038$ m/s drift at 10k RPM — rests on the framework-derived $\rho_{bulk}\approx7.9\times10^6$ kg/m³ via the same Sagnac-RLVE entrainment chain (imported). The Lock-In SNR recoverability of $0.26\,\mu$V against motor EMI / mains / ground-loop noise is asserted with no leaf-level noise budget. Closes given imports but with a real open dependency on $\rho_{bulk}$ plus an unshown SNR claim.
- strengthen-by:
  - Provide a noise budget proving $\sim0.26\,\mu$V is recoverable on a high-RPM rig.
  - Ground $\rho_{bulk}$ / $v_{vac}$ independently of the framework derivation.

---

## ZENER-04 Impedance Avalanche Detector — Anomalous Knee at 43.65 kV
<!-- id: clm-cltls0 -->

- 80 kV transient (sub-µs rise) into an encapsulated spherical electrode in vacuum; AVE predicts an anomalous "Avalanche Knee" — a sudden non-linear spike in displacement current $I_D = C\,dV/dt$ at the moment the localized field crosses $V_{yield} = 43.65$ kV.
- _Specific Claims_
  - The vacuum LC network behaves identically to a Transient Voltage Suppression (TVS) Zener diode: rigid $Z_0 \approx 377\,\Omega$ until $V > V_{yield}$, then absolute impedance rupture ($\Gamma = -1$) drops the effective impedance to zero.
  - Standard linear electrostatics predicts $I_D = C\,dV/dt$ remains perfectly linear during charging of an isolated spherical capacitor; AVE predicts a distinct, anomalous discontinuity exactly at the topological yield voltage.
  - Falsification: a perfectly linear $I_D(V)$ across the 43.65 kV crossing falsifies the impedance-rupture mechanism that underlies the SPICE leaky-cavity model, the autoresonant PLL bypass, and the Zener-avalanche side of the vacuum impedance mirror.
- _Specific Non-Claims and Caveats_
  - Has NOT been performed; this is the proposed Marx-generator protocol.
  - The 43.65 kV figure is the same $V_{yield} = \sqrt{\alpha} \cdot m_e c^2/e$ used elsewhere in Vol 4. Note that several adjacent leaves (autoresonant-breakdown, levitation-array) instead use 60 kV as the avalanche threshold — see the $V_{yield}$ vs $V_{snap}$ entry for the regime distinction; ZENER-04 specifically targets the 43.65 kV onset.
  - "Encapsulated spherical electrode in vacuum" is a hardware mitigation for atmospheric Paschen arcing; classical surface-arc artefacts inside an imperfect chamber would mimic an avalanche knee and must be excluded by the vacuum quality. The leaf does not specify a vacuum-quality threshold.

> **Leaf references:** [project-zener-04](./falsification/ch11-experimental-bench-falsification/project-zener-04.md), [pcba-bench-protocols](./falsification/ch11-experimental-bench/pcba-bench-protocols.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (TVS-Zener impedance-rupture mechanism)
  - INVARIANT-C1 ($V_{yield}\approx43.65$ kV)
  - clm-kezk9z ($Z_0\approx377\,\Omega$ baseline)
  - clm-o2shcn (TVS solid→slipstream phase transition driving the Zener rupture)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.70)]
- rationale: The predicted "Avalanche Knee" — an anomalous $I_D=C\,dV/dt$ discontinuity exactly as the localized field crosses $V_{yield}=43.65$ kV — follows cleanly from the TVS impedance-rupture mechanism (clm-o2shcn), contrasted against the linear electrostatic prediction. The protocol (80 kV sub-µs Marx into an encapsulated spherical electrode) is concrete and falsifiable, and the leaf correctly anchors on the 43.65 kV onset (vs the 60 kV figure used elsewhere). Disclosed gap: no vacuum-quality threshold specified to exclude surface-arc mimics. A clean mechanism-following prediction with one disclosed protocol gap.
- strengthen-by:
  - Specify the vacuum-quality threshold needed to exclude classical surface-arc artefacts mimicking the knee.

---

## TORSION-05 Horizontal Metric Rectification — $\sim 100\,\mu$N DC Thrust
<!-- id: clm-kl1ern -->

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

> **Leaf references:** [project-torsion-05](./falsification/ch11-experimental-bench-falsification/project-torsion-05.md), [pcba-bench-protocols](./falsification/ch11-experimental-bench/pcba-bench-protocols.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 4 (impedance-rupture / $\Gamma=-1$ at fast edge)
  - INVARIANT-C1 ($V_{yield}\approx43.65$ kV one-way valve)
  - clm-ui3m8a (1.846 g vertical cap this protocol bypasses)
  - clm-o2shcn (TVS solid→slipstream transition enabling the fast-edge rupture)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.60)]
- rationale: The one-way-impedance-valve concept (slow $+500$ V grip → $+0.207$ mN matched; fast $-75$ kV kickback → ruptured $\Gamma=-1$ → $0$ mN reaction) gives a $\sim100\,\mu$N time-averaged DC thrust, but this rests on an IDEALIZED perfect step-function rectification at the $V_{yield}$ crossing. The leaf explicitly does NOT quantify the finite-rise-time backward-reaction leakage floor (even at $<10$ ns) and does not enumerate Cavendish-pendulum systematics (patch potentials, gas drift, seismic) at the 100 µN level. Real open gaps in the quantitative prediction pin it at substantive-open-dependency.
- strengthen-by:
  - Quantify the backward-reaction leakage from the finite 75 kV flyback rise time, which sets the actual net-thrust floor.
  - Enumerate and bound the Cavendish systematic backgrounds at the $100\,\mu$N scale.

---

## Achromatic Impedance Lens (Protocol 9) — $\Gamma = 0$ Across All Angles
<!-- id: clm-k9up5c -->

- Gravity scales $\mu(r)$ and $\varepsilon(r)$ proportionally → $Z_{gravity} = \sqrt{\mu_0\, n(r)/(\varepsilon_0\, n(r))} = Z_0$, identically. A laboratory metamaterial dielectric with $\mu_r$ and $\varepsilon_r$ co-doped at the same radial gradient should mimic a gravitational well and exhibit $\Gamma = 0$ at all incidence angles, bypassing classical Fresnel reflection.
- _Specific Claims_
  - Identifies gravity as an *achromatic* impedance lens: the physical reason photons bend in a gravitational well without producing any Fresnel reflection (no $S_{11}$ return) is that $\mu$ and $\varepsilon$ scale together, preserving the characteristic impedance.
  - Provides a benchtop falsifier: a co-doped $\mu_r$/$\varepsilon_r$ metamaterial under VNA or optical-laser sweep should display physically zero reflection across all angles — a signature standard non-engineered metamaterials cannot reproduce.
  - Sharp discriminator vs. standard impedance-mismatched lenses (whose $\Gamma$ rises with angle off normal).
- _Specific Non-Claims and Caveats_
  - This is the asymmetric-vs-symmetric saturation distinction that anchors the cross-cutting Symmetric-vs-Asymmetric Saturation entry. The Achromatic Lens prediction is the *symmetric* invariance result; the Vacuum Impedance Mirror entry is the *asymmetric* divergence result. Do NOT mix the two: the same axiom set produces opposite reflection behavior depending on which constitutive parameter is strained.
  - Has NOT been demonstrated. Co-doping $\mu_r$ and $\varepsilon_r$ at exactly proportional radial gradients is itself a non-trivial fabrication problem; achievable proportionality is asserted, not built.
  - "Mimics a gravitational well" is structural — the metamaterial reproduces the impedance signature, not the curvature of spacetime; the experiment falsifies the impedance-pair hypothesis, not General Relativity directly.

> **Leaf references:** [achromatic-lens-test](./falsification/ch11-experimental-bench-falsification/achromatic-lens-test.md), [advanced-protocols](./falsification/ch11-experimental-bench/advanced-protocols.md).

### Quality
- confidence: 0.8
- depends-on:
  - Axiom 4 (symmetric saturation branch — $\mu$ and $\varepsilon$ scale together)
  - clm-kezk9z (symmetric-gravity $Z=Z_0$ invariance)
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 0.90)]
- rationale: $Z_{gravity}=\sqrt{\mu_0 n(r)/(\varepsilon_0 n(r))}=Z_0\Rightarrow\Gamma=0$ at all incidence angles is identity-grade algebra (the $n(r)$ cancels exactly), and the leaf correctly anchors this as the symmetric branch, explicitly opposite to the asymmetric Vacuum-Impedance-Mirror result (clm-5s5b0d). The benchtop falsifier (co-doped $\mu_r/\varepsilon_r$ metamaterial showing zero reflection all-angle) is concrete and the "mimics gravity, not GR-curvature" scope is disclosed. The derivation is clean; the fabrication of exactly-proportional gradients is disclosed as a non-trivial open engineering problem.
- strengthen-by:
  - Specify an achievable $\mu_r/\varepsilon_r$ co-doping recipe and quantify the proportionality tolerance below which $\Gamma$ stays measurably zero.

---

## Orbital Boundary Trapping (Protocol 10) — Asteroid Belt and Oort Cloud as Impedance Shocks
<!-- id: clm-h55fy1 -->

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

> **Leaf references:** [boundary-trapping-test](./falsification/ch11-experimental-bench-falsification/boundary-trapping-test.md), [advanced-protocols](./falsification/ch11-experimental-bench/advanced-protocols.md).

### Quality
- confidence: 0.3
- depends-on:
  - Axiom 1 (LC-network impedance-shear boundary)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: This is an interpretive identification of the Asteroid Belt and Oort Cloud as inner/outer termination shocks of the solar metric slipstream. The strain scaling $h_\perp\propto1/r$ is stated only qualitatively; there is no quantitative $\Delta v(r)$ prediction across the $\sim15{,}000$ AU boundary against which a probe transit could be compared, and the leaf neither refutes the standard Jupiter-resonance-shepherding / anisotropic-thermal explanations nor compares contributions. Asserted mechanism with qualitative support, no closed derivation.
- strengthen-by:
  - Produce a quantitative $\Delta v$ vs $r$ inductive-drag-spike prediction at the 15,000 AU boundary, distinguishable from resonance-shepherding and thermal-recoil alternatives.

---

## GEO-Synchronous Impedance Differential (Protocol 12) — Vertical Laser TOF Anomaly
<!-- id: clm-cwjd8t -->

- Vertical laser link from a ground station to a GEO satellite ($h = 35{,}786$ km, classical TOF $\sim 119$ ms): the AVE non-linear impedance integral $\int n(r)/c\,dr$ stretches the round-trip optical path by fractions of a millimeter relative to the linear-distance prediction. Correlated against atomic clocks, this Topological Delay maps the LC saturation envelope of Earth.
- _Specific Claims_
  - Gravity is reframed (per Axiom 3 in Vol 4) as a macroscopic spherically symmetric impedance gradient $\Delta Z_0$, with the local phase velocity $c_{eff}$ statistically faster in deep space than at the Earth's surface — a structural prediction, not a fitted gravitational redshift parameter.
  - At $O(GM/c^2 r)$ the AVE impedance integral $\int n(r)/c\,dr$ with $n(r) = 1 + 2GM/c^2 r$ is **mathematically identical to the GR Shapiro delay**, so the vertical TOF is the same in AVE as in GR — there is NO AVE-distinct prediction at this order (corroborative-null, per the leaf's 2026-05-16 scope correction). The only AVE-distinct contribution is the discrete-lattice correction, cubic-symmetry-suppressed to $\sim 10^{-22}$ (undetectable).
- _Specific Non-Claims and Caveats_
  - The "fractions of a millimeter" path-stretch is qualitative — no leaf-level numerical prediction of $\Delta t$ at the GEO altitude is given against which a measurement could be compared. Compare to the Sagnac-RLVE entry, which gives a specific 2.07 rad prediction.
  - Standard general-relativistic Shapiro delay also predicts a non-trivial $\int n(r)/c\,dr$-style integral; the leaf does not quantitatively distinguish the AVE prediction from Shapiro at this altitude.
  - "Definitively breaking Lorentz symmetry in favor of structural waveguide electrodynamics" is the framework's interpretive framing; the proposed observation is consistent with multiple gravity models, not uniquely with AVE in the absence of a numerical bound.
  - Has NOT been performed; ground-to-GEO laser-link clock-comparison experiments at the required precision are not standard.

> **Leaf references:** [geo-synchronous-impedance](./falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md), [advanced-protocols](./falsification/ch11-experimental-bench/advanced-protocols.md).

### Quality
- confidence: 0.3
- depends-on:
  - Axiom 3 (gravity as macroscopic impedance gradient $\Delta Z_0$)
- solidity: 0.30 (do not build on, rework needed) [= min(0.30, 1.00)]
- rationale: Corroborative-null. The leaf's 2026-05-16 scope correction establishes that AVE's $n(r)=1+2GM/c^2r$ is mathematically identical to the GR Gordon-metric Shapiro integrand, so $\int n(r)/c\,dr$ yields the SAME vertical TOF — no AVE-distinct prediction at $O(GM/c^2r)$. The only AVE-distinct piece is cubic-symmetry-suppressed (~$10^{-22}$, undetectable), and the earlier "16.7 mm" stretch was retracted. The entry now matches the leaf (forward Lorentz-breaking framing dropped 2026-05-24): an honest GR-equivalence, not a distinct closed prediction — hence the low local-rigor band (it reproduces a known result rather than deriving a falsifiable AVE-specific one).
- strengthen-by:
  - To become AVE-distinct, identify a regime where the discrete-lattice $(q\ell_{node})^4$ correction escapes cubic-symmetry suppression (e.g. a trans-Planckian probe), or a configuration where $n(r)$ measurably departs from the GR Shapiro form.

---

## Existing Experimental Signatures Catalog (Proton Radius, Neutron Lifetime, Hubble Tension, LIGO Echoes, Vortex Cores)
<!-- id: clm-oiw6cb -->

A catalog of five empirical anomalies presented as exact mechanical consequences of the LC lattice — no fitted parameters per anomaly.

- _Specific Claims_
  - **Proton radius puzzle** ($0.84$ fm muonic vs $0.88$ fm electronic, 4% gap): the proton has not shrunk; the muon orbits $\sim 200\times$ closer, generating $E_\mu^2 \sim 40{,}000\times$ stronger local field that activates the Vacuum Kerr Effect, compressing the local probe wavelength $\lambda_{local} = \lambda_0 / n(\mathbf{r})$. The 4% gap is the optical integration of the Kerr index over the muon's tight orbital volume.
  - **Neutron lifetime anomaly** ($\sim 9$ s shorter in bottle vs beam): the neutron is a metastable threaded knot ($6^3_2 \cup 3_1$); decay is a topological snap. Bottle walls couple resonant phonon vibration into the knot, statistically accelerating the snap.
  - **Hubble tension** ($H_0^{local} \approx 73$ vs $H_0^{CMB} \approx 67$ km/s/Mpc): the universe is actively crystallizing new spatial volume. Early universe latent-heat back-pressure throttled the genesis rate; late universe (cold vacuum) allows the un-inhibited equilibrium $H_\infty \approx 69.32$ km/s/Mpc to be approached. The tension is the cooling-curve of an ongoing spatial phase transition.
  - **LIGO GW150914 black-hole echoes**: at the **shear/bulk** rupture boundary $r_{sat}=7GM/c^2$ the reflection coefficient hits $\Gamma_{shear}=\Gamma_{bulk}=-1$ ($G_{shear}\to0\Rightarrow Z_{shear}=\rho c_{shear}\to0$, an Op3 short — **shear-mode**, *not* an $\varepsilon$-sector "dielectric rupture"; the EM channel stays matched, $\Gamma_{EM}=0$) → the horizon is a hard reflective boundary for shear/GW modes, not a one-way membrane → echoes are *predicted* by AVE. **[2026-06-17 overclaim-correction (Rule 12); original parenthetical read "($\sim 0.29$ s spacing)" with "$\Gamma = -1$ (dielectric rupture)" — RETRACTED on BOTH counts: channel (shear-mode, not $\varepsilon$-dielectric) and quantity (below).]** AVE FORCES a **parameter-free $\sim 4$ ms** shear-echo delay (`3–10 ms` band; reflector pinned at $r_{sat} = 7\,r_g$, no log-divergent tunable position; derived in [`research/2026-06-17_bh-shear-echo-forward-prereg.md`](../../../research/2026-06-17_bh-shear-echo-forward-prereg.md)). The contested Abedi+ $\sim 0.29$ s is **NOT** the AVE prediction — it would require a $\sim 480\,r_g$ reflector vs AVE's fixed $7\,r_g$, and is itself widely disputed in the literature. **Falsifier F1b:** a real $0.29$ s echo with **no** $\sim 4$ ms companion ⟹ AVE shear-reflector FALSIFIED. **Caveat F1a:** the $\sim 4$ ms delay overlaps the $\tau \approx 4$ ms ringdown damping time — physically distinct (echo spacing vs QNM decay) but observationally subtle. *(Channel-split mechanism: [`lattice-extreme-bh-rationality.md`](../vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md):75.)*
  - **Superconducting vortex core limits**: the smallest measured cores (cuprates, flat-band SC) at $\sim 1$–$2$ nm are $\sim 2{,}500\times$ larger than $\ell_{node} \approx 3.86 \times 10^{-13}$ m → no condensed-matter phenomenon yet threatens the topological resolution limit. A measurement of a vortex core or coherence length below $\ell_{node}$ instantly falsifies the framework.
- _Specific Non-Claims and Caveats_
  - These are *retrospective* explanations. The framework explains observed anomalies, not predicted them ahead of measurement. Treat as consistency / coverage claims, not zero-parameter forward-prediction matches.
  - The Hubble tension's $H_\infty \approx 69.32$ km/s/Mpc target value is quoted as "derived natively in Chapter 1" — readers must verify the derivation chain in Vol 3 cosmology rather than treat the 69.32 figure as a tuned best-fit.
  - 🔴 **CORRECTED 2026-06-17 (BH shear-reflect walk-back, Rule-12).** The LIGO echo claim is **not** in tension with the EM invariance result — they are different channels: $\Gamma_{EM}=0$ (EM, $Z_{EM}\equiv Z_0$, light transparent) AND $\Gamma_{shear}=\Gamma_{bulk}=-1$ (shear/bulk, $Z_{shear}\to0$, GW reflect). See the corrected clm-kezk9z caveat above and the cross-cutting Symmetric vs Asymmetric Saturation entry. <s>The LIGO echo claim is in interpretive tension with the cross-cutting Symmetric-Gravity invariance result ($Z = Z_0$ everywhere, $\Gamma = 0$) — both coexist by distinguishing the constitutive parameters individually collapsing from their ratio being preserved.</s> *(superseded 2026-06-17 — channel-split; preserved per Rule-12.)*
  - The vortex-core limit is a *kill-check* (negative test): no current observation falsifies, but a future sub-$\ell_{node}$ coherence-length measurement does. The leaf does not assert any positive prediction here.
  - The proton-radius muon-orbit Kerr integration is asserted; no in-leaf step-by-step integration showing the 4% gap arises with zero free parameters is presented.

> **Leaf references:** [existing-experimental-signatures](./falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md), [existing-signatures](./falsification/ch11-experimental-bench/existing-signatures.md).

### Quality
- confidence: 0.4
- depends-on:
  - Axiom 1 ($\ell_{node}$ resolution floor for the vortex-core kill-check)
  - Axiom 4 ($\Gamma=-1$ horizon-echo branch)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 1.00)]
- rationale: A catalog of five retrospective explanations (proton-radius Kerr-integration, neutron-lifetime phonon-snap, Hubble crystallization curve, LIGO $\Gamma=-1$ echo, sub-$\ell_{node}$ vortex kill-check). The leaf is honest that these are retrospective consistency/coverage claims, not forward zero-parameter matches. None carries an in-leaf closed derivation — e.g. the 4% proton-radius gap is asserted to arise from Kerr-index integration with no step-by-step integration shown, and the $H_\infty=69.32$ figure is sourced to Vol 3. The vortex-core item is a clean negative kill-check (well-posed). Mostly asserted mechanistic stories with disclosed retrospective status.
- strengthen-by:
  - Supply the in-leaf optical integration showing the 4% muonic-proton-radius gap emerges with zero free parameters.
  - Cross-link the $H_\infty\approx69.32$ km/s/Mpc derivation chain (Vol 3) so the Hubble-tension item is traceable rather than asserted.

---

## Resolving the Horsemen of Falsification (LHC and LIGO Paradoxes)
<!-- id: clm-fh6w3y -->

Standard-model empirical results that *appear* to contradict an LC-network vacuum, resolved within AVE by transmission-line theory.

- _Specific Claims_
  - **LHC paradox** (why doesn't 13.6 TeV proton-proton smashing rupture the vacuum?): the universe's dielectric relaxation time is $\tau_{tick} = \ell_{node}/c \approx 1.28 \times 10^{-21}$ s, but Lorentz-contracted protons cross each other in $\sim 10^{-28}$ s — *seven orders of magnitude faster* than the vacuum can polarize. The vacuum behaves as a perfectly linear, rigid transmission line during the impulse; standard QCD jet formation proceeds unchanged.
  - **LIGO paradox** (why don't gravitational waves get absorbed over 1.3 Gly given the asserted bulk vacuum density?): GW strain amplitudes $h \sim 10^{-21}$ are $\sim 10^{19}\times$ below the impedance-rupture point. Below rupture, the LC network is a perfect lossless line — zero Ohmic loss, infinite propagation distance. Resistive losses *only* turn on near $V_{yield}$.
- _Specific Non-Claims and Caveats_
  - Both paradox resolutions invoke the framework's own non-linearity: linear below rupture, dissipative at and above rupture. This is consistent within AVE but not independently testable here — the LHC and LIGO results are explained by a regime-switch, not by a separately measured loss curve.
  - The $\tau_{tick} \approx 1.28 \times 10^{-21}$ s figure is derived from $\ell_{node}/c$; it is the framework-derived dielectric relaxation time, not measured against an independent dielectric-spectroscopy benchmark.
  - "Standard QCD jet formation proceeds exactly as observed" is a *consistency* claim with the Standard Model in this regime — Vol 4 does not predict QCD outcomes, it asserts that AVE does not contradict them at LHC interaction times.
  - Treat as defensive resolutions of intuitive critiques, not as positive empirical confirmations.

> **Leaf references:** [horsemen-of-falsification](./falsification/ch11-experimental-bench-falsification/horsemen-of-falsification.md), [zero-parameter-derivations](./falsification/ch11-experimental-bench/zero-parameter-derivations.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (linear-below-rupture / dissipative-at-rupture regime switch)
  - Axiom 1 ($\tau_{tick}=\ell_{node}/c\approx1.28\times10^{-21}$ s from lattice pitch)
  - INVARIANT-C1 ($V_{yield}$ rupture point)
  - clm-n3un96 ($\tau_{relax}=\ell_{node}/c$ minimum state-change time bounding the edge)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.80)]
- rationale: Both resolutions are clean order-of-magnitude regime arguments: LHC ($\tau_{tick}\approx1.28\times10^{-21}$ s vs $\sim10^{-28}$ s crossing → vacuum cannot polarize → linear rigid line) and LIGO ($h\sim10^{-21}$ is $\sim10^{19}\times$ below rupture → lossless line). The framework-derived $\tau_{tick}$ and rupture threshold drive both. The leaf is explicit these are defensive consistency claims (regime-switch explanations, not separately-measured loss curves), not positive empirical confirmations. Closed regime arguments resting on disclosed framework-derived constants.
- strengthen-by:
  - Replace the regime-switch assertion with a derived loss curve $\eta(V/V_{yield})$ so the linear-below / dissipative-above transition is quantitative rather than a binary switch.

---

## Tabletop Null Results: VFDT and RVR Scalar Gap (Why Intuitive Tests Fail)
<!-- id: clm-baoa36 -->

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

> **Leaf references:** [tabletop-graveyard](./falsification/ch11-experimental-bench-falsification/tabletop-graveyard.md), [tabletop-null-results](./falsification/ch11-experimental-bench/tabletop-null-results.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 2 ($p_{vac}=\Phi\,\xi_{topo}$ flux-momentum mapping)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: Both null-result calculations are clean algebra: VFDT ($p_{vac}=\Phi\xi_{topo}\approx1.30\times10^{-8}$ kg·m/s ÷ $M_{vac}\approx97{,}450$ kg → $v_{vac}\approx1.33\times10^{-13}$ m/s → $\sim10^{-14}$ rad, undetectable) and RVR ($\delta_L\approx7.4\times10^{-26}$ → $Q\ge2.7\times10^{25}$ vs SOTA $\sim10^{11}$, 15-orders short). The required-null framing is logically sound (a positive signal would falsify $\rho_{bulk}$). The leaf discloses these are consistency checks using the same framework-derived $\rho_{bulk}$, $G/c^2$ couplings — not independent corroboration. Closed null-derivations resting on disclosed imported constants.
- strengthen-by:
  - Ground $\rho_{bulk}\approx7.91\times10^6$ kg/m³ independently so the VFDT/RVR null thresholds are not circular with the constants they test.

---

## Applied Telemetry: Boundary Layer, Schwinger Redline, Sonoluminescence FOC Isomorphism
<!-- id: clm-p12mem -->

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

> **Leaf references:** [applied-telemetry](./falsification/ch11-experimental-bench-falsification/applied-telemetry.md), [industrial-scaleup](./falsification/ch11-experimental-bench/industrial-scaleup.md).

### Quality
- confidence: 0.4
- depends-on:
  - Axiom 4 ($C_{eff}\to\infty$ near yield; $V_{yield}=43.65$ kV)
  - clm-vjv4zf (the $C_{eff}(V)$ strain-gauge readout)
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.90)]
- rationale: Three loosely-coupled telemetry concepts. The dielectric-strain-gauge ($C_{eff}\to\infty$ throttle) and Schwinger-redline (gamma-scintillation abort) are engineering proposals with no built suite. The SBSL FOC isomorphism is the most concrete but its 67.68 kV / 1 Å focal-pressure figure is a K4-TLM solver self-consistency output (Axiom-4 threshold crossing), explicitly NOT an empirical match to measured SBSL spectroscopy, and the leaf mixes 43.65 kV and 511 kV without flagging the regime distinction (the caveat notes this). Asserted proposals + a self-consistency simulation output.
- strengthen-by:
  - Produce a quantitative SBSL spectrum/temperature prediction from the K4-TLM envelope comparable against measured single-bubble sonoluminescence data.

---

## One-Parameter EFT Falsifiability Doctrine
<!-- id: clm-om0rtq -->

The framework-level epistemological claim binding the kill-switch leaves: AVE is constructed as a one-parameter Effective Field Theory deliberately optimized for vulnerability to falsification.

- _Specific Claims_
  - All masses, forces, and cosmological constants are algebraically interlocked and geometrically derived from a single fundamental calibration limit ($\ell_{node}$, equivalently the Planck-node calibration in the Vol 4 framing).
  - Because of this one-parameter coupling, altering or tuning any single output instantly breaks the entire mathematical framework. There is no degree of freedom available for back-fitting after a falsifying observation.
  - This vulnerability is presented as a positive epistemic property — explicitly contrasted with parameterized BSM frameworks (String Theory, Supersymmetry, etc.) that can absorb falsifying observations by retreating into unobservable energy regimes.
  - Operationalizes as an entry-criterion for the binary kill-switches (Neutrino Parity, GRB Dispersion, Birefringence ~~$E^4$~~ **COEFFICIENT** — Rule-12 correction 2026-06-04, commit `ad26d357`: the birefringence discriminator is the field-independent COEFFICIENT ($\sim 10^6\times$ QED, clm-pp3qwf), NOT the $E^4$-vs-$E^2$ field-exponent, which was a retracted $\sqrt{\varepsilon}$-conflation false-falsifier; both AVE and QED are $E^2$-leading): each is asserted to be sufficient on its own to falsify the entire chain.
- _Specific Non-Claims and Caveats_
  - The "one-parameter EFT" claim is framework-internal. It asserts that the algebraic chain has no slack; it does not by itself prove the chain is correct, only that it is not adjustable.
  - "All masses, forces, and cosmological constants" is a strong claim. Volume-spanning derivations exist for many quantities (electron mass, alpha, baryon ladder, $H_\infty$); a complete enumeration with chain-of-derivation pointers is not in any single Vol 4 leaf — readers should treat this as a directional claim and verify per-quantity.
  - The contrast with BSM "moving goalposts" is rhetorical — it is a meta-claim about scientific practice, not a derived result.
  - The doctrine is *meta* — it tells you how to read other leaves' falsification statements; it is not itself a hardware test.

> **Leaf references:** [epistemology-of-falsification](./falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md), [epistemology-kill-switches](./falsification/ch11-experimental-bench/epistemology-kill-switches.md), [epistemology-ch12](./falsification/ch12-falsifiable-predictions/epistemology-ch12.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 1 (single $\ell_{node}$ calibration from which the chain hangs)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 1.00)]
- rationale: A framework-internal meta-claim that AVE is a one-parameter EFT with no back-fitting slack. It is honest about its own status (the doctrine asserts the chain is not adjustable, not that it is correct; the BSM "moving-goalposts" contrast is explicitly rhetorical). But the load-bearing assertion "all masses, forces, and cosmological constants are algebraically interlocked from $\ell_{node}$" is acknowledged in-leaf to lack a complete per-quantity enumeration in any single leaf (directional, verify-per-quantity). A self-aware meta-doctrine with an open completeness gap.
- strengthen-by:
  - Provide the explicit chain-of-derivation map from $\ell_{node}$ to each major output (electron mass, $\alpha$, baryon ladder, $H_\infty$) so the "no slack" claim is enumerated rather than directional.

---

## Helicity Injection: Polarization Matching to the Chiral LC Network
<!-- id: clm-i02mhk -->

To couple maximally to the chiral vacuum substrate, an EM emitter must carry non-zero kinetic helicity $\int \mathbf{A} \cdot \mathbf{B}\,dV \neq 0$ — equivalent to wiring the emitter as a $(p,q)$ Hopf / torus knot rather than a flat toroid.

- _Specific Claims_
  - A standard toroidal inductor produces orthogonal $\mathbf{A}$ and $\mathbf{B}$ ($\int \mathbf{A} \cdot \mathbf{B}\,dV = 0$) and is therefore polarization-mismatched to the chiral vacuum.
  - A Hopf-configured (torus-knot) winding forces $\mathbf{A} \parallel \mathbf{B}$, injecting kinetic helicity into the lattice and meshing with the structural microrotation of the substrate.
  - This acts as a *topological power factor corrector*: it maximizes geometric power transfer to the metric, reducing reactive return loss.
- _Specific Non-Claims and Caveats_
  - "Maximizes geometric power transfer" is asserted as a structural consequence of helicity matching; the leaf does not present a quantitative comparison of toroid-vs-Hopf coupling efficiency at a specific drive frequency.
  - This is the polarization-matching companion claim to the HOPF-01 chiral antenna prediction (see the clm-wzezvt entry's $\Delta f/f = \alpha\,pq/(p+q)$ formula). Helicity injection is the *why* — the qualitative reason the chiral coupling exists; HOPF-01 is the *what* — the specific zero-parameter resonance shift the matched coupling produces.
  - Does NOT independently constitute a falsifiable signal: helicity-mismatched coupling is a known result in classical plasma physics. The novel claim is that the *vacuum itself* has the chiral structure that demands matched helicity — testable only through HOPF-01-style topological-resonance experiments.

> **Leaf references:** [helicity-injection](./falsification/ch12-falsifiable-predictions/helicity-injection.md).

### Quality
- confidence: 0.5
- depends-on:
  - Axiom 1 (chiral Cosserat microrotation of the substrate)
  - clm-wzezvt (HOPF-01 chiral-antenna companion prediction)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.60)]
- rationale: The polarization-matching argument is qualitatively sound: a flat toroid has $\int\mathbf{A}\cdot\mathbf{B}\,dV=0$ (mismatched), while a Hopf $(p,q)$ winding forces $\mathbf{A}\parallel\mathbf{B}\neq0$ (matched to the chiral lattice microrotation). But "maximizes geometric power transfer / reduces reactive return loss" is asserted with no quantitative toroid-vs-Hopf coupling-efficiency comparison, and the leaf concedes this is the qualitative "why" companion to HOPF-01, not an independent falsifiable signal (helicity-mismatch is a known plasma-physics result). Sketch with structural support, no closed efficiency derivation.
- strengthen-by:
  - Compute the toroid-vs-Hopf coupling efficiency at a specified drive frequency so "maximizes power transfer" becomes a quantitative claim.

---

## Active Sagnac Material-Dependent Entrainment Law
<!-- id: clm-qx9bb8 -->

The Sagnac shift in AVE depends on the rotor's *physical* properties (mass density, magnetic permeability, ambient field, altitude, latitude) — directly contradicting the GR claim that Sagnac depends only on enclosed area and angular velocity.

- _Specific Claims_
  - **Five-axis dependence**: the metric drag scales with rotor mass density $\rho_m$, magnetic permeability $\mu_r$, background EMI $B$, altitude (lower gravity → lower ambient strain → reduced coupling), and latitude (Earth's Lense-Thirring drag couples through alignment).
  - **Falsification protocol** (RE-SCOPED to self-consistency check 2026-06-03): identical fiber-loop units at the same RPM with Aerogel vs Lead rotors, and Aluminum vs Mu-Metal rotors. A density- and permeability-independent shift would falsify the AVE *scaling law*. **But this is no longer a forward AVE-vs-GR kill-switch** (`AVE-PONDER/research/2026-06-03_sagnac-rlve-fog-question-verdict.md`): the same $\kappa = \rho_{rotor}/\rho_{bulk}$ applied to Earth-as-rotor predicts a $+7\times10^{-4}$ rotation-rate bias already excluded by ring-laser-gyro Earth-rotation geodesy by $7\times10^4\times$, so A2-SAGNAC retired to corroborative-null. The material-pair scaling test survives as a **self-consistency** check (does the AVE signal scale linearly with rotor density), not a forward discriminator. ⚠ The "GR area-only Sagnac, density-independent" counterfactual is in tension with the verdict (PONDER PR #1 `eb7a49b` finds GR frame-drag scales with $I \propto \rho$ too) — flagged for Grant/auditor adjudication.
  - **Aerospace-navigation derivatives**: differential Sagnac arrays subtract the shared common-mode rotation, isolating the inductive-drag scalar — a "metric slip-velocity indicator" — alongside other proposed derivatives (3D metric gradient compass, dark-wake sensor, chiral torsion sensor) that the leaves describe as extracted to companion IP volumes.
- _Specific Non-Claims and Caveats_
  - This is the same material-dependent entrainment law that produces the Sagnac-RLVE 2.07 rad prediction (the Sagnac-RLVE experiment `exp-rth12t`, which `strengthens` this claim) — but stated as a general law rather than a specific apparatus. Treat as the parametric-law statement; `exp-rth12t` is the specific worked-example apparatus.
  - Has NOT been performed; the material-pair falsification (Aerogel/Lead, Al/Mu-Metal) is the framework's own design, not a measured result.
  - Three of the four telemetry derivatives (gradient compass, dark wake, chiral torsion) are explicitly noted as "extracted to companion IP volumes" — i.e., not present in the open KB. Cite this leaf only for the entrainment law itself and the slip-velocity-indicator architecture.
  - SNR / hardware tolerance numbers (Zerodur cavity, $<1$ mK thermal stability, $<46$ kHz linewidth, sub-pm seismic) are quoted in the index for this leaf but the body of this leaf marks them "extracted to companion IP volumes."

> **Leaf references:** [active-sagnac-impedance-drag](./falsification/ch12-falsifiable-predictions/active-sagnac-impedance-drag.md), [active-sagnac-telemetry](./falsification/ch12-falsifiable-predictions/active-sagnac-telemetry.md).

### Quality
- confidence: 0.6
- depends-on:
  - Axiom 1 (mass-density-coupled mutual inductance / metric drag)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 1.00)]
- rationale: The five-axis material-dependent entrainment law ($\rho_m$, $\mu_r$, $B$, altitude, latitude) is clearly stated with a sharp material-pair falsifier (Aerogel/Lead, Al/Mu-Metal: density/material-independent shift kills the AVE scaling law). **Walk-back 2026-06-03 (`AVE-PONDER/research/2026-06-03_sagnac-rlve-fog-question-verdict.md`):** the parent A2-SAGNAC experiment retired forward "kill-switch" → corroborative-null, because the same $\kappa$ applied to Earth-as-rotor predicts a $+7\times10^{-4}$ rotation-rate bias already excluded by ring-laser-gyro geodesy. The material-pair test survives as a **self-consistency** scaling check, not a forward AVE-vs-GR discriminator — and the "directly contradicting the GR area-only Sagnac claim, a genuine discriminator" assertion is now in tension with the verdict (PONDER PR #1 `eb7a49b`: GR frame-drag scales with $I \propto \rho$ too, so both predict $\Psi = \rho_W/\rho_{Al}$); flagged for adjudication, NOT silently resolved. This leaf is the parametric-law statement; the quantitative worked example (2.07 rad) lives in the Sagnac-RLVE experiment, and the SNR/tolerance specifics + three of four telemetry derivatives are explicitly "extracted to companion IP volumes" (not present in the open KB). A well-posed parametric law with the quantitative apparatus and SNR offloaded.
- strengthen-by:
  - Derive the functional form of the five-axis dependence (currently a list of monotonic directions) so the law makes a quantitative shift-vs-$\rho_m$ prediction testable by the material-pair experiment.

---

## TVS Phase Transition: Solid → Slipstream ($\eta_{eff}(V)$ Step)
<!-- id: clm-o2shcn -->

Mutual inductance yields above a structural shear threshold $\tau_{yield}$, mapping the vacuum onto a Transient Voltage Suppression Zener Diode: rigid drag $\eta_0$ below $V_{yield}$, frictionless flow ($\eta = 0$) above.

- _Specific Claims_
  - The constitutive step-function $\eta_{eff}(V) = \eta_0$ for $V < V_{yield}$, $\eta_{eff}(V) = 0$ for $V \geq V_{yield}$ — the "Zero-Impedance Slipstream" regime above yield.
  - Yield-stress evaluation: $\tau_{yield} = \rho_{bulk}\,c^2 \times \mathcal{V}_{total} \times \alpha \approx 1.04 \times 10^{22}$ Pa, where $\mathcal{V}_{total} = 2.0$ is the **dual-reactance count** ($X_C + X_L$ reactance sectors, Axiom 1; counted, not integrated — see `common/dual-reactance-storage-taxonomy.md`) and $p_c/(8\pi) = \alpha$ is the lattice porosity. (The $6 \times \mathcal{V}_{crossing}$ writing, with $\mathcal{V}_{crossing} \equiv V_{toroidal}/6$, is a circular re-factoring of the same $\mathcal{V}_{total} = 2.0$ — a vestige of the retired geometric halo-volume framing, not an independent geometric derivation of the value.)
  - Identifies the underlying mechanism for the $V_{yield}$-crossing impedance rupture used by the autoresonant PLL (clm-9sujp8), the ZENER-04 avalanche detector (clm-cltls0), and the asymmetric flyback in TORSION-05 (clm-kl1ern).
- _Specific Non-Claims and Caveats_
  - The step function is *idealized*. In any physical realization the transition is not literally discontinuous — finite-rise-time effects, non-uniform field distributions, and any finite quality factor smear the step. The leaf does not specify the transition width.
  - The $\tau_{yield} \approx 1.04 \times 10^{22}$ Pa figure is framework-derived; it inherits the same $\rho_{bulk}$ and $p_c$ values used elsewhere in Vol 4 (see also the Sagnac-RLVE experiment `exp-rth12t`, which uses the same framework-derived $\rho_{bulk}$).
  - "Frictionless flow" above yield is the inductive-drag-only statement; it does not assert that all dissipation channels vanish — it specifically identifies the mutual-inductance damping channel as the one that yields.
  - The TVS-Zener analogy is structural; this leaf does not present an empirical match to any specific Zener device's $\eta(V)$ characteristic.

> **Leaf references:** [tvs-transition](./circuit-theory/ch1-vacuum-circuit-analysis/tvs-transition.md).

> **🔴 $X_L$ = the FLYWHEEL (spin/frequency-regulation) sector, NOT the rest-mass store (2026-06-20, Rule 12 — the rationale's "magnetic→$X_L$→rest mass (clm-lv3uw1)" gloss below PRESERVED unedited; Grant-CONFIRMED mass-sector ruling; SYNCS this entry to the PR#260 banner at `common/dual-reactance-storage-taxonomy.md:189`).** Where the rationale glosses the **magnetic** saturation branch ($\mu_{eff}\to0$) inductive sector "$X_L$" as **rest mass**, the **$X_L$ = the inductive FLYWHEEL = the T2 / Cosserat micro-rotation ($\omega$) spin sector** (the spin/Larmor clock), whose mass-gap is the Compton/Larmor *clock* gap, **NOT** the rest-mass store. The **rest mass is the A1 longitudinal DILATATION** depression (`vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` "A1 dilatation-MASS"). The dual-reactance **COUNT** ($\mathcal{V}_{total}=2.0$, $X_C+X_L$) — the load-bearing factor in $\tau_{yield}$ here — is **UNAFFECTED**; only the "$X_L$ = rest mass" *label* is re-scoped. Consistency-class relabel, body preserved per Rule-12.

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (shear-yield TVS step at $\tau_{yield}$)
  - INVARIANT-C1 ($V_{yield}$ threshold)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: The constitutive step $\eta_{eff}(V)=\eta_0$ below / $0$ above $V_{yield}$ is well-posed, and the yield-stress numeral $\tau_{yield}=\rho_{bulk}c^2\mathcal{V}_{total}\,\alpha\approx1.04\times10^{22}$ Pa closes arithmetically. But it imports several framework-derived inputs — $\rho_{bulk}$, the dual-reactance count $\mathcal{V}_{total}=2.0$ ($X_C + X_L$ reactance sectors, Axiom 1; counted, not integrated; NOT a FEM-integrated volume — the prior "FEM-verified halo volume" provenance was fabricated and is dropped, see `common/dual-reactance-storage-taxonomy.md`), and the porosity identity $p_c/(8\pi)=\alpha$ — and the leaf discloses the step is idealized (transition width unspecified). A clean constitutive derivation gated by clearly-disclosed imports. (Structural item RESOLVED — STAYS-INHERITED, Grant 2026-06-02: the yield event is the electric (ε-only) single-sector branch (`common/dual-reactance-storage-taxonomy.md` §τ_yield; `master-equation.md:78`), so the ×2 is the **inherited** $\mathcal{V}_{total}$ count-tag — a tag for which Axiom-4 branch this is — NOT an $E_C + E_L$ within-event sum the yield derives. The count-2 manifests at the yield scale as the two mutually-exclusive saturation branches: electric→$X_C$→$\tau_{yield}$ vs magnetic→$X_L$→rest mass (clm-lv3uw1), the same $X_C + X_L$ count as baryon $\mathcal{V} = 2$. Class B axiom-manifestation; no empirical discriminator; provenance/structural identification only — does NOT lift confidence. See `research/2026-06-02_tau-yield-reactance-count.md` §7.)
- strengthen-by:
  - Specify the finite transition width (from $\tau_{relax}$ / finite rise-time) so the step is a physical profile rather than a discontinuity.
  - Derive $\mathcal{V}_{total}=2.0$ and $p_c/(8\pi)=\alpha$ from lattice primitives inline.

---

## Sagnac Inductive Drag SPICE Reproduction (Directional $L_{eff}$ on a 50-Node LC Ring)
<!-- id: clm-cbwd77 -->

A SPICE simulation that reproduces the Sagnac arrival-time shift from a discrete LC ring with a directional inductance $L_{eff} = L_0 (1 \pm S_{DRAG})$, demonstrating the effect arises from Faraday-style induction in a rotating-frame LC network — no Lorentz transformations required.

- _Specific Claims_
  - The macroscopic Sagnac phase shift is reproduced by a 50-node closed LC ring in which the per-segment inductance is direction-sensitive: photons traveling with the macroscopic phase-drag see $L_0(1 - \delta)$ (faster than $c_0$ locally); counter-traveling photons see $L_0(1 + \delta)$ (slower than $c_0$ locally).
  - Implementation uses standard behavioral-current-source SPICE primitives (`sdt(...)`, conditional `IF(I > 0, ...)` syntax over a 0-V current sense), without any tensor or relativistic kinematics in the simulator.
  - Resultant interpretive claim: deriving the Sagnac effect requires only the macroscopic equivalent of Faraday's Law of Induction operating across the spacetime metric — Lorentz transformations and Einstein's field equations are sufficient but not necessary.
- _Specific Non-Claims and Caveats_
  - The simulation reproduces the *qualitative* Sagnac arrival-time differential. The leaves do not claim the SPICE netlist's specific $L_0$, $C_0$, and $S_{DRAG}$ values quantitatively predict the Sagnac phase of any specific ring-laser gyroscope or fiber loop.
  - "No relativistic tensor math" is a property of the SPICE solver, not a derivation that relativistic tensor math is wrong — the LC-ring model and the standard relativistic derivation produce equivalent observables in the linear regime.
  - This SPICE reproduction is distinct from the Sagnac-RLVE experiment (`exp-rth12t`), which couples to *bulk vacuum* metric drag. The ch.16 simulation models a *rotating-frame fiber* with intrinsic directional induction; both share the Faraday-style mechanism but operate at different couplings.
  - Sub-microsecond transient analysis duration ($2\,\mu$s in the netlist); not a steady-state observability claim.

> **Leaf references:** [spice-netlist](./simulation/ch16-sagnac-inductive-drag/spice-netlist.md), [theory](./simulation/ch16-sagnac-inductive-drag/theory.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 1 (rotating-frame mutual inductance / directional $\mu_{eff}$)
  - clm-i9l284 (LC-ladder propagation underlying the ring)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.90)]
- rationale: The 50-node directional-$L_{eff}=L_0(1\pm\delta)$ LC ring qualitatively reproduces the Sagnac arrival-time differential from Faraday-style induction in a rotating frame, with the framing note correctly distinguishing rotor-local perturbation from a globally co-rotating bulk. The leaf is explicit this is QUALITATIVE — it does not claim the netlist's $L_0,C_0,S_{DRAG}$ values quantitatively predict any specific gyro's phase, and "no relativistic tensor math" is a property of the solver, not a refutation of the relativistic derivation (equivalent observables in the linear regime). Closes as a qualitative mechanism demonstration with that scope disclosed.
- strengthen-by:
  - Calibrate $S_{DRAG}$ from a physical rotor so the ring reproduces a measured ring-laser-gyro phase quantitatively.

---


## Op14 Cross-Sector Trading: K4-Inductive ↔ Cosserat Energy Exchange (ρ = −0.990)
<!-- id: clm-p2tp9i -->

A-012 canonical. Op14 saturation-driven impedance modulation transfers energy between the K4-inductive (Φ_link) and Cosserat substrate sectors via the bond LC tank's inductive side, empirically confirmed at ρ(H_cos, Σ|Φ_link|²) = −0.990 Pearson anti-correlation over the t ∈ [150P, 200P] recording window. H_cos alone is not conserved (5.5% drift over 50 Compton periods) but H_total = H_cos + H_K4-inductive is approximately conserved; the dominant trading frequency is ~0.020 rad/unit. This is the substrate-native mechanism for the co-stable trading state of saturated K4 bond-pairs.

- _Specific Claims_
  - ρ(H_cos, Σ|Φ_link|²) = −0.990 (Pearson, empirical); ρ(Σ|V_inc|², Σ|Φ_link|²) = −0.990; ρ(H_cos, Σ|V_inc|²) = +1.000.
  - H_total = H_cos + H_K4-inductive is approximately conserved (modulo Verlet O(dt²) drift) while H_cos alone drifts ~5.5% over 50 Compton periods.
  - Mechanism: Op14 saturation modulates Z_eff → drives slow Φ_link ↔ Cosserat oscillation at ~0.020 rad/unit; reactive (non-dissipative) trading.
- _Specific Non-Claims and Caveats_
  - The 5.5% H_cos drift is real physics (sector energy exchange), NOT numerical error.
  - Does NOT claim eigenfrequency drift with amplitude (that hypothesis is reported as falsified); does NOT close the Round 7+8 Mode III (2,3) bound-state gap.

> **Leaf references:** [op14-cross-sector-trading](./circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 1 (K4-inductive ↔ Cosserat sector structure)
  - Axiom 4 (Op14 saturation-driven $Z_{eff}$ modulation)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: The central result — $\rho(H_{cos},\Sigma|\Phi_{link}|^2)=-0.990$ anti-correlation with $H_{total}=H_{cos}+H_{K4\text{-}ind}$ approximately conserved — is an empirical engine-measurement over a stated recording window with a clearly-stated reactive-trading mechanism (Op14 $Z_{eff}$ modulation transferring energy via the bond LC tank). The 5.5% $H_{cos}$ drift is interpreted as real sector exchange, not numerical error, and a competing amplitude-eigenfrequency-drift hypothesis is reported falsified. Rests on a simulation measurement (disclosed) rather than a closed analytic derivation, with the (2,3) bound-state gap explicitly left open.
- strengthen-by:
  - Derive the $\sim0.020$ rad/unit trading frequency analytically from the Op14 coupling rather than reading it from the FFT.

---

## Op14 Saturation Modulates Local Clock Rate
<!-- id: clm-1eg13f -->

A-010 canonical. Op14's dynamic impedance Z_eff(r) = Z₀/√S(r) modulates not just impedance but the local clock rate, giving the substrate-native mechanism for time dilation: ω_local(r) = ω_global·√(1 − A²(r)), with τ_local = τ_unstrained/√(1 − A²(r)). This parallels the Vol 3 Ch 3 gravitational refractive-index local-clock effect τ_local = n(r)·τ_unstrained with n(r) = 1/√S. At rupture (A² → 1) the local clock freezes (ω_local → 0) and a Γ = −1 TIR wall forms.

- _Specific Claims_
  - ω_local(r) = ω_global·√(1 − A²(r)); local time dilation τ_local = τ_unstrained/√(1 − A²(r)).
  - Cross-volume parallel to gravitational n(r) = 1/√S; mechanism is reactive (no dissipation), energy redistributed in time.
- _Specific Non-Claims and Caveats_
  - Three regimes must NOT be conflated: uniform slowing (reactive) vs uniform damping (dissipative) vs spatially-varying slowing (mode-decomposition matters).

> **Leaf references:** [op14-local-clock-modulation](./circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md).

### Quality
- confidence: 0.8
- depends-on:
  - Axiom 4 (saturation kernel $S(A)=\sqrt{1-A^2}$; $c_{eff}=c_0\sqrt S$ relation)
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 1.00)]
- rationale: $\omega_{local}=\omega_{global}\sqrt{1-A^2}$ follows cleanly from $c_{eff}=c_0\sqrt{S}$ (wave needs $\tau=\ell/c_{eff}$ to cross a cell), giving $\tau_{local}=\tau_{unstrained}/\sqrt{1-A^2}$; the cross-volume parallel to gravitational $n(r)=1/\sqrt S$ is exact, and the three-regime non-conflation (uniform-slowing reactive vs uniform-damping dissipative vs spatially-varying) is explicit and methodologically careful. A clean derivation from the kernel; pinned just below 0.9 because the $c_{eff}=c_0\sqrt S$ wave-speed step is asserted from the kernel rather than re-derived in-leaf.
- strengthen-by:
  - Derive $c_{eff}=c_0\sqrt{S}$ from the per-cell dispersion relation inline so the clock-rate result is fully self-contained.

---

## Parametric Coupling Kernel (Axiom 4 Vacuum Varactor at Sub-Yield α-Slew Operating Point)
<!-- id: clm-6t3p6x -->

For an N-coherent-site LC apparatus embedded in the bulk substrate with vacuum varactor C_eff(V) = C₀/√(1 − (V/V_yield)²) driven by α-slew refresh at ν_slew = (α/2π)·ω_Compton, the per-electron per-cycle detection probability is ε_det = 4π·κ_quality/N_single², derived from Dicke amplitude distribution (1/N) × matched-cycle synchronization (1/N) × Theorem 3.1′ observable-Compton-cycle radiation-impedance averaging (4π; substrate-mechanism bipartite K4 lobe-count). The capacitance modulation is δC/C₀ = (1/4)(V_pump/V_yield)² ≈ 4.57% at the canonical operating point; parametric resonance occurs at ω_app = ω_slew (sub-harmonic of pump 2ω_slew). This is a REACTIVE-power class mechanism, categorically distinct from the real-power κ_entrain Sagnac-RLVE.

- _Specific Claims_
  - ε_det = 4π·κ_quality/N_single² with κ_quality = 1 for Q·δ_C ≥ 2 (deep-regenerative), (Q·δ_C/2)² sub-regenerative.
  - δC/C₀ = (1/4)(V_pump/V_yield)² ≈ 4.57%; DAMA detection rate 0.6% match derived as consequence; XENONnT null derived from sub-regenerative regime (Q·δ < 2).
  - Cross-detector predictions for COSINE/ANAIS/MAJORANA/KIMS/Sapphire.
- _Specific Non-Claims and Caveats_
  - REACTIVE-power class; NOT the real-power κ_entrain Sagnac-RLVE mechanism.

> **Leaf references:** [parametric-coupling-kernel](./circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md).

### Quality
- confidence: 0.6
- depends-on:
  - Axiom 4 (vacuum varactor $C_{eff}(V)$; Theorem 3.1' $Z_{radiation}=Z_0/4\pi$ inheritance)
  - clm-vjv4zf (constitutive $C_{eff}(V)$ form)
  - clm-rtdmsn (Theorem 3.1' $Z_{radiation}=Z_0/4\pi$ LC-tank Q-factor inherited)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.85)]
- rationale: The kernel $\varepsilon_{det}=4\pi\kappa_{quality}/N^2$ is derived substrate-native (N-parallel-LC voltage-divider for the first $1/N$, substrate-clock phase-bin enumeration for the second, $4\pi$ inherited from observable-Compton-cycle radiation impedance — substrate-mechanism bipartite K4 lobe-count), and $\delta C/C_0=\tfrac14(V_{pump}/V_{yield})^2\approx4.57\%$ is clean algebra with a textbook degenerate-parametric cross-check. But the leaf is candid that $\kappa_{quality}$ per detector and the per-defect detuning $(\Delta\omega/\omega)_{per-defect}\approx0.1$ are load-bearing-open (sub-regenerative envelope "rigorous derivation pending"; per-defect-class sub-derivations open). Closes to leading order with substantive disclosed open dependencies on $\kappa_{quality}$.
- strengthen-by:
  - Derive the per-defect-class $(\Delta\omega/\omega)_{per-defect}$ from first principles so $\kappa_{quality}(\rho_{def})$ is fully parameter-free.
  - Give the rigorous (not dimensional-analysis) form of the sub-regenerative $\kappa_{quality}=(Q\delta_C/2)^2$ envelope.

---

## Q-G22 Strain Convention: Topological-Geometric vs Coulomb-Field Ratio
<!-- id: clm-4r4jiy -->

Clarification leaf documenting the canonical strain-measure convention. The corpus uses two distinct, both-valid strain measures: the topological geometric confinement ratio A_geom(r) = ℓ_node/r (∝ 1/r) and the Coulomb field ratio A_field(r) = E·ℓ_node/V_yield (∝ 1/r²). Kernel applications (C_eff, S(A), V/V_snap, Q-G19α Petermann) use A_geom; the IVIM apparatus bench uses A_field. Both conventions yield internally consistent predictions; the apparent "four-way conflict" in A(r) definitions across chapters dissolves once the convention split is recognized.

- _Specific Claims_
  - Canonical kernel-application strain is A_geom = ℓ_node/r (geometric confinement ratio), NOT the literal Coulomb potential ratio.
  - IVIM bench uses A_field = E·ℓ_node/V_yield; both conventions are internally consistent.
- _Specific Non-Claims and Caveats_
  - Explicitly "not a new physics result" — a convention-documentation leaf.
  - Partial closure only: WHY topological strain equals ℓ_node/r rather than α·ℓ_node/r from first principles is an open multi-week analytical item.

> **Leaf references:** [q-g22-strain-convention](./circuit-theory/ch1-vacuum-circuit-analysis/q-g22-strain-convention.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 4 (kernel-application strain measure)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: A convention-documentation leaf, not a physics result (explicitly stated). It cleanly resolves the apparent "four-way conflict" by distinguishing the geometric confinement ratio $A_{geom}=\ell_{node}/r$ ($\propto1/r$, used in all kernel applications) from the Coulomb field ratio $A_{field}=E\ell_{node}/V_{yield}$ ($\propto1/r^2$, used in the IVIM bench), with multiple corpus anchor-line citations. The distinction is internally consistent and well-supported; the leaf openly flags the open piece — WHY topological strain $=\ell_{node}/r$ rather than $\alpha\ell_{node}/r$ from first principles (a multi-week item). Disclosed partial closure.
- strengthen-by:
  - Derive from first principles why the kernel strain is $\ell_{node}/r$ (not $\alpha\ell_{node}/r$) via the $V_{yield}$ scale-cascade, closing the acknowledged open piece.

---

## Q-G24 Newtonian-Limit Closure via Relativistic Inductor
<!-- id: clm-fgo20a -->

The Lorentz-invariant kinetic energy E = γm₀c² emerges structurally from the substrate's electron-as-bond-pair LC tank — not from a scalar Lagrangian and not subject to Derrick's theorem barriers. The closure proceeds via the Relativistic Inductor framework + Virial theorem + three independent Derrick-bypass mechanisms (lattice floor / Faddeev-Skyrme / bilateral chiral), with no fit parameters. The apparent "load-bearing gap" was an artifact of using a scalar Lagrangian when the corpus already carried the correct vector-Maxwell form (Vol 4 Ch 1 lines 175–184).

- _Specific Claims_
  - E = γm₀c² emerges from LC tank + virial equipartition + relativistic-inductor mapping with zero fit parameters.
  - Three independent Derrick-bypass mechanisms (lattice floor / Faddeev-Skyrme / bilateral chiral).
- _Specific Non-Claims and Caveats_
  - Does NOT derive from a scalar field Lagrangian; the "gap" was a framing artifact dissolved by corpus-grep.

> **Leaf references:** [relativistic-inductor-newtonian-limit](./circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 1 (lattice floor / Cosserat dual-axis structure)
  - Axiom 2 ($L=\xi_{topo}^{-2}m$ inductance-mass mapping)
  - clm-p5cf3t (Relativistic Inductor $L_{eff}(I)$ framework)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.85)]
- rationale: $E=\gamma m_0c^2$ (and the full $E^2=(m_0c^2)^2+(pc)^2$) is reconstructed structurally from the LC-tank virial equipartition + relativistic-inductor mapping with no fit parameters, and the leaf is honest that the prior "Derrick-theorem gap" was a framing artifact dissolved by corpus-grep. The three Derrick-bypass mechanisms are clearly stated but two of them (Faddeev-Skyrme Op10 term, bilateral chiral Cosserat structure) are imported from Vol 2 / Axiom 1 rather than re-derived here, and Step 3's "virial preserves capacitive balance under boost" is asserted. Closes structurally on disclosed imports.
- strengthen-by:
  - Show explicitly that virial equipartition survives the Lorentz boost (Step 3 currently asserts the capacitive balance adjusts to maintain $E_{total}=\gamma m_0c^2$).

---

## τ_relax = ℓ_node/c: Minimum State-Change Time from K4 Lagrangian
<!-- id: clm-n3un96 -->

Axiom-first derivation of the substrate's thixotropic relaxation time from the per-cell K4 Lagrangian + causal propagation: the per-cell saturation kernel S(A) relaxes toward equilibrium S_eq(r) = √(1 − r²) via a first-order ODE with time constant τ_relax = ℓ_node/c ≈ 1.288 × 10⁻²¹ s, and no faster relaxation mode is axiom-permitted. The substrate is therefore memristive (path-dependent), not purely algebraic. This is the load-bearing timescale for Op14 dynamics and predicts BEMF-driven defect freezing (AVE-native Kibble-Zurek) with a linear cooling-rate scaling (NOT a K-Z power law).

- _Specific Claims_
  - τ_relax = ℓ_node/c ≈ 1.288 × 10⁻²¹ s; no faster relaxation mode axiom-permitted.
  - Dynamic S(t) memristive relaxation ODE; substrate is path-dependent.
  - Prediction: linear cooling-rate scaling for defect freezing (distinct from K-Z power-law).
- _Specific Non-Claims and Caveats_
  - Distinguishes its linear-scaling prediction explicitly from the Kibble-Zurek power-law.

> **Leaf references:** [tau-relax-derivation](./circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md).

### Quality
- confidence: 0.8
- depends-on:
  - Axiom 1 (K4 LC lattice, $\ell_{node}$ pitch)
  - Axiom 3 ($c$ as universal propagation limit)
  - Axiom 4 (saturation kernel relaxing toward $S_{eq}$)
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 1.00)]
- rationale: $\tau_{relax}=\ell_{node}/c\approx1.288\times10^{-21}$ s is derived axiom-first from the per-cell K4 Lagrangian (lattice wave speed $=c$) plus the nearest-neighbor bond-length / causal-propagation argument, with a clean no-faster-mode proof (supraluminal violates Axiom 3, sub-lattice coherence violates Axiom 1). The memristive first-order ODE and the hysteresis-loop / linear-(not-Kibble-Zurek)-cooling prediction are well-posed and clearly distinguished. Pinned just below 0.9 because the continuum-limit Euler-Lagrange step to the wave equation is stated rather than carried out in detail.
- strengthen-by:
  - Carry out the continuum-limit Euler-Lagrange derivation explicitly rather than citing Vol 4 Ch 1:60-125.

---

## Theorem 3.1′ — Electron Q-Factor from LC Tank at TIR Boundary
<!-- id: clm-rtdmsn -->

The electron's fine-structure constant α⁻¹ ≈ 137.036 is the dimensionless Q-factor of its LC tank at the topological-defect Total-Internal-Reflection boundary, decomposing into three orthogonal reactance contributions: α⁻¹ = Q_tank = Q_vol + Q_surf + Q_line = 4π³ + π² + π ≈ 124.025 + 9.870 + 3.142 = 137.036, matching the M, Q, J boundary-observability structure. Two independent derivation paths (LC-tank Vol 4 Ch 1 + multipole Vol 1 Ch 8) agree to within δ_strain = 2.225 × 10⁻⁶ (CMB thermal running). Supersedes the empirically-falsified Neumann-integral framing.

- _Specific Claims_
  - α⁻¹ = Q_vol + Q_surf + Q_line = 4π³ + π² + π = 137.036.
  - Two independent paths (LC-tank + multipole) agree to δ_strain = 2.225 × 10⁻⁶.
- _Specific Non-Claims and Caveats_
  - Supersedes the Neumann-integral framing (doc 14), which is reported empirically falsified (classical Neumann integral for (2,3) at Golden Torus does not reproduce π² or 137).
  - 🔴 **Value-scoped (2026-06-15, keystone α-verdict, auditor-gated 2026-06-14 — propagating the ruling its own anchor leaf [theorem-3-1-q-factor](./circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) already carries at line 19):** this is the **Q-factor reframe** of α⁻¹, **not** a first-principles derivation of the number 137. α is one of the 3 *retained inputs*, not a derived output. α⁻¹ = 4π³+π²+π is a **Class-B named geometric identification** whose *scale* (∼1/137) is forced by the Compton-resonance trapping condition, but whose *exact value* rests on the single identification R·r = 1/4 — shared across the (2,q) bound-resonator ladder, not electron-specific — which **the substrate does not independently select** (both named lift-routes closed). The LC-tank path obtains Q_tank = 1/α *using* α = e²Z₀/(4πℏ), a **definitional identity** that predicts no independent value; the "two paths agree to δ_strain" residual is a definitional back-substitution, **not** a value-derivation (Q-DELTA-MAP-1-quant closed NEGATIVE). Value-scoped synonym: **"echo at the value level," recorded beneath the canonical Class-B label** and never as a bare standalone "echo." Canonical scope: `vol1/ch8-alpha-golden-torus.md:11`.

> **Leaf references:** [theorem-3-1-q-factor](./circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md).

### Quality
- confidence: 0.85
- depends-on:
  - Axiom 1 ($\ell_{node}$, Nyquist cutoff, Golden Torus geometry)
  - Axiom 2 ($\xi_{topo}$, $L_e=\xi_{topo}^{-2}m_e$)
  - Axiom 3 (TIR $\Gamma=-1$ confinement, per-cycle leak $=\alpha$)
- solidity: 0.85 (ok to build on) [= min(0.85, 1.00)]
- rationale: Two independent derivations of $\alpha^{-1}=Q_{tank}=4\pi^3+\pi^2+\pi=137.036$ — the LC-tank path ($Q=\omega_C L_e/R=(Z_0/4\pi\alpha)/(Z_0/4\pi)=1/\alpha$, clean algebra) and the multipole geometric-sum path — agree to $\delta_{strain}=2.225\times10^{-6}$, identified as the CMB thermal running (a numerical-verification script is cited). The $Q_i = \Lambda_i$ identification at §"The bridge: $\Lambda$'s ARE the tank reactances" (line 67) was originally disclosed as a natural-unit convention; **2026-05-27 Phase 3-A4 (AMENDED 2026-05-27 post-PR-#47-auditor — PARTIAL closure)** formalizes it at canonical-leaf rigor under the **substrate-orthogonal-channel framing** at the new canonical leaf [`op21-multi-mode-mode-counting.md`](./circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md): each $\Lambda_k$ INDEPENDENTLY constrained by its own substrate-axiom source ($\Lambda_{\text{line}}$ by Ax 1 Nyquist + Ax 2 (b)-diameter convention; $\Lambda_{\text{surf}}$ by Ax 3 spatial half-cover via K4 rotation-group chain; $\Lambda_{\text{vol}}$ by Ax 3 + same K4 chain expressed temporally), with cross-term-freeness as a *consequence* of Nyquist-cell-category mutual exclusivity at the $\Gamma = -1$ saturation boundary (NOT a separate additivity postulate). This replaces the prior natural-unit-convention shortcut with explicit per-channel substrate-axiom constraint structure at **Class B substrate-mechanism manifestation** rigor. The substrate-foundational form $Q = \ell$ at $\Gamma = -1$ is cross-scale canonical (single-channel wavelength-counting at BH ringdown / QNM / knot-mode isomorphism / universal substrate-Q derivation; substrate-orthogonal-channel mode-counting at the electron LC tank multi-codim assembly). **Full Class 2 axiom-manifestation closure of $Q_i = \Lambda_i$ remains open**: the Clifford-torus codimensional embedding is treated as canonical input from upstream leaves rather than re-derived from K4 substrate primitives; the strengthen-by item below is partially closed (formalization-rigor lift at Class B; Class 2 closure requires the further K4-substrate-primitive derivation of the embedding). Supersedes the empirically-falsified Neumann framing. Two-path-agreeing closed derivation with $Q_i = \Lambda_i$ now formalized at substrate-orthogonal-channel rigor (Class B substrate-mechanism manifestation; NOT Class 2 axiom-manifestation).
- strengthen-by:
  - **(PARTIAL closure — amendment-revised 2026-05-27 post-PR-#47-auditor)** Derive the $Q_i = \Lambda_i$ identification (geometric volume → reactance) from the substrate impedance scaling rather than asserting it as a natural-unit convention. *Partial closure status*: Phase 3-A4 amendment delivers the substrate-orthogonal-channel constraint structure at canonical-leaf rigor (each Λ_k INDEPENDENTLY constrained by its own substrate-axiom source; cross-term-freeness from Nyquist-cell-category mutual exclusivity) — a real formalization-rigor lift at Class B substrate-mechanism manifestation. Full closure (Class 2 axiom-manifestation) requires K4-substrate-primitive derivation of the Clifford-torus codimensional embedding itself, which Phase 3-A4 does not deliver. See [`op21-multi-mode-mode-counting.md`](./circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) §7 for the honest classification + the open Class 2 path; see clm-0ktpcn entry strengthen-by list for the corresponding substrate-mechanism workstream candidate.

---

## A-034 Measurement Hierarchy: Single-Emitter / Bulk / Phased-Array PLL SNR Scaling
<!-- id: clm-gv1wu4 -->

A-034 measurement-hierarchy framing for engineered-substrate kernel measurements. The same universal kernel S(A) = √(1 − A²) is accessed by three bench architectures with distinct SNR characteristics: single-emitter (SNR ∝ V, clean geometry), bulk-response (multi-emitter, SNR ∝ √N·V), and phased-array PLL (autoresonant, SNR ∝ exp(N·log Q) near rupture). This explains why most operational AVE benches use many emitters: bulk-response is the natural-SNR regime for kernel measurement, while single-emitter benches measure the same kernel at lower SNR with cleaner geometry.

- _Specific Claims_
  - Three architectures access the same A-034 kernel with SNR scalings ∝ V (single), ∝ √N·V (bulk), ∝ exp(N·log Q) near rupture (phased-array PLL).
- _Specific Non-Claims and Caveats_
  - A framing/hierarchy claim — does not assert a new kernel, only the SNR-scaling regimes for measuring the existing one.

> **Leaf references:** [measurement-hierarchy-snr](./falsification/ch11-experimental-bench/measurement-hierarchy-snr.md).

### Quality
- confidence: 0.6
- depends-on:
  - Axiom 4 (universal kernel $S(A)=\sqrt{1-A^2}$ accessed by all three architectures)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 1.00)]
- rationale: A framing/hierarchy claim (explicitly "does not assert a new kernel"). The single-emitter ($\propto V$) and bulk-response ($\propto\sqrt N\,V$ Gaussian-averaging) SNR scalings are standard, well-grounded EE results. The phased-array PLL $\propto\exp(N\log Q)$-near-rupture form is asserted as autoresonant amplification but not derived in-leaf (no model producing the exponential). The cross-scale unification table is illustrative. A sound organizing framework whose third (exponential) scaling is asserted rather than shown.
- strengthen-by:
  - Derive the phased-array-PLL $\propto\exp(N\log Q)$ near-rupture SNR scaling from the autoresonant Duffing lock dynamics.

---

## Electron Field-Component Bundle (R/X/Q/L/C) as SubstrateExcitation instance-1
<!-- id: clm-fd1e7a -->

The electron's EE field components — a real (resistive/radiative) part $R$ and a reactive part $jX$ — together with its instance values $Q_e = 1/\alpha$, $L_e = \xi_{topo}^{-2} m_e$, and $C_e = \xi_{topo}^{2} k^{-1}$, are the **instance-1** realization of the class-invariant `BoundResonator` (def-b42e9d) forms within the `SubstrateExcitation` (def-7a3f1c) class-tree. This is a **CONSISTENCY** re-expression of already-derived canon (the electron LC tank clm-kezk9z, the Q-factor $\alpha^{-1} = Q_e$ clm-rtdmsn, the topo-kinematic $L = \xi_{topo}^{-2} m$ clm-i9l284) in matched phase-space EE coordinates — **not** an emergence or class-law claim (consistency-vs-emergence; [cvr-reflection-smith.md](./circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md):5).

- _Specific Claims_
  - The electron is a **BoundResonator** — a closed, high-$Q$, TIR-confined LC cavity (the $0_1$ unknot dilatation-mass carrying a $(2,3)$ winding) — i.e. instance-1 of `SubstrateExcitation`, **not** an open (radiating) Cosserat screw (ave-cavity-class-identification).
  - Instance fields: $Q_e = 1/\alpha = 4\pi^3+\pi^2+\pi \approx 137.036$ (clm-rtdmsn); $L_e = \xi_{topo}^{-2} m_e$ ([topological-kinematics.md](./circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md):76, clm-i9l284); $C_e = \xi_{topo}^{2} k^{-1}$ ([resonant-lc-solitons.md](./circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):12). The class-invariant FORMS — the pole shape $s_\pm = -\omega_0/(2Q) \pm j\omega_d$, the root-locus, $S(A)=\sqrt{1-(A/A_c)^2}$, and the $\Gamma_{spinor}=-1$ wall — carry **no** electron value; the electron reproduces today's numbers (`pole_real_over_w0` $=-\alpha/2$) by plugging in its own $Q$.
  - The real part $R$ is the per-cycle **radiative leak** (the pole's distance $-\alpha\omega_0/2$ from the $j\omega$ axis, $= \alpha = 1/Q_e$); the reactive part $jX$ is the lossless $C\leftrightarrow L$ breather (virial-balanced $\langle E_C\rangle = \langle E_L\rangle = \tfrac12 m_e c^2$).
- _Specific Non-Claims and Caveats_
  - **CONSISTENCY, not emergence**: re-expresses derived canon as the explicit field-instance bundle; originates no new derivation. The numerical inputs ($\alpha$, $m_e$) are CODATA-derived; this is not an emergence-class result.
  - **$\alpha$ stays UNIVERSAL** (the EM coupling, not electron-specific). The reflection form is $|\Gamma_{EM}|^2 = 1-\alpha$ and is **NOT** generalized to $1-1/Q$ — only the electron's $Q$ VALUE is the factored instance field, never $\alpha$.
  - **Two distinct $\Gamma$'s, labelled not resolved (homonym; open for adjudication):** $\Gamma_{spinor}=-1$ is the topological $2\pi\to4\pi$ / perfect-short class-invariant **stability** wall (ALL fermions, electron AND proton); $|\Gamma_{EM}|^2 = 1-\alpha$ is the electron-scoped EM **radiative-leak** corollary ([cvr-reflection-smith.md](./circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md):36). Whether the impedance-short $\Gamma=-1$ ([resonant-lc-solitons.md](./circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):42-48) is identically the spinor sign is a **pending human physics ruling** — not decided here.
  - **$|\Gamma_{EM}|^2 = 1-\alpha$ as a UNIVERSAL class law is gated** on that pending ruling; kept DEFAULT electron-scoped.
  - **Mass-"3" only**: the $H(s)$/phasor view is the A1 dilatation MASS-"3"; the $(2,3)$ Cosserat micro-rotation charge-"3" winding is orthogonal (A1 $\perp$ T2) and is **never** wired into the breather's $(V_{inc}, V_{ref})$ phasor ([master-equation.md](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20).
  - **Sector attribution PROVISIONAL**: which constitutive parameter moves at the wall (capacitive $C_{eff}\to\infty$ vs magnetic $\mu_{eff}\to0$) rests on the input-only clm-lv3uw1 and the still-open FLAG-2 ([cvr-dc-operating-point.md](./circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md):55); both routes give the same $Z=Z_0\sqrt{S}$ curve, so the bundle is robust but the attribution is unsettled.
  - **Carried engine flags**: $S^{0.25}$-vs-$S^{0.5}$ exponent defect ([cvr-reflection-smith.md](./circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md):66); $S_{MIN}$/$A_{CAP}$ apparatus clip ([cvr-dc-operating-point.md](./circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md):51).

> **Leaf references:** [resonant-lc-solitons](./circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-rtdmsn — Electron $\alpha^{-1}$ as the LC-tank Q-factor (solidity 0.85)
  - clm-kezk9z — $Z_0$ from discrete LC ladder + the $\Gamma=-1$ confinement wall (solidity 0.90)
  - clm-i9l284 — $\xi_{topo} = e/\ell_{node}$ + the $L=\xi_{topo}^{-2}m$ topo-kinematic mapping (solidity 0.90)
- solidity: 0.65 (ok to build on, see caveats) [= min(0.65, 0.85)]
- rationale: A CONSISTENCY-class re-expression: it restructures already-derived canon (the LC-tank electron, $Q_e=1/\alpha$, $L=\xi_{topo}^{-2}m$) into the explicit $R/X/Q/L/C$ field-instance bundle and is byte-identical-verified against the live engine, so the algebra is clean. It is capped below the spine because (a) the sector attribution (capacitive vs magnetic) rests on the input-only clm-lv3uw1 + the open FLAG-2, and (b) the $|\Gamma_{EM}|^2=1-\alpha$-as-universal-law and the $\Gamma$-homonym resolution are gated on a pending human physics ruling. The confidence reflects a faithful re-expression, not new physics; consistency-vs-emergence honestly tags it CONSISTENCY.
- strengthen-by:
  - Resolve the $\Gamma$-homonym (is the impedance-short $\Gamma=-1$ identically the topological $2\pi\to4\pi$ spinor sign?) and the universal-vs-electron scope of $|\Gamma_{EM}|^2=1-\alpha$ (auditor + Grant physics ruling).
  - Close FLAG-2 (capacitive vs magnetic sector attribution) so the bundle's sector field is no longer provisional.

---

## Node-Up Small/Large-Signal Response and the Static-Field Grade Asymmetry
<!-- id: clm-vca7r1 -->

- The vacuum LC tank's two reactive grades key on **different drive variables**: $\varepsilon$-grade = varactor on $V$ ($C_{eff}=C_0/S(A_V)$); $\mu$-grade = relativistic inductor on circulating $I$ ($L_{eff}=L_0/S(A_I)$, $I_{max}=\xi_{topo}c\approx124.4$ A). Same Axiom-4 kernel, two keyed arguments.
- _Specific Claims_
  - **R1 (symmetric internal loading):** both grades driven ($S_\varepsilon=S_\mu=S$) $\Rightarrow Z=Z_0$ invariant (reflectionless), small-signal $n=1/\sqrt{S}$, $\delta n=1/\sqrt{S}-1\approx+\tfrac14 A^2$ (positive; canonical Op16 ray speed $c_{shear}=c_0\sqrt{S}$ drops, light slows, gravity-well-like; `manuscript/ave-kb/common/operators.md`:56) — the Symmetric-Gravity operating point (INVARIANT-S2 W6 scope, `manuscript/ave-kb/CLAUDE.md`:75).
  - **R2 (static-E route):** a static $\mathbf E$ loads $\varepsilon$ only ($S_\varepsilon<1$, $S_\mu=1$) $\Rightarrow$ asymmetric $Z_{eff}=Z_0\sqrt{S_\mu/S_\varepsilon}$, isotropic common-mode $\delta n\approx-\tfrac14(E/E_{yield})^2$ (negative; $\varepsilon_{eff}=\varepsilon_0 S$ decreases, vacuum softens), with the matched **differential falsifier** $\delta n_{bir}=n_\parallel-n_\perp\approx-\tfrac12 A^2$ (uniaxial probe, clm-pp3qwf) — the bench / HIBEF E-route.
  - **R3 (static-B):** a static $\mathbf B$ ($\partial\mathbf B/\partial t=0$, sustained by the magnet's current not the vacuum's) induces no internal circulation $\Rightarrow I_{vac}=0 \Rightarrow A_I=0 \Rightarrow S_\mu=1 \Rightarrow \mu_{eff}=\mu_0 \Rightarrow \delta n_\mu = 0$ **ANALYTICALLY EXACT** at all $B$ (trivially "flat" 2.5 T → 1 kT: the kernel argument is identically zero, not a numerical finding). The $\mu$-grade is an ideal relativistic inductor; only $dI/dt$ (circulation rate) loads it. Direct-kernel positive control (NOT the fdtd engine): `src/tests/test_vca_node_regime_sweep.py`.
  - The static-field **asymmetry** (E loads, B does not) is the load-bearing consequence of the keyed-argument duality and the substrate mechanism behind the no-static-B-birefringence side-prediction.
- _Specific Non-Claims and Caveats_
  - $B_{SNAP}=1.89\times10^9$ T is an **energy-density scale** ($B_{SNAP}^2/2\mu_0 = m_ec^2/\ell_{node}^3$), NOT a rival kernel argument; the $\mu$-grade kernel argument is $I/I_{max}$, not $B/B_{SNAP}$.
  - The three regimes are the **operating-point** (large-signal) states; the small-signal $\delta n$ is the linearized probe response about each operating point. R1/R2 magnitudes are leading-order; the exact R2 differential is the OQ-1 par−perp result (clm-pp3qwf).

> **Leaf references:** [node-up-small-large-signal](./circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md).

### Quality
- confidence: 0.85
- depends-on:
  - clm-p5cf3t (relativistic inductor $L_{eff}(I)$, $I$-keyed magnetic-sector kernel)
  - Axiom 4 (universal saturation kernel, projected onto each grade)
  - clm-i9l284 (topo-kinematic $I=\xi_{topo}v$, $L=\xi_{topo}^{-2}m$ mappings)
- solidity: 0.85 (ok to build on) [= min(0.85, 0.85)]
- rationale: The R1/R2/R3 operating points are clean projections of the already-derived Axiom-4 kernel onto the $V$-keyed varactor and the $I$-keyed relativistic inductor (clm-p5cf3t), with INVARIANT-S2's W6 scope (`manuscript/ave-kb/CLAUDE.md`:75) supplying the symmetric-vs-asymmetric taxonomy. R3's $\delta n_\mu=0$ is **analytically exact**: the $\mu$-grade kernel argument is the internal circulating current $I_{vac}$, and a static B ($\partial B/\partial t=0$) drives $I_{vac}=0 \Rightarrow A_I=0 \Rightarrow S_\mu=\sqrt{1-0^2}=1$ at every $B$ (hence trivially "flat", not a sweep finding). The direct-kernel positive control `src/tests/test_vca_node_regime_sweep.py` evaluates $S_\varepsilon$, $S_\mu$, $\delta n$ straight from the Axiom-4 kernel (NOT the fdtd engine, which carries the live $|B|$-keying VCA-R01 defect and could not reproduce R3) and confirms $\delta n_\mu=0$ at $B=2.5..1000$ T and the R2 leading coefficient $=\tfrac14$. Capped at the relativistic-inductor parent's band: the construction rests on the $I$-keyed primitive plus the kernel, no new free parameter.
- strengthen-by:
  - Land the engine I-keyed $\mu$-saturation fix (VCA-R01) so the code's mu-grade keys on circulation, matching this leaf and removing the live static-|B| keying defect (`fdtd_3d.py`, `scale_invariant.py`).

---

## PVLAS / BMV Static-B Birefringence Null is Consistent with AVE
<!-- id: clm-pvlas1 -->

- A static external $\mathbf B$ ($\partial\mathbf B/\partial t = 0$, sustained by the magnet's current not the vacuum's) induces no internal vacuum circulation $\Rightarrow S_\mu = 1 \Rightarrow \mu_{eff}=\mu_0 \Rightarrow \delta n_\mu = 0$ exactly. The PVLAS/BMV static-B birefringence null is therefore the **expected AVE result**, NOT a falsification.
- _Specific Claims_
  - The $\mu$-grade is an ideal relativistic inductor keyed on circulating current $I$ (clm-p5cf3t), so a static $\mathbf B$ does not load it — there is no $dI/dt$ to drive internal circulation (Lenz). PVLAS does **not** test AVE.
  - **Bold side-prediction:** AVE predicts **NO static-B vacuum birefringence** at any field strength (categorical, not just below current bounds). A *static-B* birefringence detection at the QED level or above would FALSIFY this AVE prediction.
  - The real AVE test is the **E-route** (static-$\mathbf E$ / HIBEF-class facility field), which biases the $V$-keyed varactor (R2) and gives the OQ-1 differential ratio $\delta n_{AVE}/\delta n_{QED}=7.5/\alpha^3\approx1.93\times10^7$ (clm-pp3qwf).
- _Specific Non-Claims and Caveats_
  - AVE does **not** claim the PVLAS null confirms AVE — a null is *consistent with* AVE (and with QED's tiny $\sim10^{-23}$ at 5 T being below sensitivity). The discriminating measurement is the E-route, where AVE and QED diverge by $\sim10^7$.
  - QED *does* predict a static-B birefringence ($\delta n\sim10^{-23}$ at 5 T); the AVE no-static-B prediction is a categorical chord that distinguishes the two frameworks once static-B sensitivity reaches the QED level.

> **Leaf references:** [pvlas-static-b-verdict](./falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md).

### Quality
- confidence: 0.8
- depends-on:
  - clm-vca7r1 (node-up static-field grade asymmetry; R3 static-B → $\delta n_\mu=0$)
  - clm-p5cf3t (relativistic inductor, $I$-keyed magnetic-sector kernel)
  - clm-pp3qwf (E-route birefringence discriminator, the matched-observable test)
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 0.80)]
- rationale: The static-B transparency follows directly from the $I$-keyed relativistic-inductor primitive (clm-p5cf3t) via the node-up asymmetry leaf (clm-vca7r1): no $dI/dt$ ⟹ $I_{vac}=0$ ⟹ $A_I=0$ ⟹ $S_\mu=1$ ⟹ $\delta n_\mu=0$ **analytically exact** at all $B$ (the kernel argument is identically zero, not a numerical fit). The direct-kernel positive control `src/tests/test_vca_node_regime_sweep.py` confirms $\delta n_\mu=0$ at $B=2.5..1000$ T by evaluating the Axiom-4 kernel directly (NOT the fdtd engine, which carries the live $|B|$-keying VCA-R01 defect). The PVLAS-consistency verdict and the no-static-B side-prediction are clean consequences. Capped at the E-route discriminator's band (clm-pp3qwf, 0.80): the verdict inherits that the AVE-distinct chord is the saturation existence + static-B transparency, while the E-route magnitude is an $\alpha$-echo.
- strengthen-by:
  - Quantify the static-B sensitivity threshold at which an AVE no-static-B prediction becomes distinguishable from QED's $\sim10^{-23}$ (currently a categorical chord, not a numbered bound).

---

## Graded-Network Response: TLM Dispersion + Symmetric/Asymmetric Loading
<!-- id: clm-gvn4r1 -->

- The K4 lattice is a **graded LC transmission line**: per-node $L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$ wired by $z=3$ mutual inductive struts. This leaf assembles the single-node response (clm-vca7r1) into the network layer and reads off the four consequences a single node cannot host (dispersion, graded index, macroscopic bridge, boundary $\Gamma$, route-separability). **Class-C CONSISTENCY re-expression** (matches the per-DOF / device-network tags); originates no new substrate primitive and no new dimensionful value.
- _Specific Claims_
  - **Dispersion (Q1):** the lossless LC ladder gives $\omega(q)=(2c_0/\ell_{node})|\sin(q\ell_{node}/2)|$; the continuum limit recovers $c_{EM}=c_0$ and $Z_0=\sqrt{\mu_0/\varepsilon_0}=376.73\,\Omega$ EXACTLY ($\ell_{node}$ cancels — **validate-on-known**, NOT emergence). The leading $(q\ell_{node})^2$ term is an **isotropic scalar** (K4 2nd-moment tensor $=(4/3)\mathbb{I}$); the **first anisotropic invariant is QUARTIC** $(q\ell_{node})^4$ (cubic harmonic $q_x^4+q_y^4+q_z^4$), set by the tetrahedral 4th moment — reproduces preferred-frame:48,:50 (clm-yr6tu4) network-up.
  - **Graded index (Q2):** a spatial bias $A_0(x)$ projects through the single Axiom-4 kernel onto both grades. **SYM co-grade** ($S_\varepsilon=S_\mu=S$) ⟹ $Z(x)=Z_0$ invariant ⟹ reflectionless lens ($n=1/\sqrt{S}$, $\delta n\approx+\tfrac14 A^2$) = the achromatic-impedance-matching leaf (clm-rd9cjm) = gravity-as-graded-index. **ASYM static-E** ($S_\mu=1$ forced by zero circulation) ⟹ $Z(x)=Z_0(1-A^2)^{-1/4}$ varies ⟹ reflective ($\delta n\approx-\tfrac14 A^2$) = the vacuum-impedance mirror. One network, two regimes; the switch is loading-symmetry, not gradient profile.
  - **Macroscopic bridge (Q3, load-bearing):** per-node $\delta n$ accumulates as the standard coherent optical-path integral $\phi=(2\pi/\lambda)\int n\,dl$ — $\ell_{node}$ cancels exactly (like $v_g=c$) — times the Fabry-Perot finesse build-up $(2F/\pi)$, NOT a per-node $\times N$ count. The birefringence COEFFICIENT $7.5/\alpha^3\approx1.93\times10^7$ (clm-pp3qwf) SURVIVES the node→macroscopic translation intact. This re-grounds the **already-canonical** OQ-1 field→cavity coupling (claim-quality.md:391); it does NOT re-derive it.
  - **Boundary $\Gamma$ (Q4):** governed by co-grading SYMMETRY. SYM ⟹ $Z=Z_0$ everywhere ⟹ $\Gamma=0$ ACHROMATIC even at an abrupt $n$-jump (light bends, never reflects = AVE-distinct). ASYM static-E ⟹ $\Gamma\ne0\approx A^2/8$ (Fabry-Perot fringes; adiabatic-taper suppression $\sim L^{-2}$).
  - **Routes don't mix (Q5):** $\varepsilon$(E-route) and $\mu$(B-route) are structurally decoupled at network scale (different kernel arguments; static E has no $dB/dt$). The static-B-transparent verdict (clm-pvlas1) is ROBUST at network scale.
- _Specific Non-Claims and Caveats_
  - **CATEGORY-ERROR GUARD:** the chiral circulator / $H_{couple}$ wires the MECHANICAL bulk(A1/mass) grade to the shear(Cosserat/charge) grade — NEITHER is the $\varepsilon$-varactor nor the $\mu$-inductor of the EM-transverse port. It is NOT the $\varepsilon$/$\mu$ route-coupling element and its magnitude is un-computed (STATED-pending-engine, cvr_model.py:243).
  - **SCOPE GUARD on the $(q\ell_{node})^4$ chord (P1b demotion, 2026-06-24):** it is a chord ONLY because the lattice is cubic/tetrahedral (a generic lattice gives $(q\ell_{node})^2$ anisotropy) AND only at the FORM level (magnitude IMPORTED, per-dof:71). The **distinctive $(q\ell_{node})^4$ PHOTON dispersion tell is DEMOTED to CONDITIONAL**: the P1b genuine 24×24 chiral-srs Bloch eigensolve (`src/scripts/vol_4_engineering/srs_bloch_dispersion.py`, branch `engine/p1b-modes-live`) MEASURES the GENERIC band-edge anisotropy slope $1.9999$, NOT 4 — the quartic photon horn is a re-stated inserted exponent that survives ONLY if the unproven weak-C no-zone-edge theorem holds (gate `wejkhvnfb`, OPEN; see `clm-k4d4ph`, register §2.2). What survives node-up is the bond-moment ISOTROPY of the 2nd moment ($=(4/3)\mathbb{I}$) and the small-$k$ emergent-Lorentz isotropy (band-edge anisotropy, NOT a low-$k$ Lorentz violation). DEMOTED, not refuted — the quartic could RETURN if weak-C is proven. Do NOT headline the network re-grounding as a solidity lift. The no-LIV continuum-limit theorem remains OPEN (gate `wejkhvnfb`).
  - The birefringence-coefficient MAGNITUDE $1.93\times10^7=7.5/\alpha^3$ is an **$\alpha$-echo** at the value level (claim-quality.md:399,405). The AVE-distinct chord is existence-of-saturation (tree-level $O(1)$) + the static-B exact-zero.

> **Leaf references:** [graded-network-response](./circuit-theory/ch1-vacuum-circuit-analysis/graded-network-response.md).

### Quality
- confidence: 0.83
- depends-on:
  - clm-vca7r1 (node-up single-tank R1/R2/R3 operating points; static-field grade asymmetry)
  - clm-pp3qwf (E-route birefringence differential coefficient $7.5/\alpha^3$)
  - clm-yr6tu4 ($(q\ell_{node})^4$ cubic-symmetry anisotropy; weak-C scoped)
  - clm-rd9cjm (achromatic impedance matching = the SYM-loading limit)
  - clm-p5cf3t (relativistic inductor; $I$-keyed $\mu$-sector)
  - Axiom 4 (universal saturation kernel, projected onto each grade)
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.83, 0.55)]
- rationale: The network layer is clean projections of already-derived primitives onto the LC-ladder framing — $c_{EM}=c_0$/$Z_0$ are validate-on-known (the $\ell_{node}$ cancellation, z0-derivation:37,:40), the $(q\ell_{node})^4$ tell is the K4 4th-moment cubic harmonic (preferred-frame:48,:50, clm-yr6tu4's 0.78 weak-C band), and the SYM/ASYM regimes are the achromatic-lens (clm-rd9cjm) and vacuum-impedance-mirror (clm-pp3qwf) limits of one graded network. The macroscopic bridge re-grounds the already-CLOSED OQ-1 coupling (claim-quality.md:391); the coefficient survives because $\ell_{node}$ cancels and $g_{eff}$ cancels in the AVE/QED ratio. No new free parameter. **Solidity capped at 0.55 by the lowest dependency, clm-rd9cjm (achromatic impedance matching, vol3:0.55) — the SYM-loading limit this leaf extends; "use as input only, don't build deeper" until that parent strengthens.** The chord content (the $(q\ell_{node})^4$ form, the achromatic $\Gamma=0$ null, the static-B exact-zero, route-cleanness) is independently grounded in clm-yr6tu4 / clm-vca7r1 / clm-pvlas1 and is NOT capped down by the achromatic-lens magnitude; the 0.55 reflects the build-on-this metadata floor, not the chord-vs-echo verdict.
- strengthen-by:
  - Close the no-LIV / exact-continuum-limit decoupling theorem (gate `wejkhvnfb`) so the $(q\ell_{node})^4$ horn is a derived theorem, not a regime-grounded prediction.
  - Compute the chiral-circulator non-reciprocity magnitude (pending the chiral-crystal engine, cvr_model.py:243) — needed for any NON-RECIPROCAL boundary $\Gamma$ ($S_{21}\ne S_{12}$) bench observable.
  - A K4-native graded-$A_0(x)$ FDTD confirmation (CPML, PML-excluded probe, reactance-pair tracking of both $V$ and $I$ states) once the VCA-R01 engine $\mu$-keying bug is fixed.

---

## Lossless-Port Measurement Back-Action = Re(Z_probe)/Z_channel
<!-- id: clm-zp4kqr -->

In a lossless-reactive substrate (Axiom 3) the entire **irreversible** measurement back-action on a substrate mode is carried by the probe port's resistive part, with **no internal-medium-loss term**: $(\Delta U/U)_{\text{per cycle}} = \kappa\,\mathrm{Re}(Z_{probe})/Z_{channel}$, $\kappa = O(1)$ port coupling. The reactive part $\mathrm{Im}(Z_{probe})$ contributes a conservative, calibratable mode-detuning only. This specializes standard loaded-$Q$ to a lossless medium by *removing* a term, not adding one; the READ-mode non-invasiveness axis is therefore $\mathrm{Re}(Z_{probe})/Z_{channel}\to0$, **not** $|Z_{probe}|$ large.

- _Specific Claims_
  - Back-action (irreversible energy drain) $= \kappa\,\mathrm{Re}(Z_{probe})/Z_{channel}$; in a lossless substrate $\mathrm{Re}(Z_{probe})$ is the exact and entire *energy* back-action budget (no internal-loss sink).
  - $\mathrm{Im}(Z_{probe})$ detunes the mode (calibratable systematic), does not drain it.
  - The READ-mode design axis is the resistive ratio, not the magnitude; $|Z_{probe}|$ is a proxy that fails for any lossy high-$|Z|$ probe.
- _Specific Non-Claims and Caveats_
  - **CONSISTENCY, not emergence / not a chord** (consistency-vs-emergence): predicts no measurable beyond ordinary loaded-$Q$ once Axiom 3 is granted. The lossless axiom removes a term; it does not produce new physics.
  - "Entire back-action" scopes the *energy* (irreversible) budget only — $\mathrm{Im}(Z_{probe})$ still detunes the mode as a separate, calibratable term.
  - Most of the surrounding measurement-coupling primitive (read-vs-measure, reactive-tap) is **textbook EE**, asserted-as-textbook, not AVE-distinct.
  - The symbol $Z_{probe}$ and the ratio name are **proposed, pending Grant ratification** (no new substrate-object glyph — INVARIANT-N1).

> **Leaf references:** [measurement-coupling-probe](./circuit-theory/ch1-vacuum-circuit-analysis/measurement-coupling-probe.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 3 (lossless-reactive substrate — removes the internal-loss sink)
  - clm-rtdmsn — loaded-vs-intrinsic $Q$ / the matched-port per-cycle leak (solidity 0.85)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.85)]
- rationale: A clean CONSISTENCY-class reframing: standard loaded-$Q$ back-action ($\propto$ resistive fraction of the loading impedance) specialized to a lossless medium, where Axiom 3 removes the internal-loss term so $\mathrm{Re}(Z_{probe})$ becomes the exact and entire energy budget. The algebra is the textbook loaded-resonator ledger (cited, not novel); the AVE-specific step is the single term-removal granted by Axiom 3. Pinned mid-band because it is a faithful specialization of existing canon with a correct, narrow lossless sharpening — not new physics (it adds no measurable beyond loaded-$Q$) and not a magnitude-framing (it explicitly undercuts $|Z|$). Capped below the spine because $\kappa$ is left as an $O(1)$ port factor rather than derived per geometry, and the symbol naming is unratified.
- strengthen-by:
  - Derive the $\kappa$ port coupling factor from the specific port geometry (the existing coupling-coefficient $k$, resonant-lc-solitons.md:118) so the relation is quantitative, not proportional.
  - Grant-ratify the $Z_{probe}$ symbol + the $\mathrm{Re}(Z_{probe})/Z_{channel}$ ratio name.

---

## Bench-Fleet Mode Partition (READ/MEASURE) Maps onto the Axiom Partition (Ax2/Ax4)
<!-- id: clm-zp7bds -->

The vacuum-impedance-network measurement frame partitions the falsification-bench fleet by coupling mode, and the mode partition maps onto the axiom partition: **Cleave-01** (femto-electrometer) is the only **READ-mode** bench and the only **Axiom-2** test; the other four benches (VacuumMirror, cRIO $C_{eff}(V)$, vacuum birefringence, GW-echo) are all **MEASURE-mode** and all gated on **Axiom 4** (the saturation kernel). Consequence: **Ax2-fail $\neq$ Ax4-fail** — the framework can survive a partial falsification with a clean walk-back, and this primitive makes that partition explicit.

- _Specific Claims_
  - Every bench classifies as READ (minimize $\mathrm{Re}(Z_{probe})/Z_{channel}$) or MEASURE (controlled small-signal, observable IS the reactance/response).
  - Cleave-01 = unique READ-mode / unique Axiom-2 bench; the other four = MEASURE-mode / Axiom-4.
  - The mode partition coincides with the axiom partition, so Ax2-fail and Ax4-fail are independently survivable.
- _Specific Non-Claims and Caveats_
  - **A design-organizing / classification claim**, not a physics claim — it correctly classifies existing bench designs; it predicts nothing on its own.
  - The MEASURE-mode coupling is **NOT power-matched** ("matched" re-imports the magnitude error); it is controlled small-signal (ratiometric lock-in for cRIO).
  - The bulk-sector READ coupling LOCATION (short vs rigid) is **OPEN, routed to Grant** (flag-don't-fix).

> **Leaf references:** [measurement-coupling-probe](./circuit-theory/ch1-vacuum-circuit-analysis/measurement-coupling-probe.md).

### Quality
- confidence: 0.6
- depends-on:
  - clm-kezk9z — $Z_0$ + the three-impedance-law channel set (solidity 0.90)
  - clm-zp4kqr — the READ-mode $\mathrm{Re}(Z_{probe})/Z_{channel}$ axis (this leaf)
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.70)]
- rationale: A framing/classification claim (it explicitly "predicts nothing on its own"). The READ/MEASURE-vs-Ax2/Ax4 mapping is a correct, useful organization of the existing bench fleet and gives every future bench a four-question design checklist. Pinned at the framing-claim band: it is sound as an organizing partition and the per-bench tags are corpus-cited, but it is a design language, not a derivation, and one of its siting questions (bulk-sector short-vs-rigid) is still open. "Use as input only" because building deeper physics on a classification scheme would over-weight a checklist.
- strengthen-by:
  - Resolve the bulk-sector coupling-location open question (§3.2 of the leaf, routed to Grant) so the GW-echo MEASURE-mode row's coupling note is settled.
  - Confirm each bench's mode/axiom tag against its own prereg as those benches mature past draft.

---

## Winding-Pair Interaction Leg of Axiom 2 — Coulomb Sign Structure via the Gapped ω Sector
<!-- id: clm-wcoul2 -->

The first **engine-derived winding-pair interaction**. Two (2,3) winding solitons, seeded at controlled separation on the S1 buckle-OFF host and evolved under the real `step()`, interact with a **Coulomb sign structure: like windings REPEL, unlike windings ATTRACT** — measured as the sign of the self-subtracted Maxwell ω-field normal-stress force $F_{int}=T^{xx}_\omega$ integrated over the mid-plane. Under Axiom 2's own winding=charge mapping (anti-handed = opposite charge sign), signed Coulomb predicts exactly co-repel/anti-attract, and the engine reproduces it. This is the **interaction leg of Axiom 2** the Cleave-01 arc lacked — the coupling-class content that says HOW like windings interact, engine-derived rather than asserted.

- _Specific Claims_
  - Self-subtracted interaction force $F_{int}$ = co-handed **REPULSIVE** (+7.07e-3 at $d$=34), anti-handed **ATTRACTIVE** (−2.02e-3) — the signed-Coulomb like/unlike rule.
  - The sign is **plane-invariant** (identical across integration planes XC±0/±1/±3), **enantiomorph-consistent** (sign(RR)=sign(LL), sign(RL)=sign(LR)), **window-invariant** ({150,250,350} steps), and **α-invariant** (α is absent from the force path; $\kappã$=6/5 literal) at $d\in\{34,38\}$.
  - **Mechanism (electric, not magnetic):** the sign is the OPPOSITE of the classical current-loop rule (co-directed circulations attract; the winding pair co-repels — validated: the classical-circulation baseline reproduces co-attract/anti-repel, its own current-loop validate-on-known). So the winding **acts as a charge, not a current** — it couples through the ELECTRIC (charge) channel of the rotation sector. A massive-vector-like exchange through the gapped ω sector gives like-repel/unlike-attract; a scalar mediator would give universal attraction. The observed signs indicate the ω (rotation) sector mediates the winding interaction electrically.
- _Specific Non-Claims and Caveats_
  - **CONSISTENCY-class, NOT a chord.** The sign structure is signed-Coulomb, which is SM-shared; by the symmetric standard it is NOT an AVE-distinct parity divergence. The winding-force parity-chord objective (register §2.4) is **RESOLVED-TO-CONSISTENCY** (not falsified) — the winding-force question produced this Ax2 interaction leg instead of a chord.
  - **The magnitude ratio $R=|F|_{co}/|F|_{anti}$ is BLOCKED** (ill-defined at current engine capability): knot overlap at stable separations ⇒ no plane-conservative integral (plane spread 4.7–9.5×); Yukawa screening ⇒ no source-free far-field ($|F|$ falls 2.6e5× over $d$=34→44). Only the SIGN STRUCTURE is claimed; NO magnitude, NO ratio.
  - **$\omega_{gap}$ = HOST KNOB.** $\omega_{gap}$=1.0 is a host default (`crystal_graft_v2.py:65`), NOT the canonical $\Omega_C=c/\ell_{node}$. So the Yukawa range ($\xi=c_\omega/\omega_{gap}\approx$0.548 cells) — the mediator "mass" / screening scale — is **artifact-scale, not a substrate prediction**. The robust content is the SIGN STRUCTURE; the range/mediator-mass is not claimed. **No bench-scale range or force magnitude is predicted.**
  - **Linear / buckle-OFF host.** The κ_chiral saturation channel is NOT exercised (the pre-committed stage-(b) successor is **MOOT** — its trigger, classical degeneracy, never fired; the sign was resolved by the Axiom-2 mapping).
  - **Verdict domain $d\in\{34,38\}$.** $d$=44 is a dead-instrument cell (force 5 OOM into the numerical floor, Yukawa-screened); the anti sign there is noise-jittered and out-of-scope (Grant SNR-scoped-gate ruling, α, 2026-07-03).

> **Leaf references:** [field-free-optical-activity](./falsification/ch12-falsifiable-predictions/field-free-optical-activity.md).

### Quality
- confidence: 0.7
- depends-on:
  - Axiom 2 (Topo-Kinematic Isomorphism — the winding=charge mapping that adjudicates the sign as signed-Coulomb)
  - Gate-0 pair-feasibility (STABLE-IN-A-WINDOW, PR #465 — the stable-pair substrate this measures on)
  - S1 winding-DOF (the (2,3) as a separately-conserved DOF, the seeded object)
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 1.00)]
- rationale: The SIGN result is robust — plane-, enantiomorph-, window-, and α-invariant at both signal-bearing separations, deterministic, self-subtracted, with two co-computed classical baselines (the current-loop circulation, which passes its own validate-on-known, and the achiral charge control). The Axiom-2 winding=charge mapping cleanly adjudicates the sign as signed-Coulomb (consistency, not chord), and the classical-circulation inversion pins the electric-not-magnetic mechanism. Held below the 0.9 identity band by two honest limits disclosed in the leaf: the mediator mass / range rides a host knob ($\omega_{gap}$, so no physical scale), and the magnitude-R is blocked (non-conservative overlap integral + screening) — so only the sign structure, not any magnitude, is claimed. Scope history: the objective began as a 2-band "dimensionless |F|-ratio chord" (register §2.4, highest-value unbuilt FORM chord), narrowed through Gate-0 (pair feasibility STABLE-IN-A-WINDOW) to the linear-channel campaign, where the magnitude-R was blocked (Grant's C) and the sign resolved-to-consistency (Grant's α + Coulomb-recovery) — the chord did not survive the symmetric standard, but the engine-derived Ax2 interaction leg did.
- strengthen-by:
  - Map $\omega_{gap}$ onto the canonical $\Omega_C=c/\ell_{node}$ (or derive the ω-tank restoring from lattice primitives) so the Yukawa range / mediator mass becomes a substrate scale rather than a host knob — then a physical range (and bench-reachability) could be assessed.
  - Find a plane-conservative force extraction (a source-free enclosing surface) at a larger domain / separation where the knots do not overlap, to convert the blocked magnitude-R into a real number — currently structurally dead at the Gate-0 stable window (screening).

---
