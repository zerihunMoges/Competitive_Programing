
        
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startx =0
        starty =0
        endy = len(matrix)-1
        endx = len(matrix[0])-1
        spirallen = 0
        
        matrixlen = len(matrix)*len(matrix[0])
        spiralarry = [0] * matrixlen
        
        while spirallen <  matrixlen:
            i = startx
            while i <= endx and spirallen< matrixlen:
                spiralarry[spirallen] = matrix[starty][i]
                spirallen += 1
                i += 1
            starty += 1

            i = starty
            while i <= endy and spirallen< matrixlen:
                spiralarry[spirallen] = matrix[i][endx]
                spirallen+=1
                i += 1

            endx -= 1

            i = endx
            while i >= startx and spirallen< matrixlen:
                spiralarry[spirallen] = matrix[endy][i]
                spirallen += 1
                i -= 1
            endy -= 1

            i = endy
            while i >= starty and spirallen< matrixlen:
                spiralarry[spirallen] = matrix[i][startx]
                spirallen += 1
                i -= 1

            startx += 1

        return spiralarry



