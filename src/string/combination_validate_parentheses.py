#
# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/
#


def validate_parenthesis(s: str) -> bool:
    """1) Greedy.

    since stars also have their locations, once they are assigned
    left parenthesis, there needs to be a corresponding right parenthesis
    so left, right, star counts wouldn't work here as it doesn't factor
    in the location of stars, stars need to be allocated to left on the move
    so use left_min, left_max to denote all stars to left or right/empty

    time complexity: O(N), space complexity: O(1)
    """
    left_min, left_max = 0, 0

    for c in s:
        if c == "(":
            left_min, left_max = left_min + 1, left_max + 1
        elif c == ")":
            left_min, left_max = left_min - 1, left_max - 1
        else:
            left_min, left_max = left_min - 1, left_max + 1

        if left_max < 0:
            return False

        left_min = max(left_min, 0)  # balance left_min to 0 with stars once it goes negative

    # left_min should have been resolved to 0
    return left_min == 0
