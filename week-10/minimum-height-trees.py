class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        neig = defaultdict(set)
        for i in edges:
            indegree[i[0]] += 1
            indegree[i[1]] += 1
            neig[i[1]].add(i[0])
            neig[i[0]].add(i[1])
            
        nodes = deque()  
        for i in range(n):
            if indegree[i] == 1 or indegree[i] == 0:
                nodes.append(i)
                
        answer = []
        count = 0
        while nodes:
            size = len(nodes)
            count += size
            for i in range(size):
                cur = nodes.popleft()
                if n - count <= 0:
                    answer.append(cur)
                for i in neig[cur]:
                    indegree[i] -= 1
                    if indegree[i] == 1:
                        nodes.append(i)
                        
        return answer
