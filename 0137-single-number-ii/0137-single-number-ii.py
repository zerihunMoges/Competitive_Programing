class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        ans = 0
        
        for i in range(32):
            count = 0
            
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                    
                if num >> i & 1 != 0:
                    count += 1
                    
                    
            if count%3 != 0:
            
                ans = ans | (1 << i)
                
        return ans - 2**32 if ans >= 2**31 else ans
            