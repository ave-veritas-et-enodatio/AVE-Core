# PREREG — Mass-Sector Field-Momentum T^{0i}: the §390 R3 false-null hatch

**Date (frozen):** 2026-06-23
**Status:** FROZEN + RUN (Rule-10). Runs the R3 false-null escape hatch from
[`2026-06-23_mass-sector-two-body-scattering_result.md`](2026-06-23_mass-sector-two-body-scattering_result.md) §1.7.
**Branch:** `analysis/soliton-mass-scattering` (worktree `/tmp/lane-scattering`, off `origin/main`). `main` PROTECTED, NO self-merge; PR for orchestrator audit + Grant merge.
**Lane:** Implementer LANE A (mass-sector follow-on, §390 R3 hatch).
**Engine (read-only, UNCHANGED):** `MasterEquationFDTD` (`src/ave/core/master_equation_fdtd.py`). The §390 driver established the §0.5 centroid-drift readout is SNR<1 (observable-limited, not substrate-closed). This is the transport-independent observable that bypasses centroid transport.

---

## §0 — Grant ruling (run-or-defer, 2026-06-23)

The §390 result doc R3 recorded the T^{0i} field-momentum integral as an OPEN,
GRANT-GATED false-null hatch — computable with ZERO engine change, NOT run.
**Grant's ruling (2026-06-23): RUN it.** Plus the load-bearing physics call:

> **Gravity = FREQUENCY MODULATION (diffraction), NOT a momentum-transport pull.**

This is the corpus ontology made measurable — `optical-refraction-gravity.md:17`:
*"it does not 'fall' due to a mechanical pulling stress tensor; it **diffracts**.
The wave packet bends toward the region of higher spacetime impedance... Gravity
is physically identical to the optical refraction of light propagating through a
non-linear dielectric medium."* The T^{0i} integral is exactly a measurement of
whether that **mechanical pulling stress tensor** (the momentum-transport
component T^{0x}) carries net momentum between two masses.

---

## §1 — Substrate-native-check walk (recorded BEFORE the new observable code)

| Checkpoint | Resolution |
|---|---|
| CP1 dynamics | Wave propagation (leapfrog FDTD). T^{0i} is a diagnostic READ from the evolved field — no engine change, no minimization. |
| CP2 sector | V-sector / A1 dilatation-mass (scalar). T^{0i}=(∂_t V)(∂_i V) is the canonical scalar-field momentum density — the field's OWN momentum, NOT an SM import. |
| CP3 objective | AVE-native: integrate the field's momentum density over each blob's half-volume + read the flux across the gap face. NOT energy-functional minimization. |
| CP4 coords | Real-space lattice-Cartesian, load-bearing (A1 mass = real-space dilatation blob; same as §390 CP4 — no A46 violation, NOT a (2,3) phase-space claim). |
| CP5 local clock | c_eff(A²) modulation IS the FM/diffraction mechanism under test. |
| CP7 sampling | PML cells EXCLUDED from every integral (the damping mask multiplies V in the PML -> T^{0i} there is a frozen-absorbing artifact). `PML ≤ {i,j,k} ≤ N−PML−1`. |
| CP10 boundary | Saturation handled by the engine's internal A_cap/S_min clip; this driver adds NO bulk term. |

**Two substrate-native corrections surfaced at driver-time (Rule 10, flag-don't-fix), see §3:**
- **TRUE-CENTER (half-integer) placement.** An N=24 grid has no single center cell; the true center is the FACE between cells 11 and 12, XC=(N−1)/2=11.5. Integer N//2=12 centering gives a stationary isolated blob a SPURIOUS net field-momentum (P_total=+21.6); at XC=11.5 it is EXACTLY 0. The whole test is centered on XC.
- **EVEN separations.** The §390 odd-d0 placement (`+ (d0%2)`) is fine for a centroid-difference readout but puts the pair off-center for a midplane-flux readout. Even d0 ∈ {6,8,10} straddles XC symmetrically.

---

## §2 — Frozen configuration (validated v14 breather, matches §390 driver)

Reuses the §390 validated v14 breather (the F1 seed-swap; `test_master_equation_v14_mode_i.py` 5/5 PASS):

| Parameter | Value | Source |
|---|---|---|
| `N` | 24 | validated v14 breather |
| `DX` | 0.5 | validated v14 |
| `V_YIELD` | 1.0 | v14 natural units |
| `SEED_AMPLITUDE` | 0.85·V_yield | validated v14 |
| `SEED_RADIUS` | 2.5 | validated v14 |
| `XC` (true center) | (N−1)/2 = 11.5 | half-integer-centering fix (§3) |
| separations `d0` | **{6, 8, 10}** (even, symmetric about XC) | midplane-flux symmetry (§3) |
| relative phase | {in (+,+), out (+,−)} — BOTH, b=0 | the load-bearing guard |
| window | transient 200 + record 400 (N_RUN=600) | v14 canonical |

---

## §3 — Observable (T^{0i} field momentum; ave-driver-script-honesty)

Substrate-native scalar field-momentum density, read from the engine's own state:

```
T^{0x}(cell) = (∂_t V)(∂_x V)
∂_t V = (V − V_prev)/dt              # the two stored leapfrog states; zero
                                      # initial velocity set by V_prev = V at seed
∂_x V = (V[i+1] − V[i−1])/(2 dx)      # central diff, matching the engine's own
                                      # _laplacian central-difference stencil
```

- **M0 — P_total interior** = Σ T^{0x} over PML-excluded interior. Momentum-conservation cross-check (≈0 for a symmetric b=0 pair; **the observable's sanity gate**).
- **M1 — dP = P_left − P_right** = net x-momentum DELIVERED to each half-volume blob (split at the 11/12 face). A real PULL delivers +x to the left blob, −x to the right -> dP>0, sustained (DC).
- **M2 — Φ_x = midplane flux** = T^{0x} integrated on the 11/12 gap face (mean of i=11, i=12 planes). The momentum TRANSPORTED across the gap.
- **M3 — single-blob control** = the radiation/breathing T^{0i} floor (M1/M2 must exceed it to count as a real two-body effect).

**AC/DC discriminator (M1).** dP std/|mean|: a sustained DC pull has ac/dc < 1 (mean dominates); AC-dominated breathing/interference has ac/dc > 1 (the imbalance sloshes and time-averages toward nothing).

---

## §4 — Pre-registered prediction (Grant's call, BEFORE adjudication)

**P0 (Grant's framing):** net momentum flux between the blobs ≈ ZERO → gravity is FREQUENCY MODULATION / diffraction (the c_eff gradient modulates phase, transports no net momentum) → #390's null is REAL for the right reason (momentum-flux-absent), not apparatus-limited.

**P-refute (refute-by-default):** if T^{0i} shows a NET non-zero phase-INDEPENDENT, DC-sustained momentum delivery to the blobs above the breathing floor → that is a real compression-sector momentum-transport force, and it OVERTURNS the diffraction picture. Report honestly; do not round either way.

**Discriminator (same logic as the §390 phase guard, now on momentum).** A true gravity pull is driven by A²(r)=|V|²/V_yield² (sign-blind) → it must be PHASE-INDEPENDENT and DC-sustained. Generic-soliton coherent overlap is sign-DEPENDENT and AC-dominated. The in-vs-out comparison + the AC/DC ratio ARE the discriminator.

---

## §5 — Outcome bins (frozen, symmetry-aware)

| Bin | M2 (transported flux) | M1 (delivered dP) | Verdict |
|---|---|---|---|
| **PASS / FM-DIFFRACTION** | Φ_x≈0 (symmetry-forced) | phase-DEPENDENT and/or AC-dominated | NO phase-independent momentum-transport force; only breathing interference. Gravity = c_eff(A²) FM of the carrier phase, NOT a stress-tensor pull. #390 null REAL for the right reason. **(P0 confirmed)** |
| **SURPRISE / REAL-PULL** | — | phase-INDEPENDENT (in≈out) AND DC-sustained (ac/dc<1) AND above floor | A real compression-sector momentum-transport force; OVERTURNS the diffraction picture. FLAG-DON'T-FIX, surface to Grant. **(P-refute)** |

**Symmetry caveat (flagged, load-bearing).** For a head-on b=0 SYMMETRIC pair, V is exactly even (in) / odd (out) about the gap face, so T^{0x} is exactly ODD about the face → Φ_x=0 by reflection symmetry. **The M2 zero is therefore SYMMETRY-FORCED, not by itself a physics discriminator** (it would be zero for ANY symmetric configuration). The load-bearing discriminator is M1 (delivered-momentum dP: phase-dependence + AC/DC), NOT M2 alone. The verdict rests on M1.

---

## §6 — CONSISTENCY-vs-EMERGENCE label (consistency-vs-emergence skill)

**Class C consistency check (NOT a chord, NOT emergence).** AVE-gravity is FORM-derived / VALUE-imported (MIXED, `optical-refraction-gravity.md:52`, G-ruling `ilk-gravmb`). A confirmed FM/diffraction (momentum-pull-absent) reproduces the corpus ontology via the engine's own c_eff(V) dynamics — a consistency check on the gravity ontology, not independent AVE-distinct evidence. No CODATA target; natural units; SIGN/PHASE/AC-DC test, no magnitude pin. The observable is engine-natural (T^{0i} from V, V_prev) with no CODATA input.

---

## §7 — Honest-negative / honest-positive discipline (Rule 11) pre-commitment

If the result is SURPRISE / REAL-PULL (phase-independent DC pull), that OVERTURNS Grant's diffraction call — report it as a real compression-sector force, surface to Grant, do NOT round it down to PASS to protect the FM framing. If the result is PASS / FM-DIFFRACTION, do NOT inflate it to "gravity confirmed" — it is a consistency check that the momentum-transport pull is absent, on a scalar-A1 engine, for a symmetric head-on pair. The bins are frozen; they will NOT be dropped post-hoc.
