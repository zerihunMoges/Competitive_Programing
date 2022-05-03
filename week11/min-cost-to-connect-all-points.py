class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distances = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if i != j:
                    d = abs(points[i][0]-points[j][0]) + abs(points[i][1]- points[j][1])
                    distances.append([d, i, j])
 
        distances.sort()
        root = [i for i in range(len(points))]
        def find(i):
            if root[i] == i:
                return i
            root[i] = find(root[i])
            return root[i]
        
        ans = 0
        for p in distances:
            p1 = find(p[1])
            p2 = find(p[2])
            if p1 != p2:
                root[p1] = p2
                ans += p[0]
        return ans
