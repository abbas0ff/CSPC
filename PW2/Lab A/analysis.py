"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
- differentiate once -> velocity
- differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
- integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run: python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into array t and y
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t (np.gradient)
#         and acceleration a = derivative of v w.r.t. t (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", np.mean(a))
print("Acceleration std:", np.std(a))

# TODO 3: integrate a back up to recover velocity and position
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

print("Max position difference:", np.max(np.abs(y - y_rec)))

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax1.plot(t, y, color='pink')
ax1.set_ylabel("Position (m)")
ax1.set_title("Motion Analysis")
ax1.grid(True)

ax2.plot(t, v, color='red')
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)

ax3.plot(t, a, color='red')
ax3.axhline(-9.81, color='yellow', linestyle='--')
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Acceleration (m/s²)")
ax3.grid(True)

plt.tight_layout()
plt.savefig('motion.png')