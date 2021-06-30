n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
for i in range(3):
    for j in range(k+1):
        if(j<3 or j>(k-3)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
