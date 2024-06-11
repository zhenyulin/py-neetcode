#
# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
#


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """*unique combinations are capped at 150.

    to find unique combinations sum to the target, we can

    1) Backtracking
    iterate through all possible combinations, record the combo when remain is 0

    since candidates are unique, iterating through candidates
    would generate unique combos only

    time complexity: O(N^x), space complexity: O(1)

    * x is the average number of elements in the combination
    """
    # optional, sort the candidates can speed up the process

    res, combo = [], []

    def dfs(total, i):
        # { the target condition}
        if total == target:
            # remember to create a copy as list is only a pointer
            res.append([*combo])

        # { the search condition}
        if i < len(candidates) and total < target:
            combo.append(candidates[i])
            dfs(total + candidates[i], i)  # try from i again
            combo.pop()
            dfs(total, i + 1)  # search the next i

    dfs(0, 0)

    return res
