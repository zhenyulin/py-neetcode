from tests.benchmark import benchmark_implementations

from rust.array import longest_sum_within_k as rust_longest_sum_within_k
from src.array.subarray_longest_sum_within_k import longest_sum_within_k


def test_longest_sum_within_k():
    assert longest_sum_within_k([1, 2, 1, 0, 1, 1, 0], 4) == 5


@benchmark_implementations({"py": longest_sum_within_k, "rs": rust_longest_sum_within_k})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 2, 1, 0, 1, 1, 0], 4) == 5
