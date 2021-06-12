l = []
for _ in range(int(input())):
  l.append(input())
nw = int(input())
for i in range(nw):
  flag = 0
  w = input()
  if w in l:
    flag = 1
  else:
    for j in l:
      if w.startswith(j):
        nexthalf = j.index(j[-1]) + 1
        if w[nexthalf:] in l:
          flag = 1
  if flag==1:
    print("Yes")
  else:
    print("No")
