a = input()
s = ""
l = []
for i in a:
    if i.isalpha():
        s += i
s = s[::-1]
j = 0
s1 = ""
for i in range(len(a)):
    if a[i].isalpha()!=True:
        s1 += a[i]
    else:
        s1 += s[j]
        j += 1
print(s1)
