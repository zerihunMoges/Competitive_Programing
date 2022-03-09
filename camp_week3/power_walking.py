test = int(input())

for i in range(test):
    amount = int(input())
    powerups = list(map(int, input().split()))
    upows = set()
    
    for i in powerups:
        upows.add(i)
    
    lpows = len(upows)
    answer = []
    for i in range(1,amount+1):
        if i < amount:
            print(lpows,end=" ") if lpows >= i else print(i, end=" ")
        elif i == amount:
            print(lpows, end="\n") if lpows >= i else print(i, end="\n")
