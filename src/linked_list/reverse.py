#
# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
#
from typing import Optional

from .list_node import ListNode, use_list_in_test


@use_list_in_test
def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
    last = None

    while node:
        node.next, last, node = last, node, node.next

    return last
