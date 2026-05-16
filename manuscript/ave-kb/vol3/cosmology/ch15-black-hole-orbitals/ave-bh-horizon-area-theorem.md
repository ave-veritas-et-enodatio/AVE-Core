[↑ Ch.15 Black Hole Orbitals](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from common/universal-saturation-kernel + vol3/condensed-matter/ch11 as canonical AVE area theorem + r_sat -->

# AVE BH Horizon: $r_{\text{sat}} = 7GM/c^2$ + Area Theorem $\delta A \geq 0$ from Ax 1 + Ax 4

Axiom-first derivation of the AVE-native BH horizon. **$r_{\text{sat}} = 7GM/c^2 = 3.5 \cdot r_s$** — AVE predicts a horizon at 3.5× the standard Schwarzschild radius (factor of 7 from Poisson-ratio Ax 2 + Ax 3 projection vs. standard GR's factor of 2). The **area theorem $\delta A \geq 0$ follows directly from Axiom 4** (saturation boundary at $r \propto M$) plus mass-energy conservation. Stronger than Hawking's 1971 area theorem: AVE's version is tied specifically to the Axiom 4 saturation boundary, not a generic "event horizon" concept. **It derives WHY the horizon can only grow** (Ax 4's saturation threshold depends linearly on embedded mass).

## Key Results

| Result | Statement |
|---|---|
| **AVE saturation-boundary radius** | $\boxed{r_{\text{sat}} = 7 G M / c^2 = 3.5 \cdot r_s}$ |
| Strain at horizon | $\varepsilon_{11}(r_{\text{sat}}) = 7 G M / (c^2 r_{\text{sat}}) = 1$ |
| Horizon area | $A = 4\pi r_{\text{sat}}^2 = 4\pi (7 G M / c^2)^2 = 196 \pi G^2 M^2 / c^4$ |
| Area theorem | $\delta A = 392 \pi G^2 M \delta M / c^4 \geq 0$ for $\delta M \geq 0$ |
| Origin of factor 7 | $7 = 1/\nu_{\text{vac}} = 1/(2/7)$ Poisson ratio (Ax 2 + Ax 3 projection) |
| Vs. standard Schwarzschild | $r_s = 2 G M / c^2$ → $r_{\text{sat}} / r_s = 3.5$ |
| Falsifiable prediction | Any high-gravity observational test of BH horizon radius can distinguish AVE ($3.5 r_s$) from standard GR ($r_s$) |
| Stronger than 1971 theorem | AVE derives **why** horizon can only grow (Axiom 4 threshold depends linearly on $M$); Hawking's theorem assumes "horizon" generically |

## §1 — The $r_{\text{sat}} = 7 G M / c^2$ derivation

Per Vol 3 Ch 21 + Vol 3 Ch 15:21-56: the horizon of a Schwarzschild BH is at $r_{\text{sat}}$, the **saturation boundary where Axiom 4's strain $\varepsilon_{11}(r)$ reaches 1**:

$$\varepsilon_{11}(r_{\text{sat}}) = \frac{7 G M}{c^2 r_{\text{sat}}} = 1$$

Solving:

$$\boxed{\, r_{\text{sat}} = \frac{7 G M}{c^2} \,}$$

**The factor 7 = $1/\nu_{\text{vac}} = 1/(2/7)$** appears from Poisson ratio Ax 2 + Ax 3 projection. The Poisson ratio of the K4 substrate is $\nu_{\text{vac}} = 2/7$ (Vol 3 Ch 15:291-355 Buchdahl bound derivation), giving the strain conversion $\varepsilon_{11} = (1/\nu) \cdot \text{strain ratio} = 7 \cdot G M / (c^2 r)$.

This is **stricter than standard GR's Buchdahl bound** (which uses $\nu = 1/2$ for incompressible matter). AVE predicts $r_{\text{sat}} = 3.5 \cdot r_s$ — a **falsifiable prediction** for any high-gravity observational test.

## §2 — Area theorem $\delta A \geq 0$ derivation

For a spherical horizon:

$$A = 4\pi r_{\text{sat}}^2 = 4\pi \cdot (7 G M / c^2)^2 = 196 \pi G^2 M^2 / c^4$$

Absorbing $\delta M$:

$$\delta r_{\text{sat}} = 7 G \delta M / c^2 > 0 \text{ if } \delta M > 0$$

$$\delta A = 8\pi r_{\text{sat}} \delta r_{\text{sat}} = 8\pi \cdot (7 G M / c^2) \cdot (7 G \delta M / c^2) = 392 \pi G^2 M \delta M / c^4 > 0$$

**The area theorem $\delta A \geq 0$ follows directly from Axiom 4 (saturation boundary at $r \propto M$) plus mass-energy conservation.**

## §3 — Why this is stronger than Hawking's 1971 theorem

Hawking's classical area theorem (1971) assumes:
1. A causally connected "event horizon" exists
2. The horizon is the boundary of a black hole region defined teleologically (the future event horizon)
3. Energy conditions hold (null energy condition for matter)

It then proves $\delta A \geq 0$ via generic-horizon geometric arguments.

**AVE's version is structurally different and stronger:**
1. The horizon is **physically located** at $r_{\text{sat}}$ where $\varepsilon_{11}(r) = 1$ — a substrate-saturation condition, NOT a teleological event-horizon definition
2. **No appeal to energy conditions** — the area theorem follows from substrate kinematics ($r_{\text{sat}} \propto M$) + mass-energy conservation
3. **Derives WHY the horizon can only grow**: Axiom 4's saturation threshold depends linearly on embedded mass; absorbing matter increases $M$, which increases $r_{\text{sat}}$, which increases $A$

The AVE framework also **derives the prefactor** ($196 \pi G^2 / c^4$ vs. standard $16 \pi G^2 / c^4$, factor of 12.25 difference) — the standard GR value is recovered only if Poisson ratio is taken as $\nu = 1/2$ instead of AVE's $\nu_{\text{vac}} = 2/7$.

## §4 — Mass-energy conservation ($dE = dM \cdot c^2$ derivation)

Per Vol 1 Ch 1:40-50 (topo-kinematic identity) and `src/scripts/vol_2_subatomic/higgs_impedance_mapping.py:48-52` ("Mass IS inductive resistance"): mass is the inductance of a confined topological structure. Inductance stores energy at rate $\tfrac{1}{2} L I^2$ where $I \sim c$ is the wave speed.

**So mass IS energy divided by $c^2$**; $dE = dM \cdot c^2$ is a definitional identity derived from Axiom 2 + Lenz BEMF identification of mass as inductive resistance. Not disputed in any AVE framing.

## §5 — Falsifiable prediction

The AVE prediction $r_{\text{sat}} = 3.5 \cdot r_s$ is **directly testable** via:

1. **Photon-ring measurements** at high-mass BHs (Event Horizon Telescope class observations) — the photon ring radius scales differently for $r_s$ vs $r_{\text{sat}}$
2. **Innermost stable circular orbit (ISCO)** at $r_{\text{ISCO}} = 6 G M / c^2$ for Schwarzschild — AVE predicts shifted ISCO due to modified horizon geometry
3. **Gravitational wave ringdown frequencies** — AVE's $\omega_R M_g = 18/49 = 0.3673$ matches GR's $0.3737$ to 1.7%; 10-18% agreement with three LIGO events (GW150914, GW170104, GW151226), per [Universal Saturation-Kernel Catalog](../../../common/universal-saturation-kernel-catalog.md)
4. **BH shadow vs. horizon ratio** in radio interferometry — different for $r_s$ vs $r_{\text{sat}}$

If high-precision measurements at BH horizons rule out $r_{\text{sat}} = 3.5 r_s$ and confirm $r_s$, AVE's Buchdahl-bound derivation requires revision.

## §6 — Implications for first-law thermodynamics

The area theorem + mass-energy conservation are TWO of the three pillars of BH thermodynamics. The third — $T \cdot dS = dE$ — has its own derivation in AVE (see [Four-Entropy Distinction](../../condensed-matter/ch11-thermodynamics/four-entropy-distinction.md) leaf) which reveals that **first-law-style $T \cdot dS = dE$ requires importing standard equipartition** that AVE rejects. The area theorem and mass-energy parts are axiom-derived; entropy-temperature relation is partial (3 of 4 entropy types coexist; only one matches standard BH formula numerically, but via imported Boltzmann counting).

This leaf focuses on the axiom-derived pillars (area + mass-energy); the entropy adjudication lives in the four-entropy leaf.

## Cross-references

- **Canonical manuscript:**
  - Vol 3 Ch 21 (BH interior, Regime IV) — saturation-boundary horizon definition
  - Vol 3 Ch 15:21-56 — $r_{\text{sat}}$ derivation from $\varepsilon_{11}(r) = 1$
  - Vol 3 Ch 15:291-355 — Buchdahl bound + Poisson ratio $\nu_{\text{vac}} = 2/7$ derivation
  - Vol 1 Ch 1:40-50 — topo-kinematic identity → $dE = dM c^2$
  - `src/scripts/vol_2_subatomic/higgs_impedance_mapping.py:48-52` — "Mass IS inductive resistance"
- **KB cross-cutting:**
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — BH event horizon + BH merger ring-down rows (saturation kernel applied at BH scale)
  - [Four-Entropy Distinction at BH Horizon](../../condensed-matter/ch11-thermodynamics/four-entropy-distinction.md) — entropy adjudication for the BH first-law
  - [Discrete-Lattice $\hat S$ at BH Horizon](../../condensed-matter/ch11-thermodynamics/discrete-lattice-entropy-constant.md) — Flag 62-G closure: ~8.7 $k_B$ per cell universal constant under symmetric saturation
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — BH horizon as canonical $\Gamma = -1$ saturation surface (M, Q, J no-hair theorem)
