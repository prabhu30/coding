def isPal(num):
	num = str(num)
	return num==num[::-1]

tc = int(input())

for cases in range(tc):
	
	num = int(input())
	num = num+1

	while(not isPal(num)):
		num = num+1

	print(num)
