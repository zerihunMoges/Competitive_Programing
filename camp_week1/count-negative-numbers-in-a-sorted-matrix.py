class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        for i in range(len(grid)):
            left = 0
            right = len(grid[i])-1
            sn = len(grid[i])
            while left<= right:
                
                mid = (left+right)//2
                if grid[i][mid] >= 0:
                    left = mid+1
                elif grid[i][mid] < 0:
                    right = mid-1
                    if grid[i][mid] < 0:
                        sn = mid
            if sn == 0:
                count += (len(grid)-i)*len(grid[i])
                break
                
            else:
                count += len(grid[i]) - sn
                
        return count
