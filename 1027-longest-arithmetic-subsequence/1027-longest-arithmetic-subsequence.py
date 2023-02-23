class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        seq = defaultdict(lambda: defaultdict(int))
        
        global_max = 0
        for i in range(len(nums)):
            for j in range(i):
                
                dif = nums[i] - nums[j]
                
                seq[i][dif] = max(seq[i][dif], seq[j][dif]+1)
                global_max = max(seq[i][dif], global_max)
                
                
        return global_max+1