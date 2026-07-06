# Problem 3 — muonic-hydrogen 2S–2P shift from the SVE elliptic kernel: METHOD pre-registration

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/problem3-muonic-lamb` (stacked on the freeze commit)
**Class:** METHOD pre-registration (frozen BEFORE any Problem-3 shift number is computed).
**Gates on:** the FROZEN electrostatic-sector fork memo.

> ## Post-freeze notes (append-only caveats on the frozen body below)
> **N1 — sign convention.** The §7 falsifier clause "*If the
> shift is NEGATIVE (it should be positive — field enhanced), my sign/inversion-branch is wrong*" is
> written in the positive-test-charge (δV) convention, which is the WRONG frame for the observable. The
> bound particle is the **µ⁻ (q = −e)**: the energy shift is `δE(nℓ) = −e·⟨nℓ|δV|nℓ⟩`, so `δV>0` (field
> enhanced) pulls levels DOWN, not up. The physical falsifier is on the level-energy sign in the µ⁻
> frame, NOT on ⟨δV⟩. Also the sign of `δ[ΔE]` is variant-dependent (penetration-dominated variants give
> `δ[ΔE]>0`, the Uehling direction; the ℓ_node-cutoff variant gives `δ[ΔE]<0` because the 2P outer
> region dominates) — so NO single sign is a clean falsifier; the routing is by MAGNITUDE, which is
> non-perturbatively large in every variant regardless of sign. The correct signed observable and the
> convention are stated in the RESULT doc's "SIGN CONVENTION" box and "Sign structure of δ[ΔE]" section.
> This note does not change any magnitude or the routed bin ([C-EXCLUDED]).
>
> **N2 — interior-variant boundary r_ns → r_turn.** §3 declares the continuum
> interior variants (C-i/C-ii/C-iii) at the no-solution radius `r_ns = 112.9 fm`. The code implements
> them at the **D-turnover radius `r_turn = r_ns·√2 = 159.6 fm`**. This is FORCED, not a drift of
> convenience: §2 of this prereg already states the constraint — the real lower branch of
> `E·√(1−(E/E_c)²)=E_C` is lost at the D-turnover `E_C = E_c/2` (at `r_turn`), NOT at `E_C = E_c` (at
> `r_ns`). δV(r_ns) as §3 literally worded it is incomputable (no real field there). The turnover
> boundary is the physically correct one and is **direction-conservative**: `r_turn > r_ns`, so cutting
> the integral at `r_turn` includes LESS of the divergent near-nucleus region than a literal-`r_ns` cut
> would — the literal-`r_ns` variant would give an EVEN LARGER shift, only strengthening [C]. §3's
> `r_ns` wording is superseded by §2's turnover constraint; the boundary used is `r_turn = r_ns√2`.
> No magnitude that routes changes direction; the routed bin stays [C-EXCLUDED].

> ## FREEZE-GATE RECORD (the ordering proof)
> **Fork-memo FREEZE commit (Grant-ratified 2026-07-05):**
> `4747630bf35e5e5abdd816ca022e8fcb5ba343ca`
> — *"freeze: electrostatic-sector fork memo FROZEN (Grant-ratified 2026-07-05) — gates Problem 3"*
> Verified on `origin/analysis/letter-v2-arm2` (the branch tip) via `git fetch origin` +
> `git branch -r --contains 4747630b` before ANY Problem-3 number was computed. This branch is
> **rebased onto that freeze commit** (`git rebase 4747630b…`); the freeze is my parent. The
> bins in §"ROUTING" below are quoted verbatim from the frozen memo §3; I route on them, I do
> not reinterpret them.
>
> This METHOD prereg is itself FROZEN (this commit) before the shift computation runs. The
> interior-variant list (§3) and the lattice-scoping forms (§4) are declared HERE, before running.

---

## 0. Regime header (mandatory — declare before any substrate word)

- **Sector:** STATIC-E (electrostatic). The SVE elliptic kernel `S(E)=√(1−(E/E_c)²)` is applied to
  the *static Coulomb field of the nucleus*, a DC-bias field.
- **Regime:** the nuclear Coulomb field near the muon orbit reaches `A²=(E/E_c)²~0.025` at the muonic
  Bohr radius and `A²→1` at `r_ns=113 fm` (below that, no real S — the interior). So the orbit
  straddles cold-linear (large r) into near-saturation (small r).
- **Phase-state:** DC bias. Per the merged AC/DC epistemological carve (`form-deriving-value-importing.md`
  §"AC/DC carve") and the frozen memo §3 Keith-arm rejection, **matter's static DC bias IS the
  saturating quantity** — the atomic static-E sector is precisely where the varactor is biased hard,
  which is why this is the sharp constraint. This is an in-scope DC-internal test (a DC potential-energy
  shift read through the atomic spectrum, itself a DC→AC-coupling observable: the 2S–2P splitting is a
  transition frequency).
- **Q-point chain:** the node sits at a self-set Q-point (`node-up-small-large-signal.md`); `E_c` is set
  by that Q-point via `E_c = E_YIELD = V_YIELD/L_NODE = √α·(m_e c²)/(e·ℓ_node) = √α·E_crit`
  (`constants.py:489,500`; Letter Eq. (Ec) `papers/2026_birefringence_letter/main.tex:186`).

## 1. Target (one sentence)

Compute the leading SVE-kernel correction δ(2S−2P) = ⟨2S|δV|2S⟩ − ⟨2P|δV|2P⟩ to the muonic-hydrogen
Lamb splitting, where δV(r)=V_SVE(r)−V_Coulomb(r) is the change in the electrostatic potential of a
point nucleus when the vacuum permittivity saturates as `ε_eff=ε₀√(1−(E/E_c)²)`, and route it against
the frozen [A]/[B]/[C] bins by comparison to the µeV-class new-physics window of the CREMA measurement.

## 2. The physics (Gauss-forced D, inverted constitutive law) — analytic core

- **D is geometry-forced.** Spherical symmetry + ∇·D=ρ ⟹ `D(r) = e/(4πr²)` EXACTLY (Gauss; independent
  of the constitutive law). Define the *Coulomb field* `E_C(r) ≡ D(r)/ε₀ = e/(4πε₀r²) = k/r²` with
  `k ≡ e/(4πε₀)` [units V·m].
- **Invert the constitutive law per r.** `D = ε₀S(E)E ⟹ E·√(1−(E/E_c)²) = E_C(r)`. The true field
  `E(r)` solves this. The LHS has maximum `E_c/2` at `E=E_c/√2` (D-turnover); above `E_C > E_c/2` there
  is no real branch below the turnover — **the interior**, `r < r_ns`, where the continuum kernel has
  no single-valued solution. (Turnover `E_C=E_c/2` occurs at `r_turn = r_ns·√2`; no-real-S at `E=E_c`,
  `E_C=0`… — note the constraint is `E_C ≤ E_c/2` for a real *lower* branch, sharpening the interior;
  this is declared and will be handled explicitly by the interior variants.)
- **Leading series (sympy-verified, this session).** For `x=E_C/E_c` small, the lower-branch inversion
  `u=E/E_c` is `u = x + ½x³ + ⅞x⁵ + …`, so the field is *enhanced*: `E = E_C + ½E_C³/E_c² + …`
  (bigger E needed to carry the same D when S<1).
- **δV tail (sympy-verified).** `δV(r) = ∫_r^∞ (E−E_C) dr' = ∫_r^∞ ½E_C(r')³/E_c² dr' + …
  = k³/(10 E_c² r⁵)` at leading order ⟹ **δV/V_C = (1/10)·A²(r)**, `A²(r)=(E_C(r)/E_c)²`. This is
  the expected (E/E_snap)²-class tail. δV > 0 (potential is *raised*).

## 3. TWO ARMS × interior variants (declared BEFORE running — the fork memo's structure)

**ARM CONTINUUM** — kernel applied at all r down to `r_ns`, interior handled by DECLARED variants:
- **(C-i) D-cap:** D held at `D_max = ε₀E_c/2` (the turnover value) inside `r_ns` ⟹ E frozen at
  `E_c/√2` there; δV integrand frozen at its `r_ns`-boundary value inside.
- **(C-ii) δV-freeze:** δV(r) held at `δV(r_ns)` for `r < r_ns` (constant-potential core).
- **(C-iii) interior-excluded:** the `r < r_ns` shell contributes zero to the perturbation integral
  (integral lower limit = `r_ns`).
The spread across (C-i/ii/iii) is the continuum arm's honest uncertainty BAND.

**ARM LATTICE-SCOPED** — kernel correction suppressed below the lattice pitch `ℓ_node = 386.16 fm`
(`constants.py:282`), per the frozen memo's declared scoping forms:
- **(L-i) hard cutoff at ℓ_node:** δV(r)=0 for `r < ℓ_node`; unmodified SVE tail for `r ≥ ℓ_node`.
- **(L-ii) soft `(qℓ_node)²`-class form:** the memo's scalar soft form — suppress the correction by a
  smooth factor that turns off below the pitch. Declared realization (frozen): multiply the δV
  integrand by `S_soft(r) = 1/(1 + (ℓ_node/r)²)` (a `(qℓ_node)²`-class scalar soft cutoff, monotone,
  →1 for `r≫ℓ_node`, `∝(r/ℓ_node)²→0` for `r≪ℓ_node` — the isotropic scalar channel of the memo's
  `(qℓ_node)²` form, NOT the anisotropic quartic). This is a declared functional form, not a fit.
Both (L-i/ii) banded.

Note: `r_ns=113 fm < ℓ_node=386 fm`, so lattice-scoping cuts OUTSIDE the breakdown radius — it is a
strictly more aggressive suppression than any continuum interior variant. Expect lattice-scoped ≪
continuum.

## 4. The shift + the tautology guard (two independent code paths)

δE(2S)−δE(2P) = ⟨2S|δV|2S⟩ − ⟨2P|δV|2P⟩, first-order perturbation with analytic hydrogen-like
wavefunctions at muonic reduced mass (Z=1):
- `R_2s(r) = (2a)^{-3/2}(2−r/a)e^{−r/2a}/√2`-normalized form; `|ψ_2s(0)|²=1/(8πa³)` (penetrates).
- `R_2p(r) ∝ r e^{−r/2a}`; `ψ_2p(0)=0`, suppressed as r² near nucleus by the ℓ=1 barrier
  (the asymmetry IS the signal — 2S sees the near-nucleus δV, 2P does not).
- `a = a_μ = a₀·(m_e/μ_red)`, `a₀=ℓ_node/α` (`constants.py:337`).

**Two independent code paths (tautology guard):**
- **PATH A (analytic/sympy):** evaluate `∫₀^∞ |R_nℓ(r)|² δV_tail(r) r² dr` in closed form where δV is the
  leading `k³/(10E_c²r⁵)` tail (tractable: reduces to Γ-function / incomplete-Γ integrals over
  `r^m e^{−r/a}`), with the interior handled analytically per variant.
- **PATH B (direct numerical quadrature):** invert the FULL constitutive law `E·√(1−(E/E_c)²)=E_C(r)`
  numerically per r (root-find the lower branch), integrate `δV(r)=∫_r^∞(E−E_C)dr'` numerically, then
  `⟨nℓ|δV|nℓ⟩` by quadrature — the full nonlinear kernel, NOT just the leading tail.
- **ReconcileGate:** PATH A (leading-tail) and PATH B (full-kernel) must agree to within the
  higher-order `⅞x⁵/…` truncation error where the tail dominates the integral (derived tolerance:
  the fractional difference ≤ the ratio of the next-order term, `~(A²_typical)`, evaluated at the
  integral's effective support). Can-fire proven by construction: A and B share NO code (A is symbolic
  integration of the truncated series; B is numerical root-find of the full transcendental law +
  numerical quadrature). A positive control: on a test where δV is set to a pure `1/r⁵` with a known
  coefficient, both paths must return the same analytic ⟨2S|·|2S⟩.

## 5. The window I adjudicate against (provenance)

- **Measured 2S–2P (2S_{1/2}–2P_{3/2}) splitting:** `202.3706(23) meV` — CREMA, Antognini et al.,
  Science 339, 417 (2013) / Pohl et al. Nature 466, 213 (2010). The `(23)` is the 1σ experimental
  uncertainty = `0.0023 meV = 2.3 µeV`.
- **QED accounts for the splitting at the µeV level** (theory uncertainty is dominated by the proton
  charge radius / higher-order QED, at the few-µeV to tens-of-µeV level). The available NEW-PHYSICS
  window — the room a non-QED static-E kernel correction has before it would already have been seen —
  is therefore **µeV-class**.
- **The window I adjudicate against (stated exactly, with provenance):** an SVE shift is
  **window-clearing** if |δ(2S−2P)_SVE| ≤ the experimental 1σ, `2.3 µeV` (the conservative edge:
  a correction smaller than the measurement error is unobservable and cannot be excluded);
  **window-violating** if it exceeds it. I ALSO report against a looser `10 µeV` edge (a
  representative combined experiment+theory scale) as a secondary band, and against the FULL splitting
  `202.4 meV` as the gross-violation reference. The PRIMARY gate is the `2.3 µeV` 1σ edge. Knife
  armed: any arm landing suspiciously ON an edge; the ½/¼-class coincidences (report, derived-only);
  the memo's `0.78` consonance (report, never lean).

## ROUTING (bins quoted VERBATIM from the frozen memo §3 — route, never reinterpret)

- **[A-CONSISTENT]** — "the continuum kernel is already safe … come in UNDER the µeV windows even
  without any regime scoping" (must survive the U91+ no-real-solution point).
  → routed if the CONTINUUM arm (all variants, banded) clears the `2.3 µeV` window.
- **[B-AVE]** — "the shifts violate the windows UNLESS the kernel is scoped to `r >> ell_node`" …
  "protected once the kernel is scoped to `r >> ell_node = 386 fm` — the lattice scale, NOT a new
  fitted parameter".
  → routed if the CONTINUUM arm violates AND the LATTICE-SCOPED arm clears.
- **[C-EXCLUDED]** — "even with the kernel scoped to `r >> ell_node`, the atomic-sector shifts violate
  the µeV windows".
  → routed if BOTH arms violate.

## Pre-registered expectation (Step 3 — with dimensional analysis, Step 3.5)

- **Dimensional ingredients (canonical values, this session):** `E_c=1.1304e17 V/m` (`E_YIELD`),
  `k=e/(4πε₀)=1.4400e−9 V·m`, `a_μ=284.75 fm` (`=a₀·m_e/μ_red`, μ_red=185.84 m_e), `r_ns=112.86 fm`,
  `ℓ_node=386.16 fm`.
- **Dimensionless combination + power-counting.** The 2S penetration integral of the `1/r⁵` tail is
  dominated by its small-r cutoff. `⟨2S|eδV|2S⟩ ~ |ψ_2s(0)|²·e·(k³/10E_c²)·4π·∫_{r_cut}r^{−3}dr
  = |ψ_2s(0)|²·e·(k³/10E_c²)·2π/r_cut²`. With `|ψ_2s(0)|²=1/(8πa_μ³)`, this is
  `~ e·k³/(40·a_μ³·E_c²·r_cut²)`. The cutoff `r_cut` is r_ns (continuum) or ℓ_node (lattice-scoped),
  and the shift scales as `1/r_cut²` — steeply cutoff-sensitive, which is the whole fork.
- **Numerical pre-estimate (rough, one-term, this session — NOT the frozen result):** continuum arm
  with `r_cut=r_ns` gives an order `~10⁴ meV` (≈ 20 eV) shift — **~10⁷× the µeV window** (gross
  violation). Lattice-scoped with `r_cut=ℓ_node` reduces by `(ℓ_node/r_ns)²≈11.7×` from the cutoff plus
  the additional suppression of the tail out at 386 fm where `A²(ℓ_node)~0.006` — still likely large.
  This rough estimate is a ONE-TERM tail cap; the frozen computation with real wavefunctions + full
  variants + full kernel is what adjudicates.
- **My prediction:** continuum arm VIOLATES the window grossly (likely by many OOM). Whether the
  lattice-scoped arm clears is the live question ⟹ I expect **[B-AVE] or [C-EXCLUDED]**, leaning
  toward whichever the ℓ_node-scoped integral lands. [A-CONSISTENT] is unlikely given the `1/r⁵`
  near-nucleus enhancement, but is on the table if the 2S penetration integral is far smaller than the
  cap estimate (the estimate is an upper bound; the real |ψ_2s|² is not constant at |ψ(0)|² over the
  core).
- **Discriminating outcomes:** [A] continuum clears (→ Letter stronger). [B] continuum violates,
  lattice clears (→ ℓ_node enters as the regime floor; forward prediction on cutoff-dependent
  coefficients). [C] both violate (→ static-E extrapolation excluded, AC birefringence + µ-sector
  survive as separate sectors per memo §3 ledger).
- **Falsifier of my framing:** if PATH A and PATH B disagree beyond the derived truncation tolerance,
  my leading-tail analytics are wrong and the full-kernel PATH B governs. If the shift is NEGATIVE
  (it should be positive — field enhanced), my sign/inversion-branch is wrong.

## SECONDARY (only if cheap once the machinery exists)

U91+ 1s shift vs the `460.2 ± 4.6 eV` Lamb measurement (Gumberidze et al.). The continuum arm may be
INCOMPUTABLE: the U91+ 1s orbit (`~575 fm`) sits INSIDE the no-solution radius (`r_ns(Z=92)=1083 fm`),
so the continuum kernel has no real solution over the bulk of the 1s density — an incomputability is
itself a reportable result, not a failure. Report the lattice-scoped arm and the incomputability.

## Discipline tags

- Canonical constants only (grep-confirmed `constants.py`). Muon mass declared as EXTERNAL CODATA input.
- Two independent code paths + ReconcileGate (no self-verifying gate; gates the CONSUMED observable,
  the 2S−2P shift).
- Magnitudes as BANDS over declared variants; no six-digit false precision.
- Pure-corpus. Honest closure (Rule 11): route on the frozen bins, no post-hoc criterion drops.
