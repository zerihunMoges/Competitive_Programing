class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = 0
        pos = None
        largestNumber=''
        k = len(nums)
        while k > 0:
            for i in range(k):
                longerNumber = nums[i] if len(str(nums[i])) >= len(str(largest)) else largest
                smallerNumber = nums[i] if len(str(nums[i])) < len(str(largest)) else largest
                if int(str(longerNumber)+str(smallerNumber)) > int(str(smallerNumber)+str(longerNumber)):
                    largest = longerNumber
                    pos = i if longerNumber == nums[i] else pos
                else:
                    largest = smallerNumber
                    pos = i if smallerNumber == nums[i] else pos

            largestNumber += str(largest)
            nums.pop(pos)
            k-=1
            largest = 0
        largestNumber = largestNumber if largestNumber[0] != "0" else str(0)

        return largestNumber 
