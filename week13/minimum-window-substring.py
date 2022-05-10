class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        td = defaultdict(int)
        for i in t:
            td[i] += 1
            
        i = 0 
        j = 0
       
        minl = []
        shortest = None
        k = len(t)
        while i < len(s):

            if s[i] in td:
                td[s[i]] -= 1
                if td[s[i]] >=0 :
                    k-=1
            while j <= i and k == 0:
                if s[j] in td:
                    td[s[j]] += 1
                    if td[s[j]] >0 :
                        k+=1
                shortest = [j,i] if shortest == None or shortest[1]-shortest[0] >= i-j else shortest   
                j+=1
            i+=1
            
        return s[shortest[0]:shortest[1]+1] if shortest else ""
