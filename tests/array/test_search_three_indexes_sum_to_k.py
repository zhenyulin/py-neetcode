from tests.benchmark import benchmark_implementations

from rust.array import three_sum as rust_three_sum
from src.array.search_three_indexes_sum_to_k import three_sum


def normalise(result):
    return sorted(sorted(triple) for triple in result)


def test_three_sum():
    assert normalise(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert normalise(three_sum([0, 1, 1])) == []
    assert normalise(three_sum([0, 0, 0])) == [[0, 0, 0]]


@benchmark_implementations({"py": three_sum, "rust": rust_three_sum})
def test_benchmark(benchmark, implementation):
    assert normalise(benchmark(implementation, [-1, 0, 1, 2, -1, -4])) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]
