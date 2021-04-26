n=int(input())
x=n-1
for i in range(n):
    for k in range(x,0,-1):
        print(" ",end="")
    x-=1
    for l in range(n):
        if(i==0 or i==n-1 or l==0 or l==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
