a = list(map(str, input().split(",")))
for i in a:
    b,c = i.split(":")
    d = str(c)
    e = 0
    s1 = ""
    s2 = ""
    for i in d:
        e += int(i)*int(i)
    if e%2==0:
        s1 += b[-1]+b[:-1]
    else:
        s1 += b[2:]+b[:2]
    print(s1)
