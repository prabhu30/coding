def solve(num):
    # write your code from here
    if num%13==0 or (num-1)%13==0:
        print("Crazy")
    else:
        print("Not Crazy")
