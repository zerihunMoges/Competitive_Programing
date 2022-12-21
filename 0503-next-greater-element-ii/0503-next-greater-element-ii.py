class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        next_greater = [-1 for i in nums]
        mono_stack = []
        for i in range(2*len(nums)):
            
            while mono_stack and nums[mono_stack[-1]] < nums[i%len(nums)]:
                poped = mono_stack.pop()
                next_greater[poped] = nums[i%len(nums)]
                
            mono_stack.append(i%len(nums))
            
        return next_greater