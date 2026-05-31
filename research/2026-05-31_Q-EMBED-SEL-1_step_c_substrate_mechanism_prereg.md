# Pre-Registration — Step (c) Substrate-Mechanism: $\sqrt{R \cdot r} = d/2$ from Op1+Op3+Op17+Axiom 3 at the (2,3) Eigenmode

**Status**: DRAFT, NOT LOCKED. PENDING Grant plumber-physical adjudication of §3 below.

**Branch**: `analysis/q-embed-sel-1-investigation` (off main).
**Draft PR**: [#59](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/59).
**Parent epic**: [`_orchestration/2026-05-31_q-embed-sel-1-evaluation.md`](../_orchestration/2026-05-31_q-embed-sel-1-evaluation.md) §4.B (analytical derivation target).
**Skills fired**: `ave-prereg` (Step 1 + 1.5 + 2 in §1-§2 below, Step 3 in §4, Step 3.5 in §5), `pre-test-physics-check` (Step 1 plumber question in §3 — surfaced to Grant), `phase-space-coordinate-check` (load-bearing — derivation is in $(V_\text{inc}, V_\text{ref})$ phasor coords per Grant 2026-04-30 Reading (3)), `verify-before-cite` (all citations grep-confirmed below), `ave-canonical-leaf-pull` (§2 corpus state), `ave-discipline-translate` (EE-as-substrate-native baseline per ave-ee-first-mapping), `consistency-vs-emergence` (§4 classification target), `ave-fundamental-ground-up-implementation` (no engineering defaults; substrate-axioms-first).

---

## §1 Derivation target (Step 1 — formulated precisely)

Derive from Op1 (Universal Impedance $Z = \sqrt{\mu/\varepsilon}$) + Op3 (Reflection Coefficient $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$) + Op17 (Power Transmission $T^2 = 1 - \Gamma^2$) + Axiom 3 ($|\Gamma|^2$ minimization at impedance boundaries) applied to the K4-substrate bond LC tank coupled to the (2,3) phase-space soliton envelope, that the matched-impedance ($\Gamma \to 0$) equilibrium has:

$$\sqrt{R \cdot r} = d/2 \quad \text{equivalently} \quad R \cdot r = (d/2)^2 = 1/4$$

in $(V_\text{inc}, V_\text{ref})$ phasor coordinates, with $d = 1 \ell_{node}$ from regime (a) Nyquist.

Closes step (c) of the ch8 three-regime substrate-mechanism chain, replacing the QED-imported spinor half-cover argument (doc 29 F5, doc 39 §3.4) with substrate-native impedance-matching at the (2,3) eigenmode. Combined with regime (a) $d = 1$ and regime (b) $R - r = d/2$, fully determines the Golden Torus phasor scaffold $R = \varphi/2, r = (\varphi-1)/2$ (the $u = d/2$ substitution gives $R = u\varphi, r = u/\varphi$).

## §2 Corpus state (Step 2 — what's already established)

### §2.1 Substrate-derived (solid foundation)

- **Axiom 1** — K4 Cosserat substrate with $\ell_{node}$ pitch, bond LC tank at characteristic impedance $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ (canonical at `axiom-definitions.md:16`).
- **Axiom 2** — $\xi_{topo} = e/\ell_{node}$; charge as phase dislocation (`axiom-definitions.md:18-31`).
- **Axiom 3** — $|\Gamma|^2$ minimization at every internal impedance boundary; operational signature $S_{11}$ minimization (`axiom-definitions.md:36-46`).
- **Op1 — Universal Impedance**: $Z = \sqrt{\mu/\varepsilon}$ — the canonical AVE geometric-mean form (`operators.md` Op1).
- **Op3 — Universal Reflection Coefficient**: $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$ (`operators.md` Op3).
- **Op17 — Power Transmission**: $T^2 = 1 - \Gamma^2$ (`operators.md` Op17).
- **Op21 — Quality Factor Phase Transition**: $Q = \ell$ (Nyquist-cell mode count) at $\Gamma = -1$ saturation/TIR boundary (`operators.md` Op21).
- **Path A LC-tank derivation** (Theorem 3.1', `theorem-3-1-q-factor.md:21-40`): $\omega_C L_e = Z_0/(4\pi\alpha)$ from substrate primitives. With $L_e = \xi_{topo}^{-2} m_e$ (Ax 2), $\omega_C = c/\ell_{node}$ (Compton frequency), $\ell_{node} = \hbar/(m_e c)$ (Ax 1 calibration): $\omega_C L_e = \hbar/e^2$. Using $\alpha = e^2 Z_0/(4\pi\hbar)$: $\omega_C L_e = Z_0/(4\pi\alpha)$. Then $Q_{tank} = \omega_C L_e / R_{rad}$ with $R_{rad} = Z_0/(4\pi)$ gives $Q_{tank} = 1/\alpha$.
- **Spin-½ from FM kink** (`finkelstein-misner-spin-half-derivation.md`): classical topology of extended unknot defect, K4 → A4 → 2T ⊂ SU(2) chain, $4\pi$ double-cover from spatial rotation. NOT QED postulate.

### §2.2 Grant adjudications (canonical, pre-existing)

- **2026-04-30 Reading (3)** (doc 100 §21, §25 + L5 tracker A-024): *"Golden Torus = mathematical scaffold for α derivation, NOT physical electron geometry."* The physical electron is the $0_1$ unknot on the K4 substrate. The Golden Torus is a phasor-space scaffold.
- **2026-04-27** (`VACUUM_ENGINE_MANUAL.md:3713`): R, r as phase-space radii of $(V_\text{inc}, V_\text{ref})$ phasor on Clifford torus, NOT spatial bond-extent.

### §2.3 Multipole-path geometric framing (Path B, ch8)

`ch8-alpha-golden-torus.md:42-46` + `theorem-3-1-q-factor.md:44-51`:

| Λ | Formula | Value at Golden Torus |
|---|---|---|
| $\Lambda_{vol}$ | $(2\pi R)(2\pi r)(2\pi \cdot 2) = 16\pi^3 (R \cdot r)$ | $4\pi^3$ |
| $\Lambda_{surf}$ | $(2\pi R)(2\pi r) = 4\pi^2 (R \cdot r)$ | $\pi^2$ |
| $\Lambda_{line}$ | $\pi \cdot d$ | $\pi$ |
| **Sum** | | $4\pi^3 + \pi^2 + \pi \approx 137.0363$ |

Key fact for §3: $\Lambda_{vol}/\Lambda_{surf} = 4\pi$ — **this ratio is independent of $R \cdot r$**. The 4π factor is substrate-derived as the spinor-temporal closure (FM 4π double-cover applied temporally). But the **absolute value** of $\Lambda_{surf}$ (and hence $R \cdot r$) is NOT independently derived in the corpus — it sits as the unmotivated ch8 step 4 "$\pi^2$ half-cover area" claim.

### §2.4 What's missing (the actual gap)

The corpus has NO explicit derivation of $R \cdot r = 1/4$ (or equivalently $\sqrt{R \cdot r} = d/2$) from substrate primitives. Path A LC-tank gives $Q_{tank} = 1/\alpha$ tautologically (from α's definition). Path B multipole gives the sum $= 1/\alpha$ at Golden Torus, but only AT Golden Torus — without an independent derivation of Golden Torus geometry from primitives. The two paths agree to $\delta_{strain}$, but the agreement validates Golden Torus *as the scaffold consistent with α*, not as a substrate-derived geometry.

The contested ch8 step 4 (spinor half-cover) was supposed to be the substrate-mechanism but was QED-leakage (doc 29 F5).

## §3 Plumber-physical question for Grant (PENDING — load-bearing for the derivation framing)

**Q-mech-pic**: What does $L_{envelope}$ — the soliton's effective inductance at the macroscopic phasor-envelope scale — scale as in terms of $R$ and $r$? Three candidate scalings give three different substrate-mechanisms for $R \cdot r = 1/4$:

- **(α) Λ-surface scaling**: $L_{envelope} \propto \Lambda_{surf} = 4\pi^2 (R \cdot r)$ — envelope-impedance is proportional to the Clifford-torus 2-cycle phasor surface area. Op17 power-conservation at the (2,3) eigenmode forces $L_{envelope} \cdot \omega_C / Z_0 = $ specific value derived from Op21 mode-count.

- **(β) Geometric-mean scaling**: $L_{envelope} \propto \sqrt{R \cdot r}$ — envelope-impedance is proportional to the geometric mean of envelope scales, matching Op1's $Z = \sqrt{\mu/\varepsilon}$ form one-level-up. Axiom 3 $\Gamma \to 0$ matching to local bond LC tank forces $\sqrt{R \cdot r} = d/2$ directly.

- **(γ) Λ-volume scaling**: $L_{envelope} \propto \Lambda_{vol} = 16\pi^3 (R \cdot r)$ — envelope-impedance is proportional to the 3-cycle phasor volume (including 4π spinor closure). Matching condition involves $\Lambda_{vol}$, not $\Lambda_{surf}$.

Sub-question: is the soliton's coupling to the surrounding substrate ground state through (i) the macroscopic envelope's 2-cycle phasor surface (β suggests), (ii) the envelope's 3-cycle phasor volume (γ), or (iii) the line-mode tube cross-section (regime a)?

The differences matter because each leads to a different specific calculation in §4. (α) makes Op17 + Op21 load-bearing; (β) makes Op1 + Axiom 3 load-bearing; (γ) makes the spinor 4π factor + Op17 load-bearing.

My read: **(β) is most consistent with the §9.2 AVE-native synthesis** (Op1's geometric-mean form scaling up to macroscopic envelope geometry). But (α) might be the cleaner direct route via Op17 since the corpus already has $\Lambda_{surf}$ as a canonical observable. I'll proceed with (β) unless you call (α) or (γ).

## §4 Expected outcome + discriminating bands (Step 3)

Under (β) — my default — the prediction is:

$$\boxed{\sqrt{R \cdot r} = d/2} \quad \text{from Op1 + Op3 + Axiom 3 } \Gamma \to 0 \text{ at the (2,3) eigenmode in phasor coords.}$$

Outcome bands:

- **Outcome A (PASS, Class 2 substrate-mechanism)**: derivation produces $\sqrt{R \cdot r} = d/2$ uniquely from Op1's geometric-mean form applied at the bond-LC-tank-to-envelope scale boundary, with Axiom 3 $\Gamma \to 0$ as the matching condition. Step (c) substrate-derived; the "half-cover" QED-leakage retired.

- **Outcome B (PASS at Class B substrate-mechanism manifestation)**: derivation produces the relation but requires an additional operator combination or a substrate-mechanism step not in the Op1+Op3+Op17+Axiom 3 set. Step (c) substrate-manifestation but not fully axiom-derivation (Class 2).

- **Outcome C (PARTIAL)**: derivation produces $R \cdot r = $ (different value) than $1/4$. Either the framework's α formula needs adjustment, or the derivation framing is wrong (e.g., (β) isn't the right scaling — try (α) or (γ)).

- **Outcome D (FAIL substrate-derivation)**: no substrate-mechanism produces $R \cdot r = 1/4$ from primitives. Reading (3) stands: Golden Torus is a mathematical scaffold, and the α derivation is consistency-with-empirics rather than substrate-emergence. Walk back the "zero-parameter" framing to one-parameter-honest per doc 39 (calibration-input position).

- **Falsifier**: substrate-derivation requires importing a non-substrate concept (e.g., the SU(2) projective-ray postulate that doc 39 §3.4 flagged). Then doc 39 was right, and α is a calibration input.

## §5 Dimensional analysis (Step 3.5 — required for scaling-law prereg per ave-prereg v1.1)

### §5.1 Dimensional ingredients (canonical primitives)

From `src/ave/core/constants.py` + INVARIANT-C* + axiom-definitions.md:

| Primitive | Symbol | Canonical value | Source |
|---|---|---|---|
| Substrate impedance | $Z_0$ | $\sqrt{\mu_0/\varepsilon_0} \approx 376.7\,\Omega$ | Op1 |
| Lattice pitch | $\ell_{node}$ | $\hbar/(m_e c) \approx 3.86 \times 10^{-13}$ m | Ax 1 (reduced Compton, electron-scale) |
| Compton freq | $\omega_C$ | $c/\ell_{node} = m_e c^2/\hbar$ | Ax 1 calibration |
| Bond inductance | $L_e$ | $\xi_{topo}^{-2} m_e = (\ell_{node}/e)^2 m_e$ | Ax 2 |
| Radiation impedance/spinor cycle | $R_{rad}$ | $Z_0/(4\pi)$ | Theorem 3.1' |
| Fine-structure | $\alpha$ | $e^2 Z_0/(4\pi\hbar) \approx 1/137.036$ | derived |
| Tube diameter | $d$ | $1 \ell_{node}$ | Ax 1 Nyquist (regime a) |

### §5.2 Dimensionless combinations

In natural units $\ell_{node} = 1$, $Z_0 = 1$ (lattice-natural per `theorem-3-1-q-factor.md:67`):

- $d/\ell_{node} = 1$ (regime a)
- $R, r$ in $\ell_{node}$ units — dimensionless
- $L_e/(Z_0/\omega_C) = 1/(4\pi\alpha)$ from Path A
- $Q_{tank} = 1/\alpha$

For the prediction $\sqrt{R \cdot r} = d/2 = 1/2$:
- $R \cdot r = 1/4$ dimensionless
- $\Lambda_{surf} = 4\pi^2 \cdot 1/4 = \pi^2$ dimensionless
- $\Lambda_{vol} = 16\pi^3 \cdot 1/4 = 4\pi^3$ dimensionless (4π factor from spinor closure)

### §5.3 Sanity check against canonical anchors

CODATA $\alpha^{-1} \approx 137.0360$. Prediction $\Lambda_{vol} + \Lambda_{surf} + \Lambda_{line} = 4\pi^3 + \pi^2 + \pi = 137.0363$. Match to $\delta_{strain} = 2.225 \times 10^{-6}$ (cold-lattice vs warm-CMB residual, interpreted as thermal running per `theorem-3-1-q-factor.md:88-90`).

The dimensionless ratio sits **at the canonical empirical anchor by construction** (the prediction reproduces the α value the framework was built to derive). The discriminator is not the numerical value but whether the (R, r, d) scaffold is **substrate-derived** vs assumed.

### §5.4 Leading-order scaling exponent (pre-frozen)

Under (β) Op1 geometric-mean scaling: $\sqrt{R \cdot r} \sim d^1$ — linear scaling. If the substrate-mechanism gives a different exponent (e.g., $R \cdot r \sim d^2$ or $\sim d^3$ instead of $d^2$), Outcome C.

Cross-check: dimensionally, $[R \cdot r] = L^2$, $[d^2] = L^2$. Ratio $[R \cdot r]/[d^2]$ is dimensionless — consistent with the framework's natural-units convention. Pre-frozen exponent: $R \cdot r = (d/2)^2$, dimensionless ratio = $1/4$.

## §6 Methodology (Step 4 — proceed-with-derivation plan)

Once Grant adjudicates §3 Q-mech-pic:

### §6.1 Derivation chain (under (β) Op1 geometric-mean scaling)

1. **Define $Z_{envelope}$** via Op1: $Z_{envelope} = \sqrt{\mu_{eff}/\varepsilon_{eff}}$ where $\mu_{eff}, \varepsilon_{eff}$ are the soliton's effective magnetic permeability and electric permittivity at the envelope scale (per Axiom 1 micropolar Cosserat decomposition: magnetic = microrotational DOF, electric = translational DOF).

2. **Identify $\mu_{eff}, \varepsilon_{eff}$ in terms of (R, r, d)**: in phasor coords, the soliton's effective $\mu, \varepsilon$ scale with the envelope geometry. Candidate scaling: $\mu_{eff} \propto R$ (toroidal microrotational coherence), $\varepsilon_{eff} \propto 1/r$ (poloidal translational coherence). Then $Z_{envelope} = Z_0 \sqrt{R \cdot r}$ (with the geometric-mean appearing naturally from Op1 form).

3. **Apply Axiom 3** $|\Gamma|^2$ minimization at the envelope-to-bond-LC-tank boundary: $\Gamma = (Z_{envelope} - Z_{bond})/(Z_{envelope} + Z_{bond}) \to 0$ requires $Z_{envelope} = Z_{bond}$.

4. **Identify $Z_{bond}$**: the local bond LC tank at the Nyquist-cell scale has $Z_{bond} = Z_0 \cdot (d/2) / \ell_{node}$ in lattice-natural units (the d/2 factor is the cross-section radius; in natural units $\ell_{node} = 1$).

5. **Match condition**: $Z_0 \sqrt{R \cdot r} = Z_0 \cdot d/2$ ⇒ $\sqrt{R \cdot r} = d/2$ ✓.

This is the §9.2 synthesis made into explicit algebra. The load-bearing step is step 2 — the identification of $\mu_{eff}, \varepsilon_{eff}$ scaling. That's where Grant's adjudication of §3 Q-mech-pic matters.

### §6.2 Cross-validation

After §6.1, cross-validate:
- **Algebraic**: check that $R \cdot r = 1/4$ + $R - r = 1/2$ (regime b) uniquely give $R = \varphi/2, r = (\varphi-1)/2$ (Golden Torus) via the $u = d/2$ substitution.
- **Λ values**: check $\Lambda_{vol} + \Lambda_{surf} + \Lambda_{line} = 4\pi^3 + \pi^2 + \pi$ at the derived (R, r, d) = Golden Torus.
- **CODATA**: check $\delta_{strain}$ residual stays $\approx 2.225 \times 10^{-6}$ (no new tension introduced).
- **Cross-particle**: §4.F — does the same matching condition give correct (R, r) for proton (3,5), Δ baryon (2,7+)? If yes, the substrate-mechanism is universal. If no, (p,q)-specific corrections needed.

### §6.3 Classification target (consistency-vs-emergence v1.3)

- **Class 2 substrate-mechanism axiom-manifestation** if §6.1 chain closes from Axioms 1+2+3 + Op1+Op3+Op17 alone, no imports.
- **Class B substrate-mechanism manifestation** if §6.1 closes but uses a substrate-mechanism step not in the canonical Op set (some new identification).
- **Class C consistency check** if §6.1 doesn't actually derive — only checks consistency of the assumed Golden Torus with primitives.

Target classification: **Class 2** (the framework's headline aspiration). Honest fallback if §6.1 hits a gap: Class B (still substrate-mechanism but requires named identification step).

## §7 Status

- [x] **Step 1 derivation target formulated** (§1)
- [x] **Step 1.5 physical picture** (per Reading (3) phasor-space framing; full envelope per Grant 2026-05-31)
- [x] **Step 2 corpus state catalogued** (§2)
- [x] **Step 3.5 dimensional analysis** (§5)
- [ ] **Step 3 prereg DRAFT** (this doc) — NOT YET LOCKED
- [ ] **§3 Q-mech-pic** — PENDING Grant adjudication of (α)/(β)/(γ) scaling
- [ ] **§6.1 derivation execution** — gated on Grant call
- [ ] **§6.2 cross-validation**
- [ ] **§6.3 classification declared**
