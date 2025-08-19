from tests.benchmark import benchmark_implementations

from rust.array import max_area as rust_max_area
from src.array.subarray_max_area_containable import max_area


def test_max_area():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([6, 11, 10, 1, 2, 3, 5, 4, 11, 7, 6]) == 77


@benchmark_implementations({"py": max_area, "rust": rust_max_area})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
