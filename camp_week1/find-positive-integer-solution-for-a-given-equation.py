"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x = 1
        
        answer=[]
        while x <= 1000:
            ly = 1
            ry = 1000 if answer == [] else answer[0][1]
            
            
            while ly <= ry:
                mid = (ly+ry)//2
                if customfunction.f(x,mid) > z:
                    ry = mid-1
                    
                elif customfunction.f(x,mid) < z:
                    ly = mid+1
                else:
                    answer.append([x,mid])
                    break
                      
            x+=1
            if customfunction.f(x, 1) > z:
                break 
            
            
        return answer
                    
          
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x = 1
        
        answer=[]
        while x <= 1000:
            ly = 1
            ry = 1000
            while ly <= ry:
                mid = (ly+ry)//2
                if customfunction.f(x,mid) > z:
                    ry = mid-1
                    
                elif customfunction.f(x,mid) < z:
                    ly = mid+1
                else:
                    answer.append([x,mid])
                    break
            if customfunction.f(x,1) > z:
                break
                
            x+=1
            
            
        return answer
   
   
                    
