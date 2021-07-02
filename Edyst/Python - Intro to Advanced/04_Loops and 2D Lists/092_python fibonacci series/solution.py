def solve(n):
    # write your code here
    fib=[]
    fib.extend([0,1])
    a = 0
    b = 1
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        fib.append(c)
    for i in range(n):
        print(fib[i], end=" ")
