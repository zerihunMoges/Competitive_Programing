class Solution:
    def subsets(self, nums: List[int], idx = 0) -> List[List[int]]:
        if idx >= len(nums):
            return [[]]
        
        
        subset = self.subsets(nums, idx+1)
        new_subsets = []
        for sub in subset:
            new_subsets.append([nums[idx]]+sub)
            new_subsets.append(sub)
            
        return new_subsets
        
        
        