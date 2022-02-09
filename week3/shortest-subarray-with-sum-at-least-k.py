class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        sums = 0
        total = []
        subarray = []
        shortest_length = len(nums)+1

        for i in range(len(nums)):
            sums += nums[i]
            total.append(sums)
            if total[i] >= k:
                shortest_length = min(shortest_length, i+1)
                
        for i in range(len(total)):
            while(len(subarray) != 0 and total[i] - total[subarray[0]] >= k):
                shortest_length = min(shortest_length, i - subarray[0])
                subarray.pop(0)
            while(len(subarray) != 0 and total[i] - total[subarray[-1]] <= 0):
                subarray.pop(-1)
            subarray.append(i)

        return shortest_length if shortest_length < len(nums)+1 else -1
