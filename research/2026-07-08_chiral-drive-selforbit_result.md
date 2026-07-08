# Chiral-drive self-orbit — RESULT: a CURL flux drives a persistent LOSSLESS self-orbit; a pure-gauge GRADIENT does not

**Date:** 2026-07-08 · **Branch:** `analysis/chiral-drive-selforbit` · **Base SHA:** `5219a0b0aa0e12b10d5a6838c56b383892b9d35b`
**Prereg (FROZEN, precedes this run):** [`research/2026-07-08_chiral-drive-selforbit_prereg.md`](2026-07-08_chiral-drive-selforbit_prereg.md)
**Module:** [`src/ave/solvers/chiral_drive_selforbit.py`](../src/ave/solvers/chiral_drive_selforbit.py) ·
**Driver:** [`src/scripts/vol_2_particle_physics/chiral_drive_selforbit_run.py`](../src/scripts/vol_2_particle_physics/chiral_drive_selforbit_run.py) ·
**Test:** [`src/tests/test_chiral_drive_selforbit.py`](../src/tests/test_chiral_drive_selforbit.py) ·
**Results:** [`results/chiral_drive_selforbit_results.json`](../results/chiral_drive_selforbit_results.json) ·
**Figure:** `research/figures/2026-07-08-chiral-drive-selforbit/chiral_drive_selforbit.png`

## HEADLINE VERDICT — **[CHIRAL-DRIVE-VIABLE]** (mechanism plausible) — with a load-bearing HONEST-SCOPE caveat

A **CURL**-type chiral bias (a nonzero plaquette/loop flux, ∮θ≠0) DOES drive a **persistent,
LOSSLESS** self-orbit of the (2,3) loop; the **GRADIENT** control (pure gauge, ∮θ=0, EQUAL per-link
magnitude) does **NOT**; the circulation is machine-precision **conservative**; the DC inter-node
mismatch tracks the circulation energy via a clean **E_circ ∝ M²** law (R²=1.000000). Every
anti-tautology gate is green. **The mechanism works.**

**BUT (the caveat that keeps this honest):** the discriminator is largely **EXPECTED-MATH** (on a
ring it is a mathematical fact that a pure gauge cannot drive a gauge-invariant current while a flux
can — the Aharonov–Bohm / persistent-current result), and the flux **VALUE** is a **FREE / IMPORTED
knob** (the canonical chiral flux θ_χ=2π·ν_vac has ν_vac=2/7 = GR-imported). So the ω_C-rate is
**NOT forced** — this is a **MECHANISM** result, **NOT** an m_e derivation. The chord potential lives
in the mechanism + the DC-mismatch observable, **not** the value.

## Per-arm results (verbatim from `results/chiral_drive_selforbit_results.json`, N=64, 6000 steps)

| Arm | Observable | Number | Bin |
|---|---|---|---|
| **1 CURL / rate law** | `C_dc(uniform) == 2t·sin(Φ/N)` | max abs err **1.33e-13**; slope(C vs Φ) 0.0312 | rate set by flux ✅ |
| **2 GRADIENT control** | curl `C_dc`=**0.09751** vs gradient `C_dc`=**−2.70e-15** | curl ∮θ=π, gradient ∮θ=**0.0** | gradient NULL ✅ / curl drives ✅ |
| **3 CONSERVATIVE** | curl H-drift **1.06e-12**, norm-drift **5.30e-13** | Cayley-unitary | LOSSLESS ✅ |
| **4 MASS OBSERVABLE** | `E_circ ∝ M^`**2.0011** (R²=**0.99999991**); bias-off C_dc=−3.2e-15, M_dc=−9.3e-17 | expected 2.0 | tracks ✅ / bias-off NULL ✅ |
| **5 A1 sourcing (proxy, sat-ON)** | curl PR=**0.5476** vs off PR=**0.5380** (curl LESS localized) | rho-peak curl 0.0430 < off 0.0446 | **NULL — no extra trapping** ⚑ |

### THE DISCRIMINATOR (RETURN item 5)
- **Curl circulation rate vs flux:** the uniform-seed persistent current equals `2t·sin(Φ/N)` to
  **1.33e-13** across Φ∈[0,2π] — linear in Φ at small flux (slope 0.0312 ≈ 2t/N=0.03125), the
  cyclotron-like rate∝flux law. The localized (emergence) seed gives the SAME DC-average (green
  squares sit on the anchor line, figure Panel A).
- **Gradient result (MUST be null):** `C_dc = −2.70e-15`, `M_dc = −7.67e-17`, Wilson loop ∮θ=**0.0**
  exactly. Ratio curl/gradient ≈ **3.6e13**. **The kill-test passes: the pure gauge is inert.**

### CONSERVATIVE CHECK (RETURN item 6)
Curl-run **H-drift = 1.06e-12**, norm-drift = 5.30e-13 (linear discriminator, exact-unitary Cayley).
No damping term is representable in the scheme, so the self-orbit is not bought by dissipation.

### MASS OBSERVABLE (RETURN item 7)
`E_circ(Φ) = ⟨H⟩_DC(Φ) − ⟨H⟩_DC(0)` vs the DC inter-node mismatch `M`: **E_circ ∝ M^2.0011,
R²=0.99999991** — the kinetic-from-circulation square law (energy ∝ momentum²). **Bias-off (Φ=0) →
C_dc, M_dc, E_circ all ≈ 0** (liveness). This is the "mass = DC network mismatch" readout with a
definite quadratic law.

### A1 SOURCING (RETURN item 8) — **NULL** (honest negative)
Under the √(1−A²) saturation (A_yield=1), the curl circulation does **NOT** produce more density
localization than bias-off (curl participation-ratio 0.548 > off 0.538 ⇒ curl is slightly *less*
concentrated; it transports the bump rather than trapping it, figure Panel C). **So in this minimal
harness the mechanism does NOT source an A1 dilatation.** ⚑ **HONEST WOBBLE:** this harness has **no
genuine A1 (dilatation) sector** — it is a single-grade Cosserat-ω-analog LC ring, so the A1 arm can
only read a density proxy, and the proxy is null. A real A1-sourcing test needs the two-sector engine
(the bulk-V ⊗ shear-ω crystal). Reported as NULL-with-caveat, not inflated.

### FORCED-vs-FREE (RETURN item 9) — **FREE / IMPORTED KNOB**
The circulation rate in engine-natural units is `I_ring(Φ)=2t·sin(Φ/N)/N` — set by the **free**
hopping scale `t` AND the flux `Φ`. The canonical chiral flux value **θ_χ=2π·ν_vac = 1.7952 rad**
(3-port loop reference 3θ_χ=5.3856 rad) has **ν_vac=2/7 = GR-imported** (`constants.py:381`; a
one-parameter family, not lattice-forced). **⇒ the ω_C-rate flux is NOT forced** — both the rate
scale and the flux value are free/imported. This exactly reproduces the node-circulator
**IMPOSED-AT-MAGNITUDE** verdict (`research/2026-06-20_node-circulator-coupling.md:152`).

## VERDICT + one-mechanism explanation (RETURN item 10)

**[CHIRAL-DRIVE-VIABLE].** ONE mechanism explains every reading: **a curl (∮θ≠0) is a genuine gauge-
invariant flux and drives a persistent gauge-invariant current; a pure gauge (∮θ=0) is not physical
and cannot.** That single fact routes Arm 1 (curl drives, rate∝flux), Arm 2 (gradient null), Arm 4
(E_circ∝M², the current's kinetic energy), and — because the generator is Hermitian and the
integrator is the Cayley transform — Arm 3 (lossless). The one arm it does **not** deliver is A1
sourcing (Arm 5, null) — because the harness carries no dilatation DOF for the circulation to source.

**What this DOES establish (the AVE-content, beyond textbook AB):**
1. Such a self-orbit can be **genuinely LOSSLESS** (Ax3-compatible) — not a priori guaranteed.
2. The (2,3) loop **supports it stably** — no dispersion / NO-SOLITON over the window.
3. A definite **mass-observable law E_circ∝M²** (the DC-mismatch network readout).
4. chirality→curl is **corpus-established** (node-circulator 3χθ_χ loop flux) ⇒ this IS the drive the
   just-closed electron-lock arc (five negative loci, no chiral term) never had.

**What it does NOT establish:** an m_e value (echo), or that the mechanism sits behind mass=A1
(A1-sourcing null in this minimal harness — mechanism stands as a distinct circulation-energy route,
NOT shown to reconcile with canon #260 here). **flag-don't-fix:** whether chiral-driven circulation
sources A1 is UNRESOLVED and needs the two-sector engine — surfaced, not silently closed.

## Anti-tautology gate statuses (RETURN item 11) — ALL GREEN
- **EMERGENT-not-PLANTED:** seed circulation at flux-OFF = 0.0 (localized AND uniform). The
  circulation appears ONLY under the flux; no spinning loop was planted. ✅
- **BIAS-OFF NULL (liveness):** Φ=0 ⇒ C_dc=−3.2e-15, M_dc=−9.3e-17. ✅
- **GRADIENT CONTROL:** ∮θ=0 at equal per-link magnitude ⇒ C_dc=−2.7e-15. ✅ (the kill-test)
- **CONSERVATIVE:** H-drift 1.06e-12, no damping term in the Cayley scheme. ✅
- **PHASE-SPACE COORDINATE (A46):** circulation read as winding of arg(ψ) on the LC quadrature, ∮
  around the PHYSICAL (2,3) ring (Wilson loop), never a Cartesian square. ✅

## Honest wobbles (RETURN item 13)
1. **The discriminator is partly EXPECTED-MATH.** curl-drives / gauge-doesn't is a mathematical fact
   on a ring (like charge-quantization's "topological invariance is expected math"). The test's
   genuine content is losslessness + the E_circ∝M² law + stability + the corpus chirality→curl link,
   NOT "AB physics works."
2. **A1-sourcing NULL is harness-limited,** not a clean physics negative: the minimal ring has no
   dilatation sector. Whether chiral circulation sources A1 stays OPEN (needs the two-sector engine).
3. **Saturation-ON energy drift = 8.7e-3** (Arm 5, Picard corrector is first-order; bounded, no
   runaway). The PRIMARY discriminator (Arm 1–4) is the LINEAR run at machine precision — the
   saturation arm is secondary and its larger drift does not touch the verdict.
4. **The flux VALUE is an echo** (θ_χ from ν_vac=2/7 GR-imported). The single-ring Wilson loop is the
   complete gauge-invariant curl content of *a loop*; the plaquette-resolved torus-surface
   generalization is named OUT-OF-SCOPE (frozen in prereg §5), not smuggled in.

## Corpus-state updates queued (implementer SURFACES; auditor LANDS)
- **`research/2026-06-20_node-circulator-coupling.md`** — this result CORROBORATES its
  IMPOSED-AT-MAGNITUDE finding on a NEW apparatus: the chiral CURL flux drives a real, lossless
  persistent circulation, but its magnitude is a free/imported knob (ν_vac=2/7). No status change to
  node-circulator; cross-link as an independent confirmation of the echo-at-magnitude.
- **The electron-lock arc close** (`research/2026-07-08_electron-lock-arc_CLOSE.md`) — the five loci
  lacked a chiral drive; this shows the chiral curl DOES drive a lossless self-orbit, but it is a
  MECHANISM (value=echo), not a rescue of the m_e value. Whether it should re-open any locus is a
  Grant/auditor call — SURFACED, not decided here.
- **No new axiom, no Ax-5 draft** (A44 / Rule 16): the residual (does chiral circulation source A1) is
  an engine coverage gap needing the two-sector engine, NOT a missing postulate. Surfaced for Grant.

**Flagged for Grant (the one physical question this test raises):** the mechanism is real and
lossless, but its VALUE is an echo and its A1-sourcing is untested (no dilatation DOF here). Is the
chiral-driven circulation the SAME object as mass=A1 (needs the two-sector engine to see if it
sources a dilatation), or a distinct circulation-energy route? That is the make-or-break for whether
this earns a full arc.
