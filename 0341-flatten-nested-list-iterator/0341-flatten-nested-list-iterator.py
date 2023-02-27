# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):  
        self.nums = deque(nestedList)
        self.nxt = None
    def getNext(self):
        
        if not self.nums:
            return None
        
        cur = self.nums.popleft()
        while not cur.isInteger():
            cur = cur.getList()
          
            while cur:
                self.nums.appendleft(cur.pop())
            if self.nums:
                cur = self.nums.popleft()
            else:
                return None
                     
        return cur.getInteger()
    
    def next(self) -> int:
        return self.nxt
    
    def hasNext(self) -> bool:
        self.nxt = self.getNext()
        return self.nxt != None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())