"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.
data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
def total_error(k):
    return np.sum((C - C0 * np.exp(-k[0] * t))**2)

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fitted = res.x[0]
print(f"Fitted k: {k_fitted:.4f}")

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
t_line = np.linspace(t.min(), t.max(), 100)
C_line = C0 * np.exp(-k_fitted * t_line)

plt.figure()
plt.plot(t, C, 'o', label='Data')
plt.plot(t_line, C_line, '-', label=f'Fit (k={k_fitted:.2f})')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.savefig('kinetics.png')