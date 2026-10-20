"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
def k_imbalance(x):
    return (2 * x)**2 / ((a - x) * (b - x)) - K

# TODO 2 (method 1): use scipy.optimize.newton
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize (SLSQP)
def obj(x):
    return k_imbalance(x[0])**2
res = minimize(obj, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]
print(f"Newton extent x: {x_newton:.4f}")
print(f"SLSQP extent x:  {x_slsqp:.4f}")

# TODO 4: report equilibrium amounts and plot
nH2 = a - x_newton
nI2 = b - x_newton
nHI = 2 * x_newton
print(f"Equilibrium amounts: H2 = {nH2:.4f} mol, I2 = {nI2:.4f} mol, HI = {nHI:.4f} mol")
x_vals = np.linspace(0, 0.99, 100)
plt.figure()
plt.plot(x_vals, a - x_vals, label='H2')
plt.plot(x_vals, b - x_vals, '--', label='I2')
plt.plot(x_vals, 2 * x_vals, label='HI')
plt.axvline(x_newton, color='gray', linestyle=':', label=f'Equilibrium (x={x_newton:.2f})')
plt.xlabel('Extent x')
plt.ylabel('Amount (mol)')
plt.legend()
plt.savefig('equilibrium.png')