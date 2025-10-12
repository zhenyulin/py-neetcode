from tests.benchmark import benchmark_implementations

from rust.array import subarray_sum as rust_subarray_sum
from src.array.subarray_count_sum_to_k import subarray_sum


def test_subarray_sum():
    assert subarray_sum([1, 1, 1], 0) == 0
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2


@benchmark_implementations({"py": subarray_sum, "rs": rust_subarray_sum})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 2, 3], 3) == 2
