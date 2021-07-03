word = input()
ans = ""
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        cs = word[i:j]
        if cs ==cs[::-1]:
            if len(cs) > len(ans):
                ans = cs
print(ans)
