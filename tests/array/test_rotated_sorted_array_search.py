from tests.benchmark import benchmark_implementations

from rust.array import search as search_rust
from src.array.rotated_sorted_array_search import search


def test_search():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1


IMPLEMENTATIONS = {"py": search, "rs": search_rust}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, [4, 5, 6, 7, 0, 1, 2], 0)
    assert result == 4
