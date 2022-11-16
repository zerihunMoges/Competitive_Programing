class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        moves = 1
        cur = capacity
        for i in range(len(plants)-1):
            cur -= plants[i]
            if cur < plants[i+1]:
                moves += (i+1)*2
                cur = capacity
                
            moves += 1
            
        return moves