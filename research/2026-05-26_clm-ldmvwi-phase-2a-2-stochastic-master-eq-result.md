# Phase 2-A.2 Result — Stochastic Master Vacuum Equation + Extracted-Energy Process

**Date**: 2026-05-26
**Workstream**: Phase 2-A of clm-zuf7g1-strengthen (Born-rule master-equation-derivation-path)
**Branch**: `analysis/clm-ldmvwi-master-eq-stochastic-derivation` @ `e80080e6` (post Phase 2-A.1 prereg)
**Pre-reg**: [`2026-05-26_clm-ldmvwi-master-eq-stochastic-derivation-prereg.md`](./2026-05-26_clm-ldmvwi-master-eq-stochastic-derivation-prereg.md) §4.2
**Verdict**: **PASS** on AC-A1.1, AC-A1.2, AC-A2.1, AC-A2.2 (all 4 acceptance criteria for Phase 2-A.2) — initial draft auditor pass returned HOLD with 4 amendments (Findings 1+2+4+6); all 4 applied per Grant adjudication 2026-05-26 + reflected in §2.2 (damping convention note), §2.3 (one-sided FDT convention reconciliation), §3.3 (signal/noise physical-independence statement), §3.4 (V↔∂tA derivation via AVE Lagrangian).

---

## §0 — One-paragraph summary

Derived the AVE-native stochastic form of the master vacuum equation (Step A1) by coupling Vol 3 Ch 11's canonical Fluctuation-Dissipation Theorem at boundary impedance to the linear-regime master vacuum equation. Result: $\Box V + 2\gamma_n \delta^3(x-x_n) \partial_t V = f_n(t)\, \delta^3(x-x_n)$ with $\langle f_n(t) f_n(t')\rangle = 2 k_B T Z_{det}\, \delta(t-t')$ — the boundary node hosts both Ohmic damping AND Nyquist stochastic forcing, balanced by FDT (factor of 2 in time-domain matches Vol 3 Ch 11's pinned one-sided convention; the convention IS NOT AVE-fundamental, but is corpus-pinned by Vol 3 Ch 11:80). Derived the extracted-energy process $W(t; x_n) = \int_0^t V(x_n,t')^2 / Z_{det}\, dt'$ (Step A2) and decomposed it into deterministic-signal + stochastic-noise contributions for downstream first-passage analysis (Phase 2-A.3). Closed the V↔$\partial_t \mathbf{A}$ identification (§3.4) via the AVE-canonical Lagrangian $\mathcal{L}_{AVE} = \tfrac{1}{2}\varepsilon_0|\partial_t \mathbf{A}|^2 - \tfrac{1}{2\mu_0}|\nabla \times \mathbf{A}|^2$ at `vol1/dynamics/ch3-quantum-signal-dynamics/index.md:17`, removing what was previously a hidden stipulation in the clm-ldmvwi rationale's "$V \sim \partial_t \mathbf{A}$" parenthetical. No Born rule invoked; no QM-formalism imported. Both steps derive from already-canonical AVE content (Vol 3 Ch 11 FDT + master-equation.md + ohmic-decoherence-born.md detector model + AVE Lagrangian).

---

## §1 — Skills compliance fired before the derivation

Per workstream-level prereg §4.2 + recent discipline lessons (Path B-prime self-audit + clm-zuf7g1 Phase 1 hygiene pass):

| Skill | Status | What it caught / confirmed |
|---|---|---|
| `substrate-native-check` | ✓ FIRED | Read Vol 3 Ch 11 §FDT/Nyquist (lines 71-138) + master-equation.md verbatim before drafting derivation. Walked the boundary-impedance-thermalization mechanism explicitly: "thermal noise enters through impedance MISMATCHES at boundaries, not through bulk injection" (line 113). Verified the AVE-native picture is FDT-at-boundary-nodes, NOT bulk Langevin forcing. |
| `ave-canonical-leaf-pull` | ✓ FIRED | Read 3 leaves end-to-end: Vol 3 Ch 11 §FDT (lines 71-138, the FDT scaffold), master-equation.md (the derivation target), ohmic-decoherence-born.md (the detector model). Confirmed no prior corpus content on stochastic master equation. |
| `ave-discipline-translate` | ✓ FIRED with explicit decision | "Langevin equation" is standard stochastic mechanics terminology. Checked translation-tables: no QM-formalism import here; the AVE-native form is exactly what Vol 3 Ch 11 establishes — FDT-at-boundary-impedance applied to the master vacuum equation. This is substrate-derivation, NOT borrowed concept. Decision: skill non-firing is appropriate because the Langevin form IS the AVE-native extension of FDT, not an imported postulate. |
| `consistency-vs-emergence-UPGRADED` | ✓ FIRED with master-eq-derivation-path tracing | Step A1: Class 2 emergence — Langevin form derives from Vol 3 Ch 11 FDT (which itself derives from substrate impedance thermodynamics + Nyquist literally on $Z_0$). Step A2: Class 2 emergence — extracted-energy process is direct master-equation energy-conservation algebra under boundary loading. Both steps trace explicitly to master vacuum equation + canonical Vol 3 Ch 11 + Axiom 1. **NO step requires additional postulate beyond what's already in corpus.** |
| `phase-space-coordinate-check` | ✓ FIRED | Three coordinate systems kept distinct: (i) K4 substrate real-space $\mathbb{R}^3$ where $V(x,t)$ lives; (ii) stochastic-process space where the Langevin forcing $f_n(t)$ and the resulting random $V_\eta$ live as samples; (iii) (deferred to A.3) measurement-outcome space. A.2 work stays entirely in (i) and (ii). |
| `ave-independence-check` | ✓ FIRED | The derivation chain (Vol 3 Ch 11 FDT → boundary Langevin master eq → Joule integral W(t)) involves NO Born-rule input. The result is the substrate's own extracted-energy process; the click-probability identification is downstream (Phase 2-A.3+). Confirmed non-circular. |
| `verify-before-cite` | ✓ continuous | Vol 3 Ch 11 verbatim quotes at lines 80, 89, 93, 113, 119, 126 all grep-verified. Master-equation.md non-linear form verified. ohmic-decoherence-born.md line 18 detector model verbatim verified. |
| `ave-evidence-framing-discipline` | ✓ continuous | Result framed as "derived from substrate FDT + master vacuum equation" — NOT as "Born rule derivation." That's the A.3+A.4 work; A.2 sets up the substrate machinery without yet making the Born-rule connection. |

---

## §2 — Step A1: Stochastic Master Vacuum Equation Derivation

### §2.1 Starting point — the linear-regime master vacuum equation

Per [`vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md) canonical form:

$$\nabla^2 V - \mu_0 \varepsilon_0 \sqrt{1 - (V/V_{yield})^2} \frac{\partial^2 V}{\partial t^2} = 0$$

In the linear regime $V \ll V_{yield}$ (the regime where Born rule is canonically tested via low-amplitude photodetection), the saturation kernel $\sqrt{1 - (V/V_{yield})^2} \approx 1$, and the equation reduces to the standard linear d'Alembertian:

$$\boxed{\Box V \equiv \nabla^2 V - \frac{1}{c^2} \frac{\partial^2 V}{\partial t^2} = 0}$$

with $c = 1/\sqrt{\mu_0 \varepsilon_0}$. This is the AVE substrate's linear-regime wave equation, derived as the leading-order EFT consequence of the non-linear master equation per `master-equation.md:55` (the explicit "EFT statement" caveat in clm-efo113).

### §2.2 Adding boundary detector — Ohmic damping term

A detector at lattice node $x_n$ couples to the field via resistive mechanical load (per `ohmic-decoherence-born.md:18`, canonical):

> "any device that couples to the $\mathbf{A}$-field and extracts kinetic energy acts as a resistive mechanical load (where $1\,\Omega \equiv \xi_{topo}^{-2}\,\text{kg/s}$)"

Energy extracted at the boundary modifies the master equation by adding a dissipation term. From Vol 3 Ch 11 eq. (`eq:damping_coefficient`):

$$\gamma_n = \frac{1}{2} \frac{Z_{det}}{\omega_0 L_{eff,n}}$$

where $\omega_0$ is the local detector resonance + $L_{eff,n}$ is the effective inductance at boundary node $x_n$.

**Convention note (per auditor Finding 1, 2026-05-26)**: Vol 3 Ch 11:134 defines $\gamma$ via the formula above but does not explicitly state whether $\gamma$ is the "half-width" convention (under which the equation-of-motion damping term is $2\gamma \, \partial_t V$) or the "full damping rate" convention ($\gamma \, \partial_t V$). **This work adopts the half-width convention** matching standard damped-harmonic-oscillator notation ($\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0$), which is the standard in stochastic-detection theory. Vol 3 Ch 11 should be amended in a future maintenance pass to make this convention explicit; for now, this work's convention choice is locked here and propagates through Phase 2-A.3+. Under this convention:

$$\Box V(x,t) + 2\gamma_n \, \delta^3(x - x_n) \, \partial_t V(x,t) = 0$$

The $\delta^3(x - x_n)$ localizes the dissipation to the detector node. **No new physics**: this is the boundary-loading form of the master equation, standard wave-mechanics machinery applied to AVE's substrate.

### §2.3 Adding boundary noise — FDT forcing term

By Vol 3 Ch 11's canonical FDT (lines 75-93 verbatim):

> "every impedance boundary is a noise source... each lattice node radiates thermal noise proportional to its local impedance"

And the explicit prescription at line 119: **inject stochastic noise only at the boundary nodes, not uniformly across the bulk field**.

For a detector boundary at $x_n$ with characteristic impedance $Z_{det}$ thermalized at temperature $T$, the Nyquist relation (Vol 3 Ch 11 eq. `eq:nyquist`) gives the **one-sided** spectral density of the thermal voltage noise (integrated over positive frequencies only — the engineering convention Vol 3 Ch 11 has implicitly pinned):

$$S_{VV}^{(\text{one-sided})}(f) = 4 k_B T Z_{det}, \qquad \text{so}\quad \langle V_{noise}^2(f) \rangle = 4 k_B T Z_{det} \, \Delta f$$

**Convention reconciliation (per auditor Finding 2 + Grant adjudication 2026-05-26)**: the time-domain delta-correlated form of a one-sided spectral density $S^{(\text{one-sided})} = 4 k_B T Z_{det}$ is $\langle f(t) f(t')\rangle = 2 k_B T Z_{det}\, \delta(t-t')$ — factor of **2** in time domain (NOT factor of 4). The factor relation derives from the symmetric two-sided spectral density $S^{(\text{two-sided})} = S^{(\text{one-sided})}/2 = 2 k_B T Z_{det}$, integrated as $\langle f(t) f(t')\rangle = \int_{-\infty}^{\infty} S^{(\text{two-sided})}(f) \, e^{2\pi i f(t-t')} df = 2 k_B T Z_{det}\, \delta(t-t')$ in the white-noise limit. Per Grant's 2026-05-26 adjudication: the one-sided convention is NOT AVE-fundamental (it's a math/engineering convention), but Vol 3 Ch 11 has implicitly pinned it via its eq. `eq:nyquist` form. This work matches Vol 3 Ch 11's pinned convention.

In the white-noise approximation (valid for detector bandwidth $\ll k_B T / \hbar \approx 4 \times 10^{13}$ Hz at 300 K — satisfied by any realistic photodetector), the Langevin forcing $f_n(t)$ at the boundary node satisfies:

$$\boxed{\langle f_n(t) f_n(t') \rangle = 2 k_B T Z_{det} \, \delta(t - t')}$$

Per FDT structure, the noise injection and the Ohmic dissipation balance to maintain thermal equilibrium — this is the fluctuation-dissipation balance Vol 3 Ch 11 line 138 names as canonical: *"the noise power injected at the boundary is exactly compensated by the Ohmic dissipation rate, maintaining thermal equilibrium at temperature $T$."*

### §2.4 Result — the stochastic master vacuum equation

Combining §2.1-§2.3:

$$\boxed{\Box V(x,t) + 2\gamma_n \, \delta^3(x - x_n) \, \partial_t V(x,t) = f_n(t) \, \delta^3(x - x_n)}$$

with $\langle f_n(t) f_n(t') \rangle = 2 k_B T Z_{det} \, \delta(t - t')$ and $\gamma_n = Z_{det} / (2 \omega_0 L_{eff,n})$ (half-width convention; see §2.2 convention note).

**This is the AVE-native Langevin master equation**: the linear-regime master vacuum equation modified to include both dissipation (energy leaving the field) and stochastic forcing (thermal noise entering the field) at a detector boundary node $x_n$, balanced by FDT.

**Derivation traces explicitly**:
- Master eq → from `master-equation.md` (linear-regime EFT)
- Boundary damping term → Vol 3 Ch 11 eq. `eq:damping_coefficient` + Axiom 1 detector model
- Boundary forcing term → Vol 3 Ch 11 eq. `eq:nyquist` literally on detector impedance (line 93: "this is not an analogy")
- FDT balance → Vol 3 Ch 11 line 138 (canonical Fluctuation-Dissipation balance)

**Every step traces to already-canonical AVE content.** The work is the explicit application to the master vacuum equation, which was missing from corpus.

### §2.5 Acceptance criteria evaluation

**AC-A1.1 (Langevin master equation derived from substrate FDT, NOT imported as ad-hoc forcing)**: ✓ **PASS**. The Langevin form derives directly from Vol 3 Ch 11's "every impedance boundary is a noise source" + "inject stochastic noise only at boundary nodes" + the canonical FDT relation. No external Langevin formalism imported.

**AC-A1.2 (Forcing satisfies canonical Vol 3 Ch 11 FDT)**: ✓ **PASS**. $\langle f_n(t) f_n(t') \rangle = 2 k_B T Z_{det} \delta(t-t')$ (time-domain form per §2.3 convention reconciliation; factor of 2, not 4 — the one-sided spectral density $\langle V^2(f)\rangle = 4 k_B T R \Delta f$ from Ch 11 eq. `eq:nyquist` halves to two-sided $S^{(2s)} = 2 k_B T R$ when integrated over $(-\infty, \infty)$, giving the time-domain delta-correlated factor of 2) applied to $R = Z_{det}$ at the detector boundary, in the white-noise approximation valid for detector bandwidth $\ll k_B T/\hbar$.

---

## §3 — Step A2: Extracted-Energy Process Derivation

### §3.1 Instantaneous extracted power

At the detector boundary $x_n$ with resistive load $Z_{det}$, the instantaneous extracted power is governed by classical Joule heating:

$$P_{load}(t; x_n) = \frac{V(x_n, t)^2}{Z_{det}}$$

This is the standard Joule formula at a resistive boundary; canonical at `ohmic-decoherence-born.md:23`.

### §3.2 Time-integrated extracted energy

Over a measurement interval $[0, t]$, the total extracted energy is:

$$\boxed{W(t; x_n) = \int_0^t P_{load}(t'; x_n)\, dt' = \int_0^t \frac{V(x_n, t')^2}{Z_{det}}\, dt'}$$

This is the canonical "$W_{extracted}$" expression from `ohmic-decoherence-born.md:23`, now with $V(x_n, t)$ being the stochastic field from the Langevin master equation derived in §2.4.

### §3.3 Signal-vs-noise decomposition

Write the field at the detector boundary as the superposition:

$$V(x_n, t) = V_s(x_n, t) + V_\eta(x_n, t)$$

where:
- $V_s(x_n, t)$ is the **deterministic signal field** (e.g., the wave packet being measured — a propagating wave from a particle source, an EM wave from an emitter, etc.)
- $V_\eta(x_n, t)$ is the **stochastic Langevin response** to the local boundary forcing $f_n(t)$, mean-zero with variance set by FDT

**Physical independence of signal and detector-noise sources (per auditor Finding 4, 2026-05-26)**: $V_s$ is a deterministic field sourced **upstream of the detector boundary** (by an external emitter, particle wake, propagating wave packet, etc.); $f_n(t)$ is the **local detector-boundary Langevin noise** generated by the detector load's thermal coupling to the ambient bath. The two are uncorrelated **by virtue of having physically independent sources**: the signal emitter's dynamics are causally disconnected from the detector's thermal-bath fluctuations (separated systems, no shared dynamical history within the measurement interval). This is the standard signal-vs-detector-noise independence assumption used in all photodetection / radar / matched-filter theory; it derives directly from the spatial separation between the signal source and the detector boundary in any realistic measurement geometry.

The extracted energy becomes:

$$W(t; x_n) = \frac{1}{Z_{det}} \int_0^t \left[ V_s(x_n,t')^2 + 2 V_s(x_n,t') V_\eta(x_n,t') + V_\eta(x_n,t')^2 \right] dt'$$

**Ensemble average** (with the physical-independence assumption above):
- $\langle V_s^2 \rangle = V_s^2$ (deterministic — fixed signal, no randomness)
- $\langle V_s V_\eta \rangle = V_s \cdot \langle V_\eta \rangle = 0$ (valid because $V_s$ is non-random AND $\langle V_\eta \rangle = 0$ from Langevin structure; the physical-independence assumption guarantees factorization)
- $\langle V_\eta^2 \rangle = \sigma_\eta^2(x_n, t)$ (Langevin variance, set by FDT — proportional to thermal noise power $k_B T \cdot Z_{det}$ per Vol 3 Ch 11 line 138)

Therefore:

$$\langle W(t; x_n) \rangle = \frac{1}{Z_{det}} \int_0^t \left[ V_s(x_n,t')^2 + \sigma_\eta(x_n,t')^2 \right] dt'$$

**Two distinct contributions**:
- **Signal contribution**: $\int V_s^2 / Z_{det}\, dt$ — scales with squared signal amplitude. Via the V↔$\partial_t \mathbf{A}$ identification derived in §3.4 below, $V_s^2 \sim |\partial_t \mathbf{A}(x_n)|^2$ for transverse EM modes, matching the existing clm-ldmvwi formula.
- **Noise contribution**: $\int \sigma_\eta^2 / Z_{det}\, dt$ — scales with $k_B T \cdot Z_{det}$, giving the thermal floor of detector noise per Vol 3 Ch 11 FDT.

**Signal-to-noise ratio**: $\text{SNR} = V_s^2 / \sigma_\eta^2$. In the rare-event detection regime (the standard photodetection regime where clm-ldmvwi's Born-rule scaling is canonically tested), $\text{SNR} \ll 1$ over short intervals but the cumulative signal becomes detectable after sufficient integration — this is the regime where Phase 2-A.3 threshold-crossing analysis applies.

### §3.4 V ↔ ∂_t A identification (per auditor Finding 6 + Grant adjudication 6-a, 2026-05-26)

The master vacuum equation §2.1 uses a scalar field $V(x, t)$. The clm-ldmvwi click formula at `ohmic-decoherence-born.md:23` uses the vector quantity $|\partial_t \mathbf{A}(x_n)|^2$. This subsection establishes their physical identification, closing the auditor-flagged "load-bearing hidden assumption" by deriving it explicitly rather than stipulating it parenthetically.

**The AVE-canonical Lagrangian** (per `vol1/dynamics/ch3-quantum-signal-dynamics/index.md:17` and `vol1/claim-quality.md:734`):

$$\mathcal{L}_{AVE} = \tfrac{1}{2}\varepsilon_0 |\partial_t \mathbf{A}|^2 - \tfrac{1}{2\mu_0} |\nabla \times \mathbf{A}|^2$$

The kinetic term is $\tfrac{1}{2}\varepsilon_0 |\partial_t \mathbf{A}|^2$ — the substrate's "electric" energy density. The potential term is $\tfrac{1}{2\mu_0}|\nabla \times \mathbf{A}|^2$ — the substrate's "magnetic" energy density. Both terms are vector-valued via the vector potential $\mathbf{A}$.

**Identification**: in the master vacuum equation, $V(x, t)$ is the **scalar mode amplitude** of the transverse field at a given polarization. For a transverse EM mode propagating with polarization $\hat{\epsilon}$:

$$V(x, t) \equiv \hat{\epsilon} \cdot \partial_t \mathbf{A}(x, t)$$

This is the polarization-projected component of $\partial_t \mathbf{A}$. The master equation $\Box V = 0$ governs each polarization mode separately; the full vector wave equation $\Box \mathbf{A} = 0$ (transverse part in the appropriate gauge) decomposes into independent scalar equations per polarization.

**Detector coupling**: an Ohmic resistive detector at boundary node $x_n$ couples to the EM field via the current it drives in the load. The current is proportional to the local electric field $\mathbf{E} = -\partial_t \mathbf{A}$ (in any gauge where the scalar potential $\phi$ vanishes locally at the detector — the standard gauge for radiation-detector analysis). For a detector with sensitivity vector $\hat{\epsilon}_{det}$ (its preferred polarization direction):

$$V_{det}(x_n, t) = \hat{\epsilon}_{det} \cdot \mathbf{E}(x_n, t) = -\hat{\epsilon}_{det} \cdot \partial_t \mathbf{A}(x_n, t)$$

Joule heating at the detector: $P_{load} = V_{det}^2 / Z_{det}$. **Summing over polarization modes** (or for a detector with isotropic polarization sensitivity), the total extracted power becomes:

$$P_{load}(x_n, t) = \frac{|\partial_t \mathbf{A}(x_n, t)|^2}{Z_{det}}$$

This is the identification:

$$\boxed{V(x_n, t)^2 \,\to\, |\partial_t \mathbf{A}(x_n, t)|^2 \quad \text{(scalar-mode amplitude squared = vector-field magnitude squared, summed over polarizations)}}$$

**Substrate-native traceability**: the identification derives from the AVE-canonical Lagrangian via the standard EM-detection chain (detector current ∝ local $\mathbf{E}$ field, $\mathbf{E} = -\partial_t \mathbf{A}$ at the detector boundary, Joule power = $V^2/R$). No QM formalism imported. The "Coulomb gauge" stipulation in the earlier §3.3 draft is unnecessary; the identification works in any gauge where the scalar potential $\phi$ contributes negligibly at the detector boundary (true for radiation-detector geometries where charges are localized away from the boundary).

**Result for the extracted-energy process**:

$$\boxed{\langle W(t; x_n) \rangle = \int_0^t \frac{|\partial_t \mathbf{A}(x_n, t')|^2 + \sigma_\eta(x_n,t')^2}{Z_{det}} dt'}$$

This is the substrate-derived form of the canonical $W_{extracted}$ formula at `ohmic-decoherence-born.md:23`, now with the explicit V↔$\partial_t \mathbf{A}$ identification + the thermal-noise contribution from FDT.

**Closure of clm-ldmvwi rationale chain step 2**: the existing clm-ldmvwi rationale (vol1/claim-quality.md:323) names "$V \sim \partial_t \mathbf{A}$" as part of the "sound algebra" of the Joule-heating chain. §3.4 here makes this explicit derivation in substrate-native terms, removing the auditor-flagged hidden assumption.

### §3.5 Acceptance criteria evaluation

**AC-A2.1 (W(t; x_n) expression derived without invoking Born rule or QM postulates)**: ✓ **PASS**. The derivation uses only Joule heating ($P = V^2/R$, classical algebra) + the substrate's stochastic Langevin field from §2.4 + the V↔$\partial_t \mathbf{A}$ identification from §3.4 (derived from AVE-canonical Lagrangian, not from QM). No Born rule input; no $|\Psi|^2$ identification (deferred to A.5); no Schrödinger / Hilbert-space formalism.

**AC-A2.2 (Substrate-native — no Schrödinger / Hilbert-space / projection-postulate language)**: ✓ **PASS**. All quantities ($V(x_n,t)$, $\partial_t \mathbf{A}(x_n,t)$, $V_s$, $V_\eta$, $W(t)$, $\sigma_\eta$, $\gamma_n$, $f_n$) are substrate-physics variables. The V↔$\partial_t \mathbf{A}$ identification (§3.4) uses the AVE-canonical Lagrangian $\mathcal{L}_{AVE}$ (which IS substrate-native — derives from Axioms 1+3 per `vol1/claim-quality.md:734`), NOT borrowed QED Lagrangian. No QM formalism imported.

---

## §4 — What's set up for Phase 2-A.3

Phase 2-A.3 (threshold-crossing first-passage analysis) takes as input:
1. The stochastic field $V(x_n, t) = V_s + V_\eta$ from §2.4
2. The extracted-energy process $W(t; x_n)$ from §3.2
3. The signal/noise decomposition from §3.3

And applies threshold-crossing physics to derive $\Pr[\text{click in }\Delta t \mid V_s(x_n, t)]$.

The Phase 2-A.3 work needs to handle:
- **Detector threshold $E_{th}$**: when does $W(t)$ cross threshold? Standard first-passage problem.
- **Reset dynamics**: after a click, the detector resets after dead time $\tau_d$. Renewal process structure.
- **Markovian-rare-event limit**: in the SNR ≪ 1 regime per cycle but cumulative integration gives detectable signal, the click process becomes Poissonian with rate proportional to signal power (Kramers' formula or analogous first-passage result).

This is standard stochastic-detection theory machinery, applied to the substrate-derived $V$ and $W$ from this phase.

---

## §5 — Honest scope per A47 v18

**What this phase delivered**:
- AVE-native Langevin master equation for the linear-regime master vacuum equation with detector boundary (Step A1)
- Stochastic extracted-energy process $W(t; x_n)$ with explicit signal/noise decomposition (Step A2)
- Both derivations trace to already-canonical AVE content (Vol 3 Ch 11 FDT + master-equation.md + ohmic-decoherence-born.md) — no external postulates imported

**What this phase did NOT do**:
- Derive click probability — that's Phase 2-A.3
- Derive Poissonian limit — that's Phase 2-A.4
- Establish $p = 2$ uniqueness — that's Phase 2-A.4
- Identify $P \equiv |\Psi|^2$ — that's Phase 2-A.5 / KB integration step

**What this phase clarifies for the workstream**:
The substrate machinery is in place. The remaining work (A.3 + A.4) is standard stochastic-detection theory applied to this substrate-derived stochastic field + energy process. The success probability of A.3 + A.4 is now better understood:
- A.3 (first-passage) has a clean stochastic-process setup; ~70% success probability conditional on this phase's outputs
- A.4 (scaling + uniqueness) is standard cumulant-expansion + Gaussian-statistics; ~80% conditional on A.3

Updated end-to-end success probability for Path 2-A: **~55%** (was ~50% pre-A.2; A.2 closing cleanly bumps the estimate modestly because the substrate machinery is in place).

---

## §6 — Honest non-claims for this phase

- This phase does NOT claim to have derived Born rule. Born rule's $|\Psi|^2$ scaling is the A.3 + A.4 + A.5 work; A.2 sets up the substrate machinery.
- This phase does NOT claim the stochastic master equation makes new predictions vs standard QM at the dynamics-level. The Langevin form is what stochastic QM (Itô/Stratonovich on lattice fields) effectively does; AVE's contribution is the substrate-derivation rather than the postulated form.
- This phase does NOT address non-linear regime corrections from the master equation kernel $\sqrt{1-(V/V_{yield})^2}$. Linear regime only.
- This phase does NOT address quantum-coherent (non-thresholded) detectors. Per workstream scope, only Ohmic resistive loads.

---

## §7 — Next session — Phase 2-A.3 scope

**Inputs ready** (from this phase):
- Stochastic master vacuum equation §2.4
- Extracted-energy process $W(t; x_n)$ §3.2
- Signal/noise decomposition §3.3

**Phase 2-A.3 goal**: derive $\Pr[\text{click in }\Delta t \mid V_s(x_n,t)]$ via threshold-crossing first-passage analysis. Apply Kramers' rate formula or analogous first-passage result to the stochastic $W(t)$ process; show that in the rare-event Markovian limit, click rate is Poissonian with rate proportional to signal power.

**Skills to fire for A.3** (per workstream prereg §7):
- substrate-native-check ✓ (threshold defined in substrate-energy terms — relate to $V_{yield}$ structure or external detector parameter)
- ave-independence-check ✓ CRITICAL (first-passage math must not assume Born-rule-like statistics)
- phase-space-coordinate-check ✓ (substrate-energy real-space vs stochastic-process space vs measurement-outcome space — three distinct, all three active in A.3)
- ave-evidence-framing-discipline ✓ continuous

**Estimated effort**: 3-4 hours of focused stochastic-process derivation.

---

*Phase 2-A.2 result doc written 2026-05-26. Per A47 v11b: this result reports against the frozen acceptance criteria from workstream prereg §4.2. Per Rule 12: future amendments preserve body via header-update retraction.*
