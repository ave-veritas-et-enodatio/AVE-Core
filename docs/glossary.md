# AVE-Core Glossary — Substrate-Native Vocabulary

**Created 2026-05-15** per E-094 substrate-vocab propagation (Tier 1 closure-roadmap).
Mirrors AVE-QED `docs/glossary.md` §5m (Grant Q1 closure 2026-05-14 evening, canonical).

**Upstream canonical:** AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex`
(7-section appendix) + AVE-QED `docs/glossary.md` §5m (14-row substrate-native /
EE / ME table). When this glossary diverges from upstream, upstream is canonical.

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
| Saturation kernel $S(A) = \sqrt{1-A^2}$ | Schwinger / breakdown | yield / rupture | Use freely; Axiom 4 canonical. |
| Boundary | (charged surface) | (yield surface) | Default: substrate-vocabulary. Always. $\Gamma = -1$ saturation surface. |
| Envelope | (wavefunction support) | (zone of influence) | Default: substrate-vocabulary. What the substrate *actually sees*. |
| **Boundary linking number $\mathcal{Q}$** | charge $Q$ | (no clean ME analog) | Use universal substrate; project to $Q$ for standard physics. Integer per boundary. |
| **Boundary winding number $\mathcal{J}$** | spin $J$ / magnetic moment | rotation | Use universal substrate; project to $J$ for QFT, $L = I\omega$ for ME. Half-integer per SU(2) double-cover. |
| **Integrated strain integral $\mathcal{M}$** | inductance $L$ / inertia (kg) | inertia | $\int_\Omega (n(\mathbf{r}) - 1)\, dV$; substrate mass-equivalent boundary observable. |
| Strain $A$ | voltage gradient | already universal | Default: substrate. Local deviation from equilibrium. |
| Machian | (no clean analog) | (no clean analog) | Use freely; relational substrate property. |
| Kernel | (no clean analog) | (no clean analog) | Use freely; Axiom-4 canonical operator. |

**Usage rule:** when writing about substrate dynamics, default to substrate-native vocabulary. Name the projection (EE / ME) explicitly when the math is committed to an observation frame.

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

### Upstream canonical (AVE-QED)
- AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex` (formal 7-section appendix)
- AVE-QED `manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex` (multi-scale Machian network)
- AVE-QED `docs/glossary.md` §5m (vocab table source)
- AVE-QED `docs/analysis/2026-05-14_three_substrate_invariants_matrix.md` (Q1 closure matrix)

### L5 framework tracking
- [`research/L5/axiom_derivation_status.md`](../research/L5/axiom_derivation_status.md) — A-026 / A-028 / A-029 / A-030 / A-031 canonical entries
- [`research/L5/manuscript_pending.md`](../research/L5/manuscript_pending.md) — E-094 (this entry) + propagation status

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
- New canonical substrate-native term added (sync from AVE-QED upstream)
- New chapter cross-reference comes online (E-094 status migration in manuscript_pending.md)
- New L5 A-NNN canonical entry affects vocabulary (sync to top tables)

Updates that should NOT be made here:
- New derivations (those land in chapters; this glossary references them)
- Speculative framings (those land in L5 axiom_derivation_status.md as A-NNN entries)
- New analogies (the trampoline analogy is sufficient; adding more dilutes the picture-first canonical reference)
