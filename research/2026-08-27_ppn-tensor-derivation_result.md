# RESULT — PPN of the AVE gravity sector: two metrics, two gammas

**Date:** 2026-08-27 · **Branch:** `research/2026-08-27-ppn-tensor-derivation` · **Base:** `origin/main` @ `a3f4fef7`
**Class:** analytical derivation + numerical cross-check. Consistency/emergence tagging per section; the per-step ledger is §1.
**Prior art consumed:** `research/2026-06-05_gravity-ppn-coherence-result.md` · `research/2026-05-17_hulse-taylor-substrate-native-derivation-sketch.md` · `research/2026-08-11_gravity-linearity-audit_result.md`
**Routed open items:** `_orchestration/open-items/2026-08-27-ppn-matter-sector-walkback.md` · `_orchestration/open-items/2026-08-27-eps11-four-objects.md`

---

## SECTOR DECLARATION (read before any standard-physics word below)

**Which sector?** The A1 dilatation (bound / mass) sector and the T2 transverse (Cosserat shear / optical) sector, treated as two *separate* propagation cones. That separation is the whole finding.

**Does the engine carry that DOF?** Not exercised here. This is an analytical lane on canon's written constitutive statements plus a high-precision ODE/quadrature cross-check; no lattice integrator was run.

**Cold or saturated?** **COLD, sub-yield, lossless-reactive throughout.** Every number below is first-order-in-$m/r$ weak field, $\varepsilon_{11} \lesssim 10^{-6}$ at solar-system radii. Axiom-4 saturation is inactive at this amplitude and no saturation kernel enters any result. A saturated-regime restatement is **not** attempted and nothing here scopes to $r \to r_{sat}$.

**Regime / phase-state:** crystalline phase, static (no bias-propagation dynamics invoked), single isolated spherically symmetric source, test-particle limit.

**Coordinates.** Every metric statement is in **isotropic coordinates**, and the PPN coefficients are read off the standard isotropic-gauge forms
$-g_{00} = 1 - 2U + 2\beta U^2 + \dots$, $g_{ij} = (1 + 2\gamma U)\delta_{ij}$, with $U \equiv GM/(c^2 r)$.
Mixing an areal-radius statement with an isotropic-radius statement moves $\gamma$ by construction; §9's control exists to catch exactly that.

## §0 — VERDICT

> # AVE has two metrics, so two gammas.
> ### The optics sector is consistent with GR. The matter sector is off by a factor of six.

Canon assigns light and matter **different refractive indices over the same strain field** — `n_\perp = 1 + \nu_{vac}\varepsilon_{11}` for the photon (Op19, `manuscript/ave-kb/common/operators.md`:59) and `n_{scalar} = 1 + \varepsilon_{11}/7` for a massive defect (`manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md`:14). Fed through canon's own Gordon metric, those are two different spacetimes, and only one of them is GR.

| quantity | AVE derived here | measured (external import) | tension |
|---|---|---|---|
| $\gamma$ (light) | $1$ | Cassini $1 \pm 2.3\times10^{-5}$ | **pass** |
| solar-limb deflection | $1.7517''$ | $1.75''$ | **pass** |
| $\gamma$ (matter) | **$0$ exactly** | $1$ | $\sim4.3\times10^{4}\sigma$ |
| $\beta$ (matter) | **$3/2$ exactly** | LLR $1 \pm 1.1\times10^{-4}$ | $\sim4.5\times10^{3}\sigma$ |
| Mercury perihelion | **$7.163''$/century** | $42.98 \pm 0.04$ | $895\sigma$ |
| Hulse-Taylor periastron | **$0.7044^\circ$/yr** | $4.226595(5)$ | short by $3.522^\circ$/yr |

$$F \;=\; \frac{2-\beta+2\gamma}{3} \;=\; \frac{2 - 3/2 + 0}{3} \;=\; \frac{1}{6}.$$

**Independently confirmed by direct geodesic integration** (§9): apsidal-angle quadrature in the AVE matter metric returns $0.1666666632$ of the GR baseline $6\pi x$, while the same integrator on an isotropic-Schwarzschild **control** returns $1.000000289$ of it. The control is what makes the AVE number a measurement of the metric rather than of the integrator.

### THE STRUCTURAL REASON — stated here, not only in §2

A refractive index is **one** scalar function of $r$. A weak-field metric needs **two** independent functions, and $\gamma$ *is* the second one. Canon's own Gordon metric,
`manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md`:17 verbatim
$g_{\mu\nu}^{AVE} = \eta_{\mu\nu} + \left(1 - \frac{1}{n^{2}(r)}\right)u_{\mu}u_{\nu}$,
gives $g_{00} = -1/n^2$ and $g_{ij} = \delta_{ij}$ **exactly**, for any $n$ and any slope. A metric whose spatial part is flat has $\gamma = 0$ identically. No coefficient choice inside the $/7$ family can move it, because the family never enters $g_{ij}$ at all.

### ⚠ WHAT THIS IS, AND WHAT IT IS NOT — read before quoting any number above

- **This is not a new falsification of AVE's optics.** $\gamma_{light} = 1$ and $1.7517''$ hold. §6 argues they are a *calibrated consistency check* and not an emergence-class result, which is a downgrade of a claim's **class**, not of its truth.
- **This is not an engine bug.** No engine ran. It is a property of two written constitutive statements and the metric canon writes for them.
- **This does not adjudicate the fix.** §7 names the cheapest repair inside the framework. Naming a repair is not performing one, and this lane edits no canonical file.
- **The matter-sector numbers are only as good as the assignment that produces them.** They follow from taking `ponderomotive-equivalence.md`:14 literally as the metric a massive test body moves in. Canon's own quality record calls that assignment *"asserted by mechanical analogy rather than derived from a wave-equation projection"* (`manuscript/ave-kb/vol3/claim-quality.md`:1158). **If that assignment falls, these numbers fall with it** — which is the point of §7.

## §1 — THE DERIVED-vs-IMPORTED LEDGER

<!-- SECTION: ledger -->

## §2 — Two metrics, two gammas: the derivation chain

<!-- SECTION: chain -->

## §3 — Why the tensor repair failed

<!-- SECTION: tensor-repair -->

## §4 — `eps_11` is four objects across canon

<!-- SECTION: four-objects -->

## §5 — The /7 family is five contractions of one rank-2 tensor

<!-- SECTION: seven-family -->

## §6 — The light result is a consistency check, not a derivation

<!-- SECTION: light -->

## §7 — The fix is cheap and inside the framework

<!-- SECTION: fix -->

## §8 — Two things logged for months and never named

<!-- SECTION: logged -->

## §9 — Independent cross-check: direct geodesic integration

<!-- SECTION: geodesic -->

## §10 — METHOD, and its blind spots

<!-- SECTION: method -->

## §11 — Cite verification ledger

<!-- SECTION: cites -->

## §12 — Flags surfaced (NOT fixed by this lane)

<!-- SECTION: flags -->

## §13 — Skill-selection retro-pass

<!-- SECTION: retro -->
