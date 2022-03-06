class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        wordn = {}
        for i in wordList:

            for j in range(len(i)+1):
                word = i[0:j]+' '+i[j+1:]
                if word in wordn:
                    wordn[word] += [i]

                else:
                    wordn[word]  = [i]

        def findNeigb(word, words):
            for j in range(len(word)+1):
                nword = word[0:j]+' '+word[j+1:]
                if nword in wordn:
                    for i in wordn[nword]:
                        if i not in visited:
                            visited.add(i)
                            words.append(i)      


        words = deque()
        words.append(beginWord)

        level = 0
        while words:
            size = len(words)
            level += 1
            for i in range(size):
                word = words.popleft()
                if word == endWord:
                    return level
                findNeigb(word, words)

        return 0
