# Genesis v10–v15 — parameter provenance audit (2026-06-12)

**Status:** AUDIT + v15a-derive implementation + production HEAL-CONFIRMED (2026-06-12)  
**Program ledger:** `research/2026-06-12_genesis-program-status.md`  
**Production result:** `research/2026-06-12_genesis-v15-nucleation-latent_result.md`  
**Trigger:** Grant — reject ad-hoc “tuning”; require AVE-native derivation under axioms + named calibrations  
**Skills:** ave-canonical-source, ave-driver-script-honesty, consistency-vs-emergence, ave-evidence-framing-discipline

---

## §1 — Calibration inputs (honest Class-B / Class-E — not derived from K4 alone)

| Symbol | Source | Class |
|:---|:---|:---|
| $\alpha$ | `constants.ALPHA` — Class-B closed-form at named identification | B |
| $\ell_{\mathrm{node}}$ | $\hbar/(m_e c)$ | Identity |
| $G$, $H_\infty$ | Machian / Vol 3 Ch 1 chain | E (joint op-point) |
| $\Omega_{\mathrm{freeze}}$ | Cosmic IC | E initial data |

**Rule:** These may appear as imports; they are **not** fit knobs for genesis gates.

---

## §2 — Vacuum native unit system (load-bearing)

Per `natural-units-cheatsheet.md` + `constants.py` N_* block:

| Native unit | Value | Engine note |
|:---|:---|:---|
| $\ell_{\mathrm{node}}$ | 1 | Spatial unit |
| $\tau_{\mathrm{relax}}=\ell/c$ | 1 | One scatter step coarse unit |
| $m_e c^2$ | 1 | Energy unit |
| $V_{\mathrm{YIELD}}$ | 1 | **Not** $V_{\mathrm{SNAP}}=1$ in engine |
| $V_{\mathrm{SNAP}}$ | $1/\sqrt{\alpha}\approx 11.7$ | Engine normalizes to `V_SNAP_NATURAL=1` |
| $r_{\mathrm{yield}}=V/V_{\mathrm{YIELD}}$ | $A_{\mathrm{vsnap}}/\sqrt{\alpha}$ | Use for amplitude scoping |
| $\xi_{\mathrm{topo}}=e$ | $\sqrt{\alpha}$ | Native charge unit |

**Normalization warning:** `amp=0.5` in engine = $0.5\,V_{\mathrm{SNAP}}$ = $5.85\,V_{\mathrm{YIELD}}$ native — massively above yield (`lattice-impedance-decomposition.md` §2).

## §3 — Fully derived (axiom + constants, native units)

| Parameter | Native value | Derivation |
|:---|:---|:---|
| `A_YIELD_SQ` (vsnap) | $2\alpha$ | Regime I/II knee; $r_{\mathrm{yield}}=\sqrt{2}$ |
| Ω_freeze seed | $r_{\mathrm{yield}}=1$ | $\sqrt{\alpha}\,V_{\mathrm{snaps}}=1\,V_{\mathrm{YIELD}}$ |
| Nucleation target | $r_{\mathrm{yield}}=\sqrt{2}$ | Same knee |
| `TAU_RELAX_NATIVE` | 1 | `tau-relax-derivation.md` |
| `H_native` | $H_\infty\cdot\tau_{\mathrm{relax,SI}}$ | Time conversion |
| `ρ_Λ_native` | $\rho_{\mathrm{SI}}\cdot\ell_{\mathrm{node}}^3/m_e$ | Mass/volume conversion |
| Cosmic deposit | $3H_{\mathrm{nat}}\rho_{\Lambda,\mathrm{nat}}$ per cell per τ | `cmb-thermal-attractor.md` |
| Local `ΔE_native/step` | $(E_{\mathrm{target}}-E_{\mathrm{seed}})/(N_\tau\cdot 2)$ | Pair §3; $E$ in $m_e c^2$ |
| `chi_shock` | 0.5 | v10 prereg D4 |

---

## §3 — Prereg-locked thresholds (not physics derivations — gate design)

| Gate | Value | Prereg |
|:---|:---|:---|
| P13 `E_frac` ≥ 0.55 | v13 | DRAFT |
| P13 `width` ≤ 2.0 | v13 | DRAFT |
| P15 `A2` ≥ $0.9 \times 2\alpha$ | v15 | DRAFT |
| P11 persist floors | v11 | DRAFT — Grant freeze pending |
| P12 transport floors | v12 | DRAFT |

**Classification:** Emergence-test **acceptance criteria**, not substrate predictions.

---

## §4 — Discrete engineering analogues (disclosed — NOT continuum-derived)

These are **consistency-class** discrete stand-ins for continuum mechanisms. Failure implicates the **analogue**, not the axiom.

| Parameter | Module | Value | Corpus target | Status |
|:---|:---|:---|:---|:---|
| `DISCRETE_TAU_STEPS` | v11 | 50 | $\tau_{\mathrm{relax}}$ = 1 scatter coarse unit | Documented O(50) map to v10 `n_persist` |
| `Z_BULK_WALL` | v13 | 12.0 | $\Gamma_{\mathrm{bulk}}\to -1$ Op3 stiffening | Prereg “discrete analogue” |
| `EXTERIOR_LEAK` | v13 | 0.04 | Hard-container leak | Prereg |
| `z_half_frac`, `r_max_frac` | v13 | 0.14, 0.18 | Compton tubular pocket | Geometry fraction — **not** from $\ell_{\mathrm{node}}$ on finite L |
| `DA2_MIN` | v10 | 1e-4 | Rate-gate apparatus floor | v10 prereg |
| Photon plant `amp` | v12–15 | 0.5 | P6 amp sweep arm | Prereg Lane B control |
| `plant_23` width_frac | v12 | 0.10–0.12 | P5 hosting | Phase-space seed |

**v14b open:** pocket-frame peak metric (comoving read).

---

## §6 — Cosmic vs local latent (critical honesty)

| Path | Formula | Per-step / yield ratio | Use in v15 |
|:---|:---|:---|:---|
| **Cosmic mean** | $3H_\infty\rho_\Lambda \cdot \ell_{\mathrm{node}}^3 \cdot (\ell_{\mathrm{node}}/c)$ | $\sim 10^{-40}$ of `E_YIELD_KINETIC` | **Computed, logged, NOT injected** |
| **Local pair ramp** | Budget $E_{\mathrm{pair}}(\sqrt{\alpha}) \to E_{\mathrm{pair}}(2\alpha)$ over $N_\tau$ | O(1) in dimensionless engine units | **Active injection path** |

**Corpus alignment:** `op14-cosmic-horizon-profile.md` lists independent $\rho_{\mathrm{latent}}$ derivation as **OPEN**. Mean cosmological flux cannot nucleate one cell in one $\tau_{\mathrm{relax}}$ window — that is a **scale honesty** result, not a bug to tune away.

**Local ramp** is the discrete Lane A test of prereg §3 (saturation seed + latent pulse), **not** a claim that $m_e c^2$ equals mean $\rho_{\mathrm{latent}}$ per step.

---

## §7 — Bugs fixed in v15a-derive

| Issue | Before | After |
|:---|:---|:---|
| `q_latent` | Ad-hoc 0.4 | Removed — `delta_e_per_step` from provenance |
| Heal cell B | `seed_single_node` (false seed) | `seed_mode="none"` |
| Seed amp | 0.08 hardcoded | $\sqrt{\alpha}$ from constants |
| `n_steps` / `n_latent` | 220 / 90 ad-hoc | $N_\tau$ + $4N_\tau$ from v11 map |

---

## §8 — Remaining open (do not assert derived)

1. $\rho_{\mathrm{latent}}$ from substrate energetics alone (`clm-s4n33u` plumber Q1)  
2. $\Gamma_{\mathrm{cryst}}$ fraction per step (`D2-RHO-LAMBDA` matrix)  
3. $Z_{\mathrm{bulk,wall}}$ from $\Gamma=-1$ impedance (Q-G43 atom-scale)  
4. Compton pocket fractions from $\ell_{\mathrm{node}}$ on srs (needs L-dependent closure)  
5. v15b $V_{\mathrm{inc}}$ — K4 engine, not srs proxy  

---

## §9 — Code artifacts

| File | Role |
|:---|:---|
| `src/ave/core/genesis_lane_a_provenance.py` | Canonical derivation + cosmic/local paths |
| `src/ave/core/chiral_lattice_v15.py` | Consumer — no free `q_latent` |
| Driver JSON | `provenance` block on every run |

---

## §10 — Classification ledger

| Claim | Class |
|:---|:---|
| Cosmic latent negligible per cell per $\tau$ | **Consistency** (honest scale comparison) |
| Local ramp budget from $2\alpha$ knee | **Consistency** (prereg discrete analogue) |
| P15 pass/fail | **Emergence candidate** (lane discrimination) |
| Bulk wall Z=12 | **Consistency** (discrete Γ analogue) |

---

## §11 — Production read (2026-06-12)

Native derived budget deposited ($9.5\,m_e c^2$ over 50 latent steps on pair). Cell A cosmic IC: $r_{\mathrm{yield}}^*\approx 0.357$ (FAIL P15-N). Photon control: $r_{\mathrm{yield}}^*\approx 2.90$ without latent. **Verdict HEAL-CONFIRMED** — not a parameter-tuning failure.

**Next:** v15a-ablation (latent-phase χ=0, snap-OFF) per program status §5-F1.
