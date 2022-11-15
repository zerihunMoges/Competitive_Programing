# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPathCount(self, cur, target):
        
        if not cur:
            return [float('inf')], 0
        
        left_sums, left_count = self.findPathCount(cur.left, target)
        right_sums, right_count = self.findPathCount(cur.right, target)
        target_count = left_count+right_count
        
        sums = left_sums + right_sums
        
        cur_sums = []
        for num in sums:
            
            if num != float('inf'):
                cur_sums.append(num+cur.val)
            
            if num+cur.val == target:
                target_count += 1
                
        if cur.val == target:
                target_count += 1
        
        cur_sums.append(cur.val)
        
        return cur_sums, target_count
            
                
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        sums, count = self.findPathCount(root, targetSum)
       
        return count
        