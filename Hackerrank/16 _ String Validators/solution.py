if __name__ == '__main__':
    s = raw_input()
    l=[0]*5
    for i in s:
        if i.isalnum():
            l[0]=1
        if i.isalpha():
            l[1]=1
            if i.isupper():
                l[4]=1
            elif i.islower():
                l[3]=1
        elif i.isdigit():
            l[2]=1
        else:
            pass
    for i in l:
        if i==1:
            print(True)
        else:
            print(False)
