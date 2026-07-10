[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Organizing REGISTER (routing aid), not a derivation. Consolidates the already-canonical separation of the lattice model into two abstraction columns (K4 graph = topology vs srs embedding = realized geometry) crossed with the small/large-signal kernel axis; every per-column fact is grounded in its own canonical leaf (cited inline). Mints no new proposition — the vocabulary/def- adjudications live in vocabulary-register.md and the FORM/VALUE per-constant accounting in form-deriving-value-importing.md + interlock-register.md."
path-stable: "the canonical lattice model-register leaf — the K4-graph/srs-embedding × small/large-signal 2×2"
-->

# Lattice Model Register — the K4-graph / srs-embedding × small/large-signal 2×2

> **What this leaf is.** A **routing register** that separates *which layer of the lattice model owns which
> quantity*, so a claim is never attributed to the wrong abstraction column. Two orthogonal axes organize it:
> **(Axis A)** the abstract **K4 graph** (connectivity/topology) vs. the realized **srs embedding** (geometry
> and scales); **(Axis B)** the constitutive kernel's **small-signal** ($S\!\approx\!1$) vs **large-signal**
> ($S=\sqrt{1-A^2}$) regime. It mints no claim (no-claim); every entry points at its canonical home. Companion
> to [`form-deriving-value-importing.md`](form-deriving-value-importing.md) (the FORM/VALUE organizing
> principle this register is the lattice-clothes restatement of) and
> [`vocabulary-register.md`](vocabulary-register.md) (the per-term `def-` adjudications).

## Axis A — the two abstraction columns (topology vs realized geometry)

| Quantity / signature | **K4 graph** (abstract connectivity) | **srs embedding** (realized geometry) |
|---|---|---|
| What it is | the Sunada-K4 connectivity — *which node bonds which*, no lengths, no frame | the physical chiral srs net at pitch $\ell_{node}$, $z=3$, right-handed $I4_132$ ([`axiom-definitions.md:16`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)) |
| Owns | **KCL/KVL** (cycle / cut-set space); the $A_4\!\leftrightarrow\!2T$ double-cover holonomy (spin-½ representability, `vol1/claim-quality.md:1011`); **winding classes**, charge $=$ Link $\in\mathbb{Z}$ (the integer **FORM**, Axiom-2 TKI); disclination classification | $\ell_{node}$ and **all scales**: $\omega_0=m_ec^2/\hbar$, the Brillouin zone / band edge, the dispersion $\omega(k)$; the network-velocity factor $1/\sqrt3=c(k\!\to\!0)/c_{link}$ ([`boundary-observables-m-q-j.md:95`](boundary-observables-m-q-j.md)); $Z_0=\sqrt{\mu_0/\varepsilon_0}$; $\nu_{\mathrm{Hill}}=2/7$ ([`vacuum-poisson-ratio.md:18`](../vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md)); chirality-as-handedness; **THE REST FRAME** |
| Sensitivity | **frequency-blind AND amplitude-blind** (pure topology) | carries every dimensionful scale (frequency- and geometry-sensitive) |

**The rest frame is a geometry-column fact.** The abstract K4 graph has **no frame** — connectivity is
frame-free. A preferred rest frame exists only once the graph is *embedded* at a pitch $\ell_{node}$; that
substrate rest frame is identified empirically with the CMB rest frame
([`cosmic-axes-and-frames-glossary.md:17`](cosmic-axes-and-frames-glossary.md)). The Letter's **P6 sidereal
signature** (a first-harmonic $P_{flip}$ modulation at fractional amplitude $4\beta\simeq4.9\times10^{-3}$,
phased to the CMB dipole; `papers/2026_birefringence_letter/provenance.md:31`) is therefore
**geometry-column physics** — it turns on the embedding's rest frame, not on the abstract graph.

**Topology owns the integers; the embedding owns the values.** Charge $=$ Link $\in\mathbb{Z}$ is the
integer FORM the graph fixes (the sourced-monopole *value* route is closed at BRANCH-3; the charge FORM is
derived, its VALUE imported via $\xi_{topo}=e/\ell_{node}$ — see
[`the-sourced-charge-no-go-cascade.md`](the-sourced-charge-no-go-cascade.md)). This is the same FORM-derives /
VALUE-imports split of [`form-deriving-value-importing.md`](form-deriving-value-importing.md), read down the
topology-vs-embedding columns.

## Axis B — the orthogonal kernel axis (small-signal vs large-signal)

Orthogonal to Axis A, the Axiom-4 constitutive kernel $S(A)=\sqrt{1-A^2}$ has two operating regimes:

| Regime | Operating point | What it looks like | Signatures |
|---|---|---|---|
| **Small-signal** | $S\approx1$ (cold, $A\ll1$) | linear Maxwell vacuum | $c$, $Z_0=377\,\Omega$, ordinary propagation |
| **Large-signal** | $S=\sqrt{1-A^2}$ | the varactor law | $V_{yield}$, the birefringence coefficient, saturation |

**The Letter lives in the weakly-nonlinear corner.** The birefringence and four-wave-mixing predictions are
**small-signal-about-a-quiescent-point** — the *first Taylor term* of the large-signal varactor law
($\delta n_{bir}\approx-\tfrac12 A^2$, the leading $|E|^2$ response about $A=0$;
[`vacuum-birefringence-e4.md`](../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md),
[`vacuum-photon-photon-channel.md`](../vol4/falsification/ch12-falsifiable-predictions/vacuum-photon-photon-channel.md)).
It is NOT the full saturating regime (that is $A\to1$, $V_{yield}$, rupture). The $\varepsilon$ / $\mu$ grades
are orthogonal reactances (A1 $\perp$ T2, [`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)).

## The IR/UV refinement — Axis A crossed against wavelength

Axis A has a wavelength-dependent reading — the **FORM/VALUE law in lattice clothes**:

- **Long wavelengths (IR, $q\ell_{node}\to0$) are embedding-universal.** The response is dominated by the
  graph connectivity + the calibrated continuum constants ($c$, $Z_0$, $\varepsilon_0$, $\mu_0$); the specific
  srs micro-structure washes out. This is why the continuum (long-wave) predictions are peer-with-Maxwell.
- **Short wavelengths (UV, $q\ell_{node}\to O(1)$) see the specific srs structure.** The band edge, the
  quartic Bloch anisotropy $(q\ell_{node})^4$, and the zone-edge cutoff are *realized-geometry* facts that
  only appear as $q$ approaches the Nyquist edge.

This is exactly [`form-deriving-value-importing.md`](form-deriving-value-importing.md) read against
wavelength: the IR is the calibrated/universal (VALUE-carrying) limit; the UV is where the substrate-distinct
FORM (the srs-specific structure) becomes visible.

## Two validity fences of the small-signal model

The weakly-nonlinear small-signal model the Letter uses is bounded on **two independent axes** — one per register axis:

1. **Amplitude fence (Axis B):** $A\ll1$. Above it the linear-about-quiescent Taylor truncation fails and the
   full $\sqrt{1-A^2}$ saturation (up to $A\to1$, rupture) takes over.
2. **Frequency fence (Axis A, embedding column):** $\omega\ll\omega_0=m_ec^2/\hbar$, i.e. below the band edge.
   Above it the constitutive (smooth-medium) description hands off to the defect / electron-pair sector — the
   NAMED OPEN ITEM of
   [`vacuum-photon-photon-channel.md`](../vol4/falsification/ch12-falsifiable-predictions/vacuum-photon-photon-channel.md).

> **Slew-identity pointer (FRAMING, not canon).** The two fences can be read as the two ratings of one
> amplifier: an *output-swing* rating (the $\varepsilon$-kernel $S(A)=\sqrt{1-A^2}$, cap $E\le E_c$) and a
> *slew-rate* rating (a $\mu$-kernel keyed on the normalized slew $A_I=\dot E/(E_c\omega_0)=(E/E_c)(\omega/\omega_0)$,
> cap $\dot E\le E_c\omega_0$), meeting at the vacuum's **full-power-bandwidth corner** $(\omega_0,E_c)$. This
> reading — and whether the above-$\omega_0$ closure is a hard band-edge cutoff (breather branch, EVADES
> ATLAS) or a power-law tail (aliased-Bloch branch, BOUNDED) — is framed in
> `research/2026-07-09_highE-carrier-fpb-corner_walked-framing.md` (**PR #595, UNMERGED — framing, not canon**;
> the derivation gate is task #29). Do not treat the slew identity as derived.

## Cross-references

- [`form-deriving-value-importing.md`](form-deriving-value-importing.md) — the FORM-derives / VALUE-imports organizing principle (this register is its lattice-column restatement).
- [`vocabulary-register.md`](vocabulary-register.md) — the per-term `def-` adjudications (e.g. `node` = spatial-Brillouin cell); this register routes, it does not re-adjudicate terms.
- [`vacuum-birefringence-e4.md`](../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) and [`vacuum-photon-photon-channel.md`](../vol4/falsification/ch12-falsifiable-predictions/vacuum-photon-photon-channel.md) — the small-signal-about-quiescent applications this register scopes.
- [`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md) — the A1 $\perp$ T2 sector orthogonality underlying Axis B's $\varepsilon$/$\mu$ grades.
