class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            
        count = defaultdict(int)
        for i in range(len(nums)):
            while heap and count[heap[0]] >= 2:
                heapq.heappop(heap)
                
            if heap:   
                n = heapq.heappop(heap)
                count[n] += 1
                nums[i] = n
            else:
                return i
            
        return len(nums)
        
            