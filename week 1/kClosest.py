class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort( key = lambda x: math.sqrt(pow(x[0], 2)+ pow(x[1],2 )))
        return points[:k]
