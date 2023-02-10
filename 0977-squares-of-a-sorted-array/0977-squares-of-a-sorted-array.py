class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        j = 0 
        i = len(nums)-1
        answer = []
        while j<=i:
            numi = pow(nums[i],2)
            numj = pow(nums[j],2)
            if numi > numj:
                answer.append(numi)
                i -= 1
            elif numj >= numi:
                answer.append(numj)
                j+=1
                
        answer.reverse()
        return answer
                