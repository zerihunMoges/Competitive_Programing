class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root = {}
        owner = {}
        
        
            
        def find(i):
            if root[i] == i:
                return root[i]
            root[i] = find(root[i])
            return root[i]
        def union(a,b):

            roota = find(a) if a in root else a
            rootb = find(b) if b in root else b

            root[rootb] = roota
        answer = defaultdict(list)
        
        for i in accounts:
            owner[i[1]] = i[0]
            for email in range(1, len(i)):
                if i[email] not in root:
                    root[i[email]] = i[1]
                else:
                    
                    union(i[email], i[1] )
                    
        
        for i in root:
            answer[find(i)].append(i)
            
        result = []
        i = 0
        for ans in answer:
            result.append([owner[ans]])
            result[i] += sorted(answer[ans])
            i+=1
            
        return result
