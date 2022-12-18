# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.r = []
        self.index = -1
        visited = set()
        stack = [root]
        while stack:
            
            cur = stack.pop()
            if cur not in visited:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                if cur.left:
                    stack.append(cur.left)
                
                visited.add(cur)
                
            else:
                self.r.append(cur.val)
            
    def next(self) -> int:
        self.index += 1
        return self.r[self.index]
    

    def hasNext(self) -> bool:
        return self.index+1 < len(self.r)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()