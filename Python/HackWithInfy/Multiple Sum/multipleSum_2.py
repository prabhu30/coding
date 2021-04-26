def multipleSum(x):

    n = x//3
    sum3 = (n * (2*3 + (n-1)*3)) / 2

    n = x//5
    sum5 = (n * (2*5 + (n-1)*5)) / 2

    n = x//15
    sum15 = (n * (2*15 + (n-1)*15)) / 2

    return int(sum3+sum5-sum15)

x = int(input())
print(multipleSum(x))
