class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        i = 1
        fre = 1
        highestFre = 1
        while i < len(nums):
            if k - (nums[i]-nums[i-1])*fre >= 0:
                k -= (nums[i]-nums[i-1])*fre
                fre +=1
                highestFre = fre if fre > highestFre else highestFre
                i+=1


            elif fre != 1 :
                k += (nums[i-1]-nums[j]) 
                fre-=1
                j+=1
            else:
                j+=1
                i+=1
        return highestFre
