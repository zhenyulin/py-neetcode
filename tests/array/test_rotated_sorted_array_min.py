import pytest

from rust.array import find_min as rust_find_min
from src.array.rotated_sorted_array_min import find_min


def test_find_min():
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11


IMPLEMENTATIONS = {"py": find_min, "rs": rust_find_min}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, [3, 4, 5, 1, 2])
    assert result == 1
