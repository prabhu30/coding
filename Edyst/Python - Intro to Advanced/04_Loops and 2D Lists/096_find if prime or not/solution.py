def solve(n):
    # write your code here
    if n < 0 or n == 1:
        print("Not Prime")
    else:
        i = 2
        flag = 1
        while i<n:
            if n%i==0:
                flag = 0
            i += 1
        if flag==1:
            print("Prime")
        else:
            print("Not Prime")
