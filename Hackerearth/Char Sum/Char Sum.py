s=input()
sum=0
for i in range(len(s)):
    sum=sum+(ord(s[i])-96)
print(sum)
