class Solution:
    def romanToInt(self, s: str) -> int:
        
        rom = {"I":1, "V":5, "X" :10, 'L':50, 'C':100, 'D':500,'M':1000}
        
        i = 0
        j = 1
        num = 0
        while i < len(s):
       
            if j == len(s):
                num += rom[s[j-1]]
            
            elif rom[s[i]] >= rom[s[j]]:
                num += rom[s[i]]
                               
            elif rom[s[j]] > rom[s[i]]:
                num += rom[s[j]] - rom[s[i]]
                i += 1
                j+=1
            
            i+=1
            j+=1
        return num