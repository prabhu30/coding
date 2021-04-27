n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    print()       
for i in range(1,n-2):
    for j in range(k-i,-1,-1):
        print(" ",end=" ")
    for l in range(i*2+1):
        print("*",end=" ")
    print()
    
