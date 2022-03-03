# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isPal(l):
            i =0
            j = len(l)-1
            while i< j:
                if l[i] != l[j]:
                    return False
                i,j = i+1,j-1
            return True
        
        nodes = deque()
        average = []
        nodes.append([root,0])
        while nodes:
            node = nodes.popleft()
            level = node[1]
            n = node[0]
            if level > len(average)-1:
                average += [[]]*(level-len(average)+1)
                if isPal(average[level-1]) == False:
                    return False

            if n:
                average[level] += [n.val]
            else: 
                average[level] += [None]
            if n:
                nodes.append([n.left,level+1])
                nodes.append([n.right, level+1])
        
        return isPal(average[-1])
