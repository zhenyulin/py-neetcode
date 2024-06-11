#
# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#

LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letterCombinations(digits: str) -> list[str]:
    """1) iterate:
    iterate through digits and results then concate string to results.

    time complexity: O(4^N), space complexity: O(4^N)
    * 4^1 + 4^2 + ... + 4^N
    """
    res = list(LETTERS[digits[0]]) if digits else []

    for d in digits[1:]:
        res = [r + c for c in LETTERS[d] for r in res]

    return res
