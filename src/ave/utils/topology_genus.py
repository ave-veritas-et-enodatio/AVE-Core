"""D16 — THREAD-THE-BUBBLE topology gate (REAL connectivity code on snap_mask).

This is a pure DIAGNOSTIC (CP9 / CP1: it changes no dynamics). It bins the
genesis snap shell's topology from the connectivity of ``snap_mask`` alone, via
``scipy.ndimage.label`` — the directive's "real topology code, not an assertion".

THE GATE (prereg §3.3 / §4 F-GENUS), three ORDERED bins:

  SHELL-NEVER-FORMS  the largest connected snap component is below F-SHELL (or the
                     snap fragmented into a cloud of disconnected specks rather
                     than condensing into one coherent shell) — there is nothing
                     to thread. The FLOOR case (evaluated first).
  NO-PENETRATION     a coherent snap shell forms (genus-0) but NO un-snapped
                     channel threads through it along the spin axis — the
                     Meissner/type-II expulsion did not carve a normal channel
                     (the topology hypothesis falsified AT this swept config;
                     honest only after the drive-M / shell-thickness sweep).
  THREADED           a connected un-snapped channel spans the shell axially
                     within the shell's transverse bounding cylinder AND is
                     encircled by shell cells at the mid-plane (ball -> torus,
                     genus-1 — the type-II expectation realized).

THE DISCRIMINATOR (torus vs hollow-sphere — the load-bearing topology):
  Both a hollow sphere-shell and a torus have an annular mid-plane cross-section,
  so the ring test ALONE cannot separate them. The genus is decided by whether
  the central un-snapped region CONNECTS THROUGH the shell along the axis:
    * hollow sphere -> the central cavity is SEALED by the polar caps; the
      un-snapped exterior below the shell does NOT reach the exterior above it
      within the shell's bounding cylinder  -> NO-PENETRATION (b1 = 0).
    * torus         -> the central hole is OPEN through the axis; exterior-below
      and exterior-above are the SAME un-snapped component within the cylinder
      -> THREADED (b1 = 1, one tunnel/handle).
  This through-connection test is pure connected-component code (scipy), and is
  validated on hand-built sphere-shell / torus-shell masks by the K-TOPOLOGY
  keeper (``test_unified_threaded_v8.py``).

A connected-component CAVITY count (b2 — enclosed un-snapped voids) is reported
alongside for corroboration; the BIN is decided by the through-channel test.
"""

from __future__ import annotations

import numpy as np
from scipy import ndimage

__all__ = [
    "STRUCT6",
    "measure_topology",
    "derive_read_torus_from_channel",
    "make_sphere_shell_mask",
    "make_torus_shell_mask",
]

# 6-connectivity (face neighbours) — the physical adjacency for a sealed snapped
# wall (a diagonal-only touch is NOT a watertight wall for the medium it bounds).
STRUCT6 = ndimage.generate_binary_structure(3, 1)


def _largest_component(mask, struct=STRUCT6):
    """(largest_component_mask, its_cell_count, n_total_components)."""
    lab, n = ndimage.label(mask, structure=struct)
    if n == 0:
        return np.zeros_like(mask, dtype=bool), 0, 0
    sizes = ndimage.sum(np.ones_like(lab, dtype=np.int64), lab, index=range(1, n + 1))
    big = int(np.argmax(sizes)) + 1
    return (lab == big), int(sizes[big - 1]), int(n)


def _encircled_2d(channel_plane, shell_plane, ca, cb):
    """4-ray encirclement test in a 2D axial slice: cast rays from the channel
    cell nearest (ca, cb) along +A/-A/+B/-B; encircled iff every ray strikes a
    shell cell before leaving the slice. A genuine through-hole is walled on all
    sides in the mid-plane; an open notch is not."""
    pts = np.argwhere(channel_plane)
    if pts.size == 0:
        return False
    d2 = (pts[:, 0] - ca) ** 2 + (pts[:, 1] - cb) ** 2
    pa, pb = pts[int(np.argmin(d2))]
    na, nb = channel_plane.shape
    for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        a, b = pa + da, pb + db
        hit = False
        while 0 <= a < na and 0 <= b < nb:
            if shell_plane[a, b]:
                hit = True
                break
            a += da
            b += db
        if not hit:
            return False
    return True


def _count_cavities(shell, struct=STRUCT6):
    """b2 — enclosed un-snapped voids (background components not touching the
    padded array boundary). Pure connectivity."""
    pad = np.pad(shell, 1, mode="constant", constant_values=False)
    bg = ~pad
    lab, n = ndimage.label(bg, structure=struct)
    if n == 0:
        return 0
    # the exterior = whatever label sits on the padded corner (always background)
    ext = lab[0, 0, 0]
    enclosed = set(int(v) for v in np.unique(lab) if v != 0 and v != ext)
    return len(enclosed)


def measure_topology(snap_mask, interior_mask, *, axis=2, f_shell=200,
                     dominance_frac=0.30, encircle_required=True):
    """Bin the snap shell's topology from ``snap_mask`` connectivity.

    Parameters
    ----------
    snap_mask, interior_mask : (N,N,N) bool arrays
    axis : the spin / threading axis (0,1,2)
    f_shell : minimum cell count for the largest connected snap component to
        count as a SHELL (re-measured at config; the F-SHELL floor §4)
    dominance_frac : the largest component must also hold at least this fraction
        of all snapped cells to be a COHERENT shell (vs one speck in a fragmented
        cavitation cloud) — guards the v8-observed scattered-cavitation regime
    encircle_required : require the mid-plane 4-ray encirclement for THREADED

    Returns a dict with ``bin`` in {SHELL-NEVER-FORMS, NO-PENETRATION, THREADED},
    the shell/fragmentation diagnostics, the cavity count b2, and (when THREADED)
    the channel cell mask under ``_channel_mask`` (for D17(b) channel-cells-live).
    """
    interior_mask = np.asarray(interior_mask, dtype=bool)
    raw_snap = np.asarray(snap_mask, dtype=bool)
    sm = raw_snap & interior_mask
    N = sm.shape[axis]
    total_snap = int(sm.sum())
    out = {
        "axis": int(axis),
        "f_shell": int(f_shell),
        "dominance_frac": float(dominance_frac),
        "total_snap": total_snap,
    }

    shell, shell_cells, n_comp = _largest_component(sm)
    dominance = shell_cells / max(total_snap, 1)
    out["shell_cells"] = shell_cells
    out["n_snap_components"] = n_comp
    out["largest_frac_of_snap"] = float(dominance)

    if shell_cells < f_shell or dominance < dominance_frac:
        out["bin"] = "SHELL-NEVER-FORMS"
        out["reason"] = (
            f"no coherent shell: largest connected snap component = {shell_cells} cells "
            f"(F-SHELL {f_shell}); it holds {dominance:.1%} of {total_snap} snapped cells "
            f"across {n_comp} disconnected components (dominance floor {dominance_frac:.0%})"
        )
        return out

    out["b2_cavities"] = _count_cavities(shell)

    # axial extent + transverse centroid of the shell
    idx = np.argwhere(shell)
    ax = idx[:, axis]
    z0, z1 = int(ax.min()), int(ax.max())
    others = [a for a in range(3) if a != axis]
    ca = float(idx[:, others[0]].mean())
    cb = float(idx[:, others[1]].mean())
    da = idx[:, others[0]] - ca
    db = idx[:, others[1]] - cb
    rmax = float(np.sqrt(da ** 2 + db ** 2).max()) + 1.0
    out["axial_extent"] = [z0, z1]
    out["transverse_centroid"] = [ca, cb]
    out["transverse_rmax"] = rmax

    # the shell's transverse bounding cylinder (all z) — the channel must thread
    # WITHIN this footprint (a path going around the OUTSIDE is not a thread)
    coords = np.indices(sm.shape)
    rr = np.sqrt((coords[others[0]] - ca) ** 2 + (coords[others[1]] - cb) ** 2)
    column = rr <= rmax

    bg_col = (~raw_snap) & column
    lab_bg, _ = ndimage.label(bg_col, structure=STRUCT6)

    def _labels_on_plane(z):
        if z < 0 or z >= N:
            return set()
        sl = [slice(None)] * 3
        sl[axis] = z
        plane = lab_bg[tuple(sl)]
        return set(int(v) for v in np.unique(plane) if v != 0)

    below = _labels_on_plane(z0 - 1)
    above = _labels_on_plane(z1 + 1)
    through = sorted(below & above)
    out["through_labels"] = through

    zc = (z0 + z1) // 2
    sl = [slice(None)] * 3
    sl[axis] = zc
    shell_plane = shell[tuple(sl)]

    channel = np.zeros_like(sm)
    threaded = False
    for cid in through:
        comp = lab_bg == cid
        comp_plane = comp[tuple(sl)]
        enc = _encircled_2d(comp_plane, shell_plane, ca, cb)
        if enc or not encircle_required:
            threaded = True
            channel |= comp
    out["encircled"] = bool(threaded and through)

    if threaded:
        out["bin"] = "THREADED"
        out["channel_cells"] = int(channel.sum())
        out["_channel_mask"] = channel
        out["reason"] = (
            "connected un-snapped channel spans the shell axially within its bounding "
            f"cylinder (through-labels {through}) and is encircled by shell at the mid-plane "
            f"(b2 cavities={out['b2_cavities']}, b1>=1 tunnel)"
        )
    else:
        out["bin"] = "NO-PENETRATION"
        out["reason"] = (
            f"coherent shell forms ({shell_cells} cells, {dominance:.0%} dominance, "
            f"b2 cavities={out['b2_cavities']}) but no un-snapped channel threads it along "
            "the axis (exterior-below and exterior-above are not the same un-snapped "
            "component within the bounding cylinder; b1=0)"
        )
    return out


def derive_read_torus_from_channel(topo, axis=2, min_r=3.0):
    """The A46 fix — derive the FIELD-DERIVED read torus (R, r) from the D16
    channel locus instead of choosing pol_R by convention.

    The read torus must wrap the SHELL WALL around the threaded hole, NOT the
    outer rim of the bounding cylinder. We take the shell's own (not the
    channel's) mid-plane radial profile from the channel axis and locate the
    wall RING — the inner edge is where the hole ends and the wall begins; the
    outer edge is where the wall ends. R = the ring midpoint; r = max(half the
    ring width, ``min_r``) so the minor circle clears the F0b r >= 3 floor.

    (The earlier ``chan_plane_r.max()`` read the thin un-snapped annulus OUTSIDE
    the tube within the bounding cylinder and returned the cylinder rim, not the
    wall — flagged + fixed; validated on the synthetic torus by K-TOPOLOGY.)

    Requires a THREADED topo (a channel exists); returns None for other bins.
    """
    if topo.get("bin") != "THREADED" or "_channel_mask" not in topo:
        return None
    ca, cb = topo["transverse_centroid"]
    shell_extent = topo.get("axial_extent")
    chan = topo["_channel_mask"]
    others = [a for a in range(3) if a != axis]
    zc = (shell_extent[0] + shell_extent[1]) // 2
    sl = [slice(None)] * 3
    sl[axis] = zc
    coords = np.indices(chan.shape)
    rr = np.sqrt((coords[others[0]] - ca) ** 2 + (coords[others[1]] - cb) ** 2)
    rr_plane = rr[tuple(sl)]
    chan_plane = chan[tuple(sl)]

    # the SHELL wall at the mid-plane = snapped channel-complement cells inside
    # the bounding cylinder (the largest-component shell), radial profile.
    shell_plane = (~chan_plane) & (rr_plane <= topo["transverse_rmax"])
    shell_r = rr_plane[shell_plane]
    if shell_r.size == 0:
        return None
    # the inner hole radius = where channel cells stop being radially connected
    # to the axis (first shell cell going outward); use the median shell ring.
    r_hole = float(np.percentile(shell_r, 5.0))   # inner wall edge
    r_wall_out = float(np.percentile(shell_r, 95.0))  # outer wall edge
    R = 0.5 * (r_hole + r_wall_out)
    r = max(0.5 * (r_wall_out - r_hole), min_r)
    return {"R": float(R), "r": float(r), "r_hole": float(r_hole),
            "r_wall_out": float(r_wall_out),
            "center": [float(ca), float(cb), float(zc)]}


# ---------------------------------------------------------------------------
# synthetic known-topology masks for the K-TOPOLOGY keeper (a known-genus-0
# sphere shell must read NO-PENETRATION; a known-genus-1 torus must read THREADED)
# ---------------------------------------------------------------------------
def make_sphere_shell_mask(N, r_in=8.0, r_out=12.0, axis=2):
    """A watertight genus-0 spherical snap shell centred in an N^3 grid."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    r2 = (i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2
    return (r2 >= r_in ** 2) & (r2 <= r_out ** 2)


def make_torus_shell_mask(N, R=12.0, a=4.0, axis=2):
    """A genus-1 solid torus (its symmetry axis = ``axis``); the central hole is
    un-snapped and threads through along the axis."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    coords = [i - c, j - c, k - c]
    az = coords[axis]
    others = [x for x in range(3) if x != axis]
    rho = np.sqrt(coords[others[0]] ** 2 + coords[others[1]] ** 2)
    return (rho - R) ** 2 + az ** 2 <= a ** 2
