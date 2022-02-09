class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targetArry = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                targetArry.append(i)
            elif nums[i] > target:
                break

        return targetArry
