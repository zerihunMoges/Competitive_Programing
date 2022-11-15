class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        after_collison = []
        
        for i in range(len(asteroids)):
            
            while after_collison and after_collison[-1] > 0 and asteroids[i] < 0:
                
                if abs(asteroids[i]) > abs(after_collison[-1]):
                    after_collison.pop()
                    
                elif abs(asteroids[i]) < abs(after_collison[-1]):
                    asteroids[i] = 0
                    
                else:
                    after_collison.pop()
                    asteroids[i] = 0
                    
            if asteroids[i]:
                after_collison.append(asteroids[i])
                
                
        return after_collison
                
                    
                
                
    