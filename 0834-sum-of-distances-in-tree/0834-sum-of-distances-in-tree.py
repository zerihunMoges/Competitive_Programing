class Solution:
    def findDistance(self, node, distance, tree,visited, n, childs_count):
        visited[node] = True
        nodes, tot_distance = 1, 0
        for child in tree[node]:
            if not visited[child]:
               
                d, childs = self.findDistance(child, distance, tree, visited, n, childs_count)
                nodes += childs
                tot_distance += d
        childs_count[node] = nodes
        distance[node] = tot_distance
        
        return tot_distance+nodes , nodes
            
    def finishDistance(self, node, distance,tree, visited, n, childs):
        visited[node] = True
    
        for child in tree[node]:
            if not visited[child]:
                distance[child] += (distance[node] - (distance[child]+childs[child])) + (n-childs[child]) 
                self.finishDistance(child, distance,tree, visited, n, childs)
                
          
        
        
    def buildTree(self, edges):
        tree1 = defaultdict(list)
        for parent, child in edges:
            tree1[parent].append(child)
            tree1[child].append(parent)
        
        return tree1
    
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        distance = [0]*n
        tree1 = self.buildTree(edges)
        childs = [0]*n
        visited = [False]*n
        root = 0
        self.findDistance(root, distance, tree1, visited, n, childs)
        visited = [False]*n
        self.finishDistance(root, distance, tree1, visited, n, childs)
        
        return distance