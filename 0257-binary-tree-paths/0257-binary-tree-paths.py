# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        if not root:
            return []
        
        new_paths = []
        
        paths = self.binaryTreePaths(root.left)
        for path in paths:
            new_paths.append(str(root.val)+'->'+path)
            
        paths = self.binaryTreePaths(root.right)
        for path in paths:
            new_paths.append(str(root.val)+'->'+path)
            
        if new_paths:
            return new_paths
        
        return [str(root.val)]