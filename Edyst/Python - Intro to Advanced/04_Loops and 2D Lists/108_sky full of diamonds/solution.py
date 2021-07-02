def solve(n):
    # write your code here
    lines = 2*n+1
    dots = n
    star = 1
    for i in range(1,n+1):
        print("."*dots + "*"*star + "."*dots)
        star += 2
        dots -= 1
    
    print("*"*lines)
    star -= 2
    dots += 1
    
    for j in range(n,0,-1):
        print("."*dots + "*"*star + "."*dots)
        star -= 2
        dots += 1
