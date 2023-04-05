#
# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
#


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """
    to find unique combinations sum to the target, we can

    1) Backtracking
    iterate through all possible combinations, record the combo when remain is 0

    since candidates are unique, iterating through candidates
    would generate unique combos only

    time complexity: O(N^x), space complexity: O(1)
    """
    # optional, sort the candidates can speed up the process

    res = []

    def dfs(total, combo, i):
        # { the target condition}
        if total == target:
            # remember to create a copy as list is only a pointer
            res.append(combo.copy())

        # { the search condition}
        if i < len(candidates) and total < target:
            combo.append(candidates[i])
            dfs(total + candidates[i], combo, i)
            combo.pop()
            dfs(total, combo, i + 1)

    dfs(0, [], 0)

    return res
