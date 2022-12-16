class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        
        
        max_space = 1
        prev = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev != -1:
                    max_space = max(max_space, (i-prev-1)//2 + (i-prev-1)%2)
                    
                else:
                    max_space = max(max_space, (i))
                    
                prev = i
                
            elif i == len(seats)-1:
                
                max_space = max(max_space, (i-prev))
                    
                
            
                
        return max_space
                
        
                
                
            
            