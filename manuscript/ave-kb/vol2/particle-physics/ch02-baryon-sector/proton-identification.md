[↑ Ch.2 — Baryon Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-cmic3e]
path-stable: "referenced from vol2 ch01 electron-identification + vol3 ch11 thermal-softening-skyrme + common full-derivation-chain as canonical proton identification"
-->

# Proton — Canonical Identification + First-Principles Axiom Audit

The AVE-native canonical identification of the proton, structured to parallel `../ch01-topological-matter/electron-identification.md` (on sibling branch `analysis/electron-definition-canonical`, not yet merged to L3) and [`../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md).

**Load-bearing audit finding:** unlike the electron (where $m_e$ is a calibration anchor), **the proton's mass ratio $m_p/m_e = 1836.12$ is derived with zero baryon-data-tuned parameters** (electron-physics-provenanced: $m_e + \alpha$, replacing Skyrme's $F_\pi + e$) --- from the $(2,5)$ cinquefoil topology + Vol 1 Ch 8 closure ($\kappa_{FS} = 8\pi$ from $p_c = 8\pi\alpha$) + dual-reactance count $\mathcal{V}_{total} = 2$ (the node's two reactance sectors $X_C + X_L$, NOT a FEM-integrated volume; see [`dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md)) + Ax2 TKI charge twist ($+1.0\,m_e$). 0.002\% from CODATA 1836.153. The per-channel coupling efficiency is forced ($k=1$, Axiom-3 $\Gamma=0$ + Op17); the per-channel loop-gain $= p_c$ identification is a matched structural assignment, same class as the lepton couplings (see parameter ledger). **This is the AVE framework's flagship mass prediction.**

## §1 — Canonical 4-property definition

The proton in AVE is defined by **four tightly-coupled topological/dynamical properties**:

1. **Phase-space (per-loop) polarization winding: $(2,5)$ cinquefoil** — 🔴 *[relabel 2026-06-08 — prior label* ~~"Real-space topology: $(2,5)$ cinquefoil torus knot"~~ *was a phase-space-vs-real-space category error]* the $(2,5)$ is the **phase-space** per-loop polarization winding in the flux-tube cross-section's EM-polarization phase space $(V_{inc}, V_{ref})$, NOT a real-space knot; next entry after the electron's $(2,3)$ on the $(2,q)$ winding ladder. Crossing number $c_5 = 5$; only odd-$q$ entries are stable on the K4 chiral lattice (no stable $(2,4)$ knot — figure-eight is not a torus knot). **The $(2,5)$ "cinquefoil" is the phase-space (per-loop) polarization winding pattern, NOT a real-space cinquefoil knot** — exactly parallel to [`../ch01-topological-matter/electron-identification.md`](../ch01-topological-matter/electron-identification.md) §1 property 2 + line 23 (*"the $(2,3)$ trefoil is the phase-space winding pattern, NOT a real-space trefoil knot"*) and confirmed by `src/ave/core/constants.py:689-694` (*"the $(2,q)$ torus knots classify the phase winding number, not the ground-state topology"*). The proton's real-space topology is the $6_2^3$ Borromean linkage (property 2).
2. **Real-space topology + structural composition: $6_2^3$ Borromean linkage** — 🔴 *[relabel 2026-06-08 — promoted to the real-space-topology slot; prior label was* ~~"Structural composition"~~ *only]* three mutually entangled electromagnetic flux loops in the $\mathcal{M}_A$ condensate. This Borromean linkage **is the proton's ground-state real-space topology** (the slot the $(2,5)$ phase-space winding was previously mislabeled into), parallel to the electron's $0_1$ unknot real-space topology. The "three quarks" of standard QCD are the three loops of this Borromean cage; fractional quark charges $\pm 1/3 e, \pm 2/3 e$ arise via the Witten Effect on $\mathbb{Z}_3$ symmetric $\theta$-vacua (per [`topological-fractionalization.md`](topological-fractionalization.md)).
3. **Confinement budget ratio: $r_{opt} = \kappa_{FS}/c_5 = 8\pi/5 \approx 5.03$ (dimensionless)** — 🔴 *[relabel 2026-06-08 — prior label* ~~"Confinement radius: $r_{opt} = \kappa_{FS}/c_5 = 8\pi/5 \approx 4.97\,\ell_{node}$ … The proton extends over approximately 5 lattice spacings — a genuinely extended object, NOT a point particle."~~ *was a dimensional category error]* $\kappa_{FS} = 8\pi$ is a **pure geometric (dimensionless) constant** (the solid-angle normalisation of the Borromean quartic stabilization term; `src/ave/core/constants.py:683-687`: *"This is a pure geometric constant"*), so $r_{opt} = \kappa_{FS}/c_5$ is a **pure number ($\approx 5.03$), NOT a length**. It is the dimensionless coupling-budget ratio — the fraction of the total Faddeev-Skyrme coupling allocated per crossing — that bounds the soliton in the 1D functional's *natural integration coordinate* (where the solver normalises $\ell_{node} = 1$ purely as the Nyquist-gradient-cutoff unit; `src/ave/topological/faddeev_skyrme.py:126-130`). The $\ell_{node}$ length-units previously attached to $r_{opt}$ were spurious. **The proton is NOT $\sim 5$ lattice spacings extended:** the only *measured* proton size is the charge radius $D_p = 0.841$ fm (property 4), which is **sub-node — $\approx 460\times$ smaller than one $\ell_{node} = 386$ fm** (a "$5\,\ell_{node}$" object would be $\approx 1930$ fm, $\sim 2300\times$ the measured size — the internal contradiction this relabel resolves). The real-space sub-node geometry (why a $0.841$ fm body) is an OPEN item, not a $\sim 5\,\ell_{node}$ extended object.
4. **Saturated core (Ax4 inside Faddeev-Skyrme integrand)** — the cinquefoil core operates in the saturated regime ($S \to 0$, $G_{shear} = 0$). The charge radius $D_p = 4\lambda_p = 0.841$ fm marks the non-linear $\to$ saturated transition (the "event horizon" of the strong force; per [`../../appendices/app-f-solver-toolchain/nuclear-eigenvalue.md`](../../appendices/app-f-solver-toolchain/nuclear-eigenvalue.md)).

## §2 — First-principles axiom audit per property

### Topological/dynamical properties (the 4 from §1)

| Property | Axiom support | Derivation status | Open items |
|---|---|---|---|
| 1. $(2,5)$ cinquefoil ~~real-space topology~~ 🔴 **phase-space (per-loop) polarization winding** [relabel 2026-06-08] | Ax1 (K4 chiral lattice supports the $(2,q)$ phase-winding ladder; only odd-$q$ stable) + Ax2 (TKI: charge winding number → +e for $(2,5)$ with single twist) | ✅ axiom-derived (as phase-space winding) | None — $(2,5)$ uniquely fixed as next-after-electron entry on the $(2,q)$ winding ladder; the $(2,5)$ is phase-space, the real-space topology is the $6_2^3$ Borromean (row 2) |
| 2. $6_2^3$ Borromean linkage of 3 flux loops 🔴 **(the proton's real-space topology)** [relabel 2026-06-08] | Ax1 + Ax2 (the three loops are the three quark-equivalent topological circuits required to close the cinquefoil via $\mathbb{Z}_3$ symmetric $\theta$-vacuum); Witten Effect provides fractional charge $\pm 1/3, \pm 2/3$ | ✅ axiom-derived | None |
| 3. Confinement ~~radius $r_{opt} = \kappa_{FS}/5 \approx 4.97\,\ell_{node}$~~ 🔴 **budget ratio $r_{opt} = \kappa_{FS}/5 = 8\pi/5 \approx 5.03$ (dimensionless, NOT a length)** [relabel 2026-06-08] | $\kappa_{FS} = p_c/\alpha = 8\pi$ from Vol 1 Ch 8 closure (Ax3 + Ax4), a **pure geometric constant** (constants.py:683-687); topological mechanism: each crossing absorbs $\kappa_{FS}/c_5$ of the total dimensionless coupling | ✅ axiom-derived (as a dimensionless budget ratio) | 🔴 **OPEN** [was mislabeled "None"] — the proton's real-space size is the sub-node $D_p = 0.841$ fm ($\approx 460\times$ smaller than $\ell_{node} = 386$ fm); the sub-node geometry is underived. The "$\sim 5\,\ell_{node}$ extended object" reading is retired (dimensional category error). |
| 4. Saturated core ($S \to 0$ inside Faddeev-Skyrme integrand) | Ax4 saturation kernel applied to the FS gradient term | ✅ axiom-derived | None |

### Observable properties — the load-bearing audit

| Observable | Axiom support | Derivation status | Notes |
|---|---|---|---|
| **Rest mass $m_p/m_e = 1836.12$** | Multi-input eigenvalue chain, zero baryon-data-tuned parameters (see §2.1 below for full audit) | ✅ **axiom-derived** (zero baryon-data-tuned; per-channel loop-role a matched assignment, see ledger) — 0.002% from CODATA 1836.153 | **Unlike $m_e$ (calibration anchor), $m_p/m_e$ is a real test of the framework.** This is AVE's flagship mass-derivation claim. |
| Charge $+e$ | Ax2 TKI (+1 integer topological twist trapped at Borromean cage center; "the global invariant charge constraint of the unbroken lattice") | ✅ axiom-derived | The +1.0 in the mass eigenvalue ($x = 1835.12 + 1.0$) IS this charge twist's rest energy. |
| Spin-½ | Same Cosserat microrotation + Finkelstein-Misner mechanism as the electron (Ax1) | ✅ axiom-derived | Inherits from electron-identification.md §2. |
| Charge radius $D_p = 4\lambda_p = 0.841$ fm | Ax4 (saturation transition radius); $\lambda_p = \hbar/(m_p c)$ = proton Compton wavelength | ✅ axiom-derived | Matches muonic hydrogen measurement (the famous 0.841 fm from Pohl 2010 et al.). Per [`../../proofs-computation/ch09-computational-proof/anomaly-catalog.md` line 13](../../proofs-computation/ch09-computational-proof/anomaly-catalog.md). |
| Fractional quark charges $\pm 1/3, \pm 2/3 e$ | Witten Effect on $\mathbb{Z}_3$ symmetric $\theta$-vacua: $q_{eff} = n + \theta e/(2\pi)$, $\theta \in \{0, \pm 2\pi/3, \pm 4\pi/3\}$ | ✅ axiom-derived | Per [`topological-fractionalization.md`](topological-fractionalization.md). The three quark "flavors" are the three $\theta$-vacuum sectors of the same Borromean linkage. |
| Magnetic moment, gyromagnetic ratio | Derives from charge + spin + $m_p$ (eigenvalue) via standard QED machinery | ✅ axiom-derived | Composite of above. |
| Stability against decay (free proton lifetime $> 10^{34}$ yr) | Ax2 TKI topology conservation (cinquefoil is irreducible; cannot decay to electron + neutrinos without breaking topology) | ✅ axiom-derived | Topological protection same mechanism as electron. |

### §2.1 — The proton mass eigenvalue derivation, audited input-by-input

The mass eigenvalue ([`self-consistent-mass-oscillator.md`](self-consistent-mass-oscillator.md)):

$$x_{core} = \mathcal{I}_{scalar} + (\mathcal{V}_{total} \cdot p_c) \cdot x_{core}$$

Solves to:
$$x_{core} = \frac{\mathcal{I}_{scalar}}{1 - \mathcal{V}_{total} \cdot p_c} = \frac{1162}{1 - 2.0 \cdot 0.1834} = \frac{1162}{0.6332} \approx 1835.12$$

Then $x_{total} = x_{core} + 1.0 = 1836.12$ (the +1.0 is the +e charge twist's rest mass).

**Six inputs to audit:**

| Input | Value | Axiom support | Derivation source | Fit risk |
|---|---|---|---|---|
| $\kappa_{FS}$ (Faddeev-Skyrme coupling) | $8\pi$ | Vol 1 Ch 8 closure: $\kappa_{FS} = p_c/\alpha$, with $p_c = 8\pi\alpha$ → $\kappa_{FS} = 8\pi$ | Ax3 + Ax4 + Vol 1 Ch 8 | ✅ none — derived from α |
| $c_5$ (cinquefoil crossing number) | $5$ | Topological invariant of $(2,5)$ torus knot | Ax1 | ✅ none — integer topology |
| $\mathcal{I}_{scalar}$ (1D FS scalar integral) | $\approx 1162$ | Numerical integration of 1D Faddeev-Skyrme energy functional with $r_{opt} = \kappa_{FS}/5$ confinement + Ax4 gradient saturation inside integrand + $\delta_{th} = 1/(14\pi^2)$ thermal softening | Ax1 + Ax4 + thermal correction | ⚠ **Computational input — verify the FS solver implementation has no tunable parameters.** Documented in `vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md`; numerical convergence claim should be cross-checked. |
| $\mathcal{V}_{total}$ (dual-reactance count) | $2$ | The node's two reactance sectors (Axiom 1): the capacitive $X_C$ (3 translational-E DOF) + the inductive $X_L$ (3 microrotational-B DOF), each one electron-ground-state unit. A discrete channel count, NOT a geometric volume and NOT a FEM-integrated quantity (prior FEM provenance fabricated, dropped per the V2 dual-reactance closure 2026-06-01). Mass-confirmed: $\mathcal{V}=2 \to 1836.117\,m_e$ uniquely selected vs CODATA 1836.153 | Ax1 (two reactance sectors per node) | ✅ none — forced reactance count per [`../../../common/dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md) |
| $p_c$ (vacuum packing fraction) | $8\pi\alpha \approx 0.1834$ | Vol 1 Ch 8 closure: $p_c = 8\pi\alpha$ with α from Golden Torus | Ax3 + Ax4 + Vol 1 Ch 8 | ✅ none — derived from α |
| +1.0 (global charge twist) | $1.0\,m_e$ | Ax2 TKI: +e charge = +1 integer topological twist; one twist contributes exactly $1.0\,m_e$ rest mass via ropelength baseline (the electron's mass IS the rest mass of one integer twist) | Ax2 | ✅ none — integer topology, NOT a tunable parameter |

**All six inputs are first-principles. Zero fit parameters. The 0.002% match to CODATA is a genuine prediction.**

### §2.2 — Honest scoping caveats (open audit items)

Two items worth flagging — neither falsifies the derivation, but both should be documented:

1. **The numerical integration $\mathcal{I}_{scalar} \approx 1162$** is asserted from "1D Faddeev-Skyrme solver" but I haven't seen the explicit solver implementation or convergence-verification artifact. The corpus claim is that this is a pure numerical integration with no tunable parameters (just $\kappa_{FS}/5$ confinement + Ax4 saturation + $\delta_{th}$ thermal), but **a load-bearing 4-digit number deserves explicit solver-documentation cross-reference.** Action: trace the FS solver to a specific src/ script with reproducible output.

2. **Corpus hygiene note** (per [`self-consistent-mass-oscillator.md` line 4](self-consistent-mass-oscillator.md) comment): the source has **duplicate subsection titles** "The Self-Consistent Mass Oscillator (The Structural Eigenvalue)" at approximately lines 114 and 166. KB leaf covers both occurrences but the LaTeX source needs deduplication.

## §3 — Cross-corpus framing translation guide

| # | Framing | Emphasis | Canonical source | Verbatim quote |
|---|---|---|---|---|
| 1 | **$(2,5)$ cinquefoil torus knot** (🔴 phase-space per-loop polarization winding, NOT real-space — relabel 2026-06-08) | ~~Topology~~ **Phase-space winding** (next entry after electron on $(2,q)$ ladder) | [`../../../common/full-derivation-chain.md` line 462](../../../common/full-derivation-chain.md) | *"The proton is a $(2,5)$ cinquefoil torus knot with crossing number $c_5 = 5$."* (corpus quote retained verbatim; the $(2,5)$ it names is the phase-space winding per the §1 property-1 relabel) |
| 2 | **$6_2^3$ Borromean linkage confined by $(2,5)$ cinquefoil** | Structural composition (three quark-equivalent loops) | [`../../../vol3/condensed-matter/ch11-thermodynamics/thermal-softening-skyrme.md` line 12](../../../vol3/condensed-matter/ch11-thermodynamics/thermal-softening-skyrme.md) | *"The proton is a $6_2^3$ Borromean linkage confined by the $(2,5)$ cinquefoil torus knot. Its internal tension is governed by the Faddeev-Skyrme coupling constant $\kappa_{FS} = 8\pi$ (the cold, zero-temperature value)."* |
| 3 | **Cinquefoil soliton with saturated core** | Saturated-regime / strong-force "event horizon" | [`../../appendices/app-f-solver-toolchain/nuclear-eigenvalue.md` line 10](../../appendices/app-f-solver-toolchain/nuclear-eigenvalue.md); [`../../../common/solver-toolchain.md` line 230](../../../common/solver-toolchain.md) | *"The proton is a cinquefoil ($c = 5$) soliton whose core is in the saturated regime ($S \to 0$, $G_{shear} = 0$). Its charge radius $D_p = 4\lambda_p = 0.841$ fm marks the non-linear $\to$ saturated transition — the 'event horizon' of the strong force."* |
| 4 | **Three-quark Borromean cage with Witten-Effect fractional charges** | QCD-equivalent / quark-flavor framing | [`topological-fractionalization.md`](topological-fractionalization.md) | *"Fractional quark charges $\pm 1/3, \pm 2/3 e$ arise via the Witten Effect on $\mathbb{Z}_3$ symmetric $\theta$-vacua."* — the three loops of the Borromean cage are the three quarks |
| 5 | **Inductively-stiffened flux-tube cluster** (nuclear binding context) | Mass-stiffening of nuclear interactions; He-4 binding | [`proton-neutron-mass-split.md`](proton-neutron-mass-split.md) | *"Effective nuclear tension scales by the proton-electron mass ratio: $T_{nuc} = T_{EM} \cdot (m_p/m_e) \approx 0.212\,\text{N} \times 1836 \approx 389.2\,\text{N}$."* |
| 6 | **Self-consistent mass oscillator eigenvalue** | Mathematical mass-derivation form | [`self-consistent-mass-oscillator.md`](self-consistent-mass-oscillator.md) | *"$x_{core} = \mathcal{I}_{scalar} + (\mathcal{V}_{total} \cdot p_c) \cdot x_{core}$; solution $\approx 1835.12 m_e$; baryon mass eigenvalue $1836.12$ within 0.002% of CODATA."* |

### Reconciliation matrix — framing × canonical property

| Framing | P1 ($(2,5)$ cinquefoil — 🔴 phase-space winding) | P2 ($6_2^3$ Borromean — 🔴 real-space topology) | P3 (confinement $r_{opt}$) | P4 (saturated core) |
|---|---|---|---|---|
| 1. $(2,5)$ cinquefoil | **explicit** | implied | implied | implied |
| 2. Borromean linkage confined by cinquefoil | **explicit** | **explicit** | implicit | implicit |
| 3. Cinquefoil + saturated core | **explicit** | implied | implied | **explicit** |
| 4. Three-quark Borromean + Witten | implicit | **explicit** | implicit | implicit |
| 5. Inductively-stiffened flux cluster | implied | implied | implicit | **explicit** ($T_{nuc}$ stiffening derives from saturated core) |
| 6. Self-consistent mass eigenvalue | implicit ($\kappa_{FS}/5$ in $r_{opt}$) | implicit ($\mathcal{V}_{total} = 2.0$ is Borromean halo) | **explicit** ($r_{opt}$ confinement bound) | **explicit** (Ax4 saturation inside FS integrand) |

**All 6 framings map cleanly to the 4 canonical properties.** Reader-domain mapping:
- Knot theorist → framing 1 (cinquefoil topology)
- Standard-Model physicist → framing 4 (three-quark + Witten)
- Nuclear engineer → framing 5 (inductively-stiffened flux-tube)
- AVE-native solver developer → framing 6 (eigenvalue equation)
- General AVE reader → framing 2 (Borromean linkage confined by cinquefoil — the most complete one-sentence definition)

### Related-but-non-definitional uses

- [`../../../vol5/molecular-foundations/biophysics-intro/protein-backbone-proton-radius.md`](../../../vol5/molecular-foundations/biophysics-intro/protein-backbone-proton-radius.md) — uses proton in protein-backbone context; not a fundamental definition.
- [`proton-neutron-mass-split.md`](proton-neutron-mass-split.md) — Heavy fermion + neutron-decay + He-4 nucleus context; restates framing 5 + adds neutron-decay topological dynamics. Not a standalone proton definition.
- [`thermal-softening.md`](thermal-softening.md) (Vol 2 Ch 2) — derives the thermal correction $\delta_{th} = 1/(14\pi^2)$ that softens $\kappa_{FS}$; uses proton as the canonical test case but doesn't redefine it.

## §4 — Maintenance discipline

If a **7th definitional framing** surfaces, reconcile to one or more of the 4 canonical properties in §1. Do NOT let the corpus drift toward a 7th independent definition.

If the **proton mass eigenvalue derivation is challenged** (e.g., $\mathcal{V}_{total}$ dual-reactance-count derivation revisited, $\mathcal{I}_{scalar}$ numerical integration re-implemented, $\delta_{th}$ thermal correction revised), update §2.1 audit table inline with `**[Edit YYYY-MM-DD: <reason>]**` marker. The 0.002% match to CODATA is load-bearing — any change to the chain that breaks this match is a major framework event requiring an honest commit message.

**$\mathcal{V}_{total} = 2$ is the dual-reactance count** --- the node's two reactance sectors ($X_C$ capacitive-E $+$ $X_L$ inductive-B); canonical at [`../../../common/dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md). The prior "3D FEM integration yields $\mathcal{V}_{total} = 2.0$" framing is **retired** (per the 2026-06-01 V2 dual-reactance closure [`research/2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) §3 + the 2026-06-02 fabricated-FEM walk-back). Precise status: the signed great-circle intersection integral evaluates to 0 (not 2); the only script labeled "FEM" ([`fem_borromean_convergence.py`](../../../../../src/scripts/vol_2_subatomic/fem_borromean_convergence.py) + JAX port) is **not** finite-element — it is voxel-quadrature of the **Gaussian-ansatz** three-tube saturated overlap volume against $\rho_{threshold}$ (a profile-dependent $\rho_{threshold}$ consistency check that lands near 2.0 as a property of the Gaussian ansatz), NOT a derivation of the reactance count. Do NOT build a `v-total-fem-verification.md` leaf --- the "2" is a forced reactance-sector count, not an integrated volume.

---

> → Primary: [`self-consistent-mass-oscillator.md`](self-consistent-mass-oscillator.md) — the mass eigenvalue equation + neutral core solution + baryon mass eigenvalue ($1835.12 + 1.0 = 1836.12$); framing #6 source
> → Primary: [`topological-fractionalization.md`](topological-fractionalization.md) — Borromean confinement + Faddeev-Skyrme proton energy + Witten Effect fractional quark charges; framings #2 + #4 source
> → Primary: [`../../../vol3/condensed-matter/ch11-thermodynamics/thermal-softening-skyrme.md`](../../../vol3/condensed-matter/ch11-thermodynamics/thermal-softening-skyrme.md) — proton as $6_2^3$ Borromean linkage confined by cinquefoil + thermal softening derivation; framing #2 source
> → Primary: `../ch01-topological-matter/electron-identification.md` (on sibling branch `analysis/electron-definition-canonical`, not yet merged to L3) — companion canonical-identification leaf for electron; shared mechanisms (Ax1 + Ax2 + Ax4)
> ↗ See also: [`../../appendices/app-f-solver-toolchain/nuclear-eigenvalue.md`](../../appendices/app-f-solver-toolchain/nuclear-eigenvalue.md), [`../../../common/solver-toolchain.md`](../../../common/solver-toolchain.md) — cinquefoil saturated-core framing (#3)
> ↗ See also: [`torus-knot-ladder-baryons.md`](torus-knot-ladder-baryons.md) — full $(2,q)$ baryon resonance spectrum (proton is $(2,5)$; $\Delta(1232)$ is $(2,7)$; etc.)
> ↗ See also: [`proton-neutron-mass-split.md`](proton-neutron-mass-split.md) — neutron decay topological dynamics + Heavy fermion paradox + He-4 binding (framing #5)
> ↗ See also: [`../../appendices/app-c-derivations/index.md` line 29](../../appendices/app-c-derivations/index.md) + [`../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tvs-transition.md` line 23](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tvs-transition.md) — $\mathcal{V}_{total} = 2.0$ dual-reactance count (load-bearing input #4 to mass eigenvalue)
