"""
AVE Electroweak Boson Simulator: Torsional vs Transverse Impedance Modes
-------------------------------------------------------------------------
Visualizes how the W and Z bosons are fundamentally the orthogonal phase-polarizations
of the discrete LC Network macroscopic strain fields:
W = Torsional Phase Rotation (Current lag)
Z = Transverse Phase Bending (Voltage lag)
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simulate_electroweak_modes():
    print("==========================================================")
    print(" AVE ELECTROWEAK BOSON MODES (Z/W IMPEDANCE POLARIZATION)")
    print("==========================================================")
    
    os.makedirs('assets/sim_outputs', exist_ok=True)
    
    fig = plt.figure(figsize=(14, 8), facecolor='#0B0F19')
    fig.patch.set_facecolor('#0B0F19')
    
    # -------------------------------------------------------------------------
    # Left Pane: W Boson Mode (Torsional Impedance Twist / Pure Inductive Phase Shift)
    # -------------------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.set_facecolor('#0B0F19')
    ax1.axis('off')
    
    z1 = np.linspace(-3, 3, 60)
    theta1 = np.linspace(0, 2*np.pi, 40)
    Z1, Theta1 = np.meshgrid(z1, theta1)
    R = 1.0
    
    # The W Boson represents a Torsional phase shift in the network geometry
    # (Effectively a pure Inductive L delay winding azimuthally)
    twist_rate = 0.5 
    Theta_twist = Theta1 + twist_rate * Z1
    X1 = R * np.cos(Theta_twist)
    Y1 = R * np.sin(Theta_twist)
    
    ax1.plot_surface(X1, Y1, Z1, color='cyan', alpha=0.3, edgecolor='none')
    
    # Grid demonstrating the geometrical inductive 'flux' lines
    z_lines = np.linspace(-3, 3, 10)
    for zl in z_lines:
        t_l = np.linspace(0, 2*np.pi, 50)
        x_l = R * np.cos(t_l + twist_rate*zl)
        y_l = R * np.sin(t_l + twist_rate*zl)
        ax1.plot(x_l, y_l, zl*np.ones_like(t_l), color='white', alpha=0.2)
        
    for th in np.linspace(0, 2*np.pi, 12, endpoint=False):
        t_line = th + twist_rate*z1
        x_l = R * np.cos(t_line)
        y_l = R * np.sin(t_line)
        ax1.plot(x_l, y_l, z1, color='#00FFFF', linewidth=1.5, alpha=0.9)
        
    ax1.set_box_aspect([1,1,2])
    ax1.set_xlim([-1.5, 1.5])
    ax1.set_ylim([-1.5, 1.5])
    ax1.set_zlim([-3, 3])
    ax1.view_init(elev=15, azim=45)
    
    title_1 = (r"$\mathbf{W^{\pm}}$ Boson: Torsional Phase Rotation" + "\n" +
               r"(Inductive Lattice Shear, $J = \frac{\pi}{2}r^4$)")
    ax1.set_title(title_1, color='white', pad=15, fontsize=14, fontweight='bold')
    
    # -------------------------------------------------------------------------
    # Right Pane: Z Boson Mode (Transverse Impedance Bending / Capacitive Shift)
    # -------------------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.set_facecolor('#0B0F19')
    ax2.axis('off')
    
    z2 = np.linspace(-3, 3, 60)
    theta2 = np.linspace(0, 2*np.pi, 40)
    Z2, Theta2 = np.meshgrid(z2, theta2)
    
    bend_amp = 0.8
    # The Z Boson represents Transverse Transverse bending in the network 
    # (Effectively a Capacitive C charging delay bowing radially)
    bend_profile = bend_amp * np.cos(np.pi * Z2 / 6)
    slope = -bend_amp * (np.pi/6) * np.sin(np.pi * Z2 / 6)
    angle = np.arctan(slope)
    
    X2 = R * np.cos(Theta2) * np.cos(angle) + bend_profile
    Y2 = R * np.sin(Theta2)
    Z2_actual = Z2 - R * np.cos(Theta2) * np.sin(angle)
    
    ax2.plot_surface(X2, Y2, Z2_actual, color='magenta', alpha=0.3, edgecolor='none')
    
    for zl in np.linspace(-3, 3, 10):
        t_l = np.linspace(0, 2*np.pi, 50)
        b_p = bend_amp * np.cos(np.pi * zl / 6)
        s_p = -bend_amp * (np.pi/6) * np.sin(np.pi * zl / 6)
        ang = np.arctan(s_p)
        x_l = R * np.cos(t_l) * np.cos(ang) + b_p
        y_l = R * np.sin(t_l)
        z_l = zl - R * np.cos(t_l) * np.sin(ang)
        ax2.plot(x_l, y_l, z_l, color='white', alpha=0.2)
        
    for th in np.linspace(0, 2*np.pi, 12, endpoint=False):
        b_p = bend_amp * np.cos(np.pi * z2 / 6)
        s_p = -bend_amp * (np.pi/6) * np.sin(np.pi * z2 / 6)
        ang = np.arctan(s_p)
        x_l = R * np.cos(th) * np.cos(ang) + b_p
        y_l = R * np.sin(th) * np.ones_like(z2)
        z_l = z2 - R * np.cos(th) * np.sin(ang)
        if np.cos(th) > 0.5 or np.cos(th) < -0.5:
            ax2.plot(x_l, y_l, z_l, color='#FF00FF', linewidth=2.0, alpha=0.9)
        else:
            ax2.plot(x_l, y_l, z_l, color='white', linewidth=1.0, alpha=0.3)
            
    ax2.set_box_aspect([1,1,2])
    ax2.set_xlim([-1.5, 1.5])
    ax2.set_ylim([-1.5, 1.5])
    ax2.set_zlim([-3, 3])
    ax2.view_init(elev=15, azim=45)
    
    title_2 = (r"$\mathbf{Z^{0}}$ Boson: Transverse Phase Bending" + "\n" +
               r"(Capacitive Lattice Bow, $I = \frac{\pi}{4}r^4$)")
    ax2.set_title(title_2, color='white', pad=15, fontsize=14, fontweight='bold')
    
    # Super-title linking them mathematically
    fig.suptitle(r"The Weak Mixing Angle ($\sin^2\theta_W \equiv 0.25$): Geometry of Impedance Polarization", 
                 color='white', fontsize=18, fontweight='bold', y=0.98)
                 
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    output_path = 'assets/sim_outputs/simulate_weak_boson_modes.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#0B0F19')
    print(f"Successfully saved Topo-Electric W/Z Boson visualization to {output_path}")

if __name__ == '__main__':
    simulate_electroweak_modes()
