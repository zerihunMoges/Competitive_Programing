class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        neig = defaultdict(list)
        
        for u,v in edges:
            
            if vals[v] >= 0:
                heapq.heappush(neig[u], vals[v])
            if len(neig[u]) > k:
                heapq.heappop(neig[u])
                
            if vals[u] >= 0:
                heapq.heappush(neig[v], vals[u])
            if len(neig[v]) > k:
                heapq.heappop(neig[v])
                
                
        max_star = -float('inf')
        for i in range(len(vals)):
            max_star = max(sum(neig[i])+vals[i], max_star)
            
        return max_star
