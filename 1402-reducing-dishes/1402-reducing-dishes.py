class Solution:
    def findMaxS(self, time, index, satisfaction, memo):
        
        if index >= len(satisfaction):
            return 0
        if (index, time) in memo:
            return memo[(index, time)]
        skip = -float('inf')
        if satisfaction[index] < 0:
            skip = self.findMaxS(time, index+1, satisfaction, memo)
        make = time*satisfaction[index] + self.findMaxS(time+1, index+1, satisfaction, memo)
        
        memo[(index, time)] = max(skip, make)
        return memo[(index, time)]
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        
        return self.findMaxS(1, 0, satisfaction, defaultdict(int))