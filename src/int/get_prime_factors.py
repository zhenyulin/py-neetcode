#
# get the prime factors of a number
#
#


def primeFactors(n: int) -> list[int]:
    """get the prime factors of a number

    1) Greedy

    we can start with divisor k=2, divide 'n' sufficiently
    then move to the next base 3, ..., until k^2 is larger than 'n'
    which means 'n' is not divisible by k or any larger base

    as non prime factors such as 4, 6, would have been sufficiently divided
    in previous factor 2, 3, so later 'n % k == 0' wouldn't be true for them
    """

    res, k = [], 2

    while k ^ 2 <= n:

        while n % k == 0:
            res.append(k)
            n //= k

        k += 1

    if n > 1:
        res.append(n)

    return res
