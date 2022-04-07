class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        neig = defaultdict(set)
        for i in prerequisites:
            indegree[i[0]] += 1
            neig[i[1]].add(i[0])
        courses = deque()  
        
        for i in range(numCourses):
            if i not in indegree:
                courses.append(i)
                
        topsort = []   
        while courses:
            cur = courses.popleft()
            topsort.append(cur)
            for i in neig[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    courses.append(i)
                    
        return topsort if len(topsort) == numCourses else []
      
 ################################################### DFS 
      
 class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        answer = []
        self.isCyclic = False
        self.path = set()
        def dfs(parent):
            visited.add(parent)
            self.path.add(parent)
            for node in neig[parent]:
                if node in self.path:
                    self.isCyclic = True
                    
                if node not in visited:    
                    dfs(node)
                
                    
            answer.append(parent)
            self.path.remove(parent)
            return 
    
        neig = defaultdict(set)
        for i in prerequisites: 
            neig[i[1]].add(i[0])
        
        
        for i in range(numCourses):
            if i not in visited:
                dfs(i)
            
        return answer[::-1] if self.isCyclic == False else []
