"""The K4 (diamond) vacuum lattice, all at once, with a localized displacement:
- nodes DISPLACED from equilibrium by a soliton's u-field (the displacement)
- node color = field amplitude / saturation level (heatmap)
- per-node polarization PHASOR (quiver) — circulating winding around the defect
Illustrative schematic of the substrate state (not an engine snapshot)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- build a chunk of the diamond (K4) lattice ----
N = 3
fcc = [(0,0,0),(0.5,0.5,0),(0.5,0,0.5),(0,0.5,0.5)]
basis = [(0,0,0),(0.25,0.25,0.25)]
nodes = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            for f in fcc:
                for b in basis:
                    nodes.append((i+f[0]+b[0], j+f[1]+b[1], k+f[2]+b[2]))
nodes = np.array(nodes)
center = np.array([N/2.0]*3)
rvec = nodes - center
r = np.linalg.norm(rvec, axis=1)
sig = 0.85

# field amplitude / saturation level (high = saturated core)
A = np.exp(-r**2/(2*sig**2))

# the DISPLACEMENT: nodes pushed radially out of equilibrium by the soliton u-field
rhat = rvec/(r[:,None]+1e-9)
u = 0.30*rhat*np.exp(-r**2/(2*sig**2))[:,None]
nd = nodes + u                       # displaced positions

# polarization PHASOR: azimuthal circulation (chiral winding) about the defect z-axis,
# magnitude peaking in the shell, with a small vertical winding component
dxy = rvec[:,:2]; nxy = np.linalg.norm(dxy,axis=1)+1e-9
pol = np.zeros_like(rvec)
pol[:,0] = -dxy[:,1]/nxy; pol[:,1] = dxy[:,0]/nxy
mag = r*np.exp(-r**2/(2*sig**2))     # shell-peaked
pol *= mag[:,None]
pol[:,2] = 0.35*mag*np.sin(3*np.arctan2(dxy[:,1],dxy[:,0]))   # (·,3)-ish winding hint

fig = plt.figure(figsize=(17,8))
fig.suptitle("The AVE vacuum lattice, all at once — diamond (K4) nodes DISPLACED by a soliton; "
             "colour = saturation level; cyan = polarization phasor (winding)", fontsize=13, fontweight="bold")

# ---- 3D ----
ax = fig.add_subplot(1,2,1, projection="3d")
ax.scatter(nodes[:,0],nodes[:,1],nodes[:,2], c="lightgray", s=6, alpha=0.35)   # equilibrium (faint)
p = ax.scatter(nd[:,0],nd[:,1],nd[:,2], c=A, cmap="inferno", s=46, alpha=0.95) # displaced, colored by saturation
ax.quiver(nd[:,0],nd[:,1],nd[:,2], pol[:,0],pol[:,1],pol[:,2],
          length=0.45, color="cyan", lw=1.1, alpha=0.75, normalize=False)
fig.colorbar(p, ax=ax, shrink=0.55, pad=0.02, label="saturation level  A/A_yield")
ax.set_title("3D — grey = equilibrium, lit = displaced + saturated; phasors wind the defect", fontsize=9.5)
ax.set_axis_off(); ax.view_init(elev=22, azim=35)

# ---- 2D z-slice ----
ax2 = fig.add_subplot(1,2,2)
zc = N/2.0; m = np.abs(nodes[:,2]-zc) < 0.45
xs,ys = nd[m,0],nd[m,1]; As=A[m]; px,py=pol[m,0],pol[m,1]
xe,ye = nodes[m,0],nodes[m,1]
ax2.scatter(xe,ye,c="lightgray",s=18,alpha=0.4)                  # equilibrium
for (x0,y0,x1,y1) in zip(xe,ye,xs,ys):                           # displacement vectors
    ax2.plot([x0,x1],[y0,y1],color="gray",lw=0.5,alpha=0.5)
sc = ax2.scatter(xs,ys,c=As,cmap="inferno",s=150,zorder=3)
ax2.quiver(xs,ys,px,py,color="cyan",scale=9,width=0.005,zorder=4)
fig.colorbar(sc,ax=ax2,label="saturation level  A/A_yield")
ax2.set_title("z-slice — nodes pulled off equilibrium (grey→lit); phasors circulate; core saturates", fontsize=9.5)
ax2.set_aspect("equal"); ax2.set_xticks([]); ax2.set_yticks([])

plt.tight_layout(rect=[0,0,1,0.96])
plt.savefig("research/figures/lattice_polarization_saturation.png", dpi=120, bbox_inches="tight")
print("saved research/figures/lattice_polarization_saturation.png")
