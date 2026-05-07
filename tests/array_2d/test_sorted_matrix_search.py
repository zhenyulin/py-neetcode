from rust.array_2d import search as rust_search
from src.array_2d.sorted_matrix_search import search
from tests.benchmark import benchmark_implementations


def test_search():
    assert search(
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ],
        3,
    )
    assert not (
        search(
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            13,
        )
    )


@benchmark_implementations({"py": search, "rust": rust_search})
def test_benchmark(benchmark, implementation):
    assert benchmark(
        implementation,
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ],
        3,
    )
