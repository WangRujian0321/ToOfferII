import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack0 = []
        # 大顶堆
        self.stack1 = []
        # 小顶堆

    def addNum(self, num: int) -> None:
        if len(self.stack0) == len(self.stack1) + 1:
            heapq.heappush(self.stack0, -num)
            temp = heapq.heappop(self.stack0)
            heapq.heappush(self.stack1, -temp)
        else:
            heapq.heappush(self.stack1, num)
            temp = heapq.heappop(self.stack1)
            heapq.heappush(self.stack0, -temp)

    def findMedian(self) -> float:
        if len(self.stack0) > len(self.stack1):
            temp = heapq.heappop(self.stack0)
            heapq.heappush(self.stack0, temp)
            return -temp
        else:
            temp = heapq.heappop(self.stack0)
            heapq.heappush(self.stack0, temp)
            temp0 = heapq.heappop(self.stack1)
            heapq.heappush(self.stack1, temp0)
            return (-temp + temp0) / 2


m = MedianFinder()
m.addNum(1)
m.addNum(2)
