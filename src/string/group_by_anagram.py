#
# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
#
# constraints:
# * 1 <= strs.length <= 104
# * 0 <= strs[i].length <= 100
# * strs[i] consists of lowercase English letters.
#
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """To group anagrams of M strings with average length of N in up to K unique characters.

    1 <= M <= 104, 0 <= N <= 100, K = 26 (lowercase English letters)

    1) use counter array converted to tuple as the hashkey

    - building the hashkey takes O(M*N) time, O(M*26) space
    - dict hashkey lookup takes O(1) time, worst case O(26) time
    - output groups takes O(M*N) space

    time complexity: O(M*N*26), space complexity: O(M*N+M*26)
    """
    # groups = defaultdict(list)
    # for s in strs:
    #     counts = [0] * 26
    #     for c in s:
    #         counts[ord(c) - ord("a")] += 1
    #     groups[tuple(counts)].append(s)
    # return list(groups.values())

    """
    2) use sorted string as the hashkey

    time complexity: O(M*N*logN), space complexity: O(M*N)

    Note: log2(N) <= [log2(100) = 6.64] < 26, it is 50% faster than solution 1 in benchmark.
    """

    groups = defaultdict(list)
    for s in strs:
        groups["".join(sorted(s))].append(s)

    return list(groups.values())
