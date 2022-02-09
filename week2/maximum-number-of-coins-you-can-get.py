class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxcoins = 0
        j = -2
        for i in range(len(piles)//3):
            maxcoins+=piles[j]
            j-=2
        return maxcoins
