[↑ Ch.2: Macroscopic Moduli](./index.md)
<!-- leaf: verbatim -->

# A-029 Secondary Scale: Geometric Shared-B-Node Distance

The K4 substrate's **secondary scale** $r_{\text{secondary}} \approx 1.187\,\ell_{\text{node}}$ is **not a free calibration parameter** — it is the geometric next-nearest-neighbor distance in the K4 lattice, set by the shared-B-node propagator structure. The over-bracing parameter $u_0^*$ that controls the magic-angle condition $K(u_0^*) = 2G(u_0^*)$ sits exactly at this distance.

Per Grant adjudication 2026-05-15 evening ("springs are shared, how else would gravity project?"), this resolves decades of ambiguity about whether the secondary scale was a calibration input or a substrate-symmetry consequence. It is the latter.

## The geometric derivation

The K4 lattice's bipartite structure has two sublattices (A and B). Each A-node is connected to 4 B-nodes (the K4 graph topology); each B-node is connected to 4 A-nodes. The **next-nearest-neighbor distance** between two A-nodes is set by the shortest path through a shared B-node:

$$r_{\text{secondary}} = \sqrt[3]{\mathcal{R}_{\text{OB}}} \cdot \ell_{\text{node}}$$

where $\mathcal{R}_{\text{OB}} = p_{\text{Delaunay}} / p_c = 0.3068 / 0.1834 \approx 1.673$ is the over-bracing ratio (sparse K4 packing vs dense Delaunay triangulation). This gives:

$$r_{\text{secondary}} \approx 1.187 \cdot \ell_{\text{node}}$$

**Not a calibration choice.** The number 1.187 is the geometric consequence of:
1. K4 graph topology (4-neighbor connectivity) — Axiom 1
2. Vacuum packing fraction $p_c = 8\pi\alpha \approx 0.1834$ — derived from $K=2G$ trace-reversal identity (Axiom 4 + EMT)
3. Dense Delaunay reference packing $p_{\text{Delaunay}} \approx 0.3068$ — standard amorphous-network result

## Why this matters: grounding gravity projection

The over-bracing parameter $u_0$ measures bond strain at the secondary-scale midpoint. The magic-angle equation:

$$K(u_0^*) = 2 G(u_0^*) \quad \text{at} \quad u_0^* \approx 0.187$$

forces the K4 lattice's bulk modulus equal to twice its shear modulus — the trace-reversal identity required by General Relativity for transverse-traceless gravitational-wave propagation. The over-bracing parameter $u_0$ at exactly this magic value puts the bond's midpoint at the saturation point $A = 1$ — the **substrate-scale instance of A-034** (Universal Saturation-Kernel Strain-Snap Mechanism applied at the K4 cell scale).

**Grant's framing:** "springs are shared, how else would gravity project?" The shared-B-node propagator is what makes gravity a non-local-but-causal effect in the K4 lattice — the impedance at one A-node affects all A-nodes reachable via shared-B-nodes (the secondary-scale neighborhood). Without shared-B-node propagation, there would be no mechanism for the substrate to project a coherent gravity response across distances $> \ell_{\text{node}}$.

This is the substrate-scale origin of the **K=2G operating point**, which is what makes the substrate a trace-reversed Chiral LC Network supporting transverse-traceless EM and GR waves (canonical in [Vol 1 Ch 2 (Macroscopic Moduli)](../../../../vol_1_foundations/chapters/02_macroscopic_moduli.tex)).

## Connection to |T| = 12 universality

The shared-B-node propagator is the **first** of the four independent routes to $|T| = 12$ — the proper tetrahedral rotation group order — converging on K4 path-count multiplicity:

- 4 B-neighbors per A-node
- × 3 other-A sublattices reachable via shared B-node
- = **12 secondary paths per node**

See [|T|=12 Universality (4 Routes)](../ch1-fundamental-axioms/tetrahedral-t-universality.md) for the full four-route convergence framework. A-029 is the foundational geometric scaffold underlying $|T| = 12$ route #1.

## Status

**Canonical** per Grant adjudication 2026-05-15 evening. The geometric derivation is straightforward from K4 graph + EMT packing fraction; the load-bearing claim is that **the number 1.187 is not free** — it is forced by Axiom 1 + Axiom 4 + standard amorphous-network packing geometry. Canonical manuscript source: [Vol 1 Ch 2 (Macroscopic Moduli)](../../../../vol_1_foundations/chapters/02_macroscopic_moduli.tex).

## Cross-references

- **Canonical manuscript anchors:**
  - [Vol 1 Ch 2 (Macroscopic Moduli)](../../../../vol_1_foundations/chapters/02_macroscopic_moduli.tex) — `r_{secondary} ≈ 1.187 ℓ_node`, over-bracing factor, $K=2G$ magic-angle
  - [Vol 1 Ch 1 (Four Axioms)](../../../../vol_1_foundations/chapters/01_fundamental_axioms.tex) — Axiom 1 K4 graph topology
- **Related KB leafs:**
  - [|T|=12 Universality (4 Routes)](../ch1-fundamental-axioms/tetrahedral-t-universality.md) — A-029 is route #1
  - [Common: Q-G47 Substrate-Scale Cosserat Closure](../../../common/q-g47-substrate-scale-cosserat-closure.md) — magic-angle equation at $u_0^* \approx 0.187$
  - [Continuous-Springs Reframing](./continuous-springs-reframing.md) — shared-B-node propagator is a property of the underlying continuous Cosserat field, sampled at the K4 Nyquist scale
  - [Dielectric Snap Limit](./dielectric-snap-limit.md) — over-bracing factor canonical
