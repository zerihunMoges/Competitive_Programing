class Solution:
    def findMinScore(self, path, city, visited):
        visited.add(city)
        min_distance = float('inf')
        for neig, s in path[city]:
            if neig not in visited:
                min_distance = min(min_distance, self.findMinScore(path, neig, visited))
            min_distance = min(min_distance, s)
                
        return min_distance
        
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        
        path = defaultdict(list)
        
        for city1, city2, dis in roads:
            path[city1].append([city2, dis])
            path[city2].append([city1, dis])
            
        visited = set()
        return self.findMinScore(path, 1, visited)
    
