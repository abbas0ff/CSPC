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
**what l build:** ## PW2 --- Lab A: Motion from Tracking datas

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







# PW3: Data, Distributions, Testing, and Causation

## Session 1: Data Characterisation (Heart Disease Dataset)

### 1. Data Overview & Shapes
first of all l install `heart.csv` containing medical records for ~300 patients and focused on four continuous variables: `age`, `chol` (cholesterol), `trestbps` (resting blood pressure), and `thalach` (max heart rate) visualised distributions using 15-bin histograms in `heart_distributions.png`.

### 2. Normality Testing
l use  the Shapiro-Wilk test (`scipy.stats.shapiro`) alongside visual check:
- **`age`**: Approximately normal (p > 0.05) symmetry observed around 55 years.
- **`trestbps`**: Roughly normal (p > 0.05) slight right skew at higher pressures.
- **`thalach`**: Approximately normal (p > 0.05) bell-shaped around 150 bpm.
- **`chol`**: **Not normal** (p < 0.05) noticeable right skew with outliers above 300 mg/dL
## Session 2: Statistical Conclusions & Causation

### 3. Comparing Heart Rate (`thalach`) by Disease Status
divided patients into healthy (`target = 0`) and unhealthly which is heart disease (`target = 1`) groups:
- **Healthy mean:** 158.38 \pm 1.50 bpm
- **Disease mean:** 139.26 \pm 1.92 bpm
- **Two-sample t-test:** p = 3.46 \times 10^{-14}

**Conclusion:** The difference is statistically significant patients with heart disease reach a noticeably lower maximum heart rate on averag plotted with SEM error bars in `thalach_by_target.png`

### 4. Age vs Max Heart Rate
Calculated ppearson correlation between `age` and `thalach`:
- Pearson r$: -0.3938 ($p = 1.11 \times 10^{-12})

**Conclusion:** Moderate negative linear relationship as age increases maximum achievable heart rate tends to decrease scatter plot and trend line saved in `age_vs_thalach.png`

### 5. Chemical Exposure Mystery (Causation vs Correlation)
Analyzed `chemicals_cancer.csv` to identify which chemical causes tumors malignancy:
- **Naive Analysis:** Calculating correlations across the full dataset suggested benzene was strongly associated with malignancy (r \approx 0.70), while Cadmium appeared weak (r \approx 0.20)
- **Controlled Analysis:** Controlled for `pollution_index` by filtering to a narrow slice (40\text{th} to 60\text{th} percentile)
- **Result:** After fixing `pollution_index`, Benzene's correlation dropped close to zero, whereas Cadmium showed a strong positive correlation (r \approx 0.65)

**Verdict:** **Cadmium is the true cause of malignancy.** Benzene only looked guilty naively because high-pollution areas had elevated Benzene levels (confounding variable) plotted comparison in `chemical_causation.png`

### Bonus: Category Unpredictability
Calculated Shannon Entropy for the `target` column:
- **Proportions:** ~54% class 1, ~46% class 0
- **Entropy:** $0.9951$ bits (close to maximum $1.0$ bit)
- **Interpretation:** The dataset is nearly balanced making the target category highly unpredictable without feature data