a=[]
b=[]
s=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        b=[]
        b.append(name)
        b.append(score)
        a.append(b)

a.sort()
for p in range(len(a)):
    s.append(a[p][1])
t=sorted(s)

min=t[0]

for i in t:
    if i>min:
        sec_min=i
        break

for i in range(len(a)):
    if a[i][1]==sec_min:
        print(a[i][0])
