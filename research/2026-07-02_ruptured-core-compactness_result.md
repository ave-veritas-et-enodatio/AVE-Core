# Result — Ruptured-Core Neutron-Star Compactness Bound

**Date:** 2026-07-02
**Branch:** `analysis/ruptured-core-compactness-bound`
**Prereg:** `research/2026-07-02_ruptured-core-compactness_prereg.md` (frozen)
**Driver:** `src/scripts/vol_3_macroscopic/ruptured_core_compactness_driver.py`
**Class:** EXPLORATORY. **Verdict: EOS-GATED — Outcome C** (prereg §6), pending
one Grant physics ruling (the Regime-IV EOS fork, §5 below).

---

## TL;DR (honest, not overclaimed)

- The AVE intact compactness bound $2GM/(c^2R) < 2/7 \approx 0.286$ is
  **reproduced exactly** by the driver and is a **surface strain-yield
  threshold**, NOT a GR-Buchdahl central-pressure integral.
- **PSR J0740+6620 sits at $C_{surface} = 0.496$** (central NICER;
  0.539 at the radius lower edge) — **ABOVE $2/7$**, i.e. **INSIDE** the
  AVE-predicted Regime-IV-core + Regime-III-crust rupture regime. This is
  **corroborative of the canonical leaf**, not a falsifier. (Confirms Grant's
  framing: the surface is compactified beyond $2/7$ *because* it has a
  melted/condensed core.)
- **Whether AVE forces a DISTINCT max compactness for the layered
  (ruptured-core) configuration is GATED on one physics input the corpus does
  not canonically pin: the Regime-IV (melted-lattice) equation of state under
  COMPRESSION.** This is a genuine framing fork, surfaced to Grant (§5). I did
  NOT posit an EOS silently.
- **This is NOT (yet) a chord.** It is either a chord, an echo, or an
  EOS-gated negative depending on the fork. Reported as such.

---

## 1. Intact-bound reproduction (prereg §4 step 1 — PASS)

Driver output [1]:

```
C_intact (2/7)   = 0.285714   (=nu_vac; eps11=(7/2)*C)
eps11 at R_min   = 1.000000   (must be 1.000000)  ✓
R_min(1.4 Msun)  = 14.48 km   (leaf ave-compactness-limit.md:33 says 14.5)  ✓
```

**Load-bearing structural finding.** The AVE $2/7$ bound is derived as
"$\varepsilon_{11}(R) = 7GM/(c^2R) < 1$ so the *surface* has not yielded"
(`ave-compactness-limit.md:12`, vol3 ch15 tex:392). It is a **surface
strain-yield threshold**. GR's Buchdahl $8/9$ is a different object — it comes
from requiring finite *central* pressure in a TOV integration of an
incompressible star. So the AVE bound and GR's Buchdahl are **not the same kind
of bound**: AVE's is a surface condition, GR's is an interior-pressure
condition. The corpus label "AVE Buchdahl bound" is a naming convenience; the
derivation is a yield threshold. This is the gap the layered analysis probes.

## 2. PSR J0740 anchor (prereg §4 step 4 — corroborative)

Driver output [2] (NICER Fonseca+2021 / Riley+2021 / Miller+2021):

```
M = 2.08 Msun, R = 12.39 (+1.30 -0.98) km
C_surface (central)      = 0.4959     <- matches Grant's quoted 0.495
C_surface (R lower edge) = 0.5385
eps11(R) central         = 1.7358  (> 1  => surface already past shear yield)
```

$C = 0.496 > 2/7$: **PSR J0740's surface is strained past the intact yield
shell.** Per the canonical leaf this means its interior is Regime IV (ruptured)
with a Regime-III crust — exactly the configuration the leaf predicts
(`ave-compactness-limit.md:28,36`). **Corroborative.** The intact bound is not
violated because it only forbids a *fully intact* static lattice at $C>2/7$;
it explicitly *permits* (indeed predicts) a ruptured-core configuration there.

## 3. The layered solve — parametric in the core-stiffness fork

Because the ruptured-core EOS is not canonical (§5), the driver computes
$C_{max}$ **as a function of the fork** so the verdict falls out the instant
Grant collapses it.

**Soft branch (Reading B), driver [3]** — no hard bulk floor, core support
fraction $f_{core}$ slides $C_{max}$ continuously from the intact $2/7$
($f_{core}=1$, fully supported = intact) to the Schwarzschild horizon $C=1$
($f_{core}=0$, no support = collapse):

```
f_core=1.00  C_max=0.286   (fully supported = intact surface, no ruptured core)
f_core=0.75  C_max=0.464
f_core=0.50  C_max=0.643
f_core=0.25  C_max=0.821
f_core=0.00  C_max=1.000   (Schwarzschild horizon r_s)
```

The soft branch has **no pinned intermediate** — the "max" is not a distinct
number, it slides to the horizon. **Reading B ⇒ echo, no chord.**

**Hard-floor branch (Reading A), driver [4]** — a hard bulk-K floor PINS
$C_{max}$ at a substrate value. The candidate anchors the substrate offers:

| Candidate | $C_{max}$ | vs Buchdahl 8/9 | vs PSR J0740 (0.496) |
|---|---|---|---|
| `nu_vac_incompress` (recover surface yield) | **0.286** | distinct | **0.496 ABOVE it — inconsistent, DISCARD** |
| `phi_pack` ($1/\varphi$, golden packing) | **0.618** | distinct | 0.496 below it (chord-compatible) |
| `horizon` (Schwarzschild $r_s$) | **1.000** | distinct | 0.496 below it (= echo) |

**Critical observation (flag-don't-fix):** the `nu_vac_incompress` candidate —
"a stiff ruptured core that merely recovers the *surface* yield" — gives back
$2/7 = 0.286$, which **PSR J0740's measured $0.496$ already exceeds.** So that
candidate is **empirically excluded**: the ruptured core cannot be merely
"as stiff as the intact surface yield" — J0740 is more compact than that. The
melted core must be **strictly stiffer than the intact-lattice surface yield**
for any hard-floor bound to be consistent with the data at all. That is a real
(if modest) empirical constraint the driver surfaced: **if AVE forces a
hard-floor $C_{max}$, it must be $> 0.539$** (J0740's upper-edge compactness) to
survive. Only `phi_pack` (0.618) and `horizon` (1.0) clear that bar.

## 4. Substrate behavior of the ruptured medium (canonical rupture_solver)

Driver [6], from `ave.regime_4_rupture.rupture_solver` (canonical):

```
r=0.99  S=0.141  c_shear/c0=0.376  ruptured=False
r=1.00  S=0.000  c_shear/c0=0.000  ruptured=True
r=1.20  S=0.000  c_shear/c0=0.000  ruptured=True
```

The **shear channel structural support $c_{shear}=c_0\sqrt{S} \to 0$ at
rupture.** The medium loses its transverse (shear) stiffness entirely in Regime
IV. This is the physical reason the fork matters: with shear gone, the *only*
possible source of a hard floor is the **bulk-K channel**. The canonical
rupture solver is silent on the bulk-K compression stiffness in Regime IV
(it reports EM $Z_{sym}=Z_0$, $c_{EM}=c_0/S$ — a $\Gamma=0$ perfect *absorber*,
which carries no structural support). **So the substrate itself leans toward
Reading B (soft) — UNLESS the bulk-K compression channel has a hard floor the
corpus has not derived.**

## 5. THE FORK — surfaced to Grant (do not resolve silently)

**The corpus does NOT canonically pin the Regime-IV compression EOS.** What
exists:

- Compression-side **intact** kernel $c_{eff}^2 = c_0^2/\sqrt{1-A^2}$ — stiffens
  to $\infty$ *up to* yield, then the lattice ruptures. Describes the medium
  *before* rupture, not after.
- Rarefaction-side EOS $c_{bulk}^2 = c_0^2(1+\bar\rho/(1-\bar\rho^2))$ →
  candidate cavitation floor $\bar\rho_{cav}=-1/\varphi$
  (`cavitation_flow.py:22-26`). This is the **opposite (tensile) sign** and is
  itself tagged **CANDIDATE / CONTESTED** (`lattice-extreme-bh-rationality.md:19,64`).
- Only a physical *analogy* for the compressed ruptured core: "quark-gluon
  plasma / color-superconducting phase" (ch15 tex:402) — not an AVE $P(\rho)$.

**The plumber-physical question for Grant (one sentence):**

> Once the lattice ruptures (Regime IV, shear modulus $\to 0$), is the melted
> core **stiffer or softer** than the intact lattice under *further
> compression* — does the bulk-K channel supply a hard incompressible floor
> (→ a finite max compactness $C_{max}$ between $2/7$ and the horizon, a
> forward-prediction chord), or does it go soft like a plasma (→ the core
> keeps collapsing to the $r_s$ horizon, and the only "max" is the
> Schwarzschild limit, an echo of GR)?

Two readings, two verdicts (frozen in prereg §6):

- **Reading A (STIFF, hard bulk floor)** → a pinned $C_{max}$. If it lands at a
  clean substrate value $> 0.539$ (to survive J0740) and $< 8/9$ (distinct from
  Buchdahl), that is a **forward-prediction chord** — the compactness ceiling of
  the most compact pulsars is a direct test. The cleanest substrate candidate
  is $C_{max} = 1/\varphi \approx 0.618$ (golden-packing floor, the same
  $\varphi$ that sets the cavitation floor on the other extreme) — **and note
  PSR J0740 at 0.496–0.539 sits just below it, so the next-more-compact pulsar
  measurement would be a live test.** But $1/\varphi$ is a *candidate anchor*,
  NOT a derived compressed-Regime-IV EOS. Naming it as the answer requires the
  Grant ruling + a derivation.
- **Reading B (SOFT, plasma)** → $C_{max}$ degenerates to the horizon $C=1$;
  no distinct chord, an **echo** of the Schwarzschild limit.

## 6. Classification (consistency-vs-emergence, prereg §5)

- **The intact $2/7$ vs J0740 corroboration**: Class C consistency (recovers
  the leaf's own prediction; no new number).
- **A forced hard-floor $C_{max}$ (Reading A)**: *would be* Class D emergence /
  forward-prediction **only if the bulk-K compression floor is axiom-derived,
  not posited.** As it stands (candidate anchor only), it caps at **Class C /
  CANDIDATE** — same status as the cavitation floor it mirrors.
- **Current headline verdict: Outcome C (EOS-gated negative)** — no canonical
  Regime-IV compression EOS, so a distinct $C_{max}$ is **not derivable** without
  either (a) Grant collapsing the fork toward Reading A + a bulk-K-floor
  derivation, or (b) importing a non-canonical EOS (which I decline to do
  silently). This is the honest, valid, valuable outcome the prereg
  pre-committed to.

## 7. What would turn this into a chord (the path, if Grant rules Reading A)

1. Grant rules the ruptured bulk-K core **stiff** (hard floor).
2. Derive the bulk-K compression floor from axioms (K4 packing fraction /
   Poisson $\nu_{vac}$ / $\varphi$ — the same machinery as the cavitation floor
   but on the compression sign). Target: is it $1/\varphi$? something
   $\nu_{vac}$-tied?
3. If the derived floor gives $C_{max} \in (0.539,\, 8/9)$ distinct from
   Buchdahl → **forward-prediction chord**: the max compactness of the most
   compact pulsars tests it. PSR J0740 (0.496–0.539) is already the closest
   probe; a future measurement of a more compact object either confirms
   ($C < C_{max}$) or falsifies ($C > C_{max}$).

## 8. Honest flags / self-audit

- **Bug caught + fixed in-session (flag-don't-fix):** the driver first computed
  `C_INTACT = 2*NU_VAC = 4/7 = 0.571` — WRONG. The compactness bound is
  $2GM/(c^2R) < 2/7$ (`= NU_VAC`), while $\varepsilon_{11} = (7/2)\cdot C$.
  Fixed to `C_INTACT = NU_VAC` (driver line ~53). Re-verified against
  `ave-compactness-limit.md:23` and the 14.5 km $R_{min}$ leaf value (recovered
  14.48 km). Documenting the transient error per audit-trail discipline.
- **TOV is non-native (CP1):** I did NOT run a real-space Cartesian TOV
  integration — the intact bound is a strain threshold, not a pressure integral,
  and the ruptured-core TOV is ill-posed without the §5 EOS. The parametric
  soft/hard sweep is the substrate-native rendering (boundary condition, not
  bulk force).
- **$1/\varphi$ is a CANDIDATE, not a derivation.** I explicitly did not
  headline "AVE forces $C_{max}=1/\varphi$." It is the cleanest substrate anchor
  offered for the Grant fork; asserting it requires the derivation in §7.
- **The `nu_vac_incompress` candidate is empirically excluded by J0740** (0.496
  > 0.286) — a real constraint the driver surfaced, reported not hidden.
