class Node:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        return self.count < other.count
    def __gt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        
        return self.count > other.count
    
import heapq

    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        fre = {}
        
        for i in range(len(words)):
            if words[i] in fre:
                fre[words[i]] += 1
            else:
                fre[words[i]] = 1
        lfre = [[0,0]]*len(fre)
        j = 0
        for i in fre:
            lfre[j] = Node(-1*fre[i], i)
            j += 1
            
        heapq.heapify(lfre)
        klargest = [0]*k
        for i in range(k):
            klargest[i] = heapq.heappop(lfre).word
            
        return klargest
        
