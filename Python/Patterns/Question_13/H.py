n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        print("H",end="")
    print()
for i in range(n+1):
    for j in range(n//2):
        print(" ",end="")
    for k in range(n):
        print("H",end="")
    for l in range(n*3):
        print(" ",end="")
    for m in range(n):
        print("H",end="")
    print()
for i in range(n//2+1):
    for j in range(n//2):
        print(" ",end="")
    for k in range(n*5):
        print("H",end="")
    print()
for i in range(n+1):
    for j in range(n//2):
        print(" ",end="")
    for k in range(n):
        print("H",end="")
    for l in range(n*3):
        print(" ",end="")
    for m in range(n):
        print("H",end="")
    print()
x=l+n
for i in range(n-1,-1,-1):
    for j in range(x,-1,-1):
        print(" ",end="")
    for k in range(i*2+1):
        print("H",end="")
    x+=1
    print()
