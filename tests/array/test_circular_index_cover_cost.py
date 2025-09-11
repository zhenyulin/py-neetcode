from tests.benchmark import benchmark_implementations

from rust.array import can_complete_circuit as rust_can_complete_circuit
from src.array.circular_index_cover_cost import can_complete_circuit


def test_can_complete_circuit():
    """Test cases for can_complete_circuit function."""
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1


@benchmark_implementations({"py": can_complete_circuit, "rs": rust_can_complete_circuit})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
