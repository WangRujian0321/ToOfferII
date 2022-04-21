import heapq


class KthLargest:
    def __init__(self, k: int, nums):
        self.n = 0
        self.capture = k
        self.heap = []
        for item in nums:
            self.add(item)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.n += 1
        if self.n > self.capture:
            heapq.heappop(self.heap)
            self.n -= 1
        ans = heapq.heappop(self.heap)
        heapq.heappush(self.heap, ans)
        return ans


a = KthLargest(3, [4, 5, 8, 2])
a.add(3)
a.add(5)