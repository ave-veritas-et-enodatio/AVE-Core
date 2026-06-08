"""Electron-as-(2,3)-flux-tube: FBD + envelope + energy + phase portrait.
All panels schematic-but-labeled with real AVE constants. Saves one PNG."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

fig, ax = plt.subplots(2, 3, figsize=(16.5, 10.5))
fig.suptitle("Electron as a (2,3) flux tube — dynamics (all standard physics; AVE-specific marked *)",
             fontsize=15, fontweight="bold")

def arrow(a, x0, y0, x1, y1, c, lw=2.2, ls="-"):
    a.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=16,
                                color=c, lw=lw, linestyle=ls))

# ---- Panel 1: FBD radial (cross-section pressure balance) ----
a = ax[0, 0]
a.add_patch(Circle((0, 0), 1.0, fill=False, lw=2.4, color="k"))
a.add_patch(Circle((0, 0), 0.18, color="crimson"))  # B-core
a.text(0, -0.02, "B", ha="center", va="center", color="white", fontweight="bold")
for ang in np.linspace(0, 2*np.pi, 8, endpoint=False):  # outward magnetic pressure
    arrow(a, 1.05*np.cos(ang), 1.05*np.sin(ang), 1.55*np.cos(ang), 1.55*np.sin(ang), "darkorange")
for ang in np.linspace(0, 2*np.pi, 8, endpoint=False)+0.39:  # inward confinement
    arrow(a, 1.85*np.cos(ang), 1.85*np.sin(ang), 1.18*np.cos(ang), 1.18*np.sin(ang), "navy")
arrow(a, 0, 1.6, 0, 2.25, "green")     # parametric gain (up)
arrow(a, 0, 2.25, 0, 1.6, "purple", ls="--")  # radiation reaction (down)
a.text(1.6, 1.7, "P_mag = B²/2μ₀\n(out)", color="darkorange", fontsize=9)
a.text(-2.55, -1.9, "S(A) confine *\n(in, Meissner)", color="navy", fontsize=9)
a.text(0.1, 2.05, "Γ_gain (parametric)\n⇅ Γ_rad (dark-wake)", color="green", fontsize=8.5)
a.set_title("FBD — radial balance\nP_mag + ρΩ²r  =  S(A) + T_hoop/r → r_eq~ℓ_node", fontsize=10)
a.set_xlim(-2.7, 2.7); a.set_ylim(-2.4, 2.6); a.set_aspect("equal"); a.axis("off")

# ---- Panel 2: FBD loop ((2,3) line-tension vs topology) ----
a = ax[0, 1]
t = np.linspace(0, 2*np.pi, 800)
p, q = 2, 3; R, r = 1.0, 0.42
xl = (R + r*np.cos(q*t))*np.cos(p*t); yl = (R + r*np.cos(q*t))*np.sin(p*t)
a.plot(xl, yl, "k", lw=2.4)
for ang in np.linspace(0, 2*np.pi, 6, endpoint=False):  # line tension inward (shrink)
    arrow(a, 1.7*np.cos(ang), 1.7*np.sin(ang), 1.15*np.cos(ang), 1.15*np.sin(ang), "navy")
for ang in np.linspace(0, 2*np.pi, 6, endpoint=False)+0.5:  # topological resist outward
    arrow(a, 0.55*np.cos(ang), 0.55*np.sin(ang), 1.0*np.cos(ang), 1.0*np.sin(ang), "darkorange")
a.text(-2.45, 1.65, "T_line = B²/μ₀\n= T_EM = 0.212 N\n(shrink)", color="navy", fontsize=9)
a.text(-0.6, -0.1, "topology\nresists", color="darkorange", fontsize=8.5, ha="center")
a.set_title("FBD — loop balance\nT_line = P_self + (knot can't unwind)", fontsize=10)
a.set_xlim(-2.1, 2.1); a.set_ylim(-2.0, 2.0); a.set_aspect("equal"); a.axis("off")

# ---- Panel 3: the (2,3) torus knot ----
a = ax[0, 2]
zc = r*np.sin(q*t)
sc = a.scatter(xl, yl, c=zc, cmap="twilight", s=6)
a.set_title("(2,3) torus knot\nLk = Tw + Wr ;  Tw = q/p = 540°/rev", fontsize=10)
a.set_xlim(-1.6, 1.6); a.set_ylim(-1.6, 1.6); a.set_aspect("equal"); a.axis("off")

# ---- Panel 4: time-averaged angular envelope (bulges/valleys) ----
a = ax[1, 0]; a.remove()
a = fig.add_subplot(2, 3, 4, projection="polar")
tt = np.linspace(0, 2*np.pi, 20000)
xe = (R + r*np.cos(q*tt))*np.cos(p*tt); ye = (R + r*np.cos(q*tt))*np.sin(p*tt)
az = np.arctan2(ye, xe); rho = np.hypot(xe, ye)
nb = 180; edges = np.linspace(-np.pi, np.pi, nb+1)
idx = np.digitize(az, edges) - 1; idx = np.clip(idx, 0, nb-1)
dens = np.bincount(idx, weights=rho, minlength=nb)  # time-weighted radial mass per az
centers = 0.5*(edges[:-1]+edges[1:])
dens = dens/dens.max()
a.plot(np.append(centers, centers[0]), np.append(dens, dens[0]), color="crimson", lw=2.2)
a.fill(np.append(centers, centers[0]), np.append(dens, dens[0]), color="crimson", alpha=0.18)
a.set_title("Time-averaged envelope\n(bulges at nodes / valleys between)", fontsize=10, pad=18)
a.set_yticklabels([])

# ---- Panel 5: energy-transfer flow ----
a = ax[1, 1]
a.add_patch(plt.Rectangle((0.1, 0.55), 0.32, 0.3, fc="#bcd", ec="k"))
a.add_patch(plt.Rectangle((0.58, 0.55), 0.32, 0.3, fc="#dcb", ec="k"))
a.text(0.26, 0.70, "C-state\n(E / V_inc)", ha="center", va="center", fontsize=10)
a.text(0.74, 0.70, "L-state\n(B / Φ_link)", ha="center", va="center", fontsize=10)
arrow(a, 0.42, 0.74, 0.58, 0.74, "k"); arrow(a, 0.58, 0.66, 0.42, 0.66, "k")
a.text(0.5, 0.79, "ω_C = m_ec²/ℏ", ha="center", fontsize=9)
arrow(a, 0.5, 0.18, 0.5, 0.53, "green")   # gain in
arrow(a, 0.9, 0.55, 1.02, 0.42, "purple")  # loss out
a.text(0.5, 0.10, "gain: saturating reactance *\n(parametric pump, 2ω_C)", ha="center", color="green", fontsize=8.5)
a.text(0.78, 0.36, "loss: dark-wake\n(far-field, α/cycle)", color="purple", fontsize=8.5)
a.text(0.5, 0.95, "stored (near-field) = m_ec²  ·  threshold: gain = loss",
       ha="center", fontsize=9, fontweight="bold")
a.set_title("Energy transfer — LC tank H=T+V", fontsize=10)
a.set_xlim(0, 1.1); a.set_ylim(0, 1.05); a.axis("off")

# ---- Panel 6: limit-cycle phase portrait (Hopf) ----
a = ax[1, 2]
mu = 1.0; om = 6.0; dt = 0.01
for r0 in (1.55, 0.25):
    rr, th = r0, 0.0; xs, ys = [], []
    for _ in range(900):
        rr += dt*rr*(mu - rr*rr); th += dt*om
        xs.append(rr*np.cos(th)); ys.append(rr*np.sin(th))
    a.plot(xs, ys, lw=1.1, color="gray")
ang = np.linspace(0, 2*np.pi, 300)
a.plot(np.sqrt(mu)*np.cos(ang), np.sqrt(mu)*np.sin(ang), color="crimson", lw=2.6)
a.text(0, 0, "gain=loss\nlimit cycle", ha="center", va="center", color="crimson", fontsize=9, fontweight="bold")
a.set_title("Limit-cycle phase portrait (Hopf)\nrings at ω_C forever = the electron", fontsize=10)
a.set_xlim(-1.7, 1.7); a.set_ylim(-1.7, 1.7); a.set_aspect("equal"); a.axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("research/figures/flux_tube_dynamics.png", dpi=115, bbox_inches="tight")
print("saved research/figures/flux_tube_dynamics.png")
