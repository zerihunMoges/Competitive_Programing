class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = [0]
        zeros = [0]
        
        for i in range(len(s)):
            if s[i] == '0':
                ones.append(ones[-1])
                zeros.append(zeros[-1]+1)
            else:
                ones.append(ones[-1]+1)
                zeros.append(zeros[-1])
                
        ways = [[0]*3 for i in range(2)]
        
        for i in range(len(s)):
            if s[i] == '0':
                ways[0][0] += 1
                for j in range(len(ways[1])-1):
                    if ways[1][j]:
                        ways[0][j+1] += ways[1][j]

            else:
                ways[1][0] += 1
                for j in range(len(ways[0])-1):
                    if ways[0][j]:
                        ways[1][j+1] += ways[0][j]

                    
        return ways[0][2] + ways[1][2]