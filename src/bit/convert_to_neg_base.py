#
# 1017. Convert to Base -2
# https://leetcode.com/problems/convert-to-base-2/
#


def negBase(n: int, base: int = -2) -> str:
    """Negative base.

        n = base*carry + bit

    while for negative base, bit can be negative from divmod
    to turn that into positive int, we will borrow from carry
    """
    if n == 0:
        return "0"

    res = ""

    while n != 0:
        # n = carry*base + bit
        n, bit = divmod(n, base)

        # borrow from carry
        if bit < 0:
            bit -= base  # negative base
            n += 1  # negative carry

        res += str(bit)

    return res[::-1]
