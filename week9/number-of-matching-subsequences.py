class Node:
    def __init__(self, child, isend):
        self.child = child
        self.isEnd = isend
        self.count = 0
        
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
                node.count += 1
                
            cur = node.child



class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index = defaultdict(deque)
        trie = Trie()
        for  i in words:
            trie.insert(i)
        cur = trie
        c = 0
    
        def count(n, cur, i):
            nonlocal c
            while i < len(s) and s[i] != n:
                i += 1
            
            if i >= len(s):
                return 

            if cur[n].isEnd:
                c += cur[n].count

            for ne in cur[n].child:
                count(ne, cur[n].child, i+1)
                
        cur = trie.children
        for n in cur:
            count(n, cur, 0)
        
        return c
