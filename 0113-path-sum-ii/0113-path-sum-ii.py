# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        if root.left == None and root.right == None and targetSum == root.val:
            return [[root.val]]
        
        new_paths = []
        paths = self.pathSum(root.left, targetSum-root.val) + self.pathSum(root.right, targetSum-root.val)
        
        for path in paths:
            cur = [root.val]
            cur.extend(path)
            new_paths.append(cur)
            
        
        return new_paths