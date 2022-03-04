# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        reverse = deque()
        traversalOrder = []
        if root:
            nodes.append([root,0])
        level = 0
        
        while nodes or reverse:
            while nodes:
                node = nodes.pop()
                n = node[0]
                level = node[1]
                if level > len(traversalOrder)-1:
                    traversalOrder += [[]]*(level - len(traversalOrder)+1)
                traversalOrder[level] += [n.val]

                if level%2 != 0:
                    if n.right:
                        reverse.append([n.right, level+1])
                    if n.left:
                        reverse.append([n.left, level+1])
                else:
                    if n.left:
                        reverse.append([n.left, level +1])
                    if n.right:
                        reverse.append([n.right, level+1])
            while reverse:
                nodes.append(reverse.popleft())
             
        return traversalOrder
