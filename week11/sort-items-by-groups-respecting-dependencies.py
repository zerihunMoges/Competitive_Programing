class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        prereq = defaultdict(set)
        prereqG = defaultdict(set)
        indegreeG = defaultdict(int)
        groups = defaultdict(set)
        indegree = defaultdict(int)
        
        
        for i in range(len(group)):
            
            if group[i] == -1:
                group[i] = m
                m+=1
            groups[group[i]].add(i)
      
        for i in range(len(beforeItems)):
            for j in  beforeItems[i]:
                if group[i] == group[j]:
                    prereq[j].add(i)
                    indegree[i] += 1
                elif group[i] not in prereqG[group[j]]:
                    prereqG[group[j]].add(group[i])
                    indegreeG[group[i]] += 1
        # print(group)
        # print(indegreeG)
        # print(prereqG)
        sgroup = deque()
        for i in groups:
            if indegreeG[i] == 0:
                sgroup.append(i)
    
        ans = []     
        while sgroup:
            curg = sgroup.popleft()
            ruque = deque()
            for i in groups[curg]:
                if indegree[i] == 0:
                    ruque.append(i)
            while ruque:
                top = ruque.popleft()
                groups[curg].remove(top)
                ans.append(top)
                for i in prereq[top]:
                    indegree[i]-=1
                    if indegree[i] == 0:
                        ruque.append(i)
                        
            for item in groups[curg]:
                if indegree[item] == 0 and indegreeG[curg] == 0:
                    ans.append(item)
         
            for i in prereqG[curg]:
                indegreeG[i] -= 1
                if indegreeG[i] == 0:
                    sgroup.append(i)
            
                    
        return ans if len(ans) == n else []
                    
        
