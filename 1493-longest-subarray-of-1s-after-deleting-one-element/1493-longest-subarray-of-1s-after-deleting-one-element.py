class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        pre = [0]
        suf = [0]
        for i in range(len(nums)):
            pre.append( nums[i]*(nums[i]+pre[-1]))
            suf.append( nums[-i-1]*(nums[-i-1]+suf[-1]))
        
        mlen = 0
        for i in range(len(nums)):
            
            mlen = max(mlen, pre[i]+suf[-i-2])
            
        return mlen
                