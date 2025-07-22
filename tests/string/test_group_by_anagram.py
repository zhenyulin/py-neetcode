from pytest_unordered import unordered

from src.string.group_by_anagram import group_anagrams


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
