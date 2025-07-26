from os import getenv


class ListNode:
    def __init__(self, val=0, next=None):  # noqa: A002
        self.val = val
        self.next = next


def to_linked_list(nums: list) -> ListNode | None:
    node = res = ListNode()

    for n in nums:
        node.next = ListNode(n)
        node = node.next

    return res.next


def to_list(node: ListNode | None) -> list:
    res = []

    while node:
        res.append(node.val)
        node = node.next

    return res


def use_list_in_test(func):
    return (
        lambda *args: to_list(func(*[to_linked_list(arg) for arg in args]))
        if getenv("ENV_ID", "").upper() == "TEST"
        else func
    )
