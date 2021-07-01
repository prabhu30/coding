def solve(acting_power,rating):
    # write your code from here
    if acting_power<2 or rating<2:
        print("No")
    elif acting_power>8 or rating>8:
        print("Yes")
    else:
        print("Maybe")
