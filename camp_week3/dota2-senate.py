class Solution:
    def predictPartyVictory(self, senate: str) -> str:
    
        senat = {"R":deque(), "D":deque()}
        s = {"R": "D", "D":"R"}
        out = set()
        
        for i in range(len(senate)):
            senat[senate[i]].append(i)
        
        j = 0
        while senat["R"] != deque([]) and senat["D"] != deque([]):
            if j not in out:
                out.add(senat[s[senate[j]]].popleft())
                senat[senate[j]].append(senat[senate[j]].popleft())
            j+=1 
            j %= len(senate)
     
        return "Radiant" if len(senat["R"]) > len(senat["D"]) else "Dire"
