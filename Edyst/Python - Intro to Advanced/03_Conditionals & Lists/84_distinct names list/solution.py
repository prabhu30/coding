def solve(student_list):
    # write your code here
    wd = []
    for i in student_list:
        if i in wd:
            pass
        else:
            wd.append(i)
    return wd
