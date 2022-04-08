class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        for i in range(1,len(nums)):
            prefix.append(nums[i-1]*prefix[i-1])
            
        suffix = [1]*len(nums)
        
        for i in range(len(nums)-2, -1,-1):
            suffix[i] = nums[i+1]*suffix[i+1]
        answer = []  
        
        for i in range(len(nums)):
            answer.append(suffix[i]*prefix[i])
            
        return answer
