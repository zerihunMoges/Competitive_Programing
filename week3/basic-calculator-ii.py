class Solution:
    
    def is_int(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def calu(self, num1, num2, operand):
        if operand == '+':
            return int(num1) + int(num2)
        elif operand == '-':
            return int(num1) - int(num2)
        elif operand == '*':
            return int(num1)*int(num2)
        elif operand == '/':
            return int(int(num1)/int(num2))
        
    def calculate(self, s: str) -> int:
        operations= []
        numbers = []
        number = ''

        for i in range(len(s)):

            if self.is_int(s[i]):
                number+=s[i]

            elif s[i] == '+' or s[i] == '-':
                operations.append(s[i])
                numbers.append(number)
                for i in range(len(operations)):
                    if len(numbers) >= 2:
                        numbers[-2] = self.calu(numbers[-2], numbers[-1], operations[-2])
                        operations.pop(-2)
                        numbers.pop(-1)
                number = ''

            elif s[i] == '*' or s[i] == '/':
                operations.append(s[i])
                numbers.append(number)
                if len(numbers) >= 2 and (operations[-2] == '*' or operations[-2] == '/'):
                    numbers[-2] = self.calu(numbers[-2], numbers[-1], operations[-2])
                    operations.pop(-2)
                    numbers.pop(-1)
                number = ''

            if i == len(s)-1:
                numbers.append(number)
                for i in range(len(operations)):
                    if len(numbers) >= 2  :
                        numbers[-2] = self.calu(numbers[-2], numbers[-1], operations[-1])
                        operations.pop(-1)
                        numbers.pop(-1)

        return numbers[0]
