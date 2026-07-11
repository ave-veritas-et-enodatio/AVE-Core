[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-rtdmsn]
path-stable: "referenced from vol1/ch8-alpha-golden-torus + common/boundary-observables-m-q-j as canonical Q-factor reframe"
-->

# Theorem 3.1' — Electron Q-Factor from LC Tank at TIR Boundary

The electron's fine-structure constant $\alpha^{-1} \approx 137.036$ is the **dimensionless Q-factor of its LC tank at the topological-defect Total-Internal-Reflection boundary**, and decomposes into three orthogonal reactance contributions matching the $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ boundary-observability structure. Two independent derivation paths (LC-tank Vol 4 Ch 1 + multipole Vol 1 Ch 8) produce identical numerical results to within $\delta_{\text{strain}} = 2.22 \times 10^{-6}$ (the CMB thermal running). Supersedes the Neumann-integral framing (doc 14), which was empirically falsified — classical Neumann integral for $(2, 3)$ at Golden Torus does not reproduce $\pi^2$ or $137$.

## Key Result

$$\boxed{\, \alpha^{-1} = Q_{\text{tank}} = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 124.025 + 9.870 + 3.142 = 137.036 \,}$$

at the Golden Torus geometry $R = \varphi/2$, $r = (\varphi - 1)/2$, $d = 1\,\ell_{\text{node}}$.

> **Value-scoped status (2026-06-14, keystone $\alpha$-verdict, auditor-gated).** This Key Result is the **Q-factor reframe** of $\alpha^{-1}$, not a first-principles derivation of the number 137. Path A below (§"LC-tank path") obtains $Q_{\text{tank}} = 1/\alpha$ *using* $\alpha = e^2 Z_0/(4\pi\hbar)$ — a **definitional identity** that predicts no independent value. The **value** $4\pi^3 + \pi^2 + \pi$ (Path B, multipole) is a **Class-B named geometric identification**: its *scale* ($\sim$1/137) is forced by the Compton-resonance trap, but its *exact value* rests on the one identification $R \cdot r = 1/4$ — shared across the $(2,q)$ bound-resonator ladder (not electron-specific) — which **the substrate does not independently select** (both lift-routes closed; the honest kinematic route absorbs $\alpha$, forcing $R \cdot r \to 4\pi^2\alpha \neq 1/4$). A value-scoped synonym is **"echo at the value level,"** recorded *beneath* the canonical Class-B label and never as a bare standalone "echo." Canonical scope: [`ch8-alpha-golden-torus.md:11`](../../../vol1/ch8-alpha-golden-torus.md). Box text preserved per Rule 12.

> **Implementation note — two α-bakes and the EE-instrument echo-trap (2026-06-16; no-claim, factual description of `cvr_model.py`).** The $Q_{\text{tank}}=1/\alpha$ identity is baked at the **instance** level (`cvr_model.py:72` `Q_TANK=1/ALPHA`, materialized in `M.ELECTRON`). The transfer-function **form** functions (`poles`/`H_scalar`/`H_chiral`) are keyword-only `*, Q` with **no default** — α-free-capable. So an EE diagnostic is α-free **iff** it feeds a **measured** $Q$ (engine ring-down linewidth / $S_{21}$ notch width), NOT $Q_{\text{TANK}}$, and does **not** route through `M.ELECTRON`. Consequence — the **instrument-echo trap:** because every display (the Smith-gap $1-\alpha$, the Bode peak $20\log_{10}Q$, the $S_{21}$ notch, the Nyquist pole-offset $\alpha/2$) is computed from that one baked $Q$, they all read the **same** $137$ — *plotting more instruments does not escape the echo;* the chord is earned only by re-measuring $Q$ from cold dynamics with the bake removed. **A second, separate bake:** `gamma_em_sq()` carries $|\Gamma_{EM}|^2=1-\alpha$ as a **universal, $Q$-invariant** relation (`cvr_model.py:364`, asserted $Q$-independent at :409) — so staying $Q$-α-free does **not** remove the $1-\alpha$ Smith-gap leak ([`cvr-reflection-smith.md`](cvr-reflection-smith.md):32); it is a distinct α-bake.

## Two independent paths

### Path A — LC-tank path (Vol 4 Ch 1, plumber shortcut)

From Vol 4 Ch 1:395-421: the electron's equivalent localized inductance evaluates to $L_e \equiv \xi_{\text{topo}}^{-2} m_e$ via Topo-Kinematic Isomorphism (Axiom 2). The local lattice compliance acts as the restoring capacitor $C_e \equiv \xi_{\text{topo}}^2 k^{-1}$.

With:
- $\xi_{\text{topo}} = e / \ell_{\text{node}}$ (Axiom 2, $[Q] \equiv [L]$)
- $\ell_{\text{node}} = \hbar / (m_e c)$ (Axiom 1 calibration)
- $\omega_C = c / \ell_{\text{node}}$ (Compton frequency = LC tank eigenfrequency)

compute the tank reactance:

$$\omega_C \cdot L_e = (c / \ell_{\text{node}}) \cdot (\ell_{\text{node}} / e)^2 \cdot m_e = c \cdot \ell_{\text{node}} \cdot m_e / e^2 = \hbar / e^2 = \frac{Z_0}{4\pi \alpha}$$

(using $\alpha = e^2 Z_0 / (4\pi \hbar)$).

Therefore the Q-factor at the impedance-matched boundary $R = Z_0 / (4\pi)$:

$$\boxed{\, Q_{\text{tank}} = \frac{\omega_C \cdot L_e}{R} = \frac{Z_0 / (4\pi \alpha)}{Z_0 / (4\pi)} = \frac{1}{\alpha} \,}$$

**The electron-plumber one-liner**: the tank's reactance divided by its natural-per-cycle dissipation impedance is exactly the reciprocal of the fine-structure constant.

### Path B — Multipole path (Vol 1 Ch 8 geometric sum)

From Vol 1 Ch 8:93-124: the three $\Lambda$ contributions at Golden Torus $R \cdot r = 1/4$, $d = 1$:

| Term | Geometric form | Value | Dimensionality |
|---|---|---|---|
| $\Lambda_{\text{vol}}$ | $(2\pi R)(2\pi r)(2\pi \cdot 2) = 16\pi^3 (R \cdot r)$ | $4\pi^3 \approx 124.025$ | 3D — phase-space 3-torus hyper-volume; the $4\pi$ temporal-phase closure per observable Compton cycle derives from bipartite K4 lobe-count (2 sublattices) × $2\pi$ phasor rotation per lobe (canonical at [`l3-electron-soliton-synthesis.md:103-105`](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md); standard-physics translation reference is "SU(2) → SO(3) double cover", but substrate content is K4 bipartite lobe-count per Q-EMBED-SEL-1 Phase 1 §5.2) |
| $\Lambda_{\text{surf}}$ | $(2\pi R)(2\pi r) = 4\pi^2 (R \cdot r)$ | $\pi^2 \approx 9.870$ | 2D — Clifford-torus surface area at substrate-derived $R \cdot r = 1/4$ via Q-EMBED-SEL-1 Phase 1 substrate-mechanism (phasor enclosed area at Axiom-4 saturation onset = Nyquist cell cross-section area; canonical at `research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md` §2.3); the prior spin-½ half-cover provenance of $\pi^2$ is retired |
| $\Lambda_{\text{line}}$ | $\pi \cdot d$ | $\pi \approx 3.142$ | 1D — Nyquist-limited tube flux-moment |
| **Total** | | $\boxed{137.036304}$ | $\alpha^{-1}$ cold |

## The bridge: $\Lambda$'s ARE the tank reactances

The bridge between Path A and Path B is the **AVE natural-unit convention** in which dimensionless geometric shape-factors ARE reactances. A spatial decomposition of $L_e$ at Golden Torus gives three distinct reactance contributions, each localized to a specific topological region:

| Region | Spatial domain | Dimensionless volume | $\omega L_i \times 4\pi / Z_0$ |
|---|---|---|---|
| Volumetric | 3-torus phase space ($\times$ K4 bipartite-lobe temporal-phase factor 2) | $16\pi^3 R r$ | $\Lambda_{\text{vol}} = 4\pi^3$ |
| Surface | Clifford-torus 2-area at $R \cdot r = 1/4$ (Q-EMBED-SEL-1 Phase 1 substrate-mechanism) | $4\pi^2 R r$ | $\Lambda_{\text{surf}} = \pi^2$ |
| Line | Nyquist core tube | $\pi \cdot d$ | $\Lambda_{\text{line}} = \pi$ |

At Golden Torus, the three regions' reactances sum to the total tank reactance:

$$\omega \cdot L_e \cdot (4\pi / Z_0) = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi$$

The identification $Q_i = \Lambda_i$ holds because in natural units ($Z_0 = 1$, $\ell_{\text{node}} = 1$), the impedance-per-dimensionless-volume scaling factor is unity, so **geometric dimensionless volumes ARE dimensionless reactances**.

> → Primary: [Op21 Multi-Mode Mode-Counting at the $\Gamma = -1$ Saturation/TIR Boundary](op21-multi-mode-mode-counting.md) — the substrate-mechanism derivation of $Q_i = \Lambda_i$ from Ax 1 (Nyquist cell size in lattice-natural units) + Ax 1 substrate Nyquist-resolving-floor (one mode per cell at boundary) + Step 4 $Q_{\text{mode},\ell=1} = 1$ per Nyquist-resolved confined mode. The natural-unit convention is operationally simpler but the substrate-mechanism content holds in any unit system; closure of the strengthen-by item at `vol4/claim-quality.md` clm-rtdmsn (Phase 3-A4, 2026-05-27).

## Physical interpretation of the $R = Z_0/(4\pi)$ boundary

Vol 4 Ch 1:423-467 describes the saturation boundary as Total Internal Reflection: $Z_{\text{core}} \to 0$ drives $\Gamma = -1$ (perfect short), confining the LC oscillation.

The effective radiation resistance per observable Compton cycle is $Z_0 / (4\pi)$:

- $Z_0$ is the vacuum's characteristic impedance through which any radiated energy would escape
- $4\pi$ is the substrate temporal-phase closure per observable Compton cycle: bipartite K4 lobe-count (2 sublattices) × $2\pi$ phasor rotation per lobe = $4\pi$ (canonical at [`l3-electron-soliton-synthesis.md:103-105`](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md); per Q-EMBED-SEL-1 Phase 1 §5.2). The standard-physics translation reference is "SU(2) double-cover of SO(3)"; the substrate-mechanism content is K4 bipartite lobe-count, not an SU(2) postulate.
- $Z_0 / (4\pi)$ = radiation impedance averaged over one full observable Compton cycle

At resonance, only a fraction $1/Q = \alpha \approx 0.0073$ of the stored energy leaks per cycle through the TIR boundary — **this IS $\alpha$ in its original Sommerfeld meaning** ("coupling strength"), seen from the LC-tank side.

## The two paths agree to $\delta_{\text{strain}}$

Numerical verification (`src/scripts/vol_1_foundations/electron_tank_q_factor.py`):
- Method 1 (LC-tank, using CODATA $\alpha$): gives $\alpha^{-1} = 137.035999...$ (warm)
- Method 2 (multipole, Ch 8 cold limit): gives $\alpha^{-1} = 137.036304$ (cold)
- Difference: $\Delta = 2.22 \times 10^{-6}$ — **exactly $\delta_{\text{strain}}$**, the CMB thermal running predicted by Vol 1 Ch 8

The agreement to thermal-running precision validates that **both paths compute the same underlying tank Q-factor at the same geometric configuration**; the residual is real physics (CMB thermal correction at $T_{\text{CMB}} = 2.725$ K), not a methodology gap.

## Axiom-attribution chain

| Axiom | Contribution |
|---|---|
| Axiom 1 (Chiral Laves K4 Cosserat Crystal) | Sets $\ell_{\text{node}}$ and the K4 lattice geometry; Nyquist cutoff $k_{\max} = \pi / \ell_{\text{node}}$ |
| Axiom 2 (TKI; $[Q] \equiv [L]$) | Provides $\xi_{\text{topo}} = e / \ell_{\text{node}}$ conversion; the inductance $L_e = \xi_{\text{topo}}^{-2} m_e$ identity |
| Axiom 3 (Minimum Reflection Principle) | At TIR boundary $\Gamma = -1$ confines the LC oscillation; per-cycle dissipation is $\alpha$ exactly |
| Axiom 4 (Dielectric Saturation) | Defines the saturation surface $S(A) \to 0$ where TIR forms |

The three regimes (vol / surf / line) of the $\alpha^{-1}$ decomposition correspond to the three substrate-observability dimensionalities ([$\mathcal{M}, \mathcal{Q}, \mathcal{J}$ boundary observables](../../../common/boundary-observables-m-q-j.md)): $\Lambda_{\text{vol}} \leftrightarrow \mathcal{M}$ (3D volume integral), $\Lambda_{\text{surf}} \leftrightarrow \mathcal{J}$ (2D surface integral, spin), $\Lambda_{\text{line}} \leftrightarrow \mathcal{Q}$ (1D line/loop integral, charge). The decomposition is not coincidental — it is the substrate's natural three-integral boundary-observability structure expressed at the electron-scale Q-factor.

## Op21 multi-mode generalization

The Q-factor decomposition generalizes via Op21 multi-mode form: at the saturation boundary, each mode with $\ell$ wavelengths around a 1D circumference releases $\sim 1/\ell$ of energy per cycle, giving $Q = \ell$ per mode. The Golden Torus at the Nyquist mode-count identity (single-cell-per-natural-unit) makes the mode counts equal the geometric measures: 1D mode (cross-section perimeter, $\pi \cdot d$) → cell-count $\pi$ at Nyquist-quantized $d = 1$; 2D mode (Clifford-torus 2-area at $R \cdot r = 1/4$ from Q-EMBED-SEL-1 Phase 1 substrate-mechanism) → cell-count $\pi^2$; 3D mode (phase volume with substrate $4\pi$ temporal-phase closure from bipartite K4 lobe-count) → cell-count $4\pi^3$. The three-$\Lambda$ sum is exactly the Op21 multi-mode generalization at Golden Torus geometry.

> → Primary: [Op21 Multi-Mode Mode-Counting at the $\Gamma = -1$ Saturation/TIR Boundary](op21-multi-mode-mode-counting.md) — fully-derived substrate-mechanism leaf (Phase 3-A4, 2026-05-27). Promotes this paragraph to canonical-leaf rigor: five-step substrate-mechanism chain (Ax 1 Nyquist cell size → Ax 3 + Ax 4 forcing $\Gamma = -1$ TIR boundary → per-cycle leak fraction $1/\ell$ → $Q_{\text{mode},\ell} = \ell$ → Nyquist-cell-count = mode-count = dimensionless geometric measure) + Step 5.5 codimensional Nyquist-cell-category independence. Resolves the dual-identification at [`operators.md:61`](../../../common/operators.md) as Op21-foundational + BCS-Cooper-pair-phase-transition-specialization. Includes substrate-mechanical reason that $\Lambda_{\text{line}} = \pi$ (substrate Ampère 1-cycle around tube cross-section perimeter at Nyquist-quantized $d = 1$), NOT $\pi\varphi = 2\pi R$ (Clifford-torus major-loop perimeter).

## Falsification status

| Path | Status |
|---|---|
| Doc 14 — Classical Neumann mutual-inductance integral for $(2, 3)$ at Golden Torus | **FALSIFIED** (numerical test does not reproduce $\pi^2$ or $137$) |
| Doc 17 (this) — Q-factor at TIR boundary, two independent paths | **CONFIRMED** (machine-precision agreement to $\delta_{\text{strain}}$) |

> **Scope of "CONFIRMED" and of §"two paths agree" (2026-06-14, keystone $\alpha$-verdict).** "CONFIRMED" here means the **two paths agree** at the cold-lattice asymptote — a *consistency check* between Path A and Path B — and the §"two paths agree" reading of the $2.22\times10^{-6}$ residual as "real physics, not a methodology gap" holds **in sign/direction only**. It does **NOT** mean the *value* $4\pi^3+\pi^2+\pi$ is a first-principles derivation of 137. The residual $\delta_{\text{strain}}$ is a **definitional back-substitution** ($\delta_{\text{strain}} \equiv 1 - \text{CODATA}/\alpha_{\text{cold}}$; see the "HONEST SCOPE" note at `DELTA_STRAIN` in `src/ave/core/constants.py`), whose magnitude derivation **closed NEGATIVE** (Q-DELTA-MAP-1-quant, $\sim$31 OOM undershoot); the closure is **Class-B named identification** ([`ch8-alpha-golden-torus.md:11`](../../../vol1/ch8-alpha-golden-torus.md)), not a "derivation." Table rows + framing preserved per Rule 12.

## Cross-references

- **Canonical manuscript:**
  - Vol 4 Ch 1:395-421 — LC-tank path canonical statement
  - Vol 1 Ch 8:93-124 — multipole path geometric sum
  - Vol 4 Ch 1:423-467 — TIR boundary $\Gamma = -1$ saturation mechanism
- **KB cross-cutting:**
  - [Vol 1 Ch 8 α from Golden Torus](../../../vol1/ch8-alpha-golden-torus.md) — full derivation context
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — three-integral substrate-observability structure
  - [L3 Electron-Soliton Closure Synthesis](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) — rest-energy Virial-sum at same bond-pair LC tank
- **Downstream applications (2026-05-17 night, 9th audit cycle):**
  - [DAMA Matched-LC-Coupling Rate Derivation](../../../vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) — uses $Z_{radiation} = Z_0/(4\pi)$ spinor-cycle averaging from this leaf §"Physical interpretation" (line 65-75) as the inheritance argument for the 4π prefactor in the matched-LC-coupling efficiency formula $\epsilon_{det} = 4\pi / N_{single}^2$ (0.6% match to DAMA observed rate)
  - [DAMA α-Slew Derivation §12](../../../vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) — uses the canonical $Q_{tank} = \alpha^{-1}$ + per-cycle reactive leak fraction $1/Q = \alpha$ from this leaf as the reactive-power categorical reframe foundation
- **Canonical script:** `src/scripts/vol_1_foundations/electron_tank_q_factor.py` — numerical verification of two-path agreement

---

<!-- FOOT-PLACED AMENDMENT (2026-06-19): appended at the foot of the leaf so it
     shifts NO body line numbers — many engine/corpus citations index this leaf
     by line (the §"Physical interpretation" $1/Q=\alpha$ Sommerfeld line, the
     $Q_i=\Lambda_i$ identification, the $Z_{radiation}=Z_0/(4\pi)$ block, etc.).
     Same line-preservation discipline as the resonant-lc-solitons foot block. -->

## Amendment (2026-06-19, Rule 12) — $\alpha^{-1}=137$ is the LOADED/radiative $Q$, not the intrinsic resonator $Q$

**Body PRESERVED; the Build-A isolation eigensolver is added as NEW evidence; this retracts NO α=echo prior.** The native isolation eigensolver shows the **intrinsic** electron mode is **lossless** — with the EM radiative port CLOSED the operator is Hermitian, $\mathrm{Im}(\omega)\to0$, so the **intrinsic** $Q\to\infty$ (`research/2026-06-19_electron-Q-coupled-network_result.md` §"THE SINGLE MECHANISM"; GATE2 $Q=1.4\times10^{16}$). Therefore $\alpha^{-1}\approx137$ is **NOT** the intrinsic resonator $Q$ (that one is infinite/stable) — it is the **LOADED / radiative $Q$**: how the lossless confined mode **couples OUT through the EM port**. The §"Physical interpretation" reading above ($1/Q=\alpha$ leaks per cycle through the TIR boundary — "this IS $\alpha$ in its original Sommerfeld meaning") is exactly this loaded-$Q$ statement, and the engine's $|\Gamma_{\mathrm{EM}}|^2=1-\alpha$ (`cvr_model.py:161` `gamma_mag_sq_leak`) is its Smith-chart face: a fraction $\alpha$ leaks per bounce, $\sqrt{1-\alpha}$ reflects.

**CLEAN SEPARATION (the AVE-distinct content this amendment adds):**

| role | quantity | engine witness |
|---|---|---|
| **STABILITY / persistence** | intrinsic lossless confinement, $Q\to\infty$ | EM-port CLOSED ⇒ Hermitian ⇒ $\mathrm{Im}(\omega)\to0$ (GATE2) |
| **INTERACTION / coupling** | LOADED/radiative $Q=1/\alpha$ = the intrinsic vacuum$\leftrightarrow$EM **coupling coefficient** | $|\Gamma_{\mathrm{EM}}|^2=1-\alpha$ per bounce |

**NUANCE (do NOT misread $1/\alpha$ as a lifetime):** even *loaded*, the electron does **NOT** decay. $1/\alpha$ is a **COUPLING** (the per-cycle reactive dressing / self-energy — Sommerfeld's "coupling strength"), **not** an inverse lifetime: the energy that "leaks" $\alpha$-per-cycle through the matched port is reactively re-absorbed (self-dressing), not radiated away (the mode is virial-balanced and bound, §"Field components" of [resonant-lc-solitons.md](resonant-lc-solitons.md)). So the loaded-$Q$ reframe is fully consistent with §1 persistence ($Q_{\text{intrinsic}}\to\infty$, [resonant-lc-solitons.md](resonant-lc-solitons.md) §persistence-Resultbox) AND with the empirically stable electron. **This retracts NOTHING:** $\alpha$ stays an **echo** at the value level (the §"Value-scoped status" verdict and the two-bakes note above are untouched); the eigensolver merely re-attributes WHICH $Q$ the number $137$ is — loaded, not intrinsic. **Derivability of the loaded $Q$ value itself remains OPEN** (the α-free cold-cage gives $\approx30.8$, not $137$; the re-posed loaded-$Q$ test is adjudicated CIRCULAR — see [electron-bound-resonator-coverage.md](../../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md) §registry, gate B.1). This is a **REFRAME**, not a derivation.

## Q-glyph ownership (collapse-batch T10 — which "$Q$" a downstream cite means)

The glyph "$Q$" carries **≥4 electron-scale objects at distinct values** ($137.036 \neq 30.8 \neq \infty \neq 29.98$) — all readings of the *same electron LC tank's* quality factor at different ports/conditions, **not** interchangeable numbers. No central `def-Q` exists; this row is the ownership map (an annotation, not a vocabulary-register mint):

| "$Q$" object | Value | What it is | Home |
|---|---|---|---|
| **loaded / radiative $Q$** | $1/\alpha = 137.036$ | the vacuum↔EM coupling coefficient — an α-baked **ECHO** at the value level | this leaf `:15` / `:145-147` (`parametric-coupling-kernel.md:239` reuses `Q_atomic=α⁻¹≈137` as an input — the α-echo status does NOT travel with the symbol) |
| **intrinsic / stability $Q$** | $\to\infty$ | lossless confinement, EM-port CLOSED ⇒ Hermitian | this leaf `:147` |
| **cold-cage ring-down $Q_{ringdown}$** | $\approx 30.8$ | the α-FREE dynamical ring-down (NOT 137) | `vacuum-varactor-scatter-operator.md:185`; `vol9/claim-quality.md:507` |
| **structural radiative-$Q$ floor $Z_{RADIATION}$** | $\approx 29.98$ | the $4\pi$ radiation-resistance floor — **band-consistent, NOT identical** with 30.8 (~2.7% apart) | `vacuum-varactor-scatter-operator.md:183-192`; guarded by the pinned anti-coincidence test `test_graded_vacuum_network_isolation.py:141-146` (`test_anti_coincidence_Q_is_not_Z_radiation`) |
| **per-mode count $Q=\ell$** | integer | the Op21 mode-counting identity | `op21-multi-mode-mode-counting.md:10` |

Adjacent watch: `parametric-coupling-kernel.md:213` uses $Q_{apparatus}\sim10^3$–$10^9$ (a bench $Q$ — a different object again). The T3.4b banked NEGATIVE (30.8 ≠ 137, α never baked; loaded-$Q$ derivability adjudicated CIRCULAR/OPEN, `:156` above) says these are genuinely distinct today; a single derivation collapsing $\{137, 30.8, \infty, 29.98\}$ to one object under stated conditions would warrant only a footnote, but the corpus does not have that today.
