[↑ Ch.1 Gravity and Yield](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-3zz0f6, clm-rd9cjm]
path-stable: "referenced from kb/claim-quality.md \"α Invariance Under Symmetric Gravity\" entry and from vol3/claim-quality.md \"Refractive Index of Gravity\" entry"
-->

---

## Derived Consequence 2: Temporal vs. Spatial Lattice Compression
<!-- claim-quality: clm-rd9cjm (canonical refractive-index decomposition $n_{temporal}, n_{spatial}$ as functions of $\varepsilon_{11} = 7GM/(c^2 r)$) -->

The principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses the lattice asymmetrically. The refractive index decomposes into:

$$
\begin{align}
    n_{temporal} &= 1 + \tfrac{2}{7}\,\varepsilon_{11} && (\text{bulk/coordinate-time propagation index, slope 2}) \\
    n_{spatial} &= 1 + \tfrac{9}{7}\,\varepsilon_{11} && (\text{controls matter-wave parallax, C11})
\end{align}
$$

<!-- claim-quality: clm-3zz0f6 (the gravitational potential entering the α-invariance derivation acts via this temporal component; the symmetric scaling of $\mu, \varepsilon$ that yields $\Delta\alpha/\alpha = 0$ is built on this decomposition) -->
$n_{temporal}$ (slope 2) is the **bulk/coordinate-time** temporal propagation index — what a signal *traversing* the gradient accumulates (Shapiro-class integrated delay, $\approx 1/g_{00}$). It is **distinct** from the **local clock rate / gravitational redshift**, which is a slope-1 quantity: the proper tick of a clock *sitting* at $r$ is $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/(c^2 r)$, giving redshift $z \approx GM/(c^2 r)$. The two are bridged by $z = (n_{temporal} - 1)/2$ — a propagating signal picks up $2\times$ the local clock effect. The spatial component governs the electron matter-wave (de Broglie) parallax measured by **C11-MACH-ZEHNDER** ($\Delta n = n_{spatial} - n_{temporal} = \varepsilon_{11}$, ~250 rad on a 1-m baseline) and frame dragging.

> **W1 walk-back (2026-06-05, Class-C internal-coherence; basis: `research/2026-06-05_gravity-ppn-coherence-result.md`).** The "$n_{spatial}$ controls light deflection" attribution was an outlier and is corrected here: light deflection couples to the **(2/7) transverse Cosserat-shear index** $n_\perp = 1 + (2/7)\chi_{vol}$ (Ch 2 §double_deflection → $4GM/bc^2$ = the observed 1.75″), NOT to $n_{spatial}$. Reading $n_{spatial}$ as the photon index gives $18GM/bc^2$ (4.5× GR). The (9/7) index is **kept** — it is load-bearing for the C11 electron matter-wave parallax (live-fire 249.64 rad). KEEP-BOTH: only the "light deflection" attribution is corrected, not the (9/7) value or its C11 role.

> **W2 walk-back (2026-06-05, Class-C internal-coherence; Grant bulk-vs-local adjudication; basis: `research/2026-06-05_gravity-sign-frequency-modulation-result.md`).** The "controls clock rate, redshift" annotation on $n_{temporal}$ conflated **two distinct temporal quantities**. $n_{temporal} = 1 + (2/7)\varepsilon_{11}$ has slope 2 ($= 1 + 2GM/rc^2 \approx 1/g_{00}$) and is the **bulk / coordinate-time propagation index** — the integrated index a signal *traversing* the gradient accumulates (Shapiro). The genuine **local clock rate / gravitational redshift** is a slope-1 quantity: $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/rc^2$, so $z = GM/rc^2$ (the $c_{shear}$ clock — what a clock *sitting* at $r$ ticks). **Bridge: $z = (n_{temporal} - 1)/2$** (a propagating signal picks up $2\times$ the local clock effect). RELABEL ONLY: the $n_{temporal}$ value ($2/7\,\varepsilon_{11}$) and every derivation are **unchanged**; only the "clock rate, redshift" label is disambiguated — the slope-2 index (bulk/propagation) vs the slope-1 local clock/redshift. KEEP-BOTH.

> **Source:** `manuscript/common_equations/eq_gravity_derived.tex` (lattice decomposition; gravity content relocated here from `eq_axiom_3.tex` per the 2026-04-27 axiom homologation). Both $n_{temporal}$ and $n_{spatial}$ carry the leading "$1+$" DC unit so each reduces to $n=1$ in flat vacuum and $\Delta n = n_{spatial} - n_{temporal} = \varepsilon_{11}$.

---
