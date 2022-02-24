import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
                
        for i in range(k-1):
            lst = heapq.heappop(matrix)
            heapq.heappop(lst)
            if lst:
                heapq.heappush(matrix, lst)
                
     
        return matrix[0][0]

#second

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for lst in matrix:
            for i in lst:
                heapq.heappush(heap, i)
                
                
        for i in range(k-1):
            heapq.heappop(heap)
                
     
        return heap[0]
