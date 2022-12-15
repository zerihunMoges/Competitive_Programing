class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        
        difference = defaultdict(list)
        
        for i in range(len(points)):
            x,y = points[i]
            for j in range(len(points)):
                x1,y1 = points[j]
                if i != j:
                    
                    distance = math.sqrt((x-x1)**2+(y-y1)**2)
                    
                    difference[i].append(distance)
                    
               
        ways = 0
        for key in difference:
            count = Counter(difference[key])
            
            for num in count:
                c = count[num]
                ways += c*(c-1)
                
        return ways
                
                    