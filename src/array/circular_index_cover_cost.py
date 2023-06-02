#
# 134. Gas Station
# https://leetcode.com/problems/gas-station/
#


def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    """
    1) Greedy

    Try a index and iterate until it is not working
    Record the tried starting index, and try next from the last end

    time complexity: O(N), space complexity: O(1)

    2) Greedy, Two Pointers

    start from indexes [-1, 0],
    if the start index doesn't have enough diff (gas - cost) to reach end,
    then move one step forward to see if the diff can help to reach it,
    otherwise move the end one step forward to see if it can be reached
    when the two indexes converges we are at the target

    time complexity: O(N), space complexity: O(1)
    """

    start, end = len(gas) - 1, 0
    total = gas[start] - cost[start]

    while start >= end:
        # when start can't reach end directly
        # check if it can be reached from previous index
        while total <= 0 and start > end:
            start -= 1
            total += gas[start] - cost[start]

        # when it converges
        # watch out for pseudo converge where total < 0
        if start == end and total >= 0:
            return start

        # when start can reach end
        # check if next index from end can be reached
        total += gas[end] - cost[end]
        end += 1

    return -1
