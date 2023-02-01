class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
        
        count = [1]
        
        for i in blocks:
            if i == "W":
                count.append(count[-1]+1)
            else:
                count.append(count[-1])
        print(count)
        m = len(blocks)
        for i in range(k, len(count)):
            m = min(m, count[i]-count[i-k])
            
        return m