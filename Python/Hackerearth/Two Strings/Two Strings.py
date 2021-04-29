n=int(input())
for i in range(n):
    s=list(map(str,input().split()))
    l1=[]
    l2=[]
    l1[:0]=s[0]
    l2[:0]=s[1]
    l1.sort()
    l2.sort()
    flag=1
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            flag=0
    if(flag==1):
        print("YES")
    else:
        print("NO")
            
