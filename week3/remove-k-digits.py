class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        minimum =[]
        removed = k
        for  i in range(len(num)):

            while minimum and int(num[i]) < int(minimum[-1]):
                if removed <= 0:
                    break
                minimum.pop()
                removed -= 1    
                
            minimum.append(num[i])
         
        length = len(minimum)
        while length > len(num) - k:
                minimum.pop(-1)
                length -= 1

        return str(int(''.join(minimum))) if len(num) > k else '0' 
