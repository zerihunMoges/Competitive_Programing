class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minimum = []
        maximum = []
        length = 0
        left = 0
        for i in range(len(nums)):
            while (maximum and nums[i] > nums[maximum[-1]]) or minimum and nums[i] < nums[minimum[-1]]:
                if nums[i] > nums[maximum[-1]]:
                    maximum.pop()
                else:
                    minimum.pop()
            maximum.append(i)
            minimum.append(i)

            if nums[maximum[0]] - nums[minimum[0]] <= limit:
                length = max(length, i+1 - left)
            else:
                left = min(maximum[0], minimum[0])+1
                minimum.pop(0) if minimum[0] == min(maximum[0], minimum[0]) else maximum.pop(0)

        return length
