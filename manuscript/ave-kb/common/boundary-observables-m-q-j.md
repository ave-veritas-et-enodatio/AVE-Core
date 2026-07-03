[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-ze4clw, clm-ofys5v, clm-vnp57s, clm-sjjvhf, clm-3bwhad]
path-stable: "referenced from vol1, vol2, vol3, vol4, vol5, vol6 as canonical M, Q, J boundary-observables reference"
-->

# The Three Canonical Boundary Observables: $\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$

At every $\Gamma = -1$ saturation surface $\partial\Omega$ in the substrate — the boundary where Axiom 4's kernel (the Universal Saturation Kernel) reaches $S(A) \to 0$ locally — exactly **three integrated quantities are externally observable**. This leaf is the canonical AVE-Core reference; manuscript canonicalization lives at Common Foreword §"Three Boundary Observables and the Substrate-Observability Rule" + Vol 1 Ch 1 §sec:substrate_vocab_box_ch1. The substrate noun is the Chiral LC Network, corresponding to a chiral Laves K4 Cosserat crystal at the substrate level.

## The three invariants

<!-- claim-quality: clm-ze4clw -->

| Symbol | Canonical name | Operational definition | Dimensionality | EE projection | ME projection | QFT projection |
|---|---|---|---|---|---|---|
| $\mathcal{M}$ | Integrated strain integral | $\displaystyle\int_\Omega (n(\mathbf{r}) - 1)\, dV$ | **3D volume** | inductance $L$ | inertia (kg) | rest energy $m c^2$ |
| $\mathcal{Q}$ | Boundary linking number | $\mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ | **1D line/loop** | charge $Q$ | (no clean analog) | electromagnetic charge |
| $\mathcal{J}$ | Boundary winding number | $\mathrm{Wind}(\partial\Omega)$, half-integer per $SU(2)$ double-cover | **2D surface** | magnetic moment | rotation | spin $J$ |

**Stokes-theorem dimensional structure.** Each invariant uses one fewer integration dimension than the substrate's 3D bulk — $\mathcal{M}$ counts a volume, $\mathcal{J}$ counts a surface winding, $\mathcal{Q}$ counts a line/loop linking. The three dimensions are exhaustive: there is no fourth integrated boundary observable at this scale-invariant structure.

> **Pair physics on $\mathcal{Q}$ (2026-07-03).** Two $\mathcal{Q}$ (winding) objects now have an engine-derived *interaction* — like windings repel / unlike attract with Coulomb sign structure (`clm-wcoul2`, consistency-class; `vol4/claim-quality.md`) — the Axiom-2 interaction leg, complementing the single-object $\mathcal{Q}=\mathrm{Link}(\partial\Omega,\mathbf{F})$ dictionary above.

## The substrate-observability rule

<!-- claim-quality: clm-ofys5v -->

For any localized region $\Omega$ in the substrate enclosed by a $\Gamma = -1$ saturation surface:

1. The boundary totally reflects substrate waves outside and totally traps them inside.
2. The interior is causally and impedance-disconnected from external observers.
3. **Only $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ are externally measurable.** Interior eigenmode wavelengths, microrotation profiles, soliton topology, and bond-stress distributions are invisible to the substrate.

This is the **no-hair theorem applied universally** — not as a black-hole-specific theorem but as the substrate's fundamental observability constraint at every scale.

## Same mechanism at all scales

The same three observables appear at every $\Gamma = -1$ saturation surface in the substrate hierarchy:

| Scale | Boundary | Internal solitons | Observables |
|---|---|---|---|
| Electron ($\ell \sim 10^{-13}$ m) | Horn-torus tube wall (TIR at saturation) | $0_1$ unknot single soliton | $m_e c^2$, $e$, $\hbar/2$ |
| Nucleus ($\ell \sim 10^{-15}$ m) | Borromean confinement on $(2,5)$ cinquefoil | 3-strand $SU(3)$ Borromean linkage | nucleon mass, electric charge, nuclear spin |
| Atom ($\ell \sim 10^{-10}$ m) | Outer shell saturation | Nucleus + $Z$ electrons | atomic mass, ionization, total angular momentum |
| Planetary magnetopause | Magnetosphere boundary | Planet + field-aligned solitons | planet mass, dipole moment, rotation |
| Black-hole event horizon ($r = 2GM/c^2$) | Schwarzschild horizon | All matter → pre-geodesic plasma | $M$ (ADM mass), $Q$, $J$ (Kerr-Newman) |
| Cosmic horizon ($R_H \sim 10^{26}$ m) | Parent-BH Schwarzschild radius | All observable matter + dark sector | $\mathcal{M}_{\text{cosmic}}$, $\mathcal{Q}_{\text{cosmic}}$, $\mathcal{J}_{\text{cosmic}}$ (CMB anomalies, LSS rotation, Hubble flow anisotropy) |

**The substrate observes integer/half-integer counts of relational observables; everything else is interior plumbing.** The electron's real-space body listed here is the $0_1$ unknot soliton; its $(2,3)$/trefoil structure is the phase-space (Clifford-torus) winding label, not the real-space body.

## The fine-structure constant as electron-scale $\mathcal{M} + \mathcal{J} + \mathcal{Q}$

<!-- claim-quality: clm-vnp57s -->

The Vol 1 Ch 8 canonical $\alpha^{-1}$ derivation decomposes into exactly three contributions corresponding to the three boundary-integral dimensionalities:

$$
\alpha^{-1} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.036
$$

| Term | Value | Dimensionality | Maps to |
|---|---|---|---|
| $\Lambda_{\text{vol}} = 4\pi^3$ | volume integral | 3D | $\mathcal{M}$ (mass) |
| $\Lambda_{\text{surf}} = \pi^2$ | surface integral | 2D | $\mathcal{J}$ (spin) |
| $\Lambda_{\text{line}} = \pi$ | line integral | 1D | $\mathcal{Q}$ (charge) |

Each power of $\pi$ counts one dimension of boundary integration, as in Stokes-theorem dimensional reduction. The load-bearing $R \cdot r = 1/4$ normalization that makes $\Lambda_{\text{vol}} = 16\pi^3 \cdot R \cdot r$ evaluate to exactly $4\pi^3$ is derived via the Q-EMBED-SEL-1 Phase 1 substrate-mechanism (canonical at [`research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md`](../../../research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md) §2.3): Axiom 4 self-saturation at the bond LC tank + Op14 Meissner-asymmetric coupling at the $(2,3)$ chirality + the named substrate-mechanism identification that the time-averaged phasor enclosed area at Axiom-4 self-saturation onset equals the Nyquist cell cross-section area, giving $\pi R r = \pi(d/2)^2 \Rightarrow R \cdot r = 1/4$ at $d = 1\,\ell_\text{node}$. The prior derivation chain via the spin-$\tfrac{1}{2}$ half-cover of the standard Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (substrate-native via the $K_4 \to A_4 \to 2T \subset SU(2)$ chain + Finkelstein–Misner mechanism) is preserved as historical context for the spin-½ structure of the electron — that chain remains canonical for spin-½ — but is **retired as load-bearing per Q-EMBED-SEL-1 2026-05-31** for the $R \cdot r = 1/4$ normalization; the substrate-mechanism path is now via the Q-EMBED-SEL-1 phasor-area-equals-Nyquist-cell-area identification, not via half-cover area-halving. **The decomposition is not coincidental** — it is the substrate's natural three-integral boundary-observability structure expressed at the electron-scale Q-factor.

> → Primary: [Vol 1 Ch 8 — Alpha Golden Torus](../vol1/ch8-alpha-golden-torus.md) — the geometric three-regime closure derivation of $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$. The present leaf supplies the distinct boundary-integral *dimensional reading* (3D→$\mathcal{M}$, 2D→$\mathcal{J}$, 1D→$\mathcal{Q}$) of that same formula.

## Operational analysis recipe

For any localized region $\Omega$ in the substrate:

1. **Identify the saturation surface** $\partial\Omega$ — the boundary where $S(A) \to 0$ locally.
2. **Compute $\mathcal{M}, \mathcal{Q}, \mathcal{J}$** as the three integrated invariants over the substrate fields ($\mathcal{M}$ from a 3D volume integral; $\mathcal{J}$ from a 2D surface integral; $\mathcal{Q}$ from a 1D line/loop integral).
3. **Compare against measured observables** (mass, charge, spin or angular momentum in the appropriate projection).
4. **The interior topology is invisible from outside** — only the boundary integrals matter.

## Implications: interior eigenmodes and "substrate compression"

<!-- claim-quality: clm-sjjvhf -->

The substrate-observability rule has two non-obvious consequences that supersede prior framings (Grant 2026-05-14 evening):

**Interior eigenmodes are not lattice-Nyquist-constrained.** Any interior Beltrami / phase-space eigenmode of a bounded soliton (e.g., the electron's horn-torus interior at $k \approx 6.36 / \ell_{\text{node}}$) lives entirely inside the $\Gamma = -1$ wall and is causally disconnected from the exterior substrate. The K4 propagating-mode Nyquist wavevector edge $k_{\max} \sim \pi / \ell_{\text{node}}$ (measured $\sqrt2\,\pi \approx 4.44/\ell_{\text{node}}$ along the chiral srs axis — the $\sqrt n$ is the crystallographic plane-spacing projection of the 1-bond $\pi/\ell_{\text{node}}$ edge) does NOT apply to interior structure because the substrate never propagates that wave through the lattice — it lives only in the bounded interior cell. Forcing a multi-cell propagating-eigenmode test on a bounded interior is a category error; the substrate-correct test measures integrated boundary observables ($\mathcal{M}, \mathcal{Q}, \mathcal{J}$).

> **🟢 ADDITIVE CORROBORATION (2026-06-24; STRENGTHENS — no retraction).** The Stage-2 native-cage make-or-break ([`research/2026-06-24_engine-stage2-native-cage_result.md`](../../../research/2026-06-24_engine-stage2-native-cage_result.md), branch `analysis/engine-stage2-native-cage-imex` @ `edb19872`) returned 🔴 **MODE-III DISPERSE** (energy-conservation-certified): a seeded interior SECH precursor on the native K4 stencil WITH c_eff(V) does **not** form a persistent propagating interior mode — it disperses. This **empirically confirms the bulk interior hosts no propagating self-trapped mode**, which is exactly what this claim's observability exemption predicts (the interior is not a propagating-lattice carrier). It therefore **partially discharges** the register caveat that the exemption "is taken from the boundary-observability rule rather than **shown for the specific** interior mode" (`claim-quality.md` clm-sjjvhf rationale): the bulk-interior-mode route is now shown empty, so the localization is boundary/topological (the surviving route), consistent with this leaf. **Scope:** this rules out the BULK self-trap mechanism; **boundary/topological localization STANDS; mass = A1 (#260) UNTOUCHED.**

> 🟡 **EXPOSURE POINTER (2026-07-03, verdict-exposure sweep — status-demotion, NOT retraction).** The Stage-2 DISPERSE evidence the corroboration banner above leans on is now **HIGH-exposed**: its operator (the diamond `TETRA_OFFSETS` `L_D`) is nullspace-heavy / sublattice-decoupled, and the "instrument-can-SEE-a-trap" positive control ran on the *Cartesian* `MasterEquationFDTD` engine, not the native pipeline that rendered DISPERSE. So the "partial discharge" above is **itself under re-adjudication**, and clm-sjjvhf's authored confidence is demoted accordingly (0.65 → 0.60). The claim's **core exemption STANDS** (interior-mode Nyquist exemption via the observability rule); only the empirical strengthening demotes. **mass = A1 (#260) untouched.** See [`research/2026-07-03_engine-verdict-exposure-sweep_result.md`](../../../research/2026-07-03_engine-verdict-exposure-sweep_result.md).

> **✅ $k_{\max}$ RELABELED 2026-06-16 (Grant-approved; empirical settle @ `b72045d4`; KEEP-BOTH trail).** The claim above formerly read "$k_{\max} = 0.577/\ell_{\text{node}}$" — but $0.577 = 1/\sqrt3$ is the band's low-$k$ phase-**velocity** factor $c(k\to0)/c_{\text{link}}$ (the 3D-TLM network-velocity projection, `chiral_lattice_dynamics.py:48`), dimensionally length/time, **not** a wavevector $k_{\max}$. It is now relabeled to the actual propagating Nyquist WAVEVECTOR edge, the $\pi/\ell_{\text{node}}$ family: measured $\sqrt2\,\pi\approx4.44/\ell_{\text{node}}$ on the chiral srs axis ($\sqrt3\,\pi\approx5.44$ on the cubic control). **The exemption is reinforced:** the interior $k\approx6.36/\ell_{\text{node}}$ exceeds the corrected wavevector edge ($1.43\times$ srs, $1.17\times$ cubic). The old "$6.36$ vs $0.577$" comparison was a category error (wavevector vs velocity). Relabel propagated in lockstep to the clm-sjjvhf register (`claim-quality.md`) + the derived `claims.jsonl` index. The frozen original framing is preserved verbatim in `session/grants-random-tangents.md:159`.

<!-- claim-quality: clm-3bwhad -->

**"Substrate compression" near a soliton is impedance gradient, not geometric.** The canonical gravity-as-substrate-strain prediction $n(r) = 1 + 2GM/(rc^2)$ is **refractive index** modulation (i.e., impedance modulation $\varepsilon_{\text{eff}}, \mu_{\text{eff}}$ via Axiom 4's kernel $S(A)$ at each cell), NOT geometric bond-length compression. The substrate's "compression" near matter is an impedance gradient via the kernel saturating at the boundary; bond rest length $L_{\text{spring}}$ is a cosmological-genesis frozen value (per the substrate-scale cooled-equilibrium closure), not a per-cell dynamic field. Engine implementations using fixed `dx` Eulerian small-strain on rigid grid geometry are CORRECT for substrate-observability purposes — not a limitation, the right physics for boundary-only observability.

## We sit inside the cosmic $\Gamma = -1$ boundary

The substrate-observability rule applies to ourselves. We are inside the cosmic $\Gamma = -1$ surface (the cosmic horizon = parent-black-hole Schwarzschild radius per the generative cosmology). We measure $\mathcal{M}_{\text{cosmic}}, \mathcal{Q}_{\text{cosmic}}, \mathcal{J}_{\text{cosmic}}$ from inside via local-physics consequences: CMB anomalies, large-scale-structure rotation, Hubble flow anisotropy. The mechanism that set $\mathcal{J}_{\text{cosmic}}$ at lattice genesis is the universal Axiom 4 strain-snap mechanism — directly observable at every smaller scale.

## Cross-references

- **Canonical manuscript anchors:**
  - Common Foreword §"Three Boundary Observables and the Substrate-Observability Rule"
  - Vol 1 Ch 1 (Four Fundamental Axioms) §sec:substrate_vocab_box_ch1
  - Vol 1 Ch 8 (Alpha Golden Torus) — $\alpha^{-1}$ decomposition derivation
  - Backmatter Ch 7 — Universal Saturation-Kernel Catalog — same-mechanism-at-all-scales empirical demonstration
- **KB cross-cutting:**
  - [trampoline-framework.md §4-§7](trampoline-framework.md) — picture-first multi-scale hierarchy
  - [Vol 1 Ch 8 — Alpha Golden Torus](../vol1/ch8-alpha-golden-torus.md) — geometric derivation of the $\alpha^{-1}$ three-regime closure