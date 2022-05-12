class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        mis = 0
        for i in nums:
            mis = mis^i
        s = 0   
        
        for i in range(len(nums)+1):
            s = s^i
            
        return mis^s 
