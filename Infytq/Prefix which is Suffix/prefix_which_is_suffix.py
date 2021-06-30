s = input()
half = len(s)//2
new = ""
for i in range(half+1):
    a = s[:i]
    if s.endswith(a):
        new = a
    else:
        pass
print(len(new))
