class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        neig = defaultdict(set)
        supplies = set(supplies)
        for i in range(len(recipes)):
            for j in ingredients[i]:
                if j not in supplies:
                    indegree[recipes[i]] += 1
                    neig[j].add(recipes[i])
        
        recipe = deque()  
        
        for i in recipes:
            if i not in indegree:
                recipe.append(i)
        possible = []
        while recipe:
            cur = recipe.popleft()
            possible.append(cur)
            for i in neig[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    recipe.append(i)
                    
        return possible
