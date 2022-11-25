# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        cur = preorder[0]
        root = TreeNode(cur)        
        idx = inorder.index(cur)
        right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.left = left
        root.right = right
        
        return root
        