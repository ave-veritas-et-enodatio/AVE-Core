# Phase 1 — Moduli Pinning Self-Consistency Check

**Status:** Phase 1 wrap-up task. Publication-rigor check of the three moduli pinnings proposed in [`02_lagrangian_derivation.md`](02_lagrangian_derivation.md) §9.
**Prerequisites:** `00_` – `03_`.

This document verifies (or corrects) the three pinnings $\{G, G_c, \gamma\}$ of the Cosserat moduli in $\mathcal{L}_{\text{AVE}}$ (eq. 6.1 of `02_`). The three proposed pinnings in `02_` §9 are:

1. $G = \rho_{\text{vac}}$ (from $c_{\text{photon}} = 1$ in natural units).
2. $G_c = 3\gamma$ (from Cosserat characteristic length = $\ell_{\text{node}}$).
3. $\gamma = 1$ (from $\alpha^{-1}$ recovery at Q-factor normalization).

The three consistency checks (i), (ii), (iii) of `02_` §9.1:

- **(i)** No additional dimensional constants enter the Ch 8 recovery.
- **(ii)** Cosserat characteristic length equals K4 lattice pitch exactly.
- **(iii)** Photon dispersion non-dispersive at leading order, deviates at $k \sim 1/\ell_{\text{node}}$.

The check turns up **one correction needed in `02_` §9** (factor-of-3 error + misattributed rationale for Pinning 2), documented in §5 below. All three pinnings hold self-consistently after the correction.

---

## §1  Dimensional framework

In SI units:

| Quantity | Dimensions | Natural units (AVE) |
|---|---|---|
| $\varepsilon_{ij}$ (strain) | dimensionless | dimensionless |
| $\kappa_{ij}$ (curvature-twist) | $\mathrm{rad/length}$ | dimensionless (via $\ell_{\text{node}} = 1$) |
| $G, G_c$ (shear moduli) | $\mathrm{J/m^3}$ | dimensionless (via $E_\star = 1$) |
| $\gamma, \beta_c, \gamma'_c$ (bending moduli) | $\mathrm{J/m}$ | dimensionless |
| $\rho_{\text{vac}}$ (mass density) | $\mathrm{kg/m^3}$ | dimensionless |
| $J$ (micro-inertia) | $\mathrm{kg/m}$ | dimensionless |

The ratio $\gamma / G_c$ has dimensions $\mathrm{(J/m)/(J/m^3)} = \mathrm{m^2}$. The square root is the **Cosserat characteristic length**:

$$\boxed{\ell_{\text{Cos}} := \sqrt{\gamma / G_c}}$$

This is the length scale at which the Cosserat bending term $\gamma\,|\nabla\boldsymbol{\omega}|^2$ becomes comparable to the Cosserat antisymmetric-shear term $G_c\,|\varepsilon^a|^2$, i.e., the scale at which Cosserat corrections to ordinary Cauchy elasticity become $O(1)$.

**This is the cleanest dimensionally-natural definition**, derivable from matching the coefficients in the dispersion relation (§4.1) or from the crossover of the static Green's function (§4.2).

---

## §2  Pinning 1 — $G = \rho_{\text{vac}}$ from $c_{\text{photon}} = 1$

The photon in AVE is the transverse Cosserat shear wave (`vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex` line 139). For the linearized $\mathbf{u}$-sector wave equation under $\boldsymbol{\omega} = 0$ (no Cosserat corrections), the transverse dispersion is

$$\rho_{\text{vac}}\,\ddot{u}_\perp = G\,\nabla^2 u_\perp \Longrightarrow \omega_{\text{freq}}^2 = (G/\rho_{\text{vac}})\,k^2$$

so the transverse-photon speed is $c_\perp = \sqrt{G/\rho_{\text{vac}}}$.

Natural units set $c = 1$, hence

$$\boxed{G = \rho_{\text{vac}}}$$

**Status: pinned, no free parameter.** Equivalently, the units of §1 of `02_` are chosen so that $G = \rho_{\text{vac}} = 1$ when expressed in AVE natural units. ✓

---

## §3  Pinning 2 — $G_c$ from $\ell_{\text{Cos}} = \ell_{\text{node}}$ (with correction)

`02_` §9 proposed: *"Cosserat characteristic length $\ell_{\text{Cos}} = \sqrt{(\gamma_c + \beta_c + \gamma'_c)/G_c}$ must equal $\ell_{\text{node}}$ (Axiom 1 Nyquist). Under isotropic bending, $\ell_{\text{Cos}} = \sqrt{3\gamma/G_c} = 1$, giving $G_c = 3\gamma$."*

**This is wrong by a factor of 3.** The issue: the formula naively sums three bending moduli, but the physical Cosserat characteristic length uses the *coefficient of* $|\nabla\boldsymbol{\omega}|^2$ *in the isotropic energy functional*, not the sum of three independent moduli that happen to all be $\gamma$ in the isotropic ansatz.

### 3.1  Correct derivation

From `02_` §4, under the isotropic bending ansatz $\gamma_c = \beta_c = \gamma'_c = \gamma$, the curvature-energy density reduces to

$$W_\kappa(\kappa) = \gamma\,\kappa_{ij}\kappa_{ij} = \gamma\,|\nabla\boldsymbol{\omega}|^2$$

The coefficient of $|\nabla\boldsymbol{\omega}|^2$ in the isotropic energy functional is $\gamma$ (not $3\gamma$). The dimensionally-natural Cosserat length is

$$\ell_{\text{Cos}}^2 = \frac{\text{bending modulus coeff of } |\nabla\boldsymbol{\omega}|^2}{\text{shear modulus coeff of } |\varepsilon^a|^2} = \frac{\gamma}{G_c}$$

Setting $\ell_{\text{Cos}} = \ell_{\text{node}} = 1$:

$$\boxed{G_c = \gamma}$$

### 3.2  Rationale correction

`02_` §9 wrote: *"$G_c$: pinned by the $\nu_{\text{vac}} = 2/7$ operating point."*

**This attribution is wrong.** $\nu_{\text{vac}} = 2/7$ is a *translational* Poisson ratio, derived from $K = 2G$ (bulk and shear of the Cauchy sector, §3.1 of `02_`). It does not directly constrain $G_c$ (the Cosserat antisymmetric-shear modulus, a different quantity entirely).

The correct rationale for Pinning 2 is: $G_c$ is pinned by requiring the Cosserat characteristic length $\ell_{\text{Cos}} = \sqrt{\gamma/G_c}$ to equal $\ell_{\text{node}}$, which is Axiom 1's Nyquist scale. Cosserat corrections to Cauchy behavior become $O(1)$ exactly at the lattice scale — physically, this says the Cosserat microstructure "lives on" the K4 graph, not on a coarser or finer scale.

### 3.3  Queue item

`02_` §9's factor-of-3 error and mis-attributed rationale are queued as a correction in `DOCUMENTATION_UPDATES_QUEUE.md` item [5] (added at end of this document).

---

## §4  Pinning 3 — $\gamma = 1$ from $\alpha^{-1}$ recovery

At the Golden Torus ground state, the multipole decomposition of the Cosserat bending energy (§6 of `03_existence_proof.md`) gives

$$\mathcal{E}_{\text{ground}} = \gamma\,\big(4\pi^3 + \pi^2 + \pi\big)$$

The AVE identification $\alpha^{-1} = \mathcal{E}_{\text{ground}}$ (Ch 8 §3) requires

$$\gamma \cdot (4\pi^3 + \pi^2 + \pi) = 4\pi^3 + \pi^2 + \pi \Longrightarrow \boxed{\gamma = 1}$$

This is the "Q-factor normalization" choice — by setting $\gamma = 1$, the bending-energy scale is identified with the dimensionless Q-factor of the dielectric-ropelength electron.

**Status: this is a unit convention, not a physical derivation.** One could equivalently take $\gamma$ dimensional and set $\mathcal{E}_{\text{ground}} = \alpha^{-1}$ with appropriate dimensional factors; the content is the same. AVE's natural-unit convention (§1 of `02_`) picks $\gamma = 1$ as the cleanest choice. ✓

---

## §5  Consistency checks

### 5.1  Check (i): No additional dimensional constants in Ch 8 recovery

The Ch 8 Q-factor $4\pi^3 + \pi^2 + \pi$ is pure geometry (numerical factors of $\pi$ from multipole integrations on the Clifford torus). The recovery chain from $\mathcal{L}_{\text{AVE}}$ is:

$$\text{Lagrangian }(G, G_c, \gamma, \rho_{\text{vac}}, J) \xrightarrow{\text{static GS}} \text{bending energy at Golden Torus } (\gamma \cdot 4\pi^3 + \gamma \cdot \pi^2 + \gamma \cdot \pi)$$

With $\gamma = 1$, the energy is purely geometric. $G$ and $\rho_{\text{vac}}$ don't appear (static — no kinetic contribution). $J$ doesn't appear (same reason). $G_c$ enters *only* if $\varepsilon^a \neq 0$ at the ground state, which would happen if the SU(2) microrotation deviated from the geometric macrorotation; at the Golden-Torus ground state this is not the case (the configuration is purely microrotational, $\mathbf{u} \equiv 0$, and $\varepsilon^a$ vanishes identically).

**(i) PASSES.** ✓

### 5.2  Check (ii): Cosserat characteristic length = K4 lattice pitch

With Pinning 2 corrected ($G_c = \gamma$): $\ell_{\text{Cos}}^2 = \gamma/G_c = 1$, so $\ell_{\text{Cos}} = 1 = \ell_{\text{node}}$.

**(ii) PASSES** (after the factor-of-3 correction). ✓

### 5.3  Check (iii): Photon dispersion non-dispersive at leading order

For the fully-coupled linearized wave equation (transverse $\mathbf{u}$ with Cosserat back-reaction), the dispersion relation has the form

$$\omega_{\text{freq}}^2 = c^2 k^2 \cdot \bigg[1 + O\big((\ell_{\text{Cos}} k)^2\big)\bigg]$$

At leading order (small $k$, long wavelengths), $\omega_{\text{freq}} \approx c k$ (non-dispersive). Corrections appear at $k \sim 1/\ell_{\text{Cos}}$, which with the corrected Pinning 2 is $k \sim 1/\ell_{\text{node}}$ — the K4 Nyquist cutoff.

This matches the AVE claim that the vacuum is non-dispersive at leading order and begins to show lattice structure only at wavelengths $\lesssim \ell_{\text{node}}$ (cf. `vol_4_engineering/chapters/11_experimental_falsification.tex` on GRB dispersion bounds).

**(iii) PASSES.** ✓

---

## §6  Final self-consistent pinnings

After the §3 correction:

$$\boxed{
\begin{aligned}
G &= \rho_{\text{vac}} \quad\text{(from } c_\text{photon} = 1\text{)} \\
G_c &= \gamma \quad\text{(from } \ell_\text{Cos} = \ell_\text{node}\text{)} \\
\gamma &= 1 \quad\text{(from } \alpha^{-1} \text{ Q-factor normalization)}
\end{aligned}
}$$

In AVE natural units: $G = G_c = \gamma = \rho_{\text{vac}} = 1$.

This leaves **no free parameters in the Lagrangian for the static ground-state problem.** All three Cosserat moduli and the translational shear modulus collapse to unity in natural units. The micro-inertia $J$ is the remaining free parameter, relevant only for dynamics (Phase 3 timestepping), and can be pinned separately by matching the transverse-microrotation mode speed (the "optical" branch of the Cosserat dispersion) — deferred to Phase 3.

---

## §7  Corrections to queue

Appending to `DOCUMENTATION_UPDATES_QUEUE.md`:

**Item [5] — `02_lagrangian_derivation.md §9`: Pinning-2 factor-of-3 error + mis-attributed rationale.**

- Change: Replace the formula $\ell_{\text{Cos}} = \sqrt{3\gamma/G_c}$ with $\ell_{\text{Cos}} = \sqrt{\gamma/G_c}$; replace $G_c = 3\gamma$ with $G_c = \gamma$; replace the "pinned by $\nu_{\text{vac}} = 2/7$ operating point" rationale with "pinned by $\ell_{\text{Cos}} = \ell_{\text{node}}$ (Axiom 1 Nyquist match)." Retain the rest of §9 structure.
- Why: The factor of 3 came from naively summing three bending moduli that are identified in the isotropic ansatz; the dimensionally-natural characteristic length uses the coefficient of $|\nabla\boldsymbol{\omega}|^2$ in the isotropic energy functional, which is $\gamma$, not $3\gamma$. The $\nu_{\text{vac}}$ attribution was a confusion with the translational Poisson ratio (which pertains to $K/G$, not to $G_c$).
- Self-consistency check of the corrected pinnings is this document (`04_`).

---

## §8  Status

- All three proposed pinnings hold self-consistently **after correcting §9 of `02_`**.
- All three consistency checks (i), (ii), (iii) pass.
- No free parameters remain in the Lagrangian for the static electron ground-state problem.
- The micro-inertia $J$ is the only parameter left to pin for Phase-3 dynamics; it is separately derivable from the Cosserat optical-mode dispersion.

**Phase-1 wrap-up status:** moduli pinning check complete. Remaining Phase-1 wrap-up items: rigorous completion of existence/uniqueness (queue [4]); Reading (a) ↔ Reading (b) equivalence check; Reading (c) observable search.
