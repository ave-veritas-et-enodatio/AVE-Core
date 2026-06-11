"""
Annihilation / Evaporation engine additions (Phase-2 of the 2026-06-11 prereg)
==============================================================================

`research/2026-06-11_annihilation-evaporation_prereg.md` (frozen ALONE @
b883c9b4): the REVERSE reaction of the v6 condensation channel ledger — two
converged v6-class dilatation masses, opposite drive helicity, energized
relative translation, COAST to encounter.

ENGINE-LINEAGE HARD CONSTRAINT (prereg header): every annihilation-phase
addition is a NEW method/parameter that DEFAULTS to the v6 byte-identical path.
This subclass adds NO step() override and NO new EOM term — `step()` is the
inherited `UnifiedGenesisEngine.step()` verbatim. The additions are:

  imprint_drift(...)        the §4.2 NEW capability: a drift velocity imprinted
                            on V_prev as an INITIAL CONDITION (CP10 — boundary/
                            IC, NOT a bulk closing force; ave-conserved-vs-
                            pumped: energized ONCE, then coasts). The exact
                            analog of seed_photon's group-velocity imprint
                            (crystal_engine.py:323-326): a rigid mover
                            V(x,t)=f(x−vt) has V(x,t−dt)=V+v·dt·∇V, so
                            V_prev += v·dt·∇V  ⇒  ∂_tV += −v·∇V.
  drive_chiral_photon_at()  per-object chiral drive at an arbitrary center that
                            imprints w_prev ADDITIVELY. The inherited
                            seed_photon ASSIGNS w_prev components
                            (crystal_engine.py:325-326), so a SECOND drive call
                            would clobber the first photon's group-velocity
                            imprint (a large spurious ∂_t w on photon A). For a
                            single call on a fresh (w≡0) engine the additive
                            form is value-identical to the inherited one
                            (keeper-tested).
  windowed observers        per-object FIELD reads (mass, photon spin, ω-AM,
                            reactance pair) over a region mask — the F0c/K-
                            HANDED/K-MASS probes. Pure reads; mutate nothing.

substrate-native-check: CP1 (no minimization — all dynamics inherited), CP9
(every observer reads the EVOLVED field), CP10 (the drift is an initial
condition; the saturation walls stay boundary conditions).
"""

from __future__ import annotations

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine


class AnnihilationEngine(UnifiedGenesisEngine):
    """UnifiedGenesisEngine + transport-IC imprint + per-object windowed probes.
    NO step() override — inherited physics byte-identical by construction."""

    # ------------------------------------------------ per-object chiral drive
    def drive_chiral_photon_at(self, center, helicity: int = +1,
                               sigma: float = 5.0, wavelength: float = 8.0,
                               amplitude: float = 0.05, axis: int = 2):
        """Additive per-object chiral photon drive (the §4.1 two-object build).

        Identical construction to the inherited seed_photon/drive_chiral_photon
        EXCEPT w_prev is accumulated ADDITIVELY (+=) instead of assigned (=),
        so two drives at independent centers coexist, each keeping its own
        group-velocity imprint. On a fresh engine (w≡0, w_prev≡0) one call is
        value-identical to the inherited drive (keeper: K-DRIVE-EQUIV)."""
        self.helicity = float(helicity)
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r2 = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
        env = np.exp(-r2 / (2.0 * sigma ** 2))
        direction = [0.0, 0.0, 0.0]
        direction[axis] = 1.0
        d = np.asarray(direction, dtype=float)
        s = i * d[0] + j * d[1] + k * d[2]
        kk = 2.0 * np.pi / wavelength
        ax1 = (axis + 1) % 3
        ax2 = (axis + 2) % 3
        h = float(helicity)
        self.w[..., ax1] += amplitude * env * np.cos(kk * s)
        self.w[..., ax2] += amplitude * env * h * np.sin(kk * s)
        # additive group-velocity imprint (one phase back, the inherited form)
        self.w_prev[..., ax1] += amplitude * env * np.cos(kk * s + kk * self.c_T * self.dt)
        self.w_prev[..., ax2] += amplitude * env * h * np.sin(kk * s + kk * self.c_T * self.dt)
        # FOC bookkeeping (same fields drive_chiral_photon sets; cosmetic)
        self.foc_axis = int(axis)
        self.drive_helicity = int(np.sign(helicity)) or 1
        self.bemf_arm = False
        self.tau_zx_arm = False
        self._bemf_work = 0.0
        self._tau_zx_work = 0.0

    # ----------------------------------------------------- transport imprint
    def imprint_drift(self, v_vec, region_mask=None) -> dict:
        """§4.2: energize a rigid drift velocity v on the V-sector inside
        `region_mask` as an INITIAL CONDITION (then COAST — no closing force).

        V(x,t)=f(x−vt) ⇒ V(x,t−dt) = V(x,t) + v·dt·∇V  ⇒  V_prev += v·dt·∇V
        (equivalently ∂_tV += −v·∇V). Returns the energized-KE bookkeeping
        (the §5 ledger's KE_approach), measured FROM the conserved functional
        (gross-vs-field: a field read, not an accumulator)."""
        v = np.asarray(v_vec, dtype=float)
        if region_mask is None:
            region_mask = np.ones_like(self.V, dtype=bool)
        ke_before = self.bulk_energy_conserved(True)
        gx, gy, gz = np.gradient(self.V, self.dx)
        adv = v[0] * gx + v[1] * gy + v[2] * gz
        self.V_prev = self.V_prev + self.dt * adv * region_mask
        ke_after = self.bulk_energy_conserved(True)
        return {
            "v_vec": [float(x) for x in v],
            "KE_cons_before": float(ke_before),
            "KE_cons_after": float(ke_after),
            "KE_approach": float(ke_after - ke_before),
        }

    # ------------------------------------------------- windowed field probes
    def half_masks(self, axis: int = 0):
        """Two half-box interior masks split at the grid midplane along `axis`
        (object A side = lower indices, object B side = upper). Pure geometry."""
        idx = np.indices((self.N, self.N, self.N))[axis]
        m = self.interior_mask()
        lo = m & (idx < self.N // 2)
        hi = m & (idx >= self.N // 2)
        return lo, hi

    def windowed_mass_cons(self, mask) -> float:
        """The conserved-functional V-sector energy restricted to `mask` (the
        per-object T1 mass read; CP2 functional, the v6 D11 lesson)."""
        pV = self.bulk_velocity()
        c_eff_sq = self.c_eff_squared(self.V)
        gx, gy, gz = np.gradient(self.V, self.dx)
        dens = 0.5 * pV ** 2 / np.maximum(c_eff_sq, 1e-30) \
            + 0.5 * (gx ** 2 + gy ** 2 + gz ** 2)
        return float(np.sum(dens * mask))

    def windowed_photon_spin(self, mask, axis: int = 2) -> float:
        """Per-object photon axial spin S_φ = ∫_mask (w × ∂_tw)·n̂ dV — the
        K-HANDED probe (must separate ±h on the fresh two-object seed)."""
        piw = (self.w - self.w_prev) / self.dt
        s_dens = np.cross(self.w, piw)[..., axis]
        return float(np.sum(s_dens * mask) * self.dx ** 3)

    def windowed_L_omega(self, mask, axis: int = 2) -> float:
        """Per-object ω-carrier axial AM over `mask` (about the GRID axis —
        the global-ledger contribution, not an object-frame spin)."""
        pw = (self.omega - self.omega_prev) / self.dt
        if axis == 2:
            Ln = self._bx * pw[..., 1] - self._by * pw[..., 0]
        elif axis == 1:
            Ln = self._bz * pw[..., 0] - self._bx * pw[..., 2]
        else:
            Ln = self._by * pw[..., 2] - self._bz * pw[..., 1]
        return float(np.sum(Ln * mask) * self.dx ** 3)

    def windowed_reactance_pair(self, mask) -> dict:
        """F0c: the C-state (∫V²) and L-state (∫(∂_tV)²) of the bulk reactance
        pair over `mask` — recorded EVERY step over the encounter window so a
        lock-vs-unbind verdict has the complete pair."""
        pV = self.bulk_velocity()
        return {
            "C2": float(np.sum((self.V ** 2) * mask)),
            "L2": float(np.sum((pV ** 2) * mask)),
        }

    # ------------------------------------------------------ regime witnesses
    def strain_max_interior(self) -> float:
        """max A = max|V|/V_yield over the interior — the §1.5/§10-D1 overlap-
        rupture witness in the DILATATION channel (r₃ = 1.0)."""
        return float(np.max(np.abs(self.V) * self.interior_mask()) / self.V_yield)

    def rho_min_interior(self) -> float:
        """min ρ̄ over the interior — the §1.5 rupture witness in the CAVITATION
        channel (RHO_CAV = −1/φ ≈ −0.618)."""
        return float(np.min(np.where(self.interior_mask(), self.rho_bar, np.inf)))

    def field_momentum_x(self) -> float:
        """V-sector field momentum P_x = −∫ (∂_tV)(∂_xV)/c_eff² dV (interior) —
        the transport/momentum witness (weighted consistently with the
        conserved functional). A coasting mover holds it; the K-TRANSPORT probe."""
        pV = self.bulk_velocity()
        gx = np.gradient(self.V, self.dx, axis=0)
        c_eff_sq = self.c_eff_squared(self.V)
        dens = -pV * gx / np.maximum(c_eff_sq, 1e-30)
        return float(np.sum(dens * self.interior_mask()) * self.dx ** 3)

    def x_profile_peak_count(self, frac_of_max: float = 0.25) -> int:
        """Count of distinct local maxima of the y,z-integrated interior V²
        profile along x, above `frac_of_max`·peak — the one-blob-vs-two-blobs
        classifier witness (MERGE vs BOUNCE/PASS-THROUGH), from the field."""
        m = self.interior_mask()
        prof = np.sum((self.V ** 2) * m, axis=(1, 2))
        if prof.max() <= 0.0:
            return 0
        bar = frac_of_max * prof.max()
        peaks = 0
        for i in range(1, len(prof) - 1):
            if prof[i] > bar and prof[i] >= prof[i - 1] and prof[i] > prof[i + 1]:
                peaks += 1
        return peaks

    def x_centroid_V2(self) -> float:
        """|V|²-weighted x-centroid over the interior (grid units) — the
        transport trajectory witness (does the object MOVE?)."""
        m = self.interior_mask()
        w2 = (self.V ** 2) * m
        tot = float(np.sum(w2))
        if tot <= 0.0:
            return float((self.N - 1) / 2.0)
        i = np.indices((self.N, self.N, self.N))[0]
        return float(np.sum(w2 * i) / tot)
