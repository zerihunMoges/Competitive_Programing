from sortedcontainers import SortedList
class MRUQueue:

    def __init__(self, n: int):
        self.query = 0
        self.queue = SortedList([[self.query, i] for i in range(1, n+1)])

        
    def fetch(self, k: int) -> int:
        self.query += 1
        query, cur = self.queue.pop(k-1)
        self.queue.add([self.query, cur])
        return cur


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)