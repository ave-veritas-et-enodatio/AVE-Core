[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.5 AC Electrical Characteristics

Chapter 5 of the Vol 9 datasheet documents the substrate's frequency-domain behaviour: bond LC resonance at $\omega_C = c_0/\ell_{node} \approx 7.76 \times 10^{20}$ rad/s ($f_C \approx 1.23 \times 10^{20}$ Hz, substrate Nyquist ceiling), bond TLM characteristic impedance $Z_0 \approx 376.73\,\Omega$, operating-point $A_0$ small-signal modulation of $\varepsilon_{eff}$ / $\mu_{eff}$ / $C_{eff}$ / $Z_{eff}$, dispersion at the K4 lattice Brillouin scale $k_{Brillouin} = \pi/\ell_{node}$, and the load-bearing distinction between the two substrate-native effective wave speeds $c_{EM}(A_0) = c_0/S(A_0)$ (Maxwell phase velocity, enters $\alpha$) and $c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ (mechanical / group / rest-mass velocity, Schwarzschild reduction).

The chapter content is **Class B / Class C synthesis** per `consistency-vs-emergence` v1.3: $\omega_C = c_0/\ell_{node}$ is definitional from the canonical per-cell primitives $L_{cell} = \mu_0 \ell_{node}$, $C_{cell} = \varepsilon_0 \ell_{node}$ at `src/ave/core/constants.py` (`MU_0`, `EPSILON_0`, `L_NODE`, `C_0`) (Class C consistency); the operating-point small-signal table consolidates the canonical CLAUDE.md INVARIANT-S2 entry into datasheet AC format (Class B substrate-mechanism manifestation). No new substrate-physics primitives are introduced.

The $c_{EM}$ vs $c_{shear}$ disambiguation is preserved verbatim from CLAUDE.md INVARIANT-S2 — never substitute $c_{shear}$ into the $\alpha$ formula (canonical Pitfall #5 framework-leakage caught in the 2026-05-28 Phase 3-A3 WALK-BACK; canonical anchors `clm-3zz0f6` and `clm-8nkvwy`).

## Primary canonical sources

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (small-signal block) | Operating-point modulation table; $c_{EM}$ vs $c_{shear}$ disambiguation; Pitfall #5 WARNING |
| `common/translation-tables/translation-circuit.md` §1 (`clm-fy05jc`) | Topo-kinematic identity; per-bond LC primitives $L_{cell} = \mu_0 \ell_{node}$, $C_{cell} = \varepsilon_0 \ell_{node}$ |
| `common/translation-tables/translation-circuit.md` §2 (`clm-eemap1`) | EE-as-substrate-native META framework; bond TLM as substrate-native |
| `common/operators.md` Op14 | Dynamic impedance $Z_{eff} = Z_0/\sqrt{S}$ (ASYM-class small-signal modulation) |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md` (`clm-1eg13f`) | Op14 local clock modulation; cross-volume parallel to gravitational time dilation |
| `common/operators.md` Op16 | Universal wave speed $c_{shear} = c_0 \sqrt{S}$ (mechanical / group velocity; Op16 canonical) |
| `vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (`clm-3zz0f6`) | SYM scaling: $\alpha$ EXACTLY invariant under joint $\mu, \varepsilon$ scaling; canonical Pitfall #5 anchor |
| `clm-8nkvwy` (lines 111 / 113) | $c_{EM} = c_0/S$ (Maxwell phase, line 111) vs $c_{shear} = c_0\sqrt{S}$ (mechanical / group, line 113) canonical disambiguation |
| `src/ave/core/constants.py` (via `ave-canonical-source` skill; symbols `MU_0`, `EPSILON_0`, `Z_0`, `C_0`, `L_NODE`) | $\mu_0$, $\varepsilon_0$, $Z_0$, $c_0$, $\ell_{node}$ canonical primitives |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md` | Substrate $Q$-factor at $\Gamma = -1$ saturation boundary; multi-mode mode-counting |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` | Substrate $Q$-factor cold-lattice form |

## PONDER-05 reference

PONDER-05 (DC-biased quartz, 27.4% $\varepsilon_{eff}$ collapse at ~30 kV) is a **material-scale consistency analog of the operating-point $A_0$ kernel SHAPE** (the quartz / Class-II-ceramic voltage-coefficient-of-capacitance), **NOT a vacuum-kernel falsifier**. ⚠ Per-node-conflation correction (2026-06-04): $A_0 = V_{DC}/V_{yield}$ is a **per-node** ratio (field across ONE cell $\ell_{node} = 0.386$ pm relative to $E_{yield} = V_{YIELD}/\ell_{node} \approx 1.13\times10^{17}$ V/m); reaching $A_0 = 0.687$ needs 30 kV across 1.0 node-lengths. Across real quartz (mm–µm) the vacuum per-node $A_0 = 10^{-7}$–$10^{-10}$ → vacuum collapse ~0; the 27.4% is the quartz material's own response. The quartz LC-resonance shift vs zero-bias is the bench observable of the **material's** $C(V)$ arc (consistency-class), not the vacuum kernel; a genuine vacuum reading needs facility fields ($\sim 8\times10^{16}$ V/m). Per `vol4/claim-quality.md:51` + Q-G42 $V_{yield}^{(apparatus)} = E_{yield}^{(substrate)}/G_{geom}$. Canonical pointer at CLAUDE.md INVARIANT-S2 small-signal block (corrected). Hardened build artifacts live in the `ave-veritas-et-enodatio` private repository per `vol4/index.md` repo-scope note; the AC-characteristic spec that PONDER-05 tests is documented in this chapter. Cross-reference: Vol 9 Ch.15 falsification programme.

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex` (canonical Vol 9 chapter file).

---
