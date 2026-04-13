[↑ Ch.3 HOPF-01 Chiral Verification](index.md)
<!-- leaf: verbatim -->

## The Falsification Protocol

1. **Fabrication:** Order a single 160$\times$120 mm, 2-layer FR-4 panel from JLCPCB ($\varepsilon_r = 4.3 \pm 0.05$, 1.6 mm thickness, 1 oz Cu, ENIG finish) with unplated stitching holes. Thread 24 AWG enameled magnet wire through the holes following the silkscreen guide, creating five 3D torus knots plus the meander control. Solder wire starts to the SMA feed pads.

2. **Calibration:** Perform SOL (Short-Open-Load) calibration of the VNA at the SMA reference plane.

3. **Measurement (Air):** Sweep each of the six antennas individually in air. Record $f_{res}$ (the deepest S$_{11}$ dip below $-10$ dB). Repeat 10 times per antenna, rotating the cable to average connector noise.

4. **Measurement (Oil):** Submerge the entire board in a glass dish of mineral oil ($\varepsilon_r \approx 2.1$, transformer grade). Re-measure all six antennas. The oil changes the wave speed but **not** the topology.

5. **Measurement (Vacuum):** Place the board inside a vacuum chamber at $\sim$5 Torr. At this pressure, $\varepsilon_{air} \approx 1.000004$ --- effectively unity. The effective permittivity drops to $\varepsilon_{eff} \approx 1.294$ (enamel correction only). Connect via SMA vacuum feedthrough and re-measure all six antennas.

6. **Extract the Anomaly:** For each knot and each medium, compute:

$$
\Delta f_i = f_{measured,i} - f_{Maxwell,i}
$$

   where $f_{Maxwell}$ is the standard prediction using the measured $\varepsilon_{eff}$.

7. **Test the Scaling Law:** Plot $\Delta f / f$ vs. $pq/(p+q)$ for all five knots (plus the $pq/(p+q)=0$ control point).
   - **AVE confirmed:** $\Delta f/f$ is linear through the origin with slope $\alpha$, and *identical* in all three media (air, oil, vacuum).
   - **AVE falsified:** $\Delta f/f$ is zero, random, does not scale as $pq/(p+q)$, or differs between media.

8. **Substrate Independence:** The air/oil/vacuum comparison replaces the need for multiple PCB substrates (Rogers, duroid). The fractional shift $\Delta f / f$ must be identical in all three media---it depends only on $\alpha$ and $pq/(p+q)$, not on $\varepsilon_{eff}$.

### Three-Medium Verification

| Medium | $\varepsilon_{eff}$ | $f_{res}$ range (GHz) | $\Delta f/f$ |
|---|---|---|---|
| Vacuum (5 Torr) | 1.294 | 0.51--1.05 | $\alpha \cdot pq/(p{+}q)$ |
| Air (760 Torr) | 1.295 | 0.51--1.05 | $\alpha \cdot pq/(p{+}q)$ |
| Mineral oil | 2.265 | 0.38--0.79 | $\alpha \cdot pq/(p{+}q)$ |

A single $10 FR-4 board tested in three media provides a more powerful substrate independence check than any number of different substrates.

### Manufacturing Tolerance Rejection

A Monte Carlo analysis with $N = 5{,}000$ trials per knot sweeps over the noise sources specific to the wire-stitched form factor: wire length tolerance ($\pm 0.5$ mm), wire height variance ($\pm 0.3$ mm), and SMA connector repeatability ($\pm 200$ kHz). The residual noise is $\sim$130 kHz per knot, while the chiral signal exceeds 8.5 MHz for all knots, yielding SNR $> 74\sigma$.

### Decision Gate

| Phase | Medium | Pass Criterion | Confidence |
|---|---|---|---|
| 1 | Air | $\Delta f/f$ monotonic in $pq/(p{+}q)$, control null | Proceed |
| 2 | Oil | $\Delta f/f$ identical to Phase 1 ($\pm\sigma$) | Strong |
| 3 | Vacuum | $\Delta f/f$ identical to Phases 1&2 | Decisive |

If all three phases pass, the AVE framework has produced a genuine, zero-parameter electromagnetic prediction that no existing Maxwell solver can reproduce. If the scaling law is *not* confirmed at any phase, the chiral coupling term is falsified.

### Bill of Materials

| Item | Qty | Est. Cost |
|---|---|---|
| PCB 160$\times$120 mm, 2L FR-4, ENIG (JLCPCB, 5 pcs) | 1 lot | $12 |
| SMA edge-launch connectors (TE/Linx CONSMA003.062) | 6 | $34 |
| 50$\Omega$ SMA terminators | 5 | $15 |
| Enameled magnet wire, 24 AWG, 1 lb spool (Remington) | 1 | $14 |
| M3 hardware kit + 10 mm nylon standoffs | 1 kit | $8 |
| SMA-to-SMA cable, 30 cm, RG316 | 1 | $8 |
| Mineral oil, 500 mL, transformer grade | 1 | $10 |
| Glass dish, 9$\times$13" (Pyrex, oil bath) | 1 | $10 |
| SMA vacuum feedthrough (KF-25 flange or panel-mount) | 1 | $40 |
| **Subtotal (excl. VNA)** | | **$151** |
| LiteVNA-64 (50 kHz -- 6.3 GHz, incl. cal kit) | 1 | $100 |
| **Grand Total** | | **$251** |

---
