[↑ Ch.5 PONDER-05 DC-Biased Quartz](index.md)
<!-- leaf: verbatim -->

## The Mineral Oil Dielectric Bath

The quartz cylinder operates submerged in degassed mineral oil, providing three critical engineering advantages simultaneously.

### Corona Suppression

At $30\text{ kV}$ across a $50\text{ mm}$ gap, the applied field is $E_{app} = 0.60\text{ MV/m}$. Mineral oil has a breakdown field of $12\text{ MV/m}$, providing a $20\times$ safety margin against arcing. In contrast, air at STP has only a $5\times$ margin, and surface tracking along the quartz cylinder can produce ion-wind artifacts indistinguishable from thrust.

### Impedance Matching

The mineral oil layer ($\varepsilon_r = 2.2$, $Z \approx 254\,\Omega$) serves as a quarter-wave impedance transformer between quartz ($Z \approx 178\,\Omega$) and free space ($Z_0 = 377\,\Omega$). The ideal transformer impedance is $Z_{match} = \sqrt{Z_q \cdot Z_0} \approx 259\,\Omega$; mineral oil at $254\,\Omega$ is a $98\%$ match:

> **[Resultbox]** *Quarter-Wave Impedance Transformation*
>
> $$
> \text{Reflected power:} \quad
> \begin{cases}
>     \text{Quartz} \to \text{Vacuum (direct):} & 12.9\% \\
>     \text{Quartz} \to \text{Oil} \to \text{Vacuum:} & \sim 0.03\%
> \end{cases}
> $$

This $\sim 400\times$ reduction in reflected acoustic power ensures that the generated thrust wave efficiently radiates into the surrounding medium.

### Thermal Management

Quartz dissipates $< 0.001\text{ mW}$ at these operating conditions ($\tan\delta = 10^{-5}$). The oil bath provides additional convective cooling ($h \approx 100\text{ W/m}^2\text{K}$), rendering thermal artifacts entirely negligible. The temperature rise of the quartz surface is $< 0.001$°C even after hours of continuous operation.

---
