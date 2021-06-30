def count_substring(string, sub_string):
    c = 0
    ls = len(sub_string)
    fs = string.find(sub_string)
    for i in range(0,len(string)):
        if string[i]==sub_string[0]:
            if string[i:i+ls]==sub_string:
                c += 1
    return c

