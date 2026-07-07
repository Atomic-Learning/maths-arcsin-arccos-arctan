#!/usr/bin/env python3
"""
Generate a graph showing the inverse trigonometric functions: arcsin, arccos, and arctan.
Outputs to inverse-trig-functions.png in the same directory.
"""

import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(12, 6), dpi=150)

# Generate x values for arcsin and arccos (domain is [-1, 1])
x_restricted = np.linspace(-1, 1, 500)
arcsin_values = np.arcsin(x_restricted)
arccos_values = np.arccos(x_restricted)

# Generate x values for arctan (domain is all real numbers)
x_full = np.linspace(-3, 3, 500)
arctan_values = np.arctan(x_full)

# Plot the three inverse trigonometric functions
ax.plot(x_restricted, arcsin_values, color='blue', linewidth=2.5, label=r'$\arcsin(x)$', alpha=0.8)
ax.plot(x_restricted, arccos_values, color='green', linewidth=2.5, label=r'$\arccos(x)$', alpha=0.8)
ax.plot(x_full, arctan_values, color='purple', linewidth=2.5, label=r'$\arctan(x)$', alpha=0.8)

# Add horizontal reference lines at key angles
key_angles = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
for angle in key_angles:
    ax.axhline(y=angle, color='gray', linewidth=0.8, linestyle=':', alpha=0.3)

# Add vertical line at x=0
ax.axvline(x=0, color='k', linewidth=0.8, alpha=0.5)

# Grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Set labels
ax.set_xlabel('x', fontsize=12, fontweight='bold')
ax.set_ylabel('Angle (radians)', fontsize=12, fontweight='bold')

# Set x-axis ticks
x_ticks = [-1, -0.5, 0, 0.5, 1]
ax.set_xticks(x_ticks)
ax.set_xticklabels(['-1', '-0.5', '0', '0.5', '1'], fontsize=11)

# Set y-axis ticks with π labels
pi_ticks = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
pi_labels = [r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', 
             r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$']
ax.set_yticks(pi_ticks)
ax.set_yticklabels(pi_labels, fontsize=11)

# Set limits
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-np.pi/2 - 0.5, np.pi + 0.5)

# Add legend
ax.legend(loc='upper left', fontsize=12, framealpha=0.95)

# Add shading to show domain restrictions for arcsin and arccos
ax.axvspan(-1, 1, alpha=0.05, color='gray', label='Domain of arcsin/arccos')

plt.tight_layout()
plt.savefig('inverse-trig-functions.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: inverse-trig-functions.png")
plt.close()
