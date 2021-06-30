def solve(string):
    # write your code from here
    if string.startswith("f") and string.endswith("b"):
        print("FizzBuzz")
    elif string.startswith("f"):
        print("Fizz")
    elif string.endswith("b"):
        print("Buzz")
    else:
        print(string)
