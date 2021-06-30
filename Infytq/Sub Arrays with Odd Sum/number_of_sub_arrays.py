na = int(input())
a = list(map(int,input().split()))
l=[]
for i in range(0,len(a)+1):
    for j in range(i+1,len(a)+1):
        l.append(a[i:j])
c = 0
for i in l:
    sm = sum(i)
    #print(sm)
    if sm%2!=0:
        c += 1
print(c)
