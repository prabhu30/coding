n=int(input())
x=n//2+1
for j in range(n*2-1):
    print("*",end=" ")
print()
for i in range(x-1,1,-1):
    for k in range(x-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    for l in range(x-i):
        print(" ",end=" ")
    for o in range(x-i-1):
        print(" ",end=" ")
    for m in range(i*2-1):
        print("*",end=" ")
    print()
for i in range(n//2+1):
    for j in range(k+i+2):
        print(" ",end=" ")
    for m in range(n-i*2):
        print("*",end=" ")
    print()
            
