class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        given = set()
        
        for i in range(len(street)):
            if street[i] == 'H':
                if i-1 not in given and i+1 < len(street) and street[i+1] == '.':
                    given.add(i+1)
                elif i>0 and street[i-1] == '.':
                    given.add(i-1)
                else:
                    return -1
                
        return len(given)
         
         
         
         
         
         
         
         
         
        METHOD 2, O(1) space ##############################################
        
        boundbyhouse = lambda x:  x > 0 and len(street)-x >= 2 and street[x-1] == "H" == street[x+1]
        deadend = lambda x: len(street) == 1 or (x ==0 and street[x+1] == 'H')  or (x == len(street)-1 and street[x-1] == 'H') 
     
        count = 0
        i = 0
        j = 0
        while i < len(street):
            if i >= j and street[i] == '.' and boundbyhouse(i):
                count += 1
                j = i +3
                
            elif street[i] == 'H' and (boundbyhouse(i) or deadend(i)):
                return -1
            i+=1
            
        houses = street.count("H") 
        return  houses-count
