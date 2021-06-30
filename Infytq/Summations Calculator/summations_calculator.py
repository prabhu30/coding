line = input().split()

lb = int(line[0])
ub = int(line[1])
opr = line[2]
opn = int(line[3])

ops = ["+","-","*","/","%"]

if opr in ops:
    res = ops.index(opr)
    
    sm = 0
    if res == 0:
        for i in range(lb,ub+1):
            sm = sm + (i + opn)
            
    if res == 1:
        for i in range(lb,ub+1):
            sm = sm + (i - opn)
            
    if res == 2:
        for i in range(lb,ub+1):
            sm = sm + (i * opn)
            
    if res == 3:
        for i in range(lb,ub+1):
            sm = sm + (i // opn)
            
    if res == 4:
        for i in range(lb,ub+1):
            sm = sm + (i % opn)
    
print(sm)
