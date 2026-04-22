# Step 1 — K4 Rotation Group Action on Tetrahedral Port Labels

**Status:** DERIVATION. Step 1 of the two-node-electron derivation plan
at `.claude/plans/read-the-collaboration-md-first-resilient-mccarthy.md`
§19. Foundation for Step 2 (spin-½ from K4 bipartite structure).

**Goal:** explicitly derive how 3D rotations act on the K4 tetrahedral
port basis `{p_0, p_1, p_2, p_3}`, identify the symmetry group, and
prepare the framework for Step 2's SU(2) double-cover analysis.

**Falsification criterion:** if the rotation action does not form a
faithful representation of the tetrahedral group `T = A_4`, the K4
lattice does not have the symmetry we claim, and the spin-½ derivation
fails immediately.

---

## §1 The K4 tetrahedral port basis

From [`src/ave/core/k4_tlm.py:80-86`](../../src/ave/core/k4_tlm.py#L80),
the K4 diamond lattice has 4 ports per node with tetrahedral connection
vectors (A → B sublattice direction):

```
p_0 = (+1, +1, +1)
p_1 = (+1, −1, −1)
p_2 = (−1, +1, −1)
p_3 = (−1, −1, +1)
```

These four vectors:
- Have equal magnitude `|p_j| = √3`
- Have product of components +1 (even parity — i.e., even number of minus signs in {+,−,−} or {−,−,+} or {+,+,+}, etc., making three +1's or one +1 and two −1's)
- Form a regular tetrahedron inscribed in the cube `[±1]³`
- Sum to zero: `Σ_j p_j = (0, 0, 0)` (centered at origin)
- Have pairwise dot products `p_i · p_j = −1` for `i ≠ j` (so angle = arccos(−1/3) ≈ 109.47°)

Verification of the dot product (e.g., `p_0 · p_1 = 1 − 1 − 1 = −1`)
gives the standard tetrahedral angle.

## §2 The tetrahedral rotation group

The symmetry group of a regular tetrahedron under rotations only is the
**tetrahedral group `T`**, isomorphic to the alternating group `A_4`
(even permutations of 4 elements), order **12**.

`T` contains three conjugacy classes:

| Class | Order | Number | Description |
|---|---|---|---|
| `{e}` | 1 | 1 | Identity |
| `C_3` | 3 | 8 | Rotations by ±120° about each of the 4 vertex axes (4 axes × 2 directions = 8) |
| `C_2` | 2 | 3 | Rotations by 180° about each of the 3 face-midpoint axes |

Total: 1 + 8 + 3 = 12 = |A_4| ✓

(The full symmetry group `T_d` includes reflections and has order 24,
isomorphic to `S_4`. We focus on rotations only, giving `T = A_4`.
The double cover of `T = A_4` is the binary tetrahedral group
`2T`, order 24, a subgroup of SU(2) — used in Step 2.)

## §3 Explicit permutations under each rotation class

### §3.1 Identity

`e: p_j → p_j` for all j. Permutation = `(0)(1)(2)(3)` = identity.

### §3.2 Vertex-axis rotations (`C_3` class, 8 elements)

A 120° rotation about the axis along `p_0 = (+1,+1,+1)` cycles the
other three ports in the plane perpendicular to `p_0`:

`R_{p_0, +120°}: p_0 → p_0, p_1 → p_2, p_2 → p_3, p_3 → p_1`

Permutation in cycle notation: `(123)` (fixing 0).

To verify: the rotation matrix about axis `n̂ = (1,1,1)/√3` by 120°
is `R = exp(120° · n̂ × ·)`. Applied to `p_1 = (+1,−1,−1)` should
give `p_2 = (−1,+1,−1)`. (Standard tetrahedral group action — verified
in any group theory text or by direct matrix calculation.)

The 8 elements of class `C_3`:
| Axis | Direction | Permutation |
|---|---|---|
| `p_0` axis | +120° | (123) |
| `p_0` axis | −120° | (132) |
| `p_1` axis | +120° | (032) |
| `p_1` axis | −120° | (023) |
| `p_2` axis | +120° | (013) |
| `p_2` axis | −120° | (031) |
| `p_3` axis | +120° | (021) |
| `p_3` axis | −120° | (012) |

Each is a 3-cycle (even permutation). 8 elements total.

### §3.3 Edge-midpoint axis rotations (`C_2` class, 3 elements)

A 180° rotation about an axis through the midpoints of two opposite
edges of the tetrahedron. The three pairs of opposite edges are:

| Edge pair | Axis | Permutation |
|---|---|---|
| (01) & (23) | through midpoints of edges 0-1 and 2-3 | (01)(23) |
| (02) & (13) | through midpoints of edges 0-2 and 1-3 | (02)(13) |
| (03) & (12) | through midpoints of edges 0-3 and 1-2 | (03)(12) |

Each is a product of two 2-cycles (even permutation). 3 elements total.

To verify: the midpoint of edge 0-1 is `(p_0 + p_1)/2 = (+1, 0, 0)`,
and the midpoint of edge 2-3 is `(p_2 + p_3)/2 = (−1, 0, 0)`. The
axis through these midpoints is the x-axis. A 180° rotation about
x-axis: `(x, y, z) → (x, −y, −z)`. Applied to `p_0 = (+1,+1,+1)`:
gives `(+1, −1, −1) = p_1`. So `p_0 ↔ p_1` ✓. Similarly `p_2 ↔ p_3`. ✓

### §3.4 Total

1 (identity) + 8 (vertex) + 3 (edge) = **12 elements** = |A_4|.

All permutations are EVEN (3-cycles and double-2-cycles are both even).
This is the alternating group `A_4`.

## §4 The K4 rotation group is faithfully `T = A_4`

The 12 explicit permutations above are all distinct and form a closed
group under composition. They map bijectively onto the 12 even
permutations of {0,1,2,3} (which is `A_4`). The action of 3D rotations
on the K4 tetrahedral port basis is therefore a **faithful
representation** of the tetrahedral rotation group.

**Falsification check passed.** K4 has tetrahedral rotation symmetry
exactly as claimed. The action is `T = A_4`.

## §5 Beyond pure rotations — the bipartite A↔B action

The K4 diamond lattice is BIPARTITE with sublattices A and B. Under
the rotations of `T = A_4`, A-sites map to A-sites and B-sites map to
B-sites (the rotation preserves the bipartite structure when applied
about a vertex of the bipartite cell).

However, AVE Cosserat constitutive relations involve REFLECTIONS that
swap A ↔ B. These are in `T_d \ T` (the elements of the full
tetrahedral group not in the rotation subgroup). Specifically, the
4 mirror planes (containing one vertex axis and one edge axis) exchange
A ↔ B by swapping vertex pairs.

**Implication for Step 2:** if we restrict to rotations only (`T = A_4`),
A and B sublattices are preserved separately. To get an A↔B SWAP
(needed for the bipartite-spinor argument), we need to include
reflections (full `T_d = S_4`) or some other physical mechanism.

**This complicates the bipartite-spinor argument.** Step 2 must address:
either (a) extend the symmetry group to T_d to include A↔B swaps, or
(b) identify a different mechanism by which 2π rotation produces a
non-trivial bipartite action.

## §6 The double cover `2T` of `T = A_4`

The double cover of `A_4` is the binary tetrahedral group `2T`,
order 24. This sits inside SU(2) as a discrete subgroup.

The exact sequence:
```
1 → ℤ_2 → 2T → A_4 → 1
```

For each element of `A_4`, there are two preimages in `2T` differing
by the central element `−I ∈ SU(2)`.

The central element `−I` corresponds to a 2π rotation in SO(3)
lifted to SU(2): a 2π rotation gives `−I`, only 4π gives `+I`.

**For Step 2:** if physical fields on the K4 lattice transform under
`2T` (not just `T`), then a 2π rotation gives sign flip on the field.
This IS spin-½ behavior, derived from K4 geometry without importing
SU(2) from QM.

**The load-bearing question for Step 2:** under what physical condition
do K4 fields transform under `2T` rather than just `T`?

Two candidate arguments:

**(a) Relativistic coupling.** Standard QFT: the Dirac equation forces
spinor fields under SO(3,1) double-cover. AVE's relativistic structure
comes from Cosserat dynamics — does Cosserat naturally produce spinor
fields, or only vector fields?

**(b) Bipartite phase-tracking.** The A/B sublattice labels can be
encoded as a binary state per site. If the field has a phase that
tracks bipartite alternation under rotation, then a rotation that
swaps A↔B (i.e., a reflection in T_d) produces a sign flip via the
2T action. But under pure rotations (T = A_4 only, A↔A and B↔B),
no obvious sign flip mechanism.

This is the unresolved question. Step 2 will tackle it head-on.

## §7 Summary

- The K4 rotation group is `T = A_4`, order 12. **Faithful representation
  on the 4 ports verified.**
- The full symmetry group with reflections is `T_d = S_4`, order 24.
  Reflections swap A↔B sublattices.
- The double cover of `T = A_4` is `2T`, order 24, a subgroup of SU(2).
  In `2T`, a 2π rotation gives `−I`; 4π gives `+I`.
- **For spin-½ to be DERIVED from K4 (not imported from QM), physical
  fields on the K4 lattice must transform under `2T` rather than `T`.**
  This requires a physical argument that Step 2 must provide.
- The bipartite A↔B swap is in the FULL symmetry group `T_d`, not just
  rotations `T`. The mechanism by which a pure 2π rotation in 3D
  produces a sign flip on K4 fields is the load-bearing claim for Step 2.

## §8 Falsification status

Step 1 PASSES its falsification criterion. The K4 lattice has the
tetrahedral rotation symmetry `T = A_4` faithfully. **The framework
for Step 2 is in place.**

The risk identified for Step 2: under pure SO(3) rotations, K4 has
`A_4` symmetry without an obvious mechanism for sign flip at 2π. The
double cover `2T` exists mathematically; whether it physically acts
on K4 fields is the open question.

## §9 What this derivation does NOT yet prove

- That spin-½ is derived from K4 (Step 2's job)
- That bipartite A↔B alternation gives a 2π → −I sign flip (Step 2's job)
- That the (2,3) torus knot is the natural electron topology on K4 (Step 4's job)

## §10 Files referenced

- [`src/ave/core/k4_tlm.py:80-86`](../../src/ave/core/k4_tlm.py#L80) — port vector definitions
- Standard group theory: tetrahedral group `T = A_4` (e.g., Hall, *The Theory of Groups*, Ch 12)
- Standard SU(2) representation theory: binary tetrahedral group `2T` as discrete SU(2) subgroup
