#
# 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights/
#
from collections import Counter
from heapq import heapify, heappop


def canBeGrouped(hand: list[int], group_size: int) -> bool:
    """
    to check if it is consecutively groupable to the fixed size,
    we can check from the smallest number for consecutive sequences
    remove the found, and iterate forward

    1) Greedy

    a counter to record the counts and a heap to sort the numbers
    pop the smallest starting number, check the consecutives reducing the count

    pop the number when the count is reduced to zero
    if a bigger number is consumed up earlier than smaller numbers
    then it means for the remaining smaller numbers
    it wouldn't be possible to form another consecutive group
    so the popped number needs to be the smallest in the group

    time complexity: O(NlogN), space complexity: O(N)
    * N is the amount of unique numbers in hand
    """
    if len(hand) % group_size:
        return False

    counts = Counter(hand)

    heap = list(counts.keys())
    heapify(heap)

    while heap:
        s = heap[0]
        for n in range(s, s + group_size):
            if n not in counts:
                return False

            counts[n] -= 1

            if counts[n] == 0:
                if n != heap[0]:
                    return False
                heappop(heap)

    return True
