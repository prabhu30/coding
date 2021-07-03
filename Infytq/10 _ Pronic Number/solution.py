word = input()
found = False
for i in range(0,9):
    if (str(i) in word and str(i+1) in word and str((i*(i+1))) in word):
        print(i*(i+1), end = " ")
        found = True

if not found:
    print(-1)
