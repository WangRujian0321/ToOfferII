from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self.num = 0
        self.sum = 0


    def next(self, val: int) -> float:
        if self.size == self.num:
            left = self.queue.popleft()
            self.sum = self.sum - left
            self.num -= 1
        self.sum += val
        self.queue.append(val)
        self.num += 1
        return self.sum / self.num



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)