class Solution:
    def getPaths(self, cur, paths, start):
        if cur == start:
            return [[start]]
        
        path = []
        for node in paths[cur]:
            ps = self.getPaths(node, paths, start)
            for p in ps:
                path.append(p+[cur])
            
            
        return path
            
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        graph = defaultdict(list)
        
        for word in wordList:
            
            new_word = list(word)
            for i in range(len(word)):
                for j in range(ord('a'), ord('z')+1):
                    og = word[i]
                    new_word[i] = chr(j)
                    graph[''.join(new_word)].append(word)
                    new_word[i] = og
        
        words = deque([beginWord])
        path = defaultdict(list)
        visited = set()
        answer = []
        while words and answer == []:
            size = len(words)
            temp = set()
            for i in range(size):
                cur = words.popleft()
                if cur == endWord:
                    answer.append([cur])


                for neig in graph[cur]:
                    
                    if neig not in visited and neig not in temp:
                        temp.add(neig)
                        words.append(neig)
                    if neig not in visited:
                        path[neig].append(cur)
                        
            visited = visited.union(temp)
        
        return self.getPaths(endWord, path, beginWord)
        
        
   