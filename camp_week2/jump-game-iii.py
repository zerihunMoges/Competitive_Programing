from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        inbound = lambda x: 0 <= x < len(arr)
        def isCyclic(start):
            positions = deque()
            positions.append(start)
    
            while positions:
                
                pos = positions.popleft()
                visited.add(pos)
                if arr[pos] == 0:
                    return True
                    break
          
                
                    
                if inbound(arr[pos] + pos):
                    if arr[pos] + pos not in visited:
                        positions.append(arr[pos] + pos)
                   
                        
                if inbound(pos-arr[pos]):
                    if pos-arr[pos] not in visited:
                        positions.append(pos-arr[pos])
                    
        
        answer = isCyclic(start)
        return answer if answer == True else False
