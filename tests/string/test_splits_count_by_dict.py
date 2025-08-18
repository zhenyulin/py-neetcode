from tests.benchmark import benchmark_implementations

from rust.string import ways_of_decoding as ways_of_decoding_rust
from src.string.splits_count_by_dict import ways_of_decoding


def test_ways_of_decoding():
    assert ways_of_decoding("12") == 2
    assert ways_of_decoding("226") == 3
    assert ways_of_decoding("06") == 0


IMPLEMENTATIONS = {"py": ways_of_decoding, "rs": ways_of_decoding_rust}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, "226")
    assert result == 3
