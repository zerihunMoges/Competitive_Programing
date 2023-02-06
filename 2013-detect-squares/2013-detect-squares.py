class DetectSquares:

    def __init__(self):
        
        self.points = defaultdict(lambda: defaultdict(int))
        

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]]+=1

    def count(self, point: List[int]) -> int:
        
        count = 0
        for p in self.points[point[0]]:
            
            dif = abs(point[1] - p)
            if dif > 0 :
                count += self.points[point[0]-dif][point[1]]*self.points[point[0]-dif][p]*self.points[point[0]][p]
                count += self.points[point[0]+dif][point[1]]*self.points[point[0]+dif][p]*self.points[point[0]][p]
            
        return count
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)