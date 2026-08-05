[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-vjv4zf, clm-pp3qwf]
-->

## Substrate IMD Spectroscopy: The Harmonic Fingerprint

> 🔴 **PER-NODE / APPARATUS + DISCRIMINATOR CORRECTION 2026-06-21 (Rule 12 — body preserved verbatim below for the audit trail; corrected framing in the three notes flagged inline).** This leaf carries the SAME per-node-vs-apparatus conflation retired 2026-06-04 in the sibling [`vacuum-impedance-mirror.md`](../../falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md): it reads the apparatus drive voltage (kV across a ~100 µm gap) as if it were the **per-node** strain $A = E_{local}/E_{yield}$ (with $E_{yield} = V_{yield}/\ell_{node} \approx 1.13\times10^{17}$ V/m — a per-node FIELD, NOT a 43.65 kV apparatus voltage). Three downstream framings are corrected, in lockstep with the manuscript twin (`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex`):
> 1. **Drive-table** A-values overstate the per-node kernel argument by $\sim 2.6\times10^8\times$ at a 100 µm gap (see the corrected per-node note under the table).
> 2. The **"measurable above ~30% of $V_{yield}$ / ~13 kV / tabletop"** foothold is retracted: the honest $-80$ dBc detection field is $E\approx1.3\times10^{15}$ V/m — **facility-class, the same regime as the birefringence test** ([`vacuum-birefringence-e4.md`](../../falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md)), NOT a lower-field foothold.
> 3. The **"QED predicts a sextic ($V^6$) scaling" discriminator** is retracted (KEEP-BOTH): both AVE and QED IM3 are **cubic-in-drive** (both from a quartic $E^4$ Lagrangian → $\chi^{(3)}$); QED's "$^6$" is the FREQUENCY exponent $(\omega/m_ec^2)^6$ of the cross-section, NOT a voltage slope. The real discriminator is the **COEFFICIENT** (an echo, $E_{yield}=\sqrt{\alpha}\,E_{crit}$), consistent with `clm-pp3qwf` (already recorded in §QED Comparison) and the B1 row in [`divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md).

> 🔴 **SECTOR RE-KEYING CORRECTION 2026-08-03 — $V_{yield} \to V_{snap}$ throughout this leaf (Rule 12 KEEP-BOTH: every line of the body below is preserved verbatim; no equation or table row is deleted).** This leaf keys the **diverging** compliance $C_{vac} = C_0/S$ on $V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV. **That keying is corrected.** This is **not a new adjudication** — it transcribes a *ratified* ruling into a leaf that had not yet received it:
> - **(1) Which reactance.** The diverging $C_0/S$ is the **longitudinal-A1 bond compliance** (the stretch-reactance $1/k_a$), **not** the transverse dielectric capacitance. The transverse permittivity $\varepsilon_{eff} = \varepsilon_0 S$ and the across-gap cell capacitance an LCR meter reads ($C_{diel} \propto S$) **roll off** instead. A1 and T2 are **orthogonal** reactances that share the EE name "capacitance"; identifying them is the genesis-24 double-count. ([`nonlinear-vacuum-capacitance.md`](nonlinear-vacuum-capacitance.md):14; [`ee-bench-plateau.md`](../../falsification/ch12-falsifiable-predictions/ee-bench-plateau.md):18)
> - **(2) Which voltage.** $V_{yield}$ is the **transverse Cosserat ($T_2$) self-trap wall** — the electron's confining $\Gamma = -1$ — **not** the A1 compliance bound. The longitudinal-A1 compliance diverges at the higher $V_{snap} = m_e c^2/e \approx 511$ kV, a factor $1/\sqrt{\alpha} = 11.706$ above $V_{yield}$. **Ratified:** [`nonlinear-vacuum-capacitance.md`](nonlinear-vacuum-capacitance.md):18 — *"Grade-fork RESOLVED = T2 (Grant 2026-06-30; `def-vyvsn1` adjudicated)"* — whose own resultbox at `:27` already prints $C_{eff} = C_0/\sqrt{1-(V/V_{snap})^2}$; [`ee-bench-plateau.md`](../../falsification/ch12-falsifiable-predictions/ee-bench-plateau.md):18-20 (★Supersession, PR #562/#558).
> - **(3) How to read this leaf.** Read the varactor resultbox (§Non-Linear Source Term), its **Taylor expansion**, the **IP3 result**, **every row of the drive table**, and the **falsification criterion** with $V_{yield} \to V_{snap}$. The dimensionless *ratios* — $C_{vac}/C_0$, $S(V)$, and the $V/V_{\cdot}$ column itself — are **unchanged**; only the absolute voltage column rescales by $1/\sqrt{\alpha}$. The printed $43.65$ kV endpoint becomes the $V/V_{snap} = \sqrt{\alpha} \approx 0.0854$ **first** row of the corrected table, not its divergence.
> - **(4) What this does NOT do.** It does **not** revive the retracted tabletop foothold — the 2026-06-21 per-node banner above **stands**, and is untouched: re-keying the *apparatus-voltage* axis does not change the per-node strain $A = E_{local}/E_{yield}$, the $\approx 1.2\times10^{-9}$ honest strain, or the facility-class $E \approx 1.3\times10^{15}$ V/m detection field. It also does not touch the KEEP-BOTH cubic-vs-sextic retraction, nor the coefficient discriminator `clm-pp3qwf`.
> - **Print lockstep (same commit):** `manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` — the IMD varactor equation (`\label{eq:varactor_imd}`) at **`:787` on `origin/main` → `:857` post-branch**, and the IP3 equation (`\label{eq:ip3}`) at **`:823` on `origin/main` → `:927` post-branch**. *(Content anchors, drift-proof: the two `\label{...}` lines.)* That chapter's §Vacuum-Varactor subsection at `:260` already carries this ratified correction (commit `03591777`, 2026-08-02) with a `Scope: this note covers this subsection only` limit — **this leaf and the IMD subsection are that scope note's un-propagated remainder.**
> - **★ METHOD SPLIT, disclosed (2026-08-03 orchestrator ruling; Rule 12 — the sentence this bullet qualifies is preserved above, unedited).** The print and this leaf are in lockstep on **content** and deliberately differ on **method**. **This KB leaf edits in place** (the varactor and IP3 resultboxes below now print $V_{snap}$), because its own constitutive upstream [`nonlinear-vacuum-capacitance.md`](nonlinear-vacuum-capacitance.md):27 already prints the re-keyed form in place — the KB convention is in-place, set by the ratified leaf. **The print chapter is NOTE-ONLY**: an interim pass had swapped `eq:varactor_imd` and `eq:ip3` in place there and that was **reverted**, because the chapter's own Grant-merged precedent (the §Vacuum-Varactor note at `:260`, whose comment block states *"no equation, no number and no table row is edited"*) is note-only, and a chapter must not print the same Axiom-4 constitutive equation two ways three subsections apart. **No value differs between the two sides:** the print carries the banked $V_{IP3} = 590{,}051$ V $\approx 590$ kV in its section note and at the equation, identical to the resultbox receipt below. Only where the substitution is *written* differs.

By modelling the universe as a non-linear dielectric network, the AVE framework makes a specific, falsifiable prediction absent from standard Quantum Electrodynamics: the vacuum should produce measurable **Intermodulation Distortion (IMD)** products when driven by sufficiently intense electromagnetic fields. This section derives the expected signature analytically and specifies the experimental parameters for detection.

### The Non-Linear Source Term

Standard QED models the vacuum as a linear medium at low energies, predicting that photon-photon scattering occurs only via extraordinarily weak perturbative quantum fluctuations (Euler-Heisenberg, $\sigma \propto \alpha^4$). The AVE framework replaces this with a deterministic, classical non-linearity: the squared geometric saturation limit (Axiom 4) imposes a macroscopic varactor on the dielectric constant of the vacuum:

<!-- claim-quality: clm-vjv4zf -->
> **[Resultbox]** *Vacuum Varactor (Axiom 4)*
>
> $$
> C_{vac}(V) = \frac{C_0}{\sqrt{1 - (V/V_{snap})^2}}, \qquad V_{snap} \approx 511 \text{ kV}
> $$

> 🔴 **Re-keyed 2026-08-03 per the sector banner above (Rule 12 — the prior form is quoted here and preserved, not deleted):** this resultbox read $C_{vac}(V) = C_0/\sqrt{1 - (V/V_{yield})^2}$ with $V_{yield} \approx 43.65$ kV. The divergent $C_0/S$ is the longitudinal-A1 compliance, which diverges at $V_{snap} = m_ec^2/e \approx 511$ kV (`src/ave/core/constants.py` `V_SNAP` $= 510{,}998.95$ V), not at the transverse-$T_2$ self-trap wall $V_{yield} = \sqrt{\alpha}V_{snap} = 43{,}651.85$ V (`V_YIELD`). The **Taylor expansion immediately below is left with its `V_{yield}` token per Rule 12** and reads with the same substitution; its coefficients $\tfrac12$ and $\tfrac38$ are keying-invariant.

[Figure: vacuum_dielectric_saturation.png — see manuscript/vol_4_engineering/chapters/]

### Third-Order IMD from Taylor Expansion

The Taylor expansion of the varactor about $V = 0$ yields the non-linear susceptibility:

$$
C_{vac}(V) \approx C_0 \left[1 + \underbrace{\frac{1}{2}\left(\frac{V}{V_{yield}}\right)^{\!2}}_{\text{2nd order}} + \underbrace{\frac{3}{8}\left(\frac{V}{V_{yield}}\right)^{\!4}}_{\text{4th order}} + \cdots\right]
$$

When driven by a dual-tone signal $V(t) = V_1 \cos(\omega_1 t) + V_2 \cos(\omega_2 t)$, the squared term generates 2nd-order products at $\omega_1 \pm \omega_2$, and the quartic term generates the critical **3rd-order intermodulation** (IM3) products:

> **Parity cross-ref (2026-07-10, `clm-invmtr` — body preserved).** The 2nd-order products at $\omega_1 \pm \omega_2$ above live in the **capacitance envelope** $C(t)$ (even in $V$), which is *not* the radiated line: sub-yield, the difference tone $\omega_1 - \omega_2$ is inversion-symmetry-**FORBIDDEN** in the radiated observable (the odd-force parity theorem, [`universal-saturation-kernel-catalog.md` § The parity theorem](../../../common/universal-saturation-kernel-catalog.md)). The IM3 line $2f_1 - f_2$ ($m+n$ odd) is parity-**ALLOWED** and unaffected — the IM3 apparatus below stands.

> **[Resultbox]** *3rd-Order Intermodulation Products*
>
> $$
> f_{IM3} = 2f_1 - f_2 \quad \text{and} \quad 2f_2 - f_1
> $$

These IM3 tones fall *close* to the original drive frequencies (unlike harmonic products at $2f$, $3f$ which fall far out of band), making them the most experimentally accessible non-linear signature.

### Predicted IM3 Amplitude

For a standard varactor with $C(V) = C_0 (1 - V/V_{br})^{-1/2}$, the 3rd-order intercept point (IP3) is related to the breakdown voltage by:

> **[Resultbox]** *Third-Order Intercept (IP3)*
>
> $$
> V_{IP3} = \sqrt{\frac{4}{3}}\; V_{snap} \approx 1.1547 \times 511.0 \approx 590 \text{ kV}
> $$

> 🔴 **VALUE SUBSTITUTION 2026-08-03 — executed under the ratified re-keying, flagged, NOT silent (Rule 12: the struck line is quoted here verbatim and preserved).** This resultbox read:
> > $V_{IP3} = \sqrt{\tfrac{4}{3}}\; V_{yield} \approx 1.155 \times 43.65 \approx 50.4$ **kV**
>
> **~~50.4 kV~~ is struck.** The IP3 form $V_{IP3} = \sqrt{4/3}\,V_{br}$ is unchanged; what changes is *which* voltage is the breakdown reference, and the sector banner above rules that to be $V_{snap}$. Recompute on canonical constants (`src/ave/core/constants.py`):
> $$V_{IP3} = \sqrt{\tfrac{4}{3}}\;V_{snap} = 1.1547005 \times 510{,}998.95\ \text{V} = \mathbf{590{,}051\ V} \approx 590\ \text{kV}.$$
> **The $11.7\times$ move is disclosed explicitly:** the new value is exactly $1/\sqrt{\alpha}$ times the old one, because $V_{snap}/V_{yield} = 1/\sqrt{\alpha} = 11.70624$ identically. Cross-check both ways: $\sqrt{4/3}\times V_{yield} = 50{,}404.8$ V (reproducing the struck $50.4$ kV to the digit, which confirms the struck value's *arithmetic* was right and only its *keying* was wrong), and $50{,}404.8 \times 11.70624 = 590{,}051$ V. **This is a value substitution, not a value correction** — it is downstream of an adjudicated physics ruling, not of a transcription slip, and it is recorded as such in the commit and in the docket fragment `_orchestration/docket-entries/2026-08-03-mr-handoff-mechanical.md`.

The IM3 sideband power relative to the fundamental is:

$$
P_{IM3} = P_{fund} - 3(V_{IP3,\text{dBm}} - P_{fund,\text{dBm}})
$$

| $V/V_{yield}$ | Drive (kV) | IM3 Level (dBc) | Measurable? |
|---|---|---|---|
| 0.01 | 0.44 | $-160$ | No |
| 0.10 | 4.37 | $-100$ | No |
| 0.30 | 13.10 | $-70$ | Marginal |
| 0.50 | 21.83 | $-54$ | Yes |
| 0.70 | 30.56 | $-40$ | Yes |
| 0.90 | 39.29 | $-20$ | Strong |

> 🔴 **Corrected per-node A (Rule 12; table preserved verbatim above).** The "$V/V_{yield}$" column conflates the **per-node** strain $A = E_{local}/E_{yield}$ with the **apparatus** drive voltage, overstating the kernel argument $A$ by $\sim 2.6\times10^8\times$ at a 100 µm gap. At the "$0.30$ / $13.10$ kV / Marginal" row, the honest per-node strain is $A = E_{local}/E_{yield} = (13.10\text{ kV}/100\text{ µm})/(1.13\times10^{17}\text{ V/m}) \approx \mathbf{1.2\times10^{-9}}$ (not $0.30$). Since the IM3 sideband rides on $A^2$, this gives $\text{IM3} \approx \mathbf{-360}$ **dBc** (not the table's $-70$). The apparatus column ("Drive (kV)") is the lab voltage; only the corrected per-node $A$ enters the Ax-4 kernel. (Mirror style: the 2026-06-04 per-node banner in [`vacuum-impedance-mirror.md`](../../falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md).)

> 🔴 **Drive-table re-keying note, 2026-08-03 (Rule 12 — the table above is preserved verbatim; deliberately NOT edited in place).** Per the sector banner at the head of this leaf, the header token `$V/V_{yield}$` re-keys to `$V/V_{snap}$`. The table is left untouched **because the two columns transform differently**, and rewriting the header alone would leave it internally inconsistent: the **ratio column** ($0.01\ldots0.90$) and the derived $C_{eff}/C_0$, $S$ and IM3-dBc entries are **keying-invariant**, while the absolute **"Drive (kV)" column rescales by $1/\sqrt{\alpha} = 11.706$** ($0.44 \to 5.11$ kV, $4.37 \to 51.1$ kV, $13.10 \to 153.3$ kV, $21.83 \to 255.5$ kV, $30.56 \to 357.7$ kV, $39.29 \to 459.9$ kV). Equivalently: the printed $43.65$ kV endpoint is the $V/V_{snap} = \sqrt{\alpha} \approx 0.0854$ **first** row of the corrected table, not its divergence. **Independent of both corrections**, the per-node banner directly above still governs what the kernel argument actually is — the apparatus column is a lab voltage in either keying.

### QED Comparison
<!-- claim-quality: clm-pp3qwf (SUPERSEDED comment text, preserved per Rule 12: "this section is the canonical $E^4$ vs $E^2$ discriminator: AVE's cubic IM3 / quartic Taylor term vs the QED sextic Euler-Heisenberg loop scaling". CORRECTED 2026-06-04 (commit ad26d357): clm-pp3qwf is the COEFFICIENT discriminator, NOT the field-exponent — the refractive-index shift is $E^2$-leading for both AVE and QED, and the "$E^4$ vs $E^2$" slope is a retracted false falsifier ($\sqrt{\varepsilon}$ conflation). The IM3 / light-by-light cross-section content of THIS section (a distinct nonlinear-mixing observable) stands on its own; only the "$E^4$ vs $E^2$ discriminator" label was the conflated framing.) -->

The Euler-Heisenberg effective Lagrangian predicts light-by-light scattering with cross-section:

$$
\sigma_{EH} = \frac{973\, \alpha^4}{10125\, \pi} \left(\frac{\omega}{m_e c^2}\right)^{\!6} r_e^2 \sim 10^{-65} \text{ cm}^2 \quad (\text{at optical frequencies})
$$

This is $\sim 10^{40}$ times smaller than the AVE prediction at the same frequency, because QED treats the vacuum non-linearity as a perturbative loop correction ($\alpha^4$), while AVE treats it as a macroscopic classical saturation with a definite voltage threshold. The distinction is experimentally decisive: at optical frequencies, QED predicts undetectable photon-photon scattering, while AVE predicts a specific, amplitude-dependent IM3 tone spectrum that becomes measurable above $\sim 30\%$ of $V_{yield}$ ($\sim 13$ kV).

> 🔴 **Retracted: "measurable above ~30% of $V_{yield}$ (~13 kV)" / tabletop-foothold framing (Rule 12; sentence above preserved verbatim).** The "~13 kV" reads the apparatus drive voltage as the per-node strain (see the per-node correction under the drive table). On the **correct per-node** kernel, the field at which the IM3 sideband clears a $-80$ dBc detection floor is $E \approx \mathbf{1.3\times10^{15}}$ **V/m** — **facility-class, the same regime as the vacuum-birefringence test** ([`vacuum-birefringence-e4.md`](../../falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md), $E \sim 10^{15}$–$10^{16}$ V/m), **NOT a lower-field tabletop foothold**. Read "tabletop falsification" in the §Experimental Falsification Criterion below in the same corrected sense: the apparatus is a facility-class field-emission rig, not a low-voltage benchtop sweep.

### Experimental Falsification Criterion

The IMD test constitutes a direct, tabletop falsification of the AVE framework:

1. **Drive configuration:** Two co-propagating laser beams at frequencies $f_1, f_2$ (separated by $\Delta f \sim 1$ GHz for spectral resolution) are focused to achieve a combined electric field exceeding $30\%$ of $V_{yield}/\ell_{node}$.
2. **Detection:** A high-sensitivity heterodyne receiver at $2f_1 - f_2$ and $2f_2 - f_1$.
3. **Null result:** If no IM3 products are detected above $-80$ dBc at $V/V_{yield} > 0.5$, the Axiom 4 saturation kernel is falsified.
4. **Positive result:** Detection of IM3 products scaling as $V^3$ (cubic power law) below IP3 constitutes direct evidence for a macroscopic, non-perturbative vacuum non-linearity consistent with the AVE saturation threshold.

> 🔴 **Criterion re-keying note, 2026-08-03 (Rule 12 — items 1–4 above preserved verbatim).** Per the sector banner at the head of this leaf, `$V_{yield}$` in item 1 (*"a combined electric field exceeding $30\%$ of $V_{yield}/\ell_{node}$"*) and item 3 (*"at $V/V_{yield} > 0.5$"*) re-keys to `$V_{snap}$`: the divergent $C_0/S$ form these criteria test is the longitudinal-A1 compliance, whose bound is $V_{snap}$. The **fractional** thresholds ($30\%$, $0.5$) and the $-80$ dBc detection floor are keying-invariant; only the absolute field they correspond to rescales by $1/\sqrt{\alpha} = 11.706$. **This does not restore a tabletop foothold** — the 2026-06-21 retraction above stands on the *per-node* argument, which is orthogonal to (and unaffected by) which apparatus voltage normalizes the ratio; the honest detection field remains facility-class $E \approx 1.3\times10^{15}$ V/m.

The predicted cubic power-law scaling of IM3 amplitude with drive level is the unique AVE signature. QED predicts a sextic ($V^6$) scaling from the $\alpha^4$ loop correction. Measuring the exponent to within $\pm 0.5$ would definitively distinguish the two frameworks.

> 🔴 **Retracted discriminator (Rule 12, KEEP-BOTH — legacy line above preserved verbatim).** The "QED predicts a sextic ($V^6$) **voltage** scaling" claim is **wrong** and is NOT the discriminator. Both AVE and QED IM3 are **cubic-in-drive** ($\text{IM3} \propto V^3$): both descend from a quartic $E^4$ effective Lagrangian → a third-order susceptibility $\chi^{(3)}$, so both give an $V^3$ IM3 slope (cf. the AVE cubic line itself, two sentences up). QED's "$^6$" is the **FREQUENCY** exponent $(\omega/m_ec^2)^6$ in the Euler-Heisenberg cross-section $\sigma_{EH}$ (§QED Comparison above), **NOT a voltage slope** — measuring the IM3-vs-drive exponent therefore canNOT distinguish the two (both read $3$). The **real discriminator is the COEFFICIENT** (an echo: the AVE coefficient is O(1) against the un-suppressed $E_{yield}=\sqrt{\alpha}\,E_{crit}$, vs QED's $\alpha^2$-loop-suppressed coefficient against $E_{crit}$ — the field-independent ratio $\sim 10^6$), consistent with `clm-pp3qwf` already recorded in §QED Comparison and the B1 row in [`divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md). Same correction graft as the 2026-06-20 birefringence $E^4$-vs-$E^2$ walk-back (clm-pp3qwf, commit `ad26d357`).

---
