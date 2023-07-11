# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        if not root.right and not root.left:
            return 1
        
        return 1+ min(self.minDepth(root.left) if root.left else float('inf') , self.minDepth(root.right) if root.right else float('inf'))
    