#
# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
#


def add(a: int, b: int) -> int:
    """In Python, negative int is signed using MSB(Most Significant Bit).

    e.g. -10 -> 0b11111111111111111111111111110110 -> 00110 - 10000 = -01010
    e.g. -2 -> 110+ = 110 - 1000 ~ 6-8 = -2
    e.g. -2 - 3 = -5 -> 110 - 1000 + 101 - 1000 = 1011 - 1000 - 1000 = 011+ (-5)

    e.g. -2 + 3 = 1 -> 110 - 1000 + 011 = 001
    -2 + 3 = 1 using only bit & would lead to an unresolved excessive carry

        (...1)110+
        (...0)011
        (1...)001

    which may lead to overflow and put the programme into infinite loop

    1) Bit Operation & Mask

    For addition involves no negative int, we can use xor(^) to determine 1s
    and find carry over bits using and(&) and shift them(<<1) until carry is 0

    But for negative int, there can be an excessive carry in `while carry:`
    so we will need to use bit mask ignore the carry if it goes beyong 32 bits

    In the case of negative + positive = positive, the result can be overflowed
    from the carry, and since positive int isn't represented in MSB form
    e.g. result, carry for -2 + 3 = 1
        - 101, 100
        - 001, 1000
        - 1001,
        overflowed 1 (0...01) would be -268435455 -(1...11) (MSB: 1,0..01)
    we will need to apply mask to the result as well

    """
    mask = 0xFFFFFFF  # 32 bit mask in hexadecimal
    result, carry = a, b

    while carry & mask:
        result, carry = result ^ carry, (result & carry) << 1

    return result & mask if carry else result
