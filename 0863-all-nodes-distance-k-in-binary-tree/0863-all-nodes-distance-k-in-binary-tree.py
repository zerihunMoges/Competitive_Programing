# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict()
        
        start = [root]
        while start:
            cur = start.pop()
            
            if cur.left:
                parent[cur.left.val] = cur
                start.append(cur.left)
            if cur.right:
                parent[cur.right.val] = cur
                start.append(cur.right)
            
        
        nodes = deque([target])
        visited = set()
        level = 0 
        while nodes:
            size = len(nodes)
            if level == k:
                return [i.val for i in nodes]
            for i in range(size):
                cur = nodes.popleft()
                visited.add(cur.val)
         
                
                if cur.left and cur.left.val not in visited:
                    nodes.append(cur.left)
                if cur.right and cur.right.val not in visited:
                    nodes.append(cur.right)
                if cur.val in parent and parent[cur.val].val not in visited:
                    nodes.append(parent[cur.val])
                    
            level += 1
            
    
        return []
            
            
        