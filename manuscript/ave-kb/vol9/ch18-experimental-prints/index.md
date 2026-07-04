[↑ Ch. 18: Experimental Prints](../index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Ch.18 experimental-prints routing leaf: documents the rebuilt FDM vacuum-lattice kit (real-space / DOF-basis / phase-space three-tier representation) and its topology-laboratory exercises. No new substrate-physics claim — identity-class consistency on the K4-graph diamond topology, with absolute scale tagged [RENDERING]."
-->

# Experimental Prints — Topology Laboratory Exercises

Vol.~9 Ch.~18 documents **bench-adjacent pedagogical exercises** using a 3D-printable kit that renders a K4 vacuum lattice. These are **not** falsification experiments (Ch.~15) and **not** numerical simulations (Ch.~17). They are **hands-on consistency checks** that the exported graph matches its engine net. (D1 carrier note: the kit's assembled crystal currently prints the degree-4 `build_diamond_net`, which is the non-canonical topology-demo instrument, not the ratified `srs` $z=3$ production carrier — see the Production-carrier-vs-instrument table below.)

> **STATUS — REBUILT + VALIDATED (2026-06-21).** The kit was rebuilt from the cube/sphere preview into a representative, printable model. All ~25 part STLs reload **watertight + `is_volume=True`** (verified on-disk; the saved-QC gate is GATING — the generator exits non-zero if any gated part fails). Press-fit interference is **0.10 mm diametral**. The legacy limitations (non-manifold node STLs; 0 mm press-fit) are **resolved** and are recorded below under *Resolved status* for provenance — they are not current.

## Epistemic position

| Aspect | Status |
|---|---|
| **What is verified** | Graph isomorphism: bipartite A/B nodes, $z=4$ tetrahedral ports, TL bonds along the tetrahedral NN vectors (kit port dirs $==$ engine `_DIAMOND_PORTS`; all bonds bipartite A–B; port-pair angle $109.47° = \arccos(-1/3)$) |
| **What is NOT verified** | Physical absolute scale, sub-node body resolution, particle mass sizes; no LC dynamics; no $(2,q)$ phase-space windings as geometry |
| **Scale class** | **[RENDERING]** per [`assets/3d_models/ACCURATE_SCALING.md`](../../../../assets/3d_models/ACCURATE_SCALING.md) |
| **Discipline** | `consistency-vs-emergence` v1.3: **identity-class consistency** on discrete topology. No new substrate-physics claim is asserted by a printed model. |

A printed model is a **real-space object**; this fixes what it can and cannot honestly represent — the governing principle below.

## The representation principle (three coordinate tiers)

A 3D print lives in real space, so each canonical quantity is rendered only in the tier it actually inhabits:

| Quantity | Coordinate system | Representation in the kit |
|---|---|---|
| Node positions, bonds, 4 tetrahedral ports | **real space** | **isomorphic** — the printed skeleton (degree-4 diamond, true $\sqrt{3}\,\ell_{node}$ pitch) |
| Translational vs micro-rotational vs breathing DOF basis | real-space *directions* at each node | **snap-on color accents** — triad ($\mathbf E$) + 3 rings ($\mathbf B$) + breathing core ($V$) |
| LC-tank saturation-amplitude $A$, $(V_{inc}, V_{ref})$ phasor / impedance plane | **phase space** | **labeled proxy only** — impedance disc + phasor dial, never a printed length |

**Real space is isomorphic.** The kit prints the degree-4 diamond net (the topology-demo instrument, not the `srs` production carrier — D1) with an **identical solid node body for both A and B** sublattices, four tetrahedral **round** bond sockets (round so a rigid bond press-fits both end sockets at any relative rotation — a hex tip cannot face-flush two independently-clocked sockets at once), and bonds at the true $\sqrt{3}\,\ell_{node}$ pitch. **A/B is the bipartite SUBLATTICE label only** (shown by color + a snap-on embossed A/B key) — *not* the old cube-vs-sphere storage split. Per Axiom 1 (Ch.~9), **every** node is a full LC oscillator carrying all 6 spatial DOF (3 translational $\to \mathbf E$ store *and* 3 microrotational $\to \mathbf B$ store); the prior `_capacitive` (A) / `_inductive` (B) shapes encoded a denied storage asymmetry and have been removed.

**The DOF basis is shown by accents, not by node shape.** Three snap-on color-accent parts, identical on every node:

- **triad_E** — 3-axis orthogonal triad = 3 translational DOF $\to \mathbf E$ / dielectric displacement $\to \boldsymbol\varepsilon^2$ store.
- **rings_B** — 3 orthogonal rings = 3 micro-rotational DOF $\to \mathbf B$ / inductive flywheel / spin $\to \boldsymbol\kappa^2$ store.
- **breathing_V** — a radial breathing indicator at the node core = the **A1 volumetric breathing mode** $\to V^2$ store $=$ **mass**.

This is the **7-mode store split** $A^2 = \varepsilon^2 + \kappa^2 + V^2$ (6 spatial DOF + 1 A1 breathing). The breathing axis is kept **independent of the rotation rings** — **A1 $\perp$ T2** (`master-equation.md:20`): the mass (A1 dilatation) and charge/spin (Cosserat micro-rotation) grades are orthogonal and never share one phasor.

**Phase space is a labeled proxy, never a length.** The LC-tank state — the saturation amplitude $A$ and the $(V_{inc}, V_{ref})$ phasor — is rendered only by a separate **impedance disc + phasor dial**, each stamped **`[STATE-SPACE — NOT A COORDINATE]`** (the physical analog of the `[RENDERING]` scale tag). Because **A1 $\perp$ T2**, the phasor instrument provides *two independent orthogonal* indicators, never one merged dial. The saturation amplitude $A$ is the LC-tank **state**, not a 7th spatial DOF.

## Production carrier vs topology-demo instrument (D1, Grant 2026-07-03)

| Export | Engine source | Role |
|---|---|---|
| **Production carrier** | `build_srs_net` | Degree-3 chiral `srs` net (Sunada-K4 / Laves / $I4_1 32$; the object Axiom 1 names) — the **ratified production carrier** (D1, Grant 2026-07-03); both enantiomorphs ($I4_1 32$ right / $I4_3 32$ left, $120°$ bonds), handedness glyph. Currently shipped as an accent piece. |
| **Topology-demo instrument** | `build_diamond_net` | Degree-4 diamond K4 (achiral Fd-3m); a **non-canonical topology-demo instrument** (statics-pathological). The kit's assembled crystal currently prints this net — a **deferred code-migration item** (re-home onto `srs`; `_orchestration/2026-07-03_srs-migration-policy.md` §d). |

Per the **D1 ratification** (Grant 2026-07-03, [`_orchestration/index.md`](../../../../_orchestration/index.md)), the production substrate is the chiral `srs` $z=3$ net (the object Axiom 1 names) and the achiral diamond $z=4$ net is re-tagged a non-canonical instrument (statics-pathological). The kit's historical manifest label "diamond production K4 (`build_diamond_net`)" is therefore a **naming defect**, pending the deferred srs-name-walkback arc (§d; executes nothing here — the current print still emits the diamond net). The "K4" surface form is a documented three-way overload (axiom-name *chiral Laves K4* $=$ degree-3 srs, the carrier; engine *K4* $=$ degree-4 diamond, this instrument; rotation group $K_4$, a distinct group label); the kit labels each piece by its actual degree and does not silently conflate them.

## Kit roster (BOM tiers)

Generated by `src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py`; manifest `assets/3d_models/kit/vacuum_assembly_L4.json` (schema `ave-vacuum-kit/v2`). STL artifacts are **generated (gitignored)** — the generators are the source of truth.

| Tier | Parts |
|---|---|
| **Structural base** (monochrome, one filament each) | `vacuum_node_A.stl`, `vacuum_node_B.stl`, `vacuum_bond.stl` |
| **DOF accents** (color per store, snap-on) | `accent_triad_E.stl` (E / $\varepsilon^2$), `accent_rings_B.stl` (B / $\kappa^2$), `accent_breathing_V.stl` (A1 / mass / $V^2$), `key_A.stl`, `key_B.stl` |
| **Phase space** (state-space proxy) | `phase_impedance_disc.stl`, `phase_dial_body.stl`, `phase_dial_pointer.stl`, `phase_dial2_body.stl`, `phase_dial2_pointer.stl` |
| **Chiral srs instrument** | `srs_node_right.stl`, `srs_node_left.stl`, `srs_bond.stl`, `srs_handedness_right.stl`, `srs_handedness_left.stl` |
| **Assembly jig** | `jig_unit_cell.stl`, `jig_tile_*.stl` (tiled to the $250\times210$ bed) |
| **Reference only** | `reference_tetra_unit_cell.stl` (fused visual preview, not for printing), `scale_plate.stl` |

**Starter chunk ($L=4$ finite crystal).** 16 nodes (8 A + 8 B), 14 bonds; assembled bbox $300\times300\times300$ mm. Node bodies are identical (A/B differ only by key + color).

**Hero first print (recommended starter).** A single **tetrahedral unit cell** — 1 node_A + 4 node_B + 4 bonds + accents + `jig_unit_cell` (~9 parts) — shows $z=4$ coordination, A/B bipartiteness, and the tetrahedral ports without the full 30-part $L4$ build.

## Keyed base jig (forced assembly)

The four tetrahedral ports are geometrically identical, so the kit ships a **keyed baseplate** (tiled to the $250\times210$ bed) with **embossed node-id + A/B pockets** and **per-port pips**. A builder drops each node into its keyed pocket and the pips show which port $\to$ which neighbor. The placement map and the port$\to$neighbor map are carried in the manifest (`nodes[].ports`, each `{port: 0–3, neighbor: <node id>}`), so both *where each node goes* and *which port mates which neighbor* are forced rather than guessed.

## Scale and magnification

Corpus $\ell_{node} = \hbar/(m_e c) \approx 386\,\mathrm{fm}$ is **definitional** (the electron reduced-Compton length), not derived. **Kit default print pitch: $100\,\mathrm{mm}$ per $\ell_{node}$** — magnification $\approx 2.59\times10^{11}$ (`KIT_PRINT_MM_PER_L_NODE`, default 100; bridges the shared module). The corpus mnemonic $38.6\,\mathrm{mm}$ is **reference-only** (a digit tie, $\ell_{node}/10$ in fm), not the print scale. A `scale_plate` part embosses a language-free $1\text{-}\ell_{node}$ scale bar; the whole joinery/geometry block is tagged **[RENDERING]**.

## Driver registry

| Script | Output |
|---|---|
| `src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py` | Kit STLs + manifest (rebuilt driver; part roster + manifest builder) |
| `src/scripts/vol_1_foundations/generate_axiom1_diamond_vacuum_stl.py` | Monolithic LC lattice (+ optional particle embed) |
| `src/scripts/vol_1_foundations/generate_vacuum_lattice_stl.py` | Tube-network previews + unit-cell excerpts |
| `src/scripts/vol_1_foundations/vacuum_lc_geometry.py` | Shared LC cell / TL bond mesh geometry |

Regenerate: `PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py`. Environment: `KIT_PRINT_MM_PER_L_NODE` (kit default **100**), `ASSEMBLY_L` (default **4**), `KIT_FRICTION_INTERFERENCE_MM` (per-side mm; default 0.05), `KIT_ALLOW_NONMANIFOLD=1` (WIP escape hatch for the GATING QC). Requires `trimesh` + `manifold3d`.

## Laboratory Exercise L-EP1 — Assemble the diamond topology-demo chunk

**Objective.** Confirm by assembly that the production vacuum is a **bipartite diamond** with **four tetrahedral ports per node** and **TL segments between port tips** (not centre-to-centre struts).

**Materials.** Printed kit parts; the keyed base jig; manifest `vacuum_assembly_L{L}.json`.

**Procedure.**

1. Print the jig tiles; assemble the keyed baseplate.
2. Read manifest `counts`, `joinery`, and `nodes[].ports` (the port$\to$neighbor map).
3. Drop each node into its keyed jig pocket (pocket emboss $=$ node id $+$ A/B); colour A vs B per the sublattice key.
4. Press bonds into the sockets following the per-port pips (`nodes[].ports`).
5. *(Optional)* snap on the DOF accents (triad_E / rings_B / breathing_V) coloured per store; set the phasor dial / read the impedance disc as the LC-tank STATE (not a position).
6. **Checklist (pass/fail):** every active node has degree 4; every bond is A–B; bond directions match `direction_unit` within jig tolerance; no PBC wrap edges in the finite chunk.

**Pass criterion.** Assembled graph matches `build_diamond_net(L)` finite-crystal bond list (engine-isomorphic). **Fail** if degree $\neq 4$, mixed-parity inactive sites appear, or bond-length outliers indicate PBC wrap struts.

## Laboratory Exercise L-EP2 — Monolith vs kit (optional)

**Objective.** Compare the monolithic lattice export against the kit assembly for the **same $L$ chunk** at the same print pitch.

**Pass criterion.** Bbox span and bond pitch agree within print tolerance; node bodies are identical (A/B distinguished only by key + colour, *not* by shape — the storage-split mnemonic is gone).

## Laboratory Exercise L-EP3 — Production carrier vs topology-demo instrument (optional)

**Objective.** Hold the degree-3 `srs` production-carrier piece (both enantiomorphs) beside the degree-4 achiral diamond topology-demo instrument and confirm they are **distinct objects**: srs is $120°$, degree-3, handed ($I4_1 32$); the diamond net is tetrahedral, degree-4, achiral (Fd-3m).

**Pass criterion.** The handedness glyph distinguishes $I4_1 32$ (right) from $I4_3 32$ (left); the builder can state which piece is the **ratified production carrier** (the chiral `srs` net — the object Axiom 1 names, carrying the optical-activity / chirality story) and which is the **non-canonical topology-demo instrument** (the achiral diamond, statics-pathological). Records the D1-ratified srs-$z=3$-production / diamond-$z=4$-instrument reading (Grant 2026-07-03); the current kit still prints the diamond instrument (a deferred code-migration item, `_orchestration/2026-07-03_srs-migration-policy.md` §d).

## Resolved status (was: known limitations)

| Item | Legacy state | Current (2026-06-21) |
|---|---|---|
| Node STL manifoldness | Node A/B reloaded non-manifold (`watertight=False`, `is_volume=False`); bond `is_volume=False` | **Resolved** — all gated parts reload `watertight=True` + `is_volume=True`; root cause was the numpy-stl round-trip, fixed by direct `trimesh` export |
| QC gating | Report-only, shipped known-broken STLs | **Resolved** — `saved_qc` is GATING (`sys.exit(1)` on any gated failure; `KIT_ALLOW_NONMANIFOLD=1` to override for WIP) |
| Press-fit | $0.00$ mm interference (bond OD $=$ socket bore) — would not mate | **Resolved** — $0.10$ mm diametral interference; tune via `KIT_FRICTION_INTERFERENCE_MM` |
| A/B representativeness | Cube (A) vs sphere+ring (B) encoded a denied storage split | **Resolved** — identical node body; A/B is colour + snap-on key only |
| Unkeyed ports | 4 identical ports, no placement guidance | **Resolved** — keyed base jig + `nodes[].ports` map force placement and port$\to$neighbor |
| Bond pose / insertion | 143 mm bond printed vertical (20:1, topples); zero axial insertion | **Resolved** — bond prints horizontal with real insertion depth |

## Open items (Grant-gated physics — NOT touched by the print)

The print stays consistent with the adjudicated reading and asserts nothing beyond it; these seams remain open in the corpus, unchanged:

- **Chirality realization** — achiral diamond + excited $k_\chi$ Cosserat order-parameter vs natively-chiral lattice. **D1 RATIFIED (Grant 2026-07-03):** the natively-chiral `srs` $z=3$ net is the production carrier; the achiral diamond $z=4$ net is a non-canonical instrument. The physics reconciliation $Fd\text{-}3m \supset I4_1 32$ stands; the residual is purely the **naming defect** in the kit's manifest/generator (it still emits `build_diamond_net`), which the deferred srs-name-walkback arc (`_orchestration/2026-07-03_srs-migration-policy.md` §d) resolves — the datasheet prose is now walked to the ratified framing; the generator rename is future-arc code work.
- **Crystalline vs amorphous** — degree-4 crystalline $Fd\text{-}3m$ graph vs the amorphous $z_0$ effective-coordination picture (a real open seam the corpus admits). The kit prints the degree-4 crystalline graph and implies neither $z_0$ nor $z_{\text{eff}}$.
- **Proton multi-node vs nucleus-in-single-node** — sub-node body scale ($D_p \ll \ell_{node}$) is unrenderable as resolved lattice geometry; particle snap-ins would be topology demos only.
- **Phase-space $(2,q)$ windings** — dynamics *inside* nodes/bonds, represented only by the phase-space disc/dial, never as separate kit bricks.

## Cross-references

- Ch.~11 Topological Characteristics (K4 graph, bipartite sublattice, A1 $\oplus$ T2 split)
- Ch.~9 Mechanical Characteristics (6 DOF + A1 breathing; A1 $\perp$ T2)
- Ch.~3 Pin and Port Configuration (tetrahedral ports, TL bonds, breathing mode)
- Ch.~1 General Description (LC cell per node)
- Ch.~17 Engine Requirements (simulator spec — complementary, not replaced by prints)
