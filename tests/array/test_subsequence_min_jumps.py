from tests.benchmark import benchmark_implementations

from rust.array import min_jump as rust_min_jump
from src.array.subsequence_min_jumps import min_jump


def test_min_jump():
    assert min_jump([2, 3, 1, 1, 4]) == 2
    assert min_jump([2, 3, 0, 1, 4]) == 2


@benchmark_implementations({"py": min_jump, "rs": rust_min_jump})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [2, 3, 1, 1, 4]) == 2
