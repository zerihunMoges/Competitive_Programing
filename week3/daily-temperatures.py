class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        answer = [0]*len(temperatures)
    
        for i in range(1,len(temperatures)):
            if temperatures[i] > temperatures[stack[-1]]:
                while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                    j = stack.pop(-1)
                    answer[j] = i - j
                stack.append(i)
            else:
                stack.append(i)
            

        return answer
