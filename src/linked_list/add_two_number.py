#
# problem: https://leetcode.com/problems/add-two-numbers/
#
from .list_node import ListNode, use_list_in_test


@use_list_in_test
def addTwoNumber(l1: ListNode, l2: ListNode) -> ListNode:
    """Add two number with digits stored in reverse order as LinkedList.

    1) we can forward through l1 and l2 with a carry
    """
    res = node = ListNode()
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        carry, v = divmod(carry, 10)
        node.next = ListNode(v)
        node = node.next

    return res.next
