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

    1) use bytearray converted to bytes as the hashkey

    - building the hashkey takes O(M*N) time, O(M*26) space
    - dict hashkey lookup amortised to O(1) time, worst case O(26) time
    - output groups takes O(M*N) space

    amortised time complexity: O(M*N), space complexity: O(M*N+M*26)

    Note: bytearray and bytes would be slightly faster than list and tuple
    bytearray and bytes use raw bytes (uint8) instead of PyLongObject int + pointers
    """
    # groups = defaultdict(list)
    # for s in strs:
    #     counts = bytearray(26)
    #     for c in s:
    #         counts[ord(c) - 97] += 1  # ord('a') = 97
    #     groups[bytes(counts)].append(s)
    # return list(groups.values())

    """
    2) use sorted string as the hashkey

    amortised time complexity: O(M*N*logN), space complexity: O(M*N)

    Note: although the sorted method is O(N*logN), slower than the counter method
    but join(), sorted() are C-level operations, while the count is looping in python
    in benchmark, the sort approach is 1.5 faster than the count approach, especially for N<=100
    """

    groups = defaultdict(list)
    for s in strs:
        groups["".join(sorted(s))].append(s)
    return list(groups.values())
