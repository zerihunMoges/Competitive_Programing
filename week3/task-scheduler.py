#Big O of O(n) solution even though there are two loops nested they both increment the same counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = []
        for i in tasks:
            if ord(i) - 65 >= len(frequency):
                frequency += [0]*((ord(i)-64)-len(frequency))
            frequency[ord(i)-65] += 1
        frequency.sort(reverse = True)

        space = 0
        i=0
        while i < len(frequency) and n != 0:
            space += (frequency[i]-1)*n
            minspace = space//n 
            i+=1
            while i < len(frequency):
                if frequency[i] > minspace :
                    space -= minspace  + (frequency[i] - minspace -1)*n
                else: space -= frequency[i]
                i += 1
               
        space = max(space, 0)
        return int(space + len(tasks))
