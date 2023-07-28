#
# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/
#


def check_inclusion(t: str, s: str) -> bool:
    """
    check whether a substring is anagram with the target

    1)* slide window of len(t) and list Counter to check anagram

    time complexity: O(S), space complexity: O(K)

    1) slide window of len(t) and Greedy Counter to check anagram

    time complexity: O(S), space complexity: O(K)

    2) use sorted substring to check anagram and slide window of len(t)

    time complexity: O(S*T), space complexity: O(T)
    """

    if len(t) > len(s):
        return False

    ct, cs = [0] * 26, [0] * 26

    for i in range(len(t)):
        ct[ord(t[i]) - ord("a")] += 1
        cs[ord(s[i]) - ord("a")] += 1

    for i in range(len(t), len(s)):
        if ct == cs:
            return True

        cs[ord(s[i - len(t)]) - ord("a")] -= 1
        cs[ord(s[i]) - ord("a")] += 1

    return ct == cs
