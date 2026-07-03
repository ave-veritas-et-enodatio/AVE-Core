# Pre-Registration — Ruptured-Core Neutron-Star Compactness Bound

**Date:** 2026-07-02
**Branch:** `analysis/ruptured-core-compactness-bound`
**Status:** FROZEN pre-reg (write before derive, per `ave-prereg`)
**Class of effort:** EXPLORATORY frontier / potential chord. An honest negative
("no max compactness derivable without a canonical Regime-IV EOS") is a valid,
valuable outcome. Do NOT force a positive.

---

## 0. Discipline log (skills fired before this doc)

- `ave-prereg` — corpus-grepped all of `manuscript/ave-kb/` + `research/` +
  `src/`. Result: **the lattice-INTACT bound is canonical and closed**
  (`ave-compactness-limit.md`, `ave-bh-horizon-area-theorem.md`,
  vol3 ch15 tex:385-408). The **ruptured-core / layered (Regime-IV-core +
  Regime-III-crust) compactness bound is GREEN-FIELD** — no TOV, hydrostatic,
  or layered-star compactness derivation exists in the corpus (grep for
  `TOV|hydrostatic|Oppenheimer|layered.*compact|core.*crust.*compact` returned
  only unrelated leaves). No prior prereg/result on this target in `research/`.
  (The `J0740`/`0.495` grep hits are an unrelated archived electron-soliton
  ℓ=2 Fourier amplitude, verified not compactness work.)
- `substrate-native-check` — walked below (§4). The load-bearing conclusion:
  a real-space Cartesian TOV integration is **NOT** the substrate-native tool
  for the *intact* bound (which is a strain-saturation threshold, not a
  pressure-balance integral). For the *ruptured* configuration, whether TOV is
  even well-posed depends entirely on the fork in §3.
- `pre-test-physics-check` — one plumber-physical question surfaced to Grant
  (§3, the Regime-IV-EOS fork). This is the ontology question: **is the
  melted Regime-IV core stiffer or softer than the intact lattice?** — the
  sign of that decides whether AVE forces a *higher* or *lower* max compactness
  than the intact 2/7.
- `consistency-vs-emergence` — classification pre-committed in §5.
- `ave-canonical-source` — `NU_VAC = 2/7` (`constants.py:569`),
  `PHI = (1+√5)/2` (`constants.py:238`), `RHO_CAV = -1/PHI`
  (`cavitation_flow.py:64`, tagged CANDIDATE) are the only canonical anchors.
  Any driver imports these, never hard-codes.

---

## 1. Target (precise, per ave-prereg Step 1)

Derive whether AVE **forces a specific maximum surface compactness**
$C_{max} = 2GM/(c^2 R)\big|_{max}$ for a **layered** self-gravitating object
consisting of a **Regime-IV (ruptured / melted-lattice) core** out to a
transition radius $r_t$, surrounded by a **Regime-III (near-yield elastic)
crust** to the surface $R$ — and whether the measured surface compactness of
the most compact known pulsars (PSR J0740+6620, $C \approx 0.47$–0.49) lies
**below** that forced max (→ corroborative / forward-prediction chord) or
whether **no such max is derivable** without positing a non-canonical EOS
(→ honest negative, EOS-gated).

## 1.5 Physical picture (mechanical, before equations)

- **Intact bound (canonical, closed):** the control parameter is the principal
  radial strain $\varepsilon_{11}(r) = 7GM/(c^2 r)$. It hits its **elastic
  yield** ($\varepsilon_{11} = 1$) at $r_{sat} = 7GM/c^2$. A star whose surface
  sits inside $r_{sat}$ has its *surface* strained past yield → its *surface*
  is already ruptured. That is the $2/7$ bound: it is a **strain-yield
  threshold**, NOT a Buchdahl pressure-divergence integral. (This is the first
  load-bearing distinction — see §2. The corpus *labels* it "AVE Buchdahl
  bound" but it is derived as a yield threshold, not as GR's Buchdahl
  pressure-central-divergence.)
- **Grant's insight (this session):** PSR J0740's surface is compactified
  *beyond* $2/7$ **because** it has a condensed/melted lattice core. So $C=0.47$
  is INSIDE the predicted-rupture regime — the canonical leaf already says such
  a star has a Regime-IV core + Regime-III crust. It is **corroborative, not a
  falsifier**, at the level of the intact bound.
- **The open question (this doc):** the melted core is a DIFFERENT medium
  (shear modulus $G_{shear}\to 0$; the lattice topology is gone). Does that
  medium have its OWN saturation ceiling — a strain (or density, or bulk-speed)
  limit — that, integrated over the layered profile, forces a NEW max surface
  compactness $C_{max}$ strictly between $2/7$ and GR's Buchdahl $8/9$? And is
  $0.47$ below it?
- **What scales how:** in the intact crust the strain is the $7GM/(c^2r)$
  refractive-gradient strain (Regime I–III). In the ruptured core the shear
  channel is dead ($G_{shear}=0$); what carries structural support is the
  **bulk-K channel** (the same channel whose rarefaction branch has the
  CANDIDATE cavitation floor $\bar\rho_{cav}=-1/\varphi$). The core is on the
  **compression** side of that bulk channel, not the rarefaction side.
- **Discrete onset:** the transition at $r_t$ is the $\varepsilon_{11}=1$
  shell (shear yield). The question is what the core does *between* $r=0$ and
  $r=r_t$ where $\varepsilon_{11}>1$ formally — the intact strain formula is
  out of its domain there.

## 2. How the intact 2/7 bound is actually derived (grounding)

Verified verbatim (`verify-before-cite`):

- `ave-compactness-limit.md:12` — *"The saturation condition
  $\varepsilon_{11}(r)=1$ defines … an absolute upper bound on the compactness
  … Since $\varepsilon_{11}=7GM/(c^2r)$, the saturation radius is
  $r_{sat}=7GM/c^2$."*
- vol3 ch15 tex:392 — *"Any static configuration with surface radius
  $R<r_{sat}$ has $\varepsilon_{11}(R)>1$, placing the surface inside Regime IV
  … The lattice cannot support strain beyond unity — the topology is
  destroyed."*
- `ave-bh-horizon-area-theorem.md:35` — factor $7 = 2/\nu_{vac}$; the Poisson
  ratio $\nu_{vac}=2/7$ (cited to "Vol 3 Ch 15:291-355 Buchdahl bound
  derivation").

**Key structural finding for this effort:** the AVE $2/7$ bound is a
**surface strain-yield threshold** ("$\varepsilon_{11}(R)<1$ so the surface
survives"), NOT a central-pressure-divergence Buchdahl integral. GR's Buchdahl
$8/9$ comes from requiring finite central pressure in a TOV integration of an
incompressible ($\nu=1/2$) star. The AVE bound uses the same $r_s/\nu$ Poisson
projection but stops at "does the *surface* yield," not "does the *center*
pressure-diverge." **This means the intact $2/7$ is a necessary condition on
the SURFACE, and says nothing yet about whether the layered INTERIOR admits a
static solution.** That is exactly the gap this effort probes.

## 3. THE LOAD-BEARING FORK — Regime-IV EOS (SURFACE TO GRANT)

The entire derivation hinges on one physics input the corpus does **not**
canonically pin: **the equation of state of the ruptured Regime-IV core.**

What the corpus HAS (verified):
- **Compression-side kernel** $S(A)=\sqrt{1-A^2}$, $c_{eff}^2 = c_0^2/\sqrt{1-A^2}$
  — the STIFFENING saturation kernel (`cavitation_flow.py:13` names it; wave
  speed *diverges* as $A^2\to1$). This is the **intact-lattice** approach to
  yield, on the compression side. At $A^2=1$ the lattice ruptures — but this
  kernel describes the medium *up to* rupture, not the ruptured medium itself.
- **Rarefaction-side EOS** $c_{bulk}^2 = c_0^2(1+\bar\rho/(1-\bar\rho^2))$
  softening to the CANDIDATE floor $\bar\rho_{cav}=-1/\varphi$
  (`cavitation_flow.py:22-26`) — but this is the RAREFACTION extreme (warp
  pocket / cavitation), the OPPOSITE sign from a compressed stellar core.
  Explicitly tagged **CANDIDATE / CONTESTED** (`lattice-extreme-bh-rationality.md:19,64`).
- **No canonical EOS for the ruptured-lattice (post-yield, $\varepsilon_{11}>1$)
  medium under COMPRESSION.** The manuscript says only that the interior is
  "similar to quark deconfinement" / "quark-gluon plasma or color-supercon-
  ducting phase" (ch15 tex:402) — a *physical analogy*, not an AVE-derived
  $P(\rho)$.

**Fork (the plumber-physical question for Grant):**

> The intact lattice STIFFENS as it approaches yield ($c_{eff}^2 = c_0^2/\sqrt{1-A^2}
> \to \infty$). But once it RUPTURES (Regime IV, $\varepsilon_{11}>1$, shear
> modulus $\to 0$), is the melted core **stiffer or softer** than the intact
> lattice — i.e. does the ruptured bulk-K medium resist further compression
> MORE (a hard floor, like the divergent stiffening extrapolated past yield →
> would force a max compactness ABOVE 2/7, a genuine chord) or LESS (shear
> gone, only bulk support, a soft plasma → the core would keep collapsing to
> the BH horizon $r_s=2GM/c^2$ with no intermediate static max → the only
> "max" is the BH limit itself, which is an echo of the horizon, not a
> distinct chord)?

Two readings, each with a different test outcome:

- **Reading A — RUPTURED CORE IS STIFF (hard bulk floor).** If the ruptured
  Regime-IV medium has a finite maximum sustainable density / minimum bulk
  wave-speed floor (an AVE-native analog of a hard EOS), then a layered TOV-like
  or energy-balance integration yields a **finite max surface compactness
  $C_{max}$ strictly in $(2/7,\, r_s\text{-limit})$**. If $C_{max}$ is a clean
  AVE-forced number (e.g. tied to $\nu_{vac}$, $\varphi$, or a K4 packing
  fraction) and distinct from Buchdahl $8/9$, and $0.47 < C_{max}$, that is a
  **forward-prediction chord**.
- **Reading B — RUPTURED CORE IS SOFT (plasma, no intermediate floor).** If the
  ruptured core cannot support itself against further compression (shear gone,
  bulk soft), there is **no static layered solution between $2/7$ and the BH
  horizon** — a compactified object either sits with an intact surface
  ($C<2/7$) or collapses through to $r_s$ (BH). Then the "max compactness for a
  ruptured-core star" is **not derivable as a distinct bound** — it degenerates
  to the horizon $2GM/c^2 R < 1$ (an ECHO of the Schwarzschild limit, which GR
  already has). Honest negative for the chord.

**I will NOT posit the Regime-IV EOS silently.** Per `pre-test-physics-check`
Step 4 + the flag-don't-fix directive, this fork is Grant's physics call. §4
below scaffolds the layered solve *parametrically in the core stiffness sign*
so that when Grant collapses the fork, the answer falls out immediately — but
the headline verdict (chord vs echo vs negative) is GATED on his ruling.

## 4. Method (substrate-native-check walk)

- **CP1 (dynamics):** the intact bound is NOT a minimization and NOT a
  pressure-balance integral — it is a strain-yield threshold. So for the
  *intact* piece there is no TOV. For the *layered* piece, hydrostatic balance
  is only meaningful if the core has a well-defined $P(\rho)$ (the §3 fork). A
  real-space Cartesian TOV is a borrowed-GR tool; I will use it ONLY as a
  cross-check and flag it as non-native.
- **CP2 (sector):** this lives in the **bulk-K + shear** gravitational sector
  (Regime III crust = near-yield elastic shear; Regime IV core = bulk-K only,
  shear dead). NOT the V-sector electron phase-space. Real-space radial profile
  IS the matching coordinate here (this is a macroscopic strain field, not a
  phase-space topology claim) — CP4 satisfied: real-space is correct.
- **CP3 (objective):** AVE-native objective is "at what surface compactness does
  the layered strain profile first admit no static configuration" — a
  yield/saturation-boundary question, rendered as a **boundary condition**
  ($\varepsilon_{11}=1$ shell at $r_t$; core EOS floor), NOT a bulk confining
  force (CP10).
- **CP7 (sampling):** N/A (analytic/1-D radial), no PML, no top-K.
- **CP10 (boundary-not-bulk):** the rupture at $r_t$ is a phase-boundary
  ($G_{shear}\to0$, $\Gamma_{shear}=-1$), rendered as an interface condition,
  not a bulk force term.

**Concrete solve plan (parametric in the §3 fork):**
1. Reproduce the intact $2/7$ as a sanity check (must recover exactly).
2. Model the layered profile: core $[0,r_t]$ with a **parametrized** core EOS
   (stiffness parameter $s$: $s\to\infty$ = hard floor = Reading A;
   $s\to 0$ = soft plasma = Reading B), crust $[r_t,R]$ with the near-yield
   elastic strain law $\varepsilon_{11}=7GM(r)/(c^2 r)$.
3. Sweep $s$ and read off $C_{max}(s)$. Locate where (if anywhere) a finite
   $C_{max}\in(2/7, 1)$ appears, and its value at the two limits.
4. Overlay PSR J0740 ($C\approx0.47$–0.49) and Buchdahl $8/9$.
5. Report $C_{max}$ as a **function of the fork**, with the headline verdict
   deferred to Grant's collapse of the fork.

## 5. Pre-committed classification (consistency-vs-emergence)

- If **Reading A** yields a clean $\nu_{vac}$/$\varphi$-tied $C_{max}$ distinct
  from Buchdahl AND $0.47<C_{max}$: **candidate Class D emergence / forward
  prediction** (a forced dimensionless bound from substrate primitives, testable
  by compactness measurements) — but only if the core EOS floor is itself
  axiom-derived, not posited. If the floor is posited → drops to Class C at best.
- If **Reading B**: the "bound" degenerates to the Schwarzschild horizon
  $2GM/c^2R<1$ → **Class A/echo** (GR already has this; not AVE-distinct).
- If the fork cannot be collapsed / no canonical Regime-IV EOS: **NOT-DERIVABLE
  negative**, reported as such (EOS-gated). This is the most likely honest
  outcome absent a Grant ruling.

## 6. Discriminating outcomes (frozen)

- **Outcome A (chord):** Grant rules core is STIFF + a clean AVE-forced
  $C_{max}\in(2/7, 8/9)$ falls out, $0.47<C_{max}$, distinct from Buchdahl.
  → forward-prediction chord; the most-compact-pulsar compactness ceiling is a
  test.
- **Outcome B (echo):** ruptured-core max degenerates to the $r_s$ horizon
  → echo of Schwarzschild, no distinct chord.
- **Outcome C (EOS-gated negative):** no canonical Regime-IV EOS; $C_{max}$ not
  derivable without positing one → honest negative, fork surfaced to Grant.
- **Outcome D (falsifier):** a forced $C_{max} < 0.47$ would FALSIFY — it would
  mean AVE forbids PSR J0740's measured compactness. (This would be the
  discriminating chord in the *dangerous* direction and must be reported
  loudly if it appears.)

**Falsifier of my own framing:** if the intact $2/7$ turns out NOT to be a
surface-yield threshold but a genuine central-pressure Buchdahl integral (i.e.
I misread §2), the whole layered reframing is moot — the bound would already be
the interior bound. I checked (§2): it is a surface-strain threshold. If a
reviewer shows otherwise, this prereg is void.
