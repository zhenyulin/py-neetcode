from tests.benchmark import benchmark_implementations

from rust.array import two_sum as rust_two_sum
from src.array.sorted_array_two_indexes_sum_to_k import two_sum


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]


@benchmark_implementations({"py": two_sum, "rs": rust_two_sum})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [2, 7, 11, 15], 9) == [1, 2]
