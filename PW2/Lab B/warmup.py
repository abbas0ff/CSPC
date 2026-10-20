"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result
print("=== Part 2A: Minimizing f(x) ===")

x_gd = 0.0
lr = 0.1
for _ in range(100):
    x_gd = x_gd - lr * df(x_gd)
print("Gradient Descent:", x_gd)

x_newton = newton(df, 0.0, fprime=d2f)
print("Newton method:", x_newton)

res_slsqp = minimize(f, 0.0, method="SLSQP")
print("SLSQP:", res_slsqp.x[0])

def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
print("\n=== Part 2B: Minimizing g(x) ===")

for x0 in [0.0, 2.0]:
    print(f"\n--- Starting from x0 = {x0} ---")
    
    #  Gradient descent
    x_gd = x0
    lr = 0.01
    for _ in range(200):
        x_gd = x_gd - lr * dg(x_gd)
    print("Gradient Descent:", x_gd)
    
    #  Newton's method
    x_newt = newton(dg, x0, fprime=d2g)
    check = "minimum" if d2g(x_newt) > 0 else "maximum"
    print(f"Newton method: {x_newt:.4f} ({check})")
    
    #  SLSQP
    res_s = minimize(g, x0, method="SLSQP")
    print("SLSQP:", res_s.x[0])