class Solution:
    def findPermutations(self, string, idx):
        if idx >= len(string):
            return ['']
        
        new_permutations = []
        permutations = self.findPermutations(string, idx+1)
        
        for permutation in permutations:
            new_permutations.append(string[idx] + permutation)
            
            if ord('A') <= ord(string[idx]) <= ord('Z'):
                new_permutations.append(chr(ord('a') + ord(string[idx])-ord('A')) + permutation)
            elif ord('a') <= ord(string[idx]) <= ord('z'):
                new_permutations.append(chr(ord('A') + ord(string[idx])-ord('a')) + permutation)

        return new_permutations
        
    def letterCasePermutation(self, s: str) -> List[str]:
        
        permutations = self.findPermutations(s, 0)
        return permutations
        
        
        
        