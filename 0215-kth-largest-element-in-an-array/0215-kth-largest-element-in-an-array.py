import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, -1*i)
            
        for i in range(k-1):
            heapq.heappop(heap)
            
        return -1*heap[0]