class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        myan = defaultdict(set)
        
        indegree = defaultdict(int)
        neig = defaultdict(list)
        
        for i in edges:
            indegree[i[1]] += 1
            neig[i[0]].append(i[1])
        nodes = deque()
        for i in neig:
            if i not in indegree:
                nodes.append(i)
                
        while nodes:
            
            cur = nodes.popleft()
            
            for i in neig[cur]:
                myan[i].add(cur)
                myan[i].update(myan[cur])
                indegree[i] -= 1
                if indegree[i] == 0:
                    nodes.append(i)
        ans = [[]]*n
        
        for i in myan:
            ans[i] = sorted(list(myan[i]))
            
        return ans
