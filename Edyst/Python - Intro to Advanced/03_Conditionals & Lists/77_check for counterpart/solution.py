def solve(A,k):
    # write your code here
    if k-A[0] in A[1:]:
        print("Exists")
    else:
        print("Doesn't Exist")
