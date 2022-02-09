class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lists = []
    
        for i in range(1, n+1):
            if (i)%3 == 0:
                lists.append('Fizz')
                if (i)%5 == 0:
                    lists[i-1] = lists[i-1]+'Buzz'
            elif (i)%5 == 0:
                lists.append('Buzz')
            else: 
                lists.append(str(i))
        return lists    
