def solve(n):
    # write your code here
    lines = 2*n + 1   #7
    oneline = lines-2   #7
    for i in range(1,n+1):   #1,8
        print("*"*i + "."*oneline + "*"*i)
        oneline -= 2
    
    print("*"*lines)
    oneline = 1
    
    for j in range(n,0,-1):
        print("*"*j + "."*oneline + "*"*j)
        oneline += 2
