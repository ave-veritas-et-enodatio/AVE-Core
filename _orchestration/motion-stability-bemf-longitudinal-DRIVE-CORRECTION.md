# DRIVE CORRECTION — longitudinal probe re-dispatch (2026-06-04)

**Status:** the first implementer (driver skeleton `51a38953` + WIP edit) was
**killed mid-flight** because its longitudinal drive was a **longitudinal/shear
MIX, not clean compression** — the exact mislabel trap the transverse-vs-
longitudinal audit warned about. This addendum locks down the corrected drive.
The original prereg (`motion-stability-bemf-longitudinal.md`) stands; this
supersedes only **STEP 0 (the drive)** and adds a mandatory validation gate.

---

## The flaw (why the first run was killed)

The WIP drive (`apply_longitudinal_drive` Variant A) wrote:

```python
engine.cos.u_dot[..., 0] += v_drive * env(r)        # env(r) = exp(-r²/2σ²), r²=(x-cx)²+(y-cy)²+(z-cz)²
```

A **radial** Gaussian times x̂. Its curl is NOT zero:

```
curl u = (∂_y u_z − ∂_z u_y,  ∂_z u_x − ∂_x u_z,  ∂_x u_y − ∂_y u_x)
       = (0,                  v·∂_z env,           −v·∂_y env)      ≠ 0
```

Because `env` depends on y and z, `∂_y env ≠ 0` and `∂_z env ≠ 0` → **curl u ≠ 0**.
The drive carried a transverse/shear component. It satisfied the prereg's
`div u ≠ 0` test but was NOT a clean longitudinal (compression) drive — so a
"motion" result could be the **shear/transverse channel re-driven under a
longitudinal label** (the same channel both prior runs already PINNED on). The
probe also had only `cos_div_rms` — **no curl witness, no gate** — so the mix
was invisible.

## The two load-bearing facts from the transverse-vs-longitudinal audit

1. **TRANSVERSE = T₂** (`V_inc` common-mode + Cosserat `ω` microrotation), shear
   modulus G, speed `c_T = √(G/ρ) = 1`. The (2,3) self-trap shell lives here and
   is shear-frozen (`c_eff = c·√S → 0`). Op16 `c_eff = c√S` is the **shear speed
   only** (`operators.md:56`, `eq:c_shear`).
2. **LONGITUDINAL = A₁** (`div u ≠ 0` compression on the translational `u`
   field), bulk modulus K, speed `c_L = √((K+4G/3)/ρ) = √(10/3) ≈ 1.826`
   (`cosserat_field_3d.py:1491,1500`). **There is NO derived bulk-freeze
   `c_L·√S`** — the longitudinal channel is NOT frozen by the V-sector saturation
   S. So the transverse PIN does **not** predetermine the longitudinal result;
   the bulk channel is genuinely OPEN. (The first implementer got THIS right —
   `C_LONG = √(10/3)`, "NOT frozen by S". Keep it.)

A genuine longitudinal drive must therefore be **curl-free** (pure compression),
on `cos.u` / `cos.u_dot`, NOT on `V_inc` / `omega`, and must NOT inherit the
shear frozen-clock.

---

## STEP 0 (CORRECTED) — the curl-free longitudinal drive

A clean compression field is **curl-free**: the gradient of a scalar potential,
`u = ∇φ` ⇒ `curl u ≡ 0` (continuum) and `div u = ∇²φ ≠ 0`. Two admissible
realizations (the anti-stall 2-try cap picks between them):

- **Variant A (PRIMARY — directional compression dipole / co-moving wake):**
  `φ(x,y,z) = (x−c_x)·G(r)`, `G(r)=exp(−r²/2σ²)`; drive `u_dot = v_drive·∇φ`
  (or `u = v_drive·∇φ` for the displacement form). This is a **+x/−x-asymmetric
  compression** (compression ahead, rarefaction behind) — the literal moving-
  electron longitudinal wake of `de-broglie:50`. Curl-free by construction;
  localized on the host. NOTE: a localized curl-free field has **zero net linear
  momentum** by ∮ — that is EXPECTED and fine. The drive is a **directional
  compression bias**, not a momentum blob; the motion test is whether that bias
  **drags the knot centroid** (via the `z_local` saturation-impedance gradient).
  → Reframe the prereg's "net +x momentum" as "directional +x compression."

- **Variant B (ANTI-STALL fallback — x-planar longitudinal pulse):**
  `u_x = w(x)·sin(k_x·x)`, `u_y=u_z=0`, with the envelope `w` a function of **x
  ONLY** (uniform across y,z). Then `∂_y u_x = ∂_z u_x = 0` ⇒ `curl u ≡ 0`
  exactly, `div u = ∂_x u_x ≠ 0`. This CAN carry net +x momentum (a one-sided
  pulse) at the cost of being a transverse slab. Use only if Variant A's LINEAR
  smoke test fails.

Both are on `engine.cos.u` / `u_dot` (the A₁/bulk channel). One-shot imprint
(no sustained pump). `v_drive = 0` → identity.

## MANDATORY VALIDATION GATE (the fix the killed run lacked)

Immediately after applying the drive, **before accepting it**, compute over the
interior (alive ∩ non-PML):

```python
div_rms  = rms( div u )          # bulk/compression witness (the killed probe had this)
curl_rms = rms( |curl u| )       # NEW — the shear witness it was missing
assert curl_rms / max(div_rms, eps) < 0.10, \
    f"DRIVE MISLABELED: curl/div = {curl_rms/div_rms:.3f} — this is a shear/longitudinal MIX, not clean compression"
```

`curl u` and `div u` via the same tetrahedral operators the engine uses
(`tetrahedral_gradient` for div; build the discrete curl from the same per-
component gradients). The `< 0.10` threshold means the drive is **≥90 %
compression**. This gate ALSO catches discrete `curl(grad)≠0` operator error —
if the tetrahedral operators don't commute well at the chosen σ, the gate fails
and σ/resolution must be raised until it passes. **If the gate cannot be passed
by either variant → return `BLOCKED-drive` (do NOT run a mixed drive).**

Print `curl/div` for every arm in the results JSON so the audit trail shows the
drive was clean.

---

## Everything else in the original prereg STANDS

- Durable Arm-C (2,3) host; LINEAR (sub-saturation, SM-counterfactual) +
  BASELINE (net-zero / standing-compression, matched-energy) arms.
- Forward-predicted `PIN-even-longitudinal` (no fit).
- Native longitudinal readout + the honest `z_local` coupling path
  (`disable_cosserat_lc_force=True`).
- A SUPPORTS triggers FULL `ave-discrimination-check` BEFORE any positive
  framing — on the axes the transverse (ii) "MOVES" positive collapsed under:
  **(1)** LINEAR control advects the same → generic transport, not bemf;
  **(2)** core A² decays during "motion" (A 0.85→0.4 never reaching Γ=−1) → a
  dying blob being pushed, not a stable soliton translating — **track A²(t) and
  report it**; **(3)** velocity below the lattice-artifact floor; **(4)** BASELINE
  matched-energy confound. All four must be cleared.
