def solve(n):
    # write your code here
    num = 1
    res = 1
    while res<=n:
        res = 2**num
        num += 1
    print(res//2)
