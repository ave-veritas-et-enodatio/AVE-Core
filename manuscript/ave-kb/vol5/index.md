[↑ AVE Knowledge Base](../entry-point.md)
<!-- claim-quality (subtree): rppigm -->

> ⛔ **Bootstrap.** Leaves are canonical; this index and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this volume, load [`./claim-quality.md`](./claim-quality.md) and [`../claim-quality.md`](../claim-quality.md). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Vol 5: Topological Biology

Vol 5 derives a complete biological circuit framework from the AVE vacuum lattice axioms, with zero free parameters. The electromechanical transduction constant $\xi_\text{topo} = e/\ell_\text{node}$ maps atomic mass to inductance and bond stiffness to capacitance, enabling amino acids to be modeled as SPICE electronic circuits.

> **Repo scope note.** The protein folding engine (Chs. 3–5: $Z_\text{topo}$ definition and per-residue impedance table, 8-tier simulation architecture, 2D TL network solver, compaction physics, folding timescale derivation, 20-protein PDB validation, $S_{11}$ objective function, Kramers folding time) is maintained in a separate private repository (`AVE-Protein`) within the `ave-veritas-et-enodatio` GitHub organization. This index covers Chs. 1–2 (LC mapping theory) and Ch. 6 (biological-application hypotheses) — the material that lives in this repo. Cross-repo content is not surfaced here.

## Key Results

| Result | Statement |
|---|---|
| Electromechanical Transduction Constant | $\xi_\text{topo} \equiv e / \ell_\text{node} = e \, m_e \, c / \hbar \approx 4.149 \times 10^{-7}$ C/m |
| Topological Inductance | $L_\text{atom} = m_\text{atom} / \xi^2_\text{topo}$ |
| Topological Capacitance | $C_\text{bond} = \xi^2_\text{topo} / k_\text{bond}$ |
| Bond eigenvalue | $d_\text{eq} = \sqrt{2}\,\sqrt{r_A \cdot r_B} \times \sqrt{T^2(N_\text{eff})/T^2(2)}$ |
| Hydrogen bond distance | $d_\text{HB} = 1.754$ Å (Op4 equilibrium) |
| Hydrogen bond energy | $E_\text{HB} = 4.98$ kcal/mol (experimental: $5.02 \pm 0.05$) |
| Membrane yield temperature | $T_c \approx 278.3$ K ($+5.1^\circ$C); cholesterol buffers to $\sim$485 K |

## Domains

| Domain | Summary |
|---|---|
| [Molecular Foundations](./molecular-foundations/index.md) | Atomic translation layer: $\xi_\text{topo}$ derivation, mass→inductance, stiffness→capacitance, amino acid SPICE circuits, FTIR validation, first-principles force constants, H-bond Op4 equilibrium ($d_\text{HB}=1.754$ Å, $E_\text{HB}=4.98$ kcal/mol), membrane phase buffering. Chapters 1--2. |
| [Biological Applications](./biological-applications/index.md) | Pharmacology and pathology hypotheses: cancer as impedance decoupling, red light therapy, methylene blue as molecular impedance bridge, creatine as neural decoupling capacitor, consciousness as cavity eigenmode, EMDR as impedance annealing. Chapter 6. No resultboxes — predictions and hypotheses. |

## Translation Tables

| Document | Contents |
|---|---|
| [Vol 5 Translation Tables](./common/index.md) | Biology $\leftrightarrow$ EE $\leftrightarrow$ AVE mapping tables for protein folding and solver domains |
