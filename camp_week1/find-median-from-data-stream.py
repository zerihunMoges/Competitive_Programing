import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.right) < 2:
            heapq.heappush(self.right, num)
            
        elif (len(self.right) + len(self.left))%2 == 0:
            heapq.heappush(self.right, num)
            heapq.heappush(self.left, -1*(heapq.heappop(self.right)))
           
            
        elif (len(self.right) + len(self.left))%2 != 0:
            heapq.heappush(self.left, -1*num)
            heapq.heappush(self.right, -1*(heapq.heappop(self.left)))
            
    def findMedian(self) -> float:
        
        if len(self.right) + len(self.left) < 3:
            return(self.right[0]/1 if len(self.right)==1 else (self.right[0]+self.right[1])/2 )
        elif (len(self.right) + len(self.left))%2 != 0:
            return self.right[0]/1
        elif (len(self.right) + len(self.left))%2 == 0:
        
            return (self.right[0]+min(self.right[1],self.right[2]))/2
