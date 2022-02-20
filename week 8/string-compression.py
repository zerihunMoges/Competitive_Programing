class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0
        s = ""
        for i in range(len(chars)):
            if chars[i] != chars[j]:
                s+= chars[j] +( str(i-j) if i-j > 1 else '')
                j = i
            if i == len(chars)-1:
                s+= chars[j] +( str(i-j+1) if i-j+1 > 1 else '')
                
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
