"""
Electron genesis animation — real-space (the drop) + phase-space (the (2,3) winding)
SIDE BY SIDE, channels overlaid, dark aesthetic.

Reads an r11_genesis_*_capture.npz (written by r11_electron_genesis_drop.save_capture)
and renders the birth narrated in every coordinate at once:

  LEFT  (real-space)  : A^2 mid-plane slice — the photon(s) propagating, colliding,
                        the antinode driving A->1 (the saturation skin, |Gamma|=1),
                        pinching off into localized breathing droplet(s).
  RIGHT (phase-space) : the (V_inc, V_ref) phasor trajectory at each drop's core bond
                        (theory.md:16: the (2,3) lives HERE, not in real space) — the
                        winding(s) closing; the two drops colored by chirality sign
                        (the e- = (2,3) vs e+ = mirror-(2,3) split).
  BOTTOM (channels)   : max A^2 / A^2_yield (pinch-off then settle), interior energy
                        (the splash radiating), per-drop |V_inc|/V_yield (-> sub-yield),
                        with a moving time cursor + the drive-off marker.

Usage:
  python r11_electron_genesis_animation.py <capture.npz> [out.mp4] [title]
"""

import sys
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import animation  # noqa: E402

CYAN = "#19d3f3"  # drop 0 (lo-x)  — e- = (2,3)
MAGENTA = "#ff4fd8"  # drop 1 (hi-x)  — e+ = mirror-(2,3)
AMBER = "#ffb000"
GREY = "#7a8290"


def load(npz_path):
    d = np.load(npz_path, allow_pickle=False)
    return {k: d[k] for k in d.files}


def _dom_port(vinc_slot):
    """Dominant port over the settled second half of the trace."""
    half = vinc_slot.shape[0] // 2
    return int(np.argmax(np.mean(np.abs(vinc_slot[half:]), axis=0)))


def build(cap, out_path, title):
    slices = cap["slices"]  # (F, N, N) mid-plane A^2
    slice_t = cap["slice_t"]  # (F,)
    t = cap["t"]  # (T,) per-step time
    maxA2 = cap["maxA2"]
    energy = cap["energy"]
    vinc, vref = cap["vinc"], cap["vref"]  # (2, T, 4)
    A_YIELD = float(cap["A_YIELD"])
    A2_YIELD = float(cap["A2_YIELD"])
    n_drive = int(cap["n_drive"])
    dt = float(cap["dt"])
    n_drops = 2 if np.any(np.abs(vinc[1]) > 1e-12) else 1
    drive_off_t = n_drive * dt

    # per-drop dominant ports + the |V_inc|/V_yield channel
    ports = [_dom_port(vinc[s]) for s in range(2)]
    vy = [np.sqrt(np.sum(vinc[s] ** 2, axis=1)) / A_YIELD for s in range(2)]  # |V_inc|/V_yield
    colors = [CYAN, MAGENTA]

    # map each slice frame -> nearest per-step index
    step_of_frame = [int(np.argmin(np.abs(t - st))) for st in slice_t]
    F = len(slices)

    plt.rcParams.update({"font.size": 8.5, "axes.edgecolor": GREY, "text.color": "#d8dde6"})
    fig = plt.figure(figsize=(11.5, 6.4), facecolor="#0a0d12")
    gs = fig.add_gridspec(
        2, 2, height_ratios=[2.35, 1.0], hspace=0.30, wspace=0.22, left=0.06, right=0.975, top=0.90, bottom=0.10
    )
    ax_real = fig.add_subplot(gs[0, 0])
    ax_phase = fig.add_subplot(gs[0, 1])
    ax_chan = fig.add_subplot(gs[1, :])
    for ax in (ax_real, ax_phase, ax_chan):
        ax.set_facecolor("#0a0d12")
        ax.tick_params(colors=GREY, labelsize=7)
    fig.suptitle(title, color="#eaf2ff", fontsize=12, y=0.975)

    # color scale: sqrt(A^2)=A so the sub-yield core and the A->1 skin both show
    vmax = float(np.sqrt(max(slices.max(), A2_YIELD * 4)))
    im = ax_real.imshow(
        np.sqrt(slices[0]).T,
        origin="lower",
        cmap="inferno",
        vmin=0.0,
        vmax=vmax,
        interpolation="bilinear",
        aspect="equal",
    )
    # the |Gamma|=1 saturation skin contour (red, A=1) + the V_yield contour (green);
    # drawn per-frame by _draw_skin in update() (mpl-3.10-safe). skin starts empty.
    skin = None
    ax_real.set_title(
        "real-space  |  A = |V_inc|/V_SNAP   (green=V_yield, red=|Γ|=1 skin)", color="#9fb3c8", fontsize=8
    )
    ax_real.set_xlabel("x (lattice)", color=GREY)
    ax_real.set_ylabel("y (lattice)", color=GREY)

    # phase-space: accumulating (V_inc, V_ref) trajectories per drop
    ax_phase.axhline(0, color=GREY, lw=0.5)
    ax_phase.axvline(0, color=GREY, lw=0.5)
    vmx = max(1e-6, float(np.max([np.abs(vinc[s, :, ports[s]]).max() for s in range(n_drops)])))
    vmxr = max(1e-6, float(np.max([np.abs(vref[s, :, ports[s]]).max() for s in range(n_drops)])))
    lim = 1.15 * max(vmx, vmxr)
    ax_phase.set_xlim(-lim, lim)
    ax_phase.set_ylim(-lim, lim)
    ax_phase.set_aspect("equal")
    ax_phase.set_title("phase-space  |  (V_inc, V_ref) phasor — the (2,3) winding", color="#9fb3c8", fontsize=8)
    ax_phase.set_xlabel("V_inc", color=GREY)
    ax_phase.set_ylabel("V_ref", color=GREY)
    lines_ph, heads = [], []
    labels = ["drop e⁻ (2,3)", "drop e⁺ mirror"]
    for s in range(n_drops):
        (ln,) = ax_phase.plot([], [], color=colors[s], lw=0.9, alpha=0.85, label=labels[s] if n_drops == 2 else "drop")
        (hd,) = ax_phase.plot([], [], "o", color=colors[s], ms=5)
        lines_ph.append(ln)
        heads.append(hd)
    ax_phase.legend(loc="upper right", fontsize=6.5, facecolor="#11161d", edgecolor=GREY)

    # channels
    ax_chan.plot(t, maxA2 / A2_YIELD, color=AMBER, lw=1.1, label="max A² / A²_yield")
    ax_chan.axhline(1.0, color="#39ff14", lw=0.6, ls=":", label="V_yield")
    ax_chan.axhline(1.0 / A2_YIELD, color="#ff2d2d", lw=0.6, ls=":", label="|Γ|=1 (A²=1)")
    e0 = max(energy.max(), 1e-9)
    ax_chan.plot(t, energy / e0, color=GREY, lw=0.9, label="interior energy (norm)")
    for s in range(n_drops):
        ax_chan.plot(t, vy[s], color=colors[s], lw=0.8, alpha=0.8, label=f"|V_inc|/V_yield drop{s}")
    ax_chan.axvline(drive_off_t, color="#eaf2ff", lw=0.8, ls="--", alpha=0.6)
    ax_chan.text(
        drive_off_t,
        ax_chan.get_ylim()[1] * 0.86,
        " source OFF →\n free-evolve",
        color="#eaf2ff",
        fontsize=6.5,
        alpha=0.8,
    )
    ax_chan.set_yscale("log")
    ax_chan.set_ylim(max(1e-3, (maxA2 / A2_YIELD).min() * 0.5), (maxA2 / A2_YIELD).max() * 2)
    ax_chan.set_xlim(t[0], t[-1])
    ax_chan.set_xlabel("time (natural units; 2π = one ω_C period)", color=GREY)
    ax_chan.legend(loc="upper right", ncol=3, fontsize=6, facecolor="#11161d", edgecolor=GREY)
    cursor = ax_chan.axvline(t[0], color="#eaf2ff", lw=1.2)

    txt = ax_real.text(
        0.02, 0.97, "", transform=ax_real.transAxes, va="top", color="#eaf2ff", fontsize=8, family="monospace"
    )

    def _draw_skin(field2d):
        # mpl 3.10: ContourSet is an Artist (no .collections); levels outside the
        # data range raise -> guard. Returns the ContourSet or None.
        levels = [lv for lv in (A_YIELD, 1.0) if field2d.min() < lv < field2d.max()]
        if not levels:
            return None
        cols = ["#39ff14" if abs(lv - A_YIELD) < 1e-9 else "#ff2d2d" for lv in levels]
        return ax_real.contour(field2d, levels=levels, colors=cols, linewidths=0.9)

    def update(f):
        nonlocal skin
        sl = np.sqrt(slices[f]).T
        im.set_data(sl)
        if skin is not None:
            try:
                skin.remove()
            except Exception:  # noqa: BLE001
                pass
        skin = _draw_skin(sl)
        si = step_of_frame[f]
        for s in range(n_drops):
            xi = vinc[s, : si + 1, ports[s]]
            yi = vref[s, : si + 1, ports[s]]
            lines_ph[s].set_data(xi, yi)
            if len(xi):
                heads[s].set_data([xi[-1]], [yi[-1]])
        cursor.set_xdata([t[si], t[si]])
        phase = "DRIVE (γγ collide → A→1 pinch-off)" if si < n_drive else "FREE-EVOLVE (does the drop remain?)"
        txt.set_text(f"t={t[si]:6.1f}  ({phase})\nmax A²={maxA2[si]:.3g}")
        return [im, cursor, txt, *lines_ph, *heads]

    anim = animation.FuncAnimation(fig, update, frames=F, interval=90, blit=False)
    out_path = Path(out_path)
    fps = 11
    try:
        anim.save(
            str(out_path),
            writer=animation.FFMpegWriter(fps=fps, bitrate=2400),
            dpi=120,
            savefig_kwargs={"facecolor": "#0a0d12"},
        )
        print(f"  saved {out_path}")
    except Exception as exc:  # noqa: BLE001
        print(f"  ffmpeg failed ({exc}); writing gif")
        gif = out_path.with_suffix(".gif")
        anim.save(str(gif), writer=animation.PillowWriter(fps=fps), dpi=100, savefig_kwargs={"facecolor": "#0a0d12"})
        print(f"  saved {gif}")
    plt.close(fig)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    npz = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else npz.with_suffix(".mp4")
    title = sys.argv[3] if len(sys.argv) > 3 else f"Electron genesis — {npz.stem}"
    cap = load(npz)
    build(cap, out, title)


if __name__ == "__main__":
    main()
