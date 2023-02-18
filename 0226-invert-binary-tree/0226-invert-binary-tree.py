# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertBinaryTree(self, cur):
        if not cur:
            return 
        
        left = cur.left
        right = cur.right
        cur.left = right
        cur.right = left
        
        self.invertBinaryTree(cur.left)
        self.invertBinaryTree(cur.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.invertBinaryTree(root)
        return root