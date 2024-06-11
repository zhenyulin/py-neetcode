#
# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
#
from typing import Optional

from .list_node import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    """1) Fast, Slow Pointers.

    time complexity: O(N), space complexity: O(1)
    """
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
