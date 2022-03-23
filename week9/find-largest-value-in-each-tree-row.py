# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        level = deque()
        if root:
            level.append(root)
        
        while level:
            maxx = -float("inf")
            size = len(level)
            for i in range(size):
                node = level.popleft()
                maxx = max(maxx,node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                
            answer.append(maxx)
            
        return answer
            
        
        
        
        
        
