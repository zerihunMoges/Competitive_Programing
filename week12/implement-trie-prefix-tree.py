class Node:
    def __init__(self, child, isend):
        self.child = child
        self.isEnd = isend
        
class Trie:

    def __init__(self):
        self.children= defaultdict(set)

    def insert(self, word: str) -> None:
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
        for i in word:
            if i not in cur:
                return False
            
            node = cur[i]
                
            cur = node.child
            
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = None
        cur = self.children
        for i in prefix:
            node = None
           
            if i not in cur:
                return False
            
            node = cur[i]
                
            cur = node.child
        return True
