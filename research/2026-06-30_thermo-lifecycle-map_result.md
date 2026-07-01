# Thermodynamic-Lifecycle-Map of Dark Energy: Result (FRAMING/SCOPING)

**Status:** MAP-VERIFIED framing/scoping result 2026-06-30. This doc captures the
thermo-lifecycle-map workflow verdict (workflow `wfe1g5zjn`, HEAD `205d6e6b` on
`analysis/stage4-a1-eos-scope`) that greenlit CANONICALIZATION of the AVE
dark-energy definition into the KB + manuscript (Grant greenlit 2026-06-30). It
is a **consolidation of already-grounded corpus content** — it introduces **no
new `clm-`** and no new numerical physics. The banked leaf reuses the existing
phantom/latent-heat claim `clm-3ii690`.

**Class:** FRAMING/SCOPING (a corpus-map, not a derivation).
**Source synthesis:** thermo-lifecycle-map workflow `wfe1g5zjn` (JSON `.result`).
**Banked into:**
[`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md)
(new consolidation leaf) + `04_generative_cosmology.tex` §"Dark Energy" (lockstep paragraph).

---

## §1 — The reservoir / flow / phase map (verbatim intent, condensed)

The workflow assembled a coherent, Ax3-clean, sector-legal thermodynamic map of
the vacuum's ongoing crystallization. Its chosen frame is a **monotone de-Sitter
RUN-DOWN read as a constant-rate throughput ATTRACTOR** (Design B / reading-ii) —
NOT a chirality-ratcheted dissipative-structure engine (Design A / reading-i,
REJECTED), and NOT a closed numeric cycle (ρ_latent has ZERO numeric value; there
is no total state vector, no global conservation law, no `a(t)` evolver). The
cyclic/bounce variant is REJECTED (grep for bounce/crunch/re-melt returns zero;
corpus fate is monotone de Sitter). "Steady-state" is honest ONLY as the
asymptotic attractor of the run-down (H→H_∞, T_CMB→permanent ¾ρ_latent floor),
not a recurrence cycle and not an independently-simulated equilibrium.

**Reservoirs (6 energy stores + 2 non-energy roots):**

| Reservoir | Sector | Role |
|---|---|---|
| Un-crystallized free-store / DE "fuel" (ρ_free, ρ_latent) | ε | HIGH-POTENTIAL SOURCE consumed at the horizon frontier; ρ_latent symbolic-only |
| Crystallized-matter interior (finished LOSSLESS A1 tank) | A1 | COMPLETED SINK; ∂_t ρ_n=0; the electron lives here, paid latent heat ONCE |
| CMB / T2 transverse photon gas | T2 | ENTROPIC SINK (Ax3-compliant dS>0); permanent ¾ρ_latent floor |
| Crystallization FRONTIER (horizon phase-boundary) | cross | the ONLY dissipation locus; ∂_t A²(R_H)≠0; advances at ~c |
| Horizon vacuum-energy / de-Sitter-asymptote store (ρ_Λ, H_∞) | ε | STEADY-STATE ATTRACTOR VALUE; ρ_Λ=3H_∞²/8πG = ECHO |
| μ-sector chirality / over-bracing (u₀*≈0.187, sign-selector) | μ/ε | PARITY/sign-selector, NOT a cosmological energy reservoir |
| Substrate operating point (u₀* at K4 magic-angle, single-DOF root) | cross | parameter-space root, NOT an energy reservoir |

**Flows (8):** frontier crystallization (ε→A1 + new volume, rate H); latent-heat
expulsion to CMB (Γ=3H·ρ_latent, the reading-ii dissipation law); phantom-EoS
volume funding (w_vac=−1−ρ_latent/ρ_vac<−1); Op14 cross-sector reactive trade
(ε↔A1↔T2 at horizon, REVERSIBLE, "NOT dissipation; reactive trading"); interior
reactive cycling (finished-tank LOSSLESS null-flow, ∂_t ρ_n=0); BH knot-unraveling
(A1→latent floor, Ax4 saturation-rupture); structure-formation accretion
(τ_ind≈65.1 Myr, JWST back-solved); and the **F6 DE-tracks-matter depletion
coupling** (dQ/dt=k·n_matter, reading-i) — ABSENT-INVENTED, the single chord
candidate, UNBUILT.

**Lifecycle phases (6):** pre-crystallization ground (hot disordered ε-store) →
nucleation/symmetry-break (chiral seed, BBN-era; chirality here is PARITY not
time-arrow) → radiation era (IMPORTED, absent) → matter era (IMPORTED, a~t^0.667
absent) → ongoing quasi-steady DE-dominated genesis (NOW; frontier advances at ~c)
→ asymptotic de Sitter attractor (heat-death-as-floor; ASSERTED analytically, not
simulated).

## §2 — The arrow-of-time verdict

**RESOLVED: the arrow is the T2 ENTROPIC SINK, NOT chirality.** The chirality-
ratchet arrow is POSTULATED / ABSENT-INVENTED — it is NOT forced, and the
substrate mechanics actively ROUTE AROUND it. The only Ax3-legal, corpus-carried
arrow is **geometric entropic spreading of latent heat at the crystallization
frontier into the exponentially-growing T2 CMB photon-mode count**
([`arrow-of-time.md:16`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/arrow-of-time.md)
verbatim: "spherical wave radiation across a Cartesian grid is effectively a
one-way street"; reconvergence probability "effectively zero"). This is an
energy-conserving one-way TRANSFER into the huge T2 reservoir (dS>0), NOT a
friction loss — so it is Ax3-COMPLIANT, and it is ∝ crystallization-FRONTIER-rate
(3Hρ_latent), i.e. reading-ii by construction.

Chirality is RULED OUT as the arrow-source three grep-verified ways: (1) the
genesis freeze is mirror-SYMMETRIC —
[`trampoline-framework.md:105`](../manuscript/ave-kb/common/trampoline-framework.md)
verbatim "Mirror-image freeze-in gives left-handed universe with identical ...
physics" — a static handedness is a PARITY choice that cannot set a TIME
direction; (2) negative-search for `chiral.*ratchet|chiral.*arrow|dissipative
structure` returns zero; (3) the one measured chiral-director payment attempt
(`bemf-smoke` 2026-06-10) landed INERT — the reactive back-EMF "never pays for
its torque" because the source is undepleting; panel verdict "the missing
primitive is SOURCE DEPLETION, not reaction." The "chirality-ratchet as arrow"
must NOT be re-introduced by any future reader.

HONESTY FLAG: the corpus arrow is ASSUMED (2nd law imported as geometric-spreading),
NOT FORCED from a chiral asymmetric-bracing ratchet; and `arrow-of-time.md` lives
in vol3/CONDENSED-MATTER, used cosmologically — see §6 flag (2). WATCH:
`crystal_graft_v4.py:225` (`omega_damped = omega_new - lock_eta*corr*mm*dt`) is an
un-booked interior L_ω velocity-drain with no named T2 sink — must be adjudicated
formation-only (map-safe, reading-ii holds) vs ongoing (would force reading-i).

## §3 — The Dark-Energy definition

> **Dark Energy = the thermodynamic LATENT HEAT of the vacuum's ongoing
> macroscopic crystallization.** NOT a scalar field, NOT zero-point energy, NOT a
> horizon residual. It is the ε-sector residual un-crystallized FREE-STORE
> ("fuel") consumed at the horizon crystallization FRONTIER (rate Γ=3H·ρ_latent),
> funding the A1-channel volume-creation cost while expelling latent heat to the
> transverse CMB (T2). This is the Op14 CROSS-SECTOR TRADE made mechanical:
> w_vac = −1 − ρ_latent/ρ_vac < −1 (stable phantom, forbids Big Rip). DE sits in
> the ε-sector state space; the finished crystallized matter behind the frontier
> is a LOSSLESS A1 tank (∂_t ρ_n=0) — dissipation is FRONTIER-ONLY (reading-ii).

**Placement (sector-clean):** DE sits in the ε-SECTOR state space as the residual
un-crystallized free-store (ρ_free); its dynamical action is the Op14 cross-sector
trade at the ε-saturation event r→R_H (∂_t A²(R_H)≠0) — the ε-sector projection
of the substrate state, NOT μ-sector
([`op14-cosmic-horizon-profile.md:91`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md)).
The chiral over-bracing u₀* is a STATIC magnitude+sign living in the finished
A1/interior; it holds the (2,3) winding and is paid ONCE at the frontier — it is
NOT the DE arrow and does not continue to consume DE. DE (ε, frontier) and bracing
(interior) touch ONLY at the ∂_t A²≠0 phase-boundary. The DE=A1 writing is REFUTED
(grade-attribution + K=2G symmetry-inversion); neither surviving flow re-introduces
it.

## §4 — The honest ledger

Per `consistency-vs-emergence`: the AVE-distinct content is the DEFINITION /
MECHANISM (latent heat of crystallization), NOT the number.

| Element | Class | Status |
|---|---|---|
| Frontier crystallization ε→A1 (metric expansion = new-node genesis) | FORCED | engine-realized (`genesis_lane_a_provenance.py`) |
| Latent-heat expulsion Γ=3H·ρ_latent to CMB | FORCED (form) / ASSERTED (rate) | closure:111 "doesn't derive Γ from substrate" |
| Phantom-EoS volume funding w_vac<−1 | FORCED | first-law constraint (phantom-EoS:10,17) |
| Op14 cross-sector reactive trade (DE placement) | FORCED | op14:72,91; "NOT dissipation; reactive trading" |
| Arrow = geometric entropic-spreading into T2 CMB modes | ASSERTED | arrow-of-time:16; imported from CONDENSED-MATTER (flag 2) |
| Interior lossless null-flow (electron = finished lossless tank) | POSTULATED-NULL | Ax3+∂_t ρ_n=0; defended by negative-search, `crystal_graft_v4:225` a live counterexample |
| ρ_Λ = 3H_∞²/8πG = 9.03e-27 kg/m³ (+H_∞) | ECHO / CONSISTENCY | Friedmann projection of standard GR — closure:101 "no AVE-distinct content"; VALUE imported |
| ρ_latent numeric value | ABSENT | symbolic-only, ZERO numeric; `clm-s4n33u` solidity 0.45, build_status "input-only"; ΔE_cryst from {ℓ_node,α,G} OPEN (closure:110) |
| μ-chirality-ratchet as arrow-setter | ABSENT-INVENTED | mirror-symmetric freeze (trampoline:105); grep zero |
| reading-i dQ/dt∝n_matter (F6 depletion) | ABSENT-INVENTED | new physics AVE does not possess; photon_deplete=True DETONATES |
| Era-ordering + scale-factor laws a~t^0.5/t^0.667 | ABSENT / IMPORTED | negative-search; era ORDER imported by assumption |
| Total state vector + global conservation law | ABSENT | only LOCAL first-law + ∂_t ρ_n=0 |
| a(t) Friedmann time-evolver | ABSENT | `solve_backreaction` is static-elliptic; de Sitter fate asserted analytically |

**Bottom line:** the ρ_Λ VALUE is a CONSISTENCY-class Friedmann back-projection of
corpus H_∞ (do not headline as emergence); the DEFINITION/MECHANISM is the AVE
content; ρ_latent is symbolic-only and Γ is asserted — the whole map is
un-pressure-testable numerically until ΔE_cryst is derived.

## §5 — F6 placement (the one ΛCDM-distinct chord)

Exactly ONE ΛCDM-distinct chord lives anywhere in the map: **DE-tracks-the-
crystallization-FRONTIER (reading-ii, realized) vs DE-tracks-EXISTING-n_matter
(reading-i, F6)**. The corpus realizes ONLY the frontier form (Γ=3Hρ_latent);
the n_matter chord is the **UNBUILT F6 depletion primitive** — new physics AVE
does not possess, whose one prior attempt (`photon_deplete=True`) detonates
(indefinite Hamiltonian). F6 does NOT modify the frontier flow; it is a NEW second
dissipation channel that would drain the ε-free-store ∝ existing n_matter, routed
entropically into T2. It is the instantiation of reading-i (Prigogine dissipative
structure) vs Design B's completed lossless tank.

**F6 is the open forward-prediction handle, NOT a realized result.** Its
make-or-break gates: (1) a BOUNDED norm-preserving ε→T2 depletion primitive that
does NOT detonate (hard blocker); (2) Ax3-legality (entropic transfer THROUGH the
winding to T2, not friction on the winding); (3) coupling k + response derived
from {ℓ_node,α,G} (chord) vs hand-set (echo); (4) proton-lifetime consistency
(>10^34 yr); (5) ρ_latent numeric prerequisite (hard blocker). The chord lives in
F6's forward observable (DESI/Euclid DE-vs-matter cross-correlation), NOT inside
the lifecycle mechanics. **Cite reading-ii / frontier-only as the canonical
default; do NOT headline F6 as corpus physics.**

## §6 — Two flags surfaced (flag-don't-fix)

These are surfaced with verbatim evidence for Grant adjudication; NOT resolved here.

**FLAG 1 — Daughter-cosmology contradiction.**
[`vol9/ch12-cosmological-characteristics/index.md:23-24`](../manuscript/ave-kb/vol9/ch12-cosmological-characteristics/index.md)
FORBIDS daughter cosmologies, verbatim: "NO baby-universe black holes with
daughter cosmologies" and "NOT a daughter cosmology; NOT an inner cosmic genesis."
But
[`omega-freeze-cosmic-grain-cascade.md:122`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
ASSERTS "our cosmic substrate is the daughter K4 lattice formed inside a parent
BH," and
[`cosmic-parameter-horizon-a031-refinement.md:12`](../manuscript/ave-kb/common/cosmic-parameter-horizon-a031-refinement.md)
ASSERTS "the parent black hole that crystallized our K4 lattice." The likely
reconciliation ("we are a daughter but spawn none") is UNWRITTEN — and it is
load-bearing for the Ω_freeze source + the CMB-QNM low-ℓ observable (Observable 8).
DO NOT silently fix; adjudication owed to Grant.

**FLAG 2 — Arrow mechanism imported cross-chapter.**
[`arrow-of-time.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/arrow-of-time.md)
lives in vol3/CONDENSED-MATTER; its "spherical-spreading one-way street" + the Ŝ
scattering-irreversibility operator are used COSMOLOGICALLY (the sole Ax3-legal
arrow of this map) without either the map or the source flagging the import, and
the discrete-K4 (non-Cartesian) version is "asserted but not separately worked
out" (claim-quality:758). Verify Ŝ is defined at the cosmic impedance boundary
before leaning on it cosmologically, OR lift the arrow properly into a cosmology
leaf. Surfaced, not lifted.

---

## Provenance and scope

All source citations trace to HEAD `205d6e6b` on `analysis/stage4-a1-eos-scope`
(off brief-main); all load-bearing cites named in §2/§4/§6 were re-verified on
this branch (`analysis/de-latent-heat-banking`, off main `eaadeaf1`) before
banking. This doc CONSOLIDATES existing corpus content; it introduces no new
`clm-` and builds no new numerical physics. Do NOT build deeper on `clm-s4n33u`
(build_status "input-only") without Grant go.

