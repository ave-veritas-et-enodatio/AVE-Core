# Crystal-Graft v4 — the photon's helicity IS the winding (PREREG, frozen before the full run)

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-graft-v4-photon-helicity` · **Lane:** implementer
**Base:** `analysis/2026-06-09-crystal-graft-v3` (`4627651a`, Outcome C after the B→C adversarial demotion)
+ locally merged `analysis/2026-06-09-genesis-perf-utils` (parallel arm-runner + bit-identical fast extractor).
**Engine (new):** `src/ave/core/crystal_graft_v4.py` · **Driver (new):** `src/scripts/vol_1_foundations/crystal_graft_v4_run.py`
**CI gate (new, hardened):** `src/tests/test_graft_v4_alpha_free.py`

## §0 — Grant adjudication (2026-06-10, the twist question) — RECORDED VERBATIM

> Asked: "is the poloidal '3' the photon's own conserved twist (energize+lock — confinement CONVERTS the
> photon's helicity into the winding), rather than anything a source grows or a template imprints?" —
> **Grant: "proceed" on that recommended framing.**

So v4 tests a CONSERVATION statement: **the electron's spin IS the photon's spin, trapped.**
`ave-conserved-vs-pumped` applied to the TOPOLOGY itself — the winding is ENERGIZED from the photon's
conserved helicity and LOCKED; never grown, never template-imprinted, never dialed.

## §0.1 — What v3 left fatal (the two lenses this build targets)

The graft-v3 adversarial panel demoted B→C on two FATAL lenses (`2026-06-09_crystal-graft-v3_result.md`):
1. **The source was DECOUPLED from the photon.** v3's director `b_λ` was a FROZEN, DIALED template; its
   handedness χ was a SOURCE INPUT. The `no_photon_null` arm was BYTE-FOR-BYTE identical to signal — the
   photon carried nothing. → CHANGE 1.
2. **The LOCK was UNBUILT.** Only the energize half existed; `|L_ω|` pumped unbounded `t^0.43`, and even the
   χ=0 / zero-helicity arm pumped `|L_ω|` to 347.7 — a PUMP, not a conserved knot. → CHANGE 2.
   Plus the v3 probe (`2026-06-09_extractor-poloidal-misread_note.md`): the de-novo read was at r≈1.1 cells,
   BELOW the extractor's poloidal-resolution floor → every de-novo `w_pol` verdict was VOID. → RESOLUTION GATE.

## §1 — The two physics changes (everything else carried forward from v3/v2/CrystalEngine unchanged)

**CHANGE 1 — χ-FROM-PHOTON (kills the template).** Replace the frozen Beltrami director `b_λ` with the
photon's OWN evolved shear field `w`. A circularly-polarised photon IS a force-free Beltrami field
(`∇×w=±k·w`, A∥B) — the SAME A∥B object v3 used, but its handedness is now PHYSICALLY the photon's helicity,
not a dialed input. Derived ground-up (the brief's `h_loc=ω·∇×ω` candidate is a suggestion, not a mandate):

```
H_couple = κ̃ ∫ g_wall(r) · V · [ w · (∇×ω) ] d³r ,   κ̃ = pq/(p+q) = 6/5  (α-FREE)
  f_V = −δH/δV = −κ̃ g_wall [ w·(∇×ω) ]            (back-reaction ω→V)
  f_ω = −δH/δω = −κ̃ ∇×( g_wall·V·w )               (BUCKLE: compression→ω, DIRECTOR = live photon w)
  f_w = −δH/δw = −κ̃ g_wall·V·(∇×ω)                 (photon depletion / absorption — see §1.1)
```
Automatic consequences (VERIFIED, not assumed): (a) **no-photon ⇒ w=0 ⇒ f_ω≡0 ⇒ ω=0 ⇒ H_bel=0** — the
no-photon control is null BY PHYSICS, v3's byte-identical failure is IMPOSSIBLE; (b) **handedness from the
photon** — for a CP photon ∇×w=±kw ⇒ ω∝∇×(gVw)∝∇×w ⇒ ∇×ω∝w ⇒ `H_bel=∫ω·(∇×ω)∝∫(∇×w)·w` = the photon's OWN
helicity density; **no dialed χ anywhere**; (c) **zero-helicity (linear-pol) photon** has net `∫w·(∇×w)=0`
⇒ no chirality input ⇒ no net winding, no net charge while depositing comparable ENERGY (the sharpest control).

### §1.1 — The depletion term `f_w` is an INDEFINITE pump (frozen finding, run as the DETONATION CONTRAST)
The full trilinear coupling (with `f_w` ON) conserves the continuum energy but is an INDEFINITE Hamiltonian
(linear in each field, unbounded below); its discrete dynamics DETONATE (H_photon, H_bel, |L_ω| runaway —
verified, `photon_deplete=True` arm). The lock cannot arrest an indefinite-Hamiltonian runaway. An indefinite
coupling is NOT substrate-native (a real bounded medium). So the OPERATIVE engine drops `f_w`
(`photon_deplete=False`): the live photon `w` is a BOUNDED chiral DIRECTOR (coupling bilinear in the dynamical
pair (V,ω), stable), χ-from-photon WITHOUT the pump. The `photon_deplete=True` arm is reported as the
documented detonation contrast (ave-conserved-vs-pumped: the pump is named, not hidden). **Consequence for the
ledger:** without 1:1 depletion the photon is a non-depleting chiral source, so the ledger's "input=trapped"
closure is an OPEN empirical question (measured, not engineered).

**CHANGE 2 — THE LOCK (the gyroscope's missing half).** Woltjer/Taylor selective decay toward the force-free
A∥B Beltrami state, rendered DISCRETE-STABLE. The literal `∂_tω=η(λ∇×ω−∇×∇×ω)` flow DETONATES (curl-of-curl
Nyquist null space — verified H_bel 9.5→4.9e5 in 300 steps). The poloidal "3" lives in the LOCAL (ω,π_ω) LC
quadrature; the runaway is a GLOBAL rigid rotation (|L_ω| pumping). They are SEPARABLE, so the lock removes
only a fraction η of the rigid-body rotation Ω×r (Ω=I⁻¹L_ω):

```
π_ω ← π_ω − η·(Ω×r)          ⇒   L_ω ← (1−η)·L_ω   (EXACT per-step contraction)
```
SATURATES |L_ω| WITHOUT bleeding the LC quadrature (a plain velocity damp drives π_ω→0 and KILLS the poloidal
winding — verified (2,3)→(2,1) collapse, the load-bearing v4 lesson). `lock_OFF` is the v3-behaviour contrast.
**η=0.05 is FROZEN** from the saturation smoke (gives the doubling-ratio→1.00); tuned ONCE on the lock, never
on a de-novo arm.

### Substrate-native-check (walked before scaffolding)
- **CP8** the de-novo arms seed only the GENERATIVE PRECURSOR (photon + pre-compressed dilatation); the planted
  (2,3) is a CARRIER-GATE diagnostic only (lock smoke + resolution gate), clearly labeled.
- **CP9** ω and the deposited helicity are dynamically EVOLVED; the director is the LIVE evolved photon (NOT a
  frozen template — that is the whole point of CHANGE 1); the lock is a dynamical relaxation, not the answer.
- **CP10** the buckle is boundary-localized at the frozen Γ=−1 wall shell `g_wall`.

## §2 — Frozen gates (each CAN fail; STOP + localize honestly on a smoke failure)

**LOCK BEFORE SOURCE — the smoke ladder runs FIRST, in this order; a fail STOPS the run:**
- **LOCK SMOKE (the prerequisite):** plant a (2,3) at a RESOLVABLE scale (r≳3 cells), run 500+ live steps with
  source ON + lock ON; the planted (2,3) must SURVIVE (read back (2,3), is_2_3). If it cannot, **verdict
  LOCK-FAIL**, localize, report. (v3 destroyed it: (2,3)→(2,1).)
- **INDEPENDENCE + POSITIVE CONTROL:** the real photon-director arm's winding INTEGER is robust under a V
  perturbation (ω is an independent carrier) AND an explicitly SLAVED arm (ω:=F(V) overwritten each step) is
  FLAGGED False by the SAME gate (demonstrated reachable-False — v3's gate could not fail, an auto-VOID
  condition this removes). If the gate cannot flag the slaved arm → auto-VOID.
- **RESOLUTION GATE:** the de-novo torus minor radius r ≳ 3 cells AND plant-(2,3)-at-the-de-novo-scale →
  read-(2,3). A de-novo read at unresolvable scale is VOID. (Config N=72 frozen below gives de-novo r≈3.5.)
- **SATURATION (STOP gate):** |L_ω|_max doubling ratio (L,2L,4L) → 1.0 (tolerance ≤1.3) on the frozen wall;
  recorded on ALL arms incl χ-null/no-photon + a LIVE-wall case; H_total(t) + |L_ω|(t) on the operative
  nonlinear run. (v3's gate passed unbounded t^0.43 — demoted; this is a real STOP gate.)

**α CI gate (HARDENED, separate test):** AST scan of the engine CHAIN + the DRIVER for `ast.Import`,
`ast.ImportFrom`, attribute access (`constants.ALPHA`), and bare CODATA literals; assert
`ALPHA_COLD_INV`/`PHI`/`RR_GOLDEN_TORUS` never enter engine STATE.

**EMF reciprocal:** default-OFF. Its conservative-vs-pump contradiction is a separate Grant adjudication
(flagged in Vol-9); **v4 does NOT use that channel** (`converter_on=False` inherited; only the photon-director
buckle + lock).

**FROZEN CONFIG (FIXED across all compared arms):** N=72, S_min=2e-3, A_cap=0.999, ω_gap=1.0, wall_center=0.62,
wall_width=0.30, κ̃=6/5, pml=6, lock_eta=0.05; breather σ=14 frac=0.999; photon σ=9 λ=10 amp=0.35; n_steps=1200.

## §3 — The HEADLINE measurement (the conservation test) + provenance

**The HELICITY LEDGER:** `H_photon(t=0)` vs `H_bel(trapped, end)` vs `H_photon(residual, end)` vs
`H_radiated = input − trapped − residual` (boundary deficit). Does the photon's helicity SURVIVE absorption as
the trapped winding (input ≈ trapped + residual, to tolerance)? PLUS:
- **w_pol ≈ 3 de-novo** on a RESOLVABLE, alias-checked contour (no plant, CP8)?
- **Provenance:** flipping the PHOTON's helicity flips everything downstream (trapped H_bel sign, charge,
  w_pol sign); the **zero-helicity arm** gives null winding + null charge while depositing comparable energy.

## §4 — A/B/C adjudication (Rule 11, no debug-toward-A; written BEFORE the run; a false-positive is worse than C)

- **A — the photon's helicity converts + locks (the conservation-genesis CANDIDATE, panel decides):** the
  ledger closes to tolerance (trapped ≈ input); `w_pol≈3` de-novo on a resolvable contour; charge + w_pol sign
  trace to the photon; zero-helicity arm null; lock saturates →1.0; all gates falsifiable-and-passed; α-guards
  green.
- **B — REAL PROGRESS (report honestly as B):** the helicity ledger closes (trapped H_bel = photon's,
  sign-traced, locked + saturating) but the (2,3) does NOT close as integer winding (w_pol partial /
  non-integer / sub-gate at resolvable scale) — the conversion is real, the knot-closure ingredient is the
  localized residual.
- **C — the helicity does NOT survive** (radiates / cancels; trapped H_bel ≁ photon's), OR the lock fails the
  planted-knot smoke (LOCK-FAIL), OR a fatal gate fires (VOID).

**Expected-honest prior (recorded so the run can surprise it):** CHANGE 1 should deliver the no-photon-null-
by-physics + sign-provenance + zero-helicity-null cleanly (a genuine repair of the v3 fatal lens). The ledger
MAGNITUDE closure is uncertain (no depletion term — §1.1); the de-novo poloidal "3" likely still does not
self-assemble from a photon-director source (v3's w_pol=0 residual). Most-likely honest landing: **B on the
conversion + sign-provenance, with the (2,3) integer-closure as the localized residual** — unless the de-novo
poloidal fibre genuinely fires. **I will not debug toward A.**
