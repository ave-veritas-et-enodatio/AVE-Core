[↑ Ch.7: Stellar Interiors and Neutrino Oscillation](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-o6kgkz]
-->

---

## Stellar Regime Classification

Each stellar object occupies a well-defined position on the universal regime map via the gravitational control parameter $\varepsilon_{11} = 7GM/(c^2 r)$:

| **Object** | $\varepsilon_{11}$ | **Regime** | **Physical consequence** |
|---|---|---|---|
| Solar surface | $1.486 \times 10^{-5}$ | I | Standard GR; $\Delta S < \alpha$ |
| Red giant ($5\,M_\odot$, $100\,R_\odot$) | $7 \times 10^{-7}$ | I | Linear optics |
| White dwarf (Sirius B) | $1.81 \times 10^{-3}$ | I | Gravitational redshift $\sim 10^{-4}$ |
| Neutron star (1.4 $M_\odot$, 10 km) | 1.46 | IV | Ruptured topology; no static solution |
| Black hole at $r_s$ | 3.50 | IV | Complete lattice rupture |

All terrestrial and main-sequence stellar physics operates deep in Regime I ($\Delta S < \alpha$), validating the use of unmodified Einstein gravity for all solar system applications.

The gravitational control parameter $\varepsilon_{11}$ uses the same seven-mode compliance factor derived from $\nu_{vac} = 2/7$.

> **Correction (2026-08-01 — factor-7 residual).** The solar-surface row previously read $2.1 \times 10^{-6}$ = $GM_\odot/(c^2R_\odot)$, factor-7 low against the $\varepsilon_{11} = 7GM/(c^2r)$ definition above; corrected to $7GM_\odot/(c^2R_\odot) = 1.486\times10^{-5}$. Full provenance + the routed white-dwarf question in [`domain-catalog.md`](../../../vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md). The red-giant ($7\times10^{-7}$), neutron-star (1.46) and black-hole (3.50) rows already carry the 7 and are unchanged; the **white-dwarf (Sirius B) row is left as-is and routed** — $3\times10^{-4}$ matches $GM/(c^2R) = 2.59\times10^{-4}$ (the measured gravitational redshift its own consequence-column cites) rather than $7GM/(c^2R) = 1.81\times10^{-3}$, at the $M = 1.018\,M_\odot$ / $R = 5800$ km Sirius B parameters tabulated in [`white-dwarf-gravitational-predictions.md`](../../../vol3/gravity/ch20-white-dwarf-predictions/white-dwarf-gravitational-predictions.md) — which prints the **with-7** value $1.81\times10^{-3}$ for the same body, so the two leaves disagree by exactly the factor under audit.

> **Resolution (2026-08-02 — Grant ruling D8, verbatim [sic]: *"2. correct plus note"*).** The white-dwarf row is **corrected to $1.81\times10^{-3}$** — the with-7 strain $7GM/(c^2R) = 1.8148\times10^{-3}$ at the tabulated Sirius B parameters ($M = 1.018\,M_\odot$, $R = 5800$ km), matching the value the companion [`white-dwarf-gravitational-predictions.md`](../../../vol3/gravity/ch20-white-dwarf-predictions/white-dwarf-gravitational-predictions.md)`:32` already carried. The *"left as-is and routed"* disposition in the 2026-08-01 note above is thereby discharged; that text is **preserved unedited per Rule 12**. **The note the ruling attaches:** the displaced $3\times10^{-4}$ was **not a rounding of the strain** — it is the one-significant-figure round of the **un-7'd** $GM/(c^2R) = 2.59\times10^{-4}$, which is the **gravitational redshift** (the **GR-predicted** $z$; the *measured* line shift is $80.65 \pm 0.77$ km/s $= 2.69\times10^{-4}$), i.e. exactly the observable this row's own *Physical consequence* cell cites ($c\,GM/(c^2R) = 77.72$ km/s; exact Schwarzschild $77.75$ km/s = the $v_{\text{GR}}$ that companion leaf quotes against Sirius B's $80.65 \pm 0.77$ km/s line shift). **The consequence cell is correct and unchanged**; the 7 is what distinguishes the strain from the redshift, not a correction to either. Full provenance + the code-site routing in [`domain-catalog.md`](../../../vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md).

> **Correction note (2026-08-03 — predicted-vs-measured; propagating the merged #830 relabel to its own flagged upstream site).** The 2026-08-01 note above calls the un-7'd $GM/(c^2R) = 2.59\times10^{-4}$ *"(the measured gravitational redshift its own consequence-column cites)"*. **That label carries the same defect the Resolution above corrects, and the same correction applies:** $2.59\times10^{-4}$ is the **GR-PREDICTED** $z$, not the measured one. Receipt, on the Sirius B parameters both notes tabulate ($M = 1.018\,M_\odot$, $R = 5800$ km): $c\,GM/(c^2R) = 77.72$ km/s, exact-Schwarzschild $77.75$ km/s — against a **measured** line shift of $80.65 \pm 0.77$ km/s $= 2.69\times10^{-4}$, i.e. $3.7\%$ higher and $(80.65 - 77.75)/0.77 = 3.8\sigma$ on the quoted uncertainty. Predicted and measured are **not interchangeable at the printed precision**. The clause's *other* assertion — that the redshift, not the strain, is the observable this table's *Physical consequence* column cites — is **correct and unaffected**; only the predicted-vs-measured word moves.
> **Why this is an additive note and not an in-place relabel.** The 2026-08-01 text is left **BYTE-UNTOUCHED**: the Resolution above states that it is *"preserved unedited per Rule 12"*, so editing it would falsify a merged sentence in this same file. Merged **#830** (`4abc407c`) reached the same conclusion from the other side — it corrected its own new prose at the Resolution and **flagged this inherited site rather than editing it**, routing the relabel forward to *"whichever lane next opens the factor-7 file set"*. This note discharges that routing in the shape the constraint allows: the defect is quoted, the correct label and its arithmetic are stated, and the preserved text stays preserved. **No physics moves** — the row value $1.81\times10^{-3}$ and the consequence cell are both unchanged.

> ↗ See also: [Ch.7: The Universal Regime Map](../../../vol1/operators-and-regimes/ch7-regime-map/index.md) — universal regime classification and control parameter definitions

---
