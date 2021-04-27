# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = map(int, input().split())
s2 = ".|."
s1 = "-"
c = b-3
d = 1
for i in range(1,(a+1)//2):
    print(s1*int(c/2)+s2*d+s1*int(c/2))
    if i== ((a+1)//2)-1:
        break
    c = c - ((b/a)*2)
    d += 2
e = (b-7)//2
print("-"*e+"WELCOME"+"-"*e)
for i in range((a//2)+1,a):
    print(s1*int(c/2)+s2*d+s1*int(c/2))
    c = c + ((b/a)*2)
    d -= 2

