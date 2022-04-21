class MyCalendar:

    def __init__(self):
        self.date = []

    def book(self, start: int, end: int) -> bool:
        for item in self.date:
            if (start < item[1] and end > item[0]):
                return False
        self.date.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)