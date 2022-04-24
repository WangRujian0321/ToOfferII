from collections import deque
class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.max_q = deque()

    def max_value(self) -> int:
        if self.max_q:
            return self.max_q[0]
        else:
            return -1


    def push_back(self, value: int) -> None:
        while self.max_q and self.max_q[-1] < value:
            self.max_q.pop()
        self.max_q.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.max_q:
            return -1
        ans = self.queue.popleft()
        if ans == self.max_q[0]:
            self.max_q.popleft()
        return ans
