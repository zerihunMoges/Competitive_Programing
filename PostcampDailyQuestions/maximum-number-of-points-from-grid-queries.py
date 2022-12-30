class Solution:
    def inBound(self, row, col, grid):
        
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])
    
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        cells = []
        heapq.heappush(cells, [grid[0][0], 0,0])
        
        minimum = min(queries)
        maximum = max(queries)
        max_score = defaultdict(int)
        
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        visited = set()
        visited.add((0,0))
        cells_count = 0
        for i in range(minimum,maximum +1):
            while cells and cells[0][0] < i:
                val, row, col = heapq.heappop(cells)
                cells_count += 1
                for row_dir, col_dir in directions:
                    new_row = row+row_dir
                    new_col = col+col_dir
                    if self.inBound(new_row, new_col, grid) and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        heapq.heappush(cells, [grid[new_row][new_col], new_row,new_col])
                        
            max_score[i] = cells_count  
        answer = []
        
        for query in queries:
            answer.append(max_score[query])
                
                
        return answer
