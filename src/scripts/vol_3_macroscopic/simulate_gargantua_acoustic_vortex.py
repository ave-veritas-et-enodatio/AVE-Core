#!/usr/bin/env python3
r"""
AVE: Gargantua Acoustic Vortex Simulation (v2)
===============================================

High-fidelity rendering of a near-extremal Kerr black hole (~10^8 M_sun,
a* = 0.999) using the AVE optical-acoustic framework:

    Spacetime Curvature  ≡  Refractive Index Gradient n(r)
    Frame Dragging       ≡  Circulating Fluid Vortex v_φ(r)
    Event Horizon        ≡  Dielectric Rupture (n→∞, Γ→+1)

v2 improvements:
    - Adaptive step size: large dt far from BH, fine dt near horizon
    - ACES filmic tone mapping (cinema-grade color)
    - Multi-octave hash noise disk texture (no moiré banding)
    - Wider temperature range for visible blue/red Doppler asymmetry
    - Enhanced photon ring + dual bloom
    - Denser star field with magnitude distribution
    - 4 samples/pixel for clean anti-aliasing

DAG Compliance:
    Upstream: ave.core.constants, ave.gravity
    Outputs: 2000×1000 cinematic render (250 dpi)

Vol 3 Ch. 2 — Optical-Mechanical Acoustic Vortex (Kerr Metric)
"""

import os
import sys
import time

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))


# ─────────────────────────────────────────────────────────────
# Blackbody → sRGB conversion (Planck spectrum)
# ─────────────────────────────────────────────────────────────
def _blackbody_rgb(T):
    """Convert temperature (K) to approximate sRGB [0,1].
    Tanner Helland approximation (1000 K – 40,000 K)."""
    T = np.atleast_1d(np.asarray(T, dtype=float))
    T_100 = np.clip(T / 100.0, 10.0, 400.0)

    rgb = np.zeros((len(T_100), 3))

    mask_lo = T_100 <= 66.0
    rgb[mask_lo, 0] = 1.0
    hi = ~mask_lo
    if np.any(hi):
        tmp = 329.698727446 * (T_100[hi] - 60.0) ** (-0.1332047592)
        rgb[hi, 0] = np.clip(tmp / 255.0, 0.0, 1.0)

    if np.any(mask_lo):
        tmp = 99.4708025861 * np.log(T_100[mask_lo]) - 161.1195681661
        rgb[mask_lo, 1] = np.clip(tmp / 255.0, 0.0, 1.0)
    if np.any(hi):
        tmp = 288.1221695283 * (T_100[hi] - 60.0) ** (-0.0755148492)
        rgb[hi, 1] = np.clip(tmp / 255.0, 0.0, 1.0)

    hot = T_100 >= 66.0
    rgb[hot, 2] = 1.0
    mid = (~hot) & (T_100 > 19.0)
    if np.any(mid):
        tmp = 138.5177312231 * np.log(T_100[mid] - 10.0) - 305.0447927307
        rgb[mid, 2] = np.clip(tmp / 255.0, 0.0, 1.0)
    rgb[(~hot) & (~mid), 2] = 0.0

    return rgb


def _aces_tonemap(color):
    """ACES filmic tone mapping for cinema-grade HDR → LDR."""
    a, b, c, d, e = 2.51, 0.03, 2.43, 0.59, 0.14
    return np.clip((color * (a * color + b)) / (color * (c * color + d) + e), 0.0, 1.0)


def _hash_noise(x, y, seed=0.0):
    """Deterministic 2D hash noise for disk texture."""
    val = np.sin(x * 127.1 + y * 311.7 + seed) * 43758.5453
    return val - np.floor(val)


def render_gargantua():
    t_start = time.time()
    print("=" * 70)
    print("  GARGANTUA ACOUSTIC VORTEX — AVE RAYMARCHER v2")
    print("  Adaptive-step Hamiltonian optics through refractive fluid")
    print("=" * 70)

    # ── Render parameters ──
    WIDTH, HEIGHT = 2000, 1000
    MAX_STEPS = 5000
    N_SAMPLES = 4

    # Adaptive step: dt = DTAU_BASE × min(r/r_adapt, 1.0)
    # Far from BH → large steps.  Near BH → fine steps.
    DTAU_BASE = 0.12  # Large base step for far-field
    R_ADAPT = 5.0  # Below this radius, step shrinks linearly
    DTAU_MIN = 0.04  # Minimum step near horizon

    R_IN = 1.0
    R_OUT = 20.0
    R_ESCAPE = 50.0  # Background escape radius
    T_INNER = 12000.0

    M = 1.0
    rh = 0.5 * M
    a_star = 0.999
    a_kerr = a_star * M

    # ── Camera ──
    cam_pos = np.array([0.0, -40.0, 10.0])
    look_at = np.array([0.0, 0.0, -0.5])
    up = np.array([0.0, 0.0, 1.0])

    forward = look_at - cam_pos
    forward /= np.linalg.norm(forward)
    right = np.cross(forward, up)
    right /= np.linalg.norm(right)
    cam_up = np.cross(right, forward)

    FOV = 0.55
    aspect = WIDTH / HEIGHT
    u = np.linspace(-1, 1, WIDTH) * aspect * np.tan(FOV / 2)
    v = np.linspace(-1, 1, HEIGHT) * np.tan(FOV / 2)
    uu, vv = np.meshgrid(u, v)
    uu = uu.flatten()
    vv = vv.flatten()
    num_pixels = WIDTH * HEIGHT

    du = u[1] - u[0] if len(u) > 1 else 1e-4
    dv = v[1] - v[0] if len(v) > 1 else 1e-4

    rng = np.random.default_rng(42)
    accumulated_color = np.zeros((num_pixels, 3))

    print(f"\n  Resolution: {WIDTH}×{HEIGHT} ({num_pixels:,} pixels)")
    print(f"  Samples: {N_SAMPLES}/pixel")
    print(f"  Adaptive dt: {DTAU_BASE} (far) → {DTAU_MIN} (near)")

    for sample in range(N_SAMPLES):
        t_sample = time.time()
        print(f"\n  ── Sample {sample + 1}/{N_SAMPLES} ──")

        jitter_u = (rng.random(num_pixels) - 0.5) * du
        jitter_v = (rng.random(num_pixels) - 0.5) * dv

        ray_dirs = forward + (uu + jitter_u)[:, None] * right + (vv + jitter_v)[:, None] * cam_up
        ray_dirs /= np.linalg.norm(ray_dirs, axis=1)[:, None]

        # Use contiguous arrays for cache efficiency
        r = np.ascontiguousarray(np.tile(cam_pos, (num_pixels, 1)))
        p = np.ascontiguousarray(ray_dirs.copy())

        color_map = np.zeros((num_pixels, 3))
        final_mask = np.zeros(num_pixels, dtype=bool)
        hit_count = np.zeros(num_pixels, dtype=int)

        for step in range(MAX_STEPS):
            active = ~final_mask
            active_count = np.sum(active)

            if step % 500 == 0:
                elapsed = time.time() - t_sample
                print(f"    Step {step:5d}/{MAX_STEPS}  " f"active: {active_count:>10,}  " f"({elapsed:.1f}s)")

            if active_count == 0:
                break

            active_idx = np.where(active)[0]
            r_act = r[active_idx]
            p_act = p[active_idx]
            r_mag = np.linalg.norm(r_act, axis=1)

            # ── Event horizon ──
            hit_bh = r_mag < rh
            if np.any(hit_bh):
                final_mask[active_idx[hit_bh]] = True

            active_sub = ~hit_bh
            if not np.any(active_sub):
                continue

            r_act = r_act[active_sub]
            p_act = p_act[active_sub]
            r_mag = r_mag[active_sub]
            sub_idx = active_idx[active_sub]

            # ── Adaptive step size ──
            # Large steps far from BH, fine steps near horizon
            dt = np.clip(DTAU_BASE * r_mag / R_ADAPT, DTAU_MIN, DTAU_BASE)

            # ── AVE Hamiltonian optics ──
            W = 1.0 + rh / r_mag
            U = np.maximum(1.0 - rh / r_mag, 1e-4)
            n = (W**3) / U

            dn_dr = -(W**2) * (rh / r_mag**2) * (4.0 - 2.0 * rh / r_mag) / U**2
            r_hat = r_act / r_mag[:, None]
            grad_n = dn_dr[:, None] * r_hat

            # Frame dragging
            r2 = r_mag**2
            denom = (r2 + a_kerr**2) ** 2
            omega = 2.0 * M * a_kerr * r_mag / denom
            v_drag = np.zeros_like(r_act)
            v_drag[:, 0] = -omega * r_act[:, 1]
            v_drag[:, 1] = omega * r_act[:, 0]

            Lz = r_act[:, 0] * p_act[:, 1] - r_act[:, 1] * p_act[:, 0]
            domega_dr = 2.0 * M * a_kerr * (a_kerr**2 - 3.0 * r2) / (r2 + a_kerr**2) ** 3
            grad_pv = domega_dr[:, None] * r_hat * Lz[:, None]
            grad_pv[:, 0] += omega * p_act[:, 1]
            grad_pv[:, 1] -= omega * p_act[:, 0]

            p_mag_sq = np.sum(p_act**2, axis=1)

            # Symplectic Euler with adaptive dt
            dt_3d = dt[:, None]
            dr = (p_act / (n**2)[:, None] + v_drag) * dt_3d
            dp = ((p_mag_sq / (n**3))[:, None] * grad_n - grad_pv) * dt_3d

            r_new = r_act + dr
            p_new = p_act + dp

            # ── Accretion disk crossing ──
            crosses = (r_act[:, 2] * r_new[:, 2]) <= 0
            if np.any(crosses):
                c_mag = np.linalg.norm(r_act[crosses], axis=1)
                too_close = c_mag < rh * 1.5
                if np.any(too_close):
                    cross_all = np.where(crosses)[0]
                    crosses[cross_all[too_close]] = False

            if np.any(crosses):
                c_idx = np.where(crosses)[0]
                dz = r_new[c_idx, 2] - r_act[c_idx, 2]
                t_cross = -r_act[c_idx, 2] / (dz + 1e-8)

                rc_x = r_act[c_idx, 0] + t_cross * dr[c_idx, 0]
                rc_y = r_act[c_idx, 1] + t_cross * dr[c_idx, 1]
                rc_mag = np.sqrt(rc_x**2 + rc_y**2)

                hit_disk = (rc_mag >= R_IN) & (rc_mag <= R_OUT)
                if np.any(hit_disk):
                    hd = np.where(hit_disk)[0]
                    ci = c_idx[hd]
                    gi = sub_idx[ci]
                    rc_r = rc_mag[hd]
                    rcx = rc_x[hd]
                    rcy = rc_y[hd]

                    x = R_IN / rc_r
                    T_disk = T_INNER * x**0.75 * np.maximum(1.0 - np.sqrt(x), 0.01) ** 0.25

                    W_c = 1.0 + rh / rc_r
                    U_c = np.maximum(1.0 - rh / rc_r, 0.05)
                    z_grav = W_c / U_c

                    r_schwarz = rc_r * (1.0 + rh / rc_r) ** 2
                    v_orb = np.sqrt(np.minimum(1.0 / r_schwarz, 0.95))
                    v_disk_x = -rcy / rc_r * v_orb
                    v_disk_y = rcx / rc_r * v_orb
                    beta_sq = v_orb**2
                    gamma_inv = np.sqrt(1.0 - beta_sq)
                    v_dot_p = v_disk_x * p_act[ci, 0] + v_disk_y * p_act[ci, 1]
                    doppler = gamma_inv / np.maximum(1.0 - v_dot_p, 0.05)
                    doppler = np.clip(doppler, 0.1, 5.0)

                    T_observed = T_disk * doppler / z_grav
                    disk_rgb = _blackbody_rgb(T_observed)

                    phi = np.arctan2(rcy, rcx)
                    noise1 = _hash_noise(phi * 3.0, rc_r * 0.7, seed=1.0)
                    noise2 = _hash_noise(phi * 7.0, rc_r * 1.3, seed=2.0)
                    noise3 = _hash_noise(phi * 13.0, rc_r * 2.1, seed=3.0)
                    texture = 0.8 + 0.12 * noise1 + 0.05 * noise2 + 0.03 * noise3

                    base_lum = (2.8 / (rc_r - R_IN + 0.5) ** 1.3) * texture
                    base_lum *= doppler**3.0

                    opacity = np.clip(1.0 - ((rc_r - R_IN) / (R_OUT - R_IN)) ** 2.5, 0.05, 1.0)
                    base_lum *= opacity

                    order = hit_count[gi]
                    ring_boost = np.where(order == 0, 1.0, np.where(order == 1, 0.65, 0.35))
                    base_lum *= ring_boost

                    contrib = disk_rgb * np.clip(base_lum, 0, 4.0)[:, None]
                    color_map[gi] = np.minimum(color_map[gi] + contrib, 4.0)
                    hit_count[gi] += 1
                    final_mask[gi[hit_count[gi] >= 4]] = True

            # ── Escape ──
            r_new_mag = np.linalg.norm(r_new, axis=1)
            escapes = r_new_mag > R_ESCAPE
            if np.any(escapes):
                esc_idx = np.where(escapes)[0]
                g_esc = sub_idx[esc_idx]

                no_hit = hit_count[g_esc] == 0
                if np.any(no_hit):
                    nh_g = g_esc[no_hit]
                    p_esc = p_new[esc_idx[no_hit]]

                    h1 = np.sin(p_esc[:, 0] * 314.159 + p_esc[:, 1] * 271.828) * 1000.0
                    h1 = h1 - np.floor(h1)
                    h2 = np.sin(p_esc[:, 0] * 173.267 + p_esc[:, 2] * 432.111) * 1000.0
                    h2 = h2 - np.floor(h2)

                    bg = np.zeros((len(nh_g), 3))
                    bg[:, 0] = 0.003
                    bg[:, 1] = 0.002
                    bg[:, 2] = 0.015

                    is_star = h1 > 0.99
                    if np.any(is_star):
                        star_T = 3000.0 + h2[is_star] * 30000.0
                        star_rgb = _blackbody_rgb(star_T)
                        brightness = 0.15 + 0.85 * h1[is_star] ** 2
                        bg[is_star] = star_rgb * brightness[:, None]

                    faint = (h1 > 0.97) & (h1 <= 0.99)
                    if np.any(faint):
                        bg[faint] = np.array([0.08, 0.07, 0.09])

                    color_map[nh_g] = bg

                final_mask[g_esc] = True

            r[sub_idx] = r_new
            p[sub_idx] = p_new

        sample_time = time.time() - t_sample
        print(f"    Sample {sample + 1} done in {sample_time:.1f}s")
        accumulated_color += color_map

    accumulated_color /= N_SAMPLES

    print("\n  [Post] Tone mapping + bloom...")

    image = accumulated_color.reshape((HEIGHT, WIDTH, 3))

    # ACES filmic tone mapping with exposure
    image = _aces_tonemap(image * 1.8)

    # Dual bloom
    try:
        from scipy.ndimage import gaussian_filter

        bloom_tight = gaussian_filter(image, sigma=[2, 2, 0])
        bloom_wide = gaussian_filter(image, sigma=[8, 8, 0])
        image = np.clip(image + bloom_tight * 0.15 + bloom_wide * 0.1, 0.0, 1.0)
    except ImportError:
        pass

    # Gamma
    image = np.power(image, 0.85)

    # Vignette
    yy, xx = np.mgrid[0:HEIGHT, 0:WIDTH]
    cx, cy = WIDTH / 2, HEIGHT / 2
    vignette = 1.0 - 0.15 * ((xx - cx) ** 2 / cx**2 + (yy - cy) ** 2 / cy**2)
    image *= vignette[:, :, None]
    image = np.clip(image, 0.0, 1.0)

    # ── Render ──
    fig, ax = plt.subplots(figsize=(20, 10))
    fig.patch.set_facecolor("black")

    ax.imshow(image, interpolation="bilinear", origin="lower")
    ax.axis("off")

    total_time = time.time() - t_start
    ax.text(
        30,
        25,
        "GARGANTUA ACOUSTIC VORTEX\n"
        "AVE Raymarcher v2: Blackbody + Grav. Redshift + "
        "Doppler Beaming + ACES Filmic\n"
        r"Mass $\sim 10^8\;M_\odot$   Spin = 0.999   "
        f"Samples/px = {N_SAMPLES}   "
        f"Render time: {total_time:.0f}s",
        color="white",
        alpha=0.35,
        fontsize=10,
        family="monospace",
        verticalalignment="bottom",
    )

    plt.tight_layout(pad=0)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gargantua_acoustic_vortex.png")
    plt.savefig(out_path, dpi=250, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()

    # Copy to manuscript
    ms_dir = os.path.join(os.path.dirname(__file__), "..", "..", "manuscript", "vol_3_macroscopic", "figures")
    os.makedirs(ms_dir, exist_ok=True)
    import shutil

    shutil.copy2(out_path, os.path.join(ms_dir, "gargantua_acoustic_vortex.png"))

    print(f"\n  Saved: {out_path}")
    print(f"  Copied to manuscript figures")
    print(f"  Total render time: {total_time:.1f}s")
    print("=" * 70)


if __name__ == "__main__":
    render_gargantua()
