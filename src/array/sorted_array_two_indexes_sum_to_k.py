#
# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#


def two_sum(numbers: list[int], target: int) -> list[int]:
    """1) Two Pointers.

    we can search from the two ends to the centre

    time complexity: O(N), space complexity: O(1)
    """
    i, j = 0, len(numbers) - 1

    while i < j:
        total = numbers[i] + numbers[j]
        if total < target:
            i += 1
        elif total > target:
            j -= 1
        else:
            return [i + 1, j + 1]

    return []
