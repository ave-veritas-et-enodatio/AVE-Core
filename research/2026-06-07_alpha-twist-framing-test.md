# α as the per-revolution cross-section TWIST of the (2,3) flux tube — pre-reg + test

**Date:** 2026-06-07
**Branch:** `analysis/2026-06-07-alpha-twist-framing`
**Status:** PRE-REGISTERED (framing + adjudication frozen before the driver was run)
**Discipline skills fired:** `substrate-native-check` (Checkpoint 4 phase-space-vs-real-space),
`phase-space-coordinate-check`, `pre-test-physics-check`, `ave-canonical-source`,
`consistency-vs-emergence`, `ave-prereg`.

---

## 0. Grant's framing (the hypothesis under test)

> α = how much the 2-D **cross-section** of the collimated/shaped flux tube (the
> electron's B-core, the (2,3) loop) **TURNS PER REVOLUTION** — the per-revolution
> **TWIST** (the framing / self-linking $\mathrm{Tw}$ in the Calugareanu–White sum
> $\mathrm{Lk} = \mathrm{Tw} + \mathrm{Wr}$) of the (2,3) flux tube. This = the spin
> slip = the precession = the loss tangent (~0.42° per revolution). It is a
> **phase-space** quantity (the framing on the $(V_\text{inc}, V_\text{ref})$
> Clifford torus), **not** a real-space length.

Numerically the target candidates Grant's "~0.42° per revolution" could mean:

| Label | Value (rad) | Value (turns) | Value (deg) |
|---|---|---|---|
| **α radians** | $\alpha = 7.29735\times10^{-3}$ | $1.1614\times10^{-3}$ | $0.41812°$ |
| **1/137 dimensionless** | $7.29927\times10^{-3}$ | $1.1617\times10^{-3}$ | $0.41823°$ |
| **1/137 of a turn** | $4.5862\times10^{-2}$ | $7.2993\times10^{-3}$ | $2.6277°$ |

"~0.42°/rev" $\Rightarrow$ Grant's intended target is **α radians** (equivalently 1/137
dimensionless), NOT 1/137-of-a-turn. Adjudication will report against all three.

## 1. The test (one line)

Compute the per-revolution cross-section twist $\mathrm{Tw}$ (the Calugareanu–White
framing / self-linking twist part) of the (2,3) flux tube, **α-free**, **in
phase-space** (on the $(V_\text{inc}, V_\text{ref})$ Clifford torus where the (2,3)
lives). Does it give $\alpha = 1/137$ — or α radians (~0.0073) — or 1/137 of a turn —
or a near-miss?

## 2. Distinct-from-the-mode-count declaration (frozen pre-run)

The Golden-Torus **mode-count** route (canonical, [ch8-alpha-golden-torus.md](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md))
gives $\alpha^{-1} = \Lambda_\text{vol} + \Lambda_\text{surf} + \Lambda_\text{line} =
4\pi^3 + \pi^2 + \pi \approx 137.0363$ — a **codimensional vol/surf/line measure** of
the Clifford-torus embedding (3-cycle phase volume + 2-cycle surface + 1-cycle
cross-section perimeter). That is a SIZE/MEASURE quantity.

The **twist** $\mathrm{Tw}$ under test here is a DIFFERENT geometric quantity on the
**same** (2,3) torus: the **framing** (self-linking twist part) — how the cross-section
rotates about the tube axis per revolution. Tw is a holonomy/rotation, not a measure.
A genuine new α-route would have Tw reproduce α through geometry orthogonal to the
mode-count. **Pre-registered question: is Tw an INDEPENDENT geometric quantity, or is
it secretly $1/(\text{mode-count})$ (i.e. loss-tangent $\tan\delta = 1/Q$ with
$Q = $ mode-count $= \alpha^{-1}$)?** The second would be α-recovering but NOT
independent (it just restates $Q = 137$). The driver reports both the raw Tw and the
$1/Q$ identity so the distinction is explicit.

## 3. What gets computed (α-free), and in which coordinates

Per `phase-space-coordinate-check`: the corpus claim is **phase-space** (the (2,3) is
the Clifford-torus $(V_\text{inc},V_\text{ref})$ winding; real-space the electron is
the $0_1$ unknot — [torus-knot-uniqueness.md §Note](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md)).
So the **load-bearing** computation is the phase-space (flat Clifford torus, $\mathbb{R}^4$)
one; the real-space (torus-of-revolution, $\mathbb{R}^3$) computation is the diagnostic
**shadow** reported alongside.

**Embedding A — phase-space, flat Clifford torus in $\mathbb{R}^4 = \mathbb{C}^2$:**
$$\gamma(t) = (R\cos pt,\; R\sin pt,\; r\cos qt,\; r\sin qt),\quad t\in[0,2\pi),\ (p,q)=(2,3)$$
with $z_1 = R e^{ipt} = V_\text{inc}$-axis circle, $z_2 = r e^{iqt} = V_\text{ref}$-axis
circle. The (p,q) winding is a geodesic on the flat torus. Reported: the surface-framing
twist (rotation of the normal-plane framing about the tangent), the natural winding-ratio
twist $q/p$, and the topological self-linking $pq$.

**Embedding B — real-space, torus of revolution in $\mathbb{R}^3$ (Golden Torus):**
$$\gamma(t) = \big((R + r\cos qt)\cos pt,\; (R + r\cos qt)\sin pt,\; r\sin qt\big)$$
Reported (Calugareanu–White / Moffatt–Ricca decomposition $\mathrm{Lk}=\mathrm{Tw}+\mathrm{Wr}$):
- **Writhe** $\mathrm{Wr}$ via the Gauss double integral.
- **Frenet/total-torsion twist** $\mathrm{Tw}_\text{Fr} = \frac{1}{2\pi}\oint\tau\,ds$.
- **Surface-framing twist** $\mathrm{Tw}_\text{surf} = \frac{1}{2\pi}\oint (T\times U)\cdot U'\,ds$
  with $U$ the outward tube-surface normal; internal cross-check $\mathrm{Wr}+\mathrm{Tw}_\text{surf}\stackrel{?}{=}pq=6$.
- **Pohl self-linking** $\mathrm{SL} = \mathrm{Wr} + \mathrm{Tw}_\text{Fr}$ (integer for a closed Frenet ribbon).

**Normalizations reported for every twist:** total (whole knot), **per toroidal
revolution** ($\div p = \div 2$), in turns / radians / degrees, plus the
small-defect candidates (fractional part / integer defect) in case Tw $= N + \epsilon$
with $\epsilon \sim \alpha$.

Geometries: Golden Torus ($R=\varphi/2$, $r=(\varphi-1)/2$, $R\cdot r=1/4$) AND a generic
$(p,q)=(2,3)$ torus (to show Tw depends on geometry but never on α).

## 4. ALPHA-CIRCULARITY GUARD (headlined — frozen pre-run)

Every input to $\mathrm{Tw}$ traced:

| Input | Source | Contains α / e / ε₀ / ħ / Z₀ / c (SI chain)? |
|---|---|---|
| $p=2,\ q=3$ | (2,3) winding (topology: smallest coprime, both ≥2) | **NO** — pure integers |
| $R=\varphi/2,\ r=(\varphi-1)/2$ | Golden Torus ($R\cdot r=1/4$ from Nyquist+self-avoidance; $\varphi$ from $2R^2-R-1/2=0$) | **NO** — golden ratio, α-free |
| $d=1\,\ell_\text{node}$ | Ax 1 Nyquist | **NO** |
| $\pi$ | pure math | **NO** |
| generic torus $R=1, r=0.3$ | arbitrary control geometry | **NO** |

**No α, e, ε₀, ħ, Z₀, c anywhere in the Tw computation.** `ALPHA` / `ALPHA_COLD_INV`
are imported **COMPARISON-ONLY** (final adjudication block, clearly tagged), never as
an input. Verdict logic:
- Pure (2,3)+golden-torus framing geometry → α-free → **if** Tw $=1/137$ → a
  GEOMETRIC α-derivation (the twist). 
- α-encoded anywhere → circular (would falsify the "α-free route" claim).
- α-free but $\neq 1/137$ → report the **near-miss** number, classify honestly.

## 5. Adjudication criteria (frozen pre-run — Rule 11, no post-hoc drift)

Let $\mathrm{Tw}_\star$ = the phase-space per-revolution twist (load-bearing). Compare
each reported normalization against the three §0 targets with tolerance bands:

- **PASS (geometric α-derivation):** some α-free, clearly-named, non-cherry-picked
  normalization of $\mathrm{Tw}_\star$ equals a §0 target within $|{\Delta}/{\text{target}}| < 1\%$,
  AND it is NOT the trivial $1/Q$-with-$Q$-defined-as-mode-count identity (§2), AND the
  same normalization is stable across the Golden vs generic torus in the way α-physics
  would require.
- **NEAR-MISS:** an α-free normalization lands within a factor ~2 of a target but not <1%.
- **NEGATIVE (distinct O(1) quantity):** the twist is an O(1) geometric number (e.g.
  near $pq=6$, near the writhe ~3, or $q/p=3/2$ turns) with no α-scale normalization →
  the twist route does NOT carry α; α lives in the mode-count, not the framing.
- **CIRCULAR:** α appears in an input → route rejected.

Honest-closure commitment (Rule 11): whichever bin the literal numbers fall in is the
recorded result. No debugging toward α; no dropping a criterion to convert ❌→✅.

## 6. Pre-test physics question (surfaced per `pre-test-physics-check`)

> **Plumber question for Grant:** is the "per-revolution cross-section twist" meant to
> be the **Calugareanu framing-twist $\mathrm{Tw}$** (an O(1) self-linking quantity,
> α-free and independent of the mode-count), or the **loss-tangent $\tan\delta = 1/Q$**
> where $Q$ is the golden-torus mode-count — because the former is a new independent
> route while the latter is $1/(\text{mode-count})$ and so not independent of the
> 137-mode-count?

Grant pre-specified the test in full detail (Calugareanu Tw, phase-space, α-free), so
the framing is taken as Grant-adjudicated at design time; the driver reports BOTH
quantities so the distinction is empirically explicit rather than assumed. Recorded
here so a future reader can see the fork was named before the run.

---

## 7. RESULTS

Driver: [`src/scripts/vol_1_foundations/alpha_twist_framing.py`](../src/scripts/vol_1_foundations/alpha_twist_framing.py).
Raw: [`2026-06-07_alpha-twist-framing-result.json`](2026-06-07_alpha-twist-framing-result.json).

### 7.1 Numerics validated (internal Calugareanu–White cross-check)

For all three tori the surface-framing identity $\mathrm{Wr} + \mathrm{Tw}_\text{surf} =
-pq = -6.0000$ holds to 4 decimals, and the Pohl self-linking is an exact integer
($\mathrm{SL} = -6$ golden, $-3$ generic-$r0.3$). $|\mathrm{Wr}|\approx 3.3$ also matches
the known ideal-trefoil writhe $\approx 3.4$. Both independent twist computations (Gauss
writhe integral + direct surface-framing integral) agree via the exact identity → numerics
trustworthy. (The overall sign is the (2,3) chirality; magnitudes carry the α comparison.)

### 7.2 The literal twist numbers (Golden Torus, $(p,q)=(2,3)$, $R\cdot r=1/4$)

| Quantity | Value | per toroidal rev ($\div 2$) |
|---|---|---|
| **PHASE-SPACE** winding twist $q/p$ (load-bearing) | — | **1.50000 turns = 9.42478 rad = 540.000°** |
| PHASE-SPACE framing turns $(V_\text{inc}, V_\text{ref})$ | $(2.0000, 3.0000)$, self-link $pq=6$ | — |
| REAL-SPACE writhe $\mathrm{Wr}$ | $-3.30708$ | $-1.6535$ turns |
| REAL-SPACE surface-framing twist $\mathrm{Tw}_\text{surf}$ | $-2.69292$ turns | **$-1.34646$ turns = $-8.46006$ rad = $-484.726°$** |
| REAL-SPACE Frenet/torsion twist $\mathrm{Tw}_\text{Fr}$ | $-2.69292$ turns | $-1.3465$ turns |
| integer-defects ($\mathrm{Tw}_\text{surf}$, $\mathrm{Wr}$, $\mathrm{SL}$) | $+0.30708,\ -0.30708,\ 0$ | — |

**Targets:** α-rad $=0.0072974$, 1/137 $=0.0072993$, 1/137-turn $=0.045863$ rad.

### 7.3 Adjudication — answers to the 7 return items

**(1) Tw (phase-space, the number + normalization).** The phase-space per-revolution
cross-section twist is **$q/p = 3/2$ turns = $540°$ = $9.42478$ rad per toroidal
revolution** — exact, and **geometry-independent** (identical $540°$ for the golden torus
and both generic tori; it depends only on the winding ratio $q/p$, not on $R,r$). On the
flat Clifford torus the $(V_\text{inc},V_\text{ref})$ framing makes exactly $p=2$ and $q=3$
turns in the two C-factors; the topological self-linking is $pq=6$.

**(2) α-free or α-encoded — full input trace.** **α-FREE.** Every input to Tw is
$\{p=2, q=3, R=\varphi/2, r=(\varphi-1)/2, d=1, \pi\}$. **No α, e, ε₀, ħ, Z₀, or c (SI
chain) appears anywhere** in the geometry. `ALPHA` / `ALPHA_COLD_INV` enter only the final
COMPARISON-ONLY adjudication block (verified by reading the driver: the constants are
imported, asserted canonical, and used solely inside `adjudicate()`; the geometry
functions take only `p,q,R,r,n`). The circularity guard (§4) is satisfied.

**(3) = 1/137 / α-rad / near-miss?** **NONE — clean NEGATIVE, not even a near-miss.**
Zero twist normalizations land within 1% of any target (`hits_within_1pct = []` for all
three geometries). The load-bearing phase-space number ($1.5$ turns $= 9.425$ rad) is
**$\sim 1292\times$ larger than α-rad** and **$\sim 205\times$ larger than 1/137-of-a-turn**.
The real-space surface-framing twist ($\approx 1.35$ turns/rev) is the same order. The
integer-defects ($\pm 0.307$) are not α either. The twist is an **$O(1)$ quantity, three
orders of magnitude away from $\alpha$**.

**(4) Phase-space vs real-space twist.** They **DIFFER**, and the difference is exactly
the writhe. Phase-space (flat Clifford torus): twist/rev $= q/p = 1.5$ turns **exactly**,
geometry-independent, no writhe (a flat-torus geodesic has no $\mathbb{R}^3$ writhe; the
full self-linking $pq=6$ is carried by the framing, framing-turns $(2,3)$). Real-space
(torus of revolution): surface-framing twist/rev $\approx 1.35$ turns, **writhe-modified
and geometry-dependent** (ranges $1.24$–$1.41$ turns/rev across the three tori), because
$\mathrm{Wr}+\mathrm{Tw}_\text{surf}=-pq$ splits the fixed self-linking $-6$ between writhe
$(-3.31)$ and framing $(-2.69)$. **Neither frame carries $1/137$.** The real-space shadow
is the phase-space twist with the writhe subtracted off.

**(5) DISTINCT from the Golden-Torus mode-count, or the same quantity?** **DISTINCT — and
the test confirms it empirically.** The mode-count is a **measure** ($\Lambda_\text{vol}+
\Lambda_\text{surf}+\Lambda_\text{line}=4\pi^3+\pi^2+\pi\approx 137.04$, a vol/surf/line
SIZE). The twist is a **framing/holonomy** (a rotation, $O(1)$: $1.5$ turns phase-space,
$1.35$ real-space). Different geometric class, magnitudes differing by $\sim 90\times$
($1.5$ vs $137$). The twist does **not** reduce to, reproduce, or invert the mode-count as
a geometric fact. **The only α-connection that exists is the separate loss-tangent identity
$\tan\delta = 1/Q$** — and that gives α **only if** $Q$ is set equal to the mode-count
($1/(4\pi^3+\pi^2+\pi)=\alpha_\text{cold}$, reported in the JSON). That identity
**presupposes the mode-count route** ($Q=137$); it is **not an independent twist-geometry
derivation of α**. So: twist-as-geometry and mode-count are distinct quantities, and the
twist does **not** carry α; the loss-tangent route is the mode-count route wearing a
$1/Q$ hat, not a new route.

**(6) Honest classification (Rule 11, `consistency-vs-emergence`).** **NEGATIVE /
falsification of the twist-as-α emergence candidate.** The computation is α-free
(non-circular — the good news: had it hit, it would have been a genuine geometric
derivation), but the twist is an $O(1)$ framing quantity that does **NOT** manifest $\alpha
= 1/137$, α-rad, or 1/137-turn. Class: this is **not** an emergence and **not** a
consistency-pass; it is a clean negative result with a single explanatory mechanism —
**α lives in the codimensional mode-count (the SIZE/measure of the Clifford-torus
embedding), not in the framing twist (the holonomy)**. The branch is closed: per Rule 11,
the falsification is recorded; per Rule 12 no rescue hypothesis is refilled into the slot.
The corpus's existing α route (mode-count, Class B at ch8) is unaffected and remains the
canonical home of $1/137$; this test independently re-confirms that the framing twist is a
*different* geometric object on the same (2,3) torus.

**(7) Doc + branch + SHAs:** this doc + driver + result.json on branch
`analysis/2026-06-07-alpha-twist-framing`; SHAs recorded in the PR / commit log.

### 7.4 One-line summary

> The per-revolution cross-section twist of the (2,3) flux tube is **$q/p = 1.5$ turns
> ($540°$) in phase-space** (exact, geometry-independent) / **$\approx 1.35$ turns
> real-space** (writhe-modified) — **α-free** and an **$O(1)$ quantity $\sim 10^3\times$
> away from $\alpha$**. The twist is a **framing/holonomy, distinct from the
> $4\pi^3+\pi^2+\pi$ mode-count (a measure)**, and it does **not** carry $1/137$. α is in
> the mode-count, not the twist. **Twist-as-α: FALSIFIED, branch closed (Rule 11).**
