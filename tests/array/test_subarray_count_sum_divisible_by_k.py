from tests.benchmark import benchmark_implementations

from rust.array import subarray_div_by_k as rust_subarray_div_by_k
from src.array.subarray_count_sum_divisible_by_k import subarray_div_by_k


def test_subarray_div_by_k():
    assert subarray_div_by_k([4, 5, 0, -2, -3, 1], 5) == 7
    assert subarray_div_by_k([5], 9) == 0


@benchmark_implementations({"py": subarray_div_by_k, "rs": rust_subarray_div_by_k})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [4, 5, 0, -2, -3, 1], 5) == 7
