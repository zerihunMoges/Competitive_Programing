class Solution:
    def isPalindrom(self, string):
        for i in range(len(string)//2):
            if string[i] != string[-i - 1]:
                return False
        return True
    
    @lru_cache(maxsize=None)
    def getPartitions(self, string, i, j):
        if j >= len(string):
            return [[]]
       
        partitions = []
        
        cont = self.getPartitions(string, i, j+1)
        
        if cont != [[]]:
            partitions.extend(cont)
            
        if self.isPalindrom(string[i:j+1]):
            end = self.getPartitions(string, j+1,j+1)
            
            for partition in end:
                partitions.append([string[i:j+1]] + partition)
                
        
        
        return partitions
            

        
    def partition(self, s: str) -> List[List[str]]:
        
        partitions = self.getPartitions(s, 0,0)
        return partitions
    

        