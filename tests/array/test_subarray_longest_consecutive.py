from tests.benchmark import benchmark_implementations

from rust.array import longest_consecutive_sequence as rust_longest_consecutive_sequence
from src.array.subarray_longest_consecutive import longest_consecutive_sequence


def test_longest_consecutive_sequence():
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


@benchmark_implementations({"py": longest_consecutive_sequence, "rust": rust_longest_consecutive_sequence})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [100, 4, 200, 1, 3, 2]) == 4
