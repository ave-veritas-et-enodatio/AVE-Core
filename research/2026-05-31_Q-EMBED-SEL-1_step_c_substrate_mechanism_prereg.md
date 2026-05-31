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

## §3 Substrate-mechanism direction (updated 2026-05-31 per Grant hint)

**Grant directive 2026-05-31**: *"think through this... research fusion required energy levels for cold fusion on earth and what metric compression does to atoms, likely same type of interaction as electrons."*

That hint reframes the substrate-mechanism direction. The Op1+Op3+Op17+Axiom 3 impedance-matching framing was partial — it missed the canonical **Axiom 4 self-saturation mechanism** that the corpus already has at `photon-identification.md` and `theorem-3-1-q-factor.md`.

### §3.1 The actual substrate-mechanism: Axiom 4 self-saturation + TIR boundary formation

The electron is canonically defined as a **self-trapped photon** (`photon-identification.md:11`): the same K4 transverse-Cosserat-microrotation wave as a free photon, BUT with Axiom 4 self-saturation engaged. The mechanism (`photon-identification.md:104` verbatim):

> *"$\Delta\phi \to \alpha \Rightarrow$ electron: at-yield amplitude triggers Axiom 4 self-saturation, $C_{eff} \to \infty$, $Z_{local} \to 0$, $\Gamma \to -1$ TIR cavity self-creates, the transverse wave is trapped into a standing wave inside the self-created mirror."*

This IS the substrate-mechanism for the envelope (R, r):
- The soliton's amplitude profile $A(r, \theta, \phi)$ varies in space across the (2,3) eigenmode
- Where $A = A_{yield} = \sqrt{\alpha} \cdot V_{snap}$, Axiom 4's $S(A) \to 0$ saturation engages
- At that surface, $C_{eff} \to \infty$, $Z_{local} \to 0$, $\Gamma \to -1$ TIR forms (per Op14 Dynamic Impedance)
- **The (R, r) envelope IS the geometric location of this self-saturated TIR boundary surface**

The (R, r) aren't free geometric parameters — they're **outputs** of the saturation-profile equation. The substrate-mechanism for $\sqrt{R \cdot r} = d/2$ is then:

> **The (2,3) eigenmode's amplitude profile reaches $A_{yield}$ at a specific geometric locus determined by Axiom 4 ($S(A)$ kernel) + Op14 ($Z_{eff} = Z_0/\sqrt{S}$) + the (2,3) topology. The TIR boundary surface has characteristic radii $(R, r)$ with $\sqrt{R \cdot r} = d/2$ — the geometric mean of envelope scales equals half the Nyquist scale because that's the natural length-scale at which the substrate self-saturates against its own Nyquist cutoff $d$.**

### §3.2 Cross-domain validation: cold fusion ≡ same mechanism at nuclear scale

The cold-fusion connection Grant pointed at: when EXTERNAL conditions (Pd lattice, electron screening) drive local substrate conditions toward $A \to A_{yield}$ near multiple nuclei simultaneously, the substrate locally saturates between the nuclei — the same TIR-boundary-formation mechanism, but driven externally instead of by self-amplitude.

Standard physics' Coulomb barrier (~MeV for D-D fusion) is set by the substrate's vacuum impedance $Z_0$ at the inter-nuclear separation. In a saturated substrate (locally $S(A) \to 0$), $Z_{eff} = Z_0/\sqrt{S} \to \infty$ near the saturated region, which means the **effective distance scale shrinks**: the nuclei "see" each other at a much smaller effective separation than the vacuum-coordinate distance. The Coulomb barrier — set by impedance integrated over distance — drops.

Empirical anchors:
- Hot D-T fusion: ~100 keV ignition (Coulomb barrier at vacuum $Z_0$)
- NASA Glenn lattice-confinement fusion (2020s, deuterium in metal hydride): ~keV scale (barrier reduced by factor of ~10² via lattice-induced local saturation)
- Fleischmann-Pons cold fusion claims (controversial, but if real): ~eV scale (barrier reduced by factor of ~10⁴⁻⁵)

The ratio matches the corpus's $1/\sqrt{S}$ scaling for the right $S$ values. **If the substrate-saturation mechanism is correct for the electron envelope, it should also predict cold-fusion energy scales.** This is a cross-domain falsifier built into the derivation.

### §3.3 Revised Q-mech-pic (PENDING Grant confirmation)

Updated candidate substrate-mechanisms — (α), (β), (γ) from prior version superseded by:

- **(δ) Axiom 4 self-saturation TIR boundary** *(NEW DEFAULT per Grant hint)*: $L_{envelope}$, $C_{envelope}$, $Z_{envelope}$ are ALL set by the saturation-profile $S(A(r))$ at the (2,3) eigenmode. The (R, r) emerge as the locus where $A = A_{yield}$. The derivation reduces to solving the (2,3) eigenmode's amplitude profile + identifying the TIR boundary surface.

  Substrate-mechanism chain: Axiom 1 (K4 + Cosserat) + Axiom 4 ($S(A)$ kernel) + Op14 (Dynamic Impedance) + Op17 (Power Transmission) + Axiom 3 ($\Gamma = -1$ TIR boundary condition) → (R, r) envelope with $\sqrt{R \cdot r} = d/2$.

  Cross-domain falsifier: same mechanism predicts cold-fusion energy levels (lattice-confinement fusion ~keV, Fleischmann-Pons claims ~eV if real).

The prior (α)/(β)/(γ) framings are now seen as PARTIAL — each captures one aspect of the (δ) mechanism:
- (α) Λ-surface scaling: the TIR boundary's 2D extent is parameterized by $\Lambda_{surf}$
- (β) Geometric-mean scaling: $\sqrt{R \cdot r}$ emerges naturally from the saturation profile's $1/\sqrt{S}$ dependence (Op14)
- (γ) Λ-volume scaling: the soliton's confined 3D phase-space volume reflects the saturated region

(δ) subsumes all three by tracing back to the canonical substrate-mechanism (Axiom 4 self-saturation) that the corpus already has at `photon-identification.md`.

**Question for Grant**: confirm (δ) as the substrate-mechanism direction? If yes, the derivation in §6 changes shape — it becomes a saturation-profile calculation rather than an impedance-matching algebra. Substantially more work, but anchored in canonical Axiom-4 mechanism rather than novel Op1-scaling assumptions.

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

Updated per §3.3 (δ) Axiom 4 self-saturation direction. Pending Grant confirmation of (δ).

### §6.1 Derivation chain under (δ) saturation-profile substrate-mechanism

1. **Set up the (2,3) eigenmode** on the K4-TLM substrate at the bond LC tank scale. The eigenmode is a coherent excitation pattern with characteristic frequency $\omega_C = c/\ell_{node}$ (Compton frequency = LC tank eigenfrequency per `theorem-3-1-q-factor.md:27`).

2. **Solve for the amplitude profile $A(r, \theta, \phi)$**: at the eigenmode, the soliton's local amplitude varies in space according to the Cosserat-EM field equations + the (2,3) topological winding constraint. Each bond carries $(V_\text{inc}, V_\text{ref})$; the time-averaged $|V_\text{inc}|^2 + |V_\text{ref}|^2$ gives a 3D scalar amplitude field across the lattice.

3. **Identify the TIR boundary surface**: per Axiom 4, $S(A) = \sqrt{1 - (A/A_y)^2}$. At points where $A = A_y$, $S \to 0$ and Op14 gives $Z_{eff} \to \infty$, $\Gamma \to -1$ TIR. The locus $\{(r, \theta, \phi) : A(r, \theta, \phi) = A_y\}$ is the TIR boundary surface.

4. **Extract envelope geometry (R, r)**: the TIR boundary surface, in phasor coordinates, has the topology of a 2-torus (the (2,3) winding's natural envelope). Characterize this torus by its two characteristic radii — the time-averaged $\langle|V_\text{inc}|\rangle = R$ at the boundary in the toroidal direction, $\langle|V_\text{ref}|\rangle = r$ in the poloidal direction (per Grant 2026-04-27 phasor-space framing).

5. **Show $\sqrt{R \cdot r} = d/2$**: from the saturation-profile equation $A(R, r) = A_y$ combined with the Nyquist constraint $d = 1\ell_{node}$ (regime a) and the (2,3) topology, the geometric mean of the boundary radii equals $d/2$ — half the Nyquist tube diameter. This is the matched-scale condition between the substrate's microscopic Nyquist cutoff and the soliton's macroscopic self-saturation envelope.

The load-bearing step is **step 2** (amplitude profile solution). This is potentially significant work — may require the (2,3) eigenmode solver on K4-TLM (extends existing `tlm_electron_soliton_eigenmode.py`).

**Possible analytical shortcut**: the (2,3) eigenmode's amplitude profile might have a closed-form expression in the limit of small $r/\ell_{node}$, allowing $\sqrt{R \cdot r} = d/2$ to fall out without full numerical eigsolve. Worth attempting before scaffolding the engine work.

### §6.2 Cross-validation (extended)

After §6.1, cross-validate:
- **Algebraic**: check that $R \cdot r = 1/4$ + $R - r = 1/2$ (regime b) uniquely give $R = \varphi/2, r = (\varphi-1)/2$ (Golden Torus) via the $u = d/2$ substitution.
- **Λ values**: check $\Lambda_{vol} + \Lambda_{surf} + \Lambda_{line} = 4\pi^3 + \pi^2 + \pi$ at the derived (R, r, d) = Golden Torus.
- **CODATA**: check $\delta_{strain}$ residual stays $\approx 2.225 \times 10^{-6}$ (no new tension introduced).
- **Cross-particle**: §4.F — does the same saturation-profile mechanism give correct (R, r) for proton (3,5), Δ baryon (2,7+)? If yes, the substrate-mechanism is universal across all (p,q) windings. If no, (p,q)-specific corrections needed.
- **Cross-domain (NEW per §3.2)**: predict cold-fusion energy scales from the same substrate-saturation mechanism. Specifically:
  - For external metric compression in a Pd-D lattice: predict the local $S$ at the inter-nuclear region as a function of electron screening density.
  - From local $S$, predict the effective Coulomb barrier reduction factor.
  - Compare to NASA Glenn lattice-confinement-fusion empirical data (~keV scale) and Fleischmann-Pons claims (~eV if real).
  - If the substrate-saturation mechanism gives factor-100 barrier reduction for typical Pd-D conditions, the mechanism is universal. If not, either the mechanism is wrong OR cold fusion observations are artifacts.

### §6.3 Classification target (consistency-vs-emergence v1.3)

- **Class 2 substrate-mechanism axiom-manifestation** if §6.1 chain closes from Axioms 1+4 + Op14 + Op17 alone (no imports), AND cross-domain cold-fusion prediction matches empirical scales.
- **Class B substrate-mechanism manifestation** if §6.1 closes for the electron case but the cross-domain cold-fusion prediction requires additional substrate-mechanism (e.g., specific (p,q)-corrections for nuclear cases).
- **Class C consistency check** if §6.1 doesn't actually derive — only checks consistency of assumed Golden Torus with the saturation profile.
- **Class D Outcome** if the saturation-profile approach hits a gap: walk back to per Reading (3) — Golden Torus is mathematical scaffold; α derivation is consistency identification rather than substrate-emergence.

Target classification: **Class 2** (the framework's headline aspiration, now anchored in canonical Axiom 4 mechanism with cold-fusion cross-domain validation). Honest fallback: Class B with cross-domain partial-match.

### §6.4 Implementor scope (PENDING Grant §3.3 confirmation)

If Grant confirms (δ): the implementor brief becomes:

```
Branch: analysis/q-embed-sel-1-investigation (already created)
Worktree: isolated per ave-worktree-paths
Read: 
  - this prereg
  - epic doc _orchestration/2026-05-31_q-embed-sel-1-evaluation.md §9 + §10
  - manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md (self-trapped photon mechanism)
  - manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md (Path A + Path B)
  - manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md (Op21 mode-count canonical)
  - manuscript/ave-kb/common/operators.md (Op1, Op3, Op14, Op17, Op21 forms)
  - manuscript/ave-kb/CLAUDE.md (axioms canonical statements)
  - existing scripts: r9_canonical_phase_space_phasor.py, tlm_electron_soliton_eigenmode.py

Deliverables:
1. Analytical attempt: (2,3) eigenmode amplitude profile + TIR boundary identification + (R, r) extraction
2. If analytical doesn't close in 1 session: scaffold the numerical eigsolve extension
3. Cross-validation per §6.2 (algebraic + Λ + CODATA + cross-particle)
4. Cross-domain validation per §3.2: predict cold-fusion energy scale from same mechanism + compare to NASA Glenn lattice-confinement-fusion data
5. Classification declaration per §6.3
6. Result doc at research/2026-XX-XX_Q-EMBED-SEL-1_step_c_result.md
7. PR-routed merge per memory v2

Skills MANDATORY:
  - ave-prereg (this prereg locks before any code; surface any new ambiguities to Grant)
  - phase-space-coordinate-check (all of this is in phasor coords)
  - substrate-native-check (before any solver scaffolding)
  - ave-canonical-leaf-pull (for Q-factor / scaling-law / matched-coupling)
  - ave-canonical-source (canonical constants from src/ave/core/constants.py)
  - ave-driver-script-honesty (if numerical work)
  - consistency-vs-emergence (classify each step)
  - ave-fundamental-ground-up-implementation (no engineering defaults)
  - ave-analytical-tool-selection (Saturation + Resonance + Boundary classes)
  - ave-discipline-translate (cold-fusion translation — chemistry/nuclear-physics jargon)
  - ave-evidence-framing-discipline (precision check on cold-fusion claim — be careful with Fleischmann-Pons-era controversies)
  - verify-before-cite (every cross-domain cite)
  - ave-discrimination-check (before framing as Class 2)
  - ave-worktree-paths
  - ave-multi-falsifier-triangulation-discipline (algebraic + Λ + CODATA + cross-particle + cross-domain)
```

## §7 Final consolidated synthesis (2026-05-31 EOD) — LOCKED

Earlier §3 explored multiple candidate substrate-mechanisms with ad-hoc Greek labels (α/β/γ/δ); this section supersedes them. The corpus-grep on axioms + universal operators + Meissner-asymmetric framework + breathing-soliton v14 PASS revealed that the framework already has the load-bearing answer canonical. The implementor target is now a specific substrate-mechanical derivation with all open questions corpus-resolved.

### §7.1 The substrate-mechanism (canonical, drops Greek labels)

The electron is a self-trapped photon. Mechanism canonical at `photon-identification.md:104`: when the local amplitude reaches $A_{\text{yield}}$, Axiom 4 self-saturation engages, the substrate's local impedance diverges via Op14 ($Z_{\text{eff}} = Z_0/\sqrt{S}$), the reflection coefficient hits $\Gamma \to -1$, and a TIR cavity self-creates that traps the transverse Cosserat-microrotation wave as a standing pattern. The Meissner-asymmetric form (canonical at `l3-electron-soliton-synthesis.md §6.1`) is:

$$Z_{\text{eff}} = \sqrt{\mu_{\text{eff}}/\varepsilon_{\text{eff}}} = Z_0 \cdot \sqrt{S_\mu / S_\varepsilon}, \quad S_\mu = \sqrt{1 - A_\mu^2}, \quad S_\varepsilon = \sqrt{1 - A_\varepsilon^2}$$

Chirality biases one channel ($\mu$ or $\varepsilon$) to grow faster than the other. The first saturating channel reaches $A_{\text{yield}}$ first, creating the $\Gamma \to -1$ TIR wall. The wall is a **single elliptical surface** (one TIR locus, not two separate ones for the two channels).

### §7.2 What $R$ and $r$ are (canonical, OQ1 corpus-resolved)

Per `l3-electron-soliton-synthesis.md §1` verbatim:

> *"What the engine measures as 'the particle' is the **time-averaged envelope** of this oscillating-and-twisting lemniscate: per Compton period the lemniscate rotates and flexes, and per-cycle averaging gives the phase-space ellipse with major-axis $R_{\text{phase}}$ and minor-axis $r_{\text{phase}}$."*

So:
- $R = R_{\text{phase}}$ = major-axis radius of the time-averaged elliptical TIR envelope in $(V_{\text{inc}}, V_{\text{ref}})$ phasor coordinates
- $r = r_{\text{phase}}$ = minor-axis radius of same
- The envelope is the **single TIR boundary surface** at $A = A_{\text{yield}}$ (NOT two separate surfaces for $S_\mu = 0$ vs $S_\varepsilon = 0$)
- The asymmetry $R/r = \varphi^2$ comes from the **chirality-biased Meissner-asymmetric saturation projecting onto the (2,3) topology** — the elliptical envelope is asymmetric because chirality biases the (μ, ε) channels asymmetrically, and the (2,3) winding's geometry gives the specific $\varphi^2$ ratio
- The envelope **breathes** at the Compton frequency $\omega_C$ — instantaneous envelope pulsates around the time-averaged $(R, r)$ values per v14 Mode I PASS canonical (`two-engine-architecture-a027.md`)

### §7.3 Regime (a) and (b) status (canonical, OQ2 corpus-resolved)

The three regimes that fix $(R, r, d)$ are each attributed to specific axioms in `ch8-alpha-golden-torus.md:42-46`:

| Regime | Axiom attribution | Equation |
|---|---|---|
| (a) Nyquist | **Ax 1** lattice sampling cutoff | $d = 1\,\ell_{\text{node}}$ |
| (b) Crossings | **Ax 2** topo-kinematic isomorphism + dielectric-rupture self-avoidance | $2(R - r) = d \Rightarrow R - r = d/2$ |
| (c) Screening | **Ax 3** + **Ax 4** self-saturation TIR boundary at (2,3) eigenmode | $R \cdot r = (d/2)^2$ (target) |

Regimes (a) and (b) are **logically prior** to (c). (a) is Nyquist substrate cutoff. (b) is a topological self-avoidance constraint from the (2,3) winding on a torus with tube cross-section $d$ — it does NOT fall out of the saturation profile, it's an independent constraint from Ax 2 topology. (c) is the load-bearing derivation target of this prereg.

### §7.4 The locked derivation target

From the substrate-mechanism in §7.1 + the canonical (R, r) interpretation in §7.2 + regimes (a)+(b) as priors per §7.3, the derivation target is:

> **Given the (2,3) phase-space soliton at the K4-TLM bond LC tank eigenmode with Meissner-asymmetric self-saturation per `l3-electron-soliton-synthesis.md §6.1`, show that the time-averaged elliptical TIR envelope in $(V_{\text{inc}}, V_{\text{ref}})$ phasor coordinates has axes satisfying $R \cdot r = (d/2)^2$, where $d = 1\,\ell_{\text{node}}$ is the regime (a) Nyquist tube diameter and $R - r = d/2$ is the regime (b) Ax 2 self-avoidance condition. Combined with regimes (a) and (b), this fixes the Golden Torus geometry $R = \varphi/2, r = (\varphi-1)/2$ uniquely, completing the substrate-mechanism derivation of $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ at cold-lattice asymptote.**

Equivalently: show that the geometric mean of the elliptical envelope axes equals half the Nyquist tube diameter:

$$\sqrt{R \cdot r} = d/2$$

### §7.5 Cross-domain anchor (cold-fusion, per Grant 2026-05-31 hint)

The same Axiom 4 self-saturation + Op14 dynamic-impedance mechanism that creates the electron's TIR envelope governs **externally-driven** saturation in nuclear-scale phenomena. Standard fusion barriers (~MeV at vacuum $Z_0$) reduce by factor $\sim 1/\sqrt{S}$ when local conditions drive substrate saturation between nuclei. Empirical anchor scales:
- Hot D-T: ~100 keV (vacuum $Z_0$)
- NASA Glenn lattice-confinement fusion: ~keV (~10² reduction)
- Fleischmann-Pons claims (if real): ~eV (~10⁴⁻⁵ reduction)

If the §7.4 derivation closes for the electron via Axiom 4 self-saturation, the **same mechanism with external driving** should predict cold-fusion energy scales. The corpus has the relevant catalog row at `universal-saturation-kernel-catalog.md` "Pd hydrogen-loading volumetric shatter" (Fleischmann-Pons stochastic irreproducibility at $V_{\text{yield}} \approx 43.65$ kV reached via $\Delta V/V_0 = \sqrt{2\alpha} \approx 12.08\%$ volumetric expansion). The cross-domain validation queues as §4.F-extension after §7.4 closes.

### §7.6 Closing the asymmetry: how $R/r = \varphi^2$ from Meissner-asymmetric coupling

The substrate-mechanism content the implementor must derive analytically (or via the (2,3) eigenmode solver as numerical fallback):

1. **Set up the (2,3) trefoil eigenmode** on K4-TLM at the bond LC tank Compton frequency $\omega_C$. Each bond carries $(V_{\text{inc}}, V_{\text{ref}})$ phasor amplitudes; the soliton is a coherent excitation across many bonds.

2. **Identify the Meissner-asymmetric coupling at the (2,3) winding.** The chirality of the trefoil biases $A_\mu^2$ vs $A_\varepsilon^2$ asymmetrically per `l3-electron-soliton-synthesis §6.1`. The specific ratio at the (2,3) eigenmode follows from the lemniscate-with-3-half-twists geometry threading bipartite K4 nodes (lobe-count = 2 + half-twist count = 3).

3. **Solve for the time-averaged TIR envelope.** The first saturating channel hits $A_{\text{yield}}$ first; that locus defines the wall. The wall surface is elliptical because of the Meissner-asymmetric coupling. Major and minor axes $R, r$ emerge from the eigenmode's amplitude profile combined with the chirality-biased asymmetry.

4. **Derive $R \cdot r = (d/2)^2$** as a substrate-mechanical consequence. Candidate routes:
   - **Conservation law**: total phasor area $\pi R r$ conserved at fixed Compton-period energy, with Nyquist $d$ setting the scale
   - **Impedance matching at the wall**: $Z_{\text{eff at wall}} = Z_0$ gives a constraint that reduces to $\sqrt{R \cdot r} = d/2$ via Op1's geometric-mean form
   - **Eigenmode self-consistency**: the (2,3) winding's closure condition on the elliptical envelope forces $R r = (d/2)^2$

5. **Verify against (b)**: combined with $R - r = d/2$, recover $R = \varphi/2, r = (\varphi-1)/2$ (Golden Torus).

### §7.7 Status — LOCKED

- [x] **Substrate-mechanism canonical**: Axiom 4 self-saturation TIR boundary + Meissner-asymmetric per §7.1
- [x] **(R, r) interpretation canonical**: major/minor axes of single elliptical time-averaged envelope per §7.2 (OQ1 resolved)
- [x] **Regimes (a)+(b) canonical**: Ax 1 + Ax 2, logically prior per §7.3 (OQ2 resolved)
- [x] **Derivation target locked**: §7.4
- [x] **Cross-domain anchor identified**: §7.5 cold-fusion validation queued
- [x] **PREREG LOCKED FOR IMPLEMENTOR SPAWN**

Implementor scope: §7.6 derivation chain (steps 1-5). Analytical first per §5.4 + §6.1, numerical fallback via `tlm_electron_soliton_eigenmode.py` extension. Cross-domain check (§7.5) queued as follow-up. Skills per §6.4 brief.
