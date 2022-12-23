class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        
        state = deque([])
        dominoes = list(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                sign = 1 if dominoes[i] == 'R' else -1
                state.append([i+sign, dominoes[i]])
                
        while state:
            size = len(state)
            changed = set()
            for i in range(size):
                cur, dirc = state.popleft()
                
                if 0 <= cur < len(dominoes) and dominoes[cur] == '.':
                    
                    dominoes[cur] = dirc
                    sign = 1 if dirc == 'R' else -1
                    state.append([cur+sign, dirc])
                    changed.add(cur)
                    
                elif cur in changed:
                    
                    dominoes[cur] = '.'
                    
        return ''.join(dominoes)
                
                
                
                