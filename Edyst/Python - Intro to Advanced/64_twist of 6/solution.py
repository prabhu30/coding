def solve(num1,num2):
    # write your code from here
    if num1==num2:
        print(0)
    elif num1%6 == num2%6:
        if num1 < num2:
            print(num1)
        else:
            print(num2)
    else:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
