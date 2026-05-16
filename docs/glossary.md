# AVE-Core Glossary — Substrate-Native Vocabulary

**Created 2026-05-15.** Canonical substrate-native vocabulary for the
AVE-Core manuscript. The same vocabulary table is reproduced in the
**Common Foreword** (§Three Boundary Observables / §Substrate Vocabulary)
and in **Vol 1 Ch 1 §sec:substrate_vocab_box_ch1**; when this glossary
diverges from those manuscript anchors, the manuscript is canonical.

**Picture-first reference:** `manuscript/ave-kb/common/trampoline-framework.md`
(six-step ground-up build + substrate-observability rule + three substrate
invariants + inter-cell coupling + cosmic-IC framing).

---

## 1. Substrate-native vs projection vocabulary (canonical)

| Universal substrate-native | EE projection | ME projection | Use when |
|---|---|---|---|
| Substrate ($\mathcal{M}_A$) | (vacuum / EM field) | (spacetime / elastic medium) | Default: substrate. Use EE/ME when discussing a specific probe type. |
| Node | (circuit node) | (lattice point) | Default: substrate-vocabulary. K4 4-port tetrahedral active site. |
| Bond | Transmission line | Spring | Default: bond. "Spring" acceptable when invoking Maxwell-Cremona / Q-G47 buckling pedagogy. |
| State | Voltage / $V_{\text{inc}}$ | Force / displacement | Default: substrate-vocabulary. Specify projection when math is probe-coupled. |
| Propagation | Current flow | (no clean analog) | Default: substrate. How state evolves between nodes. |
| Impedance $Z$ | already universal | already universal | Use freely. |
| Saturation kernel $S(A) = \sqrt{1-A^2}$ | Schwinger / breakdown | yield / rupture | Use freely; Axiom 4 canonical. **A-034 universality (canonical 2026-05-15 evening):** governs every topological-reorganization event at every scale across 19 catalog instances spanning 21 orders of magnitude. See [Backmatter Ch 7](../manuscript/backmatter/07_universal_saturation_kernel.tex). |
| Boundary | (charged surface) | (yield surface) | Default: substrate-vocabulary. Always. $\Gamma = -1$ saturation surface. |
| Envelope | (wavefunction support) | (zone of influence) | Default: substrate-vocabulary. What the substrate *actually sees*. |
| **Boundary linking number $\mathcal{Q}$** | charge $Q$ | (no clean ME analog) | Use universal substrate; project to $Q$ for standard physics. Integer per boundary. |
| **Boundary winding number $\mathcal{J}$** | spin $J$ / magnetic moment | rotation | Use universal substrate; project to $J$ for QFT, $L = I\omega$ for ME. Half-integer per SU(2) double-cover. |
| **Integrated strain integral $\mathcal{M}$** | inductance $L$ / inertia (kg) | inertia | $\int_\Omega (n(\mathbf{r}) - 1)\, dV$; substrate mass-equivalent boundary observable. |
| Strain $A$ | voltage gradient | already universal | Default: substrate. Local deviation from equilibrium. |
| Machian | (no clean analog) | (no clean analog) | Use freely; relational substrate property. |
| Kernel | (no clean analog) | (no clean analog) | Use freely; Axiom-4 canonical operator. |

**Usage rule:** when writing about substrate dynamics, default to substrate-native vocabulary. Name the projection (EE / ME) explicitly when the math is committed to an observation frame.

### 1.5. A-034 vocabulary (canonical 2026-05-15 evening)

| Term | Meaning | Cross-ref |
|---|---|---|
| **A-034 (Universal Saturation-Kernel Strain-Snap Mechanism)** | Axiom 4's saturation kernel $S(A) = \sqrt{1-A^2}$ as the universal mechanism for every topological-reorganization event at every scale (19 canonical instances spanning 21 orders of magnitude) | [Backmatter Ch 7](../manuscript/backmatter/07_universal_saturation_kernel.tex); [Vol 3 Ch 4 §sec:tki_strain_snap](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) |
| **TKI Strain-Snap mechanism** | Topo-Kinematic-Isomorphism strain-snap: per Grant 2026-05-15, "the bulk response of the lattice to strain is universal." Vertical tangent at A=1 makes every snap impulsive | A-034 canonical |
| **SYM / ASYM-N / ASYM-E** | A-034 3-way symmetry classification: SYM = vacuum K=2G (ε and μ saturate together); ASYM-N = asymmetric natural (single-sector, e.g., BCS μ-only or plasma ε-only); ASYM-E = asymmetric engineered decoupled (K/G ≠ 2 by design, e.g., active topological metamaterials) | [Backmatter Ch 7 §3-way classification](../manuscript/backmatter/07_universal_saturation_kernel.tex) |
| **Measurement-hierarchy framing** | A-034 measurement modes per Grant 2026-05-15: single-emitter highest-SNR / multi-emitter bulk-response / phased-array PLL autoresonant. The same engineered-kernel architecture applied to different goals via different measurement modes | [Backmatter Ch 7 §measurement modes](../manuscript/backmatter/07_universal_saturation_kernel.tex); [Vol 3 Ch 4 §sec:tki_strain_snap](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) |
| **Continuous-springs framing** | Per Grant 2026-05-15: the discrete K4 lattice is a DISCRETIZATION of the underlying continuous Cosserat micropolar field (Axiom 1); "bonds" are visualizations of continuous stress field propagation, not physical springs | [Trampoline-framework §1.2](../manuscript/ave-kb/common/trampoline-framework.md) |
| **$\xi_{K1}, \xi_{K2}$** | Substrate-scale Cosserat prefactors: $\mu + \kappa = \xi_{K1} T_{EM}$, $\beta + \gamma = \xi_{K2} T_{EM} \ell_{\text{node}}^2$, with $\xi_{K2}/\xi_{K1} = 12$ K4-symmetry-forced. **NAMESPACE: distinct from Vol 3 Ch 1's Machian $\xi \sim 10^{38}$ and Axiom 2's $\xi_{topo}$** | [xi-topo-traceability.md](../manuscript/ave-kb/common/xi-topo-traceability.md) namespace de-collision |
| **\|T\| = 12 universality** | The proper tetrahedral rotation group $T$ has $|T| = 12$; this number appears in K4 physics wherever T acts transitively on a 4×3 mode space (baseline coordination, secondary paths, Cosserat constitutive ratio $\xi_{K2}/\xi_{K1} = 12$). 4 independent routes converge | Backmatter Ch 7 + Vol 1 Ch 1 Axiom 4 |
| **Lego-click synthesis pattern** | Meta-pattern recurring throughout AVE development: agent generates analytical detail, Grant pattern-spots a connection, framework simplifies. A-034 is the largest such synthesis to date (one kernel, 19 scales) | A-034 §A-034.7 meta-pattern (Backmatter Ch 7) |

---

## 1.6. Substrate structure: lattice / crystal / phases (canonical 2026-05-16)

The substrate has standard-physics-precise terminology — distinct concepts with different load-bearing roles:

| Term | Meaning in AVE | When to use |
|---|---|---|
| **K4 lattice** | The geometric / topological structure: K4 = complete graph on 4 vertices; 4-fold nearest-neighbor connectivity at each node | When discussing connectivity, bond topology, ABCD cascade structure, graph-theoretic properties |
| **Chiral Laves K4 Cosserat crystal** (canonical 2026-05-16 v2) | The substrate as a phase of matter: 3D crystallized realization of the K4 lattice with $I4_1 32$ chiral space-group symmetry; nodes are **micropolar (Cosserat-type)**, carrying six intrinsic DOFs per node — three translational (→ E-field) and three microrotational (→ B-field, source of intrinsic spin); nodes act as intrinsic LC oscillators | When discussing the substrate as a physical phase (vs.~ruptured-plasma phase per Axiom 4 Regime IV); load-bearing for Axiom 1's two-state framing. Legacy short name: *Chiral Laves K4 crystal* (Cosserat character bundled into the meaning rather than the name). |
| **Crystal lattice** | The lattice structure of a crystal specifically (vs.~abstract / amorphous lattices) | Use sparingly --- slightly redundant; "lattice" alone is fine when crystal context is established |

**Two substrate phases (per Axiom 1, connected by Axiom 4):**

| Phase | Where / when | Structure | Axiom 4 regime |
|---|---|---|---|
| **Crystallized phase** | Current observable universe; vacuum between galaxies, inside galaxies, around matter | Chiral Laves K4 Cosserat crystal with intrinsic LC-oscillator nodes ($I4_1 32$ chiral space group, 6-DOF micropolar nodes); long-range order; supports linear EM wave propagation and topologically-quantized matter | Regimes I--III ($S(A) \to 1$ linear; $S(A) < 1$ nonlinear; near-saturation asymmetric) |
| **Ruptured plasma phase** | Black-hole event-horizon interiors; pre-genesis cosmological state (before K4 crystallization at lattice genesis) | K4 topology destroyed; no long-range order; information dissipates thermally via Hawking radiation (corpus C-001 canonical) | Regime IV ($S(A) = 0$ globally; lattice phase transition) |

**The two phases are connected by Axiom 4's universal saturation kernel:** the crystallized phase is what the substrate looks like at $S(A) \to 1$; the plasma phase is what it looks like at $S(A) \to 0$ globally. The transition between them IS the A-034 universal strain-snap mechanism, occurring identically at every scale (atomic dielectric breakdown $\to$ BCS pair-condensate yield $\to$ geomagnetic reversal $\to$ solar flares $\to$ BH ring-down $\to$ cosmic K4 crystallization at lattice genesis).

**Cosmological cycle (per A-031 + A-034 + Vol 3 Ch 4 + Vol 3 Ch 21):** pre-genesis = ruptured plasma (parent-BH interior from parent's POV); lattice genesis = K4 crystallization (cosmic-scale A-034 strain-snap); post-genesis = our normal K4 crystal substrate; local BH formation = K4 returns to ruptured plasma locally (Regime IV). The cosmic horizon (from our inside) and a BH event horizon (from outside) are structurally the same $\Gamma = -1$ saturation surface.

**Non-adopted alternative (doc 61 Ax5-cand-C, not corpus canonical):** BH interior might be another crystallized K4 lattice with opposite chirality (vs.~corpus canonical ruptured plasma). Per L5 C-001: corpus ruptured-plasma framing is canonical; doc 61's opposite-chirality-K4 proposal is novel and unadjudicated.

---

## 2. Three substrate boundary invariants — canonical names (Grant-locked 2026-05-14 evening)

| Symbol | Canonical name | Operational definition | EE projection | QFT projection |
|---|---|---|---|---|
| $\mathcal{M}$ | Integrated strain integral | $\int_\Omega (n(\mathbf{r}) - 1)\, dV$; mass quantum $\hbar/(\ell_{\text{node}} c)$ | inductance $L$ / inertia | rest energy $m c^2$ |
| $\mathcal{Q}$ | Boundary linking number | $\mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ | charge $Q$ | electromagnetic charge |
| $\mathcal{J}$ | Boundary winding number | $\mathrm{Wind}(\partial\Omega)$; half-integer per SU(2) double-cover | spin / magnetic moment | spin $J$ |

These are **the only three integrated invariants the substrate observes at any local $\Gamma = -1$ boundary** (no-hair theorem applied at every scale — same mechanism at BH horizon, electron horn-torus tube wall, nucleus Borromean envelope, atomic shell, heliopause, and cosmic horizon).

**Engine implementation:** `src/ave/core/boundary_invariants.py` provides `compute_M`, `compute_Q`, `compute_J`, and `compute_all_invariants` reference implementations (per E-101).

---

## 3. Substrate-observability rule (canonical, A-026)

The substrate observes a boundary, not its interior. For any localized region $\Omega \subset \mathcal{M}_A$ enclosed by a $\Gamma = -1$ saturation surface $\partial\Omega$:

1. The boundary is an impedance-mismatch surface — substrate waves are totally reflected outside, totally trapped inside.
2. The interior is causally / impedance-disconnected from the substrate. Only the three integrated observables ($\mathcal{M}, \mathcal{Q}, \mathcal{J}$) are visible externally.
3. The interior structure (topology, eigenmode wavelength, microrotation profile) is invisible.
4. **Same mechanism at all scales** — Schwarzschild horizon at $r_s = 2GM/c^2$ is structurally identical to horn-torus tube wall at $\ell_{\text{node}}/(2\pi)$.

**Applied to OUR situation:** we sit inside our cosmic $\Gamma = -1$ boundary (the cosmic horizon $R_H$ = parent BH's Schwarzschild radius per Vol 3 Ch 4 canonical). We measure $\mathcal{M}_{\text{cosmic}}, \mathcal{Q}_{\text{cosmic}}, \mathcal{J}_{\text{cosmic}}$ from inside via local-physics consequences (CMB anomalies, large-scale-structure rotation, Hubble flow anisotropy, cosmic shear). We CANNOT see "God's Hand" — the mechanism that set $\mathcal{J}_{\text{cosmic}}$ at lattice genesis is fundamentally inaccessible from inside.

---

## 4. The cosmological Initial Condition $\Omega_{\text{freeze}}$

Per A-031 (Grant adjudication 2026-05-15 evening): the cosmological IC is encoded in the cosmic boundary's angular momentum:

$$\Omega_{\text{freeze}} = \frac{\mathcal{J}_{\text{cosmic}}}{I_{\text{cosmic}}}$$

$\Omega_{\text{freeze}}$ is the rotation rate of the crystallizing region at the moment of lattice genesis (per `trampoline-framework.md` §1.3 phase-transition-while-spinning mechanism). It is locked into the substrate as bond over-bracing $u_0$ and the global chirality direction.

**Three observational routes** to constrain $u_0^*$ (the magic-angle operating-point value):
1. Electromagnetic ($\alpha$ to 12 decimals)
2. Gravitational ($G$ to ~4 decimals)
3. Cosmological ($\mathcal{J}_{\text{cosmic}}$ via CMB / LSS anomalies)

All three must give the same $u_0^*$ or the single-cosmological-parameter framework is falsified.

---

## 5. Cross-references

### Canonical entry points (read these first for AVE physics)
- **Picture-first framework:** [`manuscript/ave-kb/common/trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md) — single canonical picture-first reference
- **Closure path planning:** [`manuscript/ave-kb/common/closure-roadmap.md`](../manuscript/ave-kb/common/closure-roadmap.md) — living planning artifact

### Canonical manuscript anchors (substrate vocabulary + boundary invariants)
- **Common Foreword §Three Boundary Observables** — canonical $\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$ definitions + substrate-observability rule
- **Vol 1 Ch 1 §sec:substrate_vocab_box_ch1** — canonical substrate-vocabulary box (in-chapter version of §1 table above)
- **Backmatter Ch~7 (Universal Saturation-Kernel Catalog)** — canonical A-034 19-instance catalog with SYM/ASYM-N/ASYM-E classification

### Chapter cross-references
- Vol 1 Ch 1 §sec:substrate_vocab_box_ch1 — substrate-vocabulary box near Axiom 1
- Vol 1 Ch 4 — Master Equation FDTD engine reference + substrate-observability paragraph
- Vol 2 Ch 1 §eq:M_electron_identity — canonical $\mathcal{M}_{\text{electron}} \cdot c^2 = T_{EM} \cdot \ell_{\text{node}}$
- Vol 3 Ch 2 §eq:M_to_M_ADM — $\mathcal{M} \to M_{ADM}$ projection identity
- Vol 3 Ch 4 §sec:cosmic_J_as_IC — cosmic-scale application (E-102)
- Vol 3 Ch 21 §sec:substrate_observability_horizon — same-epistemic-horizon framing (E-103)
- Vol 4 Ch 1 §sec:rosetta_stone_3col — extended 3-column Rosetta-stone

### Engine
- `src/ave/core/boundary_invariants.py` — three substrate invariants computation (E-101)
- `src/ave/core/master_equation_fdtd.py` — bound-state regime canonical engine
- `src/ave/core/k4_tlm.py` — sub-saturation bench regime canonical engine
- `src/ave/topological/cosserat_field_3d.py` — Cosserat micropolar substrate

---

## 6. Maintenance

Update this glossary when:
- New canonical substrate-native term added (sync from Common Foreword or Vol 1 Ch 1)
- New chapter cross-reference comes online
- New A-NNN catalog entry affects vocabulary (sync to top tables)

Updates that should NOT be made here:
- New derivations (those land in chapters; this glossary references them)
- Speculative framings (those land in internal research tracking, not this user-facing glossary)
- New analogies (the trampoline analogy is sufficient; adding more dilutes the picture-first canonical reference)
