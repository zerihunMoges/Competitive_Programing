class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        alive = defaultdict(int)
        
        maxyear = None
        for birth, death in logs:
            
            for i in range(birth, death):
                alive[i]+=1
                
                if not maxyear or alive[maxyear] < alive[i] or (alive[maxyear] == alive[i] and maxyear > i):
                    maxyear = i
                    
        return maxyear