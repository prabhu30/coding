def solve(n):
    # write your code here
    seq = []
    seq.extend([0,1,1])
    a = 0
    b = 1
    c = 1
    for i in range(n):
        term = a+b+c
        seq.append(term)
        a = b
        b = c
        c = term
    print(seq[n-1])
