def solve(num1,num2):
    # write your code from here
    if num1 > 21 or num2 > 21:
        print("Rematch")
    elif num1 == num2:
        print("Rematch")
    else:
        p1 = abs(num1-21)
        p2 = abs(num2-21)
        if p1<p2:
            print("Player1")
        else:
            print("Player2")
