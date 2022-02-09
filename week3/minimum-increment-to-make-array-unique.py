class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        frequency = []
        steps = 0
        minrange=-1
        for i in range(len(nums)):
            if nums[i] >= len(frequency):
                frequency += [0]*((nums[i]-len(frequency)+1))
                                  
            frequency[nums[i]] += 1
                                  
        for i in range(len(frequency)):
            if i <= minrange:
                steps += (frequency[i]-1)*(frequency[i])/2 + frequency[i]*(minrange-i+1)
                minrange += frequency[i]
                
            elif frequency[i] >1:
                steps += (frequency[i]-1)*(frequency[i])/2
                minrange = i + frequency[i] - 1
                                  
                                  
        return int(steps)
