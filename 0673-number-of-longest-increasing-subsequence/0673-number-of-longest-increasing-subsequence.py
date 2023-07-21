class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
        length = [1]*len(nums)
        count = defaultdict(lambda: 1)
        simp = defaultdict(int)
        for i in range(len(nums)):
            
            for j in range(i):
                if nums[j] < nums[i]:
                    if 1+length[j] == length[i]:
                        count[i]+=count[j]
                    elif 1+length[j] > length[i]:
                        count[i] = count[j]
                    length[i] = max(length[i], 1+length[j])
            simp[length[i]] += count[i]
        
        
        return simp[max(simp.keys())]