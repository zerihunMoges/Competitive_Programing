class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        visited = set([0])
        
        keys = deque([0])
        
        while keys:
            
            cur = keys.popleft()
            
            for key in rooms[cur]:
                if key not in visited:
                    visited.add(key)
                    keys.append(key)
                
        return len(visited) == len(rooms)