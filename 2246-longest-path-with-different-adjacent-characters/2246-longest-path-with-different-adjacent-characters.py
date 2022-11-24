class Solution:
    def findLongestPath(self, cur, neigs, s):
    
        path, longest_path = 1, 1
        longest_child_path = 0

        for neig in neigs[cur]:
            child_path, child_longest_path = self.findLongestPath(neig, neigs, s)

            if s[cur] != s[neig]:
                longest_path = max(longest_child_path + 1 + child_path, longest_path)
                longest_child_path = max(longest_child_path, child_path)
            longest_path = max(longest_path, child_longest_path, child_path)
            
        return 1+longest_child_path, longest_path
    
    
    def longestPath(self, parent: List[int], s: str) -> int: 
        
        neigs = defaultdict(list)

        for i in range(len(parent)):
            neigs[parent[i]].append(i)

        root = 0
        path, longest_path  = self.findLongestPath(root, neigs, s)

        return longest_path

    