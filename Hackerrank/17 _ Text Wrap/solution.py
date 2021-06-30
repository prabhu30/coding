

def wrap(string, max_width):
    j = 0
    s = ""
    for i in range(0,len(string)):
        s += string[j:j+max_width]+"\n"
        j += max_width
    return s

