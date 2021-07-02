def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def solve(n):
    # write your code here
    pc = 0
    i = 2
    while True:
        if isPrime(i):
            pc += 1
        if pc==n:
            print(i)
            break
        i += 1
