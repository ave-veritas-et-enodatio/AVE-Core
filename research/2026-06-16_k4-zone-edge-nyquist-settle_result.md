# K4/srs Zone-Edge Nyquist — RESULT (settle of the two-k_max corpus contradiction)

**Date:** 2026-06-16
**Prereg (FROZEN):** [`2026-06-16_k4-zone-edge-nyquist-settle_prereg_FROZEN.md`](2026-06-16_k4-zone-edge-nyquist-settle_prereg_FROZEN.md)
**Driver:** [`src/scripts/vol_1_foundations/k4_zone_edge_nyquist_sweep.py`](../src/scripts/vol_1_foundations/k4_zone_edge_nyquist_sweep.py)
**JSON sidecar:** [`2026-06-16_k4-zone-edge-nyquist-settle_result.json`](2026-06-16_k4-zone-edge-nyquist-settle_result.json)
**Figure:** `src/scripts/vol_1_foundations/genesis_v9_figs/k4_zone_edge_nyquist.png`
**Class (consistency-vs-emergence):** CONSISTENCY-class (internal-corpus consistency settle; ℓ_node, c imported from `constants.py`; verdict is a dimensionless lattice ratio).

---

## §1 Verdict

| net | band-top k_max (rad/ℓ_node) | k_max / π | low-k velocity factor c(k→0)/c_link | bin |
|---|---|---|---|---|
| **srs-R** (chiral, I4₁32) | **4.4429** | **1.41421 = √2** | 0.57749 | **K4-CUTS-AT-~π/ℓ_node** |
| **srs-L** (chiral, I4₃32) | 4.4429 | 1.41421 = √2 | 0.57749 | K4-CUTS-AT-~π/ℓ_node |
| diamond (cubic control) | 5.4414 | 1.73205 = √3 | 0.57735 | NEITHER (geom-image is √3π, not √2π) |

**Verdict bin (chiral srs net): `K4-CUTS-AT-~π/ℓ_node`** — fired via the prereg-§4 geometry-rescaled-image
clause (the measured axis band-top is **exactly √2·π/ℓ_node**, the geometric projection of the canonical
1-bond Brillouin edge π/ℓ_node onto the srs axis-2 ray, AND is decisively far from 0.577: d = 3.87).
Enantiomorph-invariant (srs-R ≡ srs-L to all digits). L-stable across L ∈ {6, 8, 10}.

**The `0.577/ℓ_node` value is categorically NOT a wavevector cutoff. It is a VELOCITY.** The driver
recovers 0.577 = 1/√3 EXACTLY, but as the **low-k phase-velocity factor `c(k→0)/c_link`** (the band
slope at the zone center) — not as a `k_max`. The band does not top out anywhere near 0.577 rad/ℓ_node;
it keeps rising past it and saturates ~7.7× higher.

---

## §2 What the band actually does (the mechanism that explains the contradiction)

Full-range sweep of the EXISTING `measure_dispersion` extractor (no solver rebuilt) on srs-R, L=8,
axis-2, m = 1…16 (the commensurate axis Nyquist):

```
  m    k[rad/ℓ_node]   ω[rad/step]   c(k)/c_link
  1       0.2777         0.1602        0.5770   <- low-k SLOPE = 0.577 = 1/√3  (THE "0.577")
  4       1.1107         0.6354        0.5721
  8       2.2214         1.2311        0.5542
 12       3.3322         1.7092        0.5130
 14       3.8875         1.8572        0.4777
 15       4.1652         1.8972        0.4555
 16       4.4429         1.9105        0.4300   <- band TOP (ω max, dω/dk→0)  =  √2·π/ℓ_node
```

- At **small k** the dispersion is linear with slope `c(k→0)/c_link = 0.57749 ≈ 1/√3`. **This slope IS
  the corpus "0.577".** It is the 3D-TLM network-velocity projection (`ANALYTIC_NETWORK_FACTOR`,
  `chiral_lattice_dynamics.py:48`) — a *phase velocity*, dimensionally length/time, not a wavevector.
- As **k grows** the band bends over (sub-linear, `c(k)` rolls off from 0.577 toward 0.43), exactly as a
  discrete `ω = (2c/ℓ)·sin(kℓ/2)`-type lattice band must.
- The band **tops out (ω maximal, group velocity dω/dk → 0) at k = 4.4429 rad/ℓ_node = √2·π/ℓ_node** —
  the geometric image of the canonical Brillouin edge π/ℓ_node projected onto the srs axis-2 direction
  (whose plane spacing is ℓ/√2, denser than one bond, so its axis Nyquist sits at √2·π).

So the two corpus numbers are measuring **two different things on the same band**: 0.577 is the band's
**slope at k→0** (a velocity); π/ℓ_node is the order of the band's **k-axis edge** (a wavevector). They
were never the same quantity. Presenting them as interchangeable `k_max` values is the contradiction;
the band itself resolves it unambiguously.

---

## §3 srs vs cubic geometry (caveat committed in prereg §5.1, now quantified)

The **literal measured axis band-top is geometry-dependent**, and both nets land on a clean √n·π:

- **srs axis-2:** plane spacing ℓ/√2 → band-top at **√2·π/ℓ_node ≈ 4.443**.
- **diamond axis-2:** the cubic [001] projection of the diamond bonds gives band-top at **√3·π/ℓ_node ≈ 5.441**
  with `ω_max = 2c/ℓ = π` exactly (in step units), the textbook 1D-LC `ω=(2c/ℓ)sin(kℓ/2)` edge value.

Both are O(1) geometric multiples of the **single underlying scale π/ℓ_node** = the 1-bond Brillouin
edge. The diamond fell in NEITHER only because its geometry-image is √3·π, which the frozen π-bin's
explicit √2·π image clause (srs-specific) does not cover — this is correct, honest binning, not a
mismatch: the diamond's band-top IS π/ℓ_node-scaled, just by √3 (its axis geometry) rather than √2.

**Bottom line for the bin label:** the chiral srs net's band tops out at the π/ℓ_node *family* (√2·π),
NOT at 0.577. The bin label "~π/ℓ_node" is correct in *order and origin* (a Brillouin/Nyquist wavevector
edge, geometry-projected); it should NOT be read as "exactly 3.14159" — the raw measured number is √2·π
= 4.443 for the srs axis-2 ray. The result is reported with the raw number AND the geometric relationship,
per the prereg-§4 anti-overstate instruction.

---

## §4 Consequence for `clm-sjjvhf` (the interior-Nyquist-exemption argument)

`clm-sjjvhf` (`claims.jsonl:239`, canonical at `common/boundary-observables-m-q-j.md:87`) argues that
interior eigenmodes of a bounded soliton (e.g. the electron's horn-torus interior at k ≈ 6.36/ℓ_node) are
exempt from "the K4 Nyquist limit k_max = **0.577/ℓ_node**". **This empirical settle shows the bound it
names is mislabeled by a category error**:

- **The propagating-mode bound the lattice actually exhibits is a Brillouin/Nyquist *wavevector* edge of
  order π/ℓ_node (measured √2·π = 4.44/ℓ_node along the srs axis), NOT 0.577/ℓ_node.** 0.577 is the
  low-k *velocity*, which cannot be a "Nyquist limit" on a wavevector at all.
- This **strengthens the spirit of `clm-sjjvhf`'s exemption argument** in one direction and **complicates
  its arithmetic** in another, and the net effect is Grant's call (flag-don't-fix — I do not silently
  rewrite the claim):
  - **Strengthens:** the interior mode the claim cites lives at k ≈ 6.36/ℓ_node. Against the *correct*
    propagating edge (√2·π ≈ 4.44/ℓ_node on the srs axis; ≤ √3·π ≈ 5.44 on the cubic axis), 6.36 is
    STILL above the propagating-mode band-top — so the "interior mode sits above the propagating Nyquist
    edge, hence is not a propagating lattice mode" reading survives with the corrected (larger) edge.
  - **Complicates:** the *specific number* `0.577/ℓ_node` in the claim text is wrong as a "Nyquist limit"
    — it is a velocity. The exemption argument should cite the wavevector edge (~π/ℓ_node family), not
    0.577, or the claim invites the exact 0.577-vs-π confusion this settle exists to remove.

**I am NOT editing `clm-sjjvhf` or `boundary-observables-m-q-j.md:87`.** Per flag-don't-fix and lane
discipline (the auditor lands corpus/claim edits), I surface the finding with both verbatim sites below
and let Grant adjudicate which `k_max` binds the exemption argument and whether the claim text's "0.577"
should be relabeled to the wavevector edge.

---

## §5 Verbatim conflict sites (verify-before-cite, re-grepped 2026-06-16)

- **`manuscript/ave-kb/common/boundary-observables-m-q-j.md:87`** (0.577 as a `k_max`):
  > "The K4 Nyquist limit $k_{\max} = 0.577 / \ell_{\text{node}}$ does NOT apply to interior structure
  > because the substrate never propagates that wave through the lattice…"

- **`manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md:10`** (π as the `k_max`):
  > "The maximum spatial frequency the lattice can support without aliasing is the Brillouin boundary:
  > $k_{max} = \pi / \ell_{node}$."

- **`manuscript/ave-kb/common/ave-analytical-toolkit-index.md:179`** (π as the cutoff):
  > "K4 discrete vs continuum Maxwell — discrete dispersion has Nyquist cutoff at k_max = π/ℓ_node"

- **`src/ave/core/chiral_lattice_dynamics.py:48`** (0.577 is defined as a VELOCITY factor):
  > `ANALYTIC_NETWORK_FACTOR = 1.0 / np.sqrt(3.0)` — "the long-wavelength scalar mode propagates at the
  > 3D-isotropic projection c0 = c_link / sqrt(3)".

- **`src/ave/axioms/spectral_gap.py:89,102`** (π is the analytic Brillouin edge):
  > "Maximum at Brillouin zone edge: ω_max = 2c/ℓ at k = π/ℓ"; `brillouin_zone_edge() -> π / l_node`.

The contradiction is real and now empirically resolved: **0.577 is a velocity mislabeled as a wavevector
in `boundary-observables-m-q-j.md:87`; the actual propagating-mode k-axis edge is the π/ℓ_node family.**

---

## §6 Honest scope / limitations

- **Single scalar V-sector acoustic band.** The FFT-peak extractor reads the dominant (lowest) band;
  a degree-3 net may carry optical/folded branches not resolved here. The acoustic band's top is the
  object measured, and it is L-stable and enantiomorph-invariant.
- **±1 FFT bin at the very top.** At L=10 the band-top reads m=19 (k=4.221) vs m=16→√2·π=4.443 at L=6,8 —
  a sub-bin FFT-resolution effect at the band crest where dω/dk is already ~0; ω_max is constant (1.910)
  across all L. The √2·π identification is from the L=6,8 commensurate landings (m hits the exact axis
  Nyquist); L=10's m_nyq=20 over-resolves and the peak-finder caps one bin early. Reported, not hidden.
- **Geometry, not universality, sets the raw number.** √2·π (srs axis-2) and √3·π (diamond axis-2) are
  axis-projection-specific; a different crystallographic ray would give a different √n·π. The
  *universal* statement is: the band-top is a Brillouin/Nyquist wavevector edge of the π/ℓ_node family,
  never the 0.577 velocity. That is the load-bearing finding for the adjudication.

---

## §7 Disposition

- **Settled empirically:** the chiral K4/srs lattice's propagating scalar band tops out at a
  Brillouin/Nyquist **wavevector** edge of order **π/ℓ_node** (measured √2·π/ℓ_node on the srs axis),
  L-stable and enantiomorph-invariant. **It does NOT top out at 0.577/ℓ_node**; 0.577 is the recovered
  **low-k velocity factor** 1/√3, a category-distinct quantity.
- **Verdict bin:** `K4-CUTS-AT-~π/ℓ_node` (geometry-rescaled image clause; raw √2·π reported transparently).
- **No corpus edits in this document.** The `clm-sjjvhf` / `boundary-observables-m-q-j.md:87` "0.577 as
  k_max" mislabel is **flagged for Grant's adjudication** (which k_max binds the interior-exemption
  argument; whether to relabel the claim's 0.577 to the wavevector edge) and **for the auditor to land**
  if Grant rules a relabel — not fixed here (lane discipline).
