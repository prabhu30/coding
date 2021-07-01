def solve(A):
    # write your code here
    for i in range(len(A)):
        if A[i]>0:
            A[i] = 0-A[i]
        else:
            A[i] = 0+abs(A[i])
    return A
