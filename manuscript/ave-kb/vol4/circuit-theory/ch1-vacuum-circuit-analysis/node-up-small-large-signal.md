[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-vca7r1]
-->

## Node-Up Small- and Large-Signal Response of the Vacuum LC Tank

The substrate cell is a single LC tank. Its two reactive grades respond to **different
drive variables**: the capacitive ($\varepsilon$) grade is a **varactor keyed on VOLTAGE**
$V$ (field $E$), while the inductive ($\mu$) grade is a **relativistic inductor keyed on the
circulating CURRENT** $I$ ([`relativistic-inductor.md`](relativistic-inductor.md):15,:18,
substitution $V\to I$). This duality — same Axiom-4 kernel, two different keyed arguments —
fixes the **operating-point** (large-signal) state of each grade independently, and therefore
fixes the **small-signal** index a probe sees. The asymmetry under a *static external* field
is the load-bearing consequence: a static $\mathbf{B}$ leaves the $\mu$ grade unloaded.

## §1 — The LC-tank node and the two keyed reactances

Each substrate cell is a resonant LC tank ($L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$,
$\omega_C = 1/\sqrt{L_{cell}C_{cell}} = c_0/\ell_{node}$). Both reactive elements saturate through
the **single** Axiom-4 kernel $S(A)=\sqrt{1-(A/A_{yield})^2}$, but they are keyed on **different**
drive variables:

> **[Resultbox]** *The keyed-argument duality*
>
> $$
> \underbrace{C_{eff}(V) = \frac{C_0}{S(A_V)}, \quad A_V = \frac{V}{V_{yield}}}_{\varepsilon\text{-grade: VARACTOR, keyed on VOLTAGE}}
> \qquad\qquad
> \underbrace{L_{eff}(I) = \frac{L_0}{S(A_I)}, \quad A_I = \frac{I}{I_{max}}}_{\mu\text{-grade: RELATIVISTIC INDUCTOR, keyed on CURRENT}}
> $$
>
> with $V_{yield}\approx 43.65$ kV and $I_{max}=\xi_{topo}\,c\approx 124.4$ A
> ([`relativistic-inductor.md`](relativistic-inductor.md):15,:18).

The two forms are the same kernel under the substitution $V\to I$, $V_{yield}\to I_{max}$ — *"both
are projections of the single Axiom 4 kernel onto the electric and magnetic sectors,
respectively"* ([`relativistic-inductor.md`](relativistic-inductor.md):18). The physically
load-bearing fact is **which argument keys which grade**:

- The $\varepsilon$-grade (capacitive / transverse-T2 permittivity) responds to the **field
  amplitude** $V\sim E$ — a *potential* variable. A DC bias is a real operating point.
- The $\mu$-grade (microrotational / Cosserat-B inductive) responds to the **circulating
  current** $I$ — a *rate/flux* variable, $I\propto \oint \mathbf H\cdot d\boldsymbol\ell$ sustained
  by the vacuum's own circulation. By Lenz, internal circulation is induced only by $\partial\mathbf
  B/\partial t \ne 0$; a *static* external $\mathbf B$ (sustained by the magnet's current, not the
  vacuum's) carries no $dI/dt$ and induces **no** internal vacuum circulation.

> **Coordinate discipline (A46).** The kernel arguments $A_V$, $A_I$ are **phase-space / reactance**
> quantities (operating-point along the Axiom-4 arc), not real-space lattice-Cartesian field
> magnitudes. The $\mu$-grade is loaded by the *circulation* $I$, not by $|\mathbf B|$ at a cell.
> A test (or solver) that keys $\mu$-saturation on the static $|\mathbf B|$ magnitude measures the
> wrong coordinate — see §4 and the VCA-R01 code note in §5.

$B_{SNAP}=1.89\times10^9$ T is **not** a rival kernel argument for the $\mu$-grade: it is an
**energy-density** scale, fixed by $B_{SNAP}^2/2\mu_0 = m_ec^2/\ell_{node}^3 = 1.0$ (exactly the
soliton rest-energy density). The $\mu$-grade saturates on $I/I_{max}$, not $B/B_{SNAP}$.

## §2 — Large-signal operating point per grade (the three regimes R1/R2/R3)

The operating point is the large-signal state $(S_\varepsilon, S_\mu)$ the two grades settle into
under a given drive. Three regimes span the cases relevant to gravity, the bench, and the magnet:

| Regime | Drive | $S_\varepsilon$ | $S_\mu$ | $Z_{eff}$ | Small-signal $\delta n$ |
|---|---|---|---|---|---|
| **R1** symmetric internal | both grades (internal $\mathbf E$ **and** $\mathbf B$, e.g. mass-soliton) | $S$ | $S$ | $Z_0\sqrt{\mu_0 S/\varepsilon_0 S}=Z_0$ (invariant) | $\delta n = 1/S - 1$ (isotropic; reflectionless) |
| **R2** static-E route | static $\mathbf E$ only ($\partial\mathbf B/\partial t=0$) | $<1$ | $1$ | $Z_0\sqrt{S_\mu/S_\varepsilon}=Z_0/\sqrt{S_\varepsilon}$ (changes) | $\delta n\approx\tfrac14(E/E_{yield})^2$ ($\Gamma\ne0$) |
| **R3** static-B | static $\mathbf B$ only ($\partial\mathbf B/\partial t=0$) | $1$ | $1$ (no internal circulation) | $Z_0$ (unchanged) | $\delta n_\mu = 0$ **EXACTLY** |

- **R1 (symmetric internal loading)** is the canonical INVARIANT-S2 W6 operating point
  (`manuscript/ave-kb/CLAUDE.md`:75): when *both* sectors are driven, $S_\varepsilon=S_\mu=S$, so
  $Z=Z_0$ stays invariant and the boundary is reflectionless — Symmetric Gravity. A small-signal
  probe sees the common-mode index $\delta n = 1/S - 1$.
- **R2 (static-E / bench / HIBEF route)** is the Op14 Meissner-asymmetric case: a static $\mathbf E$
  has no $\partial\mathbf B/\partial t$ to load the $\mu$ grade, so it loads $\varepsilon$ only.
  $Z$ changes → $\Gamma\ne0$ → the vacuum-impedance-mirror bench mechanism. This is the **E-route**,
  and it is where the leading $\delta n\approx\tfrac14 A_V^2$ (and the OQ-1 par−perp differential
  $-\tfrac12 A_V^2$) lives. Verified sweep: $\delta n\approx\tfrac14(E/E_{yield})^2$ ($\mu$ unloaded).
- **R3 (static-B)** is the magnet case. $\partial\mathbf B/\partial t = 0$ ⟹ no internal vacuum
  circulation ⟹ $I_{vac}=0$ ⟹ $A_I=0$ ⟹ $S_\mu=1$ ⟹ $\mu_{eff}=\mu_0$ ⟹ $\delta n_\mu = 0$
  **exactly**. Verified flat across $2.5\,\text{T}\to1\,\text{kT}$: the $\mu$-grade index shift is
  identically zero, independent of static field strength.

## §3 — Small-signal probe → $\delta n$

## §4 — The static-field asymmetry result

## §5 — Derived-vs-asserted ledger

---
