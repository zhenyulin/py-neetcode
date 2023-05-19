from pytest import raises

from src.structure.heap import Heap


def testHeap():
    heap = Heap()
    heap.push(3)
    heap.push(1)
    heap.push(2)
    heap.push(0)
    assert list(heap) == [0, 1, 2, 3]
    assert heap.peek() == 0
    assert heap.pop() == 0
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3

    with raises(IndexError):
        heap.peek()

    with raises(IndexError):
        heap.pop()
