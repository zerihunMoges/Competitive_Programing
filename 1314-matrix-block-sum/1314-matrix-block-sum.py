class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        
        ans = [[0]*len(mat[i]) for i in range(len(mat))]
        
        
        for i in range(len(mat)):
            for j in range(1,len(mat[i])):
                mat[i][j] += mat[i][j-1]
                
        for i in range(len(mat)):
            for j in range( len(mat[i])):
                s = 0
                for m in range(max(i-k, 0), min(i+k+1, len(mat))):
                    if j-k <= 0:
                        s += mat[m][min(j+k, len(mat[i])-1)]
                    else:
                        s += mat[m][min(j+k, len(mat[i])-1)] - mat[m][j-k-1]               
                ans[i][j] = s
                
        return ans
                