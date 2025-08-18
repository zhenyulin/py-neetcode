from tests.benchmark import benchmark_implementations

from rust.string import num_match_subsequences as num_match_subsequences_rust
from src.string.subsequence_count_match_target import num_match_subsequences


def test_num_match_subsequences():
    assert num_match_subsequences("rabbbit", "rabbit") == 3
    assert num_match_subsequences("babgbag", "bag") == 5


IMPLEMENTATIONS = {"py": num_match_subsequences, "rs": num_match_subsequences_rust}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, "rabbbit", "rabbit")
    assert result == 3
