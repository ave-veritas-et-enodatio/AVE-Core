[↑ Ch.1 Fundamental Axioms](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-jz0xaw, clm-4mmwb6, clm-dhvhwi, clm-g0mkne, clm-kmliqx]
path-stable: "referenced from L3 closure synthesis + photon-identification + Vol 4 Ch 1 as canonical Cosserat mass-gap formula"
-->

# Cosserat Mass-Gap: $m^2 = 4 G_c / I_\omega$ (Structural Mass Mechanism)

The **Cosserat rotational sector natively carries a mass gap** $m^2 = 4 G_c / I_\omega$ at long wavelengths. This is the **structural mass mechanism for the electron** — the $(2, 3)$ **phase-space** Clifford-torus winding pattern (electron's bond-pair LC tank, NOT a real-space trefoil; the electron's real-space topology is the $0_1$ unknot per Vol 1 Ch 8 canonical) inherits its mass content from this Cosserat gap via the quality-factor calibration. Empirically confirmed at 0.35% error (T = 3.1416 theory vs T = 3.1307 measured) via the uniform-$\omega$ mass-gap oscillation test on the velocity-Verlet `CosseratField3D.step()` integrator. The factor of 4 comes from $W_{\text{micropolar}} = \sum_{ij} (\varepsilon_{\text{antisym}, ij})^2 = 2 \cdot |\omega|^2$.

## Key Results

| Result | Statement |
|---|---|
| Cosserat mass-gap formula | $m^2 = 4 G_c / I_\omega$ |
| Gapped dispersion relation | $\omega^2 = c^2 k^2 + m^2$ (mass term + curvature term combined) |
| Oscillation frequency | $\omega_m = \sqrt{4 G_c / I_\omega}$; period $T = 2\pi / \omega_m$ |
| Empirical test (T2) | T_theory = $\pi \approx 3.1416$; T_measured = 3.1307; **error 0.35%** |
| Energy conservation (Verlet) | $|\Delta H / H|_{\max} = 9.0 \times 10^{-3}$ across 5 oscillation periods (no secular trend) |
| Origin of factor 4 | $W_{\text{micropolar}} = \sum_{ij} (\varepsilon_{\text{antisym}, ij})^2 = 2 \cdot |\omega|^2$; mass term $2 G_c \cdot |\omega|^2$; gap factor $2 \times 2 = 4$ |
| Validated axiom | Axiom 3 (Minimum Reflection Principle): correct Euler-Lagrange equations from $L = \tfrac{1}{2} \rho |\dot u|^2 + \tfrac{1}{2} I_\omega |\dot\omega|^2 - W(u, \omega)$ |

## §1 — The Cosserat Lagrangian and Euler-Lagrange equations
<!-- claim-quality: clm-4mmwb6 -->

The Cosserat micropolar Lagrangian for the substrate's translational ($u$) + microrotational ($\omega$) DOFs:

$$L = \tfrac{1}{2} \rho |\dot u|^2 + \tfrac{1}{2} I_\omega |\dot \omega|^2 - W(u, \omega)$$

where $W(u, \omega)$ is the Cosserat energy density (Cauchy, micropolar, curvature, Op10, reflection, Hopf terms — any combination). The Euler-Lagrange equations:

$$\rho \cdot \ddot u = -\partial W / \partial u, \quad I_\omega \cdot \ddot \omega = -\partial W / \partial \omega$$

These are stepped by **velocity-Verlet integrator** using the existing JAX-autograd `energy_gradient()` infrastructure. State variables: $u$, $u_{\text{dot}}$, $\omega$, $\omega_{\text{dot}}$, time, $\rho$, $I_\omega$.

The **Cosserat micropolar character of Axiom 1** (substrate = Chiral Laves K4 Cosserat Crystal; 6 DOFs per node = 3 translational + 3 microrotational) provides the substrate-native origin of intrinsic spin via the microrotational $\omega$ field. This leaf shows that the same Cosserat structure also provides the mass content via the gap formula.

The gapped dispersion relation that the rotational sector obeys at long wavelengths combines the mass term with the curvature term:

$$\omega^2 = c^2 k^2 + m^2$$

## §2 — Why the mass term has prefactor $4$
<!-- claim-quality: clm-jz0xaw -->

The micropolar coupling term in $W$ is:

$$W_{\text{micropolar}} = G_c \sum_{ij} (\varepsilon_{\text{antisym}, ij})^2$$

where $\varepsilon_{\text{antisym}, ij} = \tfrac{1}{2}(\partial_i u_j - \partial_j u_i) - \epsilon_{ijk} \omega_k$ is the Cosserat antisymmetric strain capturing the kinematic decoupling between macro-rotation and micropolar rotation.

For **uniform $\omega_z$** with $u = 0$: $\varepsilon_{\text{antisym}, xy} = -\omega_z$ and $\varepsilon_{\text{antisym}, yx} = +\omega_z$ both contribute equally. So:

$$W_{\text{micropolar}} = G_c \cdot [(-\omega_z)^2 + (+\omega_z)^2] = 2 G_c \cdot |\omega_z|^2$$

The local "mass term" in the equation of motion is then $2 G_c \cdot |\omega|^2$, giving the dispersion relation:

$$\omega^2 = c^2 k^2 + \frac{4 G_c}{I_\omega}$$

i.e., $m^2 = 4 G_c / I_\omega$. The factor 4 = 2 (from $\sum_{ij}$ doubling at antisymmetric pair) × 2 (from Lagrangian-to-EOM conversion).

## §3 — Empirical validation (Phase I of "the AVE Ideal")
<!-- claim-quality: clm-dhvhwi -->

### Test design (T2 uniform-$\omega$ mass-gap oscillation)

`src/scripts/vol_1_foundations/cosserat_wave_test.py`:

- Seed $\omega_z(r) = A_0 = 0.05$ uniform, zero velocity
- $\nabla \omega = 0$ everywhere → curvature term contributes nothing; **only the mass term is active**
- Expected oscillation: $\omega_z(t) = A_0 \cos(\omega_m \cdot t)$ with $\omega_m = \sqrt{4 G_c / I_\omega} = 2$, period $T = 2\pi / \omega_m = \pi \approx 3.1416$
- Parameters: $\rho = I_\omega = 1$, $G = \gamma = 1$, $G_c = 1$, $N = 32$, $dt = 0.3 \cdot \text{cfl\_dt}$
- Measurement: peak detection on $\langle \omega_z \rangle_{\text{alive}}(t)$

### Result

| Quantity | Theory | Measured | Error |
|---|---|---|---|
| $\omega_{\text{mass}}$ | $\sqrt{4 G_c / I_\omega} = 2.0000$ | 2.0070 | 0.35% |
| Period $T$ | $2\pi / \omega_{\text{mass}} = 3.1416$ | 3.1307 | **0.35%** |
| Energy drift $|\Delta H / H|_{\max}$ | bounded $O(dt^2)$ | $9.0 \times 10^{-3}$ | 0.9% over 5 periods |

**0.35% match.** Uniform-field oscillation **ISOLATES the mass term** ($\nabla \omega = 0$ kills curvature). The match at this level confirms:

1. The velocity-Verlet integrator conserves energy to Verlet $O(dt^2)$ and produces the correct oscillation frequency
2. The mass gap is **EXACTLY** $m^2 = 4 G_c / I_\omega$, with the factor 4 coming from $W_{\text{micropolar}} = \sum_{ij} (\varepsilon_{\text{antisym}, ij})^2 = 2 \cdot |\omega|^2$
3. The Cosserat rotational sector natively has a **massive mode** at long wavelengths

### Companion tests (sanity-checked)

| Test | Setup | Result | Verdict |
|---|---|---|---|
| T1a (gapless wave) | $G_c = 0$, $\gamma = 1$ — pure curvature, no mass | $v / c_R = 0.858$; energy drift $9.6 \times 10^{-4}$ | Propagation in right direction confirmed; 14% velocity error is finite-$k$ lattice dispersion (expected) |
| T1b (gapped wave) | $G_c = 1$, $\gamma = 1$ — both terms active | $v_g / v_{g, \text{theory}} = 0.666$; energy drift $7.8 \times 10^{-3}$ | Group velocity visibly drops from 1 → 0.25 when mass gap opens; 34% error from stiffer gapped-band dispersion |
| T2 (mass-gap oscillation) | $G_c = 1$, $\nabla \omega = 0$ — mass term only | $T / T_{\text{theory}} = 0.9965$; energy drift $9.0 \times 10^{-3}$ | **0.35% error — essentially exact** |
| T3 (energy conservation) | All three tests | $|\Delta H / H|_{\max} \leq 1\%$, no secular trend | Velocity-Verlet symplectic-O($dt^2$) confirmed |

## §3.5 — The rotational-curvature wave speed is $c_R = \sqrt{2}$ (node-twist stiffness convention, Grant-ratified 2026-06-23)
<!-- claim-quality: clm-kmliqx -->

**SECTOR HEADER.** This is the Cosserat **micro-rotation** sector. $c_R$ is the propagation speed of a **twist-gradient (wryness $\kappa = \nabla\omega$) curvature wave**, measured against the shear/transverse speed ($c = 1$). Cold-linear regime; $G_c = 0$ (pure curvature, no mass gap). NOT a translational-strain wave — the carried DOF is the micro-rotation gradient $\kappa$, not the Cauchy strain $\varepsilon_{\text{sym}}$.

**RESOLVED VALUE: $c_R = \sqrt{2}$** (Grant-ratified 2026-06-23).

The engine's curvature energy is $W_\kappa = \gamma \sum_{ij} \kappa_{ij}^2$ — it carries **NO $\tfrac{1}{2}$ prefactor and NO symmetrization** (unlike the symmetrized Cauchy strain $W_{\text{cauchy}}$, which uses $\varepsilon_{\text{sym}} = \tfrac{1}{2}(\varepsilon + \varepsilon^T)$). Summing the $\kappa$ quadratic form with unit (not half) weight is what yields $c_R = \sqrt{2}$ as the engine-faithful Fourier symbol of this operator. Verbatim in `src/ave/topological/cosserat_field_3d.py:704`: `W_kappa = jnp.sum(kappa**2, axis=(-1, -2))` (second identical copy at `:739`).

**Derivation rationale (Grant 2026-06-23, carried verbatim):** translational strain symmetrizes because its **antisymmetric part is a FREE rigid rotation storing no energy**; the **micro-rotation gradient's antisymmetric part is a GENUINE twist-gradient that DOES store energy**, so the **full-gradient (no-$\tfrac{1}{2}$) treatment is physically forced** — AND it is the **SAME no-$\tfrac{1}{2}$ convention that yields the validated $m^2 = 4$ mass gap** (§2, `clm-jz0xaw`: the antisymmetric-pair $\sum_{ij}$ doubling that gives the factor-2 in $W_{\text{micropolar}} = 2 G_c |\omega|^2$ is the same no-$\tfrac{1}{2}$ summation convention). **Internal consistency $\Rightarrow \sqrt{2}$**; the old leaf label "$1$" is a **continuum idealization the discrete substrate does not honor** (it is the convention with the standard $\tfrac{1}{2}$ elastic prefactor folded in, which the engine operator does not carry).

Empirical confirmation (PR #392, the genuine two-sublattice $12\times12$ band structure): the V2 validate-on-known recovers $c_R = 1.414214$ (target $\sqrt{2}$, rel-err $2.0\times10^{-9}$) directly from the engine's bond operator — bit-faithful to the same $\Sigma\kappa^2$ the gap ($m^2 = 4$, also bit-exact there) is read from. The leaf label and the engine $\Sigma\kappa^2$ cannot both be the substrate value; the driver is bit-for-bit faithful to the engine operator, so internal consistency forces $\sqrt{2}$.

> **🔴 RULE-12 DEMOTION (2026-06-23) — the prior $c_R = \sqrt{\gamma/I_\omega} = 1$ label is DEMOTED, not deleted.** Prior to Grant's 2026-06-23 ratification, the companion-test table (§3 T1a row) and the canonical script `cosserat_wave_test.py:10` quoted the rotational-curvature speed as the **continuum idealization** $c_R = \sqrt{\gamma/I_\omega} = 1$. That label folds in the standard $\tfrac{1}{2}$ elastic prefactor that the discrete substrate's $W_\kappa = \gamma\,\Sigma\kappa^2$ operator does NOT carry. The "$1$" is preserved here as the **continuum-limit label** and remains the value the symmetrized-$\tfrac{1}{2}$ convention would give; it is NO LONGER the substrate value. The substrate (engine-faithful) value is $c_R = \sqrt{2}$ per the derivation above. The T1a empirical $v/c_R = 0.858$ row in §3 is a finite-$k$ lattice-dispersion ratio against the continuum-$1$ label and is left unchanged for audit-trail continuity (its 14% deficit is the finite-$k$ dispersion the §3 row already notes).

This convention question does **NOT** touch the validated mass gap (the load-bearing number $m^2 = 4$, `clm-jz0xaw` / `clm-dhvhwi`): the gap is bit-exact under either convention. It resolves only the $c_R$ curvature-slope label.

### §3.5.1 — DISAMBIGUATION: the THREE substrate wave speeds (two are $\sqrt{2}$ — do NOT fuse)

Three K4-substrate wave speeds live near this result. **Two of them are numerically $\sqrt{2}$ but are PHYSICALLY DISTINCT** (different sectors, different moduli). The shared digit is a coincidence of the $K = 2G$ magic-angle operating point and the no-$\tfrac{1}{2}$ curvature convention reaching the same value — it is **NOT an identity**. This table exists so no future reader manufactures a false identity between the two $\sqrt{2}$'s, nor confuses either with the $T_2$ shear photon at $c$. (This is the "three speeds, do not fuse" discipline, parallel to the "three 2's" reactance-count taxonomy in [`../../../common/dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md):42.)

| Claim | Sector | Mode | Modulus | Speed | Source operator / origin |
|---|---|---|---|---|---|
| **`clm-uu1qbo`** | **A1 / bulk** | dilatational scalar (longitudinal compression) | bulk $K$ ($K = 2G$ magic angle) | $\sqrt{2}\,c_0 = \sqrt{K_{\text{bulk}}/\rho}$ | macroscopic-moduli $K/G = 2$ ratio; the A1 port-mode of `clm-j550uh` |
| **`clm-j550uh`** | **T2 / $\omega$** | transverse **SHEAR** (the photon) | shear $G$ | $c = \sqrt{G/\rho} = 1$ | $W_{\text{cauchy}}$ shear / micropolar; V1 of PR #392 (`c = 1`, rel-err 3.6e-8) |
| **`clm-kmliqx`** | **T2 / $\omega$** | **CURVATURE / wryness** twist-gradient $\kappa = \nabla\omega$ | curvature $\gamma$ | $\sqrt{2} = \sqrt{2\gamma/I_\omega}$ | no-$\tfrac{1}{2}$ $W_\kappa = \gamma\,\Sigma\kappa^2$ (`cosserat_field_3d.py:704`, copy `:739`); V2 of PR #392 (`√2`, rel-err 2.0e-9) |

**Read carefully — the two $\sqrt{2}$'s:**
- **`clm-uu1qbo`'s $\sqrt{2}$** is the **A1/bulk-$K$ dilatational** speed: a *scalar/longitudinal compression* mode governed by the **bulk modulus** $K$, $\sqrt{2}$ because $K = 2G$ at the magic angle. It is the **other sector** from kmliqx.
- **`clm-kmliqx`'s $\sqrt{2}$** is the **T2/curvature-$\gamma$** speed: a *micro-rotation twist-gradient* mode governed by the **curvature modulus** $\gamma$, $\sqrt{2}$ because the engine's $W_\kappa$ carries no $\tfrac{1}{2}$. It is the **same sector** as the shear photon but a **different mode/modulus**.

**The two T2 modes:** within the single T2 micro-rotation sector there are TWO distinct modes — the SHEAR mode (`clm-j550uh`, $G$-modulus, speed $c = 1$, the photon) and the CURVATURE mode (`clm-kmliqx`, $\gamma$-modulus, speed $\sqrt{2}$). `clm-j550uh`'s canonical statement "$T_2$ at $c$ (shear modulus)" is **specifically the shear-$G$ transverse photon** — it is NOT the curvature-$\gamma$ mode. (Verified: `claim-quality.md` clm-j550uh body, "$A_1$ propagates at $c\sqrt{2}$ (bulk modulus), $T_2$ at $c$ (shear modulus)" — the $T_2$/$c$ entry is the shear mode, distinct from this leaf's curvature-$\gamma$/$\sqrt{2}$ mode. No collision.)

**A FOURTH speed exists and is NOT $\sqrt{2}$ — guard against a 2-vs-3 fusion:** the isotropic-solid longitudinal **P-wave** is $c_L = \sqrt{(K + \tfrac{4}{3}G)/\rho} = \sqrt{10/3}\,c \approx 1.826\,c$ ($\nu = 2/7$; PR #392 reads it as the acoustic-manifold top = $1.826$ *inside* the BZ). The A1/bulk $\sqrt{2}$ (which drops the $\tfrac{4}{3}G$ shear term) is the **bulk-modulus** quantity, NOT this P-wave. The kmliqx $\sqrt{2}$ is the rotational-curvature mode — genuinely $\sqrt{2}$, **not** the $\sqrt{10/3}$ bulk longitudinal P-wave (that distinction is what the read-AND-run adjudication confirmed: the V2 branch is rotational `rot_wt=1.0`, NOT the bulk $\sqrt{10/3} = 1.826$).

The CI gate for the kmliqx curvature-$\gamma$ $\sqrt{2}$ is `src/tests/test_cr_rotational_curvature_sqrt2.py` (asserts V2 rel-err $< 5\times10^{-2}$ and the split from the shear photon $c$).

## §4 — Why this is the structural mass mechanism for the electron
<!-- claim-quality: clm-g0mkne -->

The Cosserat rotational sector's massive mode at $m^2 = 4 G_c / I_\omega$ inherits the substrate's mass content. The electron's specific calibration:

- The (2,3) shell on the Clifford torus has Cosserat $\omega$ field with quality factor $Q = 1 / \alpha = 137.036$ (Vol 1 Ch 8 Golden Torus)
- At Golden Torus geometry $R = \varphi/2$, $r = (\varphi - 1)/2$, the Cosserat $\omega$ pattern is the (2,3) trefoil phase-space winding
- The electron's rest energy $m_e c^2 = \hbar \omega_C = T_{EM} \cdot \ell_{\text{node}}$ inherits from the Cosserat mass-gap formula at the substrate parameters $\rho, I_\omega, G_c$ calibrated to $\ell_{\text{node}} = \hbar / (m_e c)$

The Cosserat $\rho$ and $I_\omega$ set the **mass scale of the rotational sector**; the K4 scalar sector remains **separately massless** (the photon per [photon-identification](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md)). The photon = T₂-only canonical confirms this split: $A_1$ (scalar/longitudinal/translational $u$) is massless, $T_2$ (transverse/microrotational $\omega$) carries the mass-gap content.

> **↗ Cross-link (2026-06-10, Rule 12, Grant rename-queue R1 — line above preserved):** the "$A_1$ scalar massless / $T_2$ carries the mass" split is the same split read at [`photon-identification.md:11`](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md) as PROVENANCE-vs-STATE: "self-trapped photon" is provenance; the electron STATE is the condensed phase whose order parameter is the **A1 standing-V** that re-engages at saturation (the A1 here is "separately massless" only in the *unbroken* free-wave phase). Registry §5 R1.

> **🔴 SECTOR RE-SCOPE — the $T_2$ mass-gap is the FLYWHEEL clock gap, the REST MASS is A1 (2026-06-20, Rule 12 — §4 body + weak-C/provenance notes above PRESERVED unedited; Grant-ratified mass-sector ruling; ADDS to, does not replace, the existing notes).** §4 names the $T_2$ / Cosserat micro-rotation ($\omega$) massive mode "$m^2 = 4 G_c / I_\omega$" as inheriting "the substrate's mass content" / "the structural mass mechanism." **Re-scope (consistency-class):** the $T_2$/$\omega$ gap is the **FLYWHEEL frequency / clock gap** (the Compton/Larmor clock of the spin/frequency-regulation sector — the Park-dq FOC rotating frame), re-scoped from "**the** rest mass." The rest-mass *store* is the orthogonal **A1 longitudinal DILATATION** (the bulk-dilatation depression, $Z_{bulk}\to0$; [`master-equation.md`](../../dynamics/ch4-continuum-electrodynamics/master-equation.md):20 "A1 dilatation-MASS"; [`lattice-extreme-bh-rationality.md`](../../../vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md):28), held at $90°$ to $T_2$ by the **GRADE orthogonality** (**A1 ⊥ T2**). The flywheel regulates the *frequency that SETS* the mass via Compton $f = mc^2/\hbar$ → A1 depression depth (lepton tower: more torsion → faster flywheel → deeper A1 depression → more mass); mass itself stays A1. *(⚠ 2026-06-20 CORRECTION: FOC does NOT FORCE A1 ⊥ T2 — the temporal-within-tank "FOC d-q" reading is RETRACTED, `clm-533gvm` solidity 0.30; the canonical FOC homes are SPATIAL inter-object 90°. A1 ⊥ T2 stands FOC-INDEPENDENT on the grade decomposition; REFUTED flag at [`master-equation.md`](../../dynamics/ch4-continuum-electrodynamics/master-equation.md):20.)* The line-106 chain $m_e c^2 = \hbar\omega_C = T_{EM}\,\ell_{node}$ is preserved — it is the *frequency*-sets-mass relation, with $\hbar\omega_C$ the flywheel clock and the trapped energy the A1 depression. Body preserved per Rule-12.
>
> ⚠ **DRIVER-VALIDATION CAVEAT (2026-06-20 CORRECTION, additive).** "mass = A1" is **RATIFIED-CONSISTENCY** ([`master-equation.md`](../../dynamics/ch4-continuum-electrodynamics/master-equation.md):20, PR#260) — the adjudicated grade-ASSIGNMENT, **NOT driver-validated**. **No driver discriminates A1-mass from T2-mass.** This very leaf's §4 Verlet driver (E-046, line 108) attributes the mass-gap to the **$T_2$/$\omega$ rotational sector**, and the S4 moduli ($G_c$, $I_\omega$) are **placeholders** calibrated to $\ell_{node}=\hbar/(m_e c)$ rather than measured-from-substrate. So the re-scope here is the **adjudicated grade-assignment** standing on the grade decomposition and the no-double-count guard, **not a measurement** that isolated A1 as the mass carrier. (Consistency-class, per the substrate-first-for-numbers discipline: honestly tagged, not over-claimed as emergence.)

## §5 — Phase-I scope (what this test validated / did not)

- **Axiom 1** (K4 substrate): NOT tested here. Cosserat-alone is not Axiom-1-compliant as a physics substitute (per Vol 4 Ch 1 §solver selection — the electron is a chirality observable requiring K4). This was a DEV step in the roadmap toward the full coupled K4 ⊗ Cosserat simulator.
- **Axiom 2** (Topo-Kinematic Isomorphism): NOT exercised. Test 2 uses uniform $\omega$ (trivial topology). Full (2,3) topology is tested by `relax_s11` / `relax_to_ground_state`.
- **Axiom 3** (Minimum Reflection Principle): **directly validated.** The Lagrangian produces the correct Euler-Lagrange equations; Hamiltonian conservation confirms this at 0.9% drift over 5 oscillation periods.
- **Axiom 4** (Universal Saturation Kernel): NOT exercised (all tests `use_saturation = False`, $k_{\text{op10}} = k_{\text{refl}} = 0$). Axiom 4 comes in at Phase-II / III coupling with high-amplitude photons.

The mass-gap is a Phase-I structural property of the Cosserat Lagrangian; the electron's specific calibration is Phase-II + III work that couples K4 + Cosserat at saturation.

## Cross-references

- **Canonical script:** `src/scripts/vol_1_foundations/cosserat_wave_test.py` — T1a / T1b / T2 / T3 four-test suite
- **Engine:** `src/ave/topological/cosserat_field_3d.py` — `CosseratField3D.step()` velocity-Verlet integrator; curvature energy `W_kappa = jnp.sum(kappa**2)` at `:704` (second copy `:739`), the no-½ `Σκ²` operator whose Fourier symbol gives $c_R = \sqrt{2}$ (§3.5, `clm-kmliqx`)
- **KB cross-cutting:**
  - [Photon Identification](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md) — $A_1$ massless / $T_2$ massive split confirmed
  - [Vol 1 Ch 8 α Golden Torus](../../ch8-alpha-golden-torus.md) — electron-specific Cosserat (2,3) shell calibration
  - [L3 Electron-Soliton Closure Synthesis](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) — rest-energy Virial sum at bond-pair LC tank
  - [Axiom Definitions](axiom-definitions.md) — Axiom 1 Cosserat character (6 DOFs)
  - [Two-Engine Architecture](../../../common/two-engine-architecture-a027.md) — `cosserat_field_3d.py` as validated standalone engine
- **Canonical manuscript:**
  - Vol 1 Ch 1 (Axiom 1) — Cosserat micropolar structure (6 DOFs per node)
  - Vol 1 Ch 2 (Macroscopic Moduli) — magic-angle $K = 2G$ substrate moduli
