class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        dp = [i for i in nums]
        cur = deque([[dp[0], 0]])
        j = 0
        for i in range(1,len(nums)): 
            while cur and cur[0][1] < i-k:
                cur.popleft()           
            dp[i] += cur[0][0]
            while cur and cur[-1][0] <= dp[i]:
                cur.pop()
            cur.append([dp[i], i])
            
        return dp[-1]
