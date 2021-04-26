def solve(list1):
    # complete the method solve 
    areas = {}

    for i in list1:
        l = i[0]
        b = i[1]
        area = l*b
        
        if area in areas:
            areas[area] += 1
        else:
            areas[area] = 1
            
    for i in sorted(areas.keys()):
        print(str(i)+": "+str(areas[i]))
    print()
    
solve([(1, 4), (2, 3), (2, 2), (10, 2), (4, 5)])
