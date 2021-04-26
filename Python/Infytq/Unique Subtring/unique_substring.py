word = input()
ans = ""
for i in range(0,len(word)):
    if len(word)-i < 3:
        break
    for j in range(i+3, len(word)+1):
        curr_substr = word[i:j]
        if len(curr_substr)==len(set(curr_substr)) and (len(curr_substr) > len(ans)):
            ans = curr_substr

if ans == "":
    print(-1)
else:
    print(ans)
