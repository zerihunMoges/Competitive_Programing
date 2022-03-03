# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = deque()
        average = []
        nodes.append([root,0])
        while nodes:
            node = nodes.popleft()
            level = node[1]
            n = node[0]
            if level > len(average)-1:
                average += [[]]*(level-len(average)+1)
            average[level] += [n.val]
            
            if n.left:
                nodes.append([n.left,level+1])
            if n.right:
                nodes.append([n.right, level+1])
                
        for i in range(len(average)):
            tot = 0
            for j in range(len(average[i])):
                tot += average[i][j]
            average[i] = tot/len(average[i])
            
        return average
        
