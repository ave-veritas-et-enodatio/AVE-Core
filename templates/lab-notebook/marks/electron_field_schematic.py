import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ---- canonical AVE constants (ell_node units) ----
PHI=(1.0+5.0**0.5)/2.0
R=PHI/2.0; rmin=(PHI-1.0)/2.0          # Golden Torus  (constants.py:200-201)
LAMC=2.0*np.pi                          # Compton lambda_C = 2 pi ell_node
A=1.0                                   # lattice pitch = ell_node
L=7.5
EARTHBG='#1E1813'; RUST='#A8542E'; YLW='#FFD21E'; BLUE='#2E72FF'

N=520; xs=np.linspace(-L,L,N); X,Y=np.meshgrid(xs,xs); Rr=np.hypot(X,Y); TH=np.arctan2(Y,X)

# Voltage (capacitive/E): charge core (softened at d/2=1/2) x Compton standing wave
charge=1.0/np.sqrt(Rr**2+0.25)
V=np.abs(charge*np.cos(2*np.pi*Rr/LAMC)); V/=V.max()
# Magnetic density (inductive/B): unknot current-loop moment, ring at R, fast decay
B=1.0/(1+(Rr/R)**2)**1.4 + 0.55*np.exp(-((Rr-R)/rmin)**2); B/=B.max()

cmapV=LinearSegmentedColormap.from_list('V',[(0,'#140F0B'),(0.35,'#7A3D22'),(0.62,RUST),(0.85,YLW),(1,'#FFF4CC')])
cmapB=LinearSegmentedColormap.from_list('B',[(0,'#0C1020'),(0.40,'#1E3A78'),(0.70,BLUE),(0.90,'#8FB6FF'),(1,'#E6F0FF')])

fig,axs=plt.subplots(1,2,figsize=(13.8,7.4)); fig.patch.set_facecolor(EARTHBG)
ext=[-L,L,-L,L]
for ax,F,cm,tc,title,sub in [
    (axs[0],V,cmapV,YLW,'NODE VOLTAGE  $V$','capacitive / E-DOF  —  charge core $\\times$ Compton standing wave  ($\\lambda_C/2=\\pi\\,\\ell_{node}$ rings)'),
    (axs[1],B,cmapB,BLUE,'MAGNETIC DENSITY  $|B|$','inductive / B-DOF  —  unknot current-loop moment at $R=\\varphi/2\\,\\ell_{node}$')]:
    ax.set_facecolor(EARTHBG)
    ax.imshow(F,origin='lower',extent=ext,cmap=cm,interpolation='bilinear')
    for g in np.arange(-7,7.01,A):                       # rigid lattice, pitch = ell_node
        ax.axvline(g,color='white',lw=0.3,alpha=0.06); ax.axhline(g,color='white',lw=0.3,alpha=0.06)
    th=np.linspace(0,2*np.pi,300)
    ax.plot((R+rmin)*np.cos(th),(R+rmin)*np.sin(th),color=tc,lw=0.8,alpha=0.55)   # torus outer
    ax.plot((R-rmin)*np.cos(th),(R-rmin)*np.sin(th),color=tc,lw=0.8,alpha=0.55)   # torus inner
    ax.plot(R*np.cos(th),R*np.sin(th),color='white',lw=1.0,alpha=0.7,ls=(0,(4,2)))# unknot loop @ R
    ax.set_xlim(-L,L); ax.set_ylim(-L,L); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title,color='#EDE6D6',fontsize=15.5,fontweight='bold',pad=12)
    ax.text(0.5,-0.05,sub,transform=ax.transAxes,ha='center',va='top',color='#B9AE92',fontsize=9)
    for s in ax.spines.values(): s.set_color('#3A3320')
# scale bar = 1 ell_node, and Compton ring marker on the V panel
axs[0].plot([-6.6,-5.6],[-6.9,-6.9],color='#EDE6D6',lw=2.2); axs[0].text(-6.1,-6.45,'$1\\,\\ell_{node}$',color='#EDE6D6',ha='center',fontsize=8.5)
axs[0].annotate('',xy=(LAMC/2,0),xytext=(0,0),arrowprops=dict(arrowstyle='<->',color='#EDE6D6',lw=1.0,alpha=0.8))
axs[0].text(LAMC/4,0.32,'$\\lambda_C/2=\\pi\\,\\ell_{node}$',color='#EDE6D6',ha='center',fontsize=8,alpha=0.9)
fig.text(0.5,0.022,'Electron near-field on the rigid K4 lattice (pitch $\\ell_{node}=\\hbar/m_ec$).  Vacuum-native ratios: '
         '$R{=}\\varphi/2,\\ r{=}(\\varphi{-}1)/2,\\ R\\!\\cdot\\! r{=}1/4,\\ \\lambda_C{=}2\\pi\\,\\ell_{node}$  (schematic field forms)',
         ha='center',color='#9CC0FF',fontsize=10)
plt.subplots_adjust(left=0.012,right=0.988,top=0.92,bottom=0.115,wspace=0.04)
plt.savefig('/tmp/electron_fields2.png',dpi=150,facecolor=EARTHBG); print('saved; R=%.4f r=%.4f lamC=%.4f'%(R,rmin,LAMC))
