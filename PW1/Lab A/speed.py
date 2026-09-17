import time
import decay

N0 = 200000
rate = 0.4

t0 = time.perf_counter()
decay.simulate_loop(N0, rate)
t_loop = time.perf_counter() - t0

t0 = time.perf_counter()
decay.simulate(N0, rate)
t_numpy = time.perf_counter() - t0

speedup = t_loop / t_numpy if t_numpy > 0 else 0

print(f"loop  : {t_loop:.4f} s")
print(f"numpy : {t_numpy:.4f} s")
print(f"speed-up: {speedup:.1f} x faster")
