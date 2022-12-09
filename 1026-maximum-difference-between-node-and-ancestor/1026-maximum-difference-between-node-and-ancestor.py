# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDiff(self, node, smallest , largest):
        if not node:
            return 0
        
        leftmax = self.maxDiff(node.left, min(smallest, node.val), max(largest, node.val))
        rightmax = self.maxDiff(node.right, min(smallest, node.val), max(largest, node.val))
        
        return max(abs(node.val-smallest), abs(node.val-largest), leftmax, rightmax)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        return self.maxDiff(root, root.val, root.val)