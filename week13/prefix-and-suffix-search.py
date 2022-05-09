# class Letter:
#     def __init__(self):
#         self.index = set()
#         self.child = set()
class WordFilter:

    def __init__(self, words: List[str]):
        print(len(words))
        self.ptrie = defaultdict(list)
        self.strie = defaultdict(set)
        
        for i in range(len(words)):
            cur = self.ptrie
            for j in words[i]:
                if j not in cur:
                    cur[j] = defaultdict(list)
                    
                
                cur = cur[j]
                cur['index'].append(i)
        k = 0  
        for i in words:
            cur = self.strie
            for j in range(len(i)-1, -1, -1):
                if i[j] not in cur:
                    cur[i[j]] = defaultdict(set)
                    
                
                cur = cur[i[j]]
                cur['index'].add(k)
            k += 1

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.ptrie
        pre = []
        suf = set()
        for i in range(len(prefix)):
            if prefix[i] not in cur:
                break 
            if i == len(prefix)-1:
                pre =cur[prefix[i]]['index']   
            cur = cur[prefix[i]]
                
            
                
        cur = self.strie  
        for i in range(len(suffix)-1, -1, -1):
            if suffix[i] not in cur:
                break 
                
            if i == 0:
                suf = cur[suffix[i]]['index']
                
            cur = cur[suffix[i]]
      
        m = -1
        i = 0

        pre.sort(reverse=True)
        for i in pre:
            if i in suf:
                m = i
                break
        
        return m
