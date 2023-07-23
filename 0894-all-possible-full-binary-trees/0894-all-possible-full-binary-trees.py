# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def dfs(t):
            if t not in Solution.memo:
                ans = []
                for i in range(t):

                    res = dfs(i)
                    res2 = dfs(t-1-i)
                    for r in res:
                        for j in res2:
                            cur = TreeNode()
                            cur.left = r
                            cur.right = j

                            ans.append(cur)
                Solution.memo[t] = ans
            return Solution.memo[t]
        
        return dfs(n)