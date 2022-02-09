arguments = input().split()
arguments = list(map(int,arguments))
def count(arguments, c):
    print(c)
    if arguments[0] == 0 or arguments[0] == 1:
        arguments[1]-=1
        arguments[2]-=1
        if arguments[0] ==1:
            if arguments[1]<=0 and arguments[2] >=0:
                c += 1

        return c
    
        
    else:
        arguments
        return str(count(arguments[0]//2,arguments[1],arguments[2],c))+ str(count(arguments[0]%2,arguments[1],arguments[2],c))+ str(count(arguments[0]//2,arguments[1],arguments[2],c))
        
        
print(count(arguments, 0))