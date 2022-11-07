class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        pass
#         [[1,5],[10,11],[12,18],[20,25],[30,32]]
                                

        tiles.sort()
        gaps = [0]*len(tiles)
        max_len = 0
        for i in range(1, len(tiles)):
            gaps[i] = gaps[i-1] + (tiles[i][0] - tiles[i-1][1] - 1)
    
        for i in range(len(tiles)):
            
            start, end = tiles[i]
            left = i
            right = len(tiles)-1
            best = left
            while left <= right:
                
                mid = (left+right)//2
                cur_start, cur_end = tiles[mid]
                if cur_start - start + 1 <= carpetLen:
                    left = mid + 1
                    best = mid
                else:
                    right = mid - 1
                    
            best_start, best_end = tiles[best]
            best_end = min(start+carpetLen - 1, best_end)
           
            
            max_len = max( max_len, (best_end-start + 1) - (gaps[best] - gaps[i]))
            
        return max_len                    
        
        
        