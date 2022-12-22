class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
   
        peoples = []
        
        for h,k in people:
            peoples.append([h,k])
            
        queue = []
        for i in range(len(peoples)):
            front = None
            for j in range(len(peoples)):
                
                h , k = peoples[j]
                
                if k == 0 and ( front == None or h < peoples[front][0]):

                    front = j
     
            for j in range(len(peoples)):

                if peoples[front][0] >= peoples[j][0]:
                    peoples[j][1] -= 1

            queue.append(people[front])

            peoples[front] = [float('inf'), float('inf')]
  
        return queue
            
        
        
        
                
                
                    
                
        