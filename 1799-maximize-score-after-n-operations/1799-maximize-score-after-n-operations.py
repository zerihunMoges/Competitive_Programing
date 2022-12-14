class Solution:
    
    def findScore(self,index, nums, used, memo):
        if index > len(nums)//2:
            return 0
        if (index, used) in memo:
            return memo[(index, used)]
        
        best = 0
        for cur in range(len(nums)):
            
            if not (used & 1<<cur):
                for other in range(len(nums)):
                    if not (used & 1<<other) and other != cur:
                        best = max(index*math.gcd(nums[cur], nums[other])+self.findScore(index+1, nums, (used | 1<<other)| 1<<cur , memo), best)
               
        memo[(index, used)] = best
        return best
    
    def maxScore(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        return self.findScore(1, nums, 0, memo)