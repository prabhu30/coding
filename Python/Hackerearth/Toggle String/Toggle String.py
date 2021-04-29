a=input()
for i in range(len(a)):
    if(a[i].isupper()):
        print(a[i].lower(),end="")
    else:
        print(a[i].upper(),end="")
