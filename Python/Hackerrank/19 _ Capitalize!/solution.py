# Complete the solve function below.
def solve(s):
    a_string = s.split(' ')
    return ' '.join((word.capitalize() for word in a_string))
