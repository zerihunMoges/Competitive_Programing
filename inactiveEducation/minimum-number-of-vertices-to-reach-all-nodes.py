class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        for edge in edges:
            start, end = edge
            indegree[end] += 1
            indegree[start] += 0
        return [i for i in indegree if indegree[i] == 0]
    

    #### unionset approach inefficent 
#         root = [i for i in range(n)]

#         def find(node):
 
#             if node == root[node]:
#                 return node
            
#             root[node] = find(root[node])
#             return root[node]
        
#         for edge in edges:
#             start, end = edge
#             root[end] = find(start)
            
#         roots = set()
        
#         for i in root:
#             roots.add(find(i))
            
#         return list(roots)
