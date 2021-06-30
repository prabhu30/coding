n = int(input())
for i in range(n):
    day, boo = map(str, input().split())
    day = int(day)
    if boo == "true":
        if day == 1 or day == 7:
            print("9:00")
        else:
            print("7:00")
    else:
        if day==1 or day==7:
            print("6:00")
        else:
            print("5:00")



