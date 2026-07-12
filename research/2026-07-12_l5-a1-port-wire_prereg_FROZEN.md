# L5 Q/leakage × A1 radiating face — FROZEN prereg

**Freeze discipline.** Pushed as its own commit BEFORE any L5+A1 wire-in driver
(ave-prereg v1.7 Step 3.11). **HOLD / no merge** until Grant.

**Authorization.** Grant 2026-07-12: (1) HOLD-stack review then (2) wire A1 into a
real local driver. Review accepted A1–A3 as instrumentation; top wire-in target =
`unified_l5_q_leakage.py` (sponge PML confounds Q/leak).

**Class.** Instrumentation application — **not** a new L5 emergence claim, not
alpha emergence, not outer mesh. Rule-14: parallel `NativeCageIMEX` + A1
`port_sigma` arm beside the existing MasterEquation sponge lane. Do **not**
silently rewrite the 2026-06-07 L5 result; report a **deconvolution** comparison.

**α-CLEAN on verdict path.** Alpha remains comparison-only (existing L5 rule).

---

## Sector header

- **SECTOR** = alpha-free Q / leakage proxies for a localized solid seed; question
  is whether measured ringdown/leak is **physical confinement** or **pad
  absorption**.
- **DOF:** MasterEquation + sponge YES (existing). Matched A1 leave-taking on
  same seed class — NO on the L5 driver today.
- **MODE** = mechanical bulk (scalar V). Phasor bridge optional on A1 arm if
  `project_from_scalar` accepts IMEX `V`; if not, A1 arm reports **H-based**
  leave-taking / effective Q only and marks phasor proxies N/A.
- **REGIME** = I–II rest-scale primary; wall-window optional stress.
- **Instrument:** same sech seed on (A) sponge MasterEquation vs (B) NativeCageIMEX
  open port; compare energy leave-taking and a ringdown-Q proxy.
- **consistency-vs-emergence:** FIREABLE instrumentation. Refuse EMERGENCE.

---

## Target (one sentence)

Show that L5-style Q/leakage on a rest-scale sech can be read through an **A1
passive matched port** so pad-swallowing is replaced by certified leave-taking,
and quantify how much the sponge lane’s energy decay differs from the A1 lane.

---

## Analytic expectations

### Arms

| Arm | Carrier | Boundary |
|---|---|---|
| **sponge** | `MasterEquationFDTD` (existing L5 defaults, may use reduced N/steps for the wire-in) | `pml_thickness=4` sponge |
| **a1_port** | `NativeCageIMEX` | `port_sigma≈0.05`, A1 Newmark face |

Primary case: **rest_scale** amplitude \(0.48\) (L5 CASES). Wall-window optional.

### Observables (frozen)

1. **Passivity (a1_port):** \(H_{\max}/H_0 \le 1+10^{-3}\) during the window.
2. **Leave-taking residual:** \(\mathcal{R}=H_{\rm end}/H_0\) (both arms if sponge
   exposes comparable \(H\); else sponge uses `total_energy` as available).
3. **Effective Q from energy envelope** (both arms, same estimator):
   fit late-window \(\log H(t)\) (or center \(|V|\) if H unavailable) →
   \(\tau\), \(Q_{\rm eff}=\pi f\tau\) when a breathing frequency is available;
   if no \(f\), report \(\tau\) and \(\mathcal{R}\) only and mark `Q_eff=null`.
4. **Discrimination:** \(\Delta\mathcal{R} = |\mathcal{R}_{\rm sponge}-\mathcal{R}_{\rm a1}|\)
   or \(\Delta\tau = |\tau_{\rm sponge}-\tau_{\rm a1}|\). Floor: \(>10^{-4}\)
   relative or absolute as declared in the result.

### Expectation (picture, not entailed)

Sponge arm should show **faster / larger** energy disappearance (pad kill) than
A1’s passive leave-taking of *wave* energy — or, if sponge injects (GX5 class),
\(H_{\max}/H_0>1\). A1 should stay passive. This **deconvolves** pad artifact
from confinement Q.

---

## Frozen bins

| Bin | Label | Criterion |
|---|---|---|
| **(i)** | **PORT-DECONVOLVED** | A1 passivity PASS; both arms produce finite \(\mathcal{R}\) (or \(\tau\)); \(\Delta\mathcal{R}\) or \(\Delta\tau\) above floor; sponge does **not** silently match A1 within floor |
| **(ii)** | **PORT-INDISTINGUISHABLE** | A1 green but \(\Delta\) ≤ floor (sponge already “looked like” A1 on this seed/window) |
| **(iii)** | **PORT-FAIL** | A1 passivity fail or A1 arm cannot run the L5 seed |

Flags: wall-window arm; phasor proxies N/A on IMEX; comparison-only alpha errors.

---

## Out of scope

- Rewriting / retiring the 2026-06-07 L5 JSON as false
- Claiming alpha emergence from the A1 arm
- A2/A3 required for PASS (optional later)
- Outer mesh / Machian integral / genesis
- Merging HOLD PRs

---

## Deliverables after freeze push

- This prereg (this commit).
- Thin driver + tests + result; HOLD PR stacked on A3 tip.
