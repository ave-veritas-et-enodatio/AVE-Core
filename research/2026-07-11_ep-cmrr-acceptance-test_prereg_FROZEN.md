# EP-CMRR acceptance test — FROZEN prereg (U5, engine-refresh batch)

**Freeze discipline.** This prereg is frozen **by push**: it is pushed as its own
commit BEFORE the driver/test code exists (the `tethered_pivot_x34b.py` pattern;
methods P9–P11 addendum, PR #622). The freeze is claimed by commit ordering — the
prereg commit precedes and is pushed ahead of the test-code commit. Bins below are
frozen; per the P12 addendum (#622) **frozen bins enforce, flags don't**.

**Class.** Consistency / certification. **No chord mint** — per P10 (below) this
test CERTIFIES-AND-EXPOSES an installed keying's EP-status; it CANNOT adjudicate
which keying is physical (X36 install-tautology).

---

## Sector header (mandatory — substrate-native-first)

- **SECTOR** = A1 dilatation / gravity — the longitudinal-bulk `V` scalar
  (`src/ave/core/crystal_engine.py:18-20`, NO-QED directive).
- **Does the engine carry the DOF?** YES — the certified Master-Equation medium
  (`src/ave/core/master_equation_fdtd.py`) is the A1 bulk-trap (the scalar `V`
  field + the `S(A)=√(1−A²)` saturation kernel, `:156-161`).
- **REGIME** = sub-yield (linear, `S(A)≈1`; NOT the near-yield saturated regime).
  `V` is held sub-yield (`|V|<V_yield`) throughout so `c_eff` stays finite/stable.
- **DRIVE** = **uniform (common-mode)** vs **tidal / gradient (differential)**.
- **Kernel variable = strain, NOT force magnitude.** In the equivalence-principle
  reading the strain that loads the kernel is the **DIFFERENTIAL** deformation of
  the response — the relative displacement between neighbouring nodes, i.e. the
  spatial **gradient** `∇V` of the body-force response — NOT the absolute field
  `|V|` and NOT the drive magnitude `|g|`. A rigid translation (uniform
  displacement) has zero differential strain. **That distinction is the whole
  content of U5.**

> **flag-don't-fix (surfaced, not resolved).** The engine's literal
> `saturation_kernel(V)` keys on the per-cell **absolute** `|V|` (`:156-161`).
> Under a *sustained uniform* body-force drive the absolute field itself grows
> (`V = ½·f·t²`), so a raw `|V|`-keyed kernel is common-mode-SENSITIVE in exactly
> the same way a `|g|`-keyed kernel is. The substrate-native, EP-correct strain
> is the **differential** `∇V`. This test keys the certified leg on the
> differential strain `A_strain = |∇V|·dx/V_yield` (the EP-correct variable) and
> feeds it through the certified `√(1−A²)` kernel form. **Whether the bulk-sector
> kernel should key on `|V|` or on `∇V` is a KB/Grant physics question this test
> EXPOSES but does not adjudicate** (P10 / X36 install-tautology). Surfaced to the
> KB owner; no reconciliation picked here.

---

## The instrument

A differential-pair unit test in the Vol9-Ch17 acceptance style
(`src/tests/engine_acceptance/`; `sup-`-node discipline per INVARIANT-S9/S10 — a
simulation is a `sup-`, never an `exp-`), on the **certified Master-Equation
medium** (`src/ave/core/master_equation_fdtd.py`).

**Body-force driver (Rule-10 empirical driver).** The drive enters the certified
leapfrog as a body-force source `f(x)` on the RHS of the Master Equation
(`∂²V/∂t² = c_eff²·∇²V + f`): `V_new = 2V − V_prev + dt²·(c_eff²·∇²V + f)`. The
driver **REUSES the certified primitives verbatim** (`eng.c_eff_squared`,
`eng._laplacian`, `eng.saturation_kernel`) — it reimplements no stencil, stepper
or kernel (Rule-14 anti-rebuild). The engine module is **NOT modified**; the
body-force source is applied in a test-side helper (`_ep.py`).

**Strain observable (the EP-correct differential).** After evolving `n_steps`,
read the per-cell differential strain on the **PML-excluded deep interior**
(Rule-10 PML-exclusion corollary): `A_strain(x) = |∇V(x)|·dx / V_yield` via
central differences. `S_strain = √(1−A_strain²)` clipped (the certified kernel
form, exercised through `eng.saturation_kernel`).

**Smooth-drive note.** Both drives (uniform, linear-gradient) satisfy `∇²V = 0`
for their analytic particular solution `V_p = ½·f(x)·t²`, so they launch **no
propagating wave** — the response is the (analytically exact) rigid/tidal profile,
and the deep-interior strain read is clean. This is a non-propagating quasi-static
response, not a wave-propagation test.

---

## LEG definitions + PRE-REGISTERED BINS

Let `t = n_steps·dt`, `V_yield = 1` (natural units), drive along one axis, read at
the box centre (deep interior, PML-excluded).

### LEG-A — common-mode (uniform body force), strain-keyed / certified

Apply a **spatially-uniform** body force `f(x) ≡ f_0` (small: `V_center = ½f_0t²`
held `< 0.5·V_yield`). The translation-invariant medium accelerates **rigidly** →
uniform response → **zero differential strain**. A strain-keyed kernel does not
load: `S_strain ≡ 1` → **CMRR infinite by construction**.

- **PASS:** deep-interior `A_strain_A < 1e-3` (rigid; strain ~ integrator floor)
  AND `min S_strain_A > 0.999` AND `CMRR = A_strain_B / max(A_strain_A, 1e-12) > 1e3`.
- **FAIL:** `A_strain_A ≥ 1e-3` (a uniform drive spuriously loads a strain-keyed
  kernel — the medium is NOT translation-invariant / the strain read is wrong).

### LEG-B — differential (gradient / tidal body force), strain-keyed / certified

Apply a **pure gradient** body force `f(i) = γ·(i − i_center)` (zero at centre) →
strain `∝ γ` (the tide). `γ` is set **analytically** to target
`A_strain_B ≈ 0.2` (`γ = 0.4·V_yield/t²`, from the closed form
`A_strain_B = γ·t²/(2·V_yield)`) — a computed INPUT, not a tuned output.

- **PASS:** measured `A_strain_B` within **5%** of the analytic target `0.2`
  (dynamics reproduce the closed-form tide) AND `min S_strain_B < 0.999` (the
  kernel measurably LOADS on genuine differential/tidal strain — not trivially
  null).
- **FAIL:** measured `A_strain_B` off target by ≥ 5% OR `min S_strain_B ≥ 0.999`
  (the kernel fails to load on a real tide).

### P11 sabotage arm — deliberately key the kernel on `|g|` (force magnitude)

Plant a **common-mode-sensitive** coupling: key the kernel on the drive magnitude,
`A_sab(x) = |f(x)|/f_yield`, with `f_yield = |f_0|/0.3` (so `A_sab ≈ 0.3` under the
uniform drive). Under **LEG-A's uniform** drive, `|f| ≡ |f_0|` everywhere, so the
sabotaged kernel loads: `S_sab ≈ √(1−0.3²) ≈ 0.954 < 1`. **LEG-A must FIRE.**

- **PASS (instrument certified):** on the sabotage arm, LEG-A **fires** —
  `min S_sab < 0.99` (loading detected under the common-mode drive). The test
  correctly flags the WEP-violating keying.
- **FAIL:** `min S_sab ≥ 0.99` (the instrument failed to detect a planted
  common-mode-sensitive keying — it cannot tell WEP-exact from WEP-violating).

**Instrument is CERTIFIED iff all three pass:** LEG-A passes on the strain-keyed
medium (WEP-exact, infinite CMRR), LEG-B loads on the strain-keyed medium (not
trivially null), AND the P11 `|g|`-keyed arm fires LEG-A (the teeth: it detects a
WEP-violating keying).

---

## P10 — honesty framing (binding; stated verbatim)

**This test CERTIFIES-AND-EXPOSES; it does NOT adjudicate T4.** Per the **X36
install-tautology** (`research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`:
"the engine returns whatever node model is installed; it cannot adjudicate the
fork by itself") the engine returns whatever keying is installed — the test's
value is making the **installed keying's EP-status VISIBLE**, not deciding which
keying is physical.

Concretely: the banked **galactic `η_eff(g_N)`** MOND keying (T4,
`_orchestration/2026-07-10_rulings-docket.md` four-lane continuation §A T4 row; the
surviving branches are acceleration-keyed after the tide sub-branch's X43-A0
dimensional kill), installed as **local-`|g|` keying, will FAIL LEG-A BY DESIGN of
MOND phenomenology** — `a₀` is a *local-acceleration* scale, and a uniform
body-force drive produces uniform `|g|`, so a `|g|`-keyed kernel loads under
common-mode. **That LEG-A failure is the honest EXPOSURE of a WEP-violating
keying, NOT a bug or a defect of the test.** The P11 sabotage arm above IS this
`|g|`-keyed / MOND-class exposure in miniature. The test cleanly separates a
**strain-keyed medium** (WEP-exact, LEG-A passes) from a **`|g|`-keyed medium**
(WEP-violating, LEG-A fires) — that IS its whole content.

**CMRR ↔ EP identity (context, not a claim minted here).** CMRR is infinite BY
IDENTITY for a strain-keyed medium: gravitational charge ≡ inertial mass, nothing
to mismatch under a common-mode (uniform) drive; the **tide is the differential
mode**. Spec anchors (register, U6): WEP-CMRR ~1e-15 (Eötvös / MICROSCOPE),
SEP-CMRR ~1e-4 (LLR-Nordtvedt).

---

## Runtime / scope

Target **seconds, not minutes** (the acceptance suite already presses the CI
ceiling): modest cube `N`, ~10² steps, three legs. Runtime recorded in the batch
result doc. No new substrate-physics claim; `mass = A1` (PR#260/#311) untouched.
