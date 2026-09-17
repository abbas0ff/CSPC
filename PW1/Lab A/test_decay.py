import pytest
import numpy as np
import decay

def test_simulation_runs():
    result = decay.simulate(1000, 0.4)
    assert len(result) > 0

def test_negative_rate_raises_value_error():
    with pytest.raises(ValueError):
        decay.simulate(1000, -0.1)

def test_average_decay_matches_theory():
    N0 = 1000
    rate = 0.4
    runs = [decay.simulate(N0, rate)[1] for _ in range(50)]
    avg_remaining = np.mean(runs)
    expected = N0 * (1 - rate)
    assert avg_remaining == pytest.approx(expected, rel=0.1)
