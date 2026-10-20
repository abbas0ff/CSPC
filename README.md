 **Author:** Eltun Abbasov


## PW1 --- Lab A: Radioactive Decay & Speed
### What I Built
**`decay.py`**: Python script simulating exponential radioactive decay.
**`speed.py`**: Script benchmarking execution performance.
**`test_decay.py`**: Pytest suite for testing the decay functions.





## PW1 - Lab B 
**Status:** Completeddd
**Environment:** Python 3.11 (Miniconda `cspc` env)
**Tools used:** numpy, matplotlib, snakemake
**Description:** Plotted observed decay data against the analytical law and automated the workflow using Snakemake. and used Ai for understant the some lines of the code because l'm in trouble to memorize some fparts of phyton 





## PW2 --- Lab A: Motion from Tracking Data

**motion from traciking data:**  in this pw l try to measure acceleration velocity and trajectory why accelereation is to noisy because when we take its two derivatives it give us some errors and we lose some part of our number and making the acceleration look very rough
**what l build:** ## PW2 --- Lab A: Motion from Tracking Data

### What I Built
 **analysis.py**: A Python script that processes noisy free-fall position data (freefall.csv), computes velocity and acceleration using np.gradient, and recovers position back using cumulative_trapezoid.
**motion.png**: A plot with 3 stacked panels showing position, velocity, and acceleration over time  for comprension
 **Integration Result:** Integrating the noisy acceleration back recovers the original position within about 1 meter, demonstrating that integration suppresses noise and my results are 
max acceleration -8.6 m\s^2
acceleration std 28.72
max position difference 0.7846
**Generated File:** motion.png (3 stacked panels: position, velocity, acceleration)








---

## PW2 --- Lab B: Optimization in Chemistry

### Requirements & Objectives
The goal of this lab was to understand numerical optimization techniques and apply them to three distinct chemistry problems: fitting first-order reaction kinetics, finding chemical equilibrium composition, and detecting titration equivalence points.

### What I Built & How Problems Were Solved

1. **warmup.py (Benchmarking Optimization Algorithms)**
   - **Task:** Compare Gradient Descent, Newton's method (`scipy.optimize.newton`), and SLSQP (`scipy.optimize.minimize`) on convex $f(x) = (x-3)^2 + 1$ and non-convex $g(x) = x^4 - 3x^2 + x + 5$.
   - **Solution:** Implemented manual gradient descent loops alongside SciPy solvers. Ran trials from $x_0 = 0$ and $x_0 = 2$, and checked second derivatives ($g''$) to differentiate local minima from maxima.

2. **kinetics.py (Reaction Rate Constant Fitting)**
   - **Task:** Determine rate constant $k$ from noisy concentration-time measurements (`kinetics.csv`) following $C(t) = C_0 e^{-kt}$.
   - **Solution:** Extracted $C_0 = C[0]$ and built a total squared error function $\sum (C_{meas} - C_{model})^2$. Minimized error using SLSQP with bounds $[0, 5]$. Fitted $k \approx 0.25$ and saved comparison plot kinetics.png

3. **equilibrium.py (Chemical Equilibrium Extent)**
   - **Task:** Solve $K = \frac{(2x)^2}{(1-x)^2} = 15.6$ for reaction extent $x$ in $\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$.
   - **Solution:** Defined $k_{imbalance}(x) = 0$. Solved via Newton root-finding and SLSQP minimization on $k_{imbalance}(x)^2$. Both methods converged to $x \approx 0.66$ ($\text{HI} \approx 1.33$ mol). Saved composition curves as equilibrium.png

4. **titration.py (Titration Equivalence Point)**
   - **Task:** Locate the equivalence point where pH jumps most steeply from titration.csv.
   - **Solution:** Calculated derivative $\frac{dpH}{dV}$ using np.gradient(pH, V) and found peak index via np.argmax. Identified equivalence volume at $50.0$ mL and plotted side-by-side curves in titration.png

### Challenges & Errors Encountered
- **Newton's Method Trap:** On $g(x)$ starting from $x_0 = 0$, Newton's method converged to $x \approx 0.17$, where $g'' < 0$ (a local maximum instead of a minimum). This highlighted that solving $g'(x) = 0$ does not guarantee a minimum unless verified with $g'' > 0$.
- **Physical Constraints:** Optimization algorithms can occasionally step into non-physical negative values. Applying explicit bounds (e.g. $k \in [0, 5]$ and $x \in [0, 0.999]$) in SLSQP prevent non-physical evaluations.

### Key Learnings
- **Equivalence of Root-Finding and Minimization:** Chemical equilibrium can be framed either as finding roots of $k_{imbalance}(x) = 0$ or minimizing $k_{imbalance}(x)^2 \to 0$; bothe yield identical physical equilibria.
- **Algorithm Selection:** Simple convex functions behave predictably across all methods, but complex multi-peak functions require bounded algorithms like SLSQP or careful initial guessessss