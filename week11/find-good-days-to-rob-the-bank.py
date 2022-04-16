class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        right = [0]*len(security)
        left = [0]*len(security)
        
        count = 0
        for i in range(len(security)-2, -1, -1):
            if security[i] <= security[i+1]:
                right[i] += right[i+1]+1
            else: 
                right[i] = 0
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                left[i] += left[i-1]+1
            else: 
                left[i] = 0
        result = []    
        for i in range(len(security)):
            if right[i] >= time and left[i] >= time:
                result.append(i)
        return result
