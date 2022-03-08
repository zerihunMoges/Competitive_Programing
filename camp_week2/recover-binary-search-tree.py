# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        err = [] #2 Nodes
        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
            
            while cur == None and stack:
                cur = stack.pop()
                if err != [] and err[1].val > cur.val:
                    err[0].val, cur.val = cur.val, err[0].val
                    return
                
                elif pre != None and cur.val <= pre.val:
                   
                    err += [pre, cur]
               
                pre = cur
                cur = cur.right
                
        err[0].val, err[1].val = err[1].val, err[0].val
