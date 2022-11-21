class Solution:
    def getMaxSubbarray(self, cur, sub_idx, nums, k, memo):
        
        if sub_idx > 3:
            return [0, ""]
        if cur >= len(nums):
            return [float('inf'), ""]
        
        if (cur, sub_idx) in memo:
            return memo[(cur, sub_idx)]
        
        
        best_tot, best_idxs = float('inf'), ''
        select_tot, select_idxs = float('inf'), ''
        
        #select as starting point
        if cur+k < len(nums):
            select_tot, select_idxs = self.getMaxSubbarray(cur+k, sub_idx+1, nums, k, memo)
            select_tot -= nums[cur+k-1] - nums[cur-1] 
            select_idxs = str(cur)+' '+ select_idxs
                        
        skip_tot, skip_idxs = self.getMaxSubbarray(cur+1, sub_idx, nums, k, memo)
        best_tot, best_idxs = min([select_tot, select_idxs], [skip_tot, skip_idxs])
        
        memo[(cur, sub_idx)] = (best_tot, best_idxs)
        return memo[(cur, sub_idx)] 
        
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
    
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]
        nums.append(0)
        memo = defaultdict(tuple)
        tot, idxs = self.getMaxSubbarray(0, 1, nums, k, memo)
      
        
        return idxs.split()
        
        
        
        
        