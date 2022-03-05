class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        visited = set()
        
        province = 0  
        def findProvince(col):
            
            for i in range(len(isConnected)):
                nrow = i
                ncol = col
                if isConnected[nrow][ncol] == 1 and nrow not in visited:
                    visited.add(nrow)
                    findProvince(nrow)
            

        for i in range(len(isConnected)):
            if i not in visited:
                findProvince(i)
                
                province += 1
        
        
        return province
