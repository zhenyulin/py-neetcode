#
# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/
#


def generate_parentheses(n: int) -> list[str]:
    """1) Backtracking.

    we can set up counters for left, right parentheses
    explore adding "(" or ")" on the right condition recursively
    adding result to 'res' until condition met

    time complexity: (3^2N), space complexity: (N^2)
    * N + (N-1) + ... + 1
    """
    res = []

    def add(left, right, s):
        if left == right == 0:
            res.append(s)

        if left > 0:
            add(left - 1, right, s + "(")

        if right > left:
            add(left, right - 1, s + ")")

    add(n, n, "")

    return res
