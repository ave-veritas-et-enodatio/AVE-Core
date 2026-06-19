[↑ Ch. 18: Experimental Prints](../index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Ch.18 experimental-prints routing leaf: documents FDM kit exports and topology laboratory exercises only. No new substrate-physics claim — identity-class consistency on discrete graph isomorphism."
-->

# Experimental Prints — Topology Laboratory Exercises

> **PROVISIONAL / WORK-IN-PROGRESS.** The emitted STLs are geometry-faithful previews of the engine diamond-K4 topology, but are **not yet watertight or print/mate-validated**. Known limitations: (a) the boolean-CSG export is not yet welded watertight — the node meshes reload non-manifold (`vacuum_node_A_capacitive.stl` and `vacuum_node_B_inductive.stl` reload `watertight=False`, `is_volume=False`; the bond reloads `watertight=True` but `is_volume=False`); the kit driver now runs an on-disk QC that reports the true reloaded state per part. (b) bond↔socket press-fit interference is currently **0 mm** — the parts will **not** mate as-is. Mesh remediation is tracked.

Vol.~9 Ch.~18 documents **bench-adjacent pedagogical exercises** using 3D-printable exports of the production diamond K4 vacuum lattice. These are **not** falsification experiments (Ch.~15) and **not** numerical simulations (Ch.~17). They are **hands-on consistency checks** that the exported graph matches the engine substrate (`build_diamond_net`).

## Epistemic position

| Aspect | Status |
|---|---|
| **What is verified** | Graph isomorphism: bipartite A/B nodes, $z=4$ Op5 ports, TL bonds along tetrahedral NN vectors |
| **What is NOT verified** | Physical absolute scale, sub-node body resolution, particle mass sizes |
| **Scale class** | **[RENDERING]** per [`assets/3d_models/ACCURATE_SCALING.md`](../../../../assets/3d_models/ACCURATE_SCALING.md) |
| **Discipline** | `consistency-vs-emergence` v1.3: **identity-class consistency** on discrete topology |

Corpus $\ell_{node} \approx 386\,\mathrm{fm}$. **Kit default print pitch: $100\,\mathrm{mm}$ per $\ell_{node}$** (~10.4 mm hex collar flat-to-flat). Corpus mnemonic $38.6\,\mathrm{mm}$ is documented separately — too fine for most FDM. Override: `KIT_PRINT_MM_PER_L_NODE` (try 80–100).

**Print pose.** Kit STLs export bed-ready (`stl_export_frame: print_pose` in manifest): Type-A cube face flat; Type-B L-ring in XY; bond axis vertical (+Z). Assembly coordinates in the JSON remain engineering-frame.

## Production substrate vs chirality instrument

| Export | Engine source | Role |
|---|---|---|
| **Production vacuum** | `build_diamond_net` | D1 production K4 (achiral Fd-3m); **this is the exercise substrate** |
| **srs showpiece** | `build_srs_net` | Degree-3 chirality **acceptance instrument** (optical activity / A1b); **not** the production engine net |

## Kit SKU (DIY assembly)

Three repeatable molds + JSON manifest (`assets/3d_models/kit/`):

| Part | File | Print count (example $L=4$ starter) |
|---|---|---|
| Type-A capacitive cell | `vacuum_node_A_capacitive.stl` | 8 |
| Type-B inductive cell | `vacuum_node_B_inductive.stl` | 8 |
| Diamond TL bond insert | `vacuum_tl_bond_diamond.stl` | 14 |
| Assembly manifest | `vacuum_assembly_L4.json` | 1 |

**A/B = bipartite sublattice, not a DOF split.** Type-A / Type-B is the diamond **bipartite sublattice** (and the print's shape / port-orientation key), **not** a partition of the substrate's degrees of freedom. Per Axiom 1 (Ch.~9: 6 DOF per K4 node = 3 translational $\to \mathbf{E}$ *and* 3 microrotational $\to \mathbf{B}$), **every** node is a full LC oscillator carrying all six DOF — both the $\varepsilon_0$ E-store and the $\mu_0$ B-store. The `_capacitive` (A) / `_inductive` (B) tags are an **E-vs-B emphasis mnemonic** giving the two bodies a distinguishable shape (cube vs sphere+ring) for hand assembly; they do **not** mean an A node stores only $\mathbf{E}$ or a B node stores only $\mathbf{B}$.

Bond centre pitch $= \sqrt{3}\,\times$ (mm per $\ell_{node}$); insert length fits port-collar mouths on an A--B pair.

**Friction-fit joinery (kit v1, PROVISIONAL).** Hexagonal port collars with **hollow socket bores** from a boolean mesh that is *intended* to be watertight but is **not yet** on the saved STLs (see WIP banner — node meshes reload non-manifold). Bond OD is set **equal** to the socket inner flat-to-flat (`KIT_BOND_RADIUS = KIT_SOCKET_RADIUS`), so the actual **bond↔socket interference is 0 mm** and parts will not grip as-is — the `KIT_FRICTION_INTERFERENCE_MM=0.05` default is applied only between the peg and socket, not the bond the kit actually prints. The 0.05 mm/side is the design target, not the shipped press-fit. Regenerate after watertight/press-fit remediation.

## Driver registry

| Script | Output |
|---|---|
| `src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py` | Kit STLs + manifest |
| `src/scripts/vol_1_foundations/generate_axiom1_diamond_vacuum_stl.py` | Monolithic LC lattice (+ optional particle embed) |
| `src/scripts/vol_1_foundations/generate_vacuum_lattice_stl.py` | Tube-network previews + unit-cell excerpts |
| `src/scripts/vol_1_foundations/vacuum_lc_geometry.py` | Shared LC cell / TL bond mesh geometry |

Environment: `KIT_PRINT_MM_PER_L_NODE` (kit default **100**), `ASSEMBLY_L` (default **4**), `KIT_FRICTION_INTERFERENCE_MM`. Requires `trimesh` + `manifold3d` for export.

## Laboratory Exercise L-EP1 — Assemble the production chunk

**Objective.** Confirm by assembly that the production vacuum is a **bipartite diamond** with **four tetrahedral ports per node** and **TL segments between port tips** (not centre-to-centre struts).

**Materials.** Printed kit parts; manifest `vacuum_assembly_L{L}.json`; flat assembly surface or jig.

**Procedure.**

1. Read manifest `counts` and `joinery` (port collar radius, bond pitch, orientation key on port index 0).
2. Place Type-A nodes at every manifest `nodes[]` entry with `sublattice: "A"`; Type-B at `"B"`.
3. Press bond hex inserts into exterior port sockets on each `bonds[]` pair (bond flat-to-flat matches socket bore).
4. **Checklist (pass/fail):** every active node has degree 4; every bond is A--B; bond directions match `direction_unit` within jig tolerance; no PBC wrap edges in finite chunk.

**Pass criterion.** Assembled graph matches `build_diamond_net(L)` finite-crystal bond list (engine-isomorphic). **Fail** if degree $\neq 4$, mixed-parity inactive sites appear, or bond length outliers indicate PBC wrap struts.

## Laboratory Exercise L-EP2 — Monolith vs kit (optional)

**Objective.** Compare monolithic `vacuum_axiom1_diamond_lc_full_lattice.stl` against the kit assembly for **same $L$ chunk** at same `PRINT_MM_PER_L_NODE`.

**Pass criterion.** Bbox span and bond pitch agree within print tolerance; A/B cell bodies visually distinct (cube vs sphere+ring EE map).

## Open items (not closed by prints)

- Sub-node body scale (proton $D_p \ll \ell_{node}$) — unrenderable as resolved lattice geometry.
- Phase-space $(2,q)$ windings — dynamics **inside** nodes/bonds, not separate kit bricks.
- Accurate inter-particle size ratios — see ACCURATE_SCALING.md; particle snap-ins are topology demos only.

## Cross-references

- Ch.~11 Topological Characteristics (K4 graph, bipartite sublattice)
- Ch.~3 Pin and Port Configuration (Op5 ports, TL bonds)
- Ch.~1 General Description (LC cell per node)
- Ch.~17 Engine Requirements (simulator spec — complementary, not replaced by prints)
