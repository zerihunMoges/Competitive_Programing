# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dance(root):
            if not root:
                return 0,0
            
            left = dance(root.left)
            right = dance(root.right)
           
        
            lv = left[0]
            rv = right[0]
            myv = root.val
            tv = myv+lv+rv
            return root.val +left[0]+right[0] - 1, abs(left[1])+abs(right[1])+ abs(tv - 1)
        return dance(root)[1]
