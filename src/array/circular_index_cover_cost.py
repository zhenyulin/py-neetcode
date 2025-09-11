#
# 134. Gas Station
# https://leetcode.com/problems/gas-station/
#


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """1) Greedy.

    Iterating through the path, whenever tank drops below 0 at index i,
    none of the stations from the current start to i can be a valid start,
    so set start = i + 1 and reset tank to 0.
    """
    total = tank = start = 0
    for i, (g, c) in enumerate(zip(gas, cost, strict=False)):
        delta = g - c
        total += delta
        tank += delta
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1
