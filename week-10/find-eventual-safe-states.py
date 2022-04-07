class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
       
        visited = set()
       
        answer = []
        cy = set()
        self.path = set()
        def dfs(parent):
            visited.add(parent)
            self.path.add(parent)
            for node in graph[parent]:
                if node in self.path:
                    cy.add(node)
                    return True
                if node not in visited:    
                    r = dfs(node)
                    if r == True:
                        cy.add(node)
                        return True
            self.path.remove(parent)
            return 
    
        
        
        for i in range(len(graph)):
            if i not in visited:
                r = dfs(i)
                if r == True:
                    cy.add(i)
                    
        for i in range(len(graph)):
            if i not in cy:
                answer.append(i)
            
        return answer
