class FreqStack:

    def __init__(self):
        
        self.op = 0
        self.nums = []
        self.count = defaultdict(int)
        
                    
    def push(self, val: int) -> None:
        self.count[val] += 1
        heapq.heappush(self.nums, [-self.count[val], -self.op, val])
        self.op += 1
     
    def pop(self) -> int:
        count, op, val = heapq.heappop(self.nums)
        self.count[val]-=1
       
        return val
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()