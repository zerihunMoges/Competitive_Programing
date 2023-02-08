class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        
        
#         distance = [ 0 if target in i else float('inf') for i in routes ]
        
#         stop -> some bus -> stop 
        
        buses = defaultdict(list)
        for bus in range(len(routes)):
            for stop in routes[bus]:
                buses[stop].append(bus)
        
        visited = set()
        stops = deque([source])
        level = 0
        while stops:
            size = len(stops)
            for i in range(size):
                stop = stops.popleft()
                
                if stop == target:
                    return level
                
                for bus in buses[stop]:
                    
                    if bus not in visited:
                        visited.add(bus)
                        for s in routes[bus]:
                            stops.append(s)
                            
            level += 1
        return -1
        