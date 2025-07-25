from pytest_unordered import unordered

from rust.string import group_anagrams as group_anagrams_rs
from src.string.group_by_anagram import group_anagrams
from src.string.group_by_anagram_c import group_anagrams_26lower


def test_group_anagrams(benchmark):
    """Test cases for grouping anagrams."""
    result = benchmark(group_anagrams, ["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    for g in result:
        assert unordered(g) in expected


def test_group_anagrams_c(benchmark):
    """Test cases for grouping anagrams."""
    result = benchmark(group_anagrams_26lower, ["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    for g in result:
        assert unordered(g) in expected


def test_group_anagrams_rs(benchmark):
    """Test cases for grouping anagrams."""
    result = benchmark(group_anagrams_rs, ["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    for g in result:
        assert unordered(g) in expected
