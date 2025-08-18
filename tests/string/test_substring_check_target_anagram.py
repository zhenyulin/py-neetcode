from tests.benchmark import benchmark_implementations

from rust.string import check_inclusion as check_inclusion_rust
from src.string.substring_check_target_anagram import check_inclusion


def test_check_inclusion():
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("abc", "cccccbabbbaaaa") is True
    assert check_inclusion("a", "ab") is True


IMPLEMENTATIONS = {
    "py": check_inclusion,
    "rs": check_inclusion_rust,
}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark_check_inclusion(benchmark, implementation):
    """Benchmark the check_inclusion implementations."""
    data = ("ab", "eidbaooo")
    benchmark(implementation, *data)
