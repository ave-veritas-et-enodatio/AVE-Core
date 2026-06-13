[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Consolidation / translation leaf (consistency-vs-emergence: CONSISTENCY, not emergence). The reflection-coefficient view of the electron wall on the Smith chart, re-expressing the magnetic-branch Gamma=-1 (clm-lv3uw1) and the alpha=1/Q per-cycle leak (clm-rtdmsn) as |Gamma|^2=1-alpha. Fills the translation-circuit.md:181 Smith-chart gap. The |Gamma|^2=1-alpha relation is the AVE-DISTINCT consequence (the wall falls short of the unit circle by exactly alpha = the radiative leak). Originates no new derivation; the chiral 2x2 S off-diagonal magnitude is STATED."
-->

# CVR Reflection on the Smith Chart — $|\Gamma|^2 = 1-\alpha$

The reflection-coefficient view of the self-trapped electron: how $\Gamma$ moves on the Smith chart as the operating point sweeps from the cold matched lattice (the free photon, $\Gamma=0$) to the saturation wall (the short, $\Gamma\to-1$), and the **AVE-distinct** result that the wall is *not a perfect short* — it falls short of the unit circle by exactly $\alpha$. This fills the gap the [circuit translation table](../../../common/translation-tables/translation-circuit.md):181 flagged for the *Smith chart ($Z\leftrightarrow\Gamma$)* row (⚠ "implied by Op1 + Op3 composition; no explicit Smith-chart leaf").

## §1 — Scope and classification

> **[Resultbox]** *Classification — consolidation / consistency, with one AVE-distinct corollary*
>
> The $\Gamma(A_0)$ locus is the Op3 reflection ([operators.md](../../../common/operators.md):43) of the
> canonical $Z_{core}=Z_0\sqrt{S}$ trajectory. The matched→short sweep is CONSISTENCY (re-expression). The
> **$|\Gamma|^2 = 1-\alpha$ relation is AVE-DISTINCT** — the radiative leak made geometric. `no-claim:`
> frontmatter; the relation is owned by the $\alpha=1/Q$ leak (clm-rtdmsn).

## §2 — The $\Gamma(A_0)$ locus (Op3 of the magnetic-branch wall)

$$
\Gamma(A_0) = \frac{Z_{core}(A_0) - Z_0}{Z_{core}(A_0) + Z_0}, \qquad Z_{core}(A_0) = Z_0\sqrt{S(A_0)}
$$

- $A_0=0$ (cold lattice): $Z_{core}=Z_0$, $\Gamma=0$ — **matched, the free photon** ([photon-ee-mapping.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §2, $\Gamma=0$ at every bond, no core).
- $A_0\to1$ (saturation): $Z_{core}\to0$, $\Gamma\to-1$ — **the short-circuit TIR wall** (magnetic branch $\mu_{eff}\to0$, [master-equation.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79, clm-lv3uw1; [resonant-lc-solitons.md](resonant-lc-solitons.md):42-46).

On the Smith chart the locus runs straight along the real axis from the centre ($\Gamma=0$) to the left rim ($\Gamma=-1$): a pure resistance collapse to the short.

## §3 — The AVE-distinct result: $|\Gamma|^2 = 1-\alpha$

> **[Resultbox]** *The wall is not a perfect short — it leaks exactly $\alpha$ per cycle*
>
> $$\boxed{\; |\Gamma|^2 = 1 - \alpha \;\approx\; 0.99270, \qquad |\Gamma| = \sqrt{1-\alpha} \approx 0.99635 \;}$$
>
> The electron's reflective boundary is a **high-but-not-perfect** short. Only a fraction $1/Q=\alpha$ of the
> stored energy leaks per cycle through the TIR boundary ([theorem-3-1-q-factor.md](theorem-3-1-q-factor.md):81),
> so the reflected power is $1-\alpha$ and $|\Gamma|$ sits just **inside** the unit circle. **The hair by which
> $\Gamma$ falls short of $|\Gamma|=1$ IS $\alpha$** — the fine-structure constant read directly off the Smith
> chart as the radiative gap to the unit circle. Equivalently, the wall sits at a residual amplitude $A_\star$
> where $\sqrt{S_\star}\approx\alpha/4$ — a tiny non-zero core impedance, not an ideal $0\,\Omega$ short.

This is the same $\alpha$ as the $H(s)$ pole's distance from the $j\omega$ axis ([cvr-transfer-function.md](cvr-transfer-function.md) §2): the radiative linewidth, the per-cycle leak, and the Smith-chart gap to the unit circle are three views of one number. Computed: `gamma_mag_sq_leak = 0.9927026 = 1-α` (`cvr_ee_sweep_metrics.json`).

## §4 — The chiral 2×2 scattering matrix (STATED — winding handedness)

A scalar electron would have a $1\times1$ $\Gamma$. The $(2,3)$ winding makes it a 2-port in the $(L,R)$ handedness basis with a **non-reciprocal** scattering matrix: $S_{LR}\ne S_{RL}^{*}$ (parity-odd). Computed non-reciprocity peaks at resonance ($|S_{LR}-S_{RL}^*|=0.53$). As with [cvr-transfer-function.md](cvr-transfer-function.md) §3, the **structure** is the AVE-distinct candidate signature; the **magnitude** is STATED (needs the chiral-crystal engine; cubic FDTD averages chirality out).

## §5 — Computed figure

![CVR reflection on the Smith chart + chiral 2x2 S](../../../../../src/scripts/vol_9_device/cvr_ee_sweep/_output/fig3_reflection_smith.png)

Re-runnable: `PYTHONPATH=$PWD/src python src/scripts/vol_9_device/cvr_ee_sweep/cvr_ee_sweep.py` (View 3). Left: the $\Gamma(A_0)$ locus matched→short with the electron wall at $|\Gamma|^2=1-\alpha$ marked just inside the unit circle. Right: the non-reciprocal off-diagonal.

## §6 — Discrimination (ave-discrimination-check)

- **CONSISTENCY:** the matched→short locus is the Op3 re-expression of $Z_{core}=Z_0\sqrt{S}$; the $\Gamma=-1$ limit is the canonical TIR wall.
- **AVE-DISTINCT:** $|\Gamma|^2=1-\alpha$ — the wall's reflectivity falls short of unity by exactly the fine-structure constant. A perfect-conductor QED boundary would give $|\Gamma|=1$ identically; the AVE wall predicts a **measurable radiative leak = $\alpha$** built into the reflection. Plus the non-reciprocal $S_{LR}\ne S_{RL}^*$ (§4).

## §7 — Honest-status flags

- **Exponent defect (carried):** the engine computes $\Gamma$ from $n=S^{0.25}$, which **understates** wall depth vs the physical $n=S^{0.5}$ ([cvr-dc-operating-point.md](cvr-dc-operating-point.md) §3, `master_equation_fdtd.py:165`). The $|\Gamma|^2=1-\alpha$ relation here is anchored to the **per-cycle leak** ($\alpha=1/Q$, clm-rtdmsn), not to the defective $n$ — so it is unaffected; but any $\Gamma$-from-$n$ magnitude on the engine side is shallow. Physics-review item.
- **Sector-attribution flag (FLAG-2):** $Z_{core}=Z_0\sqrt{S}$ is robust to the magnetic-vs-capacitive sector question ([cvr-dc-operating-point.md](cvr-dc-operating-point.md) §6); the Smith locus is convention-independent. Magnetic is PRIMARY.
- **Chiral $\chi$ magnitude STATED** (§4).

## Cross-references

- **Owning canonical claims:** [master-equation.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79 (clm-lv3uw1, magnetic $\Gamma=-1$); [theorem-3-1-q-factor.md](theorem-3-1-q-factor.md) (clm-rtdmsn, the $\alpha=1/Q$ leak); [resonant-lc-solitons.md](resonant-lc-solitons.md):42-46 (the $\Gamma=-1$ short).
- **Companion sweep views:** [Transfer Function $H(s)$](cvr-transfer-function.md) · [DC Operating Point](cvr-dc-operating-point.md) · [Phasor / Reactance](cvr-phasor-reactance.md) · [Stability / Eigenmode](cvr-stability-eigenmode.md).
- **Tool-axis:** [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):181 (Smith-chart row this leaf consolidates); [operators.md](../../../common/operators.md):43 (Op3 $\Gamma$).
- **Canonical script:** `src/scripts/vol_9_device/cvr_ee_sweep/cvr_ee_sweep.py` (+ `cvr_model.py`).

---
