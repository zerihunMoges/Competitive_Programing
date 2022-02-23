import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        self.heap = heapq.nlargest(self.k, self.heap)
        
        for i in range(len(self.heap)//2):
            self.heap[i], self.heap[len(self.heap)-i-1] =  self.heap[len(self.heap)-i-1], self.heap[i]
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        
        elif val > self.heap[0]:
            if self.heap != []:
                heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]
