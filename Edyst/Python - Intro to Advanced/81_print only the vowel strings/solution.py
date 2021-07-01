def solve(A):
    # write your code here
    vowels = ['a','e','i','o','u']
    for i in A:
        if i[0] in vowels:
            print(i, end=" ")
