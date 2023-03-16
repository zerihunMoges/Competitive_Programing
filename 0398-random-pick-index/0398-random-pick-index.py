class Solution:

    def __init__(self, nums: List[int]):
        

        self.n = defaultdict(list)
        for i in range(len(nums)):
            self.n[nums[i]].append(i)
            
            
            
    def pick(self, target: int) -> int:
        
        return self.n[target][random.randint(0, len(self.n[target])-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)