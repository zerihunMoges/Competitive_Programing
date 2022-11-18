class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        
        j = len(plants) - 1
        i = 0
        refill = 0
        alice = capacityA
        bob = capacityB
        while i <= j:
            
            if i == j:
                cur = max(alice, bob)
                if cur < plants[i]:
                    refill += 1
                return refill
            
           
            if alice < plants[i] :
                refill += 1
                alice = capacityA
            if bob < plants[j]:
                refill += 1
                bob = capacityB
                
            alice -= plants[i]
            bob -= plants[j]
            
            i += 1
            j -= 1
            
        return refill
            