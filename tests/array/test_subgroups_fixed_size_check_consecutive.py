from tests.benchmark import benchmark_implementations

from rust.array import can_be_grouped as rust_can_be_grouped
from src.array.subgroups_fixed_size_check_consecutive import can_be_grouped


def test_can_be_grouped():
    assert can_be_grouped([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert can_be_grouped([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3) is True
    assert can_be_grouped([1, 2, 3, 4], 3) is False


@benchmark_implementations({"py": can_be_grouped, "rust": rust_can_be_grouped})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
