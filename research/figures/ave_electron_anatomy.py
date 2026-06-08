"""Anatomy of the AVE electron: phase-space (2,3) knot, real-space cubic (T_d)
envelope, the LC/spin/mass/charge anatomy, and the dual-POV life-cycle. Saves one PNG."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle

fig = plt.figure(figsize=(17, 11))
fig.suptitle("Anatomy of the AVE electron — a (2,3) knot in phase space, a cubic (T_d) envelope in real space",
             fontsize=15, fontweight="bold")

# ---- Panel 1: PHASE SPACE — the (2,3) torus knot ----
ax1 = fig.add_subplot(2, 3, 1, projection="3d")
t = np.linspace(0, 2*np.pi, 1200)
p, q = 2, 3
R, r = 1.0, 0.42
xk = (R + r*np.cos(q*t))*np.cos(p*t)
yk = (R + r*np.cos(q*t))*np.sin(p*t)
zk = r*np.sin(q*t)
ax1.plot(xk, yk, zk, color="crimson", lw=2.4)
ax1.set_title("PHASE SPACE\n(2,3) torus knot on the Clifford torus  ·  R/r=φ²", fontsize=10)
ax1.set_axis_off(); ax1.view_init(elev=28, azim=35)

# ---- Panel 2: REAL SPACE — the cubic (T_d) saturated envelope ----
ax2 = fig.add_subplot(2, 3, 2, projection="3d")
def sq(w, m):  # superquadric helper
    return np.sign(w)*np.abs(w)**m
u = np.linspace(-np.pi/2, np.pi/2, 60)
v = np.linspace(-np.pi, np.pi, 60)
U, V = np.meshgrid(u, v)
e = 0.32  # rounded-cube exponent
Xe = sq(np.cos(U), e)*sq(np.cos(V), e)
Ye = sq(np.cos(U), e)*sq(np.sin(V), e)
Ze = sq(np.sin(U), e)
ax2.plot_surface(Xe, Ye, Ze, color="steelblue", alpha=0.22, linewidth=0, antialiased=True)
ax2.plot(0.55*xk, 0.55*yk, 0.55*zk, color="crimson", lw=1.4, alpha=0.9)  # knot inside
ax2.set_title("REAL SPACE\ncubic (T_d) field envelope — NOT a sphere\n(sphere would falsify AVE); knot inside", fontsize=9.5)
ax2.set_axis_off(); ax2.view_init(elev=22, azim=40)

# ---- Panel 3: the anatomy (LC / spin / mass / charge / loss) ----
ax3 = fig.add_subplot(2, 3, 3)
ax3.add_patch(Circle((0.5, 0.55), 0.30, fill=False, lw=2.2, color="steelblue"))
ax3.add_patch(Circle((0.5, 0.55), 0.07, color="crimson")); ax3.text(0.5,0.55,"B",ha="center",va="center",color="w",fontsize=8,fontweight="bold")
ax3.add_patch(Circle((0.30, 0.55), 0.03, color="k")); ax3.add_patch(Circle((0.70, 0.55), 0.03, color="k"))
ax3.text(0.30,0.49,"node",ha="center",fontsize=7); ax3.text(0.70,0.49,"node",ha="center",fontsize=7)
ax3.annotate("", xy=(0.66,0.62), xytext=(0.34,0.62), arrowprops=dict(arrowstyle="<->",color="purple"))
ax3.text(0.5,0.64,"LC tank  ω_C=m_ec²/ℏ",ha="center",fontsize=8,color="purple")
ax3.annotate("", xy=(0.5,0.92), xytext=(0.5,0.86), arrowprops=dict(arrowstyle="->",color="green"))
ax3.text(0.5,0.80,"spin-½ (Cosserat, 720°)",ha="center",fontsize=8,color="green")
txt = ("• flux tube = L (B-core)\n• two nodes = C (terminals)\n• mass = stored near-field = m_ec²\n"
       "• charge = topological dislocation [Q]≡[L]\n• loss tangent = α = 1/Q (→1.5% from z₀=52)")
ax3.text(0.02, 0.30, txt, fontsize=8.5, va="top")
ax3.set_title("THE ANATOMY — one LC resonator, six readouts", fontsize=10)
ax3.set_xlim(0,1); ax3.set_ylim(0,1); ax3.axis("off")

# ---- Panel 4+5+6 (bottom row span): the dual-POV life-cycle ----
ax4 = fig.add_subplot(2, 1, 2)
stages = ["GENESIS","CONFINE","STRUCTURE","RESONATE","SPIN+MASS","PROPAGATE","LOSE (α)"]
elec = ["I form from a\nself-trapped wave","I'm walled in\nmy own TIR","I wind (2,3);\nmy shell facets cubic",
        "I tick at ω_C\n(Compton clock)","I'm a spinor;\nmy energy is my mass","I surf as λ=h/p;\nmy cube won't tumble","I slip α per orbit\n(dark-wake)"]
vac  = ["a region saturates,\nlocks a defect","I Meissner-expel\nthe field","I host a (2,3) decoration\non z=4 diamond",
        "I oscillate the\nbond LC tank","my microrotation =\nZ₂ topology","I pass it node→node,\nc_eff=c√(1−A²)","I radiate the\nfar-field"]
N = len(stages); xs = np.linspace(0.06, 0.94, N)
for i,x in enumerate(xs):
    ax4.add_patch(Rectangle((x-0.055,0.46),0.11,0.16, fc="#eef2f8", ec="navy"))
    ax4.text(x,0.54,stages[i],ha="center",va="center",fontsize=8.5,fontweight="bold")
    ax4.text(x,0.78,elec[i],ha="center",va="center",fontsize=7.2,color="crimson")
    ax4.text(x,0.20,vac[i],ha="center",va="center",fontsize=7.2,color="steelblue")
    if i<N-1: ax4.annotate("",xy=(xs[i+1]-0.06,0.54),xytext=(x+0.056,0.54),arrowprops=dict(arrowstyle="->",color="navy"))
ax4.text(0.005,0.78,"ELECTRON\nPOV",ha="left",va="center",fontsize=8.5,color="crimson",fontweight="bold")
ax4.text(0.005,0.20,"VACUUM\nPOV",ha="left",va="center",fontsize=8.5,color="steelblue",fontweight="bold")
ax4.set_title("THE LIFE OF THE ELECTRON — electron's view (red) vs the vacuum's view (blue)", fontsize=11)
ax4.set_xlim(0,1); ax4.set_ylim(0,1); ax4.axis("off")

plt.tight_layout(rect=[0,0,1,0.96])
plt.savefig("research/figures/ave_electron_anatomy.png", dpi=115, bbox_inches="tight")
print("saved research/figures/ave_electron_anatomy.png")
