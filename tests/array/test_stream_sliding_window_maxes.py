from tests.benchmark import benchmark_implementations

from rust.array import window_maxes as rust_window_maxes
from src.array.stream_sliding_window_maxes import window_maxes


def test_window_maxes():
    assert window_maxes([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert window_maxes([1, 3, 2, 1, 1], 2) == [3, 3, 2, 1]
    assert window_maxes([1], 1) == [1]


@benchmark_implementations({"py": window_maxes, "rs": rust_window_maxes})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
