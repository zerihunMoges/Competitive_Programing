class Solution:
    def frequencySort(self, s: str) -> str:
        fre = [[0,'']]*(ord('z')-ord('0') + 1)
       
        for i in s:
            fre[ord(i)-ord('A')] = [fre[ord(i)-ord('A')][0]+1, i]
       
        fre.sort(reverse=True)
        answer = ''
 
        for i in range(len(fre)):
            answer += fre[i][1]*fre[i][0]
            
        return answer