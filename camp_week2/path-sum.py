# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def depth(root, total):
            
            if not root:
                return
            total += root.val
            if root.left == None and root.right == None:
                return True if total == targetSum else False
            
            return depth(root.left, total) or depth(root.right, total)
        
        return depth(root, 0)
                
