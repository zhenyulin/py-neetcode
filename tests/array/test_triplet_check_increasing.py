from tests.benchmark import benchmark_implementations

from rust.array import increasing_triplet as rust_increasing_triplet
from src.array.triplet_check_increasing import increasing_triplet


def test_increasing_triplet():
    assert increasing_triplet([1, 2, 3, 4, 5])
    assert not increasing_triplet([5, 4, 3, 2, 1])
    assert increasing_triplet([2, 1, 5, 0, 4, 6])
    assert increasing_triplet([2, 3, 2, 1, 6])


@benchmark_implementations({"py": increasing_triplet, "rust": rust_increasing_triplet})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [2, 1, 5, 0, 4, 6])
