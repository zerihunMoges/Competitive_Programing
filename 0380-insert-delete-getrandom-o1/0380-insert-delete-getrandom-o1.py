class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indexs = defaultdict(lambda: -1)

    def insert(self, val: int) -> bool:
        if self.indexs[val] == -1:
            self.nums.append(val)
            self.indexs[val] = len(self.nums) -1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if self.indexs[val] != -1:
            self.indexs[self.nums[-1]] = self.indexs[val]
            self.nums[self.indexs[val]], self.nums[-1] = self.nums[-1],self.nums[self.indexs[val]]
            
            self.indexs[val] = -1
            self.nums.pop()
            
            return True
        
        
        return False
    def getRandom(self) -> int:
        
        return self.nums[random.randint(0,len(self.nums)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()