# SPICE-CVR constitutive-loop test — pre-registration (FROZEN 2026-06-13)

> **STATUS: FROZEN** — Grant implementor directive 2026-06-13. Freeze bins before any code run.
> **Scope:** local constitutive law only (loop / remanence / impedances / α-transformer). **NOT** spatial topology, winding, or genesis.
> **Canon fence:** `manuscript/ave-kb/common/translation-tables/translation-circuit.md` §7; coverage `CVG-NAR-001` (topology out of scope).
> **Doctrine:** `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` §1 — zero-drive persistence = mass analogue.

**Lane:** implementor `analysis/2026-06-13-spice-cvr-constitutive-loop` off `origin/main`.

**If REMANENT-LOOP lands:** proves the **retention mechanism** exists in silico — **does not make an electron.**

---

## 0. Question (one sentence)

Does the vacuum's **Level-2 constitutive law** enclose a hysteresis loop with **zero-drive remanence** ($B_r$ at $H=0$ ferrite analogue), or only dissipation / anhysteretic elasticity?

---

## 0.1 Load-bearing distinction (design around this)

| Phenomenon | Loop area $\oint$ | $B_r$ at $H\to 0$ | Mass analogue |
|:---|:---:|:---:|:---|
| **Anhysteretic** (L0) | 0 | 0 | No |
| **Pinched memristor** (L1) | $>0$ (rate-dependent loss) | **0** | **No** — lossy, not retaining |
| **Bistable / snap** (L2) | $>0$ | $\neq 0$ (rate-gated) | **Candidate** |

The documented $\tau_{\mathrm{relax}}$ ODE $dS/dt=(S_{\mathrm{eq}}-S)/\tau_{\mathrm{relax}}$ (`tau-relax-derivation.md` §3) **returns to** $S_{\mathrm{eq}}$ when drive stops → **pinched** → $B_r=0$ **by construction**. Implementing L1 and seeing a loop does **not** answer D2 remanence — only dissipation.

**Remanence requires** a latching element (rate-gated snap, double-well, or domain latch) — **L2 discriminator**.

---

## 1. Ladder arms (frozen)

| Arm | Model | Isolates |
|:---|:---|:---|
| **L0** | Instantaneous $S_{\mathrm{eq}}(r)=\sqrt{1-r^2}$ (current varactor-only `.lib`) | Harness null; $\oint=0$, $B_r=0$ |
| **L1** | Level-2 memristor ODE on $S$; drive-rate sweep $\omega\tau$ from $\ll 1$ to $\sim 1$ | Dissipation without remanence (predict pinched) |
| **L2** | L1 + rate-gated snap / latch on down-crossing | D2(b) discriminator |

**Drive:** sinusoidal normalized stress $r(t)=r_{\mathrm{amp}}\sin(\omega t)$, $r_{\mathrm{amp}}\in[0.5,0.9]\times$ yield band (log achieved $r$).

**Pre-gate (mandatory log):** $\omega\tau_{\mathrm{eff}}$ per arm. Canonical $\tau_{\mathrm{relax}}=\ell_{\mathrm{node}}/c\approx 1.288\times 10^{-21}$ s is below SPICE timestep — harness uses **dimensionless** $\omega\tau$ with $\tau_{\mathrm{eff}}=1$ native unit unless ngspice scaled-TAU arm explicitly logged.

---

## 2. Observables (executable)

| Metric | Definition |
|:---|:---|
| $\mathcal{A}_\oint$ | Shoelace area $\oint S\,dr$ on steady-state cycle 2+ in $(r,S)$ plane |
| $B_r$ | $1 - S(r=0,\,\text{down-cross})$ after steady state ($S_{\mathrm{eq}}(0)=1$) |
| `pinched` | $B_r < \epsilon_B$ with $\epsilon_B = 10^{-3}$ |
| `omega_tau` | $\omega \cdot \tau_{\mathrm{eff}}$ (dimensionless) |

---

## 3. Frozen verdict bins (ordered)

| Bin | Executable criterion |
|:---|:---|
| **ANHYSTERETIC** | L2: $\mathcal{A}_\oint < \epsilon_A$ AND $B_r < \epsilon_B$ at all swept $\omega\tau$ → loop gap fundamental at constitutive level; $\sigma$-only (D2a); remanence needs topology (out of SPICE scope) |
| **DISSIPATIVE-ONLY** | L1/L2: $\mathcal{A}_\oint \geq \epsilon_A$ but $B_r < \epsilon_B$ → lossy-reactive; no mass-memory |
| **REMANENT-LOOP** | L2: $\mathcal{A}_\oint \geq \epsilon_A$ AND $B_r \geq \epsilon_B$ at some $\omega\tau$ (rate-gated) → snap constitutive loop; D2→(b) vindicated in silico |
| **REGIME-LIMITED** | $\omega\tau$ grid does not reach $\sim 1$ cleanly OR numerical artifact (document) |

Thresholds: $\epsilon_A = 10^{-6}$, $\epsilon_B = 10^{-3}$ (native $S$ units).

Every bin = **assertion in driver JSON** — no gate-as-docstring.

---

## 4. Hypotheses (`consistency-vs-emergence`)

| ID | Statement | Class |
|:---|:---|:---|
| H0 | L0 reads $\mathcal{A}_\oint=0$, $B_r=0$ | consistency-check (harness null) |
| H1 | L1 $\mathcal{A}_\oint$ monotone in $\omega\tau$; $B_r=0$ (pinched) | consistency-check (documented gap) |
| H2 | L2 adds $B_r>0$ only when snap armed | **emergence-test** (D2 discriminator) |
| H3 | Q$=1/\alpha$ match if tested | definitional calibration — **not headline** |

---

## 5. Implementation map

| Artifact | Path |
|:---|:---|
| Memristor `.lib` | `src/ave/solvers/spice_models/ave_vacuum_cell.lib` |
| ODE harness | `src/ave/solvers/spice_cvr_loop.py` |
| Driver | `src/scripts/vol_4_engineering/spice_cvr_loop_sweep.py` |
| Keeper tests | `src/tests/test_spice_vacuum_cell.py`, `src/tests/test_spice_cvr_loop.py` |
| Result | `research/2026-06-13_spice-cvr-constitutive-loop_result.md` |
| Figures | `assets/figures/spice_cvr_loop_*.png` |

**Constants:** `ave.core.constants` — `TAU_RELAX_SI`, `V_YIELD`, `V_SNAP`; no hardcoded yield.

---

## 6. Out of scope

- Electron manufacture / $(2,3)$ winding / genesis IC
- LOOP GAP rank-4 lattice harness (parallel track)
- Promoting Q$=1/\alpha$ as AVE-distinct discovery (`device-circuit-models.md:81`)

---

## 7. Caveats (carry, do not promote)

1. $\tau_{\mathrm{relax}}\approx 1.3\times 10^{-21}$ s — slow SPICE frequency gives $\mathcal{A}_\oint\approx 0$ by construction (harness null, not physics null).
2. Scaled-$\tau$ ngspice arms must log `tau_scale` and `omega_tau`.
3. REMANENT-LOOP $\neq$ electron.

---

## 8. Skills (mandatory)

`ave-prereg` · `consistency-vs-emergence` · `ave-driver-script-honesty` · `ave-canonical-source` · `ave-evidence-framing-discipline` · `substrate-native-check`

---

## 9. Grant ratification

- [ ] Bins frozen as stated
- [ ] L2 snap form acceptable for D2 discriminator
- Date: ___
