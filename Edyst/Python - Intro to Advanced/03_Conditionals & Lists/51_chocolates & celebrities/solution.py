def solve(chocolates,is_weekend):
    # write your code from here
    if chocolates>=20 and chocolates<=40:
        print("true")
    elif chocolates>40 and is_weekend==True:
        print("true")
    else:
        print("false")
