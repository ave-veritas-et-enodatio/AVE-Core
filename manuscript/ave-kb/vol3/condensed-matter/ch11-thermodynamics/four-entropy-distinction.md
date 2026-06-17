[↑ Ch.11 Thermodynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-4o0f0h]
-->

# Four Distinct Entropy Quantities at the BH Horizon

AVE has **four physically distinct entropy quantities** for a black hole, measuring different physics. They are NOT redundant; they coexist and have ratios spanning $\sim 10^{44}$ orders of magnitude. The standard Bekenstein-Hawking $S_{BH} = A/(4 \ell_P^2)$ is recovered numerically only via **imported Boltzmann equipartition** that AVE rejects on axiomatic grounds. AVE-native geometric entropy from Vol 3 Ch 11 (Op14 scattering irreversibility) gives $\hat S_{\text{geo}} = A \cdot \log 2 / \ell_{\text{node}}^2$ under A-B interface framing — **$\sim 10^{-44} \times S_{BH}$**, the Machian dilution factor. **The first-law $T \cdot dS = dE$ is the importer**; both axiom-derived pillars (area theorem + mass-energy) hold, but the entropy-temperature relation requires Boltzmann counting that AVE rejects.

## Key Results

| Entropy | Formula | Physical meaning | AVE status |
|---|---|---|---|
| **Geometric $\hat S_{\text{geo}}$** | $\boxed{\hat S_{\text{geo}} = k_B \cdot A \cdot \log 2 / \ell_{\text{node}}^2}$ | Op14 scattering irreversibility at A-B interface horizon cells | **AVE-native** (Vol 3 Ch 11 + doc 61 A-B interface) |
| **Thermodynamic $S_{BH}$** | $S_{BH} = A / (4 \ell_P^2) = 7\xi \cdot A / (4 \ell_{\text{node}}^2) \approx 10^{44} \cdot A / (4 \ell_{\text{node}}^2)$ | First-law-integrated mass-absorption entropy | **Imported from standard GR via first law** |
| **Microstate count** $S_{\mu}$ (hypothetical) | $2^{A / \ell_{\text{node}}^2}$ total states | Binary A-B choice per horizon cell | **Doc 61 §3.2 original** (informal microstate-counting framing) |
| **Volume thermalization $S_v$** | $\approx 4 \cdot A / (4 \ell_P^2)$ | Interior thermalization of ruptured-plasma dissipative sink | **Approximately matches $S_{BH}$; uses Boltzmann counting AVE rejects** |
| Ratio $\hat S_{\text{geo}} / S_{BH}$ | $4 \log 2 / (7\xi) \approx 2.8 \times 10^{-44}$ | Machian dilution factor | — |
| Corpus ruptured-plasma | $\hat S_{\text{corpus}} = 0$ via Op14 with $\Gamma_{\text{horizon}} = 0$ **(EM channel only — see §2 FLAG)** | **EM-channel** symmetric saturation: $Z_{EM}(r) = Z_0$; no *EM* mismatch at horizon. Shear/bulk channels short ($\Gamma_{shear}=-1$) — entropy operator channel-sensitivity FLAGGED 2026-06-17 | Vol 3 Ch 15:19-29 + Ch 21:114 |

## §1 — Vol 3 Ch 11's $\hat S$-operator

From Vol 3 Ch 11:53-68:

$$\hat S = -k_B \sum_i \ln(1 - |\Gamma_i|^2)$$

Sums $-\ln(1 - |\Gamma|^2)$ over every impedance boundary at which wave energy undergoes partial reflection. Entropy is generated per boundary by the irreversibility of scattering.

For a BH horizon: sum over K4 lattice cells crossing the 2D horizon surface at $r = r_{\text{sat}}$:

$$N_{\text{cells}} \approx A / \ell_{\text{node}}^2$$

For each cell we need $|\Gamma|^2$ at the horizon interface.

## §2 — Under corpus ruptured-plasma picture: $\hat S_{\text{corpus}} = 0$

> 🔴 **FLAG → Grant (BH shear-reflect walk-back, 2026-06-17, Rule-12 — flag-don't-fix; NOT recomputed).** This §2 derivation sets $\Gamma_{\text{horizon}} = 0$ from the **EM-channel** invariance $Z_{EM}=Z_0$ — but the 2026-06-17 walk-back established that $\Gamma=0$ is the **EM channel only**; the **shear/bulk** channels short ($Z_{shear}=\rho c_{shear}\to0\Rightarrow\Gamma_{shear}=\Gamma_{bulk}=-1$, see [`electron-bh-isomorphism.md`](../../cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):34–42). The entropy operator $\hat S = -k_B\sum_i\ln(1-|\Gamma_i|^2)$ is **channel-sensitive at the horizon**:
> - EM channel ($\Gamma_{EM}=0$): $\hat S_{EM} = -k_B N\ln(1-0) = 0$ (the result below).
> - Shear/bulk channel ($|\Gamma_{shear}|=1$): $\ln(1-1)=\ln 0 = -\infty$ — the operator **diverges / is out of domain** for *total* reflection (its summand counts *partial*-reflection scattering irreversibility, and $\Gamma=-1$ is lossless total reflection, not partial scattering).
>
> **Open physics question (do not silently resolve):** which channel's $\Gamma$ enters the geometric/Op14 horizon-cell entropy — is BH horizon-cell entropy an EM-scattering quantity (→ 0, as below) or a shear-scattering quantity (→ operator out-of-domain, requiring a different formulation for total-reflection boundaries)? The "$\hat S_{\text{corpus}}=0$ via $\Gamma=0$" result below is **EM-channel-scoped** pending Grant adjudication. Preserved per Rule-12 (no recompute).

Per Vol 3 Ch 15:19-29 + Vol 3 Ch 21:114, **gravity is symmetric saturation** (**EM channel** — see FLAG above): $\mu'(r) = \mu_0 \cdot n(r)$ and $\varepsilon'(r) = \varepsilon_0 \cdot n(r)$ scale together. The **EM-transverse** characteristic impedance is invariant:

$$Z(r) = \sqrt{\mu' / \varepsilon'} = \sqrt{\mu_0 / \varepsilon_0} = Z_0 \quad \text{everywhere, interior and exterior}$$

Reflection at horizon interface between exterior ($Z_{\text{ext}} = Z_0$) and interior ($Z_{\text{int}} = Z_0$):

$$\Gamma_{\text{horizon}} = (Z_{\text{int}} - Z_{\text{ext}}) / (Z_{\text{int}} + Z_{\text{ext}}) = 0$$

**Corpus-ruptured-plasma $\hat S$ at horizon:**

$$\hat S_{\text{corpus}} = -k_B \cdot N_{\text{cells}} \cdot \ln(1 - 0^2) = 0$$

**Corpus picture gives ZERO entropy at the BH horizon via Ch 11's framework — in the EM channel ($\Gamma_{EM}=0$).** *(2026-06-17 FLAG, see §2 banner: this is EM-channel-scoped; the shear/bulk channels reflect totally ($\Gamma_{shear}=-1$), for which the partial-reflection entropy operator is out of domain — open question to Grant whether horizon-cell entropy is an EM- or shear-scattering quantity.)* In the EM channel this is consistent with Vol 3 Ch 21's "dissipative sink, information erased" — there's no EM structure at the horizon to be entropic.

## §3 — Under A-B interface picture: $\hat S_{\text{geo}} = A \log 2 / \ell_{\text{node}}^2$

Per doc 61 §1.2-§1.4: the BH horizon is an A-B sublattice rupture interface. At each K4 cell crossing the 2D horizon, there's a "frustrated bond" — an A-site trying to bond to a B-site that belongs to a differently-seeded (possibly opposite-chirality) patch.

The effective impedance at a frustrated A-B bond: the chirality mismatch means the wave can either (a) reflect back (stay on our side's A-sublattice) or (b) transmit through to the other-side B-sublattice. For a bipartite-symmetric interface, the natural binary amplitude split is:

$$|\Gamma|^2 = 1/2 \quad \text{(equal reflection/transmission at frustrated bond)}$$

This is the BINARY A-vs-B eigenmode — the wave can pick either sublattice with equal amplitude.

**$\hat S$ at horizon under A-B interface picture:**

$$\hat S_{\text{geo}} = -k_B \cdot N_{\text{cells}} \cdot \ln(1 - 1/2) = -k_B \cdot (A / \ell_{\text{node}}^2) \cdot \ln(1/2) = \boxed{k_B \cdot A \log 2 / \ell_{\text{node}}^2}$$

The equivalence isn't coincidence: doc 61 §3.2's derivation counted "1 bit per cell of A/B choice." Ch 11's framework with $|\Gamma|^2 = 1/2$ gives the SAME answer because a 50/50 beam-splitter IS a one-bit entropy-creation event.

**This is AVE-NATIVE geometric entropy** — NOT imported Boltzmann microstate counting; it's the correct application of Vol 3 Ch 11's geometric-entropy operator to the interface structure.

## §4 — Comparison to standard $S_{BH}$

Standard $S_{BH} = A / (4 \ell_P^2) = 7 \xi \cdot A / (4 \ell_{\text{node}}^2) \approx 10^{44} \cdot A / (4 \ell_{\text{node}}^2)$.

Ratio:

$$\hat S_{\text{geo}} / S_{BH} = \frac{A \log 2 / \ell_{\text{node}}^2}{7 \xi \cdot A / (4 \ell_{\text{node}}^2)} = \frac{4 \log 2}{7 \xi} \approx 2.8 \times 10^{-44}$$

**AVE-native $\hat S_{\text{geo}}$ is $\sim 10^{-44} \times$ standard $S_{BH}$.** The ratio is the **Machian dilution factor** — the "efficiency" with which local geometric-scattering events encode macroscopic thermodynamic entropy.

## §5 — Volume thermalization $S_v$ (Boltzmann-imported)

Per Vol 3 Ch 11:14-48 geometric-spreading framing: entropy is also the irreversible spreading of coherent wave energy into transverse modes across the 3D lattice. When a soliton enters a ruptured-plasma region (BH interior), its energy disperses across all available modes.

For the BH interior (volume $V_{\text{int}} \sim r_{\text{sat}}^3$):
- Number of modes $\sim V_{\text{int}} / \ell_{\text{node}}^3$
- Each mode at equipartition gets $\tfrac{1}{2} k_B T_H$
- Total thermalized energy: $N_{\text{modes}} \cdot \tfrac{1}{2} k_B T_H = (V_{\text{int}} / \ell_{\text{node}}^3) \cdot \tfrac{1}{2} k_B T_H$

For energy balance with absorbed mass $M c^2 = (V_{\text{int}} / \ell_{\text{node}}^3) \cdot \tfrac{1}{2} k_B T_H$:

$$V_{\text{int}} / \ell_{\text{node}}^3 = 2 M c^2 / (k_B T_H) = 16 \pi G M^2 / (\hbar c)$$

Entropy from this thermalization (Boltzmann-like counting):

$$S_v \sim N_{\text{modes}} \cdot k_B = 16 \pi G M^2 k_B / (\hbar c)$$

Compare to $S_{BH} = 4 \pi G M^2 k_B / (\hbar c)$: **$S_v / S_{BH} = 4$**.

**Factor-of-4 off from standard $S_{BH}$.** Could be corrected by careful counting (equipartition factor-of-2 + proper geometry). The key point: **volume-thermalization gives entropy with the correct power-of-$M$ scaling ($M^2 \to A$); prefactor is approximately right**. But it uses **Boltzmann mode-counting which is the framework AVE rejects**.

## §6 — The four entropies summarized

| Entropy | Magnitude (at $M = M_\odot$) | Physical meaning | AVE-native? |
|---|---|---|---|
| $\hat S_{\text{geo}}$ | $\sim 10^{36} k_B$ ($A \log 2 / \ell_{\text{node}}^2$ at solar mass) | Op14 scattering irreversibility at A-B horizon cells | **YES** — Vol 3 Ch 11 + A-B interface |
| $S_{BH}$ | $\sim 10^{77} k_B$ | First-law-integrated mass-absorption thermodynamic entropy | Imported from GR via first law |
| $S_\mu$ (microstate count) | $2^{10^{77}}$ states | Binary A-B choice per horizon cell | Doc 61 §3.2 informal microstate framing |
| $S_v$ (volume thermalization) | $\sim 4 \cdot S_{BH}$ | Interior thermalization of ruptured-plasma dissipative sink | Uses Boltzmann counting AVE rejects |

**Ratios:** $\hat S_{\text{geo}} : S_{BH} = 1 : 10^{44}$. The thermodynamic entropy is $10^{44} \times$ larger than the geometric entropy under AVE's framework.

## §7 — First-law $T \cdot dS = dE$ fails axiom-first

Per [AVE BH Horizon Area Theorem](../../cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md), the area theorem ($\delta A \geq 0$) and mass-energy ($dE = dM \cdot c^2$) are axiom-derived. But the first-law relation $T \cdot dS = dE$ requires:

$$dS = dE / T_H \quad \Rightarrow \quad S = 4 \pi G M^2 k_B / (\hbar c) = A k_B / (4 \ell_P^2)$$

— exactly the standard Bekenstein-Hawking entropy. **Works numerically but it's NOT AVE-derived** — it's the answer you get from STANDARD equipartition assumption, which Vol 3 Ch 11:15 explicitly rejects.

Working through the first law with AVE's native $\hat S_{\text{geo}}$ and AVE's reinterpreted $T_H = \hbar c^3 / (8 \pi G M k_B)$:

$$T_H \cdot d\hat S_{\text{geo}} / dE = 7 \log 2 / \xi \approx 3.2 \times 10^{-44}$$

**The first law is violated by a factor of $\sim 10^{-44}$.** AVE's native $\hat S_{\text{geo}}$ is WAY too small to satisfy $T \cdot dS = dE$ with AVE's $T_H$.

## §8 — Observational discriminator

These measure DIFFERENT physics. Neither is "wrong" — but they aren't the same quantity:

- **$\hat S_{\text{geo}}$** measures local wave-scattering irreversibility at boundaries. Finite and small.
- **$S_{BH}$** measures the thermodynamic entropy a BH accumulates by absorbing mass-energy. Imported from standard GR thermodynamics.
- **Ratio $10^{-44}$** is the Machian dilution factor.

**Any observational test sensitive to the AVE-native geometric entropy** (as opposed to thermodynamic $S_{BH}$) would distinguish. Specifically: **Hawking radiation modes that depend on the interface structure**. If A-B interface picture is right, there's a finite signal $\sim A \log 2 / \ell_{\text{node}}^2$ units of entropy accessible to observation. If corpus ruptured-plasma picture is right, that signal is zero and only the thermodynamic $S_{BH}$ is observable.

## Cross-references

- **Canonical manuscript:**
  - Vol 3 Ch 11:14-68 — geometric-entropy framework + $\hat S$ operator
  - Vol 3 Ch 15:19-29 — symmetric-saturation gravity ($Z(r) = Z_0$)
  - Vol 3 Ch 21:114 — ruptured-plasma BH interior
  - Vol 3 Ch 11:15 — explicit rejection of standard equipartition assumption
- **KB cross-cutting:**
  - [AVE BH Horizon Area Theorem](../../cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md) — axiom-derived pillars (area + mass-energy)
  - [Discrete-Lattice $\hat S$ at BH Horizon](discrete-lattice-entropy-constant.md) — Flag 62-G closure: ~8.7 $k_B$ per cell under symmetric saturation (lattice-discretization correction to Γ = 0)
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — BH horizon as canonical kernel instance
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — substrate-observability rule at BH horizon
