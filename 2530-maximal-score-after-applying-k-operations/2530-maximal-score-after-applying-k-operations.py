class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        
        score = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k):
            num = heapq.heappop(nums)
            score -= num
            heapq.heappush(nums, -math.ceil(-num/3))
           
        return score
            