"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def depth(root):
            
            if not root:
                return 0
            
            if root.children == []:
                return 1
            
            maxx = 0
            for i in root.children:
                maxx = max(maxx, depth(i)+1)
            return maxx
        
        return depth(root)
