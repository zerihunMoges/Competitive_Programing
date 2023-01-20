class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        heap = []
        maxsum = -float('inf')
        for i in range(len(nums)):  
            prev_max = 0
            if heap:
                prev_max = max(prev_max, -heap[0][0])
                
            heapq.heappush(heap, [-(nums[i]+prev_max), i])
            while heap and (i - heap[0][1] >= k or i == len(nums)-1):
                tot, index = heapq.heappop(heap)
                maxsum = max(-tot, maxsum)
                
        return maxsum
                
        
            