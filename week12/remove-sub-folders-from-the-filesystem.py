class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
      
        
        trie = defaultdict(set)
        
        topfolders = set()
        for path in folder:
            path = path.split('/')
            order = []
            cur = trie
            for i in range(1, len(path)):
         
                order.append('/'+str(path[i]))
                if path[i] not in cur:
                    cur[path[i]] = defaultdict(set)
                    if i == len(path)-1:
                        topfolders.add(''.join(order))
                        
                elif (path[i] in cur and len(cur[path[i]]) == 0):
                    topfolders.add(''.join(order))
                    break
                    
                cur = cur[path[i]]
      
        return list(topfolders)
