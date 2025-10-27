from tests.benchmark import benchmark_implementations

from rust.array import k_closest as k_closest_rust
from src.array.search_k_elements_closest_to_origin import k_closest


def test_k_closest():
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert k_closest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]


@benchmark_implementations({"py": k_closest, "rust": k_closest_rust})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [[1, 3], [-2, 2], [5, 8], [0, 1]], 2) == [[0, 1], [-2, 2]]
