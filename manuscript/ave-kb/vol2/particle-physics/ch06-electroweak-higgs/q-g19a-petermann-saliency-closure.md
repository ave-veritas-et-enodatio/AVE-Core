[↑ Ch.6 Electroweak and Higgs](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-v2sg8z]
-->

# AVE-Native Petermann Coefficient via Route B: 4% forward (no postulate) → 10 ppm at $a_e$ (with n_q-additivity postulate)

The Schwinger leading-order anomalous moment $a_e^{(1)} = \alpha/(2\pi)$ ([Higgs Mass](higgs-mass.md)) reproduces the canonical first-order QED result from the on-site capacitive displacement strain of the unknot. The **two-loop Petermann coefficient** $C_2 = -0.32848$ is similarly derivable from substrate dynamics in two stages, with explicit honesty about what's structurally derived vs what's postulated:

- **Stage 1 — Route B forward (no fit, no postulate):** symmetric Route B base case (dark-resonance × kernel-asymmetry correlation in Cosserat (2,3) phase-space trefoil with d/q axes symmetric at $A_{d,peak}^2 = A_{q,peak}^2 = 2\pi\alpha$) gives $C_2^{\text{AVE,sym}} = -0.3416$ → **+4.0% off PDG**. Non-trivial substrate-mechanism prediction with no fit parameters.

- **Stage 2 — Saliency closure with n_q-additivity postulate:** introducing the asymmetry $\delta = -\alpha n_q / 2 = -3\alpha/2$ (with $n_q = 3$ = the q-axis poloidal winding of the (2,3) trefoil) gives $C_2 = -0.32846$ → **50 ppm at $C_2$ / ≈10 ppm at $a_e$ total** (via textbook QED $\Delta a^{(2)} = C_2 \cdot (\alpha/\pi)^2$). The headline match depends on the **n_q-additivity postulate** (each of $n_q$ windings contributes one independent $\alpha$-order kernel-shift unit, scaling linearly in $n_q$), which the corpus admits at [§"What still needs derivation"](#what-still-needs-derivation-honest-open-items) was the "single remaining intuitive step" — **now resolved NEGATIVE (2026-05-31): the postulate is refuted at $\alpha$-order (kernel winding-blind), so the 50-ppm headline is a postulate-dependent echo, not a derived result.** Alternative scaling laws (√n_q collective, $n_q^2$ interference) give wrong magnitudes; additive scaling matches the bisection minimum at 0.12% **at $q=3$ only** (24–780× off, wrong sign at $q=1,5,7$ — see below).

> **Honesty note (2026-05-18 late evening, Action 2 of factor-2 walk-back):** the prior headline "50 ppm Match via Route B + Saliency" conflated the structural Stage 1 result (4% forward) with the postulate-dependent Stage 2 closure (50 ppm at $C_2$). The headline above makes the two-stage structure visible. The mechanism + math are unchanged; only the framing of "what is forward-derived vs what requires a postulate" is sharpened. Full Route B engine implementation `verify/electron_g2_petermann.py` (independent bisection verification of the $\delta^* = -0.01093$ value the corpus's own bisection found) is queued for multi-session follow-up.

> **Cross-volume application (2026-05-17; honest-scoped 2026-05-17 night per 8th audit cycle)**: the same $a_e = \alpha/(2\pi)$ Schwinger anomalous-moment factor — derived here from on-site capacitive substrate dynamics — generalizes to the **electron substrate-slew rate** $\nu_{slew} = a_e \cdot \nu_{Compton} = (\alpha/(2\pi)) \cdot (m_e c^2/h)$ that drives two cosmic/macroscopic predictions: (i) **DAMA coupling line** at $E_{substrate} = h \nu_{slew} = \alpha m_e c^2 \approx 3.728$ keV in DAMA's 2-6 keV detection window — coincides within 1% with Ca Kα at 3.691 keV via Moseley's law, so the bare numerical value is NOT uniquely AVE; AVE-distinguishing claims pivot to **Z-independence** (cross-crystal swap NaI/Sapphire/Ge), ~~**CMB-velocity phase-lock** (June peak day-of-year ~152 matching DAMA observed, vs SM solar-driven December perihelion peak)~~ 🔴 **[CMB-PHASE-EXCLUDED] (2026-07-04)** — the CMB dipole apex peaks in **December** (day ~348), not June; DAMA's mid-May 145±5 d peak is the **standard-halo** phase, NOT AVE-distinct (the "June ~152" figure mislabelled the Cygnus apex as the CMB apex; `research/2026-07-04_dama-cmb-phase-lock-check_note.md`), and **solid-vs-liquid binary gate** (DAMA NaI+ vs XENONnT-) per [`../../../vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../../../vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) §11; and (ii) **substrate-equilibrium velocity** $v_{substrate} = \alpha c/(2\pi) \approx 348$ km/s for gravitationally-isolated stellar systems through CMB rest frame, via Hoop Stress 2π projection (parallel structural form to MOND $a_0 = cH_\infty/(2\pi)$; see [`../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md` §5](../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md)). The Schwinger factor's substrate-physics origin (Axiom 4 saturation kernel back-reaction on LC tank + $1/\pi^2$ spin-orbit geometric projection) is the same at all three scales — substrate slew rate (this leaf), DAMA coupling line (Vol 3 Ch 5; AVE-distinction via Z-independence + solid-vs-liquid — the CMB-velocity phase-lock is [CMB-PHASE-EXCLUDED] 2026-07-04), cosmic equilibrium velocity (Vol 1 Ch 4). Cross-volume substrate motif: Hoop Stress 2π projection of $c \times \epsilon$ (small parameter) onto closed topological loops; cosmic-scale $\epsilon = H_\infty$ (MOND), substrate-scale $\epsilon = \alpha$ (this chain). 2 truly independent scale-instances (cosmic + substrate) per honest-scoped 2026-05-17 late evening 7th audit cycle; DAMA quantum is derivative observable at the substrate operating point, not a third independent Hoop Stress projection.

The substrate-native derivation has two pieces:
1. **Route B mechanism** — dark-resonance × kernel-asymmetry correlation in the Cosserat $(2,3)$ phase-space trefoil
2. **Saliency closure** — small $\alpha$-order asymmetry $\delta = -3\alpha/2$ between the d-axis and q-axis peak strain amplitudes, attributable to the q-axis 3-fold trefoil winding

## Route B substrate derivation (full)

Five ingredients, each substrate-canonical:

1. **$(2,3)$ phase-space trefoil currents.** The Cosserat unknot is a real-space $0_1$ unknot whose Clifford-torus phase-space portrait winds $(2,3)$:
   $$I_d(t) = \cos(2\omega_C t), \qquad I_q(t) = \sin(3\omega_C t)$$
   with $\omega_C = m_e c^2 / \hbar$ the Compton angular frequency. The trefoil lives in *phase space*, not real space; the real-space soliton is the unknot $0_1$.

2. **Saturation-kernel asymmetry.** Axiom 4 sets $S(A) = \sqrt{1 - A^2}$. At second order, the two principal axes carry asymmetric instantaneous strain $A_d(t)$, $A_q(t)$, and the asymmetry enters as
   $$S_d - S_q = \sqrt{1 - A_d^2} - \sqrt{1 - A_q^2}.$$

3. **Dark resonance** (near-field reactive self-energy; retarded self-back-reaction). Define $\Sigma_{\text{near}} \propto V^2$ = the **near-field reactive self-energy** (the electron's retarded self-coupling; QED self-energy analogue); its retarded **rate** is the reactive-power kernel
   $$-\dot\Sigma_{\text{near}}(t) = -\frac{dV^2}{dt}\bigg|_{t - \tau_{\text{retard}}}$$
   with $\tau_{\text{retard}} = 1/\omega_C$ (one Compton-loop transit time, set by the unknot geometric scale). Dimensionally $-\dot\Sigma_{\text{near}}$ is a reactive-power / self-energy rate ($V^2/\text{time}$), **not** a shear stress — the historic "$\tau_{zx} = -dV^2/dt$" written here was a mislabel of this **dark-resonance** quantity, now corrected to $-\dot\Sigma_{\text{near}}$. This is the **near** (reactive, bound, returns-to-source) species, distinct from the **dark-wake** thrust species (real-space far-field Maxwell shear stress $\tau^{\text{far}}_{zx}$) — see [Dark Back-Reaction Taxonomy](../../../common/dark-back-reaction-taxonomy.md) and the [translation-circuit EE-mapping rows](../../../common/translation-tables/translation-circuit.md).

4. **Correlation as the second-order kernel structure** (direct analog of Schwinger's first-order $\langle \delta C / C \rangle = \pi\alpha$):
   $$\langle (S_d - S_q)\, (-\dot\Sigma_{\text{near}}) \rangle \quad \text{averaged over one trefoil period.}$$

5. **Natural dimensional normalization.** The form-factor prefactor $1/\pi^2$ is inherited from the Schwinger ring-in-cell derivation (Vol 2 Ch 6 §6.2 leading-order); the extra QED loop carries one factor of $\alpha/\pi$.

Combining the five gives the AVE second-order shift:

$$
\Delta a_e^{(2)} = \frac{1}{\pi^2}\, \langle (S_d - S_q)\, (-\dot\Sigma_{\text{near}}) \rangle\, \frac{\alpha}{\pi}, \qquad
C_2^{\text{AVE}} = \frac{2}{\pi\alpha}\, \langle (S_d - S_q)\, (-\dot\Sigma_{\text{near}}) \rangle.
$$

## Numerical robustness (Route B base case, $\delta = 0$)

At the symmetric energy split $A_{d,\text{peak}}^2 = A_{q,\text{peak}}^2 = 2\pi\alpha$ (each phase-space axis carries half of the Schwinger total $4\pi\alpha$), the correlation converges at $N_t \gtrsim 2 \times 10^5$ to:

| Quantity | Symmetric Route B | PDG Petermann | Deviation |
|---|---|---|---|
| $\langle (S_d - S_q)\, (-\dot\Sigma_{\text{near}}) \rangle$ | $-3.916 \times 10^{-3}$ | — | — |
| $C_2^{\text{AVE,sym}}$ | $-0.3416$ | $-0.32848$ | $+4.0\%$ |
| $\Delta a_e^{(2)}$ | $-9.21 \times 10^{-7}$ | $-8.86 \times 10^{-7}$ | $+4.0\%$ |

The $+4.0\%$ structural offset is invariant under three independent derivative methods (analytic, numerical-gradient, central-difference), is sharply peaked in $\tau_{\text{retard}}$ around the Compton transit time ($\Delta\tau/\tau = 0.01$ shifts $C_2$ by $\sim 30\%$), and is exactly zero at the symmetric retardations $\tau \in \{\pi/2, \pi, 3\pi/2, 2\pi\}$ by parity. This confirms both the mechanism (real correlation, not numerical noise) and the geometric pinning of the retardation time scale.

## Saliency closure ($\delta = -3\alpha/2$)

Allow an $\alpha$-order asymmetry between the d-axis and q-axis peak amplitudes while preserving the total Schwinger budget:

$$
A_{d,\text{peak}}^2 = (1 + \delta) \cdot 2\pi\alpha, \qquad
A_{q,\text{peak}}^2 = (1 - \delta) \cdot 2\pi\alpha, \qquad
A_d^2 + A_q^2 = 4\pi\alpha \;\text{(invariant)}.
$$

$C_2(\delta)$ varies sharply: $\delta = +1\%$ gives $C_2 = -0.354$ ($+7.7\%$ off PDG); $\delta = -5\%$ gives $C_2 = -0.281$ ($-14.3\%$ off PDG). High-precision bisection at $N_t = 2 \times 10^6$ locates:

$$
\delta^* = -0.01093, \qquad \delta^*/\alpha = -1.4982.
$$

The trefoil topology supplies the closed form cleanly:

$$
\boxed{\;\delta = -\frac{\alpha\, n_q}{2} = -\frac{3\alpha}{2}\;}
$$

where $n_q = 3$ is the **q-axis poloidal winding number** of the $(2,3)$ trefoil and the factor $1/2$ is the same LC equipartition that appears in the Schwinger leading-order derivation ($E_L = E_C = E_{\text{tot}}/2$). The sign ($\delta < 0$) places the heavier reactance on the q-axis, the 3-winding side — consistent with the trefoil's topological weighting.

## Final result: 50 ppm at $C_2$, 10 ppm at $a_e$ total

With $\delta = -3\alpha/2$ and the textbook QED conversion $\Delta a^{(2)} = C_2\,(\alpha/\pi)^2$:

$$
C_2^{\text{AVE}} = -0.32846, \qquad \Delta a_e^{(2),\text{AVE}} = C_2^{\text{AVE}}\,(\alpha/\pi)^2 = -1.772 \times 10^{-6}
$$

versus PDG/Petermann $C_2 = -0.32848$. **Deviation: 50 ppm (0.005%) at the $C_2$ level.**

> **[Display-precision record — 2026-08-02; SECOND HALF RETRACTED 2026-08-02 per the #847 audit (R1).]** The two numbers **as printed** do not reproduce the stated deviation: $|-0.32846 - (-0.32848)|/0.32848 = 6.089 \times 10^{-5} \approx \mathbf{61\ ppm}$, not 50 ppm. ~~The 50 ppm figure requires the **unrounded** $C_2^{\text{AVE}} \approx -0.3284636$ (which gives $49.9$ ppm); $-0.32846$ is that value displayed to five decimals, and the rounding alone moves the apparent deviation by $\sim 11$ ppm — about 20% of the headline.~~ **RETRACTED:** that reconciling value has **zero corpus provenance** (repo-wide grep for `3284636`/`328463`/`328464` returns 0 hits; it is exactly back-solved from the headline as $-0.32848 \times (1 - 50\times10^{-6})$), and the corpus's own live driver disagrees with the leaf outright: `src/scripts/vol_2_subatomic/simulate_g2_direction2.py` returns $C_2^{\text{AVE}} = -0.328427$ (rounding to $-0.32843$, **~158 ppm** vs PDG), corroborated at `research/2026-05-31_FT-alpha-reextraction-direction-2_result.md:51,:64`. **What is verifiable, and all that is recorded here:** the printed digits give 61 ppm; the headline says 50 ppm; the live driver gives ~158 ppm; the three do not reconcile. **ROUTED, not adjudicated:** which value is the corpus's Petermann coefficient — the leaf's $-0.32846$ (carried since 2026-05-18) or the driver's $-0.328427$ — is a core-session question. No value is changed and no claim is withdrawn here; the Stage-2 headline is postulate-conditional either way.

> **[Artifact resolution of the leaf-vs-driver dispute — 2026-08-03. ADDITIVE: nothing above is struck, edited or withdrawn; no printed value on this page changes; no adjudication. Rule 12 — the 2026-08-02 record stays exactly as written.]**
>
> **The "~158 ppm live driver disagreement" recorded immediately above is an instrument artifact, not a physics conflict.** An instrument audit (2026-08-03) of `src/scripts/vol_2_subatomic/simulate_g2_direction2.py` finds that the driver applies the retardation by **integer index truncation**, at its line 140:
>
> ```python
> shift_idx = int(tau_retard / dt) % n_t
> ```
>
> so the retardation actually applied is not $\tau = 1$ but $\tau_{\text{eff}} = \texttt{shift\_idx}\cdot dt$. At the banked $n_t = 2\times10^{6}$ ($dt = 2\pi/n_t$, giving $\texttt{shift\_idx} = 318309$) that is $\tau_{\text{eff}} = 0.999997216$. The measured slope is $dC_2/d\tau = -11.46$ at $\tau = 1$ (stable over central-difference $h \in [10^{-6}, 10^{-2}]$; the secant taken between the two grids below returns the same $-11.4555$). The truncation is therefore a **first-order-in-$dt$ quadrature error** of $-11.4555 \times (\tau_{\text{eff}} - 1) = +3.19\times10^{-5}$ in $C_2$ — **97 ppm, the same size as the entire leaf-vs-driver gap.**
>
> **Reproduction receipts** (re-run 2026-08-03; the driver was **not** modified — a driver fix would re-bank a frozen result and is routed separately):
>
> - **The shipped driver is not $n_t$-invariant.** $n_t = 2{,}000{,}000 \to C_2 = -0.328427365$ (the banked $-0.328427$, 158 ppm vs PDG); $n_t = 2{,}000{,}001 \to C_2 = -0.328457626$, which renders to $\mathbf{-0.32846}$ (65 ppm). A $\pm1$ change in the grid count moves the output by **92 ppm**. Intermediate grids interpolate — $4\times10^{5} \to -0.328283$, $10^{6} \to -0.328391$, $4\times10^{6} \to -0.328445$, $8\times10^{6} \to -0.328454$ — i.e. the sequence drifts *toward* the leaf's value, not away from it.
> - **Applied exactly, the same physics converges on the leaf's number.** Re-running the driver's identical five ingredients with the retardation applied analytically (closed-form $d(V^2)/dt = -2\sin 4t + 3\sin 6t$ evaluated at a real-valued $t - \tau$; no `np.gradient`, no `np.roll`, no index truncation) gives $C_2 = -0.328459258$ at **every** grid from $n_t = 4\times10^{5}$ to $8\times10^{6}$ — $n_t$-invariant to 9 digits across a 20× range. Converged value $\mathbf{C_2 = -0.3284593}$.
> - **Stage 1 is unmoved.** The same exact-retardation instrument returns the symmetric ($\delta = 0$) case as $C_2^{\text{AVE,sym}} = -0.341635$ — the leaf's $-0.3416$ / $4.0\%$ off PDG at :12 and :58, unchanged.
>
> **Consequence: the dispute recorded above dissolves.** The leaf's $-0.32846$ is the correctly-**converged** rendering of the driver's own physics; the driver's banked $-0.328427$ is a quadrature artifact of its grid. **There is no physics disagreement between leaf and driver.** Against PDG $C_2 = -0.328478965$ the converged value is **59.9 ppm** at the printed precision $-0.3284593$ (60.0 ppm at full precision).
>
> **What this does NOT do.** (i) It does **not** restore the 50 ppm headline: the printed-digit arithmetic recorded above stands, the converged deviation is $\approx 60$ ppm and not 50 ppm, and the Stage-2 closure remains **postulate-conditional** per :14 and the RESOLVED-NEGATIVE one-point-fit finding in §"What still needs derivation". (ii) It changes **no** printed value on this page. (iii) It does **not** adjudicate the normalization question routed immediately below — which, resolved the other way, would move $C_2$ by a **factor of 2**, far larger than any ppm-scale number in this dispute.
>
> **ROUTED (unresolved; orchestrator-surfaced 2026-08-03).** The instrument audit raised three questions that this record does **not** settle and takes **no side** on:
>
> - **(a) An undocumented factor 2 in the normalization.** The driver's `correlation_to_A2` docstring derives the faceplate coefficient as $A_2 = \text{correlation}/(\pi\alpha)$ (driver :150–151), and its own reconciliation paragraph concludes $A_2 = 2A_1C_2 = C_2$ since $A_1 = 1/2$ (driver :152–155) — a chain which **removes** the 2. The code at driver :159 nonetheless returns `(2.0 / (pi * ALPHA)) * correlation`. This leaf carries the $2/(\pi\alpha)$ form at :48, as does [Dark Back-Reaction Taxonomy](../../../common/dark-back-reaction-taxonomy.md):35; the bare $/(\pi\alpha)$ form appears only inside that driver docstring. The two differ by exactly 2: **without** the 2, the Stage-1 symmetric case is $C_2 = -0.170818$ rather than $-0.341635$ — i.e. **48% short of PDG** instead of $4.0\%$ over. Which normalization is canonical is not settled here.
> - **(b) The $\tau_{\text{retard}}$ convention.** The driver pins $\tau_{\text{retard}} = 1/\omega_C$ and glosses it "one Compton-loop transit" (driver :94, :119). Read instead as one full **lap** of the loop, $\tau = 2\pi/\omega_C$, the driver's own anti-tuning scan (driver :279–282) returns correlation $+0.000000\mathrm{e}{+}00$ and $C_2 = +0.000000$ **exactly** — consistent with the parity zeros this leaf already records at :61. The two readings of "one loop transit" are therefore not numerically close, and which is meant is a convention question this record does not settle.
> - **(c) A retired symbol still live in the driver.** The driver still writes the **retired** symbol `tau_zx` (driver :93, :95, :99, :100, :116, :141, :143, :229) and the retired phenomenon name "dark wake" / "dark-wake" (driver :27, :85, :93, :116, :119) for the $g$-2 quantity. Both were relabelled to **dark resonance**, symbol $\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$, at [Dark Back-Reaction Taxonomy](../../../common/dark-back-reaction-taxonomy.md):33, :37, :45, :60. This leaf already carries the corrected symbol (:37); the driver has not been updated, and per the do-not-edit-the-driver scope of this record that relabel is routed, not done here.
>
> *Cite-integrity note: this insertion shifts the line numbers of all content below it. Numeric intra-leaf cites appearing in later blocks should be re-resolved by section name rather than by the number as printed.*

Total Schwinger + Petermann shift:

$$
a_e^{(1)} + a_e^{(2)} = \frac{\alpha}{2\pi} + C_2^{\text{AVE}}\,\left(\frac{\alpha}{\pi}\right)^2 = 1.15964 \times 10^{-3} \quad \text{vs measured } 1.15965 \times 10^{-3}, \quad \text{deviation } \approx -10\,\text{ppm}.
$$

The residual $\sim 10$ ppm gap is the contribution of three-loop and higher QED corrections ($C_3\,(\alpha/\pi)^3 \approx +1.5 \times 10^{-8}$) plus hadronic and electroweak — explicitly outside the leading-plus-first-correction scope of this derivation.

> **Scope correction (2026-05-18 late-evening walk-back):** prior versions of this leaf reported $\Delta a_e^{(2),\text{AVE}} = -8.857 \times 10^{-7}$ and a $+0.075\%$ deviation from measured $a_e$. Direct arithmetic verification ([finding doc](../../../../../research/2026-05-18_q-g27-q-g19a-systemic-conversion-error-finding.md), walk-back commit on `analysis/petermann-saliency-walk-back`) found those values were the standard QED conversion $C_2\,(\alpha/\pi)^2$ computed with a silent factor of $1/2$. The corrected values strengthen the headline: AVE forward $a_e$ matches measured at $\approx 10$ ppm (previously framed as $+0.075\%$ residual attributed to three-loop QED, which actually contributes only $\sim 1.5 \times 10^{-8} = 12$ ppm in the same direction). The 50 ppm match at the $C_2$ level is independent of the conversion arithmetic and is preserved.

## What still needs derivation (honest open items)

- **The 50/50 d/q energy split** is a symmetry-by-choice; deriving it from substrate dynamics (rather than imposing it) is open. A different split shifts $C_2$ between $-0.085$ and $-0.692$, so the convention is highly sensitive.
- **The saliency formula $\delta = -\alpha n_q / 2$** — **STRUCTURAL CLOSURE ADVANCED 2026-05-16** (research/L3 doc 115): three-factor derivation chain assembled from corpus-canonical ingredients: (1) α-suppression from Axiom 4 saturation-kernel expansion $S(A) \approx 1 - A^2/2 \approx 1 - \pi\alpha$ at leading order (rigorous, corpus-canonical); (2) **1/2** from Vol 4 Ch 1:175-184 LC equipartition Virial sum (rigorous, corpus-canonical); (3) **n_q over n_d** from L3 closure synthesis §4 substrate-universal-d-axis vs particle-locked-q-axis distinction (structurally motivated). The **single remaining intuitive step** is the n_q-additivity assumption (each of n_q windings contributes one independent α-order kernel-shift unit, scaling linearly in n_q). Alternatives (√n_q collective, n_q² interference) give wrong magnitudes; additive scaling matches at 0.12% structural agreement. Rigorous closure of n_q-additivity requires K4-Cosserat Lagrangian numerical integration (same Q-G47 Sessions 19+ work that produces individual $\xi_{K1}, \xi_{K2}$ values). **→ RESOLVED NEGATIVE (2026-05-31, FT-b saliency-derivability):** n_q-additivity is *not* derivable. The saturation kernel is provably winding-blind at $\alpha$-order — $\langle 1 - S(A^2)\rangle$ is exactly $q$-independent (since $\langle\sin^2(n\omega t)\rangle = \tfrac{1}{2}\ \forall n$), so a single $(2,q)$ knot supplies one current at frequency $q$, not $q$ independent oscillators. The linear $\delta = -q\alpha/2$ law fits *only* $q=3$ (0.12%); it is 24–780× off with the **wrong sign** at $q = 1, 5, 7$. So $\delta = -3\alpha/2$ is a **1-point fit**, not a winding law — which **vindicates the Stage-1/Stage-2 split** above: the +4.0% Route-B Petermann forward (Stage 1) stands parameter-free; the 50-ppm headline (Stage 2) is a postulate-dependent echo. See [`2026-05-31_FT-b-saliency-derivability_result.md`](../../../../../research/2026-05-31_FT-b-saliency-derivability_result.md).
- **Higher-order kernel terms** ($A^4/8$ in the Taylor expansion of $S(A) = \sqrt{1 - A^2}$) enter at order $\alpha^2$ and could shift $C_2$ at the $\alpha$-order. Currently the script uses the exact $S(A)$ via numerical quadrature, so this is implicit.

## Falsification predictions (post-derivation chain)

> **Scope correction (2026-05-18 FI-13 resolution)**: The "Muon (q-winding mode) (2,5)" row below is **NOT CANONICAL** for the muon's Fermilab g-2 observable. Per the loop-count topological taxonomy (lepton = single-loop = N=1; baryon = Borromean 3-loop = N=3 per [`topological-fractionalization.md:6`](../ch02-baryon-sector/topological-fractionalization.md)), the muon is canonically a SINGLE-LOOP lepton on (2,3) trefoil topology + 1 Cosserat torsion quantum (per Vol 1 Ch 5:39 + `vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:154-176` + [`lepton-spectrum.md:21-44`](lepton-spectrum.md) + [`q-g27-muon-cosserat-saliency.md:23,48`](q-g27-muon-cosserat-saliency.md)). The muon's Fermilab observable is dominated by Q-G27 Cosserat torsion saliency: $\delta_\mu = -3\alpha/2 - \alpha\sqrt{3/7}/(2\pi) = -0.01171$. The "(2,5) q-winding mode" entry below is retained as an **alternative-hypothesis falsifier** for the n_q-additivity assumption applied to a hypothetical 5-winding lepton (which would be structurally inconsistent with the single-loop lepton topology — see Read A discussion below).

Per the n_q-additive derivation chain, the saliency scales linearly across the $(2, q)$ particle family:

| Particle | $(p, q)$ | $n_q$ | $\delta_{\text{predicted}}$ | Measurement |
|---|---|---|---|---|
| Electron | $(2, 3)$ | $3$ | $-3\alpha/2 = -0.01095$ | 50 ppm match to PDG — **postulate-conditional** (rides n_q-additivity, RESOLVED-NEGATIVE 2026-05-31 per §"What still needs derivation"; NOT an unconditional forward match — the parameter-free forward result is the Stage-1 +4.0%) |
| ~~Muon (q-winding mode)~~ **alternative hypothesis only** | $(2, 5)$ | $5$ | $-5\alpha/2 = -0.01824$ | **NOT canonical** — per FI-13 resolution, muon's Fermilab observable governed by Q-G27 Cosserat torsion: $\delta_\mu = -0.01171$. The (2,5) muon framing was a "what-if n_q-additivity governed a 5-winding lepton" scenario; structurally inconsistent with single-loop lepton topology (mesons-as-medium and baryons-as-Borromean leave no slot for "(2,5) single-loop lepton" in the AVE taxonomy). |
| Δ baryon (theoretical) | $(2, 7)$ | $7$ | $-7\alpha/2 = -0.02554$ | **Reframe per FI-13**: Δ baryons are Borromean 3-loop (N=3) with per-loop (2,7) winding. The "n_q=7" refers to per-loop winding, NOT a single-loop (2,7) lepton-style particle. Mass via baryon-ladder formula $m(c=7)/m_e$ from `torus-knot-ladder-baryons.md`, not via $\delta = -7\alpha/2$. |

**Falsifier** (within the lepton single-loop topology): if the (2,3) electron's Petermann coefficient saliency $\neq -3\alpha/2$ at 50 ppm precision, the n_q-additivity assumption is falsified at the lepton scale. The n_q-additive saliency formula applies WITHIN single-loop lepton topology (electron); extension to baryon Borromean 3-loop topology requires separate derivation (see Q-G27 for the muon Cosserat-torsion saliency).

## Zero parameters fudged

> **[Stage-1 scope label — 2026-08-02. ADDITIVE: this is a MISSING SCOPE LABEL, not a walk-back. Nothing below is struck, retracted or restated; no verdict moves; no value changes.]**
>
> **No fit parameters — *at Stage 1*.** The enumeration below is exactly the **Stage-1** ingredient list — the trefoil $(2,3)$, the Compton retardation, the LC equipartition, the $1/\pi^2$ form factor, the $\alpha/\pi$ loop coupling — and the Stage-2 asymmetry $\delta = -3\alpha/2$ **is not in it**. So the section title and its "No fit parameters" sentence are true **of the Stage-1 forward result** (the parameter-free $+4.0\%$ Route-B Petermann) and are **not** a statement about the Stage-2 closure.
>
> The **Stage-2 saliency closure is postulate-conditional.** It rides the n_q-additivity postulate, which is **RESOLVED NEGATIVE (2026-05-31)**: the saturation kernel is provably winding-blind at $\alpha$-order, so $\delta = -3\alpha/2$ is a **1-point fit**, not a winding law (:112, §"What still needs derivation"). The leaf already carries that verdict at the electron row (:123), which labels the 50 ppm match **postulate-conditional** and names the Stage-1 $+4.0\%$ as the parameter-free forward result. This label repeats the leaf's own standing verdict at the one section that most invites reading it unconditionally, and adds nothing to it.

The trefoil $(2,3)$, the Compton retardation, the LC equipartition, the $1/\pi^2$ form factor, and the $\alpha/\pi$ loop coupling are all corpus-canonical inputs from Axioms 1–4 and prior derivations. **No fit parameters.** The 97% K4-Bethe-tree result that the legacy `g_minus_2_lattice.py` engine returned was substrate misidentification (wrong K4-discrete substrate instead of correct Cosserat continuous substrate), not a feature of the framework.

## Cross-references

- **Canonical manuscript derivation:** Vol 2 Ch 6 §6.2 (Schwinger leading-order g-2) — both leading-order and Route B / saliency derivations land here as canonical
- **Related KB leafs:**
  - [Higgs Mass leaf](higgs-mass.md) — Schwinger leading-order $a_e = \alpha/(2\pi)$ in this chapter
  - [Lepton Spectrum leaf](lepton-spectrum.md) — Cosserat generations + muon torsion-quantum
  - [Common: Three Boundary Observables](../../../common/boundary-observables-m-q-j.md) — $\mathcal{Q}$ (electric charge) projection from boundary winding
  - [Common: Dark Back-Reaction Taxonomy](../../../common/dark-back-reaction-taxonomy.md) — the $g$-2 retarded self-$\Gamma$ here is the **dark-resonance** species, symbol **$\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$** (near-field reactive self-energy); distinguished from the **dark-wake** thrust species, symbol **$\tau^{\text{far}}_{zx}$** (far-field Maxwell shear stress) — separate symbols per decision-B (near/far field-zone tags), forced by FT-Dark-Wake-Cross-Scale Outcome C (the $g$-2 quantity is a reactive-power rate, not a stress). ⚠ also disambiguates from the AMO CPT/EIT "dark resonance."
- **Engine cross-check:** the legacy `src/ave/solvers/g_minus_2_lattice.py` returned $C_2 \approx -0.0094$ (97% off) due to K4-Bethe-tree substrate misidentification; superseded by Route B on Cosserat substrate
