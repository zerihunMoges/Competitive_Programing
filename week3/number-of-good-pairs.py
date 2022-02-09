class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        arry = [0]
        numOfGoodPairs = 0
        for i in range(len(nums)):
            if len(arry) < nums[i] +1:
                arry += [0]*(nums[i]-len(arry)+1)

            arry[nums[i]] += 1
            numOfGoodPairs += arry[nums[i]] -1
        return numOfGoodPairs
