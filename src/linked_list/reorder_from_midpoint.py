#
# 143. Reorder List
# https://leetcode.com/problems/reorder-list/
#
from .list_node import ListNode


def reorderList(head: ListNode) -> ListNode:
    """to reorder a list merging from both ends

    1) Two Pointers
    we can find the mid point with fast, slow pointers,
    reverse the second half and merge it with the first half

    time complexity: O(N), space complexity: O(1)
    """

    # find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    return head
