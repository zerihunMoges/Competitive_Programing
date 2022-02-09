class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        difference = 0
        value = True
        for i in range(len(l)):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort()
            print(subarray)
            difference = subarray[1]-subarray[0]
            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j-1] != difference:
                    value = False
                    break

            answer.append(value)
            value = True
    
        return answer
