[↑ Ch.4 DC Electrical Characteristics](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Class B/C synthesis leaf — three-channel DC impedance assignments at K/G=2. Renders registry §3.11 for the datasheet; no new substrate primitive."
-->

## Three-Channel DC Impedances (canonical leaf)

Per the **three-impedance law** (Grant-ratified 2026-06-11; field-symbol registry §3.11; vocab-operator-unification audit §4a), $Z_0 \equiv Z_{\mathrm{EM}}$ is the **transverse-EM channel only**. Shear and bulk channels carry separate device-port impedances.

This leaf is the **source of truth** for Vol 9 Ch.4 §Three-channel acoustic impedances. LaTeX table `tab:vol9_dc_three_channel` renders this content.

**Skills applied (2026-06-12 pass):** `verify-before-cite` v1.4 · `consistency-vs-emergence` v1.3 Step 8 (**Class C** definitional table) · `ave-canonical-source` · `ave-dimensional-provenance-check` ($Z_{shear}$, $Z_{bulk}$ are $\rho\times$speed, not $Z_0$).

### Cold-lattice assignments ($K/G = 2$ operating point)

| Channel | Impedance | Typical (cold lattice) | $\Gamma$ at saturation |
|---|---|---|---|
| EM-transverse | $Z_{\mathrm{EM}} \equiv Z_0$ | $\approx 376.73\,\Omega$ | $\Gamma_{\mathrm{EM}}=0$ (SYM gravity) |
| Shear / GW | $Z_{\mathrm{shear}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ | $\rho_{\mathrm{bulk}}\,c_0$ at $S=1$ | $\Gamma_{\mathrm{shear}}\to -1$ |
| Bulk-longitudinal | $Z_{\mathrm{bulk}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}$ | $\sqrt{2}\,\rho_{\mathrm{bulk}}\,c_0$ | $\Gamma_{\mathrm{bulk}}\to -1$ |

At $K_{\mathrm{bulk}} = 2G_{\mathrm{vac}}$: $c_{\mathrm{bulk}} = \sqrt{2}\,c_0$ (bulk dilatational speed, not full P-wave). Verified: `src/tests/test_vacuum_moduli_and_channels.py` (lines 66–70, 108–112).

### Canonical sources

| Anchor | Content |
|---|---|
| `src/ave/core/constants.py` | `Z_0`:98, `RHO_BULK`:646, `G_VAC`:654, `V_LONG`:658 |
| [`z0-derivation.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) | $Z_{\mathrm{EM}} = Z_0$ derivation |
| [`bulk-impedance-at-saturation-boundary.md`](../../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md) | $\Gamma_{\mathrm{bulk}}=-1$ at $r_{\mathrm{sat}}$ |
| [`device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md) | Electron TIR barriers = bulk channel, not EM $\Gamma$ at $Z_0$ |
| Ch.9 mechanical characteristics | $\rho_{\mathrm{bulk}}$, $G_{\mathrm{vac}}$, $\nu_{\mathrm{vac}}=2/7$ |

### Discipline note

Electron confinement uses **bulk-channel** ports (Fig. `fig:vol9_circuit_electron_barrier`). Equating particle TIR with EM short circuit at $Z_0$ is a **mis-scope** (vocab audit §4b #4).

### Verify-before-cite audit log (2026-06-12)

| Quantity | Source | Match |
|---|---|---|
| $Z_0 \approx 376.73\,\Omega$ | `constants.py` symbol `Z_0` (`np.sqrt(MU_0/EPSILON_0)`) | ✓ |
| $c_{\mathrm{bulk}}=\sqrt{2}\,c_0$ | `test_vacuum_moduli_and_channels.py`:66–70 | ✓ pytest gate |
| $\Gamma_{\mathrm{EM}}=0$ SYM | `clm-3zz0f6` / `electron-bh-isomorphism.md`:24 | ✓ |

---
