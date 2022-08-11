import math
n, l, r = list(map(int, input().split()))

cur = n
log = 0
while cur > 1:
    cur //= 2
    log +=1

tot = 2**(log+1)-1

def rec(cur,e, i):


    if i+e -1 < l or i > r:
        return 0
    elif l <= i and i+e -1  <= r:
        return cur
        
    return rec(cur//2, e//2, i) + rec(cur%2, 1, i + e//2) + rec(cur//2, e//2, i+e//2+1)

print(rec(n, tot, 1))
