#
# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
#


def product_except_self(nums: list[int]) -> list[int]:
    """Accumulate product from the array except self.

    1) Prefix/Suffix Arrays:
    ```python
        # prefix[i] denotes product of nums[:i]
        # suffix[i] denotes product of nums[-i:]
        # suffix[-1-i] denotes product of nums[i:]
        prefix, suffix, N = [1], [1], len(nums)

        for i in range(N):
            prefix.append(prefix[-1]*nums[i])
            suffix.append(suffix[-1]*nums[-1-i])

        # nums[:i] * nums[i+1:]
        return [prefix[i]*suffix[-i-2] for i in range(N)]
    ```
    time complexity: O(N), space complexity: O(N)

    2) Two-Way Iteration:

    as 'prefix[i]', 'suffix[i]' accumulates without index interactions
    and we don't need to know 'prefix[i]' and 'suffix[-i-2]' at the same time
    as long as we multiply them eventually to the result
    we can combine the last step with the prefix, suffix accumulation
    without using arrays to store prefix, suffix

    time complexity: O(N), space complexity: O(N) (O(1) except the result array)
    """
    prefix, suffix, res = 1, 1, [1] * len(nums)

    for i in range(len(nums)):
        # times the part when nums[i], nums[-1-i] have been included
        res[i] *= prefix
        res[-i - 1] *= suffix
        prefix *= nums[i]
        suffix *= nums[-1 - i]

    return res
