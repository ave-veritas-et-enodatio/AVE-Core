[↑ Ch.1 Topological Matter](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-8c3yhs]
path-stable: "referenced from L3 closure synthesis + vol1 ch8 + torus-knot-ladder as canonical (2,3)-uniqueness derivation; depends-on from clm-unk0bd + clm-0ktpcn wired 2026-05-25 Phase 2 sub-item 1"
-->

# $(2, 3)$ Torus-Knot Uniqueness: Why the Electron Is the Trefoil

> **Bridging role of this leaf.** This is the canonical KB home of the $(2,3)$ uniqueness derivation. Two Vol 1 claims depend on it directly: **clm-unk0bd** (Electron Body Topology — supplies the $(2,3)$ phase-space winding for the $0_1$ unknot identification) and **clm-0ktpcn** (Golden Torus α Derivation — uses $(2,3)$ in regime (b) self-avoidance and regime (c) half-cover). The Vol 1 Ch 8 α derivation declares the $(2,3)$ winding at its "Topological identity of the electron" header; the derivation of WHY $(2,3)$ (vs $(4,3)$, $(5,2)$, etc.) lives here, not there. Cross-refs wired 2026-05-25 (Phase 2 sub-item 1).

Derivation of why the electron's phase-space topology is specifically $(2, 3)$, not $(1, 1)$, $(2, 5)$, $(3, 5)$, or any other torus-knot winding. **$(2, 3)$ is uniquely the smallest non-trivial coprime torus knot**, with the lowest crossing number ($c = 3$) of any non-trivial knot. Coprimality is required for a connected single-component knot (not a link). Both windings $\geq 2$ is required for non-trivial winding in both directions. The electron, as the lightest stable lepton with non-trivial topology, **must be $(2, 3)$** — it's the only assignment consistent with "electron = lightest stable non-trivial topological soliton."

> **Note on real-space vs phase-space:** Per Vol 1 Ch 8 KB leaf (canonical 2026-05-16), the electron is the $0_1$ **unknot** in real space — the simplest closed flux-tube loop with no real-space crossings. The "$(2, 3)$ trefoil" derived in this leaf refers to the **phase-space Clifford-torus winding pattern** of the electron's bond-pair LC tank (2 windings on the d-axis, 3 windings on the q-axis), NOT a real-space trefoil knot. The trefoil lives in phase space; the soliton lives in real space.

## Key Results

| Result | Statement |
|---|---|
| $(p, q)$ torus knot phase winding | $\theta(t) = p\phi(t) + q\psi(t)$ on torus $T^2 = S^1 \times S^1$ |
| Crossing number | $c(p, q) = \min(p(q - 1), q(p - 1))$ |
| Hopf invariant (self-linking) | $Q_H = p \cdot q$ |
| Coprimality requirement | $\gcd(p, q) = 1$ for single-component knot (not multi-component link) |
| Both-windings $\geq 2$ requirement | $p, q \geq 2$ for non-trivial knot (not unknot) |
| Smallest non-trivial coprime pair | $\boxed{(2, 3)}$ — trefoil, $c = 3$ |
| Electron assignment | Forced by "lightest stable non-trivial lepton = simplest stable knot" |

## §1 — The torus-knot family on K4

A $(p, q)$ torus knot is a closed curve on a torus $T^2 = S^1 \times S^1$ that wraps $p$ times around the toroidal direction (major axis) and $q$ times around the poloidal direction (minor axis). On the K4 substrate, this corresponds to a closed flux-tube loop with phase winding:

$$\theta(t) = p \phi(t) + q \psi(t)$$

where $\phi, \psi$ are the toroidal and poloidal angles.

Topological characterization:
- **Coprimality $\gcd(p, q) = 1$**: required for the path to close as a single loop (a true KNOT, not a multi-component LINK)
- **Crossing number** $c(p, q) = \min(p(q - 1), q(p - 1))$: minimum number of self-crossings in any planar projection
- **Hopf invariant** $Q_H = p \cdot q$: linking number with itself
- **Self-linking** $\text{SL} = pq - p - q$: Seifert-framing self-link

## §2 — Enumerating low-$(p, q)$ candidates

| $(p, q)$ | $\gcd$ | $c$ | $Q_H$ | SL | Topology |
|---|---|---|---|---|---|
| $(1, 0)$ | — | 0 | 0 | — | Trivial single straight loop |
| $(1, 1)$ | 1 | 0 | 1 | $-1$ | Unknot — closed loop, no knotting |
| $(1, n)$ | 1 | 0 | $n$ | $n - 2$ | Unknot — $n = 2, 3, \ldots$ still unknot |
| $(n, 1)$ | 1 | 0 | $n$ | $n - 2$ | Unknot — same as $(1, n)$ by symmetry |
| $(2, 2)$ | 2 | 2 | 4 | 0 | Composite link, NOT a single knot |
| **$(2, 3)$** | **1** | **3** | **6** | **1** | **Trefoil — smallest non-trivial knot** |
| $(3, 2)$ | 1 | 3 | 6 | 1 | Trefoil mirror — same knot type |
| $(2, 5)$ | 1 | 5 | 10 | 3 | Cinquefoil $(2, 5)$ |
| $(3, 4)$ | 1 | 8 | 12 | 5 | $(3, 4)$ torus knot |
| $(3, 5)$ | 1 | 10 | 15 | 7 | $(3, 5)$ torus knot |
| $(3, 7)$ | 1 | 14 | 21 | 11 | $(3, 7)$ torus knot |

**$(2, 3)$ is the SMALLEST coprime pair with both windings $\geq 2$. It has the LOWEST crossing number ($c = 3$) of any non-trivial knot.**

## §3 — Why both $p, q \geq 2$ (non-trivial in both directions)

For $(1, n)$ or $(n, 1)$: one of the windings is 1, meaning the loop goes around that direction only ONCE. No self-crossings ($c = 0$). This is **topologically equivalent to the UNKNOT** — a circle.

For a NON-TRIVIAL topological structure (a true knot), we need both $p \geq 2$ AND $q \geq 2$. This is a basic knot-theoretic fact.

## §4 — Why coprime $\gcd(p, q) = 1$

If $\gcd(p, q) = d > 1$, the curve doesn't close after one cycle of the parameter $t \in [0, 2\pi)$; instead it closes after $t \in [0, 2\pi/d)$ and is a **$d$-component LINK** (multiple disjoint loops linked together).

For a **SINGLE-COMPONENT closed loop (true knot)**, $\gcd = 1$ is required. This rules out $(2, 2)$, $(3, 3)$, $(2, 4)$, $(4, 2)$, $(3, 6)$, etc.

## §5 — The smallest non-trivial coprime torus knot is $(2, 3)$

Combining §3 + §4: both windings $\geq 2$ AND coprime.

Smallest pairs:
- **$(2, 3)$**: smallest with both $\geq 2$ and coprime → **trefoil**, $c = 3$
- $(2, 5)$: next smallest (skipping $(2, 4)$ which has $\gcd = 2$) → cinquefoil, $c = 5$
- $(3, 4)$: next → $c = 8$
- $(3, 5)$: next → $c = 10$

$(2, 3)$ is **uniquely the SMALLEST and SIMPLEST non-trivial torus knot**.

## §6 — Why the electron is $(2, 3)$

The electron is the **lightest stable particle of the lepton family** (stable charged matter at rest). It's the GROUND STATE of charged fermionic matter.

In the AVE topological-soliton framework:
- Lighter particle = simpler topology = lower-energy stable bound state
- The electron = **simplest non-trivial topological knot supporting charge + spin-½ + non-trivial linking**

**The simplest non-trivial torus knot is $(2, 3)$** — this is the derived *structure* (the smallest coprime pair with both windings $\geq 2$, from basic knot theory). Assigning it to the electron follows from the identification "electron = lightest non-trivial stable lepton": the winding **STRUCTURE is derived**, but the **SELECTION** (that the electron occupies the *smallest* such knot rather than another $(p,q)$) is an **imported identification**, not substrate-forced — **PEER** (clm-8c3yhs; the honest split is §8 below, and a paths-to-derived survey is tracked at clm-8c3yhs).

This matches:
- Vol 1 Ch 8 explicit derivation of $\alpha^{-1}$ at Golden Torus geometry using $(2, 3)$ phase-space winding
- AVE-HOPF antenna predictions using $(2, 3)$ for the electron
- The crossing count $c = 3$ matching AVE-HOPF's $\delta_{CP}$ and chirality derivations for electron-like topology

## §7 — The lepton family extension

**The lepton family climbs a Cosserat-torsion ladder on fixed (2,3) topology** (per FI-13 resolution 2026-05-18 + loop-count taxonomy; see scope correction block below). The electron is (2,3) trefoil phase-winding on a single-loop (N=1) flux tube; muon and tau are the SAME (2,3) topology with additional Cosserat torsional excitation quanta (per Vol 1 Ch 5 §39 + Vol 2 Ch 6 lepton-spectrum.md):

| Lepton | Topology | Mass mechanism | Mass |
|---|---|---|---|
| Electron | $(2, 3)$ trefoil + 0 Cosserat torsion quanta | base Faddeev-Skyrme on (2,3) | $\sim 0.511$ MeV (measured) |
| Muon | $(2, 3)$ trefoil + 1 Cosserat torsion quantum | $m_\mu = m_e/(\alpha\sqrt{3/7}) \approx 107$ MeV (1.24% off PDG) — *echo/import: the mass VALUE defers to its source leaf [lepton-spectrum](../ch06-electroweak-higgs/lepton-spectrum.md) (Vol 2 Ch 6); the ~1.24% residual is a fit-echo, not a chord* | $\sim 105.66$ MeV |
| Tau | $(2, 3)$ trefoil + N_torsion=? Cosserat quanta | analogous extension; details in Vol 2 Ch 6 | $\sim 1.777$ GeV |

The exact mass-from-Cosserat-torsion derivation is in Vol 2 Ch 6 (lepton-spectrum.md). **The point**: $(2, 3)$ is the SIMPLEST non-trivial torus knot, hence the electron's identity is forced if we accept "electron = lightest stable lepton." Higher-mass leptons stay at (2,3) topology — they don't climb the (p,q) torus-knot ladder; they climb the Cosserat-torsion excitation ladder.

> **Internal-consistency flag (2026-05-17 night, Foundation Item 13 audit) — RESOLVED 2026-05-18**: The previous version of this table assigned muon = $(2, 5)$, which conflicted with the proton = $(2, 5)$ assignment in [`torus-knot-ladder.md`](torus-knot-ladder.md). Per FI-13 resolution via loop-count taxonomy (see [`topological-fractionalization.md:6`](../ch02-baryon-sector/topological-fractionalization.md:6) Borromean 3-loop baryon + lepton single-loop framing): **the muon is canonically a single-loop lepton on (2,3) trefoil + 1 Cosserat torsion quantum**, NOT a (2,5) cinquefoil. The (2,5) cinquefoil topology belongs exclusively to the proton (baryon Borromean 3-loop with per-loop (2,5) winding). The three corpus uses of "(2,5)" now disambiguate cleanly:
>
> - **(a) Muon (formerly "(2,5) q-winding")** → RETRACTED. Canonical: muon = (2,3) + Cosserat torsion. The Q-G19α "(2,5) q-winding mode" framing for the muon was an alternative-hypothesis ladder framework, now scope-corrected at [`q-g19a-petermann-saliency-closure.md:108`](../ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) FI-13 block.
> - **(b) Proton (2,5)** → CANONICAL. Cinquefoil per-loop winding on Borromean 3-loop (N=3) baryon topology. Mass via $m(c=5)$ formula in [`torus-knot-ladder-baryons.md`](../ch02-baryon-sector/torus-knot-ladder-baryons.md).
> - **(c) Neutrino c_1=5** → CANONICAL as RESONANCE LABEL. The neutrino is geometrically a 0_1 unknot screw defect (single-loop, distinct mechanism from electron lepton); the {5, 7, 9} = {c_1, c_2, c_3} mode-space radii reference the SAME (2,5), (2,7), (2,9) torus-knot resonance classes that the baryon ladder uses. The neutrino COUPLES to these resonances; it doesn't INHABIT them. c_1=5 starting value is structurally derived as "the lowest stable (2,q_odd) cinquefoil resonance above the electron (2,3) trefoil baseline".
>
> **FI-13 fully resolved. C3-MUON-DELTA matrix row UN-GATED** — Q-G27 Cosserat-torsion saliency is canonical for muon Fermilab observable; driver can build with $\delta_\mu = -3\alpha/2 - \alpha\sqrt{3/7}/(2\pi) = -0.01171$.

## §8 — What this derivation establishes

1. **$(2, 3)$ is uniquely the smallest non-trivial coprime torus knot** ($\gcd = 1$, both $\geq 2$, smallest sum $p + q = 5$)
2. **It has the lowest crossing number $c = 3$** of any non-trivial knot
3. **It's the unique trefoil topology** (trefoil is THE simplest knot in all of knot theory — first entry in Rolfsen's knot tables as $3_1$)
4. **The electron is assigned $(2, 3)$** (in phase space, per the Vol 1 Ch 8 canonical clarification) if we accept it's the lightest stable lepton with non-trivial topology — the $(2,3)$ winding **structure is derived**; the **selection** (electron = the smallest such knot) is the imported identification (clm-8c3yhs, PEER), not substrate-forced

This is a **DERIVATION from basic knot-theoretic facts** plus the identification "electron = lightest stable non-trivial topological soliton." The knot theory is standard math; the identification is the AVE physical assertion.

## §9 — Falsification status

| Test | Status |
|---|---|
| Predict $(1, 1)$, $(1, 2)$, or $(2, 2)$ as electron | **WOULD HAVE FAILED** — those are unknots or composite links, not true non-trivial knots |
| Predict $(2, 3)$ as smallest non-trivial coprime | **PASSES** — by basic knot theory, $(2, 3)$ is the unique smallest |
| Predict electron = $(2, 3)$ | **PASSES** if "electron = lightest stable non-trivial lepton" is accepted |

## Cross-references

- **Canonical manuscript:**
  - Vol 1 Ch 8 — electron $\alpha^{-1}$ derivation using $(2, 3)$ phase-space winding at Golden Torus
  - Vol 2 lepton mass spectrum chapter — $(p, q)$ → mass derivation
- **KB cross-cutting:**
  - [Vol 1 Ch 8 α Golden Torus](../../../vol1/ch8-alpha-golden-torus.md) — canonical real-space $0_1$ unknot + phase-space $(2, 3)$ trefoil distinction
  - [Torus Knot Ladder](torus-knot-ladder.md) — $(2, q)$ family for stable particles
  - [L3 Electron-Soliton Closure Synthesis](l3-electron-soliton-synthesis.md) — broader $(2, q)$ family framework
  - [Electron Unknot](electron-unknot.md) — real-space $0_1$ unknot geometry
  - [Chirality and Antimatter](chirality-and-antimatter.md) — twist direction as charge polarity
- **Canonical scripts:**
  - `AVE-HOPF/scripts/beltrami_hopf_coil.py:43-53` — `harmonic_mean_winding`, `self_linking_number`, `crossing_number_torus_knot` utilities
  - Standard knot theory reference: Murasugi, *Knot Theory and Its Applications* — torus-knot crossing number $c(p, q) = \min(p(q - 1), q(p - 1))$
