n=int(input())
for i in range(n):
    for j in range(n*2):
        if(j<=i or (i+j)>=(n*2-1)):
            print("*",end="")
        else:
            print("#",end="")
    print()
