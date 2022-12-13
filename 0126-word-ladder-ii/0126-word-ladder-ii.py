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

        wordList = set(wordList)
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


                new_word = list(cur)
                for i in range(len(new_word)):
                    for j in range(ord('a'), ord('z')+1):
                        og = cur[i]
                        new_word[i] = chr(j)
                        neig = ''.join(new_word)
                        if neig in wordList:
                    
                            if neig not in visited and neig not in temp:
                                temp.add(neig)
                                words.append(neig)
                            if neig not in visited:
                                path[neig].append(cur)
                            
                        new_word[i] = og
                        
            visited = visited.union(temp)
        
        return self.getPaths(endWord, path, beginWord)
        
        
   