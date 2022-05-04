class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      

        count= defaultdict(int)
        for word in words:
            count[word] += 1
        wordc = defaultdict(list)
        
        for i in count:
            wordc[count[i]].append(i)
            
        counts = sorted(wordc, reverse=True)
        
        answer = []
        i = 0
        while len(answer) < k:
            answer+= sorted(wordc[counts[i]])[:k-len(answer)]
            i+=1
        return answer
