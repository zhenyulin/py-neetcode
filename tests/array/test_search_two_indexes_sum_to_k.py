from tests.benchmark import benchmark_implementations

from rust.array import two_sum_k as two_sum_rust
from src.array.search_two_indexes_sum_to_k import two_sum


def test_two_sum():
    # the problem has been constrained to have only one valid answer
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


@benchmark_implementations({"py": two_sum, "rs": two_sum_rust})
def test_benchmark_two_sum(benchmark, implementation):
    assert benchmark(implementation, [2, 7, 11, 15], 9) == [0, 1]
