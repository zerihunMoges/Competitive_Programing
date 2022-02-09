class RecentCounter:

    def __init__(self):
        self.counter = []
        

    def ping(self, t: int) -> int:
        self.counter.append(t)

        for i in range(len(self.counter)):
            if self.counter[0] < self.counter[-1] - 3000:
                self.counter.pop(0)
            else:
                return len(self.counter)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
