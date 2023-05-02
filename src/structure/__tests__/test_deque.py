from pytest import raises
from src.structure.deque import Deque


class TestDeque:
    def testLeft(self):
        q = Deque()
        q.append_left(3)
        q.append_left(2)
        q.append_left(1)
        assert q.right() == 3
        assert q.left() == 1
        assert q.pop_left() == 1
        assert q.left() == 2
        assert q.pop_left() == 2
        assert q.left() == 3
        assert q.pop_left() == 3

    def testRight(self):
        q = Deque()
        q.append(2)
        q.append(3)
        q.append(4)
        assert q.right() == 4
        assert q.left() == 2
        q.append_left(1)
        assert q.left() == 1
        assert q.pop() == 4
        assert q.pop() == 3
        assert q.pop() == 2
        assert q.pop() == 1

    def testError(self):
        q = Deque()

        with raises(IndexError):
            q.left()

        with raises(IndexError):
            q.right()

        with raises(IndexError):
            q.pop_left()

        with raises(IndexError):
            q.pop()
