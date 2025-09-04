from tests.benchmark import benchmark_implementations

from rust.array import count_triplets as rust_count_triplets
from src.array.triplet_count_increasing_sum_within_k import count_triplets


def test_count_triplets():
    assert count_triplets([1, 2, 3, 4, 5], 8) == 4


@benchmark_implementations({"py": count_triplets, "rs": rust_count_triplets})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 2, 3, 4, 5], 8) == 4
