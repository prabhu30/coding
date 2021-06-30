def multipleSum(x):
    sum3 = 0
    sum5 = 0
    sum15 = 0
    for i in range(3,x+1,3):
        sum3 += i
    for i in range(5,x+1,5):
        sum5 += i
    for i in range(15,x+1,15):
        sum15 += i
    return sum3+sum5-sum15

x = int(input())
print(multipleSum(x))
