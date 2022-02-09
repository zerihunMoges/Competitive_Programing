class MinStack:

    def __init__(self):
        self.stack = []
        self.minm = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minm = val if self.minm == None or val < self.minm else self.minm 

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minm = None
        for i in self.stack:
            self.minm = i if self.minm == None or i < self.minm else self.minm 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minm
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
