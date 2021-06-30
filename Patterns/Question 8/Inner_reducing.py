n=int(input())
for i in range(n):
    x=n
    y=n-i+1
    for j in range(n*2-1):
        if(i<=j and (i+j<=(n*2-2))):
            print(n-i,end="")
        elif(j<=(n-1)):
            print(x,end="")
            x-=1
        else:
            print(y,end="")
            y+=1
    print()
for i in range(n-2,-1,-1):
    x=n
    y=n-i+1
    for j in range(n*2-1):
        if(i<=j and (i+j<=(n*2-2))):
            print(n-i,end="")
        elif(j<=(n-1)):
            print(x,end="")
            x-=1
        else:
            print(y,end="")
            y+=1
    print()
        
