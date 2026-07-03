[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- claim-quality: clm-1wmyx3 -->

<!-- kb-frontmatter
kind: leaf
claims: [clm-1wmyx3]
-->

# Brillouin-Zone UV Cutoff: the 1-loop integral is FINITE by mode-count (engine capability)

> **Class + scope (load-bearing honesty).** This is the *engine-capability / consistency-class* driver
> confirmation (clm-1wmyx3) of a claim already canonical elsewhere: **the electron's finite-size lattice pitch
> $\ell_{\text{node}}$ supplies a PHYSICAL UV cutoff, so the self-energy loop is finite with no
> renormalization** — the "UV divergence is naturally absent" statement of
> [`q-g20a-lamb-shift-structural-closure.md`](q-g20a-lamb-shift-structural-closure.md) (clm-3i66gp) and the
> exact discrete-Hilbert commutator of [`../../appendices/app-e-dcve/dcve-specification.md`](../../appendices/app-e-dcve/dcve-specification.md).
> Stage-2 of the GR-QED extension arc **numerically exhibits** the loop-finiteness side-by-side against the
> continuum divergence, and declares the distinct-cutoff discipline. **The cutoff FORM is FORM-DERIVED**
> (Axiom-1 lattice pitch, α-CLEAN, guard-tested); no new value-level chord is minted here.
>
> Engine source: [`src/ave/qed/brillouin_cutoff.py`](../../../../../src/ave/qed/brillouin_cutoff.py). Result doc:
> `research/2026-06-29_grqed-stage2-qed-extension_result.md`.

---

## §1 — The band-limited lattice propagator (FORM-DERIVED)

The vacuum is a real discrete lattice of finite pitch $\ell_{\text{node}}$. The EXACT discrete-Hilbert
commutator (DCVE App-E) gives $p_{\text{disc}}=(\hbar/i\ell)\sin(k\ell)$, hence
$[x,p]=i\hbar\cos(k\ell)=i\hbar\sqrt{1-(\ell p/\hbar)^2}$ — a **physical momentum cutoff** at the Brillouin edge
$|k|\le k_{\max}=\pi/\ell_{\text{node}}$, with **no counterterm**. The lattice propagator denominator is the
cubic-bond sum:

> **[Resultbox]** *Band-limited lattice dispersion*
>
> $$
> D_{\text{lat}}(\mathbf{k}) = \frac{2}{\ell^2}\sum_{b}\big(1-\cos(\mathbf{k}\cdot\hat{b}\,\ell)\big)-\frac{\omega^2}{c^2},
> \qquad 0\le D_{\text{lat}}\le \frac{12}{\ell^2}\ \text{everywhere in the BZ}.
> $$

At $q\ell\ll1$: $\cos(k\ell)\to1-\tfrac12(k\ell)^2$, so $D_{\text{lat}}\to|\mathbf{k}|^2$ — the **continuum QED
propagator denominator** (recover-QED, with the Taylor remainder $(k\ell)^2/12$). A 1-loop integral over the
FIRST Brillouin zone is **FINITE by mode-count** ($N=V/\ell^3$ modes, no counterterm); the SAME integrand in the
continuum **DIVERGES** with the cutoff $\Lambda$. This is the numerical realisation of the "UV divergence is
naturally absent — the cutoff is geometric, finite, and derivable from Axiom 1" claim of the Lamb-shift leaf.

## §2 — Gate table: recover-QED + finite-by-mode-count

| Gate | Class | Result | Verdict |
|---|---|---|---|
| recover-QED ($q\ell\ll1$: lattice $\to$ continuum propagator) | consistency (Class C) | rel. err $=(k\ell)^2/12$; quadratic in $k\ell$ (halving $k\ell$ quarters it, ratio $4.0$); holds off-axis | **PASS** |
| activate-at-cutoff — dispersion band-limits at BZ edge | manifestation (Class B) | $D_{\text{lat}}(\pi/\ell)=4.0/\ell^2$ (one axis), $12/\ell^2$ at corner; bounded over whole BZ | **PASS** |
| ★ BZ loop integral FINITE by mode-count | — | $\int_{\text{BZ}}d^3k/(D_{\text{lat}}+m^2)=1.245\times10^{14}$ — FINITE, converged $N=32\approx48\approx72$ | **PASS** |
| continuum contrast DIVERGES (no AVE claim) | — | $\int_{|k|<\Lambda}$: $7.1\times10^{13}\to7.8\times10^{14}$ as $\Lambda:1\to8\times k_{\max}$ (~$\Lambda$ linear, no plateau) | — (control) |

The contrast is the whole point: **SAME integrand**, FINITE on the compact Brillouin zone, arbitrarily large in
the continuum as the cutoff is lifted. The BZ integral needs **no counterterm** — the lattice pitch
$\ell_{\text{node}}$ is the regulator. The continuum branch carries **no AVE claim**; it exists only to exhibit
the divergence the BZ cutoff removes. The regulator FORM is **α-CLEAN** (purely geometric, guard-tested — no
`ALPHA`/`Q_TANK` reaches it).

## §3 — Distinct-cutoff discipline (spatial $k_{\max}$ vs temporal $\omega_C$)

Two distinct k-space ceilings, NOT to be conflated (a factor-$\pi$ error):

| Cutoff | Value | Role |
|---|---|---|
| SPATIAL $k_{\max}=\pi/\ell_{\text{node}}$ | $8.135\times10^{12}$ /m | the **LOOP-INTEGRAL bound** (the BZ quadrature domain edge, where $D_{\text{lat}}$ saturates at $4/\ell^2$) |
| TEMPORAL $\omega_C=c/\ell_{\text{node}}$ ($=1/\ell_{\text{node}}$ in 1/m) | $2.590\times10^{12}$ /m | the μ-grade (circulation-rate) ceiling — NOT used in the loop quadrature |

The loop integral is bounded by the **spatial** $k_{\max}=\pi/\ell_{\text{node}}$; $\omega_C$ is the
μ-saturation ceiling and does not enter. The ratio $k_{\max}/(\omega_C/c)=\pi$ exactly (guard-tested).

> **Reconciliation note (not a contradiction).** The spatial loop bound $k_{\max}=\pi/\ell_{\text{node}}$ here
> is the **Brillouin-zone edge** (the argpartition domain for the k-space quadrature), whereas the Lamb-shift
> leaf's cutoff $1/\ell_{\text{node}}=m_e c$ (clm-3i66gp, corrected 2026-07-02) is the **Compton momentum**
> ($\ell_{\text{node}}=\hbar/m_e c$) used as the upper limit of the Bethe-log radial integral. Both are the same
> geometric lattice scale $\ell_{\text{node}}$ up to the $O(1)$ zone-shape factor $\pi$; they are the same
> physics (Axiom-1 lattice pitch supplies the finite cutoff), applied in two different integration measures.
> They are consistent, not conflicting.

## §4 — What is and is NOT claimed (F4 Lamb honesty)

- **What IS true (claim it):** the lattice cutoff regulates the self-energy loop to a **finite value without
  renormalization** — the divergence-removal is structural (Axiom 1), demonstrated finite-by-mode-count in §2.
- **What is NOT true (do NOT claim it):** "AVE predicts the Lamb shift." The numeric agreement, where it exists,
  is a **matched cutoff-ratio log** ($\ln$ of the cutoff ratio), NOT a derived dynamical Bethe logarithm. This
  result doc makes **NO Lamb-shift prediction**; it demonstrates only the finite-by-cutoff structural property.

> **Drift carried (flag-don't-fix).** The Stage-2 result doc (2026-06-29) states the matched cutoff-ratio log
> "sits ~3.5× off QED's real value." The canonical Lamb leaf
> [`q-g20a-lamb-shift-structural-closure.md`](q-g20a-lamb-shift-structural-closure.md) was **corrected
> 2026-07-02** (α-factor cutoff fix, Rule 12): the cutoff is $1/\ell_{\text{node}}=m_e c$ (not $m_e c/\alpha$),
> so the AVE log is $\ln(1/\alpha)\approx4.92$ vs QED's $2.81$ — a **$1.75\times$** ratio, and "the previously
> mis-stated $3.5\times$." The Stage-2 doc's "~3.5×" **pre-dates** that correction; the current-canon figure is
> $1.75\times$. This leaf uses "matched-not-predicted cutoff-ratio log" (magnitude-agnostic) as the durable
> statement and defers the numeric ratio to clm-3i66gp. Surfaced for the auditor; the stale "~3.5×" lives only
> in the frozen result doc, not re-asserted here.

## Cross-references

- [`q-g20a-lamb-shift-structural-closure.md`](q-g20a-lamb-shift-structural-closure.md) (clm-3i66gp) — the self-energy / "UV divergence naturally absent" claim this driver confirms; carries the corrected cutoff $1/\ell_{\text{node}}=m_e c$ and the $1.75\times$ matched-log ratio.
- [`../../appendices/app-e-dcve/dcve-specification.md`](../../appendices/app-e-dcve/dcve-specification.md) — App-E, the exact discrete-Hilbert commutator $[x,p]=i\hbar\sqrt{1-(\ell p/\hbar)^2}$ that FORM-derives the band-limit.
- [`../../particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md`](../../particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md) — the companion "UV saturation at $q\to\pi/\ell_{\text{node}}$, no Landau pole" closure.
- **The E-route birefringence half of Stage-2 is already canonical** at [`../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) (clm-pp3qwf): $\delta n_{\text{bir}}=n_\parallel-n_\perp\approx-\tfrac12 A^2$, the $7.5/\alpha^3$ α-echo, the static-B null. Stage-2's birefringence run is a driver **confirmation** of clm-pp3qwf (bit-identical $n_\perp^2=S(A)$ to `fdtd_3d._compute_local_epsilon`), not new physics — no re-mint.
- Engine source: [`src/ave/qed/brillouin_cutoff.py`](../../../../../src/ave/qed/brillouin_cutoff.py) (`lattice_dispersion_denominator`, `loop_integral_brillouin_zone`, `continuum_loop_integral`, `K_MAX_SPATIAL`).

---

