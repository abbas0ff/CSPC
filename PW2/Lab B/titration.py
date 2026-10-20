"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(pH, V)
idx_max = np.argmax(slope)
eq_volume = V[idx_max]

print(f"Equivalence point volume: {eq_volume:.2f} mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(V, pH, label='pH')
ax1.axvline(eq_volume, color='red', linestyle='--', label=f'Eq point ({eq_volume:.1f} mL)')
ax1.set_xlabel('Volume of Base (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titration Curve')
ax1.grid(True)
ax1.legend()
ax2.plot(V, slope, color='green', label='dpH / dV')
ax2.axvline(eq_volume, color='red', linestyle='--', label='Peak slope')
ax2.set_xlabel('Volume of Base (mL)')
ax2.set_ylabel('dpH / dV')
ax2.set_title('Slope (Derivative)')
ax2.grid(True)
ax2.legend()
plt.tight_layout()
plt.savefig('titration.png')