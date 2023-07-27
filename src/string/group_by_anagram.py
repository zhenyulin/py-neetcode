#
# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
#

from collections import Counter, defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    for M elements in strs with average length of N, K unique chars

    to group anagrams, we can

    1) use counter tuple as the hashkey
    find the char set first if the char set isn't fixed

    time complexity: O(M*N*K), space complexity: O(M*N + M*K)

    NOTE: tuple equality check consumes O(K) time
    N*K ~ N*logN would depend on the average length N
    """

    """
    def counter_to_tuple(counter: Counter, key_set: set) -> tuple:
        return tuple(counter[key] for key in key_set)

    CHARS = "abcdefghijklmnopqrstuvwxyz"

    counter_tuples = [counter_to_tuple(Counter(s), CHARS) for s in strs]

    groups = defaultdict(list)

    for i, ct in enumerate(counter_tuples):
        groups[ct].append(strs[i])

    return groups.values()
    """

    """

    2) use sorted string as the hashkey

    time complexity: O(M*N*logN), space complexity: O(M*N)
    """

    groups = defaultdict(list)
    for s in strs:
        groups["".join(sorted(s))].append(s)
    return groups.values()
