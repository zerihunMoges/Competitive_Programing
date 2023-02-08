class Solution:
    def path(self, node, adj, visited):
        
        visited.add(node)
        nodes = deque([node])
        p = []
        while nodes:
        
            cur = nodes.popleft()
            p.append(cur)
            for neig in adj[cur]:
                if neig not in visited:
                    visited.add(neig)
                    nodes.append(neig)
            
        return p
    
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        
        adj = defaultdict(list)
        
        for left, right in adjacentPairs:
            adj[left].append(right)
            adj[right].append(left)
            
        for left, right in adjacentPairs:
            if len(adj[left]) <= 1:
                return self.path(left, adj , set())
            if len(adj[right]) <= 1:
                return self.path(right, adj , set())