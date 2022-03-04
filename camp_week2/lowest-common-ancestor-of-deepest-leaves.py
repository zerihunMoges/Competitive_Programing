# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
 
        def lowest(node):
            
            if not node:
                return 0, None
            
            if not node.left and not node.right:
                return 1, node
            
            
            left = lowest(node.left)
            right = lowest(node.right)
                
            if left[0] == right[0]:
                return 1+left[0], node
               
            return (1+left[0], left[1]) if left[0] > right[0] else (right[0]+1 , right[1])
        
        
        
        return lowest(root)[1] 
        
