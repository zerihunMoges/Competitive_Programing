class Solution:
    def isInBound(self, row, col, x, y):
        if not 0 <= row < x:
            return False
        return 0 <= col < y
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        left = 0
        right = len(cells)-1
        
        
        
        def isPossible(isFlooded):
            lands = deque([[0,i] for i in range(col) if (1,i+1) not in isFlooded])
            
            visited = set()
            while lands:
            
                cur_row, cur_col = lands.popleft()
                if cur_row == row-1:
                    return True
                for row_dir, col_dir in directions:
                    new_row = row_dir + cur_row
                    new_col = col_dir + cur_col

                    if self.isInBound(new_row, new_col, row, col) and (new_row+1, new_col+1) not in isFlooded and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        lands.append([new_row, new_col])
                
                
    
        
        best = 1
        while left <= right:
            
            mid = (left+right)//2
            
            isFlooded = set([(tuple(cells[i])) for i in range(mid)] )
            
            if isPossible(isFlooded):
                best = mid
                left = mid+1
            else:
                right = mid-1
                
        return best
                
                
                
                
                
                
        
        