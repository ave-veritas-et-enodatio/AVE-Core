"""
Sonic-Horizon Closure — the sharp-interface free-boundary reflector on the bulk-flow branch
============================================================================================

Subclass of `cavitation_flow.CavitationFlow2D` that opens the NAMED below-floor
closure the cavitation-core probe GATED (predecessor result §0-bis(e), Rule 12):
the `c²(ρ̄)=0` locus is treated as a **sonic horizon** — a free-boundary reflector
for bulk waves whose crossing carries a shock-class, one-way, entropy-producing
dissipation. Pre-registered in `research/2026-06-10_sonic-horizon-closure_prereg.md`.  DEMOTED 2026-08-11 — R40-B1 (dated demotion note at end of file).

WHY a subclass (substrate-native-check CP2, representation-capability):
  the predecessor `CavitationFlow2D` runs the momentum RHS on a STRICTLY-POSITIVE
  floored wave speed `c_eff² = max(c²_raw, +1e-3·c₀²)` (`cavitation_flow.py:159-163`),
  so `c²<0` was never integrated and FLASH was excluded by construction. This class
  keeps that engine INTACT (it is the CONTROL) and overrides `step()` to add the
  closure. The ONLY structural change at `chi_shock=0`, `c2_floor=0` is the clamp of
  `c_eff²` at EXACTLY zero (not +floor) below the locus — the bare reflector with no
  sink. All irreversibility is opt-in via `chi_shock` (swept apparatus knob).

THE CLOSURE (prereg §2):
  1. `c_eff² = max(c²_raw, 0)` — below `ρ̄_cav` the medium is INERT (no restoring,
     no anti-restoring runaway). A `c=0` void is automatically a `Z_bulk=ρ·c→0`  [DEMOTED 2026-08-11 - R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]
     pressure-release reflector (Γ→−1, the YM `Z_knot→0` mechanism, bulk channel)
     AND a sonic horizon (`c_eff−|u|<0`). The reflector is coefficient-free.
  2. One-way pocket mask: a cell enters the void when `ρ̄ ≤ iface_thresh`; it leaves
     only when `ρ̄ > iface_thresh + heal_width` (default heal_width=0 → the
     irreversibility comes from removed ENERGY, not a built-in barrier).
  3. Void = quiescent vapor at the floor: `ρ̄` clamped to `iface_thresh`; void KE
     removed at fraction `chi_shock` (chi=1 ⇒ fully quiescent void; chi=0 ⇒ elastic
     reflector, the in-engine LOCK control). E_diss is the one-way entropy sink.
  4. Exact EOS internal-energy ledger `U(ρ̄)` (closes the predecessor's ledger gap —
     `pressure()` had zero call sites). PE_exact replaces the linear `½c₀²∫ρ̄²` proxy.

APPARATUS KNOBS (prereg §3, CLIP suspects — swept BEFORE any verdict):
  iface_thresh (N1), heal_width (N2), chi_shock (N3), + inherited c2_floor (K1,
  now default 0), nu_art (K4), N (K6). A FLASH that TRACKS any of these is CLIP.
"""

from __future__ import annotations

import numpy as np

from ave.core.cavitation_flow import RHO_CAV, CavitationFlow2D


class SonicHorizonFlow2D(CavitationFlow2D):
    """Bulk flow with the sharp-interface sonic-horizon free-boundary closure."""

    def __init__(
        self,
        *args,
        chi_shock: float = 1.0,      # N3: fraction of void KE dissipated (1=quiescent void, physical)
        heal_width: float = 0.0,     # N2: over-pressure barrier a void needs to re-close
        iface_thresh: float = RHO_CAV,  # N1: density at which a cell is declared cavitated
        c2_floor: float = 0.0,       # K1: OVERRIDE parent default 1e-3 -> 0 (clamp c_eff^2 at exactly 0)
        **kwargs,
    ):
        super().__init__(*args, c2_floor=c2_floor, **kwargs)
        self.chi_shock = float(chi_shock)
        self.heal_width = float(heal_width)
        self.iface_thresh = float(iface_thresh)
        # one-way pocket memory
        self.cav_mask = np.zeros((self.N, self.N), dtype=bool)
        self.static_mirror = np.zeros((self.N, self.N), dtype=bool)  # calibration: held void
        # ledgers (cumulative)
        self.E_diss = 0.0       # shock-class, one-way, entropy-positive
        self.E_latent = 0.0     # reversible internal-energy released crossing (diagnostic)
        self.mass_clamp = 0.0   # cumulative |mass| added by the void-floor clamp (honesty)
        self.cav_events = 0     # cumulative cell-crossing count
        self._build_U_table()

    # ---- exact EOS internal energy U(ρ̄) (closes the ledger gap; CP6) ----
    def _build_U_table(self):
        """ε(ρ) = ρ ∫_1^ρ p(s)/s² ds, ρ=1+ρ̄, p the exact EOS integral (pressure()).
        Tabulated + validated by free-run KE+PE conservation in the driver."""
        rb = np.linspace(-0.999, 3.0, 40001)   # ρ̄ grid
        rho = 1.0 + rb                          # ρ
        # p(s) as a function of ρ̄ via the parent's exact integral pressure(ρ̄)
        p = self.pressure(rb)                   # = c0^2[ρ̄ - ½ln(1-ρ̄²)]
        integrand = p / rho**2                  # p(s)/s²  (s ≡ ρ)
        # cumulative trapezoid from ρ=1 (ρ̄=0). Find index nearest ρ̄=0.
        i0 = int(np.argmin(np.abs(rb)))
        cum = np.zeros_like(rb)
        # integrate outward both directions from i0 using trapezoid on ρ
        for i in range(i0 + 1, len(rb)):
            cum[i] = cum[i - 1] + 0.5 * (integrand[i] + integrand[i - 1]) * (rho[i] - rho[i - 1])
        for i in range(i0 - 1, -1, -1):
            cum[i] = cum[i + 1] + 0.5 * (integrand[i] + integrand[i + 1]) * (rho[i] - rho[i + 1])
        eps = rho * cum                         # ε(ρ) internal energy density
        self._U_rb = rb
        self._U_eps = eps

    def U_density(self, rho_bar):
        """Exact EOS internal-energy density ε(ρ̄) (interpolated from the table)."""
        return np.interp(rho_bar, self._U_rb, self._U_eps)

    def compression_pe_exact(self):
        """C-state via the EXACT EOS internal energy (not the linear ½c₀²∫ρ̄² proxy)."""
        return float(np.sum(self.U_density(self.rho)) * self.dx**2)

    # ---- the closure, applied each step after the inherited integration ----
    def step(self):
        # 1) inherited RK2 integration + sponge + parent clips. With c2_floor=0 the
        #    parent's c_bulk2() = max(c²_raw, 0): c_eff² is clamped at EXACTLY zero
        #    below the locus (the reflector / horizon), not at a positive floor.
        super().step()

        # If a static calibration mirror is set, enforce it (held void) and return.
        if self.static_mirror.any():
            self.rho[self.static_mirror] = self.iface_thresh
            self.u[self.static_mirror] = 0.0
            self.v[self.static_mirror] = 0.0

        # 2) one-way pocket mask update (interior only; CP7)
        below = (self.rho <= self.iface_thresh) & self.interior
        newly = below & ~self.cav_mask
        healed = self.cav_mask & (self.rho > self.iface_thresh + self.heal_width)
        self.cav_mask = (self.cav_mask | below) & ~healed & self.interior
        self.cav_events += int(np.count_nonzero(newly))

        # 4) latent diagnostic: reversible internal-energy released as cells cross to
        #    the void floor (captured BEFORE the clamp). |ε(ρ̄_before) − ε(floor)|.
        if newly.any():
            rb_before = self.rho[newly]
            d_eps = self.U_density(rb_before) - self.U_density(self.iface_thresh)
            self.E_latent += float(np.sum(np.abs(d_eps)) * self.dx**2)

        if self.cav_mask.any():
            cm = self.cav_mask
            # 3a) void-floor density clamp (vapor density). Track added mass (honesty).
            deficit = self.iface_thresh - self.rho[cm]      # >0 where rho dipped below floor
            add = np.clip(deficit, 0.0, None)
            self.mass_clamp += float(np.sum(add) * self.dx**2)
            self.rho[cm] = np.maximum(self.rho[cm], self.iface_thresh)
            # 3b) shock-class dissipation: remove chi_shock of the void KE (one-way).
            rho_full = 1.0 + self.rho[cm]
            ke_void = 0.5 * np.sum(rho_full * (self.u[cm] ** 2 + self.v[cm] ** 2)) * self.dx**2
            self.E_diss += self.chi_shock * ke_void
            self.u[cm] *= (1.0 - self.chi_shock)
            self.v[cm] *= (1.0 - self.chi_shock)
        return

    # ---- pocket observers (interior; CP7) ----
    def pocket_cells(self):
        """# interior cells currently in the one-way void (the c²≤0 pocket)."""
        return int(np.count_nonzero(self.cav_mask))

    def pocket_area_frac(self):
        return self.pocket_cells() / float(np.count_nonzero(self.interior))

    def total_energy_exact(self):
        return self.kinetic_energy() + self.compression_pe_exact()

    def ledger(self):
        return {
            "KE": self.kinetic_energy(),
            "PE_exact": self.compression_pe_exact(),
            "PE_proxy": self.compression_pe(),
            "E_diss": self.E_diss,
            "mass_clamp": self.mass_clamp,
            "pocket_cells": self.pocket_cells(),
            "cav_events": self.cav_events,
        }

    # ---- calibration: a STATIC pressure-release disk (the known mirror) ----
    def set_static_mirror(self, radius: float):
        """Pin a fixed circular void (ρ̄=iface_thresh, u=0) — the perfect-mirror reference."""
        self.static_mirror = (self.R < radius) & self.interior
        self.cav_mask = self.static_mirror.copy()
        self.rho[self.static_mirror] = self.iface_thresh
        self.u[self.static_mirror] = 0.0
        self.v[self.static_mirror] = 0.0

    # ---- handedness probe: bulk azimuthal-m acoustic OAM VORTEX (CP2 bulk-channel) ----
    def add_oam_pulse(self, m: int, r0: float, amp: float = 1e-3, width: float = 0.05,
                      inward: bool = True, carrier: float | None = None):
        """Superpose a small-amplitude CONVERGING bulk (compression) acoustic VORTEX
        carrying a genuine quadrature ``e^{imφ}`` winding (prereg §2.2). The state is
        set in quadrature: the density perturbation is the cos component of
        ``A·ring·e^{iΘ}`` while the velocity is ``u = ∇Φ`` from the sin-component
        velocity potential — so ``u`` is CURL-FREE (divergence/bulk channel, NOT a
        shear/vortical probe) yet carries a nonzero second-order acoustic OAM
        ``L₂ = ∫ρ̄(x v − y u) dA ∝ m`` whose SIGN follows sign(m).

        ``+m`` (co-handed) and ``−m`` (counter-handed) are PHYSICALLY DISTINCT
        circulations (mirror-image spirals with opposite OAM), NOT the bit-identical
        fields the previous ``dens = amp·ring·cos(m·φ)`` produced — ``cos(m·φ)`` is
        EVEN in ``m`` (``cos(mφ)=cos(−mφ)``), so the old probe could not represent
        handedness by construction. The radial carrier ``Θ = mφ + sgn·kr·r`` makes
        the winding a true chiral spiral (a pure azimuthal cos(mφ) would make ±m
        either bit-identical or a global sign-flip — both give R(+m)=R(−m) since the
        reflectance is quadratic in the field). Returns ``E_incident``.
        """
        r = self.R + 1e-12
        phi = np.arctan2(self.Y, self.X)
        ring = np.exp(-((r - r0) ** 2) / (2.0 * width**2))
        # radial carrier wavenumber (≈ one carrier wave per envelope FWHM by default);
        # sgn sets the convergence direction (inward ⇒ u_r ≈ −c0·ρ̄, as for a converging
        # acoustic pulse — recovers the previous probe's radial behaviour at the carrier).
        kr = (2.0 * np.pi / (4.0 * width)) if carrier is None else float(carrier)
        sgn = -1.0 if inward else 1.0
        # complex acoustic-vortex phase Θ = mφ + sgn·kr·r
        theta = m * phi + sgn * kr * r
        # density = Re[A·ring·e^{iΘ}]  (the cos quadrature / C-state)
        dens = amp * ring * np.cos(theta)
        # velocity potential Φ = (c0/k_tot)·A·ring·sin Θ  (the sin quadrature); u = ∇Φ
        # via the engine's own FD stencil ⇒ DISCRETELY curl-free (bulk-channel).
        k_tot = np.hypot(kr, abs(m) / max(r0, self.dx))
        Phi = (self.c0 / k_tot) * amp * ring * np.sin(theta)
        du = self._ddx(Phi)
        dv = self._ddy(Phi)
        self.rho = self.rho + dens
        self.u = self.u + du
        self.v = self.v + dv
        # linear acoustic energy of the launched pulse (compression + KE)
        e_inc = 0.5 * np.sum(self.c0**2 * dens**2 + du**2 + dv**2) * self.dx**2
        return float(e_inc)

    def oam_second_order(self):
        """Second-order acoustic OAM L₂ = ∫ρ̄·(x v − y u) dA (sign-tied to the probe m;
        the handedness-discriminating, m-odd invariant the cos(mφ) probe lacked)."""
        return float(np.sum(self.rho * (self.X * self.v - self.Y * self.u)) * self.dx**2)


# ============================================================================
# DATED DEMOTION NOTE — 2026-08-11 (R40 demotion sweep, batch 1)
# ============================================================================
# Class: DIES-WITH-THE-PHANTOM. STATUS CHANGE ONLY — no code path, constant, default or
# behaviour is altered by this note; the text above is preserved verbatim (honesty-lag
# pattern, Rule 12) and stamped in place. Nothing is deleted. This module's phantom-bearing
# DOCUMENTATION is demoted; any live re-scope of the CODE is batch 2 / the engine lane.
#
# Demoted in this file:
#   :7 — "treated as a **sonic horizon** — a free-boundary reflector for bulk waves whose crossing carries a shock-class, one-way, entropy-producing dissipation"
#       stamped in place at :9
#       why it dies (audited row rationale, verbatim): Requires propagating bulk waves crossing a
#       horizon plus a one-way entropy sink — a bulk dissipative port; both are void when the
#       compression branch is removed from the spectrum.
#
# THE ARC, COMPLETE (the framing R40 rules every demotion note carries):
#   1. The kill fired (#930) — the walk-back that closed the bulk radiative-port reading.
#   2. The premise localized to the #261 K = 2G import (G-RECON, unchallenged): the
#      compressible far-field branch was minted by a GR-imported elastic modulus, not
#      forced by the axioms.
#   3. The axioms underdetermine the bulk sector — the #935 flat-direction finding: the
#      written action conserves the Gauss function pointwise and never fixes its value.
#   4. The replacement is the RATIFIED bound-sector law — AXIOM 5, SUBSTRATE DC BIAS
#      (BC-SRC clauses S / G / Q), ratified per _orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md,
#      as reconciled by _orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md
#      (R44: the full-scope R43 record is FINAL and authoritative; the partial
#      2026-08-10-ruling-r43-sg-ratified.md is SUPERSEDED and is NOT the resolution).
#      Under the ratified law the A1 / bulk slot is a BOUND RESPONSE — mechanism gloss
#      BACK-REACTION — with no independent propagating branch, no port, and zero
#      longitudinal characteristic speed. A bulk wave speed, a bulk radiative port, a bulk
#      band-branch and a bulk transit clock therefore have no referent.
#
# STANDING NAMED-OPEN DEBT (the honest rider): the ratified axiom does NOT discharge
#   everything. THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open entry —
#   clause G's elliptic law is the STATIC ABSTRACTION of underived finite-speed bias
#   dynamics (_orchestration/2026-08-10_bias-propagation-brief.md). Where a demoted claim's
#   replacement depends on finite-speed bias dynamics, the resolution is the ratified
#   axiom WITH THAT DEBT OPEN, not a closed replacement.
#
# Records: R40 ruling _orchestration/docket-entries/2026-08-10-rulings-r40-r42.md;
#   verified worklist research/drivers/r40_sweep_worklist_verified.json;
#   scope verification _orchestration/2026-08-10_r40-sweep-scope-verification.md;
#   batch-1 record _orchestration/2026-08-11_r40-sweep-batch1.md;
#   vocabulary ruling R50 _orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md
#   (canonical: the displacement pattern u0 around a deposit is THE BOUND RESPONSE,
#   mechanism gloss BACK-REACTION; eps_11 is THE BIAS; "dress", "grade"-as-canonical-noun
#   and "halo"-for-the-physics are retired, and the owed theorem is renamed
#   THE BIAS PROPAGATION THEOREM);
#   vocabulary ruling R49(b) _orchestration/docket-entries/2026-08-10-rulings-r48-r49.md
#   ("retardation" is retired; the canonical term is PROPAGATION DELAY / FINITE PROPAGATION
#   SPEED) -- the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review.
# ============================================================================
# --------------------------------------------------------------------------
# R40 batch-2a --- NEEDS-RE-DERIVATION status note (2026-08-11)
# --------------------------------------------------------------------------
# CLASS: status demotion under R40. Mints no clm-/def-/exp-/sup-/ilk-, moves no solidity number,
# adjudicates no channel and opens no fork. Every byte of each demoted claim is preserved; the
# stamped line gains a status marker only.
#
# THE ARC, IN FOUR CLAUSES (R40's header form; clause 4 points at the LANDED artifact, not at a
# ruling record). (1) The kill fired --- the walk-back that closed the bulk radiative-port
# reading. (2) The premise localized to the imported K = 2G elastic modulus: the compressible
# far-field branch was minted by a GR-imported modulus, not forced by the axioms. (3) The axioms
# underdetermine the bulk sector --- the flat-direction finding: the written action conserves the
# Gauss function pointwise and never fixes its value. (4) THE REPLACEMENT IS THE LANDED RATIFIED
# BOUND-SECTOR LAW --- AXIOM 5, SUBSTRATE DC BIAS, clauses S (deposit), G (bias coupling / bridge)
# and Q (quiescence), canonical at manuscript/common_equations/eq_axiom_5.tex with its register
# entry in manuscript/ave-kb/common/axiom-register.md. Under clause G the A1 / bulk slot is a
# BOUND RESPONSE --- u_0 = -A_g grad(eps_11), mechanism gloss BACK-REACTION --- with no
# independent propagating branch, no port and zero longitudinal characteristic speed. A bulk wave
# speed, a bulk radiative port, a bulk band-branch and a bulk transit clock therefore have no
# referent. A_g (the bias-coupling area) is an UNVALUED-RATIFIED-CONSTANT per R48
# (manuscript/ave-kb/common/interlock-register.md): it is not valued here or anywhere, and THE
# CALIBRATION COUNT STAYS 3.
#
# STANDING NAMED-OPEN DEBT (the honesty rider). The ratified axiom does NOT discharge everything.
# THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt, stated by the axiom's own
# phase-structure paragraph, clause (c1): clause G's elliptic law is the static abstraction of
# underived finite-speed bias dynamics, and the (u,pi) no-signalling theorem does NOT cover the
# bias read --- the bias's finite propagation speed is owed, not held. Every row tagged BIAS-DEBT
# below re-derives against the ratified axiom WITH THAT DEBT STANDING, never against a closed
# replacement.
#
# VOCABULARY. Canonical nouns authored here: the bound response (u_0), the bias (eps_11), the DC
# operating point / quiescent point (Q-point); back-reaction is the mechanism gloss. 'dress',
# 'grade' as eps_11's canonical noun, and 'halo' for the physics (the physics noun is the
# near-field store / added-mass) are RETIRED by R50; 'retardation' is retired by R49(b) in favour
# of propagation delay / finite propagation speed. Corpus text quoted below is byte-exact and is
# never reworded.
#
# ROWS CARRIED IN THIS FILE (verbatim quote + verbatim banked rationale):
#
#   :22  family: Z_bulk=rho*c formula  [BIAS-DEBT]
#        QUOTE (byte-exact at HEAD): A `c=0` void is automatically a `Z_bulk=ρ·c→0` pressure-release
#        reflector (Γ→−1, the YM `Z_knot→0` mechanism, bulk channel)
#       STAMPED AT: :22
#        RATIONALE (verbatim, research/drivers/r40_sweep_worklist_verified.json): Reflection ROLE is the
#        surviving class, but Z_bulk=ρc as a formula consumes c_bulk as a propagation speed — the
#        prereg's explicit Z_bulk=ρc_bulk NEEDS-RE-DERIVATION-at-formula-level case; note it rides an
#        apparatus whose premise dies.
#        RESOLUTION: the demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that
#        slot is the bound response, so the re-derivation must be re-posed on the bound-sector
#        constitutive law (bias eps_11, bound response u_0, mechanism gloss back-reaction) rather than on
#        a compression wave. BIAS-DEBT: this row turns on finite-speed bias dynamics, so the resolution
#        is the ratified axiom WITH THE BIAS PROPAGATION THEOREM STANDING (clause (c1)) --- the
#        replacement is owed, not held.
#
# RECORDS: ruling R40 (the demotion sweep); the banked worklist
# research/drivers/r40_sweep_worklist_verified.json; the batch-0 scope verification and batch-1
# execution records in _orchestration/; this batch's record
# _orchestration/2026-08-12_r40-sweep-batch2a.md.
# --------------------------------------------------------------------------
