[↑ Ch.8 Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v]
path-stable: "referenced from vol3 as sec:gw_propagation"
-->

---

## GW Propagation as Impedance Modulation

Gravitational waves are transverse inductive shear waves in the LC lattice---the same medium governed by the same operators. In accordance with the **Symmetric Scaling** axiom required to preserve a uniform optical vacuum, gravity scales both the local permittivity and permeability symmetrically via the refractive metric $n(r) = (1 - r_s/r)^{-1}$:

$$
\begin{align}
\varepsilon_{eff}(r) &= \varepsilon_0 \cdot n(r) \\
\mu_{eff}(r) &= \mu_0 \cdot n(r)
\end{align}
$$

where $r_s = 2GM/c^2$. Because both components scale proportionally, the macroscopic gravitational impedance remains invariant everywhere:

> **[Resultbox]** *Invariant Gravitational Impedance*
>
> $$
> Z(r) = \sqrt{\frac{\mu_{eff}(r)}{\varepsilon_{eff}(r)}} = \sqrt{\frac{\mu_0 \cdot n}{\varepsilon_0 \cdot n}} \equiv Z_0
> $$

Therefore, the reflection coefficient $\Gamma$ across any gravitational gradient evaluates identically to zero ($\Gamma = 0$). While the local speed of light slows down near mass ($c_l = c/n$), the impedance matching remains perfect. Gravitational waves experience zero reflection and zero scattering as they traverse deep gravitational wells, propagating seamlessly.

### Lossless Propagation

LIGO gravitational waves have strain $h \sim 10^{-21}$. The equivalent voltage per lattice cell is $V_{GW} = h \cdot c \cdot \ell_{\text{node}} \cdot 2\pi f \sim 10^{-19}$ V, which is $\sim 10^{-24}$ times smaller than $V_{\text{snap}} \approx 511$ kV. Far below the saturation threshold, the lattice acts as a perfect lossless linear transmission line. Gravitational waves propagate to cosmological distances without dissipation---~~matching LIGO observations exactly, with zero free parameters~~ *(clause struck 2026-08-02 per Rule 12 --- see the Reading-A admixture note below; the struck text is preserved, not deleted)*.

> **[2026-08-02 --- Reading-A bulk admixture: the ruled propagation of the ch08 item-3 wording]**
>
> **Status of this note.** Discharged-decision propagation of an already-ruled state --- it adjudicates nothing new. Grant ruled the #766-review F4 routed question to **option (a)** (`_orchestration/2026-07-10_rulings-docket.md:2573`; queue row `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:113`, "✅ RULED 2026-07-20 → option (a)"). That ruling was EXECUTED in the printed chapter by **PR #771** (merged 2026-07-21), whose own body records the debt this note discharges: *"any KB-leaf propagation of the item-3 admixture wording"*. Until now this leaf lagged the printed chapter --- an inversion of the standing rule that the KB is the truth source.
>
> **What this leaf omitted.** The identification of the **observed** gravitational wave as a **transverse shear** excitation (line 13 above) is **Reading-independent and stands untouched** --- it is the channel the Peters--Mathews $(v/c)^5$ formula computes and pulsar timing measures. What the leaf silently dropped is the *additional* channel. Mirroring the chapter's Reading-A statement (`manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:107`): under **Reading-A** (the standing physics as of 2026-07-20) the framework **additionally predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at $O(1)$ coupling**, $F_{\text{bulk}}/F_{\text{shear}} \approx 0.03$--$0.12$; that admixture is **not** part of the observed shear decay.
>
> **Why the clause above is struck.** "matching LIGO observations exactly, with zero free parameters" asserts a clean and *complete* match, while the framework simultaneously carries a **LIVE** pulsar exclusion of an independent $O(1)$ bulk radiative port plus an **OPEN** constituent-cage fork. The lossless linear-regime propagation of the *shear* channel is unaffected and stands; the exactness/completeness framing does not.
>
> **⚠ The bulk/shear double-count contradiction (Q1-REVERT) remains LIVE and routed. Reading-A is the standing physics --- it is NOT a closure of that contradiction.** [`common/port-register.md`](../../../common/port-register.md) (line 5) carries the live flag: the Q1 row was **REVERTED** 2026-07-20 to Reading-A-live --- the make-or-break mechanical common-mode derivation returned NONE-DERIVES (merged #761), firing the row's own clause, so the independent-radiative-port exclusion is **live against the framework**. The companion constituent-cage fork is **OPEN**: the deep-rail $k$-scaling adjudicator (#775) returned **BIN-3 / form-undetermined** --- the decisive measurement is not lattice-accessible in the quasistatic regime. This note states the honest standing state; it neither claims a clean gravitational chord nor pretends the bulk sector is settled.
>
> **⚑ FLAGGED, NOT FIXED (adjacent honesty-lag, outside this lane's scope --- flag-don't-fix).** The $\Gamma = 0$ paragraph at line 30 above is the *un-corrected* twin of [`invariant-gravitational-impedance.md`](invariant-gravitational-impedance.md) line 28, which received the **2026-06-11 three-impedance-law channel correction** ($\Gamma \to \Gamma_{EM}$; "Radio-frequency and optical signals experience zero EM reflection", not gravitational waves). This leaf never received that correction. Surfaced for adjudication, deliberately not edited here --- it is a *channel-attribution* lag, a different question from the Reading-A admixture this note propagates.

---
