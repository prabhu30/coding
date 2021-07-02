def solve(n):
    # write your code here
    upper = 2*n - 1
    k = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i+j<=n+1:
                print(k, end="")
                k += 1
                if k > 9:
                    k = 1
        print()
