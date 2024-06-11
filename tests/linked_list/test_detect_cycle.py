from src.linked_list.detect_cycle import hasCycle
from src.linked_list.list_node import to_linked_list


def testHasCycle():
    head = to_linked_list([1, 2, 3, 4, 5])
    assert not hasCycle(head)
    node = head
    while node.next:
        node = node.next
    node.next = head
    assert hasCycle(node)
