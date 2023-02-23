class Solution:
    
        
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        nums = [1] + nums + [1]
        length = len(nums)
        @lru_cache(maxsize = None)
        def getMax( i, j):
            if j - i <= 1: 
                return 0 

            ans = 0
            for k in range(i+1, j):
                ans = max(ans, getMax(i,k) + getMax(k,j) + nums[i] * nums[j] * nums[k])

            return  ans
        
        return getMax(0, length-1)
                