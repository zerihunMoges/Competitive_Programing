# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPathCount(self, cur,cursum, target, sums):
        
        if not cur:
            return 0
        
        cursum += cur.val
        
        
        curcount = sums[cursum-target]
        sums[cursum] += 1
        left_count = self.findPathCount(cur.left,cursum,  target, sums)
        right_count = self.findPathCount(cur.right,cursum, target, sums)
        target_count = left_count+right_count+curcount
        sums[cursum] -= 1
       
        return target_count
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = defaultdict(int)
        
        sums[0] = 1
    

        
        return self.findPathCount(root, 0, targetSum, sums)