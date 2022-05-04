class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = defaultdict()
        
        
        for product in products:
            cur = trie
            for l in range(len(product)):
                if product[l] not in cur:
                    cur[product[l]] = defaultdict()
                if l == len(product)-1:
                    cur[product[l]]["End"] = True
                cur = cur[product[l]]
  
        path = []
        words = []
        def get(l , cur):
            if l == "End":
                words.append(''.join(path))
                return 
            path.append(l)
            
            if l in cur:
                for nl in cur[l]:
                    get(nl, cur[l])
            
            path.pop()
        sw = ''
        cur = trie
        answer = []
        for i in searchWord:
            path = list(sw)
            sw += i
            words = []
            get(i, cur)
            if i in cur:
                cur = cur[i]
            else:
                cur[i] = defaultdict(defaultdict)
                cur = cur[i]
            
            answer.append(sorted(words)[:3])
            
        return answer
       
