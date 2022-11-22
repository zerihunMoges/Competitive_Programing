class Solution:
    def candy(self, ratings: List[int]) -> int:
        toleft = defaultdict(lambda: -1)
        toright = defaultdict(lambda: len(ratings))
        decreasing = []
        
        for i in range(len(ratings)):
            
            if decreasing and ratings[decreasing[-1]] <= ratings[i]:
                while decreasing:
                    cur = decreasing.pop()
                    toright[cur] = i
            decreasing.append(i)
            
        decreasing = []
        for i in reversed(range(len(ratings))):
            if decreasing and ratings[decreasing[-1]] <= ratings[i]:
                while decreasing:
                    cur = decreasing.pop()
                    toleft[cur] = i
            decreasing.append(i)
       
        candies = 0    
        for i in range(len(ratings)):
            
            candies += max(i-toleft[i], toright[i]-i)
                    
        return candies
            
        
        
        
        
        