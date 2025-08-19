from tests.benchmark import benchmark_implementations

from rust.array import missing_number as rust_missing_number
from src.array.consecutive_int_missing import missing_number


def test_missing_number():
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


@benchmark_implementations({"py": missing_number, "rs": rust_missing_number})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [3, 0, 1]) == 2
