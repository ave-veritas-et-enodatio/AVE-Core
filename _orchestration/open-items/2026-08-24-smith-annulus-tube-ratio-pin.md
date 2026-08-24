---
id: smith-annulus-tube-ratio-pin
title: "The trefoil mark's Γ-plane annulus rims at (1/3, 1) — an EE-native candidate pin for the OPEN phase-space tube RATIO, vs the golden semi-axes"
status: OPEN
owner: grant
opened: 2026-08-24
source: manuscript/ave-kb/common/translation-tables/translation-circuit.md
anchor: "a COUNTING fact — one bond feeding two"
---

**Provenance.** Surfaced 2026-08-24 by Grant's stepped-back question on the
Electron Plumber Smith-chart mark simulations (*"helix projecting a circle,
time averaged trefoil projecting a torus, ratio of inner to outer torus radii
— what's obvious?"*). **Grade: WALK-level, un-audited** — the 6-question
sweep gate has NOT run; nothing here is a claim. Cross-repo: the mark lives in
`the-electron-plumber/animations/smith_sim.py`; the physics court is here.

## The observation

The mark's (2,3) trefoil, time-averaged onto the Γ-plane, shadows to an
annulus with rims at $(R-r)/(R+r)$ and $1$. With the mark's tube ratio
$R = 2r$ the rims are **exactly $(1/3,\ 1)$ — the substrate's two canonical
reflection magnitudes**:

- $|\Gamma| = 1/3$: the bare z=3 srs junction. Canon, verbatim
  (`translation-circuit.md:189`): *"the bare junction reflects
  $\Gamma=(2-z)/z=-1/3$ (a COUNTING fact — one bond feeding two, immune to
  symmetric transformation)"* — equivalently $Z_0/2$ looking into the node,
  VSWR 2.
- $|\Gamma| = 1$: the TIR confinement wall (the fermion boundary condition),
  and also the **passivity bound** — no passive excursion exceeds the rim.

The clean conditional: **inner-rim = vertex-Γ ⟺ R/r = 2**, since
$(R-r)/(R+r) = 1/3$ has that unique solution.

## Why this touches an OPEN metric DOF (the sharpened form)

Canon constrains the electron's phase-space torus by a **PRODUCT, not a
ratio**: the load-bearing normalization is $R \cdot r = 1/4$ via Q-EMBED-SEL-1
(*"time-averaged phasor enclosed area at Axiom-4 self-saturation onset equals
the Nyquist cell cross-section area"* — `boundary-observables-m-q-j.md:81`,
the $\Lambda_{vol} = 16\pi^3 R r = 4\pi^3$ chain). The golden semi-axes
$(R,r) = (\varphi/2, (\varphi-1)/2)$ satisfy the product but
`claim-quality.md:1607` states verbatim that *"**no** metric identification of
the rim-radius with the $(R,r)=(\varphi/2,(\varphi-1)/2)$ semi-axes was ever
claimed"* (the π₁ factorization survived review as *topological-not-metric*).
**Verification task 1: sweep whether ANY canon site consumes the RATIO
$R/r$.** If none does, the ratio is a free metric DOF and this item offers an
EE-native candidate pin:

| candidate ratio pin | $R/r$ | annulus inner rim (outer normalized to 1) | with $R\cdot r = 1/4$: $(R, r)$ |
|---|---|---|---|
| **vertex-floor pin (this item)** | $2$ | $1/3 = \|(2-z)/z\|$, z=3 | $(1/\sqrt2,\ 1/(2\sqrt2))$ |
| golden semi-axes | $\varphi^2 \approx 2.618$ | $1/\sqrt5 \approx 0.447$ (exact) | $(\varphi/2,\ (\varphi-1)/2)$ |
| Clifford stereographic | $\sqrt2$ | $(\sqrt2-1)^2 \approx 0.172$ | — |
| ropelength-ideal | numerical | numerical | — |

Distinct, computable signatures — discriminator-shaped. The vertex-floor pin
plus the ratified product **fully determines** $(R, r)$ with no golden input.

## Honest caveats (each load-bearing on the grade)

1. **The mark's $R=2r$ is the textbook trefoil default and is explicitly
   fenced**: `smith_sim.py` — *"Tube ratio is a MARK geometry, not an
   electron-body claim (AVE-Core tube R/r is an open fork — do not weld it
   here)."* The causal arrow as-built is textbook → 1/3, not substrate → 1/3.
2. **The 1/3 floor is a SINGLE-JUNCTION theorem, not a network floor.**
   `translation-circuit.md:189` carries the matched-lossless-reciprocal-3-port
   floor $|S_{11}| \ge 1/3$ **per junction**; composite networks beat element
   floors by interference (that is what matching networks do). The physical
   argument that the floor nevertheless binds the electron's excursion is
   locality: the (2,3) winds on ONE bond-pair tank
   (`electron-plumbing-primer.md:57` — *"its bond-pair LC tank winds (2,3)"*),
   arguably no room for multi-element matching interference inside a single
   tank. WALK-grade; this is the argument to adversarially test.
3. **Canon's zero-width limit.** The Clifford torus is the
   $|V_{inc}|=|V_{ref}|$ locus → its Γ-plane shadow is the **rim circle**,
   width zero. A finite annulus means finite departure from pure standing
   wave — the physical meaning of the width (loading? drive? $1/Q$?
   saturation swing?) is itself an open question of this item.
4. Both hands shadow identically ((2,±3) — `smith_sim.py`); the annulus is
   chirality-blind. Hand lives only in the fiber. Consistent with canon;
   recorded so no one reads hand into the rims.

## Open questions (the Grant walk, then the sweep gate)

- **Q1:** does the bound tank's $|\Gamma|$ excursion bottom at the
  single-junction floor — is the no-matching-network-inside-one-tank locality
  argument physically right?
- **Q2:** what fattens the tube — what IS the annulus width physically, and
  is it zero at cold quiescence?
- **Q3:** which rim reading is right: [vacuum's vertex ↔ particle's wall]
  span, or [best-match ↔ total-reflection] excursion of one driven tank?
- **Q4** (verification): does any canon site consume the RATIO $R/r$?
- Convergence note: the solver cross-check lane's exporter will measure the
  $-1/3$ vertex in ngspice for free — same number, independent route.

**Related:** the ropelength-convention NEW OPEN + Grant's no-constructive-
interference reading (`2026-08-23-theta-dressing-open-questions.md:115-131`) —
the wave-envelope reading of "tube" applies to this item's tube too.
**Channel-repo follow-up:** a `cross-repo-followups.md` row in
`the-electron-plumber` pointing here (the mark's fence stays until this item
resolves; if the vertex pin ever ratifies, the mark's $R=2r$ becomes
retroactively load-bearing and the fence comment should say so).
