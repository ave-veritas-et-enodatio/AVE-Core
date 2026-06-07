# Saturation-TIR moving Γ=−1 impedance boundary — RESULT

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-saturation-tir-moving-boundary` (off `main`)
**Prereg (FROZEN):** [`2026-06-06_saturation-tir-moving-boundary-prereg.md`](2026-06-06_saturation-tir-moving-boundary-prereg.md)
**Engine:** `src/ave/topological/cosserat_field_3d.py` (`use_impedance_boundary`, KEEP-BOTH default OFF)
**Driver:** `src/scripts/vol_1_foundations/r10_saturation_tir_moving_boundary_genesis.py`
**Discipline:** `substrate-native-check` (CP1/2/4/6/7/8) · `ave-canonical-source` · `ave-driver-script-honesty` · `ave-evidence-framing` · KEEP-BOTH

---

## §0 Headline — VERDICT (II)

> **(II) The reflective skin forms and the boundary confines — but no clean (2,3) cavity mode self-assembles. The boundary is right; the mode-assembly isn't.**

The prereg's **central hypothesis is confirmed at the mechanism level**: rendering Axiom-4
saturation as a **moving reflective short** (the ω-wave reflects off its own `Z→0` wall) —
rather than the non-convex energy term `γ(κ²−κ⁴/ω_yield²)` — **converts collapse → confinement.**
The same helical ω-photon that the energy term blows up (`H→6.1×10⁸`, `|ω|_max→2.2×10⁵`,
localization `0.97→0.26`) is **held** by the moving Γ=−1 boundary (localization `0.97→0.94`,
`|ω|_max` bounded `3.0→3.9`, energy bounded). **Energy has no wall; the boundary IS the wall.**

What does **not** close to (I): the confined object is not the **(2,3) torus-knot electron**.
The Cosserat-ω sector carries the confinement, the **charge (Beltrami helicity, sign-flips)**, and
**one** winding (`c=2`), but **not** the full `(2,3)` double-winding (no `w₂=3`, no Hopf charge),
and the idealized **hard Γ=−1 wall is numerically delicate** (the explicit moving stiff-clamp
parametric-pumps — the §7 risk, characterized below). Both gaps are **localized** (§7).

---

## §1 The mechanism that was built (KEEP-BOTH, default OFF)

New opt-in flag `use_impedance_boundary` on `CosseratField3D` (default `False` → the
energy-saturation path is **byte-identical**; 95 cosserat tests pass unchanged). When `True`,
`step()` propagates a **clean linear elastic ω-wave** (`k_op10=k_refl=k_hopf=0`, the matched
bulk) **plus an Op3 Γ=−1 node-clamp at the moving μ-side saturation front** (the wall):

- `_impedance_gamma_field` — Op3 `Γ(r) = (Z_eff−Z₀)/(Z_eff+Z₀)` from the **Op14
  asymmetric-Meissner** impedance `Z_eff = Z₀·√(S_μ/S_ε)` (`Z₀=1`), reusing the canonical
  `_update_saturation_kernels` (`V_sq=0` in the pure-Cosserat engine).
- `_impedance_clamp_accel` — the Γ=−1 short as a **sign-gated reactive node-clamp**
  `a_ω = −(K/I_ω)·relu(−Γ)·ω`. **SECTOR SUBTLETY respected (prereg, corpus):** only the
  **μ-side** short (`Γ<0`, `Z_eff→0`) is a node (confining); the **ε-side** open (`Γ>0`,
  `Z_eff→∞`, `Γ=+1`) is an antinode and is **not** clamped.
- §7 ring/alias mitigations: clamp weight **frozen once per step** (conservative within the
  velocity-Verlet step) + **skin-depth smoothing** (keeps the wall above the Nyquist scale).
- `impedance_hamiltonian` — the **proper conserved energy** `T + W_linear + V_clamp` (CP6).
- `initialize_gaussian_wavepacket_omega` gains a `helicity` kwarg (default `0.0` →
  byte-identical) for the **charged** (circularly-polarized, Beltrami-helical) ω-photon.

**substrate-native-check:** CP1 — the reflective scatter is applied inside the wave-propagation
`step()`, **not** the gradient-descent `relax_step` and **not** the energy multiplier. CP8 — the
seed is the **generative precursor** (a helical photon), **not** the finished (2,3); tested against
a **matched baseline** (same seed, mechanism OFF).

---

## §2 Validity gate — PASS (the photon limit is recovered)

Low-amplitude photon (`A=1e-3`), wall **ON**:

| Quantity | Value | Expect |
|---|---|---|
| `Γ_min` over 80 steps | **−6.7×10⁻⁹** | ≈ 0 (matched) |
| energy `E_f/E_0` | **0.9999** | 1 (no spurious reflection) |

At `A≪1`, `S_μ≈S_ε≈1 → Z_eff≈1 → Γ≈0`: the photon **propagates freely**, the wall is
invisible. The mechanism smoothly interpolates matched → reflective across yield. **Gate passed
before the confinement test was read** (prereg §4 ordering).

---

## §3 The load-bearing result — collapse → confinement (mechanism discriminator)

Genesis amplitude `A=3.0`, helical ω-photon, three-way (CP8 matched baseline):

| Run | localization | rms | `|ω|_max` | energy `E_f` | outcome |
|---|---|---|---|---|---|
| **energy-sat baseline** (`IB=False`) | 0.967 → **0.256** | 3.67 → 11.79 | 3.0 → **2.2×10⁵** | **6.1×10⁸** | **collapse/blowup** (Arm C (III) reproduced) |
| no-wall linear (`K=0`) | 0.967 → 0.531 | 3.67 → 9.02 | 3.0 → 1.24 | 9.6×10² | disperses (free photon) |
| **moving Γ=−1 wall** (`K=400`) | 0.967 → **0.938** | 3.67 → 3.46 | 3.0 → 3.91 | 2.7×10³ | **held — confined** |

The discriminator is unambiguous: **the energy term collapses the photon; the linear wave
disperses it; the moving Γ=−1 wall holds it.** The confinement is attributable to the wall alone
(the bulk is the clean linear wave — CP8 mechanism isolation), so this is not an amplitude or
initial-condition artifact. **This is the prereg's central claim, confirmed.**

---

## §4 The six checks (on the wall run)

| # | Check | Result | Reading |
|---|---|---|---|
| 1 | **self-trap** | localization `0.967→0.938`, `|ω|_max` bounded | ✅ held (vs baseline `→0.256`) |
| 2 | **(2,3) cavity mode** | `c=2`, `Q_H≈6×10⁻⁶` | ❌ one winding only (the "2"); no `w₂=3`, no Hopf charge — **COORDINATE: read on the Cosserat ω real-space; the corpus (2,3) primarily lives in K4 `(V_inc,V_ref)`** |
| 3 | **sub-yield core + Γ=−1 skin** | core `⟨Γ⟩=−0.034`, skin `min Γ=−0.089` | ◑ reflective short **forms** but **soft** in the stable regime (hard Γ=−1 → §6) |
| 4 | **Q = ℓ** | geometric `Q=3.14` (`R=0.49, r=0.0`) | ⚠ **PROXY** — geometric `R·r` form, **NOT** the Op21 Nyquist mode-count; degenerate here (no resolved shell) |
| 5 | **charge = helicity** | §5 | ✅ carried (sign-flips) |
| 6 | **mass / size / ring** | confined `E=2.7×10³`; size `R≈0.5`; `ω_C(natural)=1.0` | ◑ mass-proxy + size measured; shell under-resolved at this `N` |

**ave-driver-script-honesty:** every number is measured from the evolved field. Check 2 is read
in the **Cosserat ω-phasor** (which matches the seeded ω-photon, `phase-space-coordinate-check`),
**not** the K4 `(V_inc,V_ref)` coordinate where the corpus (2,3) primarily lives. Check 4 is a
**geometric proxy**, not the Op21 Nyquist confined-mode count the prereg §1 specifies.

---

## §5 charge = helicity — CARRIED (the chiral photon makes a charged trapped state)

Seed `+h` vs `−h` (wall ON); read the **integrated Beltrami helicity** `H_bel = Σ ω·(∇×ω)`
(the carried charge of a chiral ω-photon — **not** the Hopf charge `Q_H`, which is ≈0 for a
circularly-polarized traveling wave that is not a knotted Hopfion):

| seed | `H_bel` | localization |
|---|---|---|
| `+h` | **−34.78** | → 0.938 |
| `−h` | **+34.93** | → 0.940 |

**The helicity sign flips with the seed; both handednesses confine.** This is the corpus's
`e⁻ (LH) / e⁺ (RH)` parity: the charge (helicity) is carried into the confined state, and the
confinement itself (the μ-side short from curvature) is helicity-independent — exactly the
expected `photon (neutral) + helicity = charged trapped state` structure.

---

## §6 The hard Γ=−1 wall — forms, but the explicit scheme pumps (§7 characterized)

Pushing the clamp to `K=800`:

| Quantity | Value |
|---|---|
| hard skin `Γ_min` | **−0.994** (the idealized total-reflection short **does form**) |
| energy `E/E₀` over 400 steps | **2.7** (and `→54×` by 750 steps — **pumping**) |

The hard Γ=−1 wall **forms** (`Γ_min=−0.994`) but the **explicit moving stiff-clamp
parametric-pumps**: the field-amplitude-dependent stiffness `K·relu(−Γ(ω))` is modulated in sync
with the oscillation, a parametric oscillator that injects energy in an explicit integrator. The
**soft-to-moderate** wall (`g_min≳−0.3`, §3) is stable and energy-bounded; the **idealized hard
Γ=−1 standing wave is not reachable with this scheme.** This is the prereg §7 risk, now
**localized**: a stable hard wall needs an **implicit / energy-conserving (symplectic-with-
amplitude-dependent-stiffness) integrator**, not the explicit velocity-Verlet.

---

## §7 Why (II) and not (I)/(III) — and the localized gaps (CP8 structural-capability findings)

**Not (III):** reflection **does** stabilize. The boundary holds the photon where the energy term
collapses it (§3) and the free wave disperses it; the skin is real (`Γ<0`); the validity gate
passes; the charge is carried. The prereg's energy-vs-boundary diagnosis is **correct** — the gap
was the missing reflective stop, and the reflective stop works.

**Not (I):** the confined object is not yet the **(2,3) electron**. Two gaps, each localized to a
specific engine capability (CP8 step 4 — each non-hostable layer names the engine to use next):

1. **The (2,3) double-winding needs the K4 sector.** The Cosserat-ω real-space read carries the
   **"2"** (toroidal winding, `c=2`) but not the **"3"** (poloidal / U(1) fibre). This matches the
   corpus projection map: the "2" is the n̂-direction (S² base, **survives** Hopf), the "3" is the
   **U(1) fibre** (the information **lost** in the Hopf projection) — which lives in the K4
   `(V_inc,V_ref)` phase, **not** the Cosserat ω real-space. The (2,3) mode-assembly load-bears the
   **coupled K4 + Cosserat engine** (`vacuum_engine.py`), consistent with the prior genesis
   findings (`substrate-native-check` CP8 worked instances).

2. **The hard Γ=−1 standing wave needs an implicit integrator** (§6). The mechanism is right; the
   explicit time-stepping of a moving hard reflective wall is the numerical gap.

---

## §8 Scope notes + flag-don't-fix

- **FLAG (V_yield vs V_SNAP):** the prereg drives "across `V_yield`," but the corpus is careful
  that the **Γ=−1 wall forms at `V_SNAP` (full saturation, `A²=1`)**, with `V_yield` (`=√α·V_SNAP`)
  being merely the **onset of nonlinearity** (`pair-production-axiom-derivation` §6: *"V_yield …
  onset of nonlinearity … no Γ=−1 wall yet; V_SNAP … full saturation … Γ=−1 forms"*). The engine
  carries a **single** yield scale (`omega_yield=π`) where `A²→1`, so the engine's "yield boundary"
  maps to the corpus's **V_SNAP full-saturation** Γ=−1 condition, and `Γ(A)` interpolates
  `0→−1` smoothly across it. The mechanism is consistent; the one-scale-vs-two-scale labeling is a
  corpus subtlety surfaced here, not resolved in-engine. **For Grant.**
- **Coordinate (CP4):** check 2 is read on the Cosserat ω-phasor (matches the seeded ω-photon),
  not the K4 phase-space where the corpus (2,3) primarily lives — see gap #1.
- **KEEP-BOTH:** `use_impedance_boundary=False` is default and byte-identical; no existing result
  changes. The energy-saturation path is preserved for audit-trail continuity.
- **No animation:** the prereg renders the real+phase animation **only on verdict (I)**; (II)
  does not trigger it.

---

## §9 Reproduce

```bash
PYTHONPATH=src ./.venv/bin/python \
  src/scripts/vol_1_foundations/r10_saturation_tir_moving_boundary_genesis.py
# → JSON: src/scripts/vol_1_foundations/r10_saturation_tir_moving_boundary_genesis_results.json
```

Corpus anchors (verified): `photon-identification.md:25` (electron = photon + TIR confinement,
`Z→0, Γ→−1`), `pair-production-axiom-derivation` §6 (`Z_core→0, Γ=−1` weaves its own topological
mirror), `dual-reactance-storage-taxonomy` (Magnetic: `μ_eff→0, Z→0, Γ→−1, short, rest mass`).
