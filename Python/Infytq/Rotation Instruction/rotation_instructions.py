l = list(map(str,input().split(":")))
s = l[0]
ls = len(s)
left = int(l[1]) % ls
right = int(l[2]) % ls
mult = int(l[3])
ri = ls-left
aftright = s[ri:]+s[:ri]
aftleft = aftright[right:]+aftright[:right]
s1 = ""
for i in range(0,len(aftleft)):
    if i%mult==0:
        pass
    else:
        s1 += aftleft[i]
print(s1)
