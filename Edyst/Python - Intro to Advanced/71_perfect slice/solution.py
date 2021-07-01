def solve(Andy_list):
    # write your code here
    length = len(Andy_list)
    half = length//2
    if length%2==0:
        return Andy_list[:half]
    else:
        return Andy_list[-half:]
