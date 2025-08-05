import pytest

from rust.string import word_break as word_break_rust
from src.string.splits_count_match_by_dict import word_break


def test_word_break():
    assert word_break("leetcode", ["leet", "code"])
    assert word_break("applepenapple", ["apple", "pen"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert not word_break("etle", ["leet"])


IMPLEMENTATIONS = {"py": word_break, "rs": word_break_rust}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, "applepenapple", ["apple", "pen"])
    assert result
