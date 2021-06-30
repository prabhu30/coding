def solve(score,is_birthday):
    # write your code from here
    if is_birthday:
        score += 5
        if score <= 60:
            print(0)
        elif score>=60 and score<=80:
            print(1)
        else:
            print(2)
    else:
        if score<=60:
            print(0)
        elif score>=60 and score<=80:
            print(1)
        else:
            print(2)
