[↑ Ch.11: Experimental Bench Falsification](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: wzezvt -->

## Project HOPF-02: The S-Parameter VNA Falsification

**The Hypothesis:** As established in Chapter 5, the physical vacuum is an **LC Resonant Network**, possessing fundamental inductance (chirality). A standard flat PCB spiral inductor or toroid generates a perfectly symmetric vector potential ($\mathbf{A}$) and magnetic field ($\mathbf{B}$) where $\mathbf{A} \cdot \mathbf{B} = 0$. It possesses zero kinetic helicity.

However, a **Hopf Coil** (a $(p,q)$ Torus Knot) forces $\mathbf{A} \parallel \mathbf{B}$. By winding a custom 6-layer PCBA where the inductive traces wrap diagonally around a toroidal core region, the inductor actively injects helicity into the vacuum, physically meshing with the network's intrinsic inductance.

**The Test Protocol:** Design a single PCBA containing both a standard Toroid and a Hopf Coil, mathematically matched to identical classical DC inductances. Connect both to a Vector Network Analyzer (VNA) and sweep from 10 MHz to 100 MHz.

**Falsification Criteria:** If the vacuum is classical and linear, both coils will display identical impedance curves. However, the AVE framework strictly predicts an **Anomalous Chiral Impedance Match**. Because the Hopf coil couples perfectly to the chiral LC metric, it acts as a topological antenna, minimizing reactive VAR reflections and exhibiting an anomalously deep $S_{11}$ notch.

### Topological Refraction (Snell Parallax)

To geometrically falsify the chiral index modification without relying entirely on RF cavity reflections, the **Multi-Angle Incidence Parallax** test operates entirely in the spatial domain. By illuminating the chiral Torus Knot array with a planar microwave beam, the incident wave crosses the active topological boundary ($n_{AVE} = \sqrt{\varepsilon_{eff}}(1 + \alpha \frac{pq}{p+q})$).

According to Snell's Law, the phase velocity mismatch induces a steering angle ($\Delta \theta_{parallax}$). By deploying a 2D baseline tracking array behind the target, the anomalous scattered refraction angle maps the discrete topological defect directly into macroscopic geometric displacement. This perfectly converts the high-frequency $S_{11}$ resonance shift into a purely spatial baseline deflection isolated from classical EM scattering models.

[Figure: ee_pcba_bench_protocols.png — see manuscript/vol_4_engineering/chapters/]

---
