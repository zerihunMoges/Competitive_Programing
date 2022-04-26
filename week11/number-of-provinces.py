class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [0]*len(isConnected)
        rank = [0]*len(isConnected)
        for i in range(len(root)):
            root[i] = i
            
        def find(i):
            if i == root[i]:
                return i
            
            root[i] = find(root[i])
            return root[i]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rank[rootx] > rank[rooty]:
                root[rooty] = rootx
            elif rank[rooty] > rank[rootx]:
                root[rootx] = rooty
            else:
                root[rootx] = rooty
                rank[rooty] += 1
        def connected(x,y):
            return find(x) == find(y)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(i,j)
        count = 0        
        for i in range(len(root)):
            root[i] = find(root[i])
                
                
        return len(set(root))
