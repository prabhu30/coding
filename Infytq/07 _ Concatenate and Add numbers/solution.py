l = list(map(int,input().split(",")))
a = l.index(5)
b = l.index(8)
s = ""
for i in range(a,b+1):
    s += str(l[i])
print(sum(l[:a])+sum(l[b+1:])+int(s))
