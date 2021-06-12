n = input()
s = [i for i in n]
l = []
for i in range(len(n)):
  for j in range(i+1,len(n)):
    x = n[i:j+1]
    if x[::-1] in n:
      l.append(x)
for i in l:
  for j in i:
    if j in s:
      s.remove(j)
print(*s, sep="")
