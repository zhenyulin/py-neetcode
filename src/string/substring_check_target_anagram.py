#
# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/
#


def check_inclusion(t: str, s: str) -> bool:
    """Check whether a substring is anagram with the target.

    1) slide window of len(t) and bytearray Counter to check anagram

    time complexity: O(S), space complexity: O(K)

    2) use sorted substring to check anagram and slide window of len(t)

    time complexity: O(S*T), space complexity: O(T)
    """
    if len(t) > len(s):
        return False

    ct, cs = bytearray(26), bytearray(26)

    for i in range(len(t)):
        ct[ord(t[i]) - 97] += 1
        cs[ord(s[i]) - 97] += 1

    for i in range(len(t), len(s)):
        if ct == cs:
            return True

        cs[ord(s[i]) - 97] += 1
        cs[ord(s[i - len(t)]) - 97] -= 1

    return ct == cs
