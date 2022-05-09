class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numtolet = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r','s'], '8': ['t', 'u','v'], '9': ['w', 'x','y','z']}
        
        answer = []
        path = []
        def dfs(i):
            
            if i == len(digits):
                if path:    
                    answer.append(''.join(path))
                return
            
            for j in numtolet[digits[i]]:
                path.append(j)
                dfs(i+1)
                path.pop()
                
        dfs(0)
        return answer
