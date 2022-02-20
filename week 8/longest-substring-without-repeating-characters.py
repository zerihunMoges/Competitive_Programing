class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        mlen = 0
        j = -1
        for i in range(len(s)):
            if s[i] in letters:
                if j <= letters[s[i]]:
                    j = letters[s[i]]
                mlen = max( mlen, i - j)
                
                letters[s[i]] = i
                
                
                
            else:
                letters[s[i]] = i
                mlen = max(mlen, i-j)
                
        return mlen
