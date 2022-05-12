class Node:
    def __init__(self, child, isend):
        self.child = child
        self.isEnd = isend
        
class WordDictionary:

    def __init__(self):
        self.children = {}

    def addWord(self, word: str) -> None:
        cur = self.children
        for i in range(len(word)):
            node = None
    
            if word[i] not in cur:
                node = Node(defaultdict(set), False)

                cur[word[i]] = node
            else:
                node = cur[word[i]]
                
            if i == len(word)-1:
                node.isEnd = True
                
            cur = node.child

    def search(self, word: str) -> bool:
        node = None
        cur = self.children
        found = False

        def get(i, cur):
         
            if i == len(word)-1 and  word[i] in cur:
                return cur[word[i]].isEnd
                                     
            if word[i] == '.':
                if i == len(word)-1:
                    v = False
                    for l in cur:
                        v = v or cur[l].isEnd
                    return v
                                     
                v = False                   
                for l in cur:
                    v = v or get(i+1, cur[l].child)
                    
                return v
                                     
            elif word[i] not in cur:
                return False
            
            return get(i+1, cur[word[i]].child)
            
        return get(0, cur)
                
