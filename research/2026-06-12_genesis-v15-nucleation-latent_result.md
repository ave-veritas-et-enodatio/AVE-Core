# Genesis v15 — Nucleation from Latent Heat Result (PRODUCTION — 2026-06-12)

> **Prereg:** `research/2026-06-12_genesis-v15-nucleation-from-latent_prereg_DRAFT.md` (DRAFT)  
> **Program ledger:** `research/2026-06-12_genesis-program-status.md`  
> **Provenance audit:** `research/2026-06-12_genesis-parameter-provenance-audit.md`  
> **Native units:** `natural-units-cheatsheet.md`; engine `genesis_lane_a_provenance.py`  
> **Context:** `research/2026-06-12_scale-spectrum-saturation-drag-vs-confinement.md`  
> **Driver:** `python src/scripts/vol_1_foundations/chiral_lattice_v15_genesis.py`

## Implementation

| Artifact | Path |
|:---|:---|
| v15 integrator | `src/ave/core/chiral_lattice_v15.py` |
| Native provenance | `src/ave/core/genesis_lane_a_provenance.py` |
| Tests | `src/tests/test_chiral_lattice_v15.py` (6/6 PASS) |
| JSON | `assets/sim_outputs/genesis_v15_nucleation_latent.json` |

---

## Unit system

**Vacuum native:** $\ell_{\mathrm{node}}=c=m_e=\hbar=\tau=1$; $E_{\mathrm{unit}}=m_e c^2$; $V_{\mathrm{YIELD}}=1$.

Reported amplitudes:

- $r_{\mathrm{yield}}^* = V_{\mathrm{vsnap}}^*/\sqrt{\alpha}$ (native yield amplitude)
- $A^2_{\mathrm{vsnap}}^*$ = engine `A2_seed_peak` ($V/V_{\mathrm{SNAP\_NATURAL}}$)²

---

## Derived inputs (no free `q_latent`)

From JSON `provenance` (production L=10, 250 steps):

| Quantity | Value |
|:---|:---|
| Injection path | `local_pair_ramp_native` |
| Seed $r_{\mathrm{yield}}$ | 1.0 |
| Target $r_{\mathrm{yield}}$ (knee) | $\sqrt{2}\approx 1.414$ |
| $E_{\mathrm{seed,pair}}$ | 2.5 native |
| $E_{\mathrm{target,pair}}$ | 12.0 native |
| $E_{\mathrm{deficit}}$ | 9.5 native |
| $\Delta E_{\mathrm{native}}$/step/pair | 0.095 |
| $N_{\mathrm{latent}}$ | 50 (= `DEFAULT_TAU_STEPS`) |
| P15 floor $r_{\mathrm{yield}}$ | $\geq 1.342$ |
| Cosmic $3H\rho_{\mathrm{latent}}$ / cell / τ | $4.95\times 10^{-72}$ native — **ratio to yield $5.8\times 10^{-71}$** (not injected) |

---

## P15 — production battery

| Cell | latent | seed | wall | $r_{\mathrm{yield}}^*$ | $A^2_{\mathrm{vsnap}}^*$ | $E_{\mathrm{frac}}$ | width× | P15-N |
|:---|:---:|:---:|:---:|---:|---:|---:|---:|:---:|
| **A cosmic IC** | ON | pair | ON | **0.357** | 0.00093 | 1.000 | 2.94 | FAIL |
| B heal | OFF | none | OFF | 0.000 | 0.00000 | 1.000 | — | FAIL |
| C photon compare | OFF | photon | ON | **2.903** | 0.0615 | 1.000 | 0.97 | FAIL |
| D latent no wall | ON | pair | OFF | 0.373 | 0.00102 | 1.000 | 12.30 | FAIL |
| E single-node | ON | single | ON | 0.432 | 0.00136 | 1.000 | — | FAIL |

**P15-H heal:** PASS — zero seed stays cold.  
**Photon ablation:** PASS — cell C fails P15-N (photon arm excluded by gate design).  
**Wall Δ$E_{\mathrm{frac}}$ (A−D):** $\approx 0$.

**VERDICT:** **HEAL-CONFIRMED** (prereg §6 taxonomy)

---

## Sub-read (honest)

1. **Derived native budget is deposited** ($9.5\,m_e c^2$ over 50 steps) but pair reaches only $r_{\mathrm{yield}}^*\approx 0.36$ vs floor 1.34 — **scatter + χ-snap during latent window** likely dissipates faster than accretion.
2. **Lane B dominates amplitude:** photon `plant_23` at `amp=0.5` reaches $r_{\mathrm{yield}}^*\approx 2.9$ without latent — expected in native units (`amp=0.5` $V_{\mathrm{SNAP}} = 5.85\,V_{\mathrm{YIELD}}$).
3. **Cosmic mean flux cannot nucleate one cell in one τ** — corpus $\rho_{\mathrm{latent}}$ derivation still OPEN; local pair ramp is the correct discrete Lane A test.
4. **Not ENGINE-GAP from ad-hoc knobs** — v15a-derive removed free parameters; failure is physics/engine-structure on open srs.

**Classification:** Emergence candidate **not landed**; HEAL-CONFIRMED strengthens manufacture (Lane B) program.

---

## Comparison to prior v15a pass (pre-native)

| | Pre-native (`q_latent`) | v15a-derive (native) |
|:---|:---|:---|
| Verdict | ENGINE-GAP | HEAL-CONFIRMED |
| Cell A $A^2_{\mathrm{vsnap}}^*$ | 0.00057 | 0.00093 |
| Heal cell | False seed bug | `seed_mode=none` correct |
| Provenance | Ad-hoc | `genesis_lane_a_provenance.py` |

---

## Next (documented in program status §5)

| Priority | Item |
|:---|:---|
| **F1** | v15a-ablation — latent phase χ=0, snap-OFF (derived, not tune) |
| **F2** | v14b — pocket-frame peak metric |
| **F3** | v15b — K4 `V_inc` gate |
| **F4** | Grant freeze v15 prereg + native-units § |

---

## Commands

```bash
./.venv/bin/pytest src/tests/test_chiral_lattice_v15.py -q
./.venv/bin/python src/scripts/vol_1_foundations/chiral_lattice_v15_genesis.py --smoke
./.venv/bin/python src/scripts/vol_1_foundations/chiral_lattice_v15_genesis.py
```
