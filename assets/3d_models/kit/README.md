# Vacuum lattice DIY kit — print exports

Bed-ready STLs for the Axiom-1 diamond K4 friction-fit kit (Vol. 9 Ch. 18).

## Start here (L=4)

Default manifest is **`vacuum_assembly_L4.json`** — a small crystal you can actually print:

| Part | Qty (L=4) |
|---|---|
| `vacuum_node_A_capacitive.stl` | 8 |
| `vacuum_node_B_inductive.stl` | 8 |
| `vacuum_tl_bond_diamond.stl` | 14 |

Use `vacuum_kit_demo_one_bond_assembly.stl` as the mated reference (not for printing).

For the full L=16 chunk (512+512+1688 parts), regenerate with `ASSEMBLY_L=16`.

## Files (this folder)

| File | Notes |
|---|---|
| `vacuum_node_A_capacitive.stl` | **Solid** cube LC cell (ε); one face on bed |
| `vacuum_node_B_inductive.stl` | **Hollow** sphere + L-ring (μ); ring in XY plane |
| `vacuum_tl_bond_diamond.stl` | Solid hex bond (OD = socket bore); axis vertical (+Z) |
| `vacuum_kit_demo_one_bond_assembly.stl` | **Reference only** — one A+B+bond mated |
| `vacuum_assembly_L{L}.json` | Node positions + bond list for assembly |

**A/B = bipartite sublattice, not a DOF split.** Type-A vs Type-B is the diamond bipartite sublattice (and the print's shape/port-orientation key for assembly), **not** a partition of the substrate's degrees of freedom. Per Axiom 1 (Vol 9 Ch 9: 6 DOF per K4 node = 3 translational → **E** *and* 3 microrotational → **B**), **every** node is a full LC oscillator carrying all six DOF — both the ε₀ E-store and the μ₀ B-store. The `_capacitive` (A) / `_inductive` (B) tags in the filenames are an **E-vs-B emphasis mnemonic** that gives the two bodies a distinguishable shape (solid cube vs sphere+ring) for hand assembly; they do **not** mean an A node stores only E or a B node stores only B.

Default scale: **100 mm / ℓ_node** — hex joinery, ~10.4 mm collar flat-to-flat, Prusa i3 MK3+ tuned.

Meshes are exported as **single watertight solids** (boolean union + bore subtraction) so socket cavities slice empty.

## Prusa i3 MK3+ slicer hints

| Setting | Node A / B | Bond |
|---|---|---|
| Layer height | 0.20 mm | 0.20 mm |
| Perimeters | 3 | 4 |
| Infill | 20% | 40% (gyroid) |
| Supports | None (flat/posed) | None (vertical rod) |
| Brim | Optional on A (port overhangs) | Skirt only |

Collars: **~10.4 mm** hex flat-to-flat, **~2.4 mm** wall. Type-A stems burrow into the cube (~10 mm inboard).

## Regenerate

From repo root (requires `trimesh` + `manifold3d`):

```bash
python -m pip install trimesh manifold3d
PYTHONPATH=src ./.venv/bin/python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
```

Starter chunk (default):

```bash
ASSEMBLY_L=4 PYTHONPATH=src ./.venv/bin/python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
```

Full crystal:

```bash
ASSEMBLY_L=16 PYTHONPATH=src ./.venv/bin/python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
```

## Assembly

Kit sockets mount on the **exterior** of each cell (cube corners for A, sphere surface for B). Press the bond into the socket bore (bond flat-to-flat matches socket inner flat-to-flat).

Monolithic previews live in the parent directory: `../vacuum_axiom1_diamond_lc_*.stl`.
