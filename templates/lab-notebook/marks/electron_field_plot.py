"""Legacy 2-panel field-density plot. Superseded by electron_field_density_v2.py
(adds envelope framing + a phase-space (2,3) panel). Kept as the simpler reference
plotter; captions match v2's honest framing (real-space envelope; (2,3) is phase-space)."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

d = np.load('/tmp/efield_solve.npz')
ell = float(d['ellnode_cells'])          # grid cells per ell_node
nx = int(d['nx']); Rg = float(d['R_grid']); rg = float(d['r_grid'])
PHI = (1+5**0.5)/2

# pick the slice plane with the most structure (the equatorial / torus plane)
def pick(prefix):
    opts = {p: d[f'{prefix}_{p}'] for p in ('xy','xz','yz')}
    return max(opts.items(), key=lambda kv: kv[1].std())
Vp, V = pick('V'); Bp, B = pick('B')
V = np.abs(V); V = V/ (V.max() or 1)
B = B / (B.max() or 1)

EARTHBG='#1E1813'; RUST='#A8542E'; YLW='#FFD21E'; BLUE='#2E72FF'
cmapV=LinearSegmentedColormap.from_list('V',[(0,'#140F0B'),(0.35,'#7A3D22'),(0.62,RUST),(0.85,YLW),(1,'#FFF4CC')])
cmapB=LinearSegmentedColormap.from_list('B',[(0,'#0C1020'),(0.40,'#1E3A78'),(0.70,BLUE),(0.90,'#8FB6FF'),(1,'#E6F0FF')])

# axes in ell_node units (grid centered)
half = (nx/2)/ell
ext = [-half, half, -half, half]

fig,axs=plt.subplots(1,2,figsize=(13.8,7.4)); fig.patch.set_facecolor(EARTHBG)
panels=[(axs[0],V,cmapV,YLW,'NODE-VOLTAGE ENVELOPE  $V=\\nabla\\!\\cdot u$',f'real space · capacitive / E-DOF · equatorial slice ({Vp})'),
        (axs[1],B,cmapB,BLUE,'MAGNETIC ENVELOPE  $|B|=|\\omega|$',f'real space · inductive / B-DOF · only the $w_1{{=}}2$ toroidal projection ({Bp})')]
for ax,F,cm,tc,title,sub in panels:
    ax.set_facecolor(EARTHBG)
    ax.imshow(F.T,origin='lower',extent=ext,cmap=cm,interpolation='bilinear')
    # K4 lattice nodes at ell_node pitch (the real lattice; grid is a fine mesh)
    gpos=np.arange(-np.floor(half),np.floor(half)+0.01,1.0)
    GX,GY=np.meshgrid(gpos,gpos)
    ax.scatter(GX,GY,s=5,c='white',alpha=0.10,linewidths=0)
    # Golden-Torus circles (ell_node units)
    th=np.linspace(0,2*np.pi,300); Re=PHI/2; re=(PHI-1)/2
    for rad in (Re+re,Re-re):
        ax.plot(rad*np.cos(th),rad*np.sin(th),color=tc,lw=0.8,alpha=0.5)
    ax.plot(Re*np.cos(th),Re*np.sin(th),color='white',lw=1.0,alpha=0.65,ls=(0,(4,2)))
    ax.set_xlim(-half,half); ax.set_ylim(-half,half); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title,color='#EDE6D6',fontsize=15.5,fontweight='bold',pad=12)
    ax.text(0.5,-0.05,sub,transform=ax.transAxes,ha='center',va='top',color='#B9AE92',fontsize=9)
    for sp in ax.spines.values(): sp.set_color('#3A3320')
axs[0].plot([-half+0.4,-half+1.4],[-half+0.45,-half+0.45],color='#EDE6D6',lw=2.2)
axs[0].text(-half+0.9,-half+0.62,'$1\\,\\ell_{node}$',color='#EDE6D6',ha='center',fontsize=8.5)
fig.text(0.5,0.022,'Continuum CosseratField3D solve at $dx\\approx0.1\\,\\ell_{node}$ (below the $\\ell_{node}=\\hbar/m_ec$ cutoff) — real-space ENVELOPE only.  '
         'The $(2,3)$ is a phase-space object in the $(V_{inc},V_{ref})$ phasor [theory.md:16], absent from this continuum field.  '
         '$R=\\varphi/2,\\ r=(\\varphi{-}1)/2,\\ R\\!\\cdot\\!r=1/4$.',
         ha='center',color='#9CC0FF',fontsize=9)
plt.subplots_adjust(left=0.012,right=0.988,top=0.92,bottom=0.115,wspace=0.04)
plt.savefig('/tmp/electron_fields_engine.png',dpi=150,facecolor=EARTHBG)
print('plotted; V slice',Vp,'B slice',Bp,'half(ell_node)=%.2f'%half)
