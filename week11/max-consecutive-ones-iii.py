class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        j = 0
        i = 0 
        fk = k
        longest = 0
        
        while i < len(nums):
            while fk == 0 and nums[i] == 0:
                 
                if nums[j] == 0:
                    fk += 1
                j+=1
                
            if nums[i] != 1:
                fk -= 1
            i+=1
            longest= max(longest, i-j)
        return longest
