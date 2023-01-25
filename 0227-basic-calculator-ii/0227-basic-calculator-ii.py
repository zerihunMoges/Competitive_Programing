class Solution:
    def precedence(self, operation):
        if operation == '*' or operation == '/':
            return 1
        
        return 0
    def calculate(self, s: str) -> int:
        s+= '#'
        current = 0
        nums = []
        operations = []
        for i in range(len(s)):
            
            if s[i].isdigit():
                current = current*10 + int(s[i])
        
            elif s[i] != ' ':
                
                while operations and self.precedence(operations[-1]) >= self.precedence(s[i]):
                    num, opr = nums.pop(), operations.pop()
                    
                    if opr == '+':
                        current += num
                    if opr == '-':
                        current = num-current
                    if opr == '*':
                        current *= num
                    if opr == '/':
                        current = num//current
                        
                nums.append(current)
                operations.append(s[i])
                current = 0
                
            print(nums)
        print(nums)
        return nums[0]
                
                