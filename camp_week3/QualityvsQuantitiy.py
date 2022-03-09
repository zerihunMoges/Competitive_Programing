test = int(input())

for k in range(test):
    amount = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    tot = [nums[0]]
    for i in range(1,len(nums)):
        tot.append(tot[i-1]+nums[i])
  
    for i in range(1, len(tot)//2+1):
        if tot[i] < tot[-1] - tot[-1*i-1]:
            print("Yes")
            break
        elif i == len(tot)//2:
            print("No")
