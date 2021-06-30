if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

b=sorted(list(arr),reverse=True)

max=b[0]
for i in b:
    if i<max:
        print(i)
        break
