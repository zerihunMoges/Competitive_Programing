class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        posmax = 0
        basket = defaultdict(int)
        j = 0
        i = 0
        while i < len(fruits):
            if fruits[i] not in basket and len(basket) == 2:
                posmax =  max(max(basket[f] for f in basket)-j+1, posmax)
                
                j = min(basket[f] for f in basket)
            
                basket.pop(fruits[j])
                basket[fruits[i]] = i
                j+=1
                
            else:
                basket[fruits[i]] = i
                posmax =  max(i-j+1, posmax)
            i +=1
        return posmax
