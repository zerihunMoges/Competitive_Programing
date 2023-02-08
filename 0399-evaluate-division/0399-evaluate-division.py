class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    
        eqtree = defaultdict(dict)
        for i in range(len(equations)):
            dividen, divider = equations[i]
            eqtree[dividen][divider] = values[i]
            eqtree[divider][dividen] = 1/values[i]
        
        def find(cur, target):
            if target in eqtree[cur]:
                return eqtree[cur][target]
            for key in eqtree[cur]:
                if key not in visited:
                    visited.add(key)
                    res = find(key, target)
                    if res != None:
                        return eqtree[cur][key]*res
            return None
        
        answer = []
        for dividen, divider in queries:
            
            visited = set()
            res = find(divider, dividen)
            if res != None:
                answer.append(1/res)
            else:
                answer.append(-1.0)
        return answer
                   
                    
                
        