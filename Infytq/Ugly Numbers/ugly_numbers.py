tc = int(input())

for cases in range(tc):

    n = int(input())
    
    if n < 1:
        print("not ugly")
        continue

    while(n%2==0):
        n = n//2

    while(n%3==0):
        n = n//3

    while(n%5==0):
        n = n//5

    if n > 1:
        print("not ugly")
    else:
        print("ugly")
