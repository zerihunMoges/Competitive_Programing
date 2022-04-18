class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = defaultdict(set)
        
        indegree = defaultdict(int)
        neig = defaultdict(list)
        
        for i in prerequisites:
            indegree[i[1]] += 1
            neig[i[0]].append(i[1])
        nodes = deque()
        for i in neig:
            if i not in indegree:
                nodes.append(i)
                
        while nodes:
            
            cur = nodes.popleft()
            
            for i in neig[cur]:
                prereq[i].add(cur)
                prereq[i].update(prereq[cur])
                indegree[i] -= 1
                if indegree[i] == 0:
                    nodes.append(i)
        answer = []
        for i in queries:
            if i[0] in prereq[i[1]]:
                answer.append(True)
            else:
                answer.append(False)
        return answer
