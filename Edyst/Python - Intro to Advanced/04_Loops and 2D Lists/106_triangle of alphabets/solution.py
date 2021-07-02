tc = int(input())

for i in range(tc):
    n = int(input())
    for k in range(n):
        for l in range(n):
            if k>=l:
                print(chr(65+k), end="")
        print()
