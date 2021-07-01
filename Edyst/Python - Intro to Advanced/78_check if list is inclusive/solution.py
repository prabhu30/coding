def solve(A):
    # write your code here
    if len(A) < 6:
        return "False"
    elif (A[0]+A[-1])/2 in A[1:-1]:
        return "True"
    else:
        return "False"
