"""Photon -> electron on the substrate (pair-production view).
Faithful to canonical clm-i4p11y "Electron = Photon + TIR Confinement":
photon builds to V_yield -> Axiom-4 saturation Gamma->-1 self-TIR mirror ->
trapped standing wave knots into the (2,3) soliton. Qualitative schematic
(no engine-validated trajectory exists yet -- clm-i4p11y, solidity 0.45)."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt

EARTHBG='#1E1813'; EARTH='#8F8367'; BLUE='#2E72FF'; BLUELT='#9CC0FF'
YLW='#FFD21E'; YLWLT='#FFE886'; RUST='#C96B3A'
np.random.seed(3)

def base_lattice(ax):
    g=np.arange(-4.4,4.41,0.62)
    GX,GY=np.meshgrid(g,g)
    ax.scatter(GX,GY,s=5,c=EARTH,alpha=0.30,linewidths=0)

def dense_region(ax,cx=1.4,sat=0.0):
    # high node DENSITY anvil (finer packing + brighter as saturation rises)
    g=np.arange(-1.5,1.51,0.30)
    GX,GY=np.meshgrid(g+cx,g)
    rr=np.hypot(GX-cx,GY)
    m=rr<1.45
    col=np.array([0.18+0.5*sat,0.5+0.3*sat,0.56+0.44*sat])
    ax.scatter(GX[m],GY[m],s=9+10*sat,c=[col],alpha=0.5+0.4*sat,linewidths=0)

def trefoil(ax,cx,cy,sc,col,lw,al=1.0):
    t=np.linspace(0,2*np.pi,240)
    kx=cx+sc*(np.sin(t)+2*np.sin(2*t)); ky=cy+sc*(np.cos(t)-2*np.cos(2*t))
    ax.plot(kx,ky,color=col,lw=lw,solid_capstyle='round',alpha=al)

def wavetrain(ax,x0,x1,amp,col,al=0.9):
    xs=np.linspace(x0,x1,400); ys=np.linspace(-1.4,1.4,80)
    XX,YY=np.meshgrid(xs,ys)
    env=np.exp(-((YY)/1.1)**2)
    F=env*np.cos(2*np.pi*XX/0.95)*amp
    ax.imshow(F,origin='lower',extent=[x0,x1,-1.6,1.6],cmap='RdBu_r',
              vmin=-1,vmax=1,alpha=al,aspect='auto',zorder=1)

fig,axs=plt.subplots(1,4,figsize=(17.5,5.2)); fig.patch.set_facecolor(EARTHBG)
titles=['1 — PHOTON IN','2 — RESONANT BUILD-UP','3 — $\\Gamma\\!\\to\\!-1$ SELF-TIR','4 — ELECTRON']
subs=['transverse wave at $c$ meets a\nhigh-density node region',
      'amplitude builds toward $V_{yield}$\n(Axiom-4 saturation onset)',
      '$\\varepsilon_{eff}\\!\\to\\!0,\\ Z\\!\\to\\!0$: saturation boundary\nbecomes a TIR mirror, reflecting inward',
      'trapped standing wave knots into\nthe $(2,3)$ soliton — rest mass']
for i,(ax,ti,su) in enumerate(zip(axs,titles,subs)):
    ax.set_facecolor(EARTHBG); base_lattice(ax)
    if i==0:
        dense_region(ax,sat=0.0); wavetrain(ax,-4.4,-0.7,0.9,BLUE)
        ax.annotate('',xy=(-0.2,0),xytext=(-1.0,0),arrowprops=dict(arrowstyle='-|>',color=BLUELT,lw=2))
    elif i==1:
        dense_region(ax,sat=0.45); wavetrain(ax,-0.2,2.9,1.0,BLUE,al=0.95)
        ax.text(1.4,1.85,'$\\to V_{yield}$',color=YLWLT,ha='center',fontsize=11)
    elif i==2:
        dense_region(ax,sat=0.8)
        th=np.linspace(0,2*np.pi,200)
        ax.plot(1.4+1.35*np.cos(th),1.35*np.sin(th),color=RUST,lw=2.4,alpha=0.9)      # TIR boundary
        ax.plot(1.4+1.5*np.cos(th),1.5*np.sin(th),color=RUST,lw=0.8,alpha=0.4,ls=(0,(3,3)))
        for a in np.linspace(0,2*np.pi,10,endpoint=False):                            # inward reflection
            ax.annotate('',xy=(1.4+0.85*np.cos(a),0.85*np.sin(a)),xytext=(1.4+1.45*np.cos(a),1.45*np.sin(a)),
                        arrowprops=dict(arrowstyle='-|>',color=BLUELT,lw=1.3,alpha=0.8))
        ax.text(1.4,1.92,'$\\Gamma\\to-1$',color=RUST,ha='center',fontsize=12,fontweight='bold')
    else:
        dense_region(ax,sat=0.85)
        th=np.linspace(0,2*np.pi,200)
        ax.plot(1.4+1.15*np.cos(th),1.15*np.sin(th),color=BLUE,lw=2.0,alpha=0.55)      # |omega| ring
        ax.plot(1.4+0.62*np.cos(th),0.62*np.sin(th),color=BLUE,lw=1.0,alpha=0.45)
        trefoil(ax,1.4,0,0.34,YLW,5.0,0.45); trefoil(ax,1.4,0,0.34,YLW,2.8); trefoil(ax,1.4,0,0.34,YLWLT,0.9)
    ax.set_xlim(-4.6,4.6); ax.set_ylim(-2.7,2.7); ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect('equal')
    ax.set_title(ti,color='#EDE6D6',fontsize=13,fontweight='bold',pad=8)
    ax.text(0.5,-0.10,su,transform=ax.transAxes,ha='center',va='top',color='#B9AE92',fontsize=8.6)
    for s in ax.spines.values(): s.set_color('#3A3320')
    if i<3: ax.annotate('',xy=(1.06,0.5),xytext=(0.99,0.5),xycoords='axes fraction',
                        arrowprops=dict(arrowstyle='-|>',color='#EDE6D6',lw=2.2))
fig.suptitle('PHOTON $\\to$ ELECTRON on the substrate  —  "Electron = Photon + TIR Confinement"  (canonical qualitative mechanism, clm-i4p11y; not engine-validated)',
             color='#9CC0FF',fontsize=12,y=0.045)
plt.subplots_adjust(left=0.008,right=0.992,top=0.88,bottom=0.16,wspace=0.05)
plt.savefig('/tmp/photon_to_electron.png',dpi=150,facecolor=EARTHBG); print('rendered')
