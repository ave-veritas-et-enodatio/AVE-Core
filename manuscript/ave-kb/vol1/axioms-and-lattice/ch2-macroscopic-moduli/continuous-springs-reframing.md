[↑ Ch.2: Macroscopic Moduli](./index.md)
<!-- leaf: verbatim -->

# Discrete K4 Lattice as Discretization of Continuous Cosserat Field

Per Grant 2026-05-15 evening (Q-G47 Sessions 16–17): the K4 lattice's "bonds" are **not** physical springs between point-mass nodes. The substrate is a continuous Cosserat micropolar field at the axiom level; the discrete K4 representation is a *discretization* of the continuous field. $\ell_{\text{node}}$ sets the Nyquist cutoff for the continuous-stress field's spatial bandwidth.

This reframing resolves a recurring class of "discrete vs continuous" framing confusions. The substrate is continuous; K4 is the discretization sampling that continuum at the substrate's natural scale.

## What "the springs are actually continuous" means

The Vol 1 Ch 1 + Ch 2 mathematical model presents the substrate as a chiral Laves K4 Cosserat crystal — a discrete graph of nodes connected by bonds. The discrete representation is computationally tractable and pedagogically useful. But **at the axiom level**, the substrate is the underlying continuous Cosserat micropolar field; the discrete K4 picture is one particular discretization of that field, not the field itself.

Concretely:

| What the K4 picture suggests | What the substrate actually is |
|---|---|
| Point-mass nodes at lattice sites | Continuous mass-density field |
| Springs between nodes | Continuous stress-field tensor |
| Bond stiffness $k$ as fundamental input | Cosserat constitutive constants $(\mu, \kappa, \beta, \gamma)$ at axiom level |
| Discrete bond-bow geometry | Continuous strain field $\epsilon(\mathbf{r})$ |
| $\ell_{\text{node}}$ as bond length | $\ell_{\text{node}}$ as the Nyquist sampling pitch for the continuous field |

The discrete K4 picture is the substrate as it appears at the discretization scale; the continuous Cosserat field is the substrate at the axiom level.

## Why this reframing matters

### 1. Discrete-bond calculations are sanity checks, not independent regimes

Discrete-bond calculations (e.g., Q-G47 Sessions 12–15 numerical K4 scaffold; standard `K = 4 k_a + 8 k_s`-style results from spring-constant sweeps) are useful **sanity-check approximations** of the continuous-field physics, not independent regimes.

The continuous-vs-discrete mapping is established via the Cosserat-characteristic-length identification:

$$\chi_K = \left(\frac{\ell_c}{d}\right)^2$$

where $\ell_c$ is the Cosserat characteristic length (substrate-continuous quantity) and $d$ is the discrete K4 bond length (sampling spacing). For the K4 substrate, $\ell_c / \ell_{\text{node}} \approx \sqrt{6}$ (Q-G47 Session 9), giving $\chi_K \approx 6 \cdot 2 = 12$ via bilateral chiral symmetry. The same number 12 appears at four independent routes (see [|T|=12 Universality](../ch1-fundamental-axioms/tetrahedral-t-universality.md)).

### 2. The Cosserat constitutive structure is the axiom-level reality

The Cosserat micropolar constants $(\mu, \kappa, \beta, \gamma)$ are the axiom-level constitutive content. Per Q-G47 Session 17, the dimensional framework closes as:

$$\mu + \kappa = \xi_{K1} \cdot T_{EM}, \qquad \beta + \gamma = \xi_{K2} \cdot T_{EM} \cdot \ell_{\text{node}}^2$$

with $T_{EM}$ the electromagnetic string tension and $\ell_{\text{node}}$ the Nyquist sampling pitch. The ratio $\xi_{K2}/\xi_{K1} = 12$ is K4-symmetry-forced (self-consistency, independent of $T_{EM}$).

The bond-spring formulation derives FROM this continuous constitutive structure; the continuous structure does not derive from the bond-spring formulation.

### 3. $\ell_{\text{node}}$ is a sampling scale, not a fundamental graininess

The pre-reframing intuition might be: "the universe is fundamentally pixelated at scale $\ell_{\text{node}}$." The continuous-springs reframing corrects this: the substrate is continuous; $\ell_{\text{node}}$ is the Nyquist resolution at which the continuous field is sampled by the discrete K4 representation.

Physical phenomena at scales $\ll \ell_{\text{node}}$ are smoothed by the substrate's intrinsic bandwidth limit — but this is a Nyquist consequence of the substrate's mode content, not a fundamental discrete-spacetime claim. (The Generalized Uncertainty Principle emerging from finite-bandwidth bond constraints is a downstream consequence; see Vol 1 Ch 3 §quantum mechanics.)

### 4. Substrate-observability extends to the continuous interpretation

Per the substrate-observability rule ([Three Boundary Observables](../../../common/boundary-observables-m-q-j.md)), only $\Gamma$ + $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ are externally observable at any saturation boundary. This is now true at both interpretations: at the discrete K4 level (boundary as a set of saturated bonds) and at the continuous Cosserat level (boundary as a 2-manifold where $S(A) \to 0$ locally). The two are the same boundary, observed in two equivalent dialects.

## Implications for cross-volume content

When KB leafs or chapters discuss the substrate using the discrete K4 / bond / spring vocabulary, this is dialect — not a different physical picture. The continuous Cosserat description is equivalent and equally canonical. The two should be cross-referenced where load-bearing, with the continuous picture treated as the axiom-level reality and the discrete picture as the convenient sampling representation.

This reframing was load-bearing for Q-G47 Sessions 16–17 closure (continuous-field axiom-level recasting; $\xi_{K2}/\xi_{K1} = 12$ self-consistency); the Cosserat constitutive structure that emerged could not have been derived from spring-constant sweeps alone.

## Cross-references

- **Canonical manuscript anchors:**
  - [Vol 1 Ch 2 (Macroscopic Moduli)](../../../../vol_1_foundations/chapters/02_macroscopic_moduli.tex) — substrate Cosserat moduli + over-bracing framework
  - [Vol 1 Ch 1 (Four Axioms)](../../../../vol_1_foundations/chapters/01_fundamental_axioms.tex) — Axiom 1 Chiral Laves K4 Cosserat Crystal (canonical substrate-vocabulary)
- **Related KB leafs:**
  - [Common: Q-G47 Substrate-Scale Cosserat Closure](../../../common/q-g47-substrate-scale-cosserat-closure.md) — full substrate-scale closure with continuous-field reframing context
  - [|T|=12 Universality](../ch1-fundamental-axioms/tetrahedral-t-universality.md) — four independent routes; route 2 (Cosserat dimensional) explicitly uses the $\ell_c$ continuous quantity
  - [Common: xi-topo-traceability](../../../common/xi-topo-traceability.md) — $\xi_{K1}, \xi_{K2}$ at the axiom-level continuous Cosserat constitutive tensor
- **Trampoline-framework picture-first reference:**
  - [trampoline-framework.md §1.5 "Layer 4: Stress field, not just springs"](../../../common/trampoline-framework.md) — same insight in picture form
