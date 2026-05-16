[↑ Ch.1 Fundamental Axioms](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from spin-half-paradox + |T|=12 universality + L3 closure synthesis as canonical K4 rotation group derivation -->

# K4 Rotation Group $T = A_4$: Faithful Representation on 4-Port Basis

Step 1 derivation of the **K4 lattice's full rotation symmetry**: the action of 3D rotations on the K4 tetrahedral port basis $\{p_0, p_1, p_2, p_3\}$ is a **faithful representation of the tetrahedral rotation group $T = A_4$** (order 12). With reflections, the full symmetry is $T_d = S_4$ (order 24). The double cover of $T = A_4$ is the binary tetrahedral group $2T \subset SU(2)$, order 24 — the K4-native source of spin-½ in the AVE framework via Finkelstein–Misner mechanism. Cosserat constitutive reflections in $T_d \setminus T$ swap A↔B sublattices.

## Key Results

| Result | Statement |
|---|---|
| K4 tetrahedral port basis | $p_0 = (+1, +1, +1)$, $p_1 = (+1, -1, -1)$, $p_2 = (-1, +1, -1)$, $p_3 = (-1, -1, +1)$ |
| Magnitude | $\|p_j\| = \sqrt{3}$; pairwise dot product $p_i \cdot p_j = -1$ ($i \neq j$); tetrahedral angle $\arccos(-1/3) \approx 109.47°$ |
| Rotation group | $T = A_4$ (alternating group on 4 elements), order $\|T\| = 12$ |
| Conjugacy classes | $\{e\}$ (1) + $C_3$ (8 rotations $\pm 120°$ about 4 vertex axes) + $C_2$ (3 rotations $180°$ about 3 edge-midpoint axes) = 12 |
| Full symmetry with reflections | $T_d = S_4$ (symmetric group on 4 elements), order 24 — adds 4 mirror planes that swap A↔B |
| Double cover | $2T \subset SU(2)$, order 24; $2\pi$ rotation gives $-I$ (spin-½ characteristic) |
| Faithful representation | All 12 permutations distinct and form closed group under composition; bijective onto $A_4$ even permutations of $\{0, 1, 2, 3\}$ |

## §1 — The K4 tetrahedral port basis

From `src/ave/core/k4_tlm.py:80-86`, the K4 diamond lattice has 4 ports per node with tetrahedral connection vectors (A → B sublattice direction):

$$p_0 = (+1, +1, +1), \quad p_1 = (+1, -1, -1), \quad p_2 = (-1, +1, -1), \quad p_3 = (-1, -1, +1)$$

These four vectors:

| Property | Value |
|---|---|
| Magnitude | $\|p_j\| = \sqrt{3}$ |
| Product of components | $+1$ (even parity — three $+1$'s or one $+1$ and two $-1$'s) |
| Geometric arrangement | Regular tetrahedron inscribed in cube $[\pm 1]^3$ |
| Sum | $\sum_j p_j = (0, 0, 0)$ (centered at origin) |
| Pairwise dot product | $p_i \cdot p_j = -1$ for $i \neq j$ |
| Tetrahedral angle | $\arccos(-1/3) \approx 109.47°$ |

Verification of the dot product (e.g., $p_0 \cdot p_1 = 1 - 1 - 1 = -1$) gives the standard tetrahedral angle.

## §2 — The tetrahedral rotation group $T = A_4$

The symmetry group of a regular tetrahedron under **rotations only** is the **tetrahedral group $T$**, isomorphic to the alternating group $A_4$ (even permutations of 4 elements), order $|T| = 12$.

### Conjugacy classes

| Class | Order | Number | Description |
|---|---|---|---|
| $\{e\}$ | 1 | 1 | Identity |
| $C_3$ | 3 | 8 | Rotations by $\pm 120°$ about each of the 4 vertex axes (4 axes × 2 directions = 8) |
| $C_2$ | 2 | 3 | Rotations by $180°$ about each of the 3 face-midpoint axes |

Total: $1 + 8 + 3 = 12 = |A_4|$ ✓

The **full symmetry group $T_d$** includes reflections and has order 24, isomorphic to $S_4$. This leaf focuses on rotations only, giving $T = A_4$.

## §3 — Explicit permutations under each rotation class

### Identity

$e: p_j \to p_j$ for all $j$. Permutation = $(0)(1)(2)(3)$ = identity.

### Vertex-axis rotations ($C_3$ class, 8 elements)

A $120°$ rotation about the axis along $p_0 = (+1, +1, +1)$ cycles the other three ports in the plane perpendicular to $p_0$:

$$R_{p_0, +120°}: \, p_0 \to p_0, \, p_1 \to p_2, \, p_2 \to p_3, \, p_3 \to p_1$$

Permutation in cycle notation: $(123)$ (fixing 0).

**All 8 elements of class $C_3$:**

| Axis | Direction | Permutation |
|---|---|---|
| $p_0$ | $+120°$ | $(123)$ |
| $p_0$ | $-120°$ | $(132)$ |
| $p_1$ | $+120°$ | $(032)$ |
| $p_1$ | $-120°$ | $(023)$ |
| $p_2$ | $+120°$ | $(013)$ |
| $p_2$ | $-120°$ | $(031)$ |
| $p_3$ | $+120°$ | $(021)$ |
| $p_3$ | $-120°$ | $(012)$ |

Each is a 3-cycle (even permutation). 8 elements total.

### Edge-midpoint axis rotations ($C_2$ class, 3 elements)

A $180°$ rotation about an axis through the midpoints of two opposite edges of the tetrahedron:

| Edge pair | Axis | Permutation |
|---|---|---|
| $(01)$ & $(23)$ | through midpoints of edges 0-1 and 2-3 | $(01)(23)$ |
| $(02)$ & $(13)$ | through midpoints of edges 0-2 and 1-3 | $(02)(13)$ |
| $(03)$ & $(12)$ | through midpoints of edges 0-3 and 1-2 | $(03)(12)$ |

Each is a product of two 2-cycles (even permutation). 3 elements total.

**Verification:** the midpoint of edge 0-1 is $(p_0 + p_1)/2 = (+1, 0, 0)$, midpoint of edge 2-3 is $(p_2 + p_3)/2 = (-1, 0, 0)$. Axis through these midpoints is the $x$-axis. A $180°$ rotation about $x$-axis: $(x, y, z) \to (x, -y, -z)$. Applied to $p_0 = (+1, +1, +1)$: gives $(+1, -1, -1) = p_1$. So $p_0 \leftrightarrow p_1$ ✓. Similarly $p_2 \leftrightarrow p_3$ ✓.

### Total

$1$ (identity) $+ 8$ (vertex) $+ 3$ (edge) $= \boxed{12 \text{ elements} = |A_4|}$.

All permutations are EVEN (3-cycles and double-2-cycles are both even). This is the alternating group $A_4$.

## §4 — Faithful representation

The 12 explicit permutations above are all distinct and form a closed group under composition. They map bijectively onto the 12 even permutations of $\{0, 1, 2, 3\}$ (which is $A_4$). **The action of 3D rotations on the K4 tetrahedral port basis is therefore a faithful representation of the tetrahedral rotation group.**

**Falsification check passed.** K4 has tetrahedral rotation symmetry exactly as claimed. The action is $T = A_4$.

## §5 — Beyond pure rotations: the bipartite A↔B action

The K4 diamond lattice is **BIPARTITE** with sublattices A and B. Under the rotations of $T = A_4$, A-sites map to A-sites and B-sites map to B-sites (the rotation preserves the bipartite structure when applied about a vertex of the bipartite cell).

However, AVE Cosserat constitutive relations involve **REFLECTIONS that swap A ↔ B**. These are in $T_d \setminus T$ (the elements of the full tetrahedral group not in the rotation subgroup). Specifically, the **4 mirror planes** (containing one vertex axis and one edge axis) exchange A ↔ B by swapping vertex pairs.

**Implication:** if we restrict to rotations only ($T = A_4$), A and B sublattices are preserved separately. To get an A↔B SWAP (needed for the bipartite-spinor argument leading to spin-½), we need to include reflections (full $T_d = S_4$) or some other physical mechanism.

## §6 — The double cover $2T \subset SU(2)$

The double cover of $A_4$ is the **binary tetrahedral group $2T$**, order 24. This sits inside $SU(2)$ as a discrete subgroup.

The exact sequence:

$$1 \to \mathbb{Z}_2 \to 2T \to A_4 \to 1$$

For each element of $A_4$, there are two preimages in $2T$ differing by the central element $-I \in SU(2)$. **The central element $-I$ corresponds to a $2\pi$ rotation in SO(3) lifted to SU(2)**: a $2\pi$ rotation gives $-I$, only $4\pi$ gives $+I$.

**For spin-½ to be DERIVED from K4** (not imported from QM), physical fields on the K4 lattice must transform under $2T$ rather than $T$. This is provided by the Finkelstein–Misner mechanism on the extended $0_1$ unknot defect embedded in the SO(3) manifold — the substrate-native source of spin-½ via the $K_4 \to A_4 \to 2T \subset SU(2)$ chain.

See [spin-half-paradox](../../../vol2/appendices/app-b-paradoxes/spin-half-paradox.md) for the full spin-½ derivation chain.

## §7 — Cross-volume implications

| Claim | Source |
|---|---|
| K4 rotation group is $T = A_4$, order 12 | This leaf §4 (faithful representation verified) |
| Full symmetry with reflections is $T_d = S_4$, order 24 | §5 (reflections swap A↔B sublattices) |
| Double cover $2T \subset SU(2)$, order 24 | §6 ($2\pi$ rotation gives $-I$, $4\pi$ gives $+I$) |
| $\|T\| = 12$ universality | Four routes in [tetrahedral-t-universality](tetrahedral-t-universality.md) — coordination, Cosserat dimensional, magic-angle multiplicity, axiom-level constitutive ratio |
| Substrate-native spin-½ | Finkelstein–Misner mechanism on $0_1$ unknot in SO(3) via $K_4 \to A_4 \to 2T$ chain (Vol 1 Ch 8 §α derivation regime (c)) |

## Cross-references

- **Canonical scripts:**
  - `src/ave/core/k4_tlm.py:80-86` — port vector definitions
- **KB cross-cutting:**
  - [$\|T\| = 12$ Universality (4 Routes)](tetrahedral-t-universality.md) — four independent K4-symmetry-forced routes converging on 12
  - [Vol 1 Ch 8 α Golden Torus](../../ch8-alpha-golden-torus.md) — $K_4 \to A_4 \to 2T \subset SU(2)$ chain via Finkelstein–Misner
  - [Spin-Half Paradox](../../../vol2/appendices/app-b-paradoxes/spin-half-paradox.md) — full spin-½ derivation
  - [L3 Electron-Soliton Closure Synthesis](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) §4 — $m_{\text{Cosserat}} = 2 m_e$ from same factor 2
  - [K4 4-port Irrep Decomposition](../../operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) — $A_1 \oplus T_2$ decomposition of the same port space (representation theory of $T_d$)
- **Standard references:**
  - Hall, *The Theory of Groups*, Ch 12 — tetrahedral group $T = A_4$
  - Standard $SU(2)$ representation theory — binary tetrahedral group $2T$ as discrete $SU(2)$ subgroup
