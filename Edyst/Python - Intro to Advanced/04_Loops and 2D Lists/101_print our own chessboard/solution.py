def solve(n,character):
    # write your code from here
    if character == 'W':
        other = 'B'
    else:
        other = 'W'
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0:
                print(character, end="")
            else:
                print(other, end="")
        print()
