# Genesis (canonical) — self-trap the ω-shear photon — PREREG

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-genesis-omega-wave` (off `main`)
**Driver:** `src/scripts/vol_1_foundations/genesis_omega_wave_selftrap.py`
**Discipline:** `substrate-native-check` (CP1 wave-dynamics, CP4 phase-space, CP5 ω_local, CP6 reactance pair, CP7 PML/density-peak, **CP8** generative-precursor + matched baseline) · `phase-space-coordinate-check` · `consistency-vs-emergence` · `ave-canonical-source` · `ave-driver-script-honesty` · `ave-evidence-framing` · `pre-test-physics-check` · `verify-before-cite`.

---

## §0 Why this run exists (the third, correct attempt)

Both prior genesis arms returned **(III)** for an understood reason
(`research/2026-06-06_simulation-assumptions-audit.md` §8, sibling branch):

- The **canonical photon is the transverse Cosserat-ω shear WAVE** —
  `photon-identification.md:11` verbatim *"a knotted transverse Cosserat shear
  wave with u=0 and ω≠0"*; `:24` *"u=0 (no Cosserat translation), ω≠0 (pure
  microrotation), no saturation (Δφ≪α), linear Z=Z_0"*. And `:11` *"the electron
  is a self-trapped photon,"* formed by **Axiom-4 saturation TIR confinement**
  (`:25` *"At V→V_yield=√α·V_snap: C_eff→∞, Z→0, Γ→−1 → self-trapped standing
  wave"*).
- **Arm A** seeded a **V-wave** → `ω≡0` (wrong sector). **Arm B** seeded an
  **ω-flywheel under force-free relaxation** → de-collimates (wrong geometry +
  wrong mechanism). Neither seeded the canonical object with the canonical
  mechanism.

**Pre-test-physics-check (Rule 16):** the one plumber-physical question — *is the
engine's V-injection a wrong-sector photon, or is TLM-V the right transverse
mode with Cosserat-ω separate?* — was surfaced to Grant in audit §8 and
collapsed by Grant's re-aim directive: **seed the transverse Cosserat-ω shear
WAVE directly (pure ω), drive it across yield, let saturation self-trap it.**
This prereg executes that re-aim. No further framing question is open pre-freeze.

---

## §1 The seed — the canonical photon (pure Cosserat-ω, chiral, transverse)

Built on the engine's forward-propagating Cosserat-ω shear-wave seeder
(`cosserat_field_3d.py:1586-1646`, `initialize_gaussian_wavepacket_omega`:
`ω_dot = c_T·|k|·A·env·sin(k·(r−c))·ê`), **extended to circular polarization
(chirality) + a counter-propagating same-chirality pair**. NOT `Source.apply`
V-injection (Arm A's error). NOT a localized flywheel (Arm B's).

Two transverse Cosserat-ω wavepackets propagate along **z**, with ω in the
transverse **(x,y)** plane (`u≡0`, `V_inc≡0` — the photon **is** ω), spatial
chirality `χ∈{+1,−1}`, packets centred at `z0 = center ± Δ` propagating toward
the centre (signs `s=±1`):

```
ω(r,0)    = A·env(ρ,z')·[cos(k z'),  χ·sin(k z'),  0]
ω_dot(r,0)= s·A·Ω·env(ρ,z')·[sin(k z'), −χ·cos(k z'), 0],  Ω = c_T·k,  c_T=√(G/ρ_m)=1
env       = exp(−ρ²/2σ⊥²)·exp(−z'²/2σ_z²),  z' = (k_idx − z0),  ρ = transverse radius
```

- **Transverse** (ω⊥propagation), **u=0**, **V_inc=0** → properties 1+2 of
  `photon-identification.md:24` (purely transverse, microrotation-sector only).
- **Sub-saturation seed, Z-matched** (property 3+4): each single packet is seeded
  below curvature yield (`A²_curv = κ²/ω_yield² < 1`); the focus crosses yield.
- **Chirality** = the spatial handedness of the ω-helix → the Beltrami helicity
  `h = ω·(∇×ω)/(|ω||∇×ω|)` sign (the seeded ± handedness / charge polarity).
- **Same-χ counter-propagating pair** → coherent net helicity (net charge) with
  zero net linear momentum (electron at rest); amplitude **ramps** at the focus.

Constants via `ave.core.constants` (NO hardcodes): `ALPHA`, `V_SNAP`, `V_YIELD`,
`L_NODE`. Native units: `ω_C = c/ℓ_node = 1`, `ℏ/2 = 0.5`, `m_e c² = 1`,
`ℓ_node = 1 cell`. Engine `ω_yield = π`, `ε_yield = 1` (`cosserat_field_3d.py:837-838`).

## §2 The drive + mechanism — saturation confinement, NOT relaxation (CP1)

The two packets **focus** at the centre; amplitude ramps until local curvature
`κ = |∇×ω| → ω_yield = π`, engaging the Axiom-4 kernel
`S_κ = √(1 − κ²/ω_yield²) → 0` in the engine's own `step()` dynamics
(`_energy_density_saturated`, `:655` `S_kappa_sq = 1 − κ²/ω_yield²`). Via the
asymmetric impedance `Z_eff/Z_0 = √(S_μ/S_ε)` (`:583-585`), `S_μ→0 ⇒ Z→0 ⇒
Γ→−1`: the lattice self-creates a TIR cavity that traps the ω-wave into a
standing wave = the electron.

- **Wave dynamics** via `engine.step()` (K4 scatter+connect + Cosserat
  velocity-Verlet), `damping_gamma=0`. **NOT** the gradient-descent settle at
  `cosserat_field_3d.py:1384` (CP1 / audit §8 A1.6 flag).
- Drive bracketed by single-packet peak amplitude `A ∈ {0.6, 1.0, 1.4}` (focus
  sub-yield / ≈critical / over-yield). Forward IC design (declared here), **not**
  a fit to the result; each run reports the **achieved** peak `A²` reached.

## §3 Coordinate discipline (phase-space-coordinate-check + flag-don't-fix)

Two flagged substrate points — surfaced, **not** silently reconciled:

1. **The Cosserat-ω saturation variable is curvature `κ/ω_yield` (ω_yield=π),
   NOT `V/V_snap`.** `photon-identification.md:25`'s `A_yield = √α` is the
   **V-phasor** framing (V/V_snap=√α at yield); the Cosserat-ω engine has no
   V_snap in its kernel — saturation engages at `κ→ω_yield=π`. The run drives
   `κ→ω_yield`; the `√α` V-phasor onset is reported only as the K4-sector cross-
   check (`a2_core`).
2. **`extract_2_3_spatial` reads `engine.k4.V_inc` (the V-sector), a DIFFERENT
   sector from the seeded Cosserat-ω.** The canonical (2,3) is two-sector (audit
   A6.3: "2"/Cosserat-ω + "3"/V-sector). The pure-ω seed lights up the Cosserat
   sector; whether the V-sector "3" lights up from a pure-ω seed is the **audit
   §8 architecture question** (even-in-ω coupling, A1.1, sources no odd V drive).
   → Check 2 is read in **BOTH** sectors: the Cosserat-ω winding (coordinate-
   matched, the load-bearing read) AND the V-sector `extract_2_3_spatial` (the
   architecture probe). The sector split is the architecture finding.

Charge=helicity (check 3) is read in the **Cosserat-ω** sector (signed Beltrami
`h`), **NOT** the V-phasor sign (audit A3.1: V-phasor sign reads noise).

## §4 The 6-check battery (forward, NO fit) + matched baseline (CP8)

| # | Check | Read (engine, coordinate-matched) | Class |
|---|---|---|---|
| 1 | **Self-trap** — Γ=−1 TIR forms + localizes (vs disperse) | `Γ` from `S_μ/S_ε` (`_update_saturation_kernels`); interior (PML-excl) localized `|ω|²` fraction at t_final; `find_soliton_centroids` persistence | EMERGENCE |
| 2 | **(2,3) emerges** | Cosserat-ω: `extract_crossing_count` (c), `extract_hopf_charge` (Q_H→6), `extract_shell_radii`, major/minor ω-director windings (w1,w2). V-sector probe: `extract_2_3_spatial(k4.V_inc)` | EMERGENCE |
| 3 | **Charge = helicity** | `signed_helicity` (|ω|²-weighted Beltrami h); sign matches seeded χ + flips with χ; beats baseline h≈0 | EMERGENCE |
| 4 | **Sub-V_yield ring at ω_C** | A²_local field (κ²/ω_yield²+ε²/ε_yield²): thin A→1 skin frac + sub-yield interior median; core ω-series FFT peak vs ω_C=1; `ω_local=ω_global·√(1−A²)` (CP5) | CONSISTENCY |
| 5 | **Size≈ℓ_node, mass=½LI², spin=Iω=ℏ/2** | centroid radius vs ℓ_node=1; `flywheel_mass`=½I_ω Σ|ω|²; spin S_z^rot=I_ω Σ(ω×ω̇)_z (carries helicity) + axial S_z | CONSISTENCY |
| 6 | **Matched baseline** | same per-cell |ω| stats, randomized directions (h≈0, no coherent helicity); emergence (1-3) must beat it | (control) |

CP6 **reactance pair** recorded every window step: C-state (capacitive: V_inc + ω)
AND L-state (inductive: Φ_link + ω̇), plus `H = T+V` conservation.

**consistency-vs-emergence tag:** checks 1-3 are the EMERGENCE content (does the
ω-wave self-organize into a localized, winding, helicity-carrying object,
**beating the matched baseline because of structure**). Checks 4-5 are
CONSISTENCY (mass=½I_ω|ω|², spin=I_ω∫ω are definitional readouts of the IC-pinned
amplitude in native units — NOT independent CODATA predictions; per audit
A6.4 + Arm B prereg). All comparisons are framework-internal native units
(ω_C=1, ℏ/2=0.5, m_ec²=1) — no CODATA, so no structural-circularity surface.

## §5 Pre-committed outcomes (honest; do NOT force success — `ave-evidence-framing`)

- **(I)** ω-shear wave **self-traps → (2,3) + charge=helicity + sub-V_yield ring**,
  beating the matched baseline → **canonical genesis WORKS** ("the electron is a
  self-trapped photon"). Render the real+phase animation.
- **(II)** self-traps (skin/Γ→−1 forms) but **no (2,3)/charge** → the carrier
  doesn't assemble even from the ω-wave (localize the gap).
- **(III)** doesn't self-trap (ω-wave disperses / saturation doesn't confine) →
  pin why.
- **Architecture finding** (orthogonal to I/II/III): if the engine **cannot
  seed/carry** the ω-shear wave as a coherent photon (V/ω structure fights it),
  or the V-sector "3" never lights from the pure-ω seed → report explicitly;
  this answers audit §8.

**Per-run verdict:** (I) self-trap (Γ→−1 + localized, beats baseline) AND (2,3)
(Cosserat c=3/Q_H≈6 OR V-sector (2,3)) AND charge=helicity (signed h matches χ).
(II) self-trap but no (2,3)/charge. (III) no self-trap.
**No post-hoc criteria drops** (Rule 11): a clean (II)/(III) with a named
mechanism is the discipline working.

## §6 Discipline checklist (exit)

- [x] CP1 wave-dynamics (`step()`, damping=0); NOT descent (`:1384`).
- [x] CP4 phase-space: (2,3) read in matched coordinates (Cosserat-ω + V-sector probe).
- [x] CP5 ω_local from A²_local at core.
- [x] CP6 reactance pair (C: V_inc+ω; L: Φ_link+ω̇) every window step + H=T+V.
- [x] CP7 PML-excluded, density-peak (centroid) sampling.
- [x] CP8 generative precursor (the ω-WAVE, not the finished (2,3)); matched baseline.
- [x] canonical constants imported (ALPHA, V_SNAP, V_YIELD, L_NODE).
- [x] driver-script-honesty: forward reads, NO `minimize`/fit; amplitude is IC
      design, achieved A² reported.
- [x] flag-don't-fix: the two §3 substrate points surfaced, not reconciled.
