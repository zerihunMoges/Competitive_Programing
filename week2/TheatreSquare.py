#By zerihun, contest: Codeforces Beta Round #1, problem: (A) Theatre Square, Accepted, #, 

def minFlagStones(size):
    size = list(map(int, size))
    side1 = size[0]//size[2] if size[0]/size[2] == int(size[0]/size[2]) else int(size[0]/size[2])+1
    side2 = size[1]//size[2] if size[1]/size[2] == int(size[1]/size[2]) else int(size[1]/size[2])+1
    print(side1*side2)
  
size = input().split()
minFlagStones(size)
