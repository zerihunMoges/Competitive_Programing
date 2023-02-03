# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = defaultdict(list)
        
        
        def trav(node, i, j):
            if not node:
                return
            
            d[(i, j)].append(node.val)
            
            
            trav(node.left, i-1, j+1)
            trav(node.right, i+1, j+1)
        trav(root, 0,0)
        
        width = min(d, key=lambda x: x[0])[0]
        maxwidth = max(d, key=lambda x: x[0])[0]
        depth = max(d, key=lambda x: x[1])[1]
    
        ans = [[] for _ in range(width,maxwidth+1)]
     
        
        for i in range(width, maxwidth+1):
            for j in range(depth+1):
                ans[i-width]+=sorted(d[(i,j)])
                
        return ans