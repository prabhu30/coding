s=input()
zcount=0
ocount=0
for i in s:
    if(i=='z' or i=='o'):
        if(i=='z'):
            zcount+=1
        else:
            ocount+=1 
if(2*zcount==ocount):
    print("Yes")
else:
    print("No")
