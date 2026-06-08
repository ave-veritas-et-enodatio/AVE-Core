"""Photon propagating ALONG vacuum cells (it moves) vs electron self-trapped in
its cubic envelope (it stands). Saves a static 3-snapshot strip PNG + a GIF.
Photon = faithful transverse wave-packet (wave-eq solution); electron = schematic
self-trapped soliton (sech) + cubic-envelope skin. Cells = K4 bond-LC nodes."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Rectangle

N = 44                      # vacuum cells along the line
xf = np.linspace(0, N-1, 500)
xs = np.arange(N)
w, k = 3.6, 1.5             # photon packet width, wavenumber
c = 0.46                    # cells/frame (photon speed)
xc, we, ke, om = 22, 2.3, 2.2, 0.5   # electron: center, width, internal-k, breathe

def photonE(t):  x0 = 4 + c*t; return np.exp(-((xf-x0)/w)**2)*np.cos(k*(xf-x0)), x0
def photonI(t):  x0 = 4 + c*t; return np.exp(-((xs-x0)/w)**2)**2
def elecE(t):    return (1/np.cosh((xf-xc)/we))*np.cos(ke*(xf-xc)-om*t)
def elecI():     I=(1/np.cosh((xs-xc)/we))**2; return I/I.max()

def draw_cells(ax):
    for xi in range(N):
        ax.add_patch(Rectangle((xi-0.45,-1.62),0.9,0.34,fc="#eef1f6",ec="#c3c9d8",lw=0.4,zorder=1))

# ---------- static 3-snapshot strip ----------
fig, axes = plt.subplots(2, 3, figsize=(15, 6.4))
fig.suptitle("A photon propagating along vacuum cells  vs  an electron standing in its cubic envelope",
             fontsize=14, fontweight="bold")
times = [6, 34, 62]
for col, t in enumerate(times):
    ap, ae = axes[0, col], axes[1, col]
    for ax in (ap, ae):
        ax.set_xlim(-1, N); ax.set_ylim(-1.75, 1.55); ax.set_xticks([]); ax.set_yticks([]); draw_cells(ax)
    # photon row
    Ep, x0 = photonE(t)
    ap.plot(xf, Ep, color="crimson", lw=2.0, zorder=3)
    ap.scatter(xs, np.full(N,-1.45), c=photonI(t)/(photonI(t).max()+1e-9), cmap="hot",
               vmin=0, vmax=1, s=42, marker="s", zorder=2)
    ap.set_title(f"PHOTON   t={col+1}", fontsize=9.5, loc="left", color="crimson")
    if col==2: ap.annotate("moves →", xy=(x0,1.25), fontsize=9, color="crimson", ha="center")
    # electron row
    ae.plot(xf, elecE(t), color="crimson", lw=2.0, zorder=3)
    ae.scatter(xs, np.full(N,-1.45), c=elecI(), cmap="hot", vmin=0, vmax=1, s=42, marker="s", zorder=2)
    ae.add_patch(Rectangle((xc-3.6,-1.1), 7.2, 2.25, fill=False, ec="steelblue", lw=2.0, zorder=4))
    ae.set_title(f"ELECTRON   t={col+1}", fontsize=9.5, loc="left", color="steelblue")
    if col==1: ae.text(xc, 1.32, "cubic envelope = the SKIN (stays put)", ha="center", fontsize=8, color="steelblue")
axes[0,0].text(0.5,1.3,"the wave-packet rides the cells →", fontsize=8, color="crimson")
axes[1,0].text(0.5,-1.95,"cells = the K4 lattice medium (the 'road'); envelope = the soliton's shell (the 'car')",
               fontsize=8, color="dimgray")
plt.tight_layout(rect=[0,0,1,0.95])
plt.savefig("research/figures/photon_vs_electron_cells_strip.png", dpi=110, bbox_inches="tight")
print("saved strip")

# ---------- GIF ----------
figg, (axp, axe) = plt.subplots(2, 1, figsize=(12, 7))
figg.suptitle("Photon propagates ALONG the cells  ·  Electron STANDS in its cubic envelope", fontsize=12.5, fontweight="bold")
for ax, ttl, col in [(axp,"PHOTON — free transverse wave, moves along the cells","crimson"),
                     (axe,"ELECTRON — self-trapped soliton, fixed inside its cubic skin","steelblue")]:
    ax.set_xlim(-1,N); ax.set_ylim(-1.75,1.55); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(ttl, fontsize=10, loc="left", color=col); draw_cells(ax)
pc, = axp.plot([],[],color="crimson",lw=2.2,zorder=3)
pcell = axp.scatter(xs, np.full(N,-1.45), c=np.zeros(N), cmap="hot", vmin=0, vmax=1, s=55, marker="s", zorder=2)
ec, = axe.plot([],[],color="crimson",lw=2.2,zorder=3)
ecell = axe.scatter(xs, np.full(N,-1.45), c=elecI(), cmap="hot", vmin=0, vmax=1, s=55, marker="s", zorder=2)
axe.add_patch(Rectangle((xc-3.6,-1.1),7.2,2.25,fill=False,ec="steelblue",lw=2.2,zorder=4))
axe.text(xc,1.3,"cubic envelope (saturation skin)",ha="center",fontsize=8,color="steelblue")

def animate(f):
    Ep,_ = photonE(f); pc.set_data(xf,Ep); I=photonI(f); pcell.set_array(I/(I.max()+1e-9))
    ec.set_data(xf, elecE(f)); ecell.set_array(elecI())
    return pc,pcell,ec,ecell
anim = FuncAnimation(figg, animate, frames=64, interval=70, blit=False)
anim.save("research/figures/photon_vs_electron_cells.gif", writer=PillowWriter(fps=14), dpi=80)
print("saved gif")
