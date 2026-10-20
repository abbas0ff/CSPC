## PW1 - Lab B 
- **Author:** Eltun Abbasov
- **Status:** Completeddd
- **Environment:** Python 3.11 (Miniconda `cspc` env)
- **Tools used:** numpy, matplotlib, snakemake
- **Description:** Plotted observed decay data against the analytical law and automated the workflow using Snakemake. and used Ai for understant the some lines of the code because l'm in trouble to memorize some fparts of phyton 





## PW2 --- Lab A: Motion from Tracking Data

- **motion from traciking data:**  in this pw l try to measure acceleration velocity and trajectory why accelereation is to noisy because when we take its two derivatives it give us some errors and we lose some part of our number and making the acceleration look very rough
- **what l build:** ## PW2 --- Lab A: Motion from Tracking Data

### What I Built
- **analysis.py**: A Python script that processes noisy free-fall position data (freefall.csv), computes velocity and acceleration using np.gradient, and recovers position back using cumulative_trapezoid.
- **motion.png**: A plot with 3 stacked panels showing position, velocity, and acceleration over time  for comprension
- **Integration Result:** Integrating the noisy acceleration back recovers the original position within about 1 meter, demonstrating that integration suppresses noise and my results are 
max acceleration -8.6 m\s^2
acceleration std 28.72
max position difference 0.7846
- **Generated File:** motion.png (3 stacked panels: position, velocity, acceleration)