def solve(num1,num2,special_mode):
    # write your code from here
    if not special_mode:
        print(num1+num2)
    else:
        if num1==num2:
            if num1==6 and num2==6:
                print((num1+num2+1)-6)
            else:
                print(num1+num2+1)
        else:
            print(num1+num2)
