from sortedcontainers import SortedList

# class TreeNode:
#     def __init__(self, val, left=None, right=None, idx=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.idx = idx
        
class Solution:
#     def buildBST(self, nums , left, right):
#         if not nums:
#             return 
#         mid = nums[len(nums)//2]
        
#         parent = TreeNode(mid, left + len(nums)//2)
        
#         parent.left = self.buildBST(nums[:len(nums)//2], left, len(nums)//2+1)
#         parent.right = self.buildBST(nums[len(nums)//2+1:], len(nums)//2+1, right)
        
#         return parent
    def reversePairs(self, nums: List[int]) -> int:
        
        
        greater = SortedList([nums[0]])
        pairs = 0
        for i in range(1, len(nums)):
            pairs += i - (greater.bisect_right(nums[i]*2))
            greater.add(nums[i])
            

        return pairs
    
        
        