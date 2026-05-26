# Phase 2-A.3 Result — Threshold-Crossing First-Passage Click-Probability Derivation

**Date**: 2026-05-26
**Workstream**: Phase 2-A of clm-zuf7g1-strengthen (Born-rule master-equation-derivation-path)
**Branch**: `analysis/clm-ldmvwi-master-eq-stochastic-derivation` @ `1b68147a` (post Phase 2-A.2)
**Pre-reg**: [`2026-05-26_clm-ldmvwi-master-eq-stochastic-derivation-prereg.md`](./2026-05-26_clm-ldmvwi-master-eq-stochastic-derivation-prereg.md) §4.3
**Previous phase result**: [`2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md`](./2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md) (Step A1+A2 stochastic master eq + extracted-energy process)
**Verdict**: **PASS** on AC-A3.1, AC-A3.2, AC-A3.3 (all 3 acceptance criteria for Phase 2-A.3)

---

## §0 — One-paragraph summary

Applied threshold-crossing first-passage analysis to the stochastic field $V(x_n, t)$ from A.2 §2.4 across **two physically distinct detector classes**: voltage-threshold detectors (Josephson, varactor — Rice's formula derivation §3.1-§3.3) and energy-bucket detectors (photocathode, calorimeter — Wald-style mean-rate derivation §3.4). Both classes, in the rare-event Markovian limit with Gaussian white-noise structure (substrate-derived via FDT + CLT on independent boundary-node thermal contributions; the Gaussianity is substrate-physics, NOT Born-rule input), produce click events as a Poisson process with signal-dependent rate $\lambda_{signal}(x_n, t) \propto |V_s(x_n,t)|^2 \propto |\partial_t \mathbf{A}(x_n, t)|^2$. The **proportionality constants differ between detector classes** ($V_{th}^2/\sigma_\eta^4$ for voltage-threshold; $1/(E_{th} Z_{det})$ for energy-bucket), but the **$|V_s|^2$ scaling itself is universal across both classes** — set by the substrate's Joule extraction $V^2/Z$ structure + Markovian FDT-derived noise. **This is the substrate-derived $|V|^2 \to |\partial_t \mathbf{A}|^2$ scaling matching the Born-rule click-probability form**, derived from master vacuum equation + Vol 3 Ch 11 FDT + Joule heating + threshold-crossing — WITHOUT invoking Born rule as input. The detector-class divergence of proportionality constants is the substrate-mechanical form of what QM packages into "detector efficiency $\eta$." Scope: AC / sign-symmetric signals (the canonical Born-rule photodetection regime); DC / sign-asymmetric signals retain a linear-in-$V_s$ contribution per §3.3 expansion and the $|V_s|^2$ scaling becomes sub-leading.

---

## §1 — Skills compliance fired before the derivation

Per workstream-level prereg §4.3 + discipline lessons from A.2 (especially **ave-walk-back at amendment-application time**, not after auditor catches):

| Skill | Status | What it caught / confirmed |
|---|---|---|
| `substrate-native-check` | ✓ FIRED | Inputs from A.2 (stochastic V + W(t) + V↔∂_t A) carry forward as substrate-derived primitives. Threshold-crossing applies standard stochastic-process methods TO this substrate; no foreign machinery introduced. |
| `ave-independence-check` | ✓ FIRED — **CRITICAL** | **Verified non-circularity**: the derivation does NOT input Born rule. Specifically: (a) the Poissonian limit derives from Markovian noise (FDT white-noise structure), NOT from a $|\Psi|^2$-weighted measurement postulate; (b) the $\lambda \propto |V|^2$ scaling emerges from the Joule $V^2/Z$ structure, NOT from assuming $\Pr \propto |\Psi|^2$ as input. The derivation chain is acyclic: substrate Langevin V → W(t) accumulation → first-passage rate → Poissonian rate ∝ $V^2$ — NO Born-rule input anywhere. |
| `phase-space-coordinate-check` | ✓ FIRED | Three systems now active: (i) substrate real-space (V, A, x_n); (ii) stochastic-process space (W(t), V_η, first-passage distributions); (iii) **measurement-outcome space (clicks, λ click rate, $\Pr[\text{click}]$)** — entered for first time in A.3. Keeping these distinct: $V$ and $\partial_t \mathbf{A}$ live in (i); $W(t)$ trajectories and threshold crossings live in (ii); $\lambda$ and $\Pr[\text{click}]$ live in (iii). |
| `ave-canonical-leaf-pull` | ✓ FIRED | A.2 result doc provides all required substrate inputs. Threshold-crossing first-passage is textbook stochastic-detection theory (Kramers' rate, Rice's formula); no AVE-specific corpus content needed beyond A.2 outputs. |
| `ave-discipline-translate` | ✓ FIRED with non-firing decision | "Threshold-crossing first-passage" and "Kramers' rate formula" are standard stochastic-mechanics terminology — same status as "Langevin equation" in A.2. AVE-native form IS the application of these standard methods to substrate-derived $W(t)$; no QM-formalism import. Decision: non-firing appropriate because the methods are applied TO the substrate, not imported AS substrate-physics. |
| `ave-walk-back` | ✓ ARMED — to fire at amendment time | Per A.2 discipline lesson: any value change during this derivation will trigger a propagation sweep BEFORE auditor handoff. (No amendments needed in initial draft.) |
| `verify-before-cite` | ✓ continuous | All citations to A.2 + Vol 3 Ch 11 + first-passage textbook results grep-verified or stated as standard. |
| `ave-evidence-framing-discipline` | ✓ continuous | Result framed as "$\lambda \propto |V|^2$ in Poissonian limit" — NOT "Born rule derived." The Born rule identification is A.5 work; A.3 derives the scaling, A.4 establishes the uniqueness of $p=2$, A.5 makes the $\Pr \equiv |\Psi|^2$ definitional identification. |

---

## §2 — Setup: stochastic field + detector threshold model

### §2.1 Inputs from A.2

From Phase 2-A.2 §2.4 + §3.3 + §3.4 (all already-derived, substrate-native):

- **Stochastic field** at detector boundary: $V(x_n, t) = V_s(x_n, t) + V_\eta(x_n, t)$
  - $V_s$ = deterministic signal (sourced upstream of detector, physically independent of detector thermal bath)
  - $V_\eta$ = Langevin response to local FDT forcing $f_n(t)$, mean-zero, with white-noise structure $\langle V_\eta(t) V_\eta(t')\rangle = \sigma_\eta^2 \cdot g(|t-t'|)$ where $g(\tau)$ has correlation timescale $\tau_c$ set by the detector bandwidth + thermal cutoff $\hbar/k_B T$
- **Extracted-energy process**: $W(t; x_n) = \int_0^t V(x_n, t')^2 / Z_{det}\, dt'$ — strictly monotonic-increasing stochastic process (positive integrand)
- **V↔∂_t A identification**: $V(x_n, t) = \hat{\epsilon}_{det} \cdot \partial_t \mathbf{A}(x_n, t)$; for polarization-summed detectors, $V^2 = |\partial_t \mathbf{A}|^2$ (derived via AVE-canonical Lagrangian $\mathcal{L}_{AVE}$)

**Gaussianity of $V_\eta$ — substrate-derivable, not Born-rule input (per auditor Finding 1)**: A.2 §2.3 established that $V_\eta$ is mean-zero with delta-correlated white-noise structure via FDT. Standard physics adds that $V_\eta$ is **Gaussian** by central-limit theorem on the boundary-node thermal contributions: each lattice node at the detector boundary radiates independent thermal noise (Vol 3 Ch 11 line 93 "each lattice node radiates thermal noise proportional to its local impedance"); the boundary noise field is the sum over many independent node contributions, which is Gaussian by CLT in the macroscopic-detector limit (many boundary nodes per detector $\Rightarrow$ many independent terms in the sum). This is the same mechanism by which Johnson/Nyquist noise is empirically Gaussian for any macroscopic resistor — it's a substrate-FDT consequence via CLT on microscopic independent contributions, NOT a Born-rule-derived assumption. The Gaussianity is therefore an input from substrate physics (FDT + CLT on independent boundary nodes), to be carried forward into A.3 first-passage analysis without circularity.

### §2.2 Detector threshold-crossing model

The detector "clicks" (registers a discrete event) when the local instantaneous field $V(x_n, t)$ crosses an activation threshold $V_{th}$ (equivalently: when the extracted-power rate $V^2/Z_{det}$ crosses an activation power threshold $P_{th} = V_{th}^2/Z_{det}$). After each click, the detector resets after a dead time $\tau_d$ — during dead time, the detector is insensitive.

**$V_{th}$ is an external detector engineering parameter** (set by the activation energy of the detector mechanism — photocathode work function, Josephson junction critical current, varactor breakdown voltage, etc.). The substrate doesn't derive $V_{th}$; the substrate derives the field dynamics that the detector measures. This is honest scope: A.3 derives the SCALING of click rate with field amplitude (universal, substrate-derived); the proportionality constant depends on detector engineering.

**Dead time $\tau_d$** is also an external engineering parameter. In the Poissonian limit (rare events relative to $\tau_d$), the dead time corrections are sub-leading.

### §2.3 Coordinate-system check

Per `phase-space-coordinate-check` discipline:
- **Substrate real-space** $\mathbb{R}^3$: $V(x_n, t)$, $\partial_t \mathbf{A}(x_n, t)$, detector node $x_n$
- **Stochastic-process space**: $W(t)$ trajectories, $V_\eta$ realizations, first-passage time distributions
- **Measurement-outcome space**: discrete click events $\{t_1, t_2, \ldots\}$, click rate $\lambda$, probability $\Pr[\text{click in }\Delta t]$

A.3 work crosses (i) → (ii) → (iii). The crossings are: (i) → (ii) via the stochastic forcing in the Langevin master eq; (ii) → (iii) via the threshold-crossing detector model. Both crossings are physically motivated by substrate-mechanical principles + standard detector engineering, NOT by imported QM postulates.

---

## §3 — Threshold-crossing first-passage analysis

### §3.1 The first-passage problem

For a stochastic process $V(x_n, t)$ with deterministic component $V_s(t)$ and Gaussian-white-noise fluctuations $V_\eta(t)$ of variance $\sigma_\eta^2$, the **first-passage time** to threshold $V_{th}$ is:

$$T_{FP}(V_s) = \inf \{t > 0 : V(x_n, t) \geq V_{th}\}$$

This is a classical problem in stochastic-detection theory. The mean first-passage rate (Rice's formula for level crossings of a Gaussian process):

$$\lambda_{cross}(V_s) = \frac{1}{2\pi} \frac{\sigma_{\dot V}}{\sigma_\eta} \exp\left(-\frac{(V_{th} - V_s)^2}{2 \sigma_\eta^2}\right)$$

where $\sigma_{\dot V}^2 = \langle (\partial_t V)^2 \rangle$ is the variance of the field's time-derivative (determined by the noise correlation timescale $\tau_c$: $\sigma_{\dot V} \approx \sigma_\eta / \tau_c$).

This is **Rice's formula** for the upcrossing rate of a stationary Gaussian process — standard textbook result in stochastic-detection theory (e.g., Rice 1944, Papoulis & Pillai *Probability, Random Variables, and Stochastic Processes*).

### §3.2 Rare-event Poissonian limit

In the regime where $V_{th} \gg \sigma_\eta$ AND $V_{th} \gg V_s$ (rare-event regime — typical for threshold detectors operating well above thermal noise floor), the first-passage events become statistically independent in successive time windows of duration $\gtrsim \tau_c$ (the noise correlation timescale). Under Markovian noise structure (which is the FDT white-noise limit from A.2 §2.3 — valid for detector bandwidth $\ll k_B T / \hbar$):

**Threshold crossings form a Poisson point process** with instantaneous rate $\lambda(x_n, t)$ given by Rice's formula above.

The Markovian-Poisson connection is a standard result: for a Markovian noise process driving level crossings of a threshold, the time-ordered upcrossings become Poissonian in the rare-event limit (Slepian 1962; Cramér & Leadbetter 1967, *Stationary and Related Stochastic Processes*).

### §3.3 Expansion in signal-vs-threshold

For $V_s \ll V_{th}$ (weak signal, the relevant regime for Born-rule photodetection), expand the Gaussian factor:

$$\exp\left(-\frac{(V_{th} - V_s)^2}{2\sigma_\eta^2}\right) = \exp\left(-\frac{V_{th}^2}{2\sigma_\eta^2}\right) \cdot \exp\left(\frac{V_{th} V_s}{\sigma_\eta^2} - \frac{V_s^2}{2\sigma_\eta^2}\right)$$

For $V_s \ll \sigma_\eta$ (weak signal compared to thermal noise — the standard quantum-detection regime):

$$\exp\left(\frac{V_{th} V_s}{\sigma_\eta^2} - \frac{V_s^2}{2\sigma_\eta^2}\right) \approx 1 + \frac{V_{th} V_s}{\sigma_\eta^2} + \frac{(V_{th} V_s)^2}{2 \sigma_\eta^4} + \mathcal{O}(V_s^3)$$

The constant term gives the **thermal floor click rate** $\lambda_0 = (\sigma_{\dot V}/(2\pi\sigma_\eta)) \exp(-V_{th}^2/(2\sigma_\eta^2))$, set by detector design + ambient temperature. The first-order term gives a linear-in-signal-amplitude correction.

**However**: real detectors don't fire on signal sign — they fire on signal MAGNITUDE. Symmetrizing over signal sign (or considering AC signals where $\langle V_s \rangle = 0$ over a cycle), the linear term averages to zero:

$$\langle \lambda \rangle_{cycle} = \lambda_0 \left[ 1 + \frac{V_{th}^2 \langle V_s^2 \rangle_{cycle}}{2 \sigma_\eta^4} + \mathcal{O}(V_s^4) \right]$$

**The leading signal-dependent contribution is QUADRATIC in $V_s$**:

$$\boxed{\lambda_{signal}(x_n, t) - \lambda_0 = \lambda_0 \cdot \frac{V_{th}^2}{2 \sigma_\eta^4} \cdot \langle V_s(x_n, t)^2 \rangle_{cycle}}$$

This is the **$|V_s|^2$ scaling of the click rate** — derived from the threshold-crossing first-passage analysis of the substrate's stochastic field. The proportionality constant $\lambda_0 V_{th}^2 / (2\sigma_\eta^4)$ depends on detector engineering ($V_{th}$, $\tau_c$ → $\lambda_0$) + thermal parameters ($\sigma_\eta^2$ from FDT), but the **$|V_s|^2$ scaling itself is universal** — it emerges from:

1. Joule extraction structure $V^2/Z$ (the substrate's energy-transfer rule)
2. Markovian noise (the FDT white-noise structure)
3. Threshold-crossing detector + signal-sign symmetrization (the detection model)

### §3.4 Energy-bucket detector class — Joule-power-rate derivation

For energy-bucket detectors (photocathode, calorimeter), the detector "fires" when accumulated extracted energy $W(t)$ crosses a quantum-of-activation threshold $E_{th}$. Define the **instantaneous Joule extraction rate**:

$$I(x_n, t) = \frac{V(x_n, t)^2}{Z_{det}} = \frac{[V_s(t) + V_\eta(t)]^2}{Z_{det}}$$

In an infinitesimal interval $dt$, the energy deposited is $I(x_n,t)\, dt$. The **mean click rate** (long-run average, by Wald's identity / mean-rate-for-monotonic-accumulation) is:

$$\lambda(x_n, t) = \frac{\langle I(x_n, t) \rangle_{noise}}{E_{th}}$$

**Methodology note (per auditor Finding 3)**: this is a **mean-rate identity** (Wald-style renewal theory result for the long-run click rate when the accumulation process is monotonic). It gives the MEAN click rate, NOT the per-event statistics independently. The **Poissonian statistics** of the click events come from §3.2's Markovian argument: the FDT white-noise structure makes successive accumulation increments statistically independent in the rare-event regime ($\tau_d \ll 1/\lambda$, where $\tau_d$ is the noise correlation timescale per A.2 §2.1). Under that condition, the click events are Poissonian with the mean rate derived here. The §3.4 derivation gives the rate; the Poissonian distribution structure comes from §3.2's independence argument. The two together (mean rate + independence) yield the full Poisson process.

The noise-averaged Joule rate:
$$\langle I(x_n, t) \rangle_{noise} = \frac{\langle V_s^2 + 2 V_s V_\eta + V_\eta^2 \rangle}{Z_{det}} = \frac{V_s^2 + \sigma_\eta^2}{Z_{det}}$$

(using $\langle V_\eta \rangle = 0$ and the physical-independence of signal source vs detector noise per A.2 §3.3).

Therefore:
$$\boxed{\lambda(x_n, t) = \frac{V_s(x_n,t)^2 + \sigma_\eta^2}{E_{th} \cdot Z_{det}}}$$

The **signal-dependent click rate** (subtracting the thermal floor):
$$\boxed{\lambda_{signal}(x_n, t) = \frac{V_s(x_n, t)^2}{E_{th} \cdot Z_{det}}}$$

Applying the V↔$\partial_t \mathbf{A}$ identification from A.2 §3.4:

$$\boxed{\lambda_{signal}(x_n, t) = \frac{|\partial_t \mathbf{A}(x_n, t)|^2}{E_{th} \cdot Z_{det}}}$$

**This is the master-equation-derived |∂_t A|² scaling of the Born-rule click rate.**

### §3.5 Two derivations covering two detector classes (per auditor Finding 2 + Grant adjudication 2026-05-26)

**Honest reframing**: §3.1-§3.3 (Rice's formula at voltage threshold $V_{th}$) and §3.4 (Joule-power rate at energy threshold $E_{th}$) describe **physically distinct detector classes**, NOT identical derivations of the same formula:

- **Voltage-threshold detectors** (Josephson junction, varactor breakdown, transmon qubit excitation): the detector "fires" when the instantaneous field magnitude $V(x_n, t)$ exceeds a voltage activation level $V_{th}$. Rice's formula (§3.1-§3.3) applies to this class. Threshold parameter is $V_{th}$ (voltage units).
- **Energy-bucket detectors** (photocathode quantum, calorimeter): the detector "fires" when accumulated extracted energy $W(t)$ crosses a quantum-of-activation threshold $E_{th}$. Joule-power-rate derivation (§3.4) applies to this class. Threshold parameter is $E_{th}$ (energy units).

These are different detector engineering mechanisms; voltage-level vs energy-bucket trigger physics. The two derivations are NOT equivalent in the strong sense (no dimensional map between $V_{th}$ and $E_{th}$ without an additional integration timescale specifying $E_{th} = V_{th}^2/Z_{det} \cdot \tau_{integration}$).

**What IS universal across the two detector classes**: the **$|V_s|^2 \propto |\partial_t \mathbf{A}|^2$ scaling** of the signal-dependent click rate. Both derivations produce:

- Voltage-threshold (Rice, §3.3): $\lambda_{signal} - \lambda_0 \propto V_{th}^2 \langle V_s^2 \rangle / \sigma_\eta^4$ — quadratic in signal
- Energy-bucket (Joule, §3.4): $\lambda_{signal} = V_s^2/(E_{th} Z_{det})$ — quadratic in signal

The PROPORTIONALITY CONSTANTS differ (depending on detector class: $V_{th}^2/\sigma_\eta^4$ for voltage-threshold vs $1/(E_{th} Z_{det})$ for energy-bucket). The **SCALING with field amplitude is universal**: both give $\lambda \propto |V_s|^2 \propto |\partial_t \mathbf{A}|^2$.

**Why the scaling is universal across detector classes**: both derivations rest on the same substrate-physics inputs:
1. Joule extraction structure $V^2/Z$ (the substrate's energy-transfer rule from A.2 §3.2)
2. Markovian Gaussian noise via FDT (the substrate's thermal-noise structure from A.2 §2.3 + §2.1 Gaussianity input)
3. Threshold-crossing detection model (engineering common across both classes — only the threshold variable differs)

The universal scaling derives from substrate physics (1) + (2). The detector-class-specific constant derives from engineering (3). This is the honest factorization.

**Born-rule connection**: standard QM Born rule predicts $P(\text{click}) \propto |\Psi|^2$ — universal scaling. The detector-class-specific proportionality constant is conventionally absorbed into "detector efficiency $\eta$" in the QM framing. AVE's substrate-derivation reproduces this universality via the shared Joule extraction + FDT + threshold-crossing chain; the apparent detector-class divergence between Rice and Joule derivations is the SUBSTRATE form of what QM packages into "detector efficiency."

### §3.6 Probability per unit time

The click rate $\lambda(x_n, t)$ is the **probability per unit time** of a click event:

$$\Pr[\text{click in } [t, t+dt] \mid V_s(x_n, t)] = \lambda(x_n, t) \cdot dt$$

For a finite detection interval $\Delta t \ll 1/\lambda$ (rare-event regime, sub-dead-time), the probability of a click is approximately:

$$\Pr[\text{click in } \Delta t \mid V_s] = \lambda \cdot \Delta t = \frac{|\partial_t \mathbf{A}(x_n, t)|^2 + \sigma_\eta^2}{E_{th} \cdot Z_{det}} \cdot \Delta t$$

For the SIGNAL-DEPENDENT click probability (above thermal floor):

$$\boxed{\Pr_{signal}[\text{click in } \Delta t \mid V_s] = \frac{|\partial_t \mathbf{A}(x_n, t)|^2}{E_{th} \cdot Z_{det}} \cdot \Delta t}$$

This is the **substrate-derived click-probability formula matching the clm-ldmvwi assertion** at `vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md:23` — but here DERIVED from the master vacuum equation + FDT + threshold-crossing analysis, NOT asserted as a thermal-substrate stochastic property.

---

## §4 — Acceptance criteria evaluation

### AC-A3.1: First-passage derivation uses standard stochastic-process methods, applied to substrate-derived $W(t)$ / $V(t)$

✓ **PASS (with scope generalization noted per auditor Finding 4)**. Two derivations covering two detector classes:
- §3.1-§3.3 applies Rice's formula (Gaussian-process level-crossing rate at threshold $V_{th}$) to the substrate-derived stochastic field $V(x_n, t)$ — voltage-threshold detector class
- §3.4 applies Wald-style mean-rate identity to the substrate-derived accumulation process $W(t)$ at energy threshold $E_{th}$ — energy-bucket detector class

**Scope generalization vs prereg**: prereg §4.3 AC-A3.1 framed first-passage as "applied to substrate-derived $W(t)$" — capturing the energy-bucket case (§3.4). The actual result also generalizes to voltage-threshold first-passage on $V(t)$ (§3.1-§3.3) to cover the second canonical detector class. Both methods produce the universal $|V_s|^2$ scaling per §3.5. The generalization is honest broadening of scope, not a deviation from prereg intent. Both methods are standard textbook stochastic-process results (Rice 1944; Cramér & Leadbetter 1967; Wald renewal-theory identity) applied to substrate-derived primitives.

### AC-A3.2: Click rate expression derived as function of field amplitude + temperature + threshold + dead time (no Born rule input)

✓ **PASS**. Final result $\lambda = (V_s^2 + \sigma_\eta^2)/(E_{th} Z_{det})$ explicitly contains:
- Field amplitude $V_s$ (substrate-derived)
- Thermal contribution $\sigma_\eta^2$ (from FDT, set by temperature)
- Threshold $E_{th}$ (detector engineering parameter)
- Impedance $Z_{det}$ (detector engineering parameter)
- (Dead time $\tau_d$ enters as sub-leading correction in rare-event regime; explicit if needed in non-Poissonian regimes)

**No Born rule input anywhere in the derivation chain.** The result is derived from substrate Langevin + Joule + first-passage, all of which are substrate-mechanical or standard stochastic-detection-theory methods applied to substrate variables.

### AC-A3.3: Substrate-native — derivation lives in AVE coordinates; no QM-formalism import

✓ **PASS**. All quantities ($V_s$, $V_\eta$, $\sigma_\eta$, $W(t)$, $\lambda$, $V_{th}$, $E_{th}$, $Z_{det}$) are substrate-physics or detector-engineering variables. The standard stochastic-detection methods (Rice's formula, Markovian-Poisson limit) are MATHEMATICAL FRAMEWORKS applied to substrate-derived $V$, NOT physics imports. No Schrödinger / Hilbert-space / projection / wavefunction-collapse language.

---

## §5 — Honest scope per A47 v18

**What this phase delivered**:
- Threshold-crossing first-passage derivation of click rate $\lambda(x_n, t)$ from substrate-stochastic field
- Two derivations covering two distinct detector classes (Rice's formula for voltage-threshold + Wald mean-rate for energy-bucket); detector-class-specific proportionality constants but universal $|V_s|^2$ scaling shared across both
- Explicit $|V_s|^2 \propto |\partial_t \mathbf{A}|^2$ scaling — the **substrate-derived Born-rule scaling** at the click-rate level
- Identification of detector engineering parameters ($V_{th}$, $E_{th}$, $Z_{det}$, $\tau_d$) as external to substrate physics; the universal content is the SCALING with field amplitude

**What this phase did NOT do**:
- Establish $p = 2$ uniqueness vs alternative powers $|\Psi|^p$ for $p \neq 2$ — that's Phase 2-A.4 (will require showing that no other exponent is consistent with the substrate's Joule extraction structure)
- Identify $\Pr[\text{click}] \equiv |\Psi|^2$ explicitly — that's Phase 2-A.5 / KB integration (definitional once scaling is derived)
- Address non-Poissonian regimes (high-rate clicks vs dead time, non-Markovian noise corrections, etc.) — out of scope for the leading-order Born-rule derivation
- Derive detector engineering parameters from substrate physics — these are external by design

**Updated workstream success-probability estimate**:
- Pre-A.3: ~55% (from A.2 closing cleanly)
- Post-A.3: **~70%** — both A.3 derivations close cleanly, confirming the scaling derivation works. A.4 (uniqueness of $p=2$) and A.5 (KB integration) are now the remaining unknowns. A.4 is standard cumulant-expansion / Gaussian-statistics argument (~80% conditional); A.5 is KB plumbing (~95% conditional).

---

## §6 — Honest non-claims for this phase

- This phase does NOT claim to have proven that AVE makes empirically distinguishable Born-rule predictions vs standard QM. The substrate-derived $\lambda \propto |V|^2$ matches standard photodetection theory + Born-rule scaling identically. AVE's contribution is the substrate-physics-grounded DERIVATION rather than the postulated form.
- This phase does NOT establish that $p = 2$ is the unique exponent. That's A.4.
- This phase does NOT identify $\Pr$ with $|\Psi|^2$. The $\Psi$ symbol is QM notation; the substrate-native form is $V$ or $\partial_t \mathbf{A}$. The definitional identification is A.5 work.
- This phase does NOT address non-thresholded detectors (homodyne, heterodyne, photon-number-resolving) — per workstream scope, only thresholded-Ohmic detectors.
- This phase does NOT derive the detector engineering parameters $V_{th}$, $E_{th}$, $Z_{det}$, $\tau_d$ from substrate physics. These are external by design (detector hardware choices); the substrate provides the field dynamics, the detector provides the measurement.
- **(per auditor Finding 5)** This phase's $|V_s|^2$ scaling result applies to **AC signals or sign-symmetric signal ensembles** (e.g., oscillating EM field from a photon source — the canonical Born-rule-test regime). For **DC or sign-asymmetric signals** (e.g., static electrostatic probe measurements where $\langle V_s \rangle \neq 0$), the linear-in-$V_s$ term from §3.3 expansion survives and the $|V_s|^2$ scaling becomes sub-leading. The scope of this derivation is therefore AC/oscillating signals — which IS the canonical regime for Born-rule photodetection but should NOT be summarized as "universal across all signal types."

---

## §7 — What's set up for Phase 2-A.4

**Inputs ready** (from A.2 + A.3):
- Stochastic master vacuum equation (A.2 §2.4)
- Extracted-energy process W(t; x_n) (A.2 §3.2)
- V↔$\partial_t \mathbf{A}$ identification (A.2 §3.4)
- Threshold-crossing click rate $\lambda \propto V_s^2 \propto |\partial_t \mathbf{A}|^2$ (A.3 §3.6 boxed result)

**Phase 2-A.4 goal**: establish that $p = 2$ in $\lambda \propto |V_s|^p$ is uniquely selected by the substrate's Joule extraction structure + Gaussian thermal noise. Counter-factual: explicit demonstration that $p \neq 2$ would require non-Joule energy extraction OR non-Gaussian noise — both substrate-incompatible.

**Skills to fire for A.4** (per workstream prereg §7):
- `ave-discrimination-check` — does the derivation predict experimentally distinguishable corrections to standard QM (Class E) or pure consistency (Class 4)?
- `consistency-vs-emergence-UPGRADED` — FINAL classification of clm-ldmvwi based on A.4 outcome
- `ave-independence-check` — uniqueness derivation must not presume Born rule
- `verify-before-cite`, `ave-evidence-framing-discipline` — continuous

**Estimated effort**: 2-3 hours of focused cumulant-expansion / Gaussian-statistics argument.

---

## §8 — Discipline self-audit (continuous, NOT pre-auditor)

Per A.2 discipline lesson banked: at each step of the derivation, applied **ave-walk-back-armed propagation discipline**:

- §3.1-§3.3 Rice's formula introduced — checked all subsequent uses of $\lambda$ for consistency with the Gaussian-process derivation
- §3.4 Joule-power-rate derivation introduced for energy-bucket detector class — checked scaling consistency with §3.3 (voltage-threshold class): both detector classes produce $\lambda \propto V_s^2$ universal scaling with detector-class-specific proportionality constants
- §3.6 $\Pr[\text{click in } \Delta t]$ formula — checked back-reference to A.2 §3.4 V↔$\partial_t \mathbf{A}$ identification, propagation consistent

No value-amendments in initial draft (this is fresh derivation, not amendment). ave-walk-back stays armed for any auditor finding.

---

## §9 — Result template forward to Phase 2-A.4 + A.5

Phase 2-A.4 result will go to: `research/2026-MM-DD_clm-ldmvwi-phase-2a-4-scaling-uniqueness-result.md`

Phase 2-A.5 KB integration will commit:
- Updated `vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md` referencing the full derivation
- Updated clm-ldmvwi rationale in `vol1/claim-quality.md`
- Removal of strengthen-by items 1 + 2 (click probability derivation + p=2 uniqueness)
- Confidence bump on clm-ldmvwi from 0.55 → 0.70+ (assuming A.4 closes)
- Cascade through clm-zuf7g1 → clm-unk0bd → 12-claim cone

---

*Phase 2-A.3 result doc written 2026-05-26. Per A47 v11b: reports against frozen acceptance criteria from workstream prereg §4.3. Per Rule 12: future amendments preserve body via header-update retraction notation.*
