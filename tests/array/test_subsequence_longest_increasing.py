from tests.benchmark import benchmark_implementations

from rust.array import longest_increasing_subsequence as rust_longest_increasing_subsequence
from src.array.subsequence_longest_increasing import longest_increasing_subsequence


def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1


@benchmark_implementations({"py": longest_increasing_subsequence, "rs": rust_longest_increasing_subsequence})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [10, 9, 2, 5, 3, 7, 101, 18]) == 4
