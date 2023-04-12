#
# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
#


def reverseBits(n: int) -> int:
    """to reverse bits

    1) Bit Iteration
    for each bit, using `n & 1` to take only the last bit
    append that to `res` from the right, and then right shift `n`

    time complexity: O(1), space complexity: O(1)
    """
    res = 0
    for _ in range(32):
        # left shift res and add the last bit of n
        res = (res << 1) + (n & 1)
        # right shift n to next bit
        n = n >> 1
    return res
