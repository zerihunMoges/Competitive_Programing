# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNums(self, node):
        if node == None:
            return []
        if node.left == None and node.right == None:
            return [node.val]
        
        
        left = self.findNums(node.left)
        right = self.findNums(node.right)
        
        answer = []
        
        for num in left+right:
            answer.append(str(node.val)+str(num))
            
        return answer
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        a = self.findNums(root)
        
        return sum(list(map(int, a)))