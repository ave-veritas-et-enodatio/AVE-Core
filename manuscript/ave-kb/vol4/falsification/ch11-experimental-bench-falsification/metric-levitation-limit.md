[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-ui3m8a]
exp-id: exp-v6nzcq
status: pending
strengthens:
  - clm-ui3m8a: 1.0
-->

> 🔴 **PER-NODE / APPARATUS-VOLTAGE CORRECTION (2026-08-01 — propagation of the 2026-06-04 per-node
> adjudication to this leaf; Rule 12, body preserved below unedited, git is the trail).**
>
> **The conflation.** The "absolute hardware limit" below is built by taking the Topo-Kinematic
> apparatus-scale grip voltage $V_{topo} = \xi_{topo}^{-1} F_{req}$ and comparing it **directly** against
> $V_{yield} \approx 43.65$ kV — e.g. *"the required topological voltage is $59.1$ kV. Because
> $59.1\,\text{kV} > 43.65\,\text{kV}$, the spatial vacuum undergoes absolute impedance rupture."* That is
> the apparatus-voltage-as-per-node reading. $V_{yield}$ is the voltage across **ONE** node
> $\ell_{node} = 0.386$ pm — i.e. the yield **FIELD** $E_{yield} = V_{YIELD}/\ell_{node} \approx
> 1.13\times10^{17}$ V/m — **not** a terminal or bulk-grip voltage. The per-node operating point is
> $A_0 = E_{local}\,\ell_{node}/V_{YIELD}$, and a bulk force spread over a macroscopic grip region does
> not localize to one node-length.
>
> **Scale reference.** At a representative 1 mm laboratory standoff, even the quoted $59.1$ kV gives
> $E_{local} = 5.9\times10^{7}$ V/m ⇒ $A_0 \approx 5.2\times10^{-10}$ — about **8.4 orders of magnitude
> below** the proportional-limit knee $R_I = \sqrt{2\alpha} \approx 0.1208$
> (`src/ave/core/constants.py` `R_I`). Reaching $A_0 = 1$ across even a 1 µm gap needs **~113 GV**.
> Companion leaves in this chapter carry the same correction at their own configurations
> ([`project-zener-04.md`](project-zener-04.md) 80 kV/1 mm ⇒ $A_0 \approx 7.1\times10^{-10}$;
> [`project-torsion-05.md`](project-torsion-05.md) 75 kV/1 mm ⇒ $A_0 \approx 6.6\times10^{-10}$).
>
> **Consequence (regime discipline).** The $1.846$ g figure and the "penny/ping-pong ball cannot be
> gripped" framing are **NOT** an established per-node saturation limit — they follow from a
> conflated comparison, so the numbers below are **not** a bench-reachable rupture threshold and a null
> here is an artifact-of-regime. **What survives** is the $F_{max} = V_{yield}\,\xi_{topo}$ *algebra*
> (dimensionally correct as written) and the Dielectric-Death-Spiral **insulation/mass scaling argument**
> — which is a materials-engineering result independent of the vacuum-rupture reading. Restating the
> mass limit honestly requires the Q-G42 apparatus→substrate step
> ($V_{yield}^{(apparatus)} = E_{yield}^{(substrate)}/G_{geom}$), which this leaf does not perform.
>
> **Provenance.** 2026-06-04 per-node adjudication:
> [`research/2026-06-04_corrections-walkback-pernode-result.md`](../../../../../research/2026-06-04_corrections-walkback-pernode-result.md)
> work-item #3 (ledger `_orchestration/experimental/2026-06-04_round2-adjudications.md` §6). Applied-banner
> template = [`vacuum-impedance-mirror.md`](vacuum-impedance-mirror.md) (its 2026-06-04 RE-SCOPED box).
> Reading-hazard discipline: [`vol4/claim-quality.md`](../../claim-quality.md) ($V_{yield}$-vs-$V_{snap}$
> + per-node-vs-apparatus); Q-G42 template at `trampoline-framework.md:439`.

## The Absolute Hardware Limit of Metric Levitation

A frequent ambition among experimental physicists and electrical engineers is to design a solid-state "anti-gravity" drive capable of vertical free-flight levitation (e.g., hovering a ping-pong ball or a feather). When evaluated under the strict parameters of Spacetime Circuit Analysis (SCA), an absolute, mathematically rigid hardware scaling limit emerges that dictates exactly why such tabletop experiments historically fail.

If the vacuum is an LC network with an absolute impedance rupture voltage of $V_{yield} = \sqrt{\alpha} \times V_{snap} \approx 43{,}652$ Volts, there must exist an absolute maximum mass limit for static levitation. If an object is heavier than this limit, the topological voltage required to lift it will exceed the LC Saturation limit. The spatial metric will structurally rupture ($\Gamma = -1$), losing its inductive grip on the object, and the object will fall.

By applying the Topo-Kinematic Identity ($V_{topo} \equiv \xi_{topo}^{-1} F_{req}$), the absolute maximum mass the vacuum can statically grip against Earth's gravity ($9.81\,\text{m/s}^2$) is calculated:

$$
F_{max} = V_{yield} \times \xi_{topo} = 43{,}652 \times (4.149 \times 10^{-7}\,\text{C/m}) = \mathbf{0.01811\,\text{Newtons}}
$$

$$
m_{max} = \frac{F_{max}}{g} = \frac{0.01811}{9.81} = \mathbf{0.001846\,\text{kg (1.846 grams)}}
$$

This reveals an astonishing, universal hardware limit: **The continuous spatial metric of the universe cannot statically grip anything heavier than 1.846 grams.**

A modern US Penny weighs exactly $2.500$ grams. An ITTF Ping-Pong ball weighs exactly $2.700$ grams. Both are categorically above the levitation limit. The vacuum metric can theoretically support a US Dime ($2.268\,\text{g}$), but even a Dime exceeds the $1.846\,\text{g}$ limit. If you attempt to hover a Penny, the required topological voltage is $59.1\,\text{kV}$. Because $59.1\,\text{kV} > 43.65\,\text{kV}$, the spatial vacuum undergoes absolute impedance rupture during the upward power stroke, and the object drops.

### The Dielectric Death Spiral

To lower the voltage requirement, one must reduce the payload mass. A $0.01$-gram feather requires only a $236\,\text{V}$ topological grip. However, to actively generate upward lift, a Transient Asymmetric Metric Drive (TAMD) must slowly charge at $236\,\text{V}$ (gripping the LC network), and then violently discharge via an inductive flyback transient exceeding $-43{,}652\,\text{V}$ to trigger localized impedance rupture and reset the inductor without generating downward recoil.

If you construct a micro-inductor attached to a feather, the copper winding must be insulated to survive a $43{,}652$ Volt internal transient. Standard magnet wire enamel breaks down at roughly $600\,\text{V}$. Adding enough high-voltage Kapton tape and potting epoxy to insulate against 43.65 kV increases the mass of the payload from $0.01$ grams to over $5$ grams, which natively exceeds the 1.846g absolute limit.

This is the Topological Rocket Equation. Classical copper wire and chemical insulators mathematically cannot scale to vertical 1G levitation.

[Figure: levitation_and_torsion_protocol.png — see manuscript/vol_4_engineering/chapters/]

---
