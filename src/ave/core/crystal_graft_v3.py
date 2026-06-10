"""
Crystal-Graft v3 — the CHIRAL BELTRAMI source (the ONE physics change over v2)
==============================================================================

Re-scoped electron-genesis engine (Grant directive 2026-06-09). v2 closed the
genesis-24/crystal DOUBLE-COUNT (ω got its own Cosserat carrier — own field +
conjugate momentum π_ω + mass-gap ω₀² reactance; a planted (2,3) reads back at
rel 0.80/0.59). v2's residual was a clean C pinned to MODE-SELECTION:

    v2's buckle  f_ω = −κ̃ ∇×(g_wall·V·h·x̂)  is a FIXED-AXIS, CENTROSYMMETRIC
    director. From a radial breather it deposits ONE coherent x-axis circulation
    (winding (0,0)); and H_bel=∫ω·(∇×ω) is QUADRATIC in ω, so a scalar handedness
    sign h cannot carry charge (RH=LH≈−1.4e-15). v2 §7 named the fix: a genuinely
    chiral Beltrami/helical drive whose handedness lives in its SPATIAL STRUCTURE.

THE ONE CHANGE — the buckle director x̂  →  a force-free (A∥B) BELTRAMI field b_λ
(∇×b_λ = ±λ·b_λ). Everything else (the conserved Hamiltonian coupling, the
functional-derivative forces, the frozen-wall localization, the ω carrier, the
hardened Γ=−1 wall) is INHERITED UNCHANGED from CrystalGraftV2:

    H_couple = κ̃ ∫ g_wall(r) · V · [ b_λ(r) · (∇×ω) ] d³r,   κ̃ = pq/(p+q) = 6/5
      f_V = −κ̃ g_wall [ b_λ · (∇×ω) ]                         (back-reaction ω→V)
      f_ω = −κ̃ ∇×( g_wall · V · b_λ )                          (BUCKLE: compression→ω)

b_λ + g_wall FROZEN ⇒ H_couple exactly bilinear in (V,ω) ⇒ the leapfrog conserves
E_V+E_ω+H_couple (energize-LOCK, ave-conserved-vs-pumped), NOT a pump.

WHY THIS CARRIES CHARGE (the mechanism): b_λ is force-free, so the leading-order
sourced micro-vorticity f_ω ≈ −κ̃ g V (χλ) b_λ ⇒ ω ∝ b_λ ⇒ the deposited field
is PARALLEL to its own curl ⇒ H_bel = ∫ω·(∇×ω) ∝ χλ∫|b_λ|² is NONZERO and ODD in
the spatial handedness χ=±1. Flipping λ→−λ flips H_bel ⇒ charge=helicity carryable.

λ(p,q) = sqrt(p²/R² + q²/r²) — the torus-knot Beltrami eigenvalue (canonical,
85_kelvin_beltrami…:558/:126), α-FREE (pure geometry).

GROUNDING (source = lock): the SAME Beltrami force-free A∥B object the reactive-
entrainment/gyroscope result (2026-06-09_reactive-entrainment-source_result.md §3,
sapphire-phonon-centrifuge.md:34) found is the electron's spin-LOCK (A∥B → rigid
gyroscopic tensor = inductive shield = the Γ=−1 confinement). Source and lock are
the same object — this engine reuses its form for the source.

α-FREEDOM (CI-enforced, test_graft_v3_alpha_free.py): this module imports NO
α-bearing symbol from constants.py. κ̃=6/5=pq/(p+q) topology, V_yield≡1, λ from
geometry — all α-free. Golden-torus / α⁻¹=4π³+π²+π are EMERGENCE targets, never
inputs.
"""

from __future__ import annotations

import numpy as np

from ave.core.crystal_graft_v2 import CrystalGraftV2


class CrystalGraftV3(CrystalGraftV2):
    """v2 with the buckle director changed from a fixed x̂-axis to a frozen
    chiral BELTRAMI (force-free A∥B) field b_λ. The single mode-selection fix."""

    def __init__(
        self,
        N: int,
        *,
        source_mode: str = "abc",
        lam_sign: int = +1,
        p: int = 2,
        q: int = 3,
        **kwargs,
    ):
        """
        New args (the Beltrami source — the ONE change):
            source_mode: 'abc'    → space-filling ABC Beltrami field
                                    b=(sin λ_sZ+cos λ_sY, sin λ_sX+cos λ_sZ,
                                       sin λ_sY+cos λ_sX), ∇×b=λ_s b EXACTLY.
                                    Carries handedness + scale, NO (p,q) phase ⇒
                                    CANNOT replant a (2,3): the de-novo helicity
                                    source.
                         'torus'  → torus flux-rope carrying the (p,q) helical
                                    pitch (GEOMETRY-TEMPLATED; source-structured,
                                    explicitly NOT de-novo — a (2,3) read here is
                                    source-carried).
                         'axis'   → v2 legacy h·x̂ (regression baseline).
            lam_sign:    χ = ±1, the SPATIAL handedness of the Beltrami field
                         (λ_s = χ·λ). λ→−λ is the matter/antimatter flip. χ=0 is
                         the centrosymmetric (no-helicity) baseline.
            p, q:        the torus-knot label (2,3); sets λ(p,q) and (torus mode)
                         the pitch. NOT α.
        The director field is built by build_beltrami_director(R, r) AFTER seeding
        (so the torus geometry R,r come from the wall shell), and FROZEN.
        """
        super().__init__(N, **kwargs)
        self.source_mode = str(source_mode)
        self.lam_sign = int(np.sign(lam_sign)) if lam_sign != 0 else 0
        self.p = int(p)
        self.q = int(q)
        self._b_dir = None  # frozen Beltrami director (N,N,N,3)
        self.lam_used = 0.0
        self.source_R = None
        self.source_r = None

    # ------------------------------------------------- the Beltrami director
    def build_beltrami_director(self, R: float, r: float):
        """Build + FREEZE the chiral Beltrami director b_λ(r) at torus geometry
        (R, r). λ(p,q)=sqrt(p²/R²+q²/r²) (α-free). Stores self._b_dir and the
        source diagnostics (force-free cos-alignment, source helicity ∫b·∇×b).

        For source_mode='axis' the director is the v2 constant h·x̂ (so the parent
        buckle is reproduced exactly — regression)."""
        self.source_R = float(R)
        self.source_r = float(r)
        lam = float(np.sqrt((self.p / R) ** 2 + (self.q / r) ** 2))
        self.lam_used = lam
        lam_s = self.lam_sign * lam

        Nn = self.N
        c = (Nn - 1) / 2.0
        i, j, k = np.indices((Nn, Nn, Nn))
        X = (i - c) * self.dx
        Y = (j - c) * self.dx
        Z = (k - c) * self.dx
        b = np.zeros((Nn, Nn, Nn, 3), dtype=np.float64)

        if self.source_mode == "axis":
            # v2 legacy: constant h·x̂ (scalar handedness, NOT spatially chiral)
            b[..., 0] = self.helicity
        elif self.source_mode == "abc":
            # ABC Beltrami: ∇×b = λ_s b EXACTLY (A=B=C=1). Cubic, no torus, no
            # (p,q) phase ⇒ carries handedness χ + scale λ only (de-novo source).
            b[..., 0] = np.sin(lam_s * Z) + np.cos(lam_s * Y)
            b[..., 1] = np.sin(lam_s * X) + np.cos(lam_s * Z)
            b[..., 2] = np.sin(lam_s * Y) + np.cos(lam_s * X)
        elif self.source_mode == "torus":
            # Torus flux-rope carrying the (p,q) helical pitch (GEOMETRY-TEMPLATED).
            # Mirrors the (2,3) structure of seed_omega_known_2_3: the transverse
            # polarization direction d̂=cos(pφ)ê_R+sin(pφ)ê_z winds p× toroidally;
            # the helical phase Θ=pφ+χ·qψ gives the q× poloidal pitch. A (2,3) read
            # from this source is SOURCE-CARRIED, not de-novo (labeled as such).
            rho = np.sqrt(X**2 + Y**2)
            phi = np.arctan2(Y, X)
            u = rho - R
            v = Z
            rt = np.sqrt(u**2 + v**2)
            psi = np.arctan2(v, u)
            env = np.exp(-(rt**2) / (2.0 * (0.6 * r) ** 2)) * (rho > 2)
            beta = self.p * phi
            Theta = self.p * phi + self.lam_sign * self.q * psi
            dR = np.cos(beta)
            dz = np.sin(beta)
            amp = env * np.cos(Theta)
            b[..., 0] = amp * dR * np.cos(phi)
            b[..., 1] = amp * dR * np.sin(phi)
            b[..., 2] = amp * dz
        else:
            raise ValueError(f"unknown source_mode {self.source_mode!r}")

        # Fair-director normalization: v2's director was a UNIT vector field
        # (|h·x̂|=1). Scale b_λ by a GLOBAL scalar so its interior RMS = 1 — this
        # makes the Beltrami source a unit-scale director (comparable coupling
        # strength to v2, no inflated source) and, because it is a global scalar,
        # PRESERVES the force-free property ∇×b=λ_s b exactly (for ABC). The
        # coupling strength is then set ONLY by κ̃=6/5 (α-free), as in v2.
        m = self.interior_mask()
        rms = float(np.sqrt(np.mean(np.sum(b**2, axis=-1)[m]))) if self.source_mode != "axis" else 1.0
        if rms > 1e-12:
            b = b / rms
        self._b_dir = b
        return self.source_diagnostics()

    def source_diagnostics(self) -> dict:
        """Force-free quality (cos-alignment of b_λ with ∇×b_λ; ±1 ⇒ exactly
        force-free, sign = handedness χ) + source helicity ∫b·(∇×b) (∝χλ for a
        Beltrami field). These are SOURCE-TEMPLATE diagnostics (NOT the evolved ω
        — that is measured separately as the deposited H_bel)."""
        if self._b_dir is None:
            return {"built": False}
        b = self._b_dir
        cb = self._curl(b, self.dx)
        m = self.interior_mask()
        bn = np.sqrt(np.sum(b**2, axis=-1))
        cn = np.sqrt(np.sum(cb**2, axis=-1))
        dot = np.sum(b * cb, axis=-1)
        sig = (bn > 1e-6) & (cn > 1e-6) & m
        cos_align = float(np.mean((dot[sig]) / (bn[sig] * cn[sig]))) if sig.sum() else 0.0
        src_hel = float(np.sum(dot * m))
        return {
            "built": True,
            "source_mode": self.source_mode,
            "lam_used": self.lam_used,
            "lam_sign": self.lam_sign,
            "force_free_cos": cos_align,  # |·|≈1 ⇒ force-free; sign = χ
            "source_helicity": src_hel,  # ∫b·(∇×b) over interior (∝ χλ)
            "R": self.source_R,
            "r": self.source_r,
        }

    # ------------------------------------------ buckle with the Beltrami director
    def _buckle_forces(self):
        """v2 buckle with n̂_χ → the frozen Beltrami director b_λ:
          f_V = −κ̃ g_wall [ b_λ · (∇×ω) ]
          f_ω = −κ̃ ∇×( g_wall · V · b_λ )
        Functional derivatives of ONE bilinear coupling (b_λ, g_wall frozen) ⇒ the
        joint H conserves (energize-LOCK). If the director was not built yet, fall
        back to the parent (x̂) buckle so smoke/regression still run."""
        if self._b_dir is None:
            return super()._buckle_forces()
        g = self._wall_window()
        b = self._b_dir
        curl_omega = self._curl(self.omega, self.dx)
        # f_V = −κ̃ g (b·∇×ω)
        f_V = -self.kappa_tilde * g * np.sum(b * curl_omega, axis=-1)
        # A_vec = g·V·b  (componentwise);  f_ω = −κ̃ ∇×A_vec
        A = (g * self.V)[..., None] * b
        f_omega = -self.kappa_tilde * self._curl(A, self.dx)
        return f_V, f_omega

    def _coupling_energy(self) -> float:
        """H_couple = κ̃ ∫ g_wall·V·[ b_λ·(∇×ω) ] — the buckle ledger term with
        the Beltrami director."""
        if not (self.omega_sector_on and self.buckle_on):
            return 0.0
        if self._b_dir is None:
            return super()._coupling_energy()
        g = self._wall_window()
        b = self._b_dir
        curl_omega = self._curl(self.omega, self.dx)
        dens = self.kappa_tilde * g * self.V * np.sum(b * curl_omega, axis=-1)
        return float((dens * self.interior_mask()).sum())

    def __repr__(self):
        return (
            f"CrystalGraftV3(N={self.N}, dt={self.dt:.3e}, source={self.source_mode}, "
            f"χ={self.lam_sign}, (p,q)=({self.p},{self.q}), λ={self.lam_used:.4f}, "
            f"κ̃={self.kappa_tilde}, ω0={self.omega_gap}, step={self.step_count})"
        )
