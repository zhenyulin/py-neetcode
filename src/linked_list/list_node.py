from os import getenv
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(nums: list) -> Optional[ListNode]:
    node = res = ListNode()

    for n in nums:
        node.next = ListNode(n)
        node = node.next

    return res.next


def to_list(node: Optional[ListNode]) -> list:
    res = []

    while node:
        res.append(node.val)
        node = node.next

    return res


def use_list_in_test(func):
    return (
        lambda *args: to_list(func(*[to_linked_list(arg) for arg in args]))
        if getenv("TEST_ENV") == "TRUE"
        else func
    )
