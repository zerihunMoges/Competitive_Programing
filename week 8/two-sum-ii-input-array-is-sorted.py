class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        j = len(numbers)-1
        i=0
        while j>i:
            if numbers[j] + numbers[i] == target:
                return [i+1,j+1]
            elif numbers[j] + numbers[i] < target:
                i += 1
                
            elif numbers[j] + numbers[i] > target:
                j-=1
