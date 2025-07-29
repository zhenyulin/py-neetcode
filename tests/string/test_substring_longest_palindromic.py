import pytest

from rust.string import longest_palindrome as longest_palindrome_rust
from src.string.substring_longest_palindromic import longest_palindrome


def test_longest_palindrome():
    assert longest_palindrome("babad") == "bab"
    assert longest_palindrome("adcba") == "a"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("aabbcc") == "aa"


def test_longest_palindrome_rust():
    assert longest_palindrome_rust("babad") == "bab"
    assert longest_palindrome_rust("adcba") == "a"
    assert longest_palindrome_rust("cbbd") == "bb"
    assert longest_palindrome_rust("aabbcc") == "aa"


IMPLEMENTATIONS = {
    "py": longest_palindrome,
    "rs": longest_palindrome_rust,
}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
@pytest.mark.parametrize("multiplier", [100, 1000], ids=lambda m: f"{m}x")
def test_longest_palindrome_benchmark(benchmark, implementation, multiplier):
    benchmark.group = multiplier
    benchmark(implementation, "aabbcc" * multiplier)
