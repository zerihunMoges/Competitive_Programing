test = int(input())
    
for i in range(test):
    amount = list(map(int, input().split()))[1]
    rams = list(map(int, input().split()))
    gains = list(map(int, input().split()))
    ramsandg = []
    for i in range(len(rams)):
        ramsandg.append([rams[i],gains[i]])
    ramsandg.sort()
    
    for i in range(len(ramsandg)):
        if ramsandg[i][0] <= amount:
            amount += ramsandg[i][1]
    print(amount)
