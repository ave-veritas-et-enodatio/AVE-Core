"""Electron anatomy v2: PHASE space (2,3 knot in E-B plane) vs REAL space (cubic
surface-tension skin with E/B energy + unknot inside) + the force balance (FBD)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

fig = plt.figure(figsize=(17, 11))
fig.suptitle("Anatomy of the AVE electron — PHASE space (E-B winding) vs REAL space (cubic surface-tension skin) + forces",
             fontsize=14.5, fontweight="bold")

def arr(ax, x0,y0,x1,y1,c,lw=2.0,ls="-"):
    ax.add_patch(FancyArrowPatch((x0,y0),(x1,y1),arrowstyle="-|>",mutation_scale=15,color=c,lw=lw,linestyle=ls))

# ---- (a) PHASE SPACE: (2,3) knot in the E-B / (V_inc,V_ref) plane ----
ax1 = fig.add_subplot(2,3,1, projection="3d")
t = np.linspace(0,2*np.pi,1400); p,q=2,3; R,r=1.0,0.42
xk=(R+r*np.cos(q*t))*np.cos(p*t); yk=(R+r*np.cos(q*t))*np.sin(p*t); zk=r*np.sin(q*t)
ax1.plot(xk,yk,zk,color="crimson",lw=2.3)
ax1.set_title("PHASE SPACE — the field STATE\n(2,3) winding on the Clifford torus\nE~(V_inc+V_ref)  ·  B~(V_inc−V_ref)/Z",fontsize=9.5)
ax1.set_axis_off(); ax1.view_init(elev=26,azim=35)

# ---- (b) REAL SPACE: cubic surface-tension skin + E/B energy + unknot inside ----
ax2 = fig.add_subplot(2,3,2, projection="3d")
def sq(w,m): return np.sign(w)*np.abs(w)**m
u=np.linspace(-np.pi/2,np.pi/2,60); v=np.linspace(-np.pi,np.pi,60); U,V=np.meshgrid(u,v); e=0.32
Xe=sq(np.cos(U),e)*sq(np.cos(V),e); Ye=sq(np.cos(U),e)*sq(np.sin(V),e); Ze=sq(np.sin(U),e)
ax2.plot_surface(Xe,Ye,Ze,color="steelblue",alpha=0.20,linewidth=0)            # the SKIN
ax2.plot_wireframe(0.985*Xe,0.985*Ye,0.985*Ze,color="navy",lw=0.3,alpha=0.25)  # facet hint
th=np.linspace(0,2*np.pi,200); ax2.plot(0.5*np.cos(th),0.5*np.sin(th),0.0*th,color="crimson",lw=1.8)  # 0_1 unknot
ax2.set_title("REAL SPACE — the field LOCATION\ncubic (T_d) SURFACE-TENSION skin (blue)\nE/B energy + 0₁ unknot loop INSIDE (red)",fontsize=9.5)
ax2.set_axis_off(); ax2.view_init(elev=20,azim=40)

# ---- (c) the FBD: radial force balance across the skin ----
ax3 = fig.add_subplot(2,3,3)
ax3.add_patch(Circle((0,0),1.0,fill=False,lw=2.4,color="steelblue"))  # the skin
ax3.add_patch(Circle((0,0),0.16,color="crimson")); ax3.text(0,0,"E/B",ha="center",va="center",color="w",fontsize=7,fontweight="bold")
for a in np.linspace(0,2*np.pi,8,endpoint=False):
    arr(ax3,0.20*np.cos(a),0.20*np.sin(a),0.92*np.cos(a),0.92*np.sin(a),"darkorange")     # field pressure OUT
    arr(ax3,1.7*np.cos(a+0.39),1.7*np.sin(a+0.39),1.06*np.cos(a+0.39),1.06*np.sin(a+0.39),"navy")  # saturation IN
for a in np.linspace(0,2*np.pi,4,endpoint=False)+0.2:  # surface tension tangent
    arr(ax3,1.0*np.cos(a)-0.18*np.sin(a),1.0*np.sin(a)+0.18*np.cos(a),1.0*np.cos(a)+0.18*np.sin(a),1.0*np.sin(a)-0.18*np.cos(a),"green",1.6)
arr(ax3,0,1.55,0,2.05,"purple",ls="--")  # radiation reaction
ax3.text(1.0,1.85,"field pressure\nB²/2μ₀ (out)",color="darkorange",fontsize=8)
ax3.text(-2.7,-1.95,"saturation\nconfine S(A) (in)",color="navy",fontsize=8)
ax3.text(-2.7,1.5,"surface tension\n(skin, tangent)",color="green",fontsize=8)
ax3.text(0.1,1.95,"radiation reaction\n(dark-wake, α/orbit)",color="purple",fontsize=7.5)
ax3.set_title("FBD — radial balance\nP_field + ρΩ²r  =  S(A) + γ_surface/r + T_line/r",fontsize=9.5)
ax3.set_xlim(-2.9,2.9); ax3.set_ylim(-2.5,2.3); ax3.set_aspect("equal"); ax3.axis("off")

# ---- (d,e,f bottom span): the answer + the two-space table + anatomy ----
ax4 = fig.add_subplot(2,1,2); ax4.axis("off"); ax4.set_xlim(0,1); ax4.set_ylim(0,1)
ax4.text(0.5,0.93,"THE CUBE IS THE SKIN, NOT THE FIELD",ha="center",fontsize=12,fontweight="bold",color="navy")
ax4.text(0.5,0.84,"cubic (T_d) envelope = the SURFACE TENSION between the soliton's energy and the vacuum  ·  E/B field = the energy CONFINED inside it",
         ha="center",fontsize=10)
# two-space table
rows = [("","PHASE SPACE  (field state)","REAL SPACE  (field location)"),
        ("coordinate","(V_inc, V_ref) = (E, B) phasor plane","lattice positions (x,y,z)"),
        ("topology","(2,3) winding on Clifford torus, R/r=φ²","0₁ unknot (simple loop, ~1 bond)"),
        ("shape","Golden Torus","cubic (T_d) surface-tension skin"),
        ("set by","SCATTER (E↔B reactive exchange at a bond)","CONNECT (node→node transport)")]
y0=0.66;
for i,(c0,c1,c2) in enumerate(rows):
    yy=y0-i*0.105; fw="bold" if i==0 else "normal"
    ax4.text(0.06,yy,c0,fontsize=9,fontweight="bold")
    ax4.text(0.30,yy,c1,fontsize=9,fontweight=fw,color="crimson" if i>0 else "k",ha="center")
    ax4.text(0.74,yy,c2,fontsize=9,fontweight=fw,color="steelblue" if i>0 else "k",ha="center")
ax4.axhline; ax4.plot([0.02,0.98],[0.715,0.715],color="gray",lw=0.6)
ax4.plot([0.52,0.52],[0.07,0.71],color="gray",lw=0.6)
ax4.text(0.5,0.02,"anatomy: ω_C=m_ec²/ℏ (LC) · spin-½ (Cosserat, 720°) · mass=near-field reactance · charge=[Q]≡[L] dislocation · α=1/Q loss tangent (→1.5% from z₀=52)",
         ha="center",fontsize=8.5,style="italic")
plt.tight_layout(rect=[0,0,1,0.96])
plt.savefig("research/figures/ave_electron_anatomy_v2.png",dpi=115,bbox_inches="tight")
print("saved research/figures/ave_electron_anatomy_v2.png")
