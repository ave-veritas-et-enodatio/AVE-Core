[↑ Vol 4: Engineering](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [hd9bee, u462e4, wzezvt]
-->

> ⛔ **Bootstrap.** Leaves are canonical; this index, the volume index, and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this subtopic, load [`../claim-quality.md`](../claim-quality.md) (volume scope) and [`../../claim-quality.md`](../../claim-quality.md) (cross-cutting). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Future Geometries

Chiral antenna engineering, computational electromagnetics mapped to the AVE lattice, and the K4-TLM native vacuum simulator. Ch.13 develops the high-Q chiral impedance antenna (Chiral Figure of Merit, Beltrami eigenvalue), surveys six CEM solver methods and their AVE isomorphisms, and presents the K4-TLM Diamond lattice simulator — a time-domain computational engine that implements AVE Axiom 1 directly.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Chiral Figure of Merit | $\text{FoM} = Q_u \times \alpha \frac{pq}{p+q} \times \eta_{\mathcal{H}}$ | Ch.13 |
| Beltrami eigenvalue | $\lambda(p,q) = \sqrt{p^2/R^2 + q^2/r^2}$ | Ch.13 |
| K4-TLM scattering matrix | $S^{(0)}_{ij} = \frac{1}{2} - \delta_{ij}$ (unitary to machine epsilon) | Ch.13 |
| Optimal topology | $(7,11)$ torus knot optimal across TX and RX; YBCO provides $1{,}300\times$ FoM gain over copper | Ch.13 |
| CEM $\leftrightarrow$ AVE mapping | MoM: $[Z][I]=[V]$ is lattice circuit equation; FDTD Yee grid is LC network; FEM eigenvalue is $\omega^2 LC = 1$; TLM is most direct computational isomorphism | Ch.13 |

## Derivations and Detail

| Chapter | Contents |
|---|---|
| [Ch.13: Future Geometries](ch13-future-geometries/index.md) | High-Q chiral antenna design (RX/TX), CEM methods survey with AVE mappings, K4-TLM Diamond lattice simulator, open-universe PML boundaries |

---
