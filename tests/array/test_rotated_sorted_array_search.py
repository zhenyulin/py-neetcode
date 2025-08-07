import pytest

from rust.array import search as search_rust
from src.array.rotated_sorted_array_search import search


def test_search():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1


IMPLEMENTATIONS = {"py": search, "rs": search_rust}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, [4, 5, 6, 7, 0, 1, 2], 0)
    assert result == 4
