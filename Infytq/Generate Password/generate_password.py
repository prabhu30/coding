word = input().split(",")

for emp in word:
	emp_details = emp.split(":")
	emp_name = emp_details[0]
	emp_num = emp_details[1]

	if str(len(emp_name)) in emp_num:
		index = len(emp_name)-1
		print(emp_name[index], end = '')

	else:
		num = -1
		length = len(emp_name)
		for i in emp_num:
			digit = int(i)
			if digit > num and digit < length:
				num = digit
		if num==-1 or num==0:
			print('X', end='')
		else:
			index = num - 1
			print(emp_name[index], end = '')
