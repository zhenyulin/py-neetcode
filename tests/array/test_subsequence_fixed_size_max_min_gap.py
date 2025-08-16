import pytest

from rust.array import max_min_gap as rust_max_min_gap
from src.array.subsequence_fixed_size_max_min_gap import max_min_gap


def test_max_min_gap():
    assert max_min_gap([2, 3, 5, 9], 3) == 3
    assert max_min_gap([2, 3, 8, 12, 13], 3) == 5
    assert max_min_gap([5, 4, 3, 2, 1, 1000000000], 2) == 999999999


IMPLEMENTATIONS = {"py": max_min_gap, "rs": rust_max_min_gap}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, [2, 3, 5, 9], 3)
    assert result == 3
