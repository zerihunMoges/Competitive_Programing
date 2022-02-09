class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                numbers.append(int(tokens[i]))
            else:    
                if tokens[i] == '+':
                    numbers[-2] = numbers[-2] + numbers[-1]
                elif tokens[i] == '-':
                    numbers[-2] = numbers[-2] - numbers[-1]
                elif tokens[i] == '*':
                    numbers[-2] = numbers[-2] * numbers[-1]
                elif tokens[i] == '/':
                    numbers[-2] = int(numbers[-2]/numbers[-1])
                numbers.pop()

        return numbers[0]
        
        
        ###solution 2 slower
        def evalRPN2(tokens):
          numbers = []
          for i in range(len(tokens)):
              if tokens[i].isdigit() or tokens[i][1:].isdigit():
                  numbers.append(tokens[i])
              else:
                  numbers[-2] = int(eval(str(numbers[-2])+' '+tokens[i]+' '+str(numbers[-1])))
                  numbers.pop()

          return numbers[0]
