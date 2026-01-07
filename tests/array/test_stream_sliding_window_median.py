from tests.benchmark import benchmark_implementations

from rust.array import sliding_window_median as rust_sliding_window_median
from src.array.stream_sliding_window_median import sliding_window_median


def test_sliding_window_median():
    assert sliding_window_median([5, 4, 3, 2, 1, 2, 6, 7, 8], 5) == [
        3.0,
        2.0,
        2.0,
        2.0,
        6.0,
    ]
    assert sliding_window_median([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        1.0,
        -1.0,
        -1.0,
        3.0,
        5.0,
        6.0,
    ]
    assert sliding_window_median([1, 2, 3, 4, 2, 3, 1, 4, 2], 3) == [
        2.0,
        3.0,
        3.0,
        3.0,
        2.0,
        3.0,
        2.0,
    ]


@benchmark_implementations({"py": sliding_window_median, "rs": rust_sliding_window_median})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        1.0,
        -1.0,
        -1.0,
        3.0,
        5.0,
        6.0,
    ]
