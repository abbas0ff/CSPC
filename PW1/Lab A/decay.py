import numpy as np

def simulate_loop(N0, rate):
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    N = N0
    history = [N]
    while N > 0:
        decays = sum(1 for _ in range(N) if np.random.rand() < rate)
        N -= decays
        history.append(N)
    return history

def simulate(N0, rate):
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    N = N0
    history = [N]
    while N > 0:
        decays = np.random.binomial(N, rate)
        N -= decays
        history.append(N)
    return history
