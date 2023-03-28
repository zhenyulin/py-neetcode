#
# problem: https://leetcode.com/problems/two-sum/
#


def twoSum(nums: list[int], target: int) -> list[int]:
    """find the indices of two numbers in `nums` that add up to `target`

    1) Hashmap
    we can use a Hashmap to store `target - n` at each index
    and check if we find the matching n through `nums`

    time complexity: O(N), space complexity: O(N)
    """

    match = {}

    for i, n in enumerate(nums):
        if n in match:
            return [match[n], i]
        match[target - n] = i
