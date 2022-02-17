class Solution:
    def play(self, players, k, i):
        if len(players) == 1:
            return players[0]
        else:
            i = (i+ k-1)%len(players)
            players.pop(i)
            return self.play(players, k, i)
        
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        i = 0
        return self.play(players,k, i)
