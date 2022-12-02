class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        prefix = [0]
        for i in range(2*len(nums)):
            prefix.append(nums[i%len(nums)] + prefix[-1])
            
        
        
        minswap = float('inf')
        for i in range(len(prefix)-window):
            minswap = min(window - prefix[i+window] + prefix[i], minswap)
            
        return minswap
            
            
                          
            
            
            
            
        