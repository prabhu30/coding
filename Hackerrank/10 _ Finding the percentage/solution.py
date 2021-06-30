if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    count=0
    s=0
    for i in student_marks[query_name]:
        s=s+i
        count+=1
    print("%.2f"%(s/count))
