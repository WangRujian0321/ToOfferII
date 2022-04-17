from collections import deque


class RecentCounter:

    def __init__(self):
        self.ping_list = deque()

    def ping(self, t: int) -> int:
        self.ping_list.append(t)
        self.set_ping_list()
        return len(self.ping_list)

    def set_ping_list(self):
        now = self.ping_list[-1]
        pre = now - 3000
        while self.ping_list:
            if self.ping_list[0] >= pre:
                break
            self.ping_list.popleft()

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)