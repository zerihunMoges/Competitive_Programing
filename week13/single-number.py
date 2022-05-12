class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        o = 0
        
        for i in nums:
            o = o^i
            
        return o
