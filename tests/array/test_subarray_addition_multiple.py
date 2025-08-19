from tests.benchmark import benchmark_implementations

from rust.array import range_addition as rust_range_addition
from src.array.subarray_addition_multiple import range_addition


def test_range_addition():
    assert range_addition(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]) == [-2, 0, 3, 5, 3]


@benchmark_implementations({"py": range_addition, "rs": rust_range_addition})
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, 5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
    assert result == [-2, 0, 3, 5, 3]
