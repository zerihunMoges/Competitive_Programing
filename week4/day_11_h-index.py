class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sortedCitations = [0]
        frequency = 0
        hIndex = 0
        
        for i in range(len(citations)):
            if citations[i] >= len(sortedCitations):
                sortedCitations += [0]*(citations[i] - len(sortedCitations)+1)
            sortedCitations[citations[i]] += 1
            
        
        for i in range(len(sortedCitations)):
            if i <= len(citations) - frequency:
                hIndex = max(hIndex, i)
            frequency += sortedCitations[i]
            
                
        return hIndex
