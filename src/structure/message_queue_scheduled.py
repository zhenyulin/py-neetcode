"""
[follow-ups]
collision handling:
* if scheduled_at time is collision with the processing time of other messages
try schedule the message at the nearest possible slot and return the actual scheduled time
* how about try defer the scheduled_at to reduce collisions?
"""


from time import time, sleep
from datetime import datetime

from .utils import binary_search_index


class ScheduledMessage:
    def __init__(self, text: str, scheduled_at: datetime):
        self.text = text
        self.scheduled_at = scheduled_at
        self.processing_at = scheduled_at - len(text) * 10


class MessageQueue:
    """
    a message queue with a single thread to process messages
    with the receiver of whom has a sliding window rate limit
    and latency of message being sent needs to be minimised

    message can be scheduled

    1) stack
    stack: [(scheduled_at, processing_at, text)]

    enqueue: O(N) time, dequeue: O(K) time
    """

    def __init__(self, window_size: int = 1000, rate_limit: int = 10):
        self.queue = []
        self.window_size = window_size
        self.rate_limit = rate_limit

    def enqueue(self, m: ScheduledMessage) -> bool:
        """
        1) Binary Search, Window Check, Insert
        binary search the potential insert index of the new message
        check whether before and after windows are within rate limit

        time complexity: O(N), space complexity: O(1)
        """
        index = binary_search_index(
            self.queue, m.scheduled_at, key=lambda x: x[1], ascending=False
        )

        window = 1

        for i in range(
            max(0, index - self.rate_limit),
            min(len(self.queue), index + self.rate_limit + 1),
        ):
            # collision
            if (
                self.queue[i][1] <= m.processing_at < self.queue[i][0]
                or m.processing_at < self.queue[i][1] < m.scheduled_at
            ):
                return False

            # no more capacity
            if abs(m.scheduled_at - self.queue[i][0]) < self.window_size:
                window += 1
                if window > self.rate_limit:
                    return False

        self.queue.insert(index, (m.scheduled_at, m.processing_at, m.text))

        return True

    def _process(self, duration: float) -> None:
        sleep(duration)

    def _send(self, text: str) -> None:
        pass

    def dequeue(self):
        """
        time complexity: O(1)
        """
        while self.queue and time() >= self.queue[-1][1]:
            scheduled_at, processing_at, text = self.queue.pop()
            self._process(scheduled_at - processing_at)
            self._send(text)

    """
    2) heap & stack

    heap: [(processing_at, scheduled_at, message)]
    stack: window [scheduled_at]

    it would be late for the user to know the message can be aborted or delayed

    enqueue: O(logN) time, dequeue: O(K*logN) time
    """
