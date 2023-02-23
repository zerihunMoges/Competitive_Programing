class Solution:
    
    def calculate(self, x,y, op):
        x = int(x)
        y = int(y)
        if op == '+':
            return x+y
        if op == '-':
            return x-y
        if op == '*':
            return x*y
        
        return 0
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        
        if expression.isdigit():
            return [int(expression)]

    
        results = []
        for i, op in enumerate(expression):
            if op in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        results.append(self.calculate(l, r, op))

        return results
        
            
        
        